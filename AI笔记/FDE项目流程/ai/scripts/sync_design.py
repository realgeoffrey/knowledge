#!/usr/bin/env python3
"""Sync design.md tokens and revision into the offline design and business pages.

Run from any directory. --check reports drift without writing anything.
Only JSON-compatible YAML front matter is supported; no YAML dependency needed.
This checks token/revision consistency, not layout, accessibility or approval.
"""

import argparse
import json
import math
import os
from pathlib import Path
import re
import sys
import tempfile


GROUPS = ("colors", "typography", "rounded", "spacing", "components")
PAGE_FILES = ("ai/prototypes/design-system.html", "ai/prototypes/pages/index.html")
FORMAT_VERSION = "alpha"
START = "/* DESIGN_TOKENS_START */"
END = "/* DESIGN_TOKENS_END */"
REVISION_LINE = re.compile(r"^规范版本：([A-Za-z0-9][A-Za-z0-9._-]*)[ \t]*$", re.MULTILINE)
VERSION_LABEL = re.compile(
    r"(<[a-zA-Z][^>]*\bdata-design-version(?:=\"[^\"]*\")?[^>]*>)"
    r"([A-Za-z0-9][A-Za-z0-9._-]*)"
    r"(</[a-zA-Z][^>]*>)"
)
VERSION_SLOT = re.compile(r"<[a-zA-Z][^>]*\bdata-design-version\b[^>]*>")


def page_files(root):
    """Reject omitted HTML pages before checking or writing any registered page."""
    folder = root / "ai/prototypes"
    if folder.is_symlink():
        raise ValueError("原型目录不支持符号链接")
    discovered = set()
    walk_errors = []
    for directory, children, files in os.walk(folder, followlinks=False, onerror=walk_errors.append):
        for name in (*children, *files):
            if (Path(directory) / name).is_symlink():
                raise ValueError(f"原型资源不支持符号链接：{name}")
        for name in files:
            if Path(name).suffix.lower() == ".html":
                discovered.add((Path(directory) / name).relative_to(root).as_posix())
    if walk_errors:
        raise walk_errors[0]
    missing = sorted(discovered - set(PAGE_FILES))
    if missing:
        raise ValueError("原型 HTML 未登记到 PAGE_FILES：" + "、".join(missing))
    return PAGE_FILES


def css_name(path):
    return "--" + "-".join(
        re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", part).lower() for part in path
    )


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"重复的设计数据键：{key}")
        result[key] = value
    return result


def render_tokens(document):
    front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", document, re.DOTALL)
    if not front:
        raise ValueError("design.md 缺少顶部 JSON 兼容 YAML 数据块")
    tokens = json.loads(front[1], object_pairs_hook=unique_object)
    if not isinstance(tokens, dict) or not isinstance(tokens.get("name"), str):
        raise ValueError("设计数据必须是对象，且包含 name")
    unknown = sorted(set(tokens) - {"name", "version", *GROUPS})
    if unknown:
        raise ValueError("未支持的设计数据键：" + "、".join(unknown))
    if tokens.get("version") != FORMAT_VERSION:
        raise ValueError(f"顶部 version 只表示 design.md 格式代，必须为 {FORMAT_VERSION}；规范版本写在正文单独一行")
    revisions = REVISION_LINE.findall(document)
    if len(revisions) != 1:
        raise ValueError("正文必须恰好有一行：规范版本：D1.0（或新版本）")
    revision = revisions[0]
    values = {}

    def collect(value, path):
        if isinstance(value, dict):
            if not value:
                raise ValueError(f"设计分组不能为空：{'.'.join(path)}")
            for key, child in value.items():
                if not isinstance(key, str) or not re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_-]*", key):
                    raise ValueError(f"无效 token 名：{key}")
                collect(child, (*path, key))
            return
        if isinstance(value, bool) or not isinstance(value, (str, int, float)):
            raise ValueError(f"token 必须是非空 CSS 值：{'.'.join(path)}")
        if isinstance(value, (int, float)) and not math.isfinite(value):
            raise ValueError(f"token 必须是有限数值：{'.'.join(path)}")
        text = str(value)
        reference = re.fullmatch(r"\{([a-zA-Z0-9_.-]+)\}", text)
        if not reference and (not text.strip() or re.search(r"[;{}<>\r\n]", text)):
            raise ValueError(f"无效 CSS 值：{'.'.join(path)}")
        if css_name(path) in {css_name(existing) for existing in values}:
            raise ValueError(f"token 生成重名 CSS 变量：{'.'.join(path)}")
        values[path] = text

    for group in GROUPS:
        if group in tokens:
            if not isinstance(tokens[group], dict):
                raise ValueError(f"{group} 必须是对象")
            collect(tokens[group], (group,))
    if not values:
        raise ValueError("未找到可同步的设计 token")
    declarations = []
    for path, value in values.items():
        reference = re.fullmatch(r"\{([a-zA-Z0-9_.-]+)\}", value)
        if reference:
            target = tuple(reference[1].split("."))
            visited = {path}
            while target in values:
                if target in visited:
                    raise ValueError(f"循环 token 引用：{'.'.join(path)}")
                visited.add(target)
                next_reference = re.fullmatch(r"\{([a-zA-Z0-9_.-]+)\}", values[target])
                if not next_reference:
                    break
                target = tuple(next_reference[1].split("."))
            else:
                raise ValueError(f"token 引用不存在：{reference[1]}")
            value = f"var({css_name(tuple(reference[1].split('.')))})"
        declarations.append(f"  {css_name(path)}: {value};")
    return revision, ":root {\n" + "\n".join(declarations) + "\n}"


def sync_page(document, page):
    revision, css = render_tokens(document)
    if page.count(START) != 1 or page.count(END) != 1:
        raise ValueError("展示页必须恰有一组 DESIGN_TOKENS_START / END")
    pattern = re.escape(START) + r".*?" + re.escape(END)
    updated, count = re.subn(pattern, lambda _: START + "\n" + css + "\n" + END, page, flags=re.DOTALL)
    if count != 1:
        raise ValueError("展示页 token 标记顺序错误")
    slots = len(VERSION_SLOT.findall(updated))
    updated, labels = VERSION_LABEL.subn(lambda match: match[1] + revision + match[3], updated)
    updated, metadata = re.subn(
        r'(<meta name="design-version" content=")[^"]*(">)',
        lambda match: match[1] + revision + match[2], updated,
    )
    if slots < 1 or slots != labels or metadata != 1:
        raise ValueError("每个 data-design-version 的文本必须恰好是规范版本，且 meta name=\"design-version\" 只能有一个")
    return updated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="只读检查 tokens 与版本是否同步")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    try:
        document = (root / "ai/specs/design.md").read_text(encoding="utf-8")
        pages = []
        for name in page_files(root):
            page_path = root / name
            current = page_path.read_text(encoding="utf-8")
            pages.append((page_path, current, sync_page(document, current)))
        drift = [path.relative_to(root).as_posix() for path, current, updated in pages if updated != current]
        if args.check and drift:
            print(f"设计值或版本未同步（{', '.join(drift)}）：请运行 python3 ai/scripts/sync_design.py", file=sys.stderr)
            return 1
        if not args.check:
            for page_path, current, updated in pages:
                if updated != current:
                    # shortcut: per-file replacement; add rollback if cross-file atomicity is required.
                    with tempfile.TemporaryDirectory(prefix=".design-sync-", dir=page_path.parent) as directory:
                        candidate = Path(directory) / page_path.name
                        candidate.write_text(updated, encoding="utf-8")
                        candidate.replace(page_path)
        print("设计 tokens 与版本检查通过" if args.check else "设计 tokens 与版本已同步")
        print("仅覆盖设计值与版本；正文、布局、交互和客户批准仍需复核。")
        return 0
    except (OSError, ValueError) as error:
        print(f"设计同步未完成，请核对页面并重试：{error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
