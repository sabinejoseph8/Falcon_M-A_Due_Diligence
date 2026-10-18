# Diligence plan: Project Falcon

Status: Approved at Checkpoint 1 (test run). Iteration budget: 3 Act/Observe iterations.

## Deal context
Arbelion Industries proposes to acquire Talonfield Systems (NASDAQ: TLFS) for $24.00 per share in cash (34% premium; implied equity value about $1,159M). IC meeting November 6, 2026; exclusivity ends November 20, 2026. The deal model (v3) relies on the March 2026 management case: FY2026E revenue $560M and Adjusted EBITDA $118M (about 11.5x EV / EBITDA).

## IC questions mapped to analysts

| # | IC question | Primary analysts | Supporting |
|---|---|---|---|
| Q1 | Is revenue growth real and sustainable? | financial-analyst, sec-filings-analyst | news-media-analyst |
| Q2 | Legal exposures that could reduce value or block closing? | litigation-analyst, sec-filings-analyst | news-media-analyst |
| Q3 | Customer dependence and relationship risk? | financial-analyst, sec-filings-analyst | news-media-analyst, litigation-analyst |
| Q4 | Balance sheet, debt and liquidity issues at closing? | financial-analyst, sec-filings-analyst | |
| Q5 | Management, governance or control concerns? | sec-filings-analyst, news-media-analyst | litigation-analyst |
| Q6 | Price adjustments and deal protections? | lead agent (synthesis) | all |

## Hypotheses to test

- **H1:** Reported 2025 growth and the March 2026 management case overstate sustainable performance. (The share price is far below the level implied by the management case.)
- **H2:** There are legal or regulatory exposures large enough to need specific protections (indemnity, escrow, closing conditions).
- **H3:** Revenue depends on a few customers whose relationships could change after a change of control.
- **H4:** Debt terms, leverage or liquidity create costs or risks at closing.

## Task lists

**sec-filings-analyst** (`data/sec-filings/`): revenue recognition policies and unusual arrangements; internal controls and auditor history; management changes; debt and covenant definitions, including change-of-control terms; customer and supplier concentration and contract terms; legal proceedings as disclosed, including accruals; compensation, change-in-control payments, related parties; changes between the 10-K, 10-Q and 8-Ks; guidance and revisions.

**news-media-analyst** (`data/news/`): dated timeline; allegations and rumors with company responses; customer and competitor moves; incidents and whether they were formally disclosed; market and trade context; share price reactions; irrelevant items.

**litigation-analyst** (`data/litigation/`): every matter in the docket index; posture and recent rulings; exposure versus caps; injunction risk; dates before and around the expected closing; items to compare with the company's own disclosures.

**financial-analyst** (`data/financials/` and `data/deal-brief.md`): growth by segment and quarter; margins; Adjusted EBITDA add-backs; DSO, allowance, contract assets, inventory; cash conversion and free cash flow; leverage and liquidity; customer concentration; KPIs; recompute the deal brief's valuation and test it against H1 2026 and LTM.

## Stop conditions
All six IC questions answered with cited, verified evidence, or 3 iterations used. Any remaining gaps go to the management request list.
