"""Phase 4: the run was graded against its target's answer key."""
import re
import unittest

from _common import ROOT, TARGETS, read, run_dir, run_target, target_checks

RUN = run_dir()
TARGET = TARGETS / run_target(RUN)
# A saved run keeps its scorecard in its own evaluation/ folder; the live run's is in the target's folder.
SCORECARD = RUN / "evaluation" / "scorecard.md"
if not SCORECARD.exists() and RUN == ROOT:
    SCORECARD = TARGET / "evaluation" / "scorecard.md"


def must_grade():
    """Planted IDs the scorecard must grade: P01 to the count in checks.json, or every P ID in the answer key."""
    count = target_checks(TARGET).get("scorecard_must_grade")
    if count is None:
        return set(re.findall(r"^\| (P\d{2}) \|", read(TARGET / "evaluation" / "answer-key.md"), re.M))
    return {f"P{n:02d}" for n in range(1, count + 1)}


@unittest.skipUnless(SCORECARD.exists(), f"no scorecard at {SCORECARD}")
class TestScorecard(unittest.TestCase):
    def setUp(self):
        self.text = read(SCORECARD)

    def test_scorecard_reports_the_four_metrics(self):
        for metric in ("Recall", "Severity accuracy", "Unsupported", "Distractor"):
            self.assertIn(metric.lower(), self.text.lower(), f"missing metric: {metric}")

    def test_every_planted_issue_is_graded(self):
        graded = set(re.findall(r"^\| (P\d{2}) \|", self.text, re.M))
        missing = sorted(must_grade() - graded)
        self.assertFalse(missing, f"not graded: {missing}")


if __name__ == "__main__":
    unittest.main()
