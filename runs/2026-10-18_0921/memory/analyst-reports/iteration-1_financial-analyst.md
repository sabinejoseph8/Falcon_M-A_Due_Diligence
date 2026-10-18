# Iteration 1: financial-analyst report (unedited)

- Saved by the lead agent: 2026-10-18 02:31 EST
- Task: Financial analysis, iteration 1
- Subagent ID: aeb3b8f2d49f888ab
- The report below is the subagent's final message exactly as returned. Only the harness's hand-back line and its two-space line indent were removed.

---

## Financial analyst: findings

### Files reviewed

- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md (context only)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/README.md
- .../data/financials/income_statement.csv
- .../data/financials/revenue_quarterly.csv
- .../data/financials/balance_sheet.csv
- .../data/financials/cash_flow.csv
- .../data/financials/adjusted_ebitda_reconciliation.csv
- .../data/financials/revenue_by_customer.csv
- .../data/financials/kpis.csv

**Integrity checks:**
- No file contains embedded instructions. I searched the folder for instruction-like text and found none.
- All statements tie. The balance sheet balances in all four periods, and the cash flow reconciles to period-end cash.
- The FY2025 equity roll-forward ties: 74.3 + 18.6 NI + 17.2 SBC - 13.3 buybacks - 4.1 net share settlement taxes + 0.8 option proceeds = 93.5.
- The Adjusted EBITDA reconciliation ties to the income statement. Quarterly revenue sums to the annual and H1 totals.

**Source caveat:** the README says no quality of earnings report has been received yet.

### Key metrics table

US$ millions unless stated. Balance sheet items in the H1 2026 column are at June 30, 2026. LTM means the twelve months to Q2 2026, calculated as FY2025 - H1 2025 + H1 2026.

| Metric (reported, company basis) | FY2023 | FY2024 | FY2025 | H1 2026 | LTM Q2 2026 |
|---|---|---|---|---|---|
| Total revenue | 368.9 | 421.7 | 502.3 | 222.6 | 498.4 |
| Revenue growth | 18.1% | 14.3% | 19.1% | -1.7% vs H1 2025 | 11.0% vs prior LTM 449.2 |
| Growth: Hardware / Software / Services | 15.1% / 29.1% / 16.7% | 11.0% / 25.9% / 11.6% | 15.1% / 27.1% / 23.4% | -12.9% / 14.6% / 14.4% | n/a |
| Gross margin | 40.1% | 40.8% | 41.1% | 38.0% (H1 2025: 40.8%) | 39.8% |
| Operating income | 21.3 | 28.8 | 37.3 | -3.7 | 20.3 |
| Net income | 11.5 | 15.2 | 18.6 | -8.9 | 4.4 |
| EBITDA (company reconciliation) | 42.2 | 52.3 | 64.1 | 10.4 | 48.2 |
| EBITDA margin | 11.4% | 12.4% | 12.8% | 4.7% | 9.7% |
| Adjusted EBITDA (company definition) | 60.4 | 74.8 | 98.8 | 29.9 | 89.7 |
| Adjusted EBITDA margin (company) | 16.4% | 17.7% | 19.7% | 13.4% (H1 2025: 17.2%) | 18.0% |
| Add-backs as % of Adjusted EBITDA | 30.1% | 30.1% | 35.1% | 65.2% | 46.3% |
| Operating cash flow (OCF) | 30.8 | 40.8 | 9.7 | -4.2 | -6.9 |
| Free cash flow (OCF - capex) | 16.2 | 24.6 | -10.1 | -13.0 | -26.4 |
| OCF / EBITDA | 73.0% | 78.0% | 15.1% | -40.4% | -14.3% |
| DSO, net receivables (days) | 60.4 | 63.5 | 86.4 | 85.4 (H1 annualized) | 76.3 |
| DSO incl. contract assets (days) | 68.4 | 72.4 | 104.3 | 101.4 (H1 annualized) | 90.6 |
| Allowance as % of gross receivables | 3.9% | 3.8% | 2.1% | 3.2% | n/a |
| Contract assets | 8.1 | 10.2 | 24.7 | 19.5 | n/a |
| Inventory / days inventory (DIO) | 55.2 / 91.2 | 63.9 / 93.4 | 71.3 / 87.9 | 84.0 / 111.1 (H1 annualized) | DIO 102.2 |
| Cash | 54.8 | 48.3 | 41.6 | 33.9 | n/a |
| Revolver drawn | 0.0 | 10.0 | 35.0 | 45.0 | n/a |
| Total debt (revolver + term loan) | 120.0 | 200.0 | 220.0 | 227.5 | n/a |
| Net debt | 65.2 | 151.7 | 178.4 | 193.6 | n/a |
| Net debt / company Adjusted EBITDA | 1.1x | 2.0x | 1.8x | n/a | 2.2x |
| Net debt / EBITDA | 1.5x | 2.9x | 2.8x | n/a | 4.0x |
| Total debt / EBITDA | 2.8x | 3.8x | 3.4x | n/a | 4.7x |
| EBITDA / interest expense | 5.7x | 5.3x | 4.7x | 1.3x | 3.2x |
| Top customer (Norvale) share | n/a | 28.0% | 31.1% | n/a | n/a |
| Top 10 customer share | n/a | 59.2% | 61.5% | n/a | n/a |
| FieldOS ARR (period end) | 86.0 | 109.5 | 139.2 | 146.8 | n/a |
| Software net revenue retention | 121% | 119% | 118% | 111% | n/a |
| Hardware order backlog | 142.0 | 168.0 | 131.0 | 118.0 | n/a |
| Implied hardware book-to-bill (my calculation) | n/a | 1.10x | 0.88x | 0.89x | n/a |
| Robots shipped (units) | 3,020 | 3,300 | 4,300 | 1,640 | n/a |
| Hardware revenue per robot shipped (US$ thousand) | 78.1 | 79.4 | 70.1 | 71.3 | n/a |
| Active customers | 212 | 248 | 276 | 281 | n/a |
| Full-time employees | 1,180 | 1,390 | 1,452 | 1,405 | n/a |
| **Analyst-adjusted (my figures, see FIN-04)** | | | | | |
| Analyst-adjusted EBITDA (SBC still added back) | 55.8 | 68.8 | 84.7 | 22.5 | 72.6 |
| Analyst-adjusted EBITDA margin | 15.1% | 16.3% | 16.9% | 10.1% | 14.6% |
| Analyst-adjusted EBITDA after SBC | 44.2 | 54.9 | 67.5 | 13.6 | 54.8 |
| FY2025 growth without the estimated Q4 2025 excess (FIN-01) | n/a | n/a | 14.0% | n/a | n/a |

### Findings

16 findings: 2 Critical (FIN-01, FIN-14), 8 High, 4 Medium, 2 Low.

#### FIN-01: Nearly half of FY2025 growth came from one quarter, and revenue fell in H1 2026
- **Finding:** Q4 2025 revenue jumped 32.4% year over year. That one quarter delivered 46.9% of FY2025's revenue growth. Revenue then fell in Q2 2026 and H1 2026. Without the Q4 spike, FY2025 growth was about 14.0%, not the reported 19.1%.
- **Evidence:**
  - Year-over-year growth by quarter:
    - Q1 2025: 108.9 / 96.2 - 1 = 13.2%
    - Q2 2025: 117.6 / 102.8 - 1 = 14.4%
    - Q3 2025: 121.4 / 106.1 - 1 = 14.4%
    - Q4 2025: 154.4 / 116.6 - 1 = 32.4%
    - Q1 2026: 109.7 / 108.9 - 1 = 0.7%
    - Q2 2026: 112.9 / 117.6 - 1 = -4.0%
  - Q4 versus Q3 uplift: 154.4 / 121.4 - 1 = 27.2% in 2025, against 116.6 / 106.1 - 1 = 9.9% in 2024. Q1 2026 versus Q4 2025: 109.7 / 154.4 - 1 = -29.0%.
  - Q4 share of the full year: 116.6 / 421.7 = 27.6% in FY2024, against 154.4 / 502.3 = 30.7% in FY2025.
  - Dependence on Q4: the Q4 increase was 154.4 - 116.6 = 37.8, out of total FY2025 growth of 502.3 - 421.7 = 80.6. 37.8 / 80.6 = 46.9%.
  - Q1 to Q3 2025 growth: 347.9 / 305.1 - 1 = 14.0%.
  - Normalized Q4 2025 at that 14.0% rate: 116.6 x 1.140 = 133.0, so the excess is 154.4 - 133.0 = 21.4. A second method uses the 2024 seasonal uplift: 121.4 x 1.099 = 133.4, giving an excess of 21.0.
  - Normalized FY2025: 502.3 - 21.4 = 480.9. Growth = 480.9 / 421.7 - 1 = 14.0%.
  - H1 2026 by segment: hardware 116.9 / 134.2 - 1 = -12.9%; software +14.6%; services +14.4%. Total -3.9 = -17.3 hardware + 8.6 software + 4.8 services.
  - Hardware drove the H2 2025 jump. H2 2025 hardware was 301.4 - 134.2 = 167.2, up 33.0 on H1 2025. That is 66.9% of the 49.3 increase in total revenue from H1 to H2 2025.
  - The same pattern shows in other data: receivables rose 45.5 and contract assets 14.5 (FIN-06), backlog fell 37.0 (FIN-12), revenue per robot fell (FIN-02), and the "customer implementation delays" add-back was 3.3 in H2 2025 (FIN-04).
  - Reported versus adjusted: reported FY2025 growth is 19.1%; my normalized figure is 14.0%.
- **Source:**
  - `data/financials/revenue_quarterly.csv`, lines 2 to 11
  - `data/financials/income_statement.csv`, lines 2 to 5 (FY2024, FY2025, H1_2025, H1_2026)
  - `data/financials/adjusted_ebitda_reconciliation.csv`, line 17
- **Severity:** Critical
- **Confidence:** High for the calculations. Medium for reading the 21.4 as a pull-forward or one-off, because the pack has no quarterly segment or customer data.
- **Deal impact:** Valuation, because it inflates the FY2025 base and the growth path behind the US$560.0 million case. Closing risk if revenue recognition is challenged.
- **Cross-check:**
  - FY2025 10-K MD&A explanation of Q4, and the revenue recognition policy (bill-and-hold, customer acceptance, shipping terms).
  - Q1 and Q2 2026 10-Q commentary, and Q4 2025 and Q1 2026 earnings 8-Ks.
  - News of large Q4 2025 orders, especially from Norvale, and of returns or delayed deployments.
  - Court records for any securities class action or SEC inquiry about revenue timing.

#### FIN-02: Hardware revenue per robot fell 11.7% in FY2025 while units rose 30.3%
- **Finding:** FY2025 hardware volume growth appears to have been bought with lower prices or a weaker mix. That fits a year-end volume push.
- **Evidence:**
  - Hardware revenue per robot shipped (US$ thousand): 236.0 / 3,020 = 78.1; 261.9 / 3,300 = 79.4; 301.4 / 4,300 = 70.1; H1 2026 116.9 / 1,640 = 71.3.
  - FY2025 change: 70.1 / 79.4 - 1 = -11.7%.
  - Units grew 1,000 / 3,300 = 30.3%, while hardware revenue grew only 15.1%.
  - Caveat: hardware revenue may include items other than robots, and revenue timing can differ from shipment timing.
- **Source:** `data/financials/kpis.csv`, line 4; `data/financials/income_statement.csv`, line 2
- **Severity:** Medium
- **Confidence:** Medium, because it assumes hardware revenue is mostly robots.
- **Deal impact:** Valuation, through hardware pricing power and the margin outlook.
- **Cross-check:** 10-K price and volume discussion. News on price competition or volume deals, for example with Norvale.

#### FIN-03: Margins compressed sharply in H1 2026 and the company swung to a loss
- **Finding:** Gross margin fell 2.8 points in H1 2026. Company Adjusted EBITDA fell 23.3% and EBITDA fell 60.5%. Operating income turned negative.
- **Evidence:**
  - Gross margin: 147.9 / 368.9 = 40.1%; 172.1 / 421.7 = 40.8%; 206.3 / 502.3 = 41.1%; H1 2025 92.4 / 226.5 = 40.8%; H1 2026 84.6 / 222.6 = 38.0%.
  - Gross margin fell even though the revenue mix moved toward software and services. Their share rose from 92.3 / 226.5 = 40.8% to 105.7 / 222.6 = 47.5%. Segment margins are not in the pack.
  - Cost of revenue rose 138.0 / 134.1 - 1 = 2.9%, while revenue fell 1.7%.
  - Operating expenses rose 88.3 / 79.1 - 1 = 11.6%. Within that, G&A rose 19.8 / 16.2 - 1 = 22.2%. G&A had already risen 36.4 / 28.8 - 1 = 26.4% in FY2025.
  - Operating income went from 13.3 to -3.7. Net income went from 5.3 to -8.9.
  - Company Adjusted EBITDA: 29.9 / 39.0 - 1 = -23.3%, with the margin down from 17.2% to 13.4%.
  - EBITDA: 10.4 / 26.3 - 1 = -60.5%, with the margin down from 11.6% to 4.7%.
- **Source:**
  - `data/financials/income_statement.csv`, lines 2 to 18
  - `data/financials/adjusted_ebitda_reconciliation.csv`, lines 7, 11 and 12
- **Severity:** High
- **Confidence:** High. Calculated directly.
- **Deal impact:** Valuation and post-closing integration plan.
- **Cross-check:** Q1 and Q2 2026 10-Q MD&A on gross margin drivers (component costs, tariffs, warranty, pricing, under-absorbed factory costs). News on competitive pricing.

#### FIN-04: Add-backs reached 65.2% of H1 2026 Adjusted EBITDA, and several "non-recurring" items recur
- **Finding:** Company Adjusted EBITDA depends more and more on add-backs. Restructuring, patent litigation and implementation delay costs recur or look like normal operating costs. On my basis, LTM EBITDA is 72.6, not the company's 89.7, which is 19.1% lower.
- **Evidence:**
  - Add-backs (company Adjusted EBITDA minus EBITDA), and their share of company Adjusted EBITDA:
    - FY2023: 60.4 - 42.2 = 18.2, or 30.1%
    - FY2024: 74.8 - 52.3 = 22.5, or 30.1%
    - FY2025: 98.8 - 64.1 = 34.7, or 35.1%
    - H1 2026: 29.9 - 10.4 = 19.5, or 65.2%
    - LTM: 89.7 - 48.2 = 41.5, or 46.3%
  - Restructuring is added back in every period: 3.1, 4.6, 5.2, 7.9, then 4.4 in H1 2026. That totals 25.2 since FY2022.
  - Vantor patent litigation costs: 0.8 in FY2024, 2.1 in FY2025 and 3.0 in H1 2026. The H1 2026 figure alone is higher than the whole of FY2025.
  - "Customer implementation delays" was 4.1 in FY2025: 0.8 in H1 and 3.3 in H2. This reads like a delivery cost.
  - CFO search costs appear in two periods: 1.1 in FY2025 and 1.4 in H1 2026.
  - Stock-based compensation (SBC): 17.2 in FY2025, which is 17.4% of company Adjusted EBITDA. In H1 2026 it was 8.9, which is 29.8% of company Adjusted EBITDA and 4.0% of revenue. In FY2025 the company spent 13.3 on buybacks and 4.1 on net share settlement taxes, a total of 17.4. That is about the same as SBC, so SBC behaves like a cash cost.
  - My adjusted EBITDA removes restructuring, implementation delays and Vantor litigation costs. It keeps the SBC add-back and the genuine one-offs (offering costs, ERP, Lumora deal costs, auditor transition, CFO search, cyber response).
    - FY2025: 98.8 - 7.9 - 4.1 - 2.1 = 84.7
    - H1 2026: 29.9 - 4.4 - 3.0 = 22.5
    - LTM: 89.7 - 9.7 - 3.3 - 4.1 = 72.6, a 14.6% margin
    - Difference from the company's LTM figure: 17.1 / 89.7 = 19.1%
    - After also treating SBC as a cost: FY2025 67.5; LTM 72.6 - 17.8 = 54.8
- **Source:**
  - `data/financials/adjusted_ebitda_reconciliation.csv`, lines 7 to 20, all columns
  - `data/financials/income_statement.csv`, lines 11 and 22
  - `data/financials/cash_flow.csv`, lines 17 and 18
- **Severity:** High
- **Confidence:** Medium. Which items count as ordinary costs is a judgment. The arithmetic is High confidence.
- **Deal impact:** Valuation (the EBITDA used for the multiple) and financing (lender EBITDA definitions).
- **Cross-check:**
  - Non-GAAP reconciliations in 8-K earnings releases, and any SEC comment letters on non-GAAP measures.
  - The 10-K restructuring note, to see whether these are multi-year programs.
  - The Vantor court docket.
  - The credit agreement EBITDA definition and its add-back caps.

#### FIN-05: Add-back labels show an auditor change, a CFO change, a cyber incident and growing patent litigation
- **Finding:** Within about 18 months the add-backs record four events: an auditor transition (2.3, FY2025), a CFO transition (2.5 across FY2025 and H1 2026), a cybersecurity incident (1.8, H1 2026) and rising Vantor patent litigation (5.9 in total). The auditor and CFO changes overlap with the Q4 2025 revenue and receivables pattern.
- **Evidence:**
  - Auditor transition: 2.3 in FY2025.
  - Executive search and CFO transition: 1.1 + 1.4 = 2.5.
  - Cybersecurity incident response: 1.8 in H1 2026.
  - Vantor litigation: 0.8 + 2.1 + 3.0 = 5.9.
  - The balance sheet has no separate litigation reserve line, and accrued liabilities fell from 38.5 to 30.5. I cannot tell whether any Vantor liability has been accrued.
- **Source:**
  - `data/financials/adjusted_ebitda_reconciliation.csv`, lines 16, 18, 19 and 20
  - `data/financials/balance_sheet.csv`, line 13
- **Severity:** High
- **Confidence:** Medium. The costs are in company data, but what they mean is inferred from the labels only.
- **Deal impact:** Closing risk, post-closing internal controls, indemnity or R&W insurance scope, and valuation if a restatement occurs.
- **Cross-check:**
  - SEC 8-K Item 4.01 for the auditor change, including any disagreements or reportable events.
  - 8-K Item 5.02 for the CFO departure.
  - 8-K Item 1.05 for the cyber incident, comparing filing timing with the date of discovery.
  - 10-K Item 9A for any material weakness.
  - The Vantor docket: damages sought, injunction risk and trial date.
  - News coverage of the CFO exit and the cyber incident.

#### FIN-06: Receivables and contract assets ballooned at FY2025 year end, while the credit reserve ratio was cut
- **Finding:** DSO rose from 63.5 to 86.4 days in FY2025, and to 104.3 days including contract assets. The allowance for credit losses fell from 3.8% to 2.1% of gross receivables. Both point to revenue booked ahead of cash. The allowance was raised back to 3.2% in H1 2026.
- **Evidence:**
  - DSO (net receivables / revenue x 365):
    - FY2023: 61.0 / 368.9 x 365 = 60.4
    - FY2024: 73.4 / 421.7 x 365 = 63.5
    - FY2025: 118.9 / 502.3 x 365 = 86.4
    - June 30, 2026: 104.2 / 498.4 (LTM) x 365 = 76.3, or 104.2 / 445.2 (H1 annualized) x 365 = 85.4
  - The rise is not only a big-Q4 effect. On Q4 annualized revenue, DSO still rose from 73.4 / 466.4 x 365 = 57.4 to 118.9 / 617.6 x 365 = 70.3.
  - Including contract assets:
    - FY2023: 69.1 / 368.9 x 365 = 68.4
    - FY2024: 83.6 / 421.7 x 365 = 72.4
    - FY2025: 143.6 / 502.3 x 365 = 104.3
    - LTM: 123.7 / 498.4 x 365 = 90.6
  - In FY2025, receivables rose 45.5 / 73.4 = 62.0% and contract assets rose 14.5 / 10.2 = 142.2%, against revenue growth of 19.1%. The combined increase of 60.0 is larger than the 37.8 Q4 revenue increase.
  - Allowance as a share of gross receivables: 2.5 / 63.5 = 3.9%; 2.9 / 76.3 = 3.8%; 2.6 / 121.5 = 2.1%; 3.4 / 107.6 = 3.2%.
  - At the FY2024 ratio, the FY2025 allowance would have been 121.5 x 3.8% = 4.6, against 2.6 booked. That is about 2.0 less reserve, which could have flattered FY2025 pre-tax income by up to 2.0.
  - In H1 2026 the allowance rose by 0.8 even though gross receivables fell by 13.9. That suggests specific credit concerns.
  - H1 2026 collections: receivables fell 14.7 and contract assets fell 5.2.
- **Source:**
  - `data/financials/balance_sheet.csv`, lines 3, 4, 22 and 23
  - `data/financials/income_statement.csv`, line 5
  - `data/financials/revenue_quarterly.csv`, lines 5 and 9
  - `data/financials/cash_flow.csv`, lines 6 and 7
- **Severity:** High
- **Confidence:** High for the calculations. Medium for the revenue recognition interpretation.
- **Deal impact:** Valuation (revenue quality), working capital and net debt at closing, and restatement risk.
- **Cross-check:**
  - 10-K and 10-Q receivables aging, the allowance roll-forward, contract asset disclosures and any bill-and-hold policy.
  - Critical audit matters in the new auditor's report.
  - News on customer distress, and court records of collection suits.

#### FIN-07: Inventory built up while hardware sales and backlog fell
- **Finding:** Inventory rose 17.8% in H1 2026. Over the same period hardware revenue fell 12.9% and backlog fell 9.9%. Days inventory rose above 100.
- **Evidence:**
  - Inventory: 84.0 / 71.3 - 1 = 17.8%.
  - DIO (inventory / cost of revenue x 365):
    - FY2023: 55.2 / 221.0 x 365 = 91.2
    - FY2024: 63.9 / 249.6 x 365 = 93.4
    - FY2025: 71.3 / 296.0 x 365 = 87.9
    - June 30, 2026: 84.0 / 299.9 (LTM) x 365 = 102.2, or 84.0 / 276.0 (H1 annualized) x 365 = 111.1
  - Inventory / backlog: 0.39, 0.38, 0.54 (71.3 / 131.0), then 0.71 (84.0 / 118.0).
  - No inventory reserve is disclosed.
- **Source:**
  - `data/financials/balance_sheet.csv`, line 5
  - `data/financials/income_statement.csv`, line 6
  - `data/financials/kpis.csv`, line 6
  - `data/financials/cash_flow.csv`, line 8
- **Severity:** Medium
- **Confidence:** High for the calculations. Medium for the obsolescence risk.
- **Deal impact:** Valuation (possible write-down), working capital peg and cash.
- **Cross-check:** The 10-Q inventory note (mix and excess and obsolete reserve). News of a new Talon model or supply chain problems.

#### FIN-08: Cash conversion collapsed and free cash flow has been negative for 18 months
- **Finding:** OCF fell from 78.0% of EBITDA in FY2024 to 15.1% in FY2025, and was negative in H1 2026. LTM free cash flow is -26.4.
- **Evidence:**
  - OCF / net income: 30.8 / 11.5 = 2.68x; 40.8 / 15.2 = 2.68x; 9.7 / 18.6 = 0.52x. H1 2026 OCF was -4.2 on a net loss of 8.9.
  - OCF / EBITDA: 73.0%, 78.0%, 9.7 / 64.1 = 15.1%. H1 2026: -4.2 / 10.4 = -40.4%. LTM: -6.9 / 48.2 = -14.3%.
  - OCF / company Adjusted EBITDA: 51.0%, 54.5%, 9.8%. LTM: -6.9 / 89.7 = -7.7%.
  - Free cash flow: 16.2, 24.6, -10.1. H1 2026: -13.0. LTM: -10.1 - 3.3 + (-13.0) = -26.4.
  - FY2025 working capital outflow was 51.7, made up of receivables -45.5, contract assets -14.5, inventory -7.4 and payables and other +15.7. Of that, 38.0 fell in H2 2025 (51.7 - 13.7), and H2 2025 OCF was 9.7 - 12.4 = -2.7.
  - H1 2026 working capital outflow was 15.4. Receivables (+14.7) and contract assets (+5.2) were inflows. Inventory (-12.7) and payables and accruals (-22.6) were outflows.
- **Source:**
  - `data/financials/cash_flow.csv`, lines 2 to 12 and 24
  - `data/financials/adjusted_ebitda_reconciliation.csv`, lines 7 and 11
- **Severity:** High
- **Confidence:** High. Calculated directly.
- **Deal impact:** Valuation, financing (Arbelion funds the cash burn) and post-closing.
- **Cross-check:** The liquidity section and risk factors in the 10-Q. News on supplier payment problems.

#### FIN-09: Leverage is 4.0x to 4.7x on reported EBITDA, interest cover is thin, and the revolver is funding the cash burn
- **Finding:** Net debt rose to 193.6. Leverage looks moderate on company Adjusted EBITDA (2.2x) but high on EBITDA (4.0x net, 4.7x total). H1 2026 EBITDA covered interest only 1.3x. Cash alone lasts about 11.5 months without more revolver draws.
- **Evidence:**
  - Net debt: 120.0 - 54.8 = 65.2; 200.0 - 48.3 = 151.7; 220.0 - 41.6 = 178.4; 227.5 - 33.9 = 193.6.
  - LTM leverage:
    - Net debt / company Adjusted EBITDA: 193.6 / 89.7 = 2.2x
    - Net debt / EBITDA: 193.6 / 48.2 = 4.0x
    - Total debt / EBITDA: 227.5 / 48.2 = 4.7x
    - On my adjusted 72.6: 2.7x net, 3.1x total
  - EBITDA / interest: 5.7x, 5.3x, 4.7x. H1 2026: 10.4 / 7.9 = 1.3x. LTM: 48.2 / 14.9 = 3.2x.
  - Operating income / interest: LTM 20.3 / 14.9 = 1.4x. H1 2026 was negative.
  - Implied interest rate: 9.8 / 160.0 = 6.1% in FY2024; 13.6 / 210.0 = 6.5% in FY2025; 15.8 / 223.75 = 7.1% annualized in H1 2026.
  - The revolver went 0.0, 10.0, 35.0, 45.0. All 25.0 of the FY2025 draw came in H2 2025, because the H1 2025 revolver line is 0.0.
  - Cash runway: H1 2026 outflows before revolver draws were 13.0 free cash flow + 2.5 term loan + 1.5 share settlement taxes + 0.7 finance lease and other = 17.7, or 2.95 per month. 33.9 / 2.95 = 11.5 months.
  - Net debt rose 15.2 in H1 2026. If H2 2026 repeats that, net debt reaches about 208.8 by December 31, 2026. Because the offer is a fixed price per share, Arbelion would absorb that through a higher EV.
- **Source:**
  - `data/financials/balance_sheet.csv`, lines 2, 16 and 17
  - `data/financials/cash_flow.csv`, lines 11 to 21
  - `data/financials/income_statement.csv`, lines 13 and 14
  - `data/financials/adjusted_ebitda_reconciliation.csv`, lines 7 and 11
- **Severity:** High
- **Confidence:** High for the ratios. Medium for the runway, which is extrapolated and does not know the revolver size.
- **Deal impact:** Financing (refinancing at closing, change-of-control clauses), closing risk (a covenant breach before closing) and valuation (net debt at closing).
- **Cross-check:**
  - The credit agreement and any amendments or waivers (8-K Items 1.01 and 2.03, plus 10-K exhibits).
  - Covenant definitions, EBITDA add-back caps, revolver commitment, maturities and pricing grid.
  - The lead agent should send me the covenant definitions so I can test headroom.

#### FIN-10: Share buybacks were funded with debt while free cash flow was negative
- **Finding:** Over FY2023 to FY2025 the company spent 65.3 net on buybacks and net share settlement, against free cash flow of 30.7. In H2 2025 it bought back 7.3 of stock while OCF was negative and it drew 25.0 on the revolver.
- **Evidence:**
  - Buybacks: 20.0 + 25.0 + 13.3 = 58.3. Plus share settlement taxes of 10.4, less option proceeds of 3.4, gives 65.3 net.
  - Free cash flow over the same years: 16.2 + 24.6 - 10.1 = 30.7. Shortfall: 34.6.
  - H2 2025 buybacks: 13.3 - 6.0 = 7.3.
  - Cash was held almost flat, at 41.5 on June 30, 2025 and 41.6 on December 31, 2025.
  - Diluted shares still rose from 45.2 to 48.3, an increase of 6.9%.
- **Source:**
  - `data/financials/cash_flow.csv`, lines 16 to 19 and 22 to 24
  - `data/financials/income_statement.csv`, line 19
- **Severity:** Medium
- **Confidence:** High. Calculated directly.
- **Deal impact:** Governance (IC question 5) and interim operating covenants (no buybacks before closing).
- **Cross-check:** Board buyback authorizations (8-K and proxy). Form 4 insider sales during H2 2025.

#### FIN-11: Norvale is 31.1% of revenue and explains 47.3% of FY2025 growth
- **Finding:** Concentration rose, and all of the increase came from Norvale. Revenue excluding Norvale grew 14.0%, the same as the Q1 to Q3 2025 rate. Norvale's 38.1 increase almost equals the 37.8 Q4 spike. That is consistent with Norvale driving Q4 2025, but it does not prove it.
- **Evidence:**
  - Norvale share: 118.1 / 421.7 = 28.0% in FY2024; 156.2 / 502.3 = 31.1% in FY2025. Growth: 38.1 / 118.1 = 32.3%.
  - Norvale's share of total FY2025 growth: 38.1 / 80.6 = 47.3%.
  - Revenue excluding Norvale: 346.1 / 303.6 - 1 = 14.0%.
  - Top 10 customers: 249.6, or 59.2%, then 308.8, or 61.5%. Customers 2 to 10 actually fell, from 131.5 / 421.7 = 31.2% to 152.6 / 502.3 = 30.4%. Top 3: 226.3 / 502.3 = 45.1%.
  - Illustration only: if Norvale carries the average gross margin, losing it would cost about 156.2 x 41.1% = 64.2 of gross profit. That is more than LTM EBITDA of 48.2.
  - The pack has no H1 2026 customer data.
- **Source:**
  - `data/financials/revenue_by_customer.csv`, lines 2 to 13
  - `data/financials/revenue_quarterly.csv`, lines 2 to 9
- **Severity:** High. Raise to Critical if news or litigation show the Norvale relationship is at risk.
- **Confidence:** High for the calculations. Medium for the link to Q4 2025.
- **Deal impact:** Valuation, post-closing risk, and a possible closing condition (customer consent or change-of-control terms).
- **Cross-check:**
  - 10-K major customer disclosures and risk factors.
  - Norvale contract terms: renewal date, termination for convenience, change of control.
  - News on Norvale's vendor choices and financial health.
  - Court records for any Norvale v. Talonfield dispute.

#### FIN-12: Leading indicators contradict the reported growth: backlog, retention, new ARR, customers and headcount all weakened
- **Finding:** Hardware backlog is down 29.8% from its peak. Implied hardware book-to-bill has been below 1.0x since FY2025. Retention fell 7 points in six months. Net new ARR slowed to about half its FY2025 pace. Customer growth nearly stopped and headcount fell.
- **Evidence:**
  - Backlog: 142.0, 168.0, 131.0 (-22.0%), 118.0 (-9.9%). Down 50.0 / 168.0 = 29.8% from the peak.
  - Implied hardware orders (hardware revenue + change in backlog):
    - FY2024: 261.9 + 26.0 = 287.9, a 1.10x book-to-bill
    - FY2025: 301.4 - 37.0 = 264.4, a 0.88x book-to-bill
    - H1 2026: 116.9 - 13.0 = 103.9, a 0.89x book-to-bill
    - FY2025 orders fell 8.2% while hardware revenue grew 15.1%.
  - Net revenue retention: 121%, 119%, 118%, 111%.
  - Net new ARR: 23.5 in FY2024; 29.7 in FY2025; 7.6 in H1 2026, which annualizes to 15.2, or 51.2% of the FY2025 pace.
  - Active customers: +17.0%, +11.3%, then +1.8% in H1 2026 (5 / 276).
  - Employees: +17.8%, +4.5%, then -3.2% in H1 2026 (-47).
- **Source:** `data/financials/kpis.csv`, lines 2, 3, 6, 7 and 8; `data/financials/income_statement.csv`, line 2
- **Severity:** High
- **Confidence:** High for the KPIs. Medium for implied orders, which assume backlog covers hardware only and has no cancellations.
- **Deal impact:** Valuation (forecast credibility).
- **Cross-check:** Backlog definition and cancellations in the 10-K and 10-Q. The March 2026 investor day deck. News on lost deals or customers pausing spending. WARN notices for the headcount cuts.

#### FIN-13: Software revenue fell behind ARR in H1 2026, and deferred revenue fell
- **Finding:** Software revenue used to run about 3.4% to 3.5% above average ARR. In H1 2026 it ran 5.6% below. H1 2026 software revenue was lower than H2 2025, even though ARR rose. Deferred revenue fell 11.8%. ARR may include subscriptions that are contracted but not yet live, or its definition may have changed.
- **Evidence:**
  - Software revenue / average ARR:
    - FY2024: 101.2 / 97.75 = 1.035
    - FY2025: 128.6 / 124.35 = 1.034
    - H1 2026: 135.0 (67.5 x 2) / 143.0 = 0.944
  - H1 2026 software revenue of 67.5 was below H2 2025's 69.7 (128.6 - 58.9), a fall of 3.2%. Over the same period ARR rose 5.5%.
  - Deferred revenue (current + non-current): 38.1, 48.0, 56.9, then 50.2, down 6.7 / 56.9 = 11.8%.
  - Caveat: deferred revenue may be seasonal, and the pack has no June 30, 2025 balance sheet to compare against.
- **Source:**
  - `data/financials/kpis.csv`, line 2
  - `data/financials/income_statement.csv`, line 3
  - `data/financials/balance_sheet.csv`, lines 14 and 15
- **Severity:** Medium
- **Confidence:** Medium. The interpretation depends on the ARR definition.
- **Deal impact:** Valuation, because the software growth story is the core of the premium.
- **Cross-check:** The ARR definition in the 10-K and investor day deck, and any change to it. SEC comment letters on KPIs.

#### FIN-14: The deal model's management case is stale. On current results the offer is 15.1x LTM Adjusted EBITDA, not 11.5x
- **Finding:** The brief's mechanics recompute correctly, but the inputs no longer hold. Reaching the US$118.0 million case would need H2 2026 Adjusted EBITDA up 47.3% year over year. At the model's own 11.5x on LTM, the shares are worth about US$17.35, below the unaffected price of US$17.85.
- **Evidence:**
  - Brief recompute:
    - Equity value: 24.00 x 48.3 = 1,159.2
    - Premium: 24.00 / 17.85 - 1 = 34.5%
    - Net debt at June 30, 2026: 193.6
    - EV: 1,352.8
    - EV / FY2026E Adjusted EBITDA of 118.0: 11.5x
    - EV / FY2026E revenue of 560.0: 2.4x
  - EV against actual results:
    - FY2025 company Adjusted EBITDA (98.8): 13.7x
    - LTM company Adjusted EBITDA (89.7): 15.1x
    - H1 2026 annualized Adjusted EBITDA (59.8): 22.6x
    - LTM analyst-adjusted EBITDA (72.6): 18.6x
    - LTM EBITDA (48.2): 28.1x
    - LTM revenue: 2.7x
  - What the case needs in H2 2026:
    - Revenue: 560.0 - 222.6 = 337.4. That is up 22.3% on H2 2025 (275.8) and averages 168.7 a quarter, above the record Q4 2025 of 154.4.
    - Adjusted EBITDA: 118.0 - 29.9 = 88.1. That is up 47.3% on H2 2025 (59.8), at a 26.1% margin, against 21.7% in H2 2025 and 13.4% in H1 2026.
  - Hardware test. Assumption: software and services grow at their H1 2026 rates for FY2026, giving 147.4 and 82.7. Implied hardware is 329.9, which needs 213.0 in H2 2026, up 27.4% on 167.2. June 30 backlog of 118.0 covers only 55.4% of that.
  - At 11.5x:
    - LTM company Adjusted EBITDA: 89.7 x 11.5 = 1,031.6 EV; less 193.6 net debt = 838.0 equity; / 48.3 = US$17.35 per share, 27.7% below the offer.
    - LTM analyst-adjusted EBITDA: 72.6 x 11.5 = 834.9 EV; 641.3 equity; US$13.28 per share, 44.7% below the offer.
  - Sensitivity: each 1.0 of EBITDA is worth 11.5 of EV, or US$0.24 per share. The gap from 118.0 to 89.7 is 28.3. 28.3 x 11.5 = 325.5 of EV, or US$6.74 per share, which is 24.1% of the deal EV.
  - Synergies of 35.0 equal 39.0% of LTM company Adjusted EBITDA and 34.9% of LTM sales, marketing and G&A (100.4). EV / (89.7 + 35.0) = 10.8x, so the price already pays away most of the synergies.
  - EV bridge gaps:
    - Net debt excludes finance leases (0.7 paid in H1 2026), any litigation accrual, restructuring accruals, transaction costs and change-of-control payments.
    - It also excludes the cash burn until closing.
    - Q3 2026 ended on September 30 but is not in the pack.
- **Source:**
  - `data/deal-brief.md`, "The deal" and "Valuation basis"
  - `data/financials/adjusted_ebitda_reconciliation.csv`, lines 7 and 11
  - `data/financials/balance_sheet.csv`, lines 2, 16 and 17
  - `data/financials/income_statement.csv`, lines 2 to 5, 9 and 10
  - `data/financials/kpis.csv`, line 6
- **Severity:** Critical. The value gap is above 10% on every measure.
- **Confidence:** High for the math. Medium for the scenarios and forecasts.
- **Deal impact:** Valuation and price, and the IC decision.
- **Cross-check:**
  - The March 2026 investor day deck, and any guidance change in the Q1 and Q2 2026 earnings 8-Ks.
  - Q3 2026 results.
  - News on guidance cuts or analyst consensus.

#### FIN-15: Goodwill from the Lumora deal and negative tangible equity
- **Finding:** Lumora added 57.4 of goodwill, bought for 85.0 cash and largely debt-funded. Tangible equity has been negative since FY2024. The H1 2026 losses raise the risk of a reporting-unit impairment.
- **Evidence:**
  - Goodwill went from 41.0 to 98.4. Lumora consideration was 85.0, and the term loan rose 70.0.
  - Tangible equity: 71.3 - 41.0 - 21.1 = 9.2; then -67.5; then -42.1; at June 30, 2026, 92.0 - 98.4 - 34.1 = -40.5.
  - Market capitalization at US$17.85 is 862.2, well above book equity, so an impairment trigger at company level is unlikely.
- **Source:**
  - `data/financials/balance_sheet.csv`, lines 8, 9, 17 and 20
  - `data/financials/cash_flow.csv`, lines 13 and 15
- **Severity:** Low
- **Confidence:** Medium
- **Deal impact:** Post-closing (purchase price allocation, impairment).
- **Cross-check:** The 10-K goodwill note, the Lumora purchase price allocation, and Lumora's performance against its acquisition case.

#### FIN-16: Reported D&A is higher than the asset roll-forward supports
- **Finding:** D&A exceeds what the fixed asset and intangible movements imply, by 5.7 in FY2025 and 3.3 in H1 2026. If D&A includes amortization of costs that are really operating costs, EBITDA is flattered.
- **Evidence:**
  - FY2025 implied D&A = capex 19.8 - net change in (PP&E + intangibles) of (4.9 - 6.2) = 21.1, against 26.8 reported.
  - H1 2026 implied D&A = 8.8 - (1.1 - 3.1) = 10.8, against 14.1 reported.
  - Possible benign explanations: robots moved from inventory into PP&E, disposals, or amortization of capitalized contract costs.
- **Source:**
  - `data/financials/balance_sheet.csv`, lines 7 and 9
  - `data/financials/cash_flow.csv`, lines 3 and 12
- **Severity:** Low
- **Confidence:** Low. Directional only, because the pack has no roll-forward.
- **Deal impact:** Valuation (EBITDA definition).
- **Cross-check:** The 10-K PP&E and intangibles notes, the D&A breakdown and the capitalization policies.

### Positive or mitigating points

- **The statements are internally consistent.** All periods tie: balance sheet, cash flow, equity roll-forward and the EBITDA reconciliation.
- **Recurring revenue is still growing.** Software and services were 105.7 in H1 2026 against 92.3 in H1 2025, up 14.5%. Their share of revenue rose to 47.5%. Software alone grew 14.6%.
- **The software base is intact.** ARR is still growing (146.8) and retention is still above 100% (111%). The installed base grew 9.4% in H1 2026 to 19,040 robots, which supports future software and service revenue.
- **Some Q4 2025 receivables turned into cash.** Receivables fell 14.7 and contract assets 5.2 in H1 2026. This lowers, but does not remove, the revenue recognition concern. The allowance was also raised to 3.2%.
- **Leverage on the company's own Adjusted EBITDA is moderate** at 2.2x net. The term loan amortizes slowly (5.0 a year) and Arbelion would likely refinance it at closing.
- **The deal brief's mechanics are correct:** 1,159.2 equity value, 1,352.8 EV and 11.5x. Only the inputs are stale.
- **The H1 2026 restructuring may lower the cost base.** Headcount fell by 47.

### Gaps and questions for management

1. **Latest results and forecast.** Q3 2026 results, the current FY2026 forecast, and a bridge from the March 2026 investor day case to actual results.
2. **Q4 2025 revenue.** Quarterly revenue by segment and by customer, Q1 2024 to Q3 2026, including Norvale. The largest Q4 2025 transactions, and any bill-and-hold, side letters, extended terms or acceptance clauses.
3. **Norvale.** The contract terms (renewal, termination, change of control, volume commitments) and H1 2026 Norvale revenue.
4. **Receivables.** Receivables and contract asset aging at December 31, 2025 and June 30, 2026, the allowance roll-forward, specific reserves, and collections since June 30.
5. **Add-backs.**
   - Map each Adjusted EBITDA add-back to its income statement line.
   - Confirm there is no double counting between "Restructuring and other charges" and "Other non-recurring items".
   - Explain what "customer implementation delays" are, and whether any were credits against revenue.
   - Give the history of the restructuring programs.
6. **Credit agreement.** Covenant definitions and headroom, compliance certificates, revolver size and availability, maturities, pricing grid, change-of-control clause, and any amendments or waivers.
7. **Cash forecast.** A 13-week cash forecast and a forecast through closing, plus the minimum operating cash level.
8. **ARR and retention.**
   - The ARR definition and any changes to it.
   - An ARR bridge showing new, expansion, contraction and churn.
   - Gross retention.
   - Any ARR that is not yet live.
   - Whether the installed base counts retired robots. The base equals cumulative shipments exactly, which implies zero retirements.
9. **Backlog.** The backlog definition, cancellations, aging, and Q3 2026 bookings.
10. **Inventory.** Inventory mix, the excess and obsolete reserve, and any product transitions.
11. **Margins.** Segment gross margins and the drivers of the H1 2026 gross margin decline.
12. **Fixed assets and D&A.** Fixed asset and intangible roll-forwards, the D&A breakdown, capitalized software and contract costs, and any robots moved from inventory into PP&E.
13. **Governance events.** The reasons for the auditor change and any disagreements, the circumstances of the CFO departure, and the cyber incident's scope, cost, insurance cover and impact on operations.
14. **Vantor case.** Status, damages claimed, any reserve, possible royalty exposure, and the legal cost forecast.
15. **Buybacks.** The board's rationale for buying back stock in H2 2025 while drawing on the revolver.
16. **Share count and EV bridge.** The fully diluted share count at US$24.00, including acceleration on change of control. A list of debt-like items: finance leases, restructuring accruals, bonuses and transaction costs.
17. **Missing data.** The H1 2025 working capital detail (blank in `cash_flow.csv`, lines 6 to 9) and a June 30, 2025 balance sheet to test seasonality.
18. **Quality of earnings report.** Not yet received.
19. **Lumora.** Revenue contribution and goodwill impairment testing.
20. **Synergies.** The build-up of the US$35.0 million synergy estimate, and any overlap with savings from the H1 2026 restructuring.
