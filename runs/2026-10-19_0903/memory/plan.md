# Diligence plan

Status: Plan approved at Checkpoint 1; 2 of 3 iterations used; run complete 2026-10-19.
Prepared: 2026-10-18 by Agent Core.

## Scope

Project Falcon: Arbelion Industries proposes to acquire Talonfield Systems (NASDAQ: TLFS) for $24.00 per share in cash (34% premium to $17.85 on Oct 16, 2026), about $1,159 million equity value on 48.3 million diluted shares. The deal model (v3, Sept 2026) uses the March 2026 investor-day management case: FY2026E revenue $560.0 million, Adjusted EBITDA $118.0 million, EV / EBITDA about 11.5x, $35.0 million run-rate synergies. IC meets Nov 6, 2026; exclusivity ends Nov 20, 2026. Sources: `data/` only (SEC filings, news, litigation dockets, financial data). No management access yet.

## IC questions mapped to analysts

| # | IC question | Primary analysts | Supporting |
|---|---|---|---|
| Q1 | Is revenue growth real and sustainable? | financial-analyst, sec-filings-analyst | news-media-analyst |
| Q2 | Legal exposures that could reduce value or block closing? | litigation-analyst | sec-filings-analyst (legal proceedings, contingencies), news-media-analyst |
| Q3 | Dependence on key customers, relationships at risk? | financial-analyst (revenue_by_customer), news-media-analyst | sec-filings-analyst (concentration), litigation-analyst |
| Q4 | Balance sheet, debt or liquidity issues inherited at closing? | financial-analyst, sec-filings-analyst (debt, covenants, change of control) | news-media-analyst |
| Q5 | Management, governance or internal control concerns? | sec-filings-analyst (8-Ks, DEF 14A, ICFR), news-media-analyst | litigation-analyst |
| Q6 | Price adjustments or deal protections? | Agent Core synthesis of all findings | all |

## Hypotheses to test

- **H1.** Reported 2025 growth overstates underlying, repeatable growth (one-off or pulled-forward revenue, recognition judgments, timing of Q4 2025 "record quarter").
- **H2.** The March 2026 management case ($560.0 million revenue, $118.0 million Adjusted EBITDA) is stale after later events (guidance cut, outage, layoffs, tariffs, customer moves), so 11.5x understates the real multiple.
- **H3.** Key customer relationships are at risk (for example a top customer acquiring a competitor) and concentration is higher than the brief assumes.
- **H4.** There are disclosure, governance or control weaknesses (auditor change, CFO exit, related-party items, litigation not reflected in filings) that call for specific deal protections.

## Task list by analyst

### sec-filings-analyst (`data/sec-filings/`)
1. Revenue recognition policies, one-off or unusual revenue items in FY2025 and H1 2026, and any changes between the 10-K and the Q2 10-Q.
2. Internal control over financial reporting: material weaknesses, auditor opinion, the Nov 2025 auditor change (reasons, disagreements, reportable events).
3. Debt: facilities, maturities, covenants (definitions and headroom), change-of-control clauses, going-concern language.
4. Customer concentration disclosures and named customers.
5. Legal proceedings and contingency reserves, with the dates of each judgment (for example as-of dates for reserves, goodwill or impairment tests).
6. Governance: CFO departure 8-K, proxy (compensation, related-party transactions, board independence, change-of-control payments).
7. Risk factors and guidance changes; note any filing made after an event it does not mention.

### news-media-analyst (`data/news/`)
1. Timeline of all articles, with a reliability rating for each source.
2. Auditor switch, CFO exit, layoffs, guidance cut, sale exploration coverage.
3. Customer and competitor news (Norvale / Kinetic Aisle), FieldOS 5 launch and outage, any customer impact.
4. Short-seller allegations: what is alleged, and what is confirmed elsewhere.
5. Market and industry context (market report, lidar tariffs) and share price data points mentioned.
6. Anything that contradicts company filings or the deal brief assumptions.

### litigation-analyst (`data/litigation/`)
1. Each matter: parties, claims, court, posture, key upcoming dates, damages sought, injunction risk.
2. Recent docket changes (use `docket_index.csv`) and what changed after each filing date.
3. Whether any matter could block or delay closing, or touches change of control or key IP.
4. Exposure estimates versus any amounts disclosed by the company.

### financial-analyst (`data/financials/`)
1. Revenue trend by year and quarter; growth rates; any one-off items; revenue mix (hardware, software, services).
2. Adjusted EBITDA reconciliation: quality of add-backs, recurring "one-off" items, reported vs adjusted.
3. Customer concentration from `revenue_by_customer.csv`: top customers, share, trend.
4. KPIs (backlog, ARR, retention, churn and so on) and trends.
5. Balance sheet and cash flow: net debt at June 30, 2026, working capital (receivables, DSO, inventory), cash burn, liquidity.
6. Recompute the deal multiple on the latest data (EV, LTM and run-rate EBITDA) versus the 11.5x in the brief.

## Iteration budget and stop conditions

- **Budget:** at most 3 Act/Observe iterations.
- **Stop when:** all six IC questions are answered with cited evidence, or the budget is used up.
- Loop again only if a Critical or High question can still be answered from the available data.
