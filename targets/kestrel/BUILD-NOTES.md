# Project Kestrel: build notes

> FICTIONAL. Everything in `targets/kestrel/` is invented for a portfolio demonstration.

## Why this target exists

Project Falcon's instructions were improved over six graded runs on one target, so its scores may partly reflect tuning to that dataset. Kestrel is a second target, built blind, to test whether the system generalizes. The builder session read only `CLAUDE.md`, `.claude/agents/`, `.claude/commands/`, `data/README.md`, the file names in `data/`, the first line of each CSV in `data/financials/`, `tests/_common.py`, `tests/test_phase2_data.py` and the shape of `tests/data_manifest.json`. It did not open the first target's answer key, scorecards, runs, sources or project docs. The planted issues were designed from general diligence knowledge.

## The deal

| | Falcon (target 1) | Kestrel (target 2) |
|---|---|---|
| Target | Talonfield Systems (from file names) | Corvane Diagnostics, Inc. (NASDAQ: CRVD), a clinical genetic testing lab |
| Buyer | Arbelion Industries | Halvard Ridge Capital Partners Fund IV, a private equity fund |
| Structure | (not read) | Take-private, all cash, US$24.00 per share, financed with a US$750.0 million term loan B and US$980.0 million of fund equity |
| Industry risk themes | (not read) | Medicare reimbursement, fraud and abuse law, payer collections, clinical trial clients, patient data |

## What is in the folder

| Path | Contents |
|---|---|
| `data/deal-brief.md` | Deal terms, financing, timeline, model assumptions and the IC's six questions |
| `data/sec-filings/` | 5 filings: 10-K FY2025, 10-Q Q2 2026, two 8-Ks, 2026 proxy |
| `data/news/` | 13 articles: wire, trade and local press, including an anonymous-source report, a short-seller report and noise |
| `data/litigation/` | `docket_index.csv` with 6 matters (4 court cases, 2 regulatory) and 4 case files |
| `data/financials/` | 7 CSV files plus a README, same file names and column headers as `data/financials/` |
| `evaluation/answer-key.md` | 18 planted issues (P01 to P18), one planted-positives row (P19) and 4 distractors (D1 to D4) |
| `data_manifest.json` | SHA-256 checksums of every file in `data/` and the answer key |

Every Markdown file in `data/` carries a FICTIONAL banner. The answer key follows the grading rules in `/evaluate` (first-listed severity, multi-source flag). Its severity mix by first-listed severity is 4 Critical, 9 High, 4 Medium and 1 Low. More than five issues need more than one source, including a disclosure-timing gap.

## How it was checked

A throwaway script (not committed) re-ran every check in `tests/test_phase2_data.py` against this folder, plus stricter ones:

- balance sheets balance and total liabilities add up, for all four dates;
- segment revenue sums to total revenue; gross profit, operating income, pre-tax income and net income all add up;
- cash flow sections sum to the change in cash; operating cash flow sums from its lines; ending cash ties to the balance sheet; net income ties to the income statement;
- the EBITDA bridge from net income works, EBITDA equals operating income plus D&A, Adjusted EBITDA reconciles, the detail rows sum to "other non-recurring items", and every LTM figure equals FY2025 minus H1 2025 plus H1 2026;
- quarters sum to FY2024, FY2025, H1 2025 and H1 2026;
- payer and client revenue sums to total revenue for both years;
- FICTIONAL banners on every Markdown file, no em dashes, every docket detail file exists, every path cited in the answer key exists, 19 P rows and 4 D rows;
- the manifest matches the files.

All checks passed. Numbers quoted in the filings and news (growth rates, ratios, premiums) were recomputed from the CSVs.

## Notes for the session making commands take a target name

- **Manifest keys are relative to the target folder** (`data/...`, `evaluation/answer-key.md`), so `_common.checksums()` works unchanged if `ROOT` points at `targets/kestrel/`.
- **Two checks in `test_phase2_data.py` are Falcon-specific.** The income statement test names `Revenue: Software (FieldOS)`; Kestrel's segments are `Revenue: Clinical testing`, `Revenue: Biopharma services` and `Revenue: Lab informatics`. Summing every row that starts with `Revenue:` works for both targets. The quarterly test hard-codes 502.3 and 222.6; for Kestrel the totals are FY2025 431.0 and H1 2026 203.4. Comparing with `Total revenue` in `income_statement.csv` works for both.
- **Permission rules.** `.claude/settings.json` denies `Edit(/data/**)`, which also matched `targets/kestrel/data/` when this folder was built. The `Read` ask rule covers `/evaluation/**` and may not cover `targets/kestrel/evaluation/**`. Before a blind Kestrel run, add matching ask and deny rules for `targets/*/evaluation/**` and `targets/*/data/**`.
- The deal brief says "See `data/README.md`", which is relative to the target folder.
