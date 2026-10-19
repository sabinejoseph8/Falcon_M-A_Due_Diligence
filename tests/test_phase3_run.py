"""Phase 3: a diligence run left a complete, consistent audit trail and report.
Checks the run folder given with run_all.py --run (default: the project root)."""
import re
import unittest

import csv

from _common import EM_DASH, ROOT, TARGETS, read, run_dir, run_target, table_rows

# Finding IDs: two or three digits, with an optional letter after the prefix (SEC-01, SEC-001, LIT-F01).
ID_BODY = r"(?:SEC|NEWS|LIT|FIN|X)-[A-Z]?\d{2,3}"
ID = re.compile(rf"^{ID_BODY}$")
WORKSTREAMS = ["SEC", "NEWS", "LIT", "FIN"]
SEVERITIES = {"Critical", "High", "Medium", "Low", "Positive", "n/a"}
STATUSES = {"Open", "Verified", "Partially verified", "Rejected"}
REPORT_SECTIONS = ["executive summary", ("investment committee", "ic questions"), "risk matrix", "workstream", "cross-source", "protections", "open questions", "appendix"]
LINKED_ID = re.compile(r"^\[([^\]]+)\]\([^)]*\)$")
ANALYSTS = ["sec-filings-analyst", "news-media-analyst", "litigation-analyst", "financial-analyst"]

RUN = run_dir()
TARGET = TARGETS / run_target(RUN)
# Court case IDs (LIT-001 and so on) name source files, not findings, so a report may cite them.
DOCKET = TARGET / "data" / "litigation" / "docket_index.csv"
CASE_IDS = set()
if DOCKET.exists():
    with open(DOCKET, newline="") as f:
        CASE_IDS = {row["case_id"] for row in csv.DictReader(f)}
# The report is named after the deal's codename, for example Project-Falcon-Due-Diligence-Report.md.
REPORT = next(iter(sorted((RUN / "output").glob("Project-*-Due-Diligence-Report.md"))), RUN / "output" / "Project-Falcon-Due-Diligence-Report.md")
LOG = RUN / "memory" / "run-log.md"
HAS_RUN = LOG.exists() and re.search(r"checkpoint 1", read(LOG), re.I) is not None
RUN_COMPLETE = HAS_RUN and re.search(r"(?:step )?5[.:]? report", read(LOG), re.I) is not None


def register():
    """Map finding ID -> (severity, status) from the findings register tables."""
    found = {}
    for cells in table_rows(read(RUN / "memory" / "findings.md")):
        if cells:
            cells[0] = LINKED_ID.sub(r"\1", cells[0])
        if cells and ID.match(cells[0]):
            severity = next((c for c in cells if c in SEVERITIES), None)
            found[cells[0]] = (severity, cells[-1], cells)
    return found


@unittest.skipUnless(HAS_RUN, f"no diligence run found in {RUN}")
class TestWorkingMemory(unittest.TestCase):
    def test_run_names_a_known_target(self):
        self.assertTrue((TARGET / "data").is_dir(), f"the run's target has no data folder: {TARGET.relative_to(ROOT)}")

    def test_every_finding_is_complete(self):
        findings = register()
        self.assertGreater(len(findings), 0, "the register is empty")
        # Guard against IDs in a format this check cannot read: every workstream must be found.
        for prefix in WORKSTREAMS:
            self.assertTrue(any(fid.startswith(prefix + "-") for fid in findings), f"no {prefix} findings read from the register (unrecognized ID format?)")
        for fid, (severity, status, cells) in findings.items():
            self.assertIsNotNone(severity, f"{fid}: no valid severity")
            self.assertIn(status, STATUSES, f"{fid}: invalid status '{status}'")
            self.assertTrue(all(cells), f"{fid}: has an empty cell (missing source?)")

    def test_loop_cap_respected(self):
        iterations = [int(n) for n in re.findall(r"ACT,? \(?iteration (\d)\)?", read(LOG))]
        self.assertTrue(iterations and max(iterations) <= 3, f"iterations used: {iterations}")

    def test_every_analyst_report_was_saved(self):
        for name in ANALYSTS:
            self.assertTrue((RUN / "memory" / "analyst-reports" / f"iteration-1_{name}.md").exists(), f"missing report for {name}")


@unittest.skipUnless(RUN_COMPLETE, f"run in {RUN} is not complete yet")
class TestCompletedRun(unittest.TestCase):
    def test_run_log_shows_all_three_checkpoints(self):
        log = read(LOG)
        for n in (1, 2, 3):
            self.assertRegex(log, re.compile(f"checkpoint {n}", re.I), f"checkpoint {n} missing from the run log")

    def test_checkpoint_rows_record_that_content_was_shown(self):
        rows = [" | ".join(r) for r in table_rows(read(LOG))]
        for n in (1, 2, 3):
            row = next((r for r in rows if re.search(rf"\|\s*checkpoint {n}\b", "| " + r, re.I)), "")
            shown = re.search(r"\bshown\b", row, re.I) and not re.search(r"\bnot (?:shown|printed)\b", row, re.I)
            self.assertTrue(shown, f"checkpoint {n}: the run-log row must say the content was shown in chat: {row!r}")


@unittest.skipUnless(HAS_RUN and REPORT.exists(), f"no report found in {RUN / 'output'}")
class TestReport(unittest.TestCase):
    def setUp(self):
        self.text = read(REPORT)

    def test_report_has_all_sections(self):
        headings = " ".join(h.lower() for h in re.findall(r"^#{2} .*$", self.text, re.M))
        for section in REPORT_SECTIONS:
            options = section if isinstance(section, tuple) else (section,)
            self.assertTrue(any(o in headings for o in options), f"missing section: {options[0]}")
        self.assertIn("cover", self.text, "missing cover page")

    def test_report_cites_only_known_findings(self):
        findings = register()
        cited = set(re.findall(rf"\b{ID_BODY}\b", self.text))
        unknown = sorted(cited - set(findings) - CASE_IDS)
        self.assertFalse(unknown, f"cited in the report but not in the register: {unknown}")

    def test_rejected_findings_stay_out_of_the_report(self):
        rejected = {fid for fid, (_, status, _) in register().items() if status == "Rejected"}
        leaked = sorted(fid for fid in rejected if re.search(rf"\b{fid}\b", self.text))
        self.assertFalse(leaked, f"rejected findings in the report: {leaked}")

    def test_report_files_exist_and_have_no_em_dashes(self):
        html = REPORT.with_suffix(".html")
        self.assertTrue(html.exists(), "missing HTML report")
        self.assertIn("<style", read(html), "HTML report does not embed its stylesheet")
        self.assertNotIn(EM_DASH, self.text)
        if not REPORT.with_suffix(".pdf").exists():
            self.skipTest("no PDF (allowed when no PDF tool is installed)")


if __name__ == "__main__":
    unittest.main()
