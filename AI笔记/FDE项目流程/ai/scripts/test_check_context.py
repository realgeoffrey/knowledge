"""Run with python3 ai/scripts/test_check_context.py; fixtures never edit project docs."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class CheckContextCLI(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        (self.root / "sources").mkdir(parents=True)
        self.cwd = Path(self.temp.name) / "unrelated"
        self.cwd.mkdir()
        self.required = (
            "README.md", "AGENTS.md", "待定&待确认.md", "ai/README.md", "spec/README.md",
            "prototypes/README.md", "prototypes/design.md", "prototypes/design-system.html",
            "prototypes/interactive/index.html", "ai/scripts/sync_design.py",
        )
        for name in self.required:
            self.write(name, "# Fixture\n")
        self.script = self.root / "ai/scripts/check_context.py"
        self.script.parent.mkdir(exist_ok=True)
        source = Path(__file__).with_name("check_context.py")
        sync = Path(__file__).with_name("sync_design.py")
        if source.exists():
            shutil.copyfile(source, self.script)
        if sync.exists():
            shutil.copyfile(sync, self.root / "ai/scripts/sync_design.py")
        self.write("prototypes/design.md", (
            "---\n"
            '{"name": "Fixture", "version": "alpha", "colors": {"primary": "#1d4ed8"}}\n'
            "---\n# Fixture\n\n规范版本：D1.0\n"
        ))
        self.write("prototypes/design-system.html", (
            "<!doctype html><html><head>"
            '<meta name="design-version" content="D1.0">'
            "<style>\n/* DESIGN_TOKENS_START */\n"
            ":root {\n  --colors-primary: #1d4ed8;\n}\n"
            "/* DESIGN_TOKENS_END */\n</style></head><body>"
            "<span data-design-version>D1.0</span></body></html>"
        ))

        self.write("prototypes/interactive/index.html", (self.root / "prototypes/design-system.html").read_text(encoding="utf-8"))

    def test_business_page_design_drift_is_detected(self):
        page = (self.root / "prototypes/design-system.html").read_text(encoding="utf-8")
        self.write("prototypes/interactive/index.html", page.replace("#1d4ed8", "#ffffff"))
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("index.html", result.stdout + result.stderr)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def run_check(self, *args):
        return subprocess.run(
            [sys.executable, str(self.script), *args], cwd=self.cwd,
            capture_output=True, text=True, encoding="utf-8", timeout=10,
        )

    def test_relative_links_work_from_unrelated_cwd(self):
        self.write("README.md", "[规格](spec/README.md)\n")
        self.write("ai/notes/nested/guide.md", "[入口](../../../README.md)\n")
        self.write("prototypes/README.md", "[页面](interactive/index.html)\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("仅检查", result.stdout)

    def test_each_required_entry_is_checked(self):
        for name in self.required:
            with self.subTest(name=name):
                path = self.root / name
                path.unlink()
                result = self.run_check()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(name, result.stdout)
                self.write(name, "# Fixture\n")

    def test_broken_link_reports_source_line_and_target(self):
        for name in ("README.md", "spec/notes.md", "ai/notes.md"):
            with self.subTest(name=name):
                self.write(name, "# Note\n\n[丢失](missing.md)\n")
                result = self.run_check()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(name + ":3", result.stdout)
                self.assertIn("missing.md", result.stdout)
                self.write(name, "# Fixture\n")

    def test_design_spec_links_are_checked(self):
        self.write("prototypes/design.md", "# 默认规范\n\n[样例](../../prototypes/missing-design.html)\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("prototypes/design.md:3", result.stdout)
        self.assertIn("prototypes/missing-design.html", result.stdout)

    def test_chinese_space_paths_encoding_titles_and_fragments(self):
        self.write("ai/文件 a.md", "# 存在\n")
        self.write("README.md", (
            '[中文](<ai/文件 a.md>)\n'
            '[编码](ai/%E6%96%87%E4%BB%B6%20a.md#存在)\n'
            '[标题](spec/README.md "可选标题")\n'
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_code_remote_placeholders_and_anchors_are_ignored(self):
        self.write("README.md", (
            "```markdown\n[示例](missing-fenced.md)\n```\n"
            "~~~\n[示例](missing-tilde.md)\n~~~\n"
            "`[示例](missing-inline.md)`\n"
            "``带 ` 的 [示例](missing-double.md)``\n"
            "[不是链接]`分隔的代码`(missing-separated.md)\n"
            "[网站](https://example.invalid/missing) [协议](//example.invalid/x)\n"
            "[邮件](mailto:nobody@example.invalid)\n"
            "[占位](<待填写>) [占位](ai/<文件>.md) [占位](ai/{name}.md)\n"
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_inline_code_cannot_close_inside_a_longer_backtick_run(self):
        self.write("README.md", "`This code includes `` [example](missing-example.md)`\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unmatched_backticks_cannot_hide_links_across_paragraphs(self):
        self.write("README.md", (
            "A literal unmatched backtick: `\n\n"
            "[real link](missing-real.md)\n\nAnother literal backtick: `\n"
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("README.md:3", result.stdout)
        self.assertIn("missing-real.md", result.stdout)

    def test_standalone_indented_code_is_not_a_link(self):
        for indentation in ("    ", "\t"):
            with self.subTest(indentation=indentation):
                self.write("README.md", (
                    "# Instructions\n\n" + indentation
                    + "[example](missing-example.md)\n"
                ))
                result = self.run_check()
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_indented_code_after_heading_is_not_a_link(self):
        self.write("README.md", "# Heading\n    [example](missing-example.md)\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_indented_paragraph_continuation_links_are_still_checked(self):
        self.write("README.md", (
            "A normal paragraph\n    [real](missing-continuation.md)\n"
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("README.md:2", result.stdout)
        self.assertIn("missing-continuation.md", result.stdout)

    def test_indented_list_links_are_still_checked(self):
        for content in (
            "- Parent\n    - [real](missing-list.md)\n",
            "- Parent\n\n    [real](missing-list.md)\n",
        ):
            with self.subTest(content=content):
                self.write("README.md", content)
                result = self.run_check()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("missing-list.md", result.stdout)

    def test_human_input_is_only_checked_for_existence(self):
        filename = "待定&待确认.md"
        inbox = self.write(filename, "[待补链接](missing.md)\n\n# REQ-999\n")
        self.write("README.md", f"[人工输入]({filename}#待补章节)\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for name in (filename, f"ai/../{filename}", "待定&待确认.MD"):
            with self.subTest(name=name):
                result = self.run_check("--check-file", name)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("人工输入只检查路径是否存在", result.stdout)
                self.assertNotIn("missing.md", result.stdout)
        inbox.unlink()
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(f"{filename}: 必需入口缺失或不是文件", result.stdout)
        self.assertIn(f"链接目标不存在: {filename}#待补章节", result.stdout)


    def test_source_files_are_only_checked_for_existence(self):
        self.write("sources/客户/原件.md", "[客户内部链接](missing.md)\n")
        self.write("README.md", "[原件](sources/客户/原件.md#客户章节)\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for name in (
            "sources/客户/原件.md", "ai/../sources/客户/原件.md", "SOURCES/客户/原件.md",
        ):
            with self.subTest(name=name):
                result = self.run_check("--check-file", name)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("原件只检查路径是否存在", result.stdout)
                self.assertNotIn("missing.md", result.stdout)
        self.write("README.md", "[原件](sources/客户/缺失.md)\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("链接目标不存在: sources/客户/缺失.md", result.stdout)

    def test_sources_must_be_a_directory_in_the_project(self):
        sources = self.root / "sources"
        sources.rmdir()
        self.write("sources", "not a directory\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("sources/: 必须是项目内的目录", result.stdout)
        sources.unlink()
        sources.symlink_to(self.cwd, target_is_directory=True)
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("sources/: 必须是项目内的目录", result.stdout)

    def test_source_link_does_not_check_fragment_of_symlink_target(self):
        alias = self.root / "sources/accepted.md"
        alias.symlink_to(self.root / "ai/README.md")
        targets = ["sources/accepted.md"]
        case_root = self.root.resolve().with_name("PROJECT")
        if case_root.is_dir() and case_root.anchor == "/":
            targets.append((case_root / "sources/accepted.md").as_posix())
        for target in targets:
            with self.subTest(target=target):
                self.write("README.md", f"[原件](<{target}#未核对的章节>)\n")
                result = self.run_check()
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


    def test_design_check_rejects_inputs_linked_to_human_files(self):
        for name, protected in (
            ("prototypes/design.md", "待定&待确认.md"),
            ("ai/scripts/sync_design.py", "sources/sync.py"),
        ):
            with self.subTest(name=name):
                path = self.root / name
                original = path.read_text(encoding="utf-8")
                target = self.write(protected, original)
                path.unlink()
                path.symlink_to(target)
                result = self.run_check()
                path.unlink()
                self.write(name, original)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("设计同步检查失败", result.stdout)
                self.assertIn(name, result.stdout)


    def test_multiple_selected_files_are_all_checked(self):
        paths = ("spec/extra/first.md", "spec/extra/second.md")
        for path in paths:
            self.write(path, "[报告](missing.txt)\n")
        result = self.run_check("--check-file", paths[0], "--check-file", paths[1])
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for path in paths:
            self.assertIn(path + ":1", result.stdout)

    def test_selected_current_file_is_not_checked_twice(self):
        self.write("README.md", "[报告](missing.txt)\n")
        result = self.run_check("--check-file", "README.md", "--check-file", "README.md")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(result.stdout.count("README.md:1:"), 1)

    def test_selected_file_must_be_a_project_markdown_without_symlinks(self):
        outside = self.cwd / "outside.md"
        outside.write_bytes(b"\xff")
        self.write("ai/log.txt", "not Markdown\n")
        (self.root / "ai/linked.md").symlink_to(outside)
        (self.root / "ai/linked-dir").symlink_to(self.cwd, target_is_directory=True)
        (self.root / "ai/internal-link.md").symlink_to(self.root / "README.md")
        (self.root / "internal-dir").symlink_to(self.root / "ai", target_is_directory=True)
        for path in (
            "../unrelated/outside.md", str(outside), "ai/missing.md",
            "ai/log.txt", "ai", "ai/linked.md", "ai/linked-dir/outside.md",
            "ai/internal-link.md", "internal-dir/specs/requirements.md",
        ):
            with self.subTest(path=path):
                result = self.run_check("--check-file", path)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("指定检查文件无效", result.stdout)
                self.assertNotIn("无法读取", result.stdout)

    def test_unreadable_markdown_is_a_failure(self):
        self.write("ai/notes.md", "").write_bytes(b"\xff")
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("ai/notes.md", result.stdout)
        self.assertIn("无法读取", result.stdout)

    def test_design_token_drift_fails_even_when_links_exist(self):
        page = self.root / "prototypes/design-system.html"
        page.write_text(page.read_text(encoding="utf-8").replace("#1d4ed8", "#000000"))
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("未同步", result.stdout + result.stderr)

    def test_symlink_directory_is_not_recursively_read(self):
        outside = self.cwd / "outside"
        outside.mkdir()
        (outside / "private.md").write_bytes(b"\xff")
        (self.root / "ai/external").symlink_to(outside, target_is_directory=True)
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_markdown_fragment_reports_source_and_anchor(self):
        for link in ("#missing", "spec/README.md#missing"):
            with self.subTest(link=link):
                self.write("README.md", f"# Fixture\n\n[定位]({link})\n")
                result = self.run_check()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("README.md:3", result.stdout)
                self.assertIn("锚点不存在", result.stdout)

    def test_explicit_chinese_duplicate_and_code_headings_resolve(self):
        self.write("spec/README.md", (
            '# 中文 `字段`\n\n<a id="stable-id"></a>\n\n'
            '## 重复\n\n## 重复\n\n```md\n# fake\n```\n'
        ))
        self.write("README.md", (
            '[标题](spec/README.md#中文-字段)\n'
            '[固定](spec/README.md#stable-id)\n'
            '[重复](spec/README.md#重复-1)\n'
            '[动态路由](prototypes/interactive/index.html#orders)\n'
        ))
        self.assertEqual(self.run_check().returncode, 0)
        self.write("README.md", '[代码不是标题](spec/README.md#fake)\n')
        self.assertEqual(self.run_check().returncode, 1)

    def test_spec_definitions_must_have_unique_ids(self):
        self.write("spec/README.md", '# 需求\n\n## REQ-001 创建\n')
        self.write("spec/02-modules/orders.md", '# 模块\n\n## REQ-001 导出\n')
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("重复定义 REQ-001", result.stdout)
        self.write("spec/02-modules/orders.md", (
            '# 模块\n\n引用 REQ-001\n\n```md\n## REQ-001 示例\n```\n'
        ))
        self.write("ai/notes/example.md", '# 示例\n\n`REQ-001`\n')
        self.assertEqual(self.run_check("--check-file", "ai/notes/example.md").returncode, 0)

    def test_duplicate_ac_definitions_are_detected_in_specs(self):
        self.write("spec/README.md", (
            '# 需求\n\n| AC | Given | When | Then |\n| --- | --- | --- | --- |\n'
            '| AC-001-01 | 已登录 | 提交 | 保存 |\n'
            '| AC-001-01 | 已登录 | 删除 | 移除 |\n'
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("重复定义 AC-001-01", result.stdout)


    def test_id_glued_to_chinese_is_a_definition(self):
        self.write("spec/README.md", '# 需求\n\n## REQ-001创建\n')
        self.write("spec/02-modules/orders.md", '# 模块\n\n## REQ-001导出\n')
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("重复定义 REQ-001", result.stdout)

    def test_duplicate_heading_suffix_skips_taken_slug(self):
        self.write("spec/README.md", '# 需求\n\n## 重复\n\n## 重复-1\n\n## 重复\n')
        self.write("README.md", (
            '[甲](spec/README.md#重复)\n'
            '[乙](spec/README.md#重复-1)\n'
            '[丙](spec/README.md#重复-2)\n'
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unregistered_business_page_is_detected(self):
        self.write('prototypes/interactive/new.html', '<html>未登记页面</html>')
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('未登记', result.stdout)


    def test_solution_ac_mapping_is_not_a_requirement_definition(self):
        self.write('spec/README.md', '# 需求\n\n| AC | Given | When | Then |\n| --- | --- | --- | --- |\n| AC-001-01 | 已登录 | 提交 | 保存 |\n')
        self.write('ai/README.md', '# 方案\n\n| 关联验收条件 | 实现 |\n| --- | --- |\n| AC-001-01 | OrderService |\n')
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


    def test_duplicate_explicit_anchor_is_rejected(self):
        self.write('ai/README.md', '# 验收\n\n<a id="duplicate-anchor"></a>\n\n<a id="duplicate-anchor"></a>\n')
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('重复锚点 duplicate-anchor', result.stdout)

    def test_comments_are_not_definitions_links_or_anchors(self):
        self.write('spec/README.md', '# 需求\n\n## REQ-001 正文\n')
        self.write('ai/notes/example.md', (
            '# 示例\n\n<!--\n## REQ-001 隐藏样例\n<a id="secret"></a>\n'
            '[隐藏链接](missing.md)\n-->\n'
        ))
        self.assertEqual(self.run_check().returncode, 0)
        self.write('README.md', '[隐藏不是锚点](ai/notes/example.md#secret)\n')
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('锚点不存在', result.stdout)


    def test_spec_and_prototype_markdown_are_discovered(self):
        for name in ("spec/03-states/order.md", "prototypes/guide.md", "ai/notes/nested.md"):
            with self.subTest(name=name):
                self.write(name, "[坏链接](missing.md)\n")
                result = self.run_check()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(name, result.stdout)
                self.write(name, "# 正常\n")

    def test_acceptance_definitions_are_checked_across_spec_directories(self):
        row = "| AC-001-01 | 已登录 | 提交 | 保存 |\n"
        self.write("spec/06-acceptance/scenarios.md", row)
        self.write("spec/02-modules/orders.md", row)
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("重复定义 AC-001-01", result.stdout)

    def test_table_indentation_preserves_id_check_but_skips_code(self):
        for spaces in range(5):
            self.write("spec/06-acceptance/scenarios.md", "# 场景\n\n" + (" " * spaces + "| AC-001-01 | 条件 | 操作 | 结果 |\n") * 2)
            result = self.run_check()
            self.assertEqual(result.returncode, 1 if spaces < 4 else 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
