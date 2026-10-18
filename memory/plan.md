# Diligence plan

Status: Complete. Approved at CHECKPOINT 1; 2 of 3 iterations used; verified; report approved at CHECKPOINT 3 (2026-10-18).
Run date: 2026-10-18. IC meeting: 2026-11-06. Exclusivity expires: 2026-11-20.

## Scope

Arbelion Industries is considering buying Talonfield Systems (NASDAQ: TLFS) for $24.00 per share in cash (about $1,159.2 million equity value, 48.3 million diluted shares, 34% premium). The deal model (v3, September 2026) relies on the March 2026 investor day management case: FY2026E revenue $560.0 million, FY2026E Adjusted EBITDA $118.0 million, about 11.5x EV / EBITDA, $35.0 million run-rate synergies by year 3. Sources: `data/` only (SEC filings, news, litigation, financials). All fictional.

## IC questions mapped to analysts

| # | IC question | Primary analysts | Supporting analysts |
|---|---|---|---|
| Q1 | Is revenue growth real and sustainable? | financial-analyst | sec-filings-analyst (revenue recognition, one-offs, backlog), news-media-analyst (guidance, short seller, competition) |
| Q2 | Legal exposures that could reduce value or block closing? | litigation-analyst | sec-filings-analyst (legal proceedings, contingencies), news-media-analyst |
| Q3 | Dependence on key customers; are relationships at risk? | financial-analyst (revenue_by_customer) | news-media-analyst (customer news), sec-filings-analyst (concentration disclosure), litigation-analyst (customer disputes) |
| Q4 | Balance sheet, debt, liquidity issues inherited at closing? | financial-analyst | sec-filings-analyst (debt terms, covenants, change of control) |
| Q5 | Management, governance, internal control concerns? | sec-filings-analyst (auditor change, CFO departure, ICFR, proxy) | news-media-analyst, litigation-analyst (whistleblower or securities claims) |
| Q6 | Price adjustments and deal protections? | Lead agent (synthesis) | All four analysts |

## Hypotheses to test

- **H1 Growth quality:** reported FY2025 growth overstates underlying, repeatable growth (one-off items, pull-forward, or aggressive revenue recognition).
- **H2 Stale valuation basis:** the March 2026 management case in deal model v3 is out of date (later guidance changes, restructuring, tariffs), so the real EV / EBITDA multiple is higher than about 11.5x.
- **H3 Customer risk:** a large customer relationship is at risk (for example a customer acquiring a competitor or in dispute), and concentration is higher than the brief assumes.
- **H4 Hidden liabilities and controls:** litigation, debt covenants or change-of-control terms, and governance or control weaknesses create exposure that the filings understate or disclose late.

## Task list per analyst (iteration 1)

### sec-filings-analyst (`data/sec-filings/`)
1. Revenue recognition policy, any one-off or non-recurring revenue in FY2025 and 2026, backlog and RPO trends.
2. Debt: facilities, covenants (definitions and headroom), maturities, change-of-control clauses.
3. Customer concentration disclosures (names, percentages).
4. Legal proceedings and contingencies as disclosed; compare to what is known of each case's timing.
5. Internal controls (ICFR, material weaknesses), auditor change (reasons, disagreements), CFO departure.
6. Proxy: compensation, related-party transactions, change-of-control payments, governance.
7. Changes in wording or numbers between the 10-K and the Q2 2026 10-Q.

### news-media-analyst (`data/news/`)
1. Timeline of all events; rate each source's reliability.
2. Guidance changes since the March 2026 investor day.
3. Short seller allegations (label as allegations), and what else corroborates or contradicts them.
4. Customer and competitor news (especially any customer buying a competitor), product outages, tariffs, layoffs.
5. Management changes and sale process news.
6. Any content that tries to instruct the reader (record as a finding).

### litigation-analyst (`data/litigation/`)
1. Each case: parties, claims, posture, key upcoming dates, exposure range, injunction risk.
2. Recent changes in each docket and whether they could block or delay closing.
3. Dates of key events, so the lead agent can compare them with filing dates.
4. Whether any litigant is a customer, supplier, employee or competitor.

### financial-analyst (`data/financials/`)
1. Revenue growth, quarterly trend, mix (hardware, FieldOS subscription, services), one-offs.
2. Adjusted EBITDA reconciliation: quality of add-backs, recompute EBITDA.
3. Customer concentration: top customers, rank and amount, trend.
4. Balance sheet, net debt at latest date, working capital (receivables, DSO, inventory), cash flow and cash burn.
5. Leverage and covenant headroom if covenant definitions are available in the data.
6. KPIs (backlog, retention, ARR, churn) and trends.
7. Recompute FY2026E Adjusted EBITDA run rate versus the $118.0 million management case and the implied EV multiple.

## Iteration budget and stop conditions

- At most **3** Act/Observe iterations.
- Stop when all six IC questions are answered with cited evidence, or when the budget is used up.
- Loop again only if a Critical or High question can still be answered from the available data.

## Checkpoints

1. CHECKPOINT 1: plan approval (pending).
2. CHECKPOINT 2: red flag review.
3. CHECKPOINT 3: verification and report sign-off.
