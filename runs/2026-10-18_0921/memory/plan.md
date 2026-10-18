# Diligence plan

Status: Approved at Checkpoint 1 (2026-10-18 01:42 EST, user replied "approve"). Iteration 1 under way.

- Run started: 2026-10-18 01:04 EST
- Lead agent: Agent Core
- Deal: Project Falcon. Arbelion Industries is considering buying Talonfield Systems (NASDAQ: TLFS) for US$24.00 per share in cash, a 34% premium to the October 16, 2026 close of US$17.85. 48.3 million diluted shares, so implied equity value is about US$1,159.2 million.
- Key dates: IC meeting November 6, 2026. Exclusivity expires November 20, 2026.
- Valuation basis in deal model v3: March 2026 investor day management case. FY2026E revenue US$560.0 million, FY2026E Adjusted EBITDA US$118.0 million, about 11.5x EV / FY2026E Adjusted EBITDA (net debt at June 30, 2026), US$35.0 million run-rate cost synergies by year 3.

## Scope

- In scope: the four source folders in `data/` (SEC filings, news, litigation, financials) and the deal brief.
- Out of scope: management access (not started yet), web sources (blocked), any file outside `data/`.
- Outputs: a verified findings register in `memory/` and a draft IC report in `output/`.

## The six IC questions and who answers them

| # | IC question | Lead analyst | Supporting analysts |
|---|---|---|---|
| Q1 | Is Talonfield's revenue growth real and sustainable? | financial-analyst | sec-filings-analyst (revenue recognition, guidance); news-media-analyst (guidance changes, customers, market, short seller claims) |
| Q2 | Are there legal exposures that could reduce value or block closing? | litigation-analyst | sec-filings-analyst (how each case is disclosed and accrued); news-media-analyst (coverage of cases) |
| Q3 | How dependent is Talonfield on key customers, and are those relationships at risk? | financial-analyst (revenue by customer) | sec-filings-analyst (concentration, contract terms); news-media-analyst (customer moves); litigation-analyst (customer disputes) |
| Q4 | Are there balance sheet, debt or liquidity issues we would inherit at closing? | financial-analyst | sec-filings-analyst (debt terms, covenants, change of control) |
| Q5 | Are there management, governance or internal control concerns? | sec-filings-analyst | news-media-analyst (executive exits, auditor change, layoffs); litigation-analyst (securities and employee claims) |
| Q6 | What price adjustments or deal protections should we ask for? | Lead agent (synthesis) | financial-analyst (valuation check); every analyst (deal impact of each finding) |

## Hypotheses to test

| ID | Hypothesis | IC questions | How we test it |
|---|---|---|---|
| H1 | Reported FY2025 growth overstates underlying, repeatable growth, because of one-off or pulled-forward revenue, aggressive revenue recognition, or reliance on a few customers. | Q1, Q3 | Quarterly revenue by segment and by customer; revenue recognition notes in the filings; KPIs (ARR, retention, backlog); short seller claims. |
| H2 | The deal model is stale. The March 2026 management case no longer matches current trading, and add-backs flatter Adjusted EBITDA, so the real multiple at US$24.00 is well above 11.5x. | Q1, Q6 | H1 2026 and LTM results; any guidance change after March 2026; quality of add-backs; recomputed EV and multiples. |
| H3 | Material events (court rulings, customer moves, incidents, auditor or executive departures) show up in court records or news before, or differently from, the company's filings. This would point to disclosure or internal control weakness. | Q2, Q5 | Compare dates and wording across filings, dockets and news; controls and auditor disclosures. |
| H4 | Debt covenants, change-of-control terms, court dates before closing or customer termination rights could create a liquidity problem or complicate closing. | Q2, Q4, Q6 | Covenant definitions and headroom on current EBITDA; change-of-control clauses; court calendar; customer contract terms. |

## Task lists

### sec-filings-analyst (SEC Filing Search, `data/sec-filings/`)

1. Read all five filings in full: the FY2025 10-K, the Q2 2026 10-Q, the two 8-Ks and the 2026 proxy (DEF 14A). Note each filing date.
2. Revenue recognition: policies, unusual arrangements (for example bill-and-hold), amounts, timing and the customers involved. Quantify each as a share of the relevant quarter and year.
3. Internal controls and auditor: auditor opinion, material weaknesses, the auditor change (stated reason, disagreements, reportable events), remediation status, and anything that changed between the 10-K and the 10-Q.
4. Management changes: the CFO departure, its exact wording, timing, any payments and interim arrangements.
5. Debt: facilities, amounts, maturities, covenant definitions (caps, step-downs, test dates), headroom at the last test date, and change-of-control provisions.
6. Concentration: top customers and suppliers, termination rights and change-of-control consents.
7. Legal proceedings: how each case is described, any accrual, and what changed between filings.
8. Governance and pay: change-in-control payments, single-trigger vesting, bonus metrics versus results, related party transactions.
9. Changes between filings and outlook: what was added, removed or reworded, what management stopped saying, and any guidance revision.

### news-media-analyst (News & Media API, `data/news/`)

1. Read every article in full and build a dated timeline.
2. Classify every claim as Fact, Allegation or Rumor, and give the company's response.
3. Short seller report: each allegation, the evidence offered, the company's response, and what would confirm or refute it.
4. Customer and competitor moves that could change Talonfield's revenue, especially a key customer building or buying its own capability.
5. Operational incidents (for example outages): customer impact and whether the company disclosed them formally.
6. Management and auditor changes, layoffs, guidance changes and share price reactions.
7. Industry context: market growth, market share, tariffs and supply chain costs.
8. Coverage of the sale process and of any litigation.
9. One line each for articles with no diligence relevance.

### litigation-analyst (Litigation Database, `data/litigation/`)

1. Read the docket index and every matter file.
2. For each matter: posture, latest change, next dates (flag anything before the November 6, 2026 IC meeting, the November 20, 2026 exclusivity expiry, or a likely closing), exposure (claimed, expert, settlement, caps), non-monetary risk (injunctions, product bans, customer effects) and trend. Cite docket entry dates.
3. Identify any matter that could enjoin a product, damage a key customer relationship or block closing.
4. List recent rulings and filings with exact dates, so the lead agent can test whether the company's SEC filings disclosed them.
5. Note insurance, indemnities or contractual caps where stated.
6. One line each for closed or minor matters.

### financial-analyst (Financial Analysis, `data/financials/`)

1. Read the README and all seven data files. Put a key metrics table (FY2023, FY2024, FY2025, H1 2026 or LTM) at the top.
2. Growth by segment, annual and quarterly. Find any quarter that breaks the trend, and how much growth depends on one quarter or one customer.
3. Margins: gross margin and Adjusted EBITDA margin trends, including H1 2026.
4. Earnings quality: add-backs as a share of Adjusted EBITDA, recurring "non-recurring" items, and add-backs that look like normal operating costs.
5. Working capital: DSO, allowance for credit losses as a share of gross receivables, contract assets and inventory.
6. Cash conversion: operating cash flow versus net income and EBITDA, and free cash flow.
7. Debt and liquidity: total and net debt, leverage on Adjusted EBITDA and on EBITDA, interest cover, revolver use and cash runway.
8. Customer concentration: top customer and top 10 share, and the change year over year.
9. KPIs: software ARR, retention, backlog and headcount. Do they support the reported growth?
10. Valuation check: recompute the deal brief's implied equity value, enterprise value and multiples. Test them against H1 2026 and LTM results, and say whether the management case still looks current.

### citation-verifier (Step 4)

Checks every Critical and High finding (including X- findings) and at least three Medium findings against the cited source. Up to four parallel runs if there are more than 20 findings.

## Lead agent tasks (Observe)

- Save each report unedited and add every finding to the register.
- Cross-source analysis: corroboration, conflicts, disclosure gaps and timing, numbers that only make sense combined, stale deal brief assumptions, and trends (three or more findings) merged into one X- finding.
- Keep `memory/open-questions.md` and `memory/datasets/key-metrics.md` current.

## Iteration budget

- At most 3 Act/Observe iterations.
- Iteration 1: all four analysts in parallel, with the task lists above.
- Iterations 2 and 3: narrow follow-ups only, sent to the analysts who can answer them, with any facts they need from other sources (cited). Loop only if a Critical or High question can still be answered from the available data.

## Stop conditions

- All six IC questions are answered with cited evidence, or
- The 3-iteration budget is used up.

Then: Checkpoint 2, verification, Checkpoint 3, report.

## Human checkpoints

| Checkpoint | When | Decision needed |
|---|---|---|
| 1 | After this plan | Approve the plan, or change it |
| 2 | After Act/Observe | Dig deeper on a topic, or proceed to verification |
| 3 | After verification | Approve the report, or change it |

## Progress

| Step | Status |
|---|---|
| Step 1: PLAN | Done. Approved at Checkpoint 1 |
| Step 2: ACT | Iteration 1 done (all four analysts). Iteration 2 done (SEC, financial, litigation follow-ups). Iteration 3 in reserve |
| Step 3: OBSERVE | Iterations 1 and 2 observed: 94 findings registered (including 13 X-). Waiting at Checkpoint 2 |

## Hypothesis status (after iteration 1)

| ID | Status | Key evidence |
|---|---|---|
| H1 | Supported | US$31.8 million Q4 2025 bill-and-hold; underlying FY2025 growth about 11.6% (X-01) |
| H2 | Supported | Guidance withdrawn August 6, 2026; price is 18.3x guidance midpoint and 15.1x LTM (X-04); add-backs 46.3% of LTM Adjusted EBITDA (X-06) |
| H3 | Supported (confirmed in iteration 2) | Vantor ruling and Norvale move appear missing from the August 6 10-Q; outage "not material" (X-03, X-08, X-09) |
| H4 | Supported | Norvale change-of-control exit right (X-02); change of control is a debt default (X-10); possible covenant breach (X-05); court dates near signing (X-12) |
| Step 4: VERIFY | Done: 68 checked, 47 Verified, 21 Partially verified, 0 Not supported. Approved at Checkpoint 3 |
| Step 5: REPORT | Done: output/ Markdown, HTML and PDF |
