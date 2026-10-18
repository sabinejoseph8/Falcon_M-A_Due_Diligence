"""All phases: house style and working links."""
import re
import unittest
from urllib.parse import unquote

from _common import EM_DASH, ROOT, read

TEXT_TYPES = {".md", ".csv", ".json", ".svg", ".css", ".html"}
SKIP_DIRS = {".git", "runs", "node_modules"}


class TestStyle(unittest.TestCase):
    def test_no_em_dashes_anywhere(self):
        offenders = []
        for path in ROOT.rglob("*"):
            if path.is_file() and path.suffix in TEXT_TYPES and not (set(path.relative_to(ROOT).parts) & SKIP_DIRS):
                if EM_DASH in read(path):
                    offenders.append(str(path.relative_to(ROOT)))
        self.assertFalse(offenders, f"em dashes found in: {offenders}")

    def test_readme_links_point_to_real_files(self):
        readme = read(ROOT / "README.md")
        for target in re.findall(r"\]\(([^)#:]+)\)", readme):
            target = unquote(target)
            self.assertTrue((ROOT / target).exists(), f"README links to a missing file: {target}")


if __name__ == "__main__":
    unittest.main()
