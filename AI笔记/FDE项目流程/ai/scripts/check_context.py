#!/usr/bin/env python3
"""Check entry files, Markdown references, current IDs, and design token sync.

Run from any directory: python3 /path/to/project/ai/scripts/check_context.py
Use --check-file <project-relative.md> for each moved or split history file.
Links to source files and the human input file are checked for existence only.
Fragments are checked only in current or explicitly selected Markdown files.
Verified AC rows require implementation information and BL/RUN anchors in Markdown read this run.
These structural checks never prove business approval or test results.
No remote requests or project commands are run.
"""

from pathlib import Path
import argparse
import html
import importlib.util
import os
import re
from urllib.parse import unquote, urlsplit


HUMAN_INPUT = Path("待定&待确认.md")
REQUIRED = (
    "README.md", "AGENTS.md", HUMAN_INPUT, "项目状态.md", "ai/specs/project.md",
    "ai/specs/requirements.md", "ai/specs/solution.md",
    "ai/records/traceability.md", "ai/records/acceptance.md", "ai/specs/design.md",
    "ai/prototypes/design-system.html", "ai/prototypes/pages/index.html", "ai/scripts/sync_design.py",
)
# Older projects may still have original files in ai/materials during migration.
SOURCE_DIRS = {Path("sources"), Path("ai/materials")}
EXCLUDED = {Path("ai/evidence"), Path("ai/archive"), Path("ai/lessons/archive")}
# shortcut: single-line inline links only; use a Markdown parser if nested labels,
# escaped destinations, reference links or multiline links become project needs.
LINK = re.compile(
    r'!?\[[^\]\n]*\]\([ \t]*(?:<([^>\n]*)>|([^()\s]+))'
    r'''(?:[ \t]+(?:"[^"\n]*"|'[^'\n]*'|\([^()\n]*\)))?[ \t]*\)'''
)
EXPLICIT_ANCHOR = re.compile(r'<a\b[^>]*\b(?:id|name)=["\']([^"\']+)["\']', re.I)


def markdown_body(text):
    """Mask code blocks and normalize table indentation, preserving line numbers."""
    visible = []
    fence = ""
    previous_boundary = True
    indented_code = False
    in_list = False
    for line in text.splitlines(keepends=True):
        marker = re.match(r" {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence:
            if (marker and marker[1][0] == fence[0]
                    and len(marker[1]) >= len(fence) and not marker[2].strip()):
                fence = ""
        elif marker:
            fence = marker[1]
        else:
            blank = not line.strip()
            indented = line.startswith(("    ", "\t"))
            # shortcut: recognize standalone indented code, not nested list/quote
            # code blocks; use a Markdown parser if those need exact handling.
            if re.match(r" {0,3}(?:[-+*]|\d+[.)])[ \t]+", line):
                in_list = True
            elif not blank and not line[0].isspace():
                in_list = False
            indented_code = (not in_list and indented
                             and (previous_boundary or indented_code))
            previous_boundary = blank or bool(re.match(r" {0,3}#{1,6}(?:[ \t]|$)", line))
            if not indented_code:
                visible.append(re.sub(r"^ {1,3}(?=\|)", "", line))
                continue
        visible.append("\n" if line.endswith("\n") else "")
    body = "".join(visible)
    parts = []
    cursor = 0
    for match in re.finditer(r"<!--.*?(?:-->|\Z)", mask_inline_code(body), re.DOTALL):
        parts.extend((body[cursor:match.start()], re.sub(r"[^\n]", " ", body[match.start():match.end()])))
        cursor = match.end()
    return "".join(parts) + body[cursor:]


def mask_inline_code(text):
    return re.sub(
        r"(?<!`)(`+)(?!`)((?:(?!\n[ \t]*\n).)*?)(?<!`)\1(?!`)",
        lambda match: re.sub(r"[^\n]", " ", match[0]),
        text, flags=re.DOTALL,
    )


def links(text):
    text = mask_inline_code(markdown_body(text))
    for number, line in enumerate(text.splitlines(), 1):
        for match in LINK.finditer(line):
            yield number, match[1] if match[1] is not None else match[2]


def anchors(text):
    body = markdown_body(text)
    result = set(EXPLICIT_ANCHOR.findall(mask_inline_code(body)))
    # shortcut: ATX headings and explicit anchors; use explicit IDs for other renderers.
    for title in re.findall(r"^ {0,3}#{1,6}[ \t]+(.+?)\s*$", body, re.MULTILINE):
        title = re.sub(r"\s+#+$", "", title)
        title = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", title)
        title = html.unescape(re.sub(r"<[^>]*>", "", title)).lower()
        slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        if slug in result:
            suffix = 1
            while f"{slug}-{suffix}" in result:
                suffix += 1
            slug = f"{slug}-{suffix}"
        result.add(slug)
    return result


def protected_input(path, root):
    """Identify human-owned inputs, including case aliases on macOS."""
    normalized = Path(os.path.normpath(path).casefold())
    try:
        relative = normalized.relative_to(Path(str(root).casefold()))
    except ValueError:
        return None
    if relative == HUMAN_INPUT:
        return "人工输入"
    if relative in SOURCE_DIRS or not SOURCE_DIRS.isdisjoint(relative.parents):
        return "原件"
    return None


def verified_anchor(source, cell, prefix, known, root):
    """Return an error phrase, or "" when the cell links a read Markdown anchor."""
    unread = []
    for _, target in links(cell):
        try:
            url = urlsplit(target)
        except ValueError:
            continue
        if url.scheme or url.netloc:
            continue
        fragment = unquote(url.fragment)
        if not re.fullmatch(prefix + r"-\d+", fragment, re.I):
            continue
        local = unquote(url.path)
        if any(char in local for char in "<>{}") or local in {"待填写", "待确认", "路径", "..."}:
            continue
        link_path = source.parent / local if local else source
        try:
            destination = link_path.resolve()
            if destination.suffix.lower() != ".md":
                continue
            relative = destination.relative_to(root)
        except (OSError, RuntimeError, ValueError):
            continue
        if protected_input(link_path, root) or protected_input(destination, root):
            continue
        if destination in known and fragment in known[destination]:
            return ""
        if destination not in known and destination.is_file():
            unread.append(relative.as_posix())
    if unread:
        return prefix + " 锚点未读 " + "、".join(dict.fromkeys(unread)) + "，需 --check-file"
    return prefix + " 固定锚点链接"


def record_errors(documents, root):
    errors = []
    definitions = {}
    known = {path: anchors(text) for path, text in documents.items()}
    for path, text in documents.items():
        relative = path.relative_to(root)
        if not EXCLUDED.isdisjoint(relative.parents):
            continue
        source = relative.as_posix()
        explicit = set()
        requirement = source == "ai/specs/requirements.md" or source.startswith("ai/specs/requirements/")
        for number, line in enumerate(mask_inline_code(markdown_body(text)).splitlines(), 1):
            for anchor in EXPLICIT_ANCHOR.findall(line):
                if anchor in explicit:
                    errors.append(f"{source}:{number}: 重复锚点 {anchor}")
                explicit.add(anchor)
            match = re.match(r"^ {0,3}#{1,6}\s+((?:REQ|TASK|CR|BL|RUN|UAT|BUG|FB|TEST|LESSON)-\d+)", line)
            if requirement and not match:
                match = re.match(r"^\|\s*(AC-\d+-\d+)\s*\|", line)
            if source == "ai/records/acceptance.md" and not match:
                match = re.match(r"^\|\s*(?:G[12]\s*/\s*)?((?:BL|FB|BUG)-\d+)", line)
                if not match:
                    match = re.match(r"^-\s+(UAT-\d+)", line)
            if match:
                identifier = match[1]
                location = f"{source}:{number}"
                if identifier in definitions:
                    errors.append(f"{location}: 重复定义 {identifier}，原定义在 {definitions[identifier]}")
                else:
                    definitions[identifier] = location
        if source != "ai/records/traceability.md":
            continue
        columns = {}
        for number, line in enumerate(markdown_body(text).splitlines(), 1):
            if not line.startswith("|"):
                columns = {}
                continue
            cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
            if "实现状态" in cells:
                columns = {"status": cells.index("实现状态")}
                for index, cell in enumerate(cells):
                    if "BL" in cell or "基线" in cell:
                        columns["baseline"] = index
                    elif "实现" in cell and "版本" in cell:
                        columns["implementation"] = index
                    elif cell in {"RUN", "执行证据"}:
                        columns["run"] = index
                continue
            if not columns:
                continue
            cells.extend([""] * (max(columns.values()) + 1 - len(cells)))
            if not cells[columns["status"]].startswith("已验证"):
                continue
            missing = []
            for key, prefix in (("baseline", "BL"), ("run", "RUN")):
                cell = cells[columns[key]] if key in columns else ""
                problem = verified_anchor(path, cell, prefix, known, root)
                if problem:
                    missing.append(problem)
            implementation = cells[columns["implementation"]] if "implementation" in columns else ""
            if implementation in {"", "<待填写>", "待填写", "待确认", "未实现", "未开始", "未验证", "—"}:
                missing.append("实现与版本信息")
            if missing:
                errors.append(f"{source}:{number}: 已验证 AC 缺少 {'、'.join(missing)}")
    return errors


def design_errors(root, documents):
    script = root / "ai/scripts/sync_design.py"
    try:
        document = documents.get(root / "ai/specs/design.md")
        if document is None:
            raise ValueError("ai/specs/design.md: 设计规范必须是可读取的项目文件")
        if script.resolve() != script:
            raise ValueError("ai/scripts/sync_design.py: 不读取符号链接及其内部文件")
        spec = importlib.util.spec_from_file_location("fde_sync_design", script)
        if spec is None or spec.loader is None:
            raise ImportError(f"无法加载 {script.name}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        errors = []
        for name in module.page_files(root):
            page = (root / name).read_text(encoding="utf-8")
            if module.sync_page(document, page) != page:
                errors.append(f"{name}: 设计值或版本未同步：请运行 python3 ai/scripts/sync_design.py")
    except (OSError, RuntimeError, ValueError, ImportError, SyntaxError, AttributeError) as error:
        return [f"设计同步检查失败：{error}"]
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-file", action="append", default=[], metavar="项目相对路径.md",
        help="额外检查指定 Markdown（含归档），可重复；不递归读取其他历史文件",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    errors = []
    paths = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"{name}: 必需入口缺失或不是文件")
    sources = root / "sources"
    if sources.is_symlink() or not sources.is_dir():
        errors.append("sources/: 必须是项目内的目录")
    for name in ("README.md", "AGENTS.md", "项目状态.md"):
        if (root / name).is_file() and not (root / name).is_symlink():
            paths.append(root / name)
    for name in ("ai",):
        start = root / name
        if not start.exists() or start.is_symlink():
            continue
        for directory, children, files in os.walk(
            start, followlinks=False,
            onerror=lambda error: errors.append(f"{error.filename}: 无法读取目录: {error}"),
        ):
            folder = Path(directory)
            children[:] = sorted(
                child for child in children
                if (folder / child).relative_to(root) not in EXCLUDED
                and not protected_input(folder / child, root)
                and not (folder / child).is_symlink()
            )
            paths.extend(
                folder / file for file in sorted(files)
                if file.lower().endswith(".md") and not (folder / file).is_symlink()
            )
    for name in args.check_file:
        try:
            relative = Path(name)
            if relative.is_absolute():
                raise ValueError("请使用项目根目录相对路径")
            path = root / relative
            resolved = path.resolve()
            resolved.relative_to(root)
            protected = protected_input(path, root) or protected_input(resolved, root)
            if protected:
                raise ValueError(f"{protected}只检查路径是否存在，不读取正文")
            cursor = root
            for part in relative.parts:
                cursor = cursor / part
                if cursor.is_symlink():
                    raise ValueError("不读取符号链接及其内部文件")
            if not resolved.is_file() or resolved.suffix.lower() != ".md":
                raise ValueError("必须是已存在的 Markdown 文件")
            paths.append(resolved)
        except (OSError, RuntimeError, ValueError) as error:
            errors.append(f"{name}: 指定检查文件无效: {error}")
    paths = list(dict.fromkeys(paths))
    checked = 0
    read = 0
    documents = {}
    for path in paths:
        source = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{source}: 无法读取: {error}")
            continue
        read += 1
        documents[path.resolve()] = text
    fragment_targets = {path: anchors(text) for path, text in documents.items()}
    for path, text in documents.items():
        source = path.relative_to(root).as_posix()
        for number, target in links(text):
            if not target or target.startswith("//"):
                continue
            try:
                url = urlsplit(target)
                if url.scheme or url.netloc:
                    continue
                local = unquote(url.path)
                if (any(char in local for char in "<>{}")
                        or local in {"待填写", "待确认", "路径", "..."}):
                    continue
                link_path = path.parent / local if local else path
                destination = link_path.resolve()
                checked += 1
                if not destination.exists():
                    errors.append(f"{source}:{number}: 链接目标不存在: {target}")
                elif (url.fragment and destination in fragment_targets
                      and not protected_input(link_path, root)
                      and not protected_input(destination, root)
                      and unquote(url.fragment) not in fragment_targets[destination]):
                    errors.append(f"{source}:{number}: Markdown 锚点不存在: {target}")
            except (OSError, RuntimeError, ValueError) as error:
                errors.append(f"{source}:{number}: 无法检查目标 {target}: {error}")
    errors.extend(record_errors(documents, root))
    errors.extend(design_errors(root, documents))
    print("仅检查必需入口、简单本地链接及已读 Markdown 锚点、现行编号定义、已验证 AC 必需引用，以及页面登记与设计同步。")
    print("不证明批准真实性、测试结果、实现版本正确性或阶段通过；不检查 HTML 动态路由、布局和手写样式。")
    print("人工输入文件和来源目录的原件只检查路径是否存在。默认跳过 ai/evidence、ai/archive、ai/lessons/archive；--check-file 额外读取指定项目 Markdown，排除人工输入文件、来源目录和符号链接。")
    print("只检查已读项目 Markdown 的锚点；已验证行指向未读历史 Markdown 时要求 --check-file。不检查任意裸 ID、远程链接、代码与占位符；指定文件路径均相对于项目根目录。")
    print("不支持嵌套、转义、参考式或多行链接及复杂列表/引用代码块；不是完整 Markdown 解析器。")
    for error in errors:
        print(error)
    print(f"结构检查{'失败' if errors else '通过'}：已读 {read} 个 Markdown，检查 {checked} 个本地目标，发现 {len(errors)} 个问题。")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
