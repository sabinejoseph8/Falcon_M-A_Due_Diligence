"""Phase 4: the run was graded against the answer key."""
import re
import unittest

from _common import read, run_dir

SCORECARD = run_dir() / "evaluation" / "scorecard.md"


@unittest.skipUnless(SCORECARD.exists(), f"no scorecard at {SCORECARD}")
class TestScorecard(unittest.TestCase):
    def setUp(self):
        self.text = read(SCORECARD)

    def test_scorecard_reports_the_four_metrics(self):
        for metric in ("Recall", "Severity accuracy", "Unsupported", "Distractor"):
            self.assertIn(metric.lower(), self.text.lower(), f"missing metric: {metric}")

    def test_every_planted_issue_is_graded(self):
        graded = set(re.findall(r"^\| (P\d{2}) \|", self.text, re.M))
        missing = sorted({f"P{n:02d}" for n in range(1, 19)} - graded)
        self.assertFalse(missing, f"not graded: {missing}")


if __name__ == "__main__":
    unittest.main()
