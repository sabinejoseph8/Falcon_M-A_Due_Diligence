# Diligence plan

Status: Complete. Approved at Checkpoint 1; 2 of 3 iterations used; report approved at Checkpoint 3 (2026-10-18).

## Scope

- Deal: Project Falcon. Arbelion Industries proposes to buy Talonfield Systems (NASDAQ: TLFS) for $24.00 per share in cash, about $1,159.2 million equity value (48.3 million diluted shares). One-step merger, funded with cash and a new Arbelion term loan.
- Key dates: IC meeting November 6, 2026. Exclusivity ends November 20, 2026.
- Valuation basis to test: deal model v3 uses the March 2026 investor day management case (FY2026E revenue $560.0 million, Adjusted EBITDA $118.0 million, about 11.5x EV / EBITDA on June 30, 2026 net debt, $35.0 million run-rate synergies by year 3).
- Sources: only `data/`. No management access yet, so management questions are collected in `memory/open-questions.md`.

## IC questions mapped to analysts

| # | IC question | Lead analysts | Supporting |
|---|---|---|---|
| Q1 | Is revenue growth real and sustainable? | financial-analyst, sec-filings-analyst | news-media-analyst |
| Q2 | Legal exposures that could reduce value or block closing? | litigation-analyst | sec-filings-analyst, news-media-analyst |
| Q3 | Dependence on key customers, and are relationships at risk? | financial-analyst, news-media-analyst | sec-filings-analyst, litigation-analyst |
| Q4 | Balance sheet, debt or liquidity issues inherited at closing? | financial-analyst, sec-filings-analyst | litigation-analyst |
| Q5 | Management, governance or internal control concerns? | sec-filings-analyst, news-media-analyst | litigation-analyst |
| Q6 | Price adjustments or deal protections to ask for? | Lead agent (synthesis of all) | all |

## Hypotheses to test

- H1: Reported 2025 and 2026 growth overstates underlying, repeatable growth (one-off items, pull-forward, or recognition timing).
- H2: The management case behind the deal model (FY2026E $560.0 million revenue, $118.0 million Adjusted EBITDA) is stale after events in 2026, so the 11.5x multiple understates the true price paid.
- H3: Talonfield depends on one or a few customers whose relationship is weakening, and this is not fully disclosed.
- H4: Leadership, auditor and control changes, together with litigation, point to governance or disclosure risks (including events that filings omit or describe late).

## Task lists

### sec-filings-analyst (`data/sec-filings/`)
1. Revenue recognition policies and any changes; one-off, multi-element or bill-and-hold items; growth drivers as described by management.
2. Internal controls: material weaknesses, remediation status, auditor opinion; the November 2025 auditor change (reasons, disagreements, reportable events, timing).
3. Debt: facilities, covenants (definitions, levels, headroom), maturities, change of control clauses.
4. Customer concentration disclosures and key contracts (terms, renewal, termination rights).
5. Legal proceedings and contingencies as disclosed; compare to what the 10-Q says vs the 10-K.
6. Governance and compensation from the DEF 14A: CFO departure (8-K), related parties, change of control payments, incentive metrics.
7. Changes between the 10-K and the Q2 2026 10-Q (risk factors, guidance, going concern, subsequent events).

### news-media-analyst (`data/news/`)
1. Rate every source for reliability (primary, reputable secondary, anonymous, short seller, promotional).
2. Customer news, especially major customers and any competitor acquisitions that could affect them.
3. Product and operations: FieldOS outage, launches, layoffs, supply chain and tariff exposure.
4. Leadership and auditor news; the short seller report claims (labeled as allegations).
5. Guidance changes and the sale process; any market data that challenges the management case.
6. Timeline of events to compare against filing dates.

### litigation-analyst (`data/litigation/`)
1. Each matter: parties, claims, posture, key upcoming dates, damages sought, realistic exposure range.
2. Injunction or other risk that could affect operations or block closing; change of control or assignment issues.
3. Recent changes in any matter (new filings, rulings, amended complaints) and their dates.
4. Facts in court records that may conflict with or be missing from company disclosures.

### financial-analyst (`data/financials/`)
1. Revenue growth: annual and quarterly, by segment if available; one-off items; recompute growth rates.
2. Adjusted EBITDA: test each add-back; recompute reported and diligence-adjusted EBITDA.
3. Customer concentration: top customers' share, trends, revenue at risk.
4. KPIs: backlog, retention or net revenue retention, ARR, churn, and their trend.
5. Balance sheet and cash flow: net debt, leverage vs covenants, liquidity, working capital trends (DSO, inventory, deferred revenue), cash conversion.
6. Valuation check: implied EV and EV / EBITDA on reported, management case and diligence-adjusted EBITDA; compare actual run-rate with the FY2026E management case.

## Iteration budget and stop conditions

- At most 3 Act/Observe iterations.
- Stop when all six IC questions are answered with cited evidence, or the budget is used up.
- Loop again only if a Critical or High question can still be answered from the available data.

## Checkpoints

1. Approve the plan (this document).
2. Review red flags after Observe.
3. Sign off verification results and draft recommendation before the report.
