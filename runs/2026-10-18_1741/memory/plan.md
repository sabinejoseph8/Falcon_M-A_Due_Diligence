# Diligence plan

Status: Complete (2026-10-18). Approved at Checkpoint 1; 2 of 3 iterations used; verified; report written.

## Scope

Project Falcon: Arbelion Industries proposes to acquire Talonfield Systems (NASDAQ: TLFS) for $24.00 per share in cash (34% premium, equity value about $1,159.0m, 48.3m diluted shares). The deal model (v3) uses the March 2026 investor day management case: FY2026E revenue $560.0m, Adjusted EBITDA $118.0m, about 11.5x EV/EBITDA, $35.0m run-rate synergies. IC meets November 6, 2026; exclusivity ends November 20, 2026.

Sources: `data/sec-filings/` (5 files), `data/news/` (13 files), `data/litigation/` (4 cases plus docket index), `data/financials/` (7 CSVs plus README). Management access has not started.

## IC questions mapped to analysts

| # | IC question | Primary analysts | Supporting |
|---|---|---|---|
| Q1 | Is revenue growth real and sustainable? | financial-analyst | sec-filings-analyst (revenue recognition, one-offs), news-media-analyst (guidance cut, outage, market) |
| Q2 | Legal exposures that could reduce value or block closing? | litigation-analyst | sec-filings-analyst (legal proceedings disclosure), news-media-analyst |
| Q3 | Key customer dependence and relationship risk? | financial-analyst (revenue by customer) | sec-filings-analyst (concentration, contract terms), news-media-analyst (Norvale, competitors), litigation-analyst (customer disputes) |
| Q4 | Balance sheet, debt or liquidity issues at closing? | financial-analyst | sec-filings-analyst (covenants, change of control, debt terms) |
| Q5 | Management, governance or internal control concerns? | sec-filings-analyst (auditor change, CFO exit, controls, proxy) | news-media-analyst, litigation-analyst (securities class action) |
| Q6 | Price adjustments and deal protections? | Lead agent synthesis | All four |

## Hypotheses to test

- H1: Reported FY2025 and 2026 growth overstates underlying growth (one-off items, pull-forward, or aggressive recognition), and the March 2026 management case used in the deal model is stale after later guidance changes.
- H2: Adjusted EBITDA is inflated by add-backs that are recurring or unsupported, so the true multiple paid is higher than 11.5x.
- H3: The largest customer relationship(s) are at risk (for example Norvale after its June 2026 acquisition of Kinetic Aisle), and this is not fully reflected in filings or the forecast.
- H4: Governance and control events (auditor switch, CFO exit, securities litigation, short seller claims) point to disclosure or control weaknesses, and some legal events may be under-disclosed or disclosed late in filings.

## Task lists

### sec-filings-analyst (`data/sec-filings/`)
1. Revenue recognition policy, one-off or non-recurring revenue, remaining performance obligations or backlog, and changes between 10-K FY2025 and 10-Q Q2 2026.
2. Customer concentration disclosures and key contract terms (term, termination, change of control).
3. Debt: facilities, covenants (definitions and headroom), maturities, change of control clauses.
4. Internal controls (material weaknesses), auditor change 8-K (reasons, disagreements, reportable events), CFO departure 8-K.
5. Legal proceedings disclosures: which cases are disclosed, how described, and as of which date.
6. Proxy: executive pay, change of control payments, related party transactions, board independence.
7. Anything that changed between filings, and any risk factor language that looks newly added.

### news-media-analyst (`data/news/`)
1. Timeline of events from November 2025 to October 2026, with source reliability for each article.
2. Customer news (Norvale, Kinetic Aisle) and competitive threats.
3. Short seller allegations: list each, label as allegation, note any rebuttal.
4. Operational events (FieldOS outage, layoffs, tariffs) and guidance changes.
5. Management and governance news (auditor switch, CFO exit, scholarship story, sale exploration).
6. Market context: market growth versus Talonfield's.

### litigation-analyst (`data/litigation/`)
1. Each case: parties, claims, posture, key upcoming dates, exposure range, injunction risk.
2. Any events after the latest SEC filing date, and any recent changes to dockets.
3. Whether any case could affect closing, a key customer, a key product, or create change of control issues.
4. Reconcile the docket index with the case files.

### financial-analyst (`data/financials/`)
1. Revenue growth by year and quarter, by segment (hardware, subscription, services) if available; identify one-offs.
2. Adjusted EBITDA reconciliation: test each add-back, compute a diligence-adjusted EBITDA.
3. Customer concentration: top customers' share, trends, and any customer decline.
4. KPIs: backlog, retention, ARR, churn, margins; direction of trend.
5. Balance sheet and cash flow: net debt, liquidity, working capital (receivables, DSO, inventory), cash conversion, capitalized costs.
6. Recompute the deal valuation: EV, implied multiples on reported and adjusted EBITDA, FY2026 run-rate versus the $560.0m / $118.0m management case.

## Iteration budget and stop conditions

- At most 3 Act/Observe iterations.
- Stop when all six IC questions are answered with cited evidence, or when the budget is used up.
- Loop again only if a Critical or High question can still be answered from the available data.

## Checkpoints

1. Approve the plan (this document).
2. Review red flags after Observe.
3. Sign off on verification results and draft recommendation before the report.
