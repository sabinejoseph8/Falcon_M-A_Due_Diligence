# Diligence plan

Status: Drafted 2026-10-18. Awaiting Checkpoint 1 approval.

## Scope

- Deal: Project Falcon. Arbelion Industries proposes to acquire Talonfield Systems (NASDAQ: TLFS) for $24.00 per share in cash (34% premium to the $17.85 close on October 16, 2026), about $1,159.0 million equity value on 48.3 million diluted shares.
- Valuation basis under test: deal model v3 (September 2026) uses the March 2026 investor day management case: FY2026E revenue $560.0 million, FY2026E Adjusted EBITDA $118.0 million, about 11.5x EV / FY2026E Adjusted EBITDA, $35.0 million run-rate cost synergies by year 3.
- Key dates: IC meeting November 6, 2026. Exclusivity expires November 20, 2026.
- Sources: only the files in `data/` (SEC filings, news, litigation dockets, financials). No management access yet.

## IC questions mapped to analysts

| # | IC question | Lead analysts | Supporting analysts |
|---|---|---|---|
| Q1 | Is Talonfield's revenue growth real and sustainable? | financial-analyst | sec-filings-analyst (revenue recognition, one-offs, guidance), news-media-analyst (guidance cut, short seller, market) |
| Q2 | Are there legal exposures that could reduce value or block closing? | litigation-analyst | sec-filings-analyst (legal proceedings and contingency disclosures), news-media-analyst |
| Q3 | How dependent is Talonfield on key customers, and are those relationships at risk? | financial-analyst (revenue_by_customer) | news-media-analyst (customer news, competitor moves), sec-filings-analyst (concentration disclosure), litigation-analyst (customer disputes) |
| Q4 | Are there balance sheet, debt or liquidity issues we would inherit at closing? | financial-analyst | sec-filings-analyst (debt terms, covenants, change of control) |
| Q5 | Are there management, governance or internal control concerns? | sec-filings-analyst | news-media-analyst (executive departures, auditor change), litigation-analyst (securities and employment claims) |
| Q6 | What price adjustments or deal protections should we ask for? | Lead agent (synthesis) | All analysts |

## Hypotheses to test

- H1: Reported 2025 and 2026 growth overstates underlying, recurring growth (one-off revenue, pull-forward or aggressive recognition), and the $560.0 million / $118.0 million management case is stale after later guidance changes.
- H2: Adjusted EBITDA is inflated by add-backs that are recurring or not truly one-off, so the 11.5x multiple understates the real price paid.
- H3: Customer concentration is high and at least one major customer relationship is at risk (for example a customer acquiring a competitor or a contract dispute).
- H4: There are legal, debt or governance issues (litigation, covenant headroom, change-of-control terms, control weaknesses, auditor and CFO changes) that the filings understate or disclose late, and that need specific deal protections.

## Task lists

### sec-filings-analyst (`data/sec-filings/`)

1. Revenue recognition policies, any one-off or non-recurring revenue items, and changes between the 10-K FY2025 and the 10-Q Q2 2026.
2. Debt: facility size, maturity, financial covenants (definitions and thresholds), reported compliance, change-of-control and prepayment terms.
3. Customer concentration disclosures (named customers, percentages, contract terms).
4. Legal proceedings and contingencies as disclosed; note dates so they can be compared with court records.
5. Internal controls (any material weakness), auditor change (reasons, disagreements, reportable events), CFO departure terms.
6. Governance and compensation in the DEF 14A: related parties, change-of-control payments, incentive metrics.
7. Changes in language between filings, and any subsequent events or risk factors that matter to the deal.

### news-media-analyst (`data/news/`)

1. Guidance changes and how they compare to the March 2026 investor day case.
2. Short seller allegations: what is claimed, evidence offered, and company response. Rate reliability.
3. Customer and competitor news (for example a major customer buying a competitor), product outages, tariffs and supply chain risk.
4. Executive departures, auditor switch, layoffs, sale process coverage.
5. Industry and market context for growth assumptions.
6. Rate each source's reliability and flag anything that is rumor or anonymous.

### litigation-analyst (`data/litigation/`)

1. For each matter: parties, claims, procedural posture, key upcoming dates (especially before the IC date and before the exclusivity end), amount at stake.
2. Injunction risk or any matter that could block closing or affect a product line.
3. Recent changes in the docket (rulings, new filings, settlement talks) and their dates.
4. Exposure estimates (range) and any insurance or indemnity mentioned.
5. Whether any litigant is also a customer or supplier.

### financial-analyst (`data/financials/`)

1. Revenue trend: annual and quarterly growth, recurring vs. one-off revenue, segment mix (hardware, FieldOS, services).
2. Quality of earnings: rebuild Adjusted EBITDA from the reconciliation, test each add-back, and compute an adjusted figure.
3. Customer concentration: top customers by revenue and share, trends by customer.
4. Balance sheet and liquidity: cash, debt, net debt, working capital (DSO, inventory), covenant metrics if computable.
5. Cash flow: operating cash flow vs. EBITDA, capex, free cash flow.
6. KPIs: backlog, bookings, retention, ARR and any weakening trends.
7. Valuation check: recompute EV and EV / Adjusted EBITDA at $24.00 per share against the management case and against a corrected run-rate.

## Iteration budget and stop conditions

- Budget: at most 3 Act/Observe iterations.
- Stop when all six IC questions are answered with cited evidence, or when the budget is used up.
- Loop again only if a Critical or High question can still be answered from the available data.

## Human checkpoints

1. Approve this plan.
2. Review the red flags after Observe.
3. Sign off on verification results and the draft recommendation before the report.
