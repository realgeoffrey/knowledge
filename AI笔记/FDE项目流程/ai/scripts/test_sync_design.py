"""Run with python3 -m unittest discover -s ai/scripts -p 'test_*.py'."""

import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest


class SyncDesignCLI(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        self.script = self.root / "ai/scripts/sync_design.py"
        self.script.parent.mkdir(parents=True)
        source = Path(__file__).with_name("sync_design.py")
        if source.exists():
            shutil.copyfile(source, self.script)
        self.page = self.root / "ai/prototypes/design-system.html"
        self.page.parent.mkdir()
        self.page.write_text(
            '<!doctype html><html lang="zh-CN"><head>'
            '<meta name="design-version" content="old">'
            '<style id="design-tokens">\n/* DESIGN_TOKENS_START */\n'
            '/* DESIGN_TOKENS_END */\n</style></head><body>'
            '<span data-design-version>old</span>'
            '<strong data-design-version>old</strong><p>手工布局保留</p>'
            '</body></html>', encoding="utf-8",
        )
        (self.root / "ai/prototypes/pages").mkdir()
        (self.root / "ai/prototypes/pages/index.html").write_bytes(self.page.read_bytes())
        self.tokens = {
            "name": "Fixture", "version": "alpha",
            "colors": {"primary": "#1d4ed8"},
            "typography": {"body-md": {"fontSize": "14px", "lineHeight": 1.6}},
            "components": {"button-primary": {"backgroundColor": "{colors.primary}"}},
        }
        self.write_design()

    def write_design(self, revision="D1.0"):
        (self.root / "ai/specs").mkdir(parents=True, exist_ok=True)
        (self.root / "ai/specs/design.md").write_text(
            "---\n" + json.dumps(self.tokens, ensure_ascii=False, indent=2)
            + "\n---\n# 设计规范\n\n规范版本：" + revision + "\n",
            encoding="utf-8",
        )

    def run_sync(self, *args):
        return subprocess.run(
            [sys.executable, str(self.script), *args], cwd=self.temp.name,
            capture_output=True, text=True, encoding="utf-8", timeout=10,
        )

    def test_sync_updates_tokens_and_all_revision_labels_from_unrelated_cwd(self):
        result = self.run_sync()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        page = self.page.read_text(encoding="utf-8")
        self.assertIn("--colors-primary: #1d4ed8;", page)
        self.assertIn("--typography-body-md-font-size: 14px;", page)
        self.assertIn("var(--colors-primary)", page)
        self.assertIn('content="D1.0"', page)
        self.assertEqual(page.count(">D1.0<"), 2)
        self.assertIn("手工布局保留", page)
        self.assertEqual(self.run_sync("--check").returncode, 0)

    def test_check_reports_drift_without_writing_then_sync_repairs_it(self):
        initial = self.run_sync()
        self.assertEqual(initial.returncode, 0, initial.stderr)
        previous = self.page.read_bytes()
        self.tokens["colors"]["primary"] = "#1646b5"
        self.write_design("D1.1")
        result = self.run_sync("--check")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(self.page.read_bytes(), previous)
        self.assertEqual(self.run_sync().returncode, 0)
        self.assertIn("--colors-primary: #1646b5;", self.page.read_text())
        self.assertIn('content="D1.1"', self.page.read_text())
        self.assertEqual(self.run_sync("--check").returncode, 0)

    def test_invalid_css_value_keeps_page_unchanged(self):
        previous = self.page.read_bytes()
        self.tokens["colors"]["primary"] = "red; } </style><script>"
        self.write_design()
        result = self.run_sync()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(self.page.read_bytes(), previous)

    def test_unknown_reference_keeps_page_unchanged(self):
        previous = self.page.read_bytes()
        self.tokens["components"]["button-primary"]["backgroundColor"] = "{colors.missing}"
        self.write_design()
        result = self.run_sync()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(self.page.read_bytes(), previous)

    def test_cyclic_reference_keeps_page_unchanged(self):
        previous = self.page.read_bytes()
        self.tokens["colors"]["primary"] = "{colors.secondary}"
        self.tokens["colors"]["secondary"] = "{colors.primary}"
        self.write_design()
        result = self.run_sync()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("循环", result.stderr)
        self.assertEqual(self.page.read_bytes(), previous)

    def test_duplicate_group_is_rejected_instead_of_silently_replacing_values(self):
        previous = self.page.read_bytes()
        path = self.root / "ai/specs/design.md"
        document = path.read_text(encoding="utf-8")
        path.write_text(document.replace('"colors": {', '"colors": {"primary": "#eeeeee"}, "colors": {'))
        result = self.run_sync()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(self.page.read_bytes(), previous)

    def test_missing_or_duplicate_generation_slot_keeps_page_unchanged(self):
        original = self.page.read_text()
        for replacement in ("", "/* DESIGN_TOKENS_START */\n/* DESIGN_TOKENS_START */"):
            with self.subTest(replacement=replacement):
                self.page.write_text(original.replace("/* DESIGN_TOKENS_START */", replacement))
                previous = self.page.read_bytes()
                result = self.run_sync()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertEqual(self.page.read_bytes(), previous)

    def test_unknown_or_empty_group_and_wrong_format_version_keep_page_unchanged(self):
        previous = self.page.read_bytes()
        cases = (
            ("colour", {"primary": "#000000"}, "colour"),
            ("colors", {}, "不能为空"),
            ("version", "D9.9", "alpha"),
        )
        for key, value, expected in cases:
            with self.subTest(key=key):
                self.tokens = {
                    "name": "Fixture", "version": "alpha",
                    "colors": {"primary": "#1d4ed8"},
                    "typography": {"body-md": {"fontSize": "14px", "lineHeight": 1.6}},
                    "components": {"button-primary": {"backgroundColor": "{colors.primary}"}},
                }
                self.tokens[key] = value
                self.write_design()
                result = self.run_sync()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(expected, result.stderr)
                self.assertEqual(self.page.read_bytes(), previous)

    def test_duplicate_revision_line_keeps_page_unchanged(self):
        previous = self.page.read_bytes()
        path = self.root / "ai/specs/design.md"
        path.write_text(path.read_text(encoding="utf-8") + "规范版本：D9.9\n", encoding="utf-8")
        result = self.run_sync()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(self.page.read_bytes(), previous)

    def test_version_label_must_be_exactly_the_revision(self):
        original = self.page.read_text()
        for replacement in (
            '<span data-design-version>D1.0 候选</span>',
            '<span data-design-version><b>old</b></span>',
        ):
            with self.subTest(replacement=replacement):
                self.page.write_text(original.replace(
                    '<span data-design-version>old</span>', replacement, 1,
                ))
                previous = self.page.read_bytes()
                result = self.run_sync()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertEqual(self.page.read_bytes(), previous)

    def test_business_page_is_synced_and_its_drift_is_read_only(self):
        business = self.root / "ai/prototypes/pages/index.html"
        business.write_bytes(self.page.read_bytes())
        result = self.run_sync()
        self.assertEqual(result.returncode, 0, result.stderr)
        synced = business.read_text(encoding="utf-8")
        self.assertIn("--colors-primary: #1d4ed8;", synced)
        business.write_text(synced.replace("#1d4ed8", "#ffffff"), encoding="utf-8")
        before = business.read_bytes()
        result = self.run_sync("--check")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("index.html", result.stderr)
        self.assertEqual(business.read_bytes(), before)

    def test_invalid_business_page_does_not_update_showcase(self):
        (self.root / "ai/prototypes/pages/index.html").write_text("<html></html>", encoding="utf-8")
        before = self.page.read_bytes()
        result = self.run_sync()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(self.page.read_bytes(), before)

    def test_repository_showcase_uses_tokens_without_a_second_value(self):
        page = Path(__file__).resolve().parents[2] / "ai/prototypes/design-system.html"
        text = page.read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"var\(--[a-z0-9-]+,", text))
        self.assertIn("h1 { font-size: var(--typography-title-font-size);", text)
        self.assertIsNone(re.search(r"h1[^{]*\{[^}]*font-size:\s*\d", text))
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("sync_design.py")), "--check"],
            cwd=self.temp.name, capture_output=True, text=True, encoding="utf-8", timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unregistered_page_fails_check_and_sync_before_any_write(self):
        extra = self.root / 'ai/prototypes/pages/new.html'
        extra.write_bytes(self.page.read_bytes())
        before = self.page.read_bytes()
        for args in (('--check',), ()):
            with self.subTest(args=args):
                result = self.run_sync(*args)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn('未登记', result.stderr)
                self.assertIn('new.html', result.stderr)
                self.assertEqual(self.page.read_bytes(), before)

    def test_unreadable_prototype_directory_fails_before_any_write(self):
        blocked = self.root / 'ai/prototypes/restricted'
        blocked.mkdir()
        (blocked / 'extra.html').write_bytes(self.page.read_bytes())
        blocked.chmod(0)
        try:
            before = self.page.read_bytes()
            result = self.run_sync()
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertEqual(self.page.read_bytes(), before)
        finally:
            blocked.chmod(0o700)


if __name__ == "__main__":
    unittest.main()
