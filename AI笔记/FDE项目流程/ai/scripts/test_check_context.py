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
        self.cwd = Path(self.temp.name) / "unrelated"
        self.cwd.mkdir()
        self.required = (
            "README.md", "AGENTS.md", "待澄清问题.md", "项目状态.md", "ai/specs/project.md",
            "ai/specs/requirements.md", "ai/records/clarifications.md", "ai/specs/solution.md",
            "ai/records/traceability.md", "ai/records/acceptance.md", "ai/specs/design.md",
            "ai/prototypes/design-system.html", "ai/prototypes/pages/index.html", "ai/scripts/sync_design.py",
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
        self.write("ai/specs/design.md", (
            "---\n"
            '{"name": "Fixture", "version": "alpha", "colors": {"primary": "#1d4ed8"}}\n'
            "---\n# Fixture\n\n规范版本：D1.0\n"
        ))
        self.write("ai/prototypes/design-system.html", (
            "<!doctype html><html><head>"
            '<meta name="design-version" content="D1.0">'
            "<style>\n/* DESIGN_TOKENS_START */\n"
            ":root {\n  --colors-primary: #1d4ed8;\n}\n"
            "/* DESIGN_TOKENS_END */\n</style></head><body>"
            "<span data-design-version>D1.0</span></body></html>"
        ))

        self.write("ai/prototypes/pages/index.html", (self.root / "ai/prototypes/design-system.html").read_text(encoding="utf-8"))

    def test_business_page_design_drift_is_detected(self):
        page = (self.root / "ai/prototypes/design-system.html").read_text(encoding="utf-8")
        self.write("ai/prototypes/pages/index.html", page.replace("#1d4ed8", "#ffffff"))
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
        self.write("README.md", "[规格](ai/specs/requirements.md)\n")
        self.write("ai/handbook/nested/guide.md", "[入口](../../../README.md)\n")
        self.write("ai/prototypes/README.md", "[页面](pages/index.html)\n")
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
        for name in ("项目状态.md", "待澄清问题.md", "ai/records/notes.md"):
            with self.subTest(name=name):
                self.write(name, "# Note\n\n[丢失](missing.md)\n")
                result = self.run_check()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(name + ":3", result.stdout)
                self.assertIn("missing.md", result.stdout)
                self.write(name, "# Fixture\n")

    def test_design_spec_links_are_checked(self):
        self.write("ai/specs/design.md", "# 默认规范\n\n[样例](../../ai/prototypes/missing-design.html)\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("ai/specs/design.md:3", result.stdout)
        self.assertIn("ai/prototypes/missing-design.html", result.stdout)

    def test_chinese_space_paths_encoding_titles_and_fragments(self):
        self.write("ai/文件 a.md", "# 存在\n")
        self.write("README.md", (
            '[中文](<ai/文件 a.md>)\n'
            '[编码](ai/%E6%96%87%E4%BB%B6%20a.md#存在)\n'
            '[标题](ai/specs/requirements.md "可选标题")\n'
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

    def test_human_notes_are_not_read_or_selected(self):
        self.write("human/笔记.md", "[缺失](missing.md)\n\n# REQ-999\n")
        self.write("human/以后/新笔记.md", "[缺失](future-missing.md)\n\n# REQ-1000\n")
        self.write("human/以后/附件.txt", "REQ-1001\n")
        self.write("项目状态.md", "[人读笔记](human/笔记.md)\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("missing.md", result.stdout)
        self.assertNotIn("future-missing.md", result.stdout)
        self.assertNotIn("REQ-999", result.stdout)
        self.assertNotIn("REQ-1000", result.stdout)
        for name in ("human/笔记.md", "ai/../human/笔记.md", "human/以后/新笔记.md", "human/以后/附件.txt"):
            with self.subTest(name=name):
                result = self.run_check("--check-file", name)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("人读笔记不读取、不纳入检查", result.stdout)
                self.assertNotIn("missing.md", result.stdout)
                self.assertNotIn("future-missing.md", result.stdout)
                self.assertNotIn("REQ-1001", result.stdout)

    def test_excluded_history_is_not_read_but_links_to_it_are_checked(self):
        for directory in (
            "ai/materials", "ai/evidence", "ai/archive", "ai/lessons/archive",
        ):
            self.write(directory + "/bad.md", "[缺失](missing.md)\n")
            (self.root / directory / "raw.md").write_bytes(b"\xff")
        self.write("README.md", "[原件](ai/materials/raw.md)\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.write("README.md", "[原件](ai/materials/absent.md)\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("ai/materials/absent.md", result.stdout)

    def test_selected_archive_detects_and_fixes_moved_evidence_link(self):
        self.write("ai/evidence/report.txt", "actual fixture report\n")
        record = "# RUN-001\n\n[报告](../evidence/report.txt)\n"
        self.write("ai/records/traceability.md", record)
        self.assertEqual(self.run_check().returncode, 0)
        archive = "ai/archive/采购首期/RUN-001.md"
        self.write(archive, record)
        self.write("ai/records/traceability.md", (
            '<a id="run-001"></a>\n\n[RUN-001](../archive/采购首期/RUN-001.md)\n'
        ))
        # Daily checks still skip history; an archive operation must select it.
        self.assertEqual(self.run_check().returncode, 0)
        result = self.run_check("--check-file", archive)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(archive + ":3", result.stdout)
        self.assertIn("evidence/report.txt", result.stdout)
        self.write(archive, record.replace("../evidence/", "../../evidence/"))
        result = self.run_check("--check-file", archive)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_selected_archive_does_not_load_unrelated_history(self):
        archive = "ai/archive/采购首期/RUN-001.md"
        self.write(archive, "[规格](../../specs/requirements.md)\n")
        self.write("ai/archive/采购首期/unrelated.md", "").write_bytes(b"\xff")
        result = self.run_check("--check-file", archive)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_multiple_selected_files_are_all_checked(self):
        paths = ("ai/archive/first.md", "ai/archive/second.md")
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
        page = self.root / "ai/prototypes/design-system.html"
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
        for link in ("#missing", "ai/specs/requirements.md#missing"):
            with self.subTest(link=link):
                self.write("README.md", f"# Fixture\n\n[定位]({link})\n")
                result = self.run_check()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("README.md:3", result.stdout)
                self.assertIn("锚点不存在", result.stdout)

    def test_explicit_chinese_duplicate_and_code_headings_resolve(self):
        self.write("ai/specs/requirements.md", (
            '# 中文 `字段`\n\n<a id="stable-id"></a>\n\n'
            '## 重复\n\n## 重复\n\n```md\n# fake\n```\n'
        ))
        self.write("README.md", (
            '[标题](ai/specs/requirements.md#中文-字段)\n'
            '[固定](ai/specs/requirements.md#stable-id)\n'
            '[重复](ai/specs/requirements.md#重复-1)\n'
            '[动态路由](ai/prototypes/pages/index.html#orders)\n'
        ))
        self.assertEqual(self.run_check().returncode, 0)
        self.write("README.md", '[代码不是标题](ai/specs/requirements.md#fake)\n')
        self.assertEqual(self.run_check().returncode, 1)

    def test_only_current_definitions_must_have_unique_ids(self):
        self.write("ai/specs/requirements.md", '# 需求\n\n## REQ-001 创建\n')
        self.write("ai/specs/requirements/orders.md", '# 模块\n\n## REQ-001 导出\n')
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("重复定义 REQ-001", result.stdout)
        self.write("ai/specs/requirements/orders.md", (
            '# 模块\n\n引用 REQ-001\n\n```md\n## REQ-001 示例\n```\n'
        ))
        self.write("ai/archive/old.md", '# 历史\n\n## REQ-001 旧版\n')
        self.assertEqual(self.run_check("--check-file", "ai/archive/old.md").returncode, 0)

    def test_duplicate_ac_definitions_are_detected_in_specs(self):
        self.write("ai/specs/requirements.md", (
            '# 需求\n\n| AC | Given | When | Then |\n| --- | --- | --- | --- |\n'
            '| AC-001-01 | 已登录 | 提交 | 保存 |\n'
            '| AC-001-01 | 已登录 | 删除 | 移除 |\n'
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("重复定义 AC-001-01", result.stdout)

    def test_verified_ac_requires_pinned_baseline_run_and_implementation(self):
        self.write("ai/records/acceptance.md", '<a id="bl-001"></a>\n# 基线\n')
        header = ('# 追踪\n\n| REQ / AC | 来源 / BL / CR | 实现 / 接口与版本 | RUN | 实现状态 |\n'
                  '| --- | --- | --- | --- | --- |\n')
        valid = ['[BL-001](acceptance.md#bl-001)', 'src/order.py @ ' + 'a' * 40,
                 '[RUN-001](#run-001)', '已验证']
        evidence = '\n<a id="run-001"></a>\n\n### RUN-001\n\n实际执行证据。\n'
        for column, bad in ((0, 'BL-999'), (1, '<待填写>'), (2, 'RUN-999')):
            with self.subTest(column=column):
                values = valid.copy()
                values[column] = bad
                self.write('ai/records/traceability.md', header + '| AC-001-01 | ' + ' | '.join(values) + ' |\n' + evidence)
                result = self.run_check()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn('已验证', result.stdout)
        self.write('ai/records/traceability.md', header + '| AC-001-01 | ' + ' | '.join(valid) + ' |\n' + evidence)
        self.assertEqual(self.run_check().returncode, 0)
        self.write('ai/records/traceability.md', header + '| AC-001-01 | 草稿 | 未实现 | 未运行 | 未开始 |\n')
        self.assertEqual(self.run_check().returncode, 0)

    def test_verified_anchor_must_resolve_in_markdown_read_this_run(self):
        self.write("ai/records/acceptance.md", '<a id="bl-001"></a>\n# 基线\n')
        self.write("ai/records/note.txt", "not markdown\n")
        header = (
            '# 追踪\n\n| REQ / AC | 风险 | 来源 / BL / CR | PAGE | TASK | 实现 / 接口与版本 | TEST / 验证入口 | RUN | 实现状态 | UAT结果 / 证据 |\n'
            '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n'
        )
        evidence = '\n<a id="run-001"></a>\n\n### RUN-001\n\n实际执行证据。\n'
        impl = 'src/order.py @ ' + 'a' * 40

        def row(baseline):
            return f'| AC-001-01 | 普通 | {baseline} | 无 | 无 | {impl} | 人工 | [RUN-001](#run-001) | 已验证 | 通过 |\n'

        self.write('ai/records/traceability.md', header + row('[BL-001](acceptance.md#bl-001)') + evidence)
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for baseline in (
            '[BL-001](待填写#bl-001)',
            '[BL-001](<待填写#bl-001>)',
            '[BL-001](ai/<文件>.md#bl-001)',
            '[BL-001](路径#bl-001)',
            '[BL-001](ai/{name}.md#bl-001)',
            '[BL-001](../prototypes/pages/index.html#bl-001)',
            '[BL-001](note.txt#bl-001)',
        ):
            with self.subTest(baseline=baseline):
                self.write('ai/records/traceability.md', header + row(baseline) + evidence)
                result = self.run_check()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn('固定锚点链接', result.stdout)
                self.assertNotIn('需 --check-file', result.stdout)
        self.write('ai/archive/old.md', '').write_bytes(b'\xff')
        self.write('ai/records/traceability.md', header + row('[BL-001](../archive/old.md#bl-001)') + evidence)
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('ai/archive/old.md', result.stdout)
        self.assertIn('--check-file', result.stdout)
        self.assertNotIn('无法读取', result.stdout)
        self.write('ai/archive/old.md', '<a id="bl-001"></a>\n')
        result = self.run_check('--check-file', 'ai/archive/old.md')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unread_history_fragments_are_not_loaded_implicitly(self):
        self.write('ai/archive/old.md', '').write_bytes(b'\xff')
        self.write('README.md', '[历史](ai/archive/old.md#old)\n')
        self.assertEqual(self.run_check().returncode, 0)

    def test_verified_wording_checks_prefix_and_whole_cell_placeholders(self):
        self.write("ai/records/acceptance.md", '<a id="bl-001"></a>\n# 基线\n')
        header = (
            '# 追踪\n\n| REQ / AC | 来源 / BL / CR | 实现 / 接口与版本 | RUN | 实现状态 |\n'
            '| --- | --- | --- | --- | --- |\n'
        )
        evidence = '\n<a id="run-001"></a>\n\n### RUN-001\n\n实际执行证据。\n'
        links = '[BL-001](acceptance.md#bl-001) | {impl} | [RUN-001](#run-001)'

        def write_row(impl, status):
            self.write(
                'ai/records/traceability.md',
                header + '| AC-001-01 | ' + links.format(impl=impl) + ' | ' + status + ' |\n' + evidence,
            )

        write_row('v1.2.0（旧导入未验证，不在本 AC）；兼容 <2.0', '已验证')
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for impl in ('无', 'TBD'):
            with self.subTest(impl=impl):
                write_row(impl, '已验证')
                result = self.run_check()
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for impl in ('', '待确认', '待填写', '<待填写>', '未实现', '未开始', '未验证', '—'):
            with self.subTest(impl=impl):
                write_row(impl, '已验证，抽样')
                result = self.run_check()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn('实现与版本信息', result.stdout)
        write_row('待确认', '已实现未验证')
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_id_glued_to_chinese_is_a_definition(self):
        self.write("ai/specs/requirements.md", '# 需求\n\n## REQ-001创建\n')
        self.write("ai/specs/requirements/orders.md", '# 模块\n\n## REQ-001导出\n')
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("重复定义 REQ-001", result.stdout)

    def test_duplicate_heading_suffix_skips_taken_slug(self):
        self.write("ai/specs/requirements.md", '# 需求\n\n## 重复\n\n## 重复-1\n\n## 重复\n')
        self.write("README.md", (
            '[甲](ai/specs/requirements.md#重复)\n'
            '[乙](ai/specs/requirements.md#重复-1)\n'
            '[丙](ai/specs/requirements.md#重复-2)\n'
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unregistered_business_page_is_detected(self):
        self.write('ai/prototypes/pages/new.html', '<html>未登记页面</html>')
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('未登记', result.stdout)

    def test_table_indentation_preserves_checks_but_skips_code(self):
        cases = (
            ('ai/records/traceability.md',
             '| AC | 来源 / BL | 实现与版本 | RUN | 实现状态 |\n| --- | --- | --- | --- | --- |\n',
             '| AC-001-01 | 草稿 | 未实现 | 未运行 | 未开始 |\n',
             '| AC-001-01 | 无 | 未实现 | 未运行 | 已验证 |\n', '已验证'),
            ('ai/specs/requirements.md',
             '| AC | Given | When | Then |\n| --- | --- | --- | --- |\n',
             '| AC-001-01 | 已登录 | 提交 | 保存 |\n',
             '| AC-001-01 | 已登录 | 提交 | 保存 |\n| AC-001-01 | 已登录 | 删除 | 移除 |\n',
             '重复定义 AC-001-01'),
            ('ai/records/acceptance.md',
             '| 门槛 / BL | 结果 |\n| --- | --- |\n',
             '| G1 / BL-001 | 已确认 |\n',
             '| G1 / BL-001 | 已确认 |\n| G2 / BL-001 | 已确认 |\n', '重复定义 BL-001'),
        )
        for path, header, valid, invalid, message in cases:
            for spaces in range(5):
                for rows, bad in ((valid, False), (invalid, True)):
                    with self.subTest(path=path, spaces=spaces, invalid=bad):
                        self.write(path, '# Fixture\n\n' + ''.join(
                            ' ' * spaces + line for line in (header + rows).splitlines(keepends=True)
                        ))
                        result = self.run_check()
                        expected = 1 if bad and spaces < 4 else 0
                        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                        if expected:
                            self.assertIn(message, result.stdout)
            self.write(path, '# Fixture\n')

    def test_verified_row_with_missing_cells_is_rejected(self):
        self.write('ai/records/traceability.md', (
            '# 追踪\n\n| AC | 实现状态 | 来源 / BL | 实现与版本 | RUN |\n'
            '| --- | --- | --- | --- | --- |\n| AC-001-01 | 已验证 |\n'
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('已验证', result.stdout)

    def test_escaped_pipe_does_not_hide_verified_status(self):
        self.write('ai/records/traceability.md', (
            '# 追踪\n\n| AC | 说明 | 来源 / BL | 实现与版本 | RUN | 实现状态 |\n'
            '| --- | --- | --- | --- | --- | --- |\n'
            '| AC-001-01 | A \\| B | 无 | v1 | 未运行 | 已验证 |\n'
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('已验证', result.stdout)

    def test_malformed_verified_link_reports_failure_without_traceback(self):
        self.write('ai/records/traceability.md', (
            '# 追踪\n\n| AC | 来源 / BL | 实现与版本 | RUN | 实现状态 |\n'
            '| --- | --- | --- | --- | --- |\n'
            '| AC-001-01 | [BL](http://[x#bl-999) | v1 | 未运行 | 已验证 |\n'
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('已验证', result.stdout)
        self.assertNotIn('Traceback', result.stderr)

    def test_solution_ac_mapping_is_not_a_requirement_definition(self):
        self.write('ai/specs/requirements.md', '# 需求\n\n| AC | Given | When | Then |\n| --- | --- | --- | --- |\n| AC-001-01 | 已登录 | 提交 | 保存 |\n')
        self.write('ai/specs/solution.md', '# 方案\n\n| 关联验收条件 | 实现 |\n| --- | --- |\n| AC-001-01 | OrderService |\n')
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_duplicate_baseline_registration_is_rejected(self):
        self.write('ai/records/acceptance.md', (
            '# 验收\n\n| 门槛 / BL | 结果 |\n| --- | --- |\n'
            '| G1 / BL-001 | 已确认 |\n| G2 / BL-001 | 已确认 |\n'
        ))
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('重复定义 BL-001', result.stdout)

    def test_duplicate_explicit_anchor_is_rejected(self):
        self.write('ai/records/acceptance.md', '# 验收\n\n<a id="bl-001"></a>\n\n<a id="bl-001"></a>\n')
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('重复锚点 bl-001', result.stdout)

    def test_comments_are_not_definitions_links_or_anchors(self):
        self.write('ai/specs/requirements.md', '# 需求\n\n## REQ-001 正文\n')
        self.write('ai/handbook/example.md', (
            '# 示例\n\n<!--\n## REQ-001 隐藏样例\n<a id="secret"></a>\n'
            '[隐藏链接](missing.md)\n-->\n'
        ))
        self.assertEqual(self.run_check().returncode, 0)
        self.write('README.md', '[隐藏不是锚点](ai/handbook/example.md#secret)\n')
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('锚点不存在', result.stdout)

    def test_moved_requirement_keeps_old_anchor_without_duplicate_definition(self):
        self.write('ai/specs/requirements.md', (
            '# 需求\n\n<a id="req-001"></a>\n<a id="req-001-创建"></a>\n'
            '## 已迁移：REQ-001 创建\n\n[REQ-001](requirements/orders.md#req-001)\n'
        ))
        self.write('ai/specs/requirements/orders.md', '<a id="req-001"></a>\n\n## REQ-001 创建\n')
        self.write('README.md', '[原标题](ai/specs/requirements.md#req-001-创建)\n')
        self.assertEqual(self.run_check().returncode, 0)


if __name__ == "__main__":
    unittest.main()
