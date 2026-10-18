"""Phase 2: the simulated sources are complete, consistent and unchanged."""
import csv
import json
import re
import unittest

from _common import MANIFEST, ROOT, checksums, read

FIN = ROOT / "data" / "financials"


def load(name):
    with open(FIN / name, encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    return rows[0][1:], {r[0]: r[1:] for r in rows[1:]}


def num(value):
    return float(value.replace("%", "")) if value not in ("", None) else 0.0


class TestFinancialsTieOut(unittest.TestCase):
    def test_balance_sheets_balance(self):
        cols, bs = load("balance_sheet.csv")
        assets = ["Cash and cash equivalents", "Accounts receivable net", "Contract assets (unbilled receivables)", "Inventory", "Prepaid expenses and other current assets", "Property and equipment net", "Goodwill", "Intangible assets net", "Other non-current assets"]
        liabilities = ["Accounts payable", "Accrued liabilities", "Deferred revenue (current)", "Deferred revenue (non-current)", "Revolving credit facility", "Term loan", "Other liabilities"]
        for i, col in enumerate(cols):
            a = sum(num(bs[k][i]) for k in assets)
            l = sum(num(bs[k][i]) for k in liabilities)
            self.assertAlmostEqual(a, num(bs["Total assets"][i]), places=1, msg=f"assets {col}")
            self.assertAlmostEqual(a, l + num(bs["Total stockholders' equity"][i]), places=1, msg=f"balance {col}")

    def test_income_statement_adds_up(self):
        cols, inc = load("income_statement.csv")
        for i, col in enumerate(cols):
            g = lambda k: num(inc[k][i])
            self.assertAlmostEqual(g("Revenue: Hardware") + g("Revenue: Software (FieldOS)") + g("Revenue: Services"), g("Total revenue"), places=1, msg=col)
            self.assertAlmostEqual(g("Total revenue") - g("Cost of revenue"), g("Gross profit"), places=1, msg=col)
            pretax = g("Operating income (loss)") - g("Interest expense") + g("Other income (expense) net")
            self.assertAlmostEqual(pretax - g("Income tax expense (benefit)"), g("Net income (loss)"), places=1, msg=col)

    def test_cash_flow_ties_to_change_in_cash(self):
        cols, cf = load("cash_flow.csv")
        for i, col in enumerate(cols):
            g = lambda k: num(cf[k][i])
            total = g("Net cash from operating activities") + g("Net cash used in investing activities") + g("Net cash from (used in) financing activities")
            self.assertAlmostEqual(total, g("Net change in cash"), places=1, msg=col)

    def test_adjusted_ebitda_reconciles(self):
        cols, eb = load("adjusted_ebitda_reconciliation.csv")
        for i, col in enumerate(cols):
            g = lambda k: num(eb[k][i])
            adjusted = g("EBITDA") + g("Add: Stock-based compensation") + g("Add: Restructuring and other charges") + g("Add: Other non-recurring items (detail below)")
            self.assertAlmostEqual(adjusted, g("Adjusted EBITDA (company definition)"), places=1, msg=col)
            detail = sum(num(eb[k][i]) for k in eb if k.startswith("Detail:"))
            self.assertAlmostEqual(detail, g("Add: Other non-recurring items (detail below)"), places=1, msg=f"detail {col}")

    def test_quarters_sum_to_years(self):
        with open(FIN / "revenue_quarterly.csv", encoding="utf-8") as fh:
            q = {r["quarter"]: float(r["total_revenue"]) for r in csv.DictReader(fh)}
        self.assertAlmostEqual(sum(v for k, v in q.items() if k.endswith("2025")), 502.3, places=1)
        self.assertAlmostEqual(q["Q1 2026"] + q["Q2 2026"], 222.6, places=1)


class TestSourcesComplete(unittest.TestCase):
    def test_every_document_is_labeled_fictional(self):
        for path in (ROOT / "data").rglob("*.md"):
            self.assertIn("FICTIONAL", read(path).upper(), f"{path.name} is not labeled fictional")

    def test_docket_detail_files_exist(self):
        with open(ROOT / "data" / "litigation" / "docket_index.csv", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row["detail_file"]:
                    self.assertTrue((ROOT / "data" / "litigation" / row["detail_file"]).exists(), row["detail_file"])

    def test_answer_key_lists_all_planted_items(self):
        ids = re.findall(r"^\| (P\d{2}|D\d) \|", read(ROOT / "evaluation" / "answer-key.md"), re.M)
        self.assertEqual(len([i for i in ids if i.startswith("P")]), 19)
        self.assertEqual(len([i for i in ids if i.startswith("D")]), 4)


class TestSourcesUnchanged(unittest.TestCase):
    def test_protected_files_match_the_manifest(self):
        self.assertTrue(MANIFEST.exists(), "no manifest: run tests/run_all.py --write-manifest once")
        expected = json.loads(MANIFEST.read_text(encoding="utf-8"))
        actual = checksums()
        changed = sorted(k for k in expected if actual.get(k) != expected[k])
        added = sorted(set(actual) - set(expected))
        self.assertFalse(changed, f"changed since the manifest was written: {changed}")
        self.assertFalse(added, f"new files not in the manifest: {added}")


if __name__ == "__main__":
    unittest.main()
