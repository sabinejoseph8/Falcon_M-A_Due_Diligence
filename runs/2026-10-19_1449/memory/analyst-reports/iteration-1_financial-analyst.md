## Financial analyst: findings

Target: Corvane Diagnostics (Project Kestrel). All figures are US$ millions unless stated. Only the files listed below were used. No source file contained any text that tried to instruct the agents, so there is no prompt-injection finding. The lead agent gave me no facts from other sources. The size and nature of the Q4 2025 one-off, the acquired lab's revenue and the credit agreement's "Consolidated EBITDA" definition are therefore estimated or listed as gaps.

### Files reviewed

- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/deal-brief.md` (context only)
- `.../targets/kestrel/data/financials/README.md`
- `.../targets/kestrel/data/financials/income_statement.csv`
- `.../targets/kestrel/data/financials/adjusted_ebitda_reconciliation.csv`
- `.../targets/kestrel/data/financials/balance_sheet.csv`
- `.../targets/kestrel/data/financials/cash_flow.csv`
- `.../targets/kestrel/data/financials/revenue_quarterly.csv`
- `.../targets/kestrel/data/financials/revenue_by_customer.csv`
- `.../targets/kestrel/data/financials/kpis.csv`

**Integrity checks (all tie):**
- Quarterly revenue sums to the annual and H1 totals: 2024 = 386.0, 2025 = 431.0, H1 2025 = 205.2, H1 2026 = 203.4.
- The EBITDA bridge recomputes for every period. For example, FY2025: 26.4 + 34.1 + 8.8 + 25.4 - 7.2 = 87.5, and 87.5 + 9.8 + 5.2 + 22.8 = 125.3.
- LTM Q2 2026 Adjusted EBITDA: 125.3 - 56.0 + 54.1 = 123.4.
- The "other non-recurring" detail sums to its total: FY2025 = 22.8, H1 2026 = 24.6, LTM = 37.4.
- The cash flow change in receivables matches the balance sheet: FY2025 (93.3 + 9.8) - (66.3 + 7.4) = 29.4.
- Revenue per accession recomputes: 314.8 / 1,705 = US$184.6.
- Deal brief arithmetic ties: 52.4 x 24.00 = 1,257.6, EV = 1,257.6 + 391.0 = 1,648.6, and 1,648.6 / 125.3 = 13.2x.

### Key metrics table

"Reported" means the company's own figures. "Diligence-adjusted" is my adjustment, defined in FIN-01. LTM Q2 2026 = FY2025 - H1 2025 + H1 2026.

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 | LTM Q2 2026 |
|---|---|---|---|---|---|
| Total revenue (reported) | 348.0 | 386.0 | 431.0 | 203.4 | 429.2 |
| Revenue growth YoY | 11.4% | 10.9% | 11.7% | -0.9% (vs H1 2025 205.2) | n/a |
| Clinical testing growth | 10.8% | 10.6% | 12.7% | -1.9% | n/a |
| Biopharma services growth | 13.4% | 13.0% | 9.8% | +2.7% | n/a |
| Lab informatics growth | 11.2% | 5.7% | 4.8% | -2.3% | n/a |
| Gross margin | 42.0% | 42.5% | 43.9% | 38.0% (H1 2025: 43.0%) | n/a |
| EBITDA (reported) | 59.6 | 71.7 | 87.5 | 19.6 | 68.1 |
| EBITDA margin | 17.1% | 18.6% | 20.3% | 9.6% | 15.9% |
| Adjusted EBITDA (company) | 82.4 | 99.9 | 125.3 | 54.1 | 123.4 |
| Adjusted EBITDA margin (company) | 23.7% | 25.9% | 29.1% | 26.6% | 28.8% |
| Add-backs as % of Adjusted EBITDA | 27.7% | 28.2% | 30.2% | 63.8% | 44.8% |
| **Diligence-adjusted EBITDA** | 67.6 | 81.5 | **101.2** | 37.3 | **93.5** |
| Diligence-adjusted margin | 19.4% | 21.1% | 23.5% | 18.3% | 21.8% |
| Net income | 4.3 | 10.7 | 26.4 | -8.9 | 10.1 |
| Operating cash flow | 27.5 | 32.1 | 28.4 | 7.8 | 22.4 |
| Free cash flow (OCF - capex) | 3.5 | 5.1 | -5.1 | -4.3 | -8.2 |
| OCF / EBITDA | 46.1% | 44.8% | 32.5% | 39.8% | 32.9% |
| OCF / Adjusted EBITDA | 33.4% | 32.1% | 22.7% | 14.4% | 18.2% |
| DSO, net AR (days) | 58.5 | 62.7 | 79.0 | 80.9 (annualized H1) | 76.7 |
| Price concession reserve, % gross AR | 22.4% | 24.3% | 25.1% | 26.7% | n/a |
| Initial claim denial rate | 8.9% | 10.7% | 13.4% | 16.2% | n/a |
| Total debt (revolver + term loan) | 400.0 | 405.9 | 421.8 | 424.7 | 424.7 |
| Net debt | 375.0 | 371.4 | 391.0 | 395.9 | 395.9 |
| Net debt / Adjusted EBITDA (company) | 4.55x | 3.72x | 3.12x | n/a | 3.21x |
| Net debt / EBITDA | 6.29x | 5.18x | 4.47x | n/a | 5.81x |
| EBITDA / interest | 1.76x | 2.06x | 2.57x | 1.11x | 1.96x |
| Top customer share (Medicare) | n/a | 24.0% | 24.2% | n/a | n/a |
| Top 10 share | n/a | 69.3% | 70.2% | n/a | n/a |
| Biopharma backlog | 182.0 | 214.5 | 246.0 | 231.4 (Jun 30) | n/a |
| Biopharma book-to-bill | 1.3 | 1.4 | 1.3 | 0.7 | n/a |
| Clinical volume (k accessions) | 1,420 | 1,560 | 1,705 | 812 | n/a |
| Revenue per accession (US$) | 177.9 | 179.1 | 184.6 | 179.8 | n/a |
| Informatics ARR | 15.6 | 16.6 | 17.4 | 17.0 | n/a |
| Headcount | 1,840 | 1,985 | 2,150 | 2,090 | n/a |

### Findings

#### FIN-01: About US$24 million of FY2025 add-backs recur every year; diligence-adjusted EBITDA is US$101.2 million (FY2025) and US$93.5 million (LTM Q2 2026)
- **Finding:** Four add-back categories appear in every year from FY2022 to H1 2026 and grow each year, so they are normal operating costs, not one-offs. These are payer denial write-offs, billing system transition costs, new lab start-up costs, and restructuring. Taking them out cuts FY2025 Adjusted EBITDA from 125.3 to 101.2 (-19.2%), and LTM from 123.4 to 93.5 (-24.2%). Add-backs rose from 30.2% of Adjusted EBITDA in FY2025 to 63.8% in H1 2026. Adjusted EBITDA also drives management bonuses (README).
- **Evidence:**
  - Add-backs by year:

    | Add-back | FY22 | FY23 | FY24 | FY25 | H1'26 | LTM | Assessment |
    |---|---|---|---|---|---|---|---|
    | Payer denial and recoupment write-offs | 4.2 | 5.9 | 7.8 | 10.6 | 7.4 | 13.1 | Recurring. A normal revenue-cycle cost for a lab. Disallow. |
    | Billing system transition | 2.5 | 3.1 | 3.6 | 4.4 | 2.6 | 5.0 | Five years and rising. Disallow. |
    | New lab start-up | 1.8 | 2.4 | 3.0 | 3.9 | 2.2 | 4.2 | Every year. A growth cost. Disallow. |
    | Restructuring and other charges | 2.1 | 3.4 | 4.0 | 5.2 | 4.6 | 7.6 | Every year. Disallow. |
    | Legal and regulatory response | 0.6 | 0.9 | 1.4 | 3.1 | 4.8 | 6.7 | Recurring baseline. Accepted in my base case, but see sensitivity. |
    | Cybersecurity incident | 0.0 | 0.0 | 0.0 | 0.0 | 6.1 | 6.1 | Genuine one-off. Accept, net of any insurance recovery. |
    | Transaction-related | 0.0 | 0.0 | 0.0 | 0.8 | 1.5 | 2.3 | Accept. |
    | Stock-based compensation | 6.0 | 7.1 | 8.4 | 9.8 | 5.3 | 10.3 | Market-standard add-back. Accepted. |

  - Diligence-adjusted EBITDA = EBITDA + SBC + legal + cyber + transaction:
    - FY2025 = 87.5 + 9.8 + 3.1 + 0.0 + 0.8 = **101.2**. Cross-check: 125.3 - 10.6 - 4.4 - 3.9 - 5.2 = 101.2.
    - LTM = 68.1 + 10.3 + 6.7 + 6.1 + 2.3 = **93.5**. Cross-check: 123.4 - 13.1 - 5.0 - 4.2 - 7.6 = 93.5.
    - H1 2026 = 19.6 + 5.3 + 4.8 + 6.1 + 1.5 = 37.3. H1 2025 = 39.0 + 4.8 + 1.2 = 45.0. Change: 37.3 / 45.0 - 1 = -17.1%.
  - Add-back share of Adjusted EBITDA:
    - FY2025: (9.8 + 5.2 + 22.8) / 125.3 = 37.8 / 125.3 = 30.2%
    - H1 2026: (5.3 + 4.6 + 24.6) / 54.1 = 34.5 / 54.1 = 63.8%
    - LTM: 55.3 / 123.4 = 44.8%
  - Sensitivities:
    - Minimum case, removing only the payer denial write-offs: FY2025 125.3 - 10.6 = 114.7, LTM 123.4 - 13.1 = 110.3.
    - Strict case, also removing legal costs and SBC: LTM 93.5 - 6.7 - 10.3 = 76.5.
- **Source:** `adjusted_ebitda_reconciliation.csv`, all rows. `income_statement.csv`, row "Restructuring and other charges". `README.md`, management note on bonuses.
- **Severity:** Critical. Test: changes value by more than 10%. At the deal's own 13.2x multiple, LTM 93.5 implies EV of 1,234.2, which is 414.4 (25.1%) below 1,648.6. Even the minimum case (110.3) gives 1,456.0, a gap of 192.6 or 11.7%.
- **Confidence:** High for the arithmetic and the recurrence pattern, which are taken directly from company data. Medium for which add-backs to disallow, which is a judgment.
- **Deal impact:** Valuation and financing (see FIN-02, FIN-06, FIN-07).
- **Cross-check:** In the 10-K and 10-Q, check the non-GAAP reconciliation and how "non-recurring" is described, any SEC comment letters on non-GAAP measures, and the proxy statement's bonus metric. Ask for the general ledger detail behind the denial write-offs: are they reductions to revenue, or bad debt in SG&A?

#### FIN-02: At US$24.00 the deal pays 16.3x FY2025 and 17.6x LTM diligence-adjusted EBITDA, not 13.2x
- **Finding:** The 13.2x headline multiple holds only on the company's FY2025 figure. On current trading and adjusted earnings the multiple is much higher. Holding 13.2x on LTM diligence-adjusted EBITDA implies about US$16.00 per share. That is below the July 31, 2026 close of US$18.10 cited in the brief.
- **Evidence:**
  - EV = 52.4 x 24.00 + 391.0 = 1,648.6.
  - Multiples on that EV:
    - LTM company: 1,648.6 / 123.4 = 13.4x
    - FY2025 diligence-adjusted: 1,648.6 / 101.2 = 16.3x
    - LTM diligence-adjusted: 1,648.6 / 93.5 = 17.6x
    - FY2025 EBITDA: 1,648.6 / 87.5 = 18.8x
    - LTM EBITDA: 1,648.6 / 68.1 = 24.2x
  - Price at a constant 13.2x on LTM diligence-adjusted EBITDA, using June 30, 2026 net debt: 13.2 x 93.5 = 1,234.2. Less 395.9 net debt = 838.3. Divided by 52.4 = US$16.00 per share.
  - Same test on FY2025 diligence-adjusted EBITDA: 13.2 x 101.2 = 1,335.8, less 391.0 = 944.8, divided by 52.4 = US$18.03 per share.
  - Premium check from the brief: 24.00 / 18.10 = 1.326, or a 32.6% premium.
- **Source:** `deal-brief.md`, section 2. `adjusted_ebitda_reconciliation.csv`. `balance_sheet.csv`, Q2_2026 column.
- **Severity:** Critical. Test: more than 10% of value. The EV gap is 414.4, or 25.1%.
- **Confidence:** Medium. The inputs are company data and the arithmetic is shown, but the result depends on the FIN-01 disallowance judgment and on holding the multiple constant.
- **Deal impact:** Valuation.
- **Cross-check:** Trading peers' multiples (news or filings), Corvane's share price since July 31, 2026, and analyst estimates for FY2026.

#### FIN-03: FY2025 growth of 11.7% depends on an abnormal Q4 2025; underlying growth is about 8% to 9% before stripping out the acquisition
- **Finding:** Q4 2025 revenue jumped to 120.5, which is +14.4% over Q3 and +19.4% over Q4 2024. Revenue then fell back to 102.6 in Q1 2026 and 100.8 in Q2 2026. The first nine months of 2025 grew only 8.9%. FY2025 also includes a lab acquisition (31.0 cash; labs went from 5 to 7), whose revenue is not disclosed. Organic growth is therefore below 8.9% by an unknown amount.
- **Evidence:**
  - 2025 growth by quarter, YoY: Q1 101.3 / 92.1 = +10.0%, Q2 103.9 / 95.4 = +8.9%, Q3 105.3 / 97.6 = +7.9%, Q4 120.5 / 100.9 = +19.4%. Growth was slowing each quarter until Q4.
  - 2026 growth, YoY: Q1 102.6 / 101.3 = +1.3%. Q2 100.8 / 103.9 = -3.0%.
  - First nine months: 2025 = 101.3 + 103.9 + 105.3 = 310.5. 2024 = 92.1 + 95.4 + 97.6 = 285.1. Growth 310.5 / 285.1 = +8.9%.
  - Estimated Q4 2025 excess (estimate):
    - (a) Sequential trend: (105.3 - 101.3) / 2 = 2.0 a quarter, so Q4 expected at 107.3 and excess = 120.5 - 107.3 = 13.2.
    - (b) Q3 YoY rate: 100.9 x 1.079 = 108.9, so excess = 11.6.
    - Range 11.6 to 13.2.
  - FY2025 excluding the excess: 431.0 - 13.2 = 417.8, and 417.8 / 386.0 = +8.2%. With the 11.6 estimate: 419.4 / 386.0 = +8.7%.
  - Price and mix: revenue per accession rose 3.1% in FY2025 (184.6 / 179.1), the year the denial rate rose from 10.7% to 13.4%. It then fell to 179.8 in H1 2026. FY2025 clinical revenue at the FY2024 rate = 179.1 x 1,705 = 305.4, which is 9.4 below the reported 314.8. This suggests (inference) that part of the spike was a collection-rate or reserve true-up in clinical testing.
  - Customer contribution: Veltrane added 12.5 (50.5 - 38.0). That is 27.8% of the 45.0 total revenue growth (12.5 / 45.0).
- **Source:** `revenue_quarterly.csv`, all rows. `income_statement.csv`, revenue rows. `kpis.csv`, rows 2 and 3. `cash_flow.csv`, row "Acquisition of business". `kpis.csv`, row "Labs in operation". `revenue_by_customer.csv`, row 2.
- **Severity:** High. It is material to price and to the deal thesis. It is not rated Critical because the one-off amount is estimated, not disclosed.
- **Confidence:** Medium. The quarterly figures are direct data, but the size of the excess is estimated.
- **Deal impact:** Valuation, and the stale thesis point "11.7% growth".
- **Cross-check:** Check the FY2025 10-K and Q4 earnings release for a one-time item, a change in the collection-rate estimate, or a milestone or catch-up payment (for example from Veltrane). Also check acquisition disclosures for the acquired revenue. The lead should send me any disclosed one-off amount so I can recompute.

#### FIN-04: H1 2026 shows broad deterioration: revenue, gross margin, EBITDA, backlog, ARR and headcount all fell
- **Finding:** In H1 2026, compared with H1 2025, the business shrank and margins compressed. The company's Adjusted EBITDA held up only because add-backs more than doubled.
- **Evidence:**
  - Revenue: 203.4 vs 205.2 (-0.9%). Clinical testing -1.9% (146.0 / 148.9).
  - Gross margin: 77.3 / 203.4 = 38.0%, vs 88.2 / 205.2 = 43.0%, a fall of 5.0 points. Cost of revenue grew 7.8% (126.1 / 117.0).
  - SG&A grew 13.6% (57.8 / 50.9).
  - Reported EBITDA: 19.6 vs 39.0 (-49.7%). Net loss of 8.9 vs a profit of 7.4.
  - Adjusted EBITDA: 54.1 vs 56.0 (-3.4%), while "other non-recurring" add-backs rose from 10.0 to 24.6.
  - Clinical volume: H1 annualized 812 x 2 = 1,624 vs 1,705 for FY2025 (-4.8%; ignores seasonality).
  - Revenue per accession: 179.8 vs 184.6 (-2.6%).
  - Backlog 246.0 to 231.4 (-5.9%). Book-to-bill 0.7. ARR 17.4 to 17.0 (-2.3%). Headcount 2,150 to 2,090 (-2.8%).
- **Source:** `income_statement.csv`, H1 columns. `adjusted_ebitda_reconciliation.csv`, H1 columns. `kpis.csv`, all rows.
- **Severity:** High
- **Confidence:** High. Computed directly from the data.
- **Deal impact:** Valuation and closing (see FIN-06).
- **Cross-check:** The Q1 and Q2 2026 10-Qs (MD&A explanation, any guidance change), and news on the cyber incident's effect on test volumes, payer actions or the loss of a client.

#### FIN-05: The deal model's FY2026 Adjusted EBITDA of US$137.0 million needs H2 2026 to be 19.6% above H2 2025
- **Finding:** The base case uses the guidance midpoint (137.0). H1 2026 Adjusted EBITDA was 54.1, down 3.4% year on year. To reach the midpoint, H2 2026 must deliver 82.9, against 69.3 in H2 2025, and H2 2025 itself included the Q4 spike. The model was built as of June 30, 2026, and its assumptions look stale.
- **Evidence:**
  - Required H2 2026 = 137.0 - 54.1 = 82.9. H2 2025 = 125.3 - 56.0 = 69.3. Required growth = 82.9 / 69.3 - 1 = +19.6%. At the low end of guidance (134.0): 79.9, or +15.3%.
  - H1 run-rate FY2026 (projection) = 54.1 x 2 = 108.2. Revenue run-rate = 203.4 x 2 = 406.8, which is -5.6% vs FY2025.
  - The 9% annual growth assumed for 2027 to 2030 compares with H1 2026 revenue growth of -0.9% and Q2 2026 growth of -3.0%.
- **Source:** `adjusted_ebitda_reconciliation.csv`. `income_statement.csv`. `revenue_quarterly.csv`. `deal-brief.md`, section 6.
- **Severity:** High
- **Confidence:** High for the arithmetic. Medium for the projection.
- **Deal impact:** Valuation.
- **Cross-check:** Whether Corvane reaffirmed or cut its FY2026 guidance in the Q2 2026 10-Q or earnings release, or in news coverage.

#### FIN-06: Headroom over the US$110.0 million closing floor is US$13.4 million and could disappear by Q2 2027 (projection)
- **Finding:** LTM Adjusted EBITDA (company definition) at Q2 2026 is 123.4, which is 13.4 (10.9%) above the financing floor. That headroom could disappear on two paths (projections):
  - if H2 2026 and H1 2027 repeat H1 2026, LTM at closing would be 108.2;
  - if the Q4 2025 spike flowed fully to EBITDA, LTM would fall to about 110.2 once that quarter rolls out of the LTM window.
- **Evidence:**
  - Headroom: 123.4 - 110.0 = 13.4, and 13.4 / 123.4 = 10.9%.
  - Q2 2027 LTM at the H1 2026 run-rate (projection): 54.1 + 54.1 = 108.2, which is 1.8 below the floor.
  - Q4 2025 excess at 100% flow-through (inference): 123.4 - 13.2 = 110.2. At the FY2025 Adjusted EBITDA margin of 29.1% flow-through: 123.4 - (13.2 x 0.291) = 123.4 - 3.8 = 119.6.
  - On diligence-adjusted LTM (93.5), the floor is already missed by 16.5. The condition uses Corvane's definition, so this only matters if the lenders' definition is narrower.
- **Source:** `adjusted_ebitda_reconciliation.csv`, LTM and H1 columns. `revenue_quarterly.csv`. `deal-brief.md`, section 3.
- **Severity:** High. It could become Critical (block closing) if the Q4 2025 one-off is confirmed as high-margin, or if H2 2026 Adjusted EBITDA comes in below about 55.9. That threshold is the H2 2026 figure that keeps the FY2026 LTM at 110.0 (110.0 - 54.1 = 55.9). I have not rated it Critical because current LTM still passes, and the failing numbers are projections.
- **Confidence:** Medium. It depends on projections and on the one-off assumption.
- **Deal impact:** Closing risk and financing.
- **Cross-check:** The commitment letter's exact definition and test date. The credit agreement's "Consolidated EBITDA" definition in the 10-K (please send it to me to recompute). Q3 2026 results if available.

#### FIN-07: The US$750.0 million term loan B is 7.4x to 8.0x diligence-adjusted EBITDA, not 6.0x
- **Finding:** The loan is sized at 6.0x the company's FY2025 figure (750.0 / 125.3 = 5.99x). On diligence-adjusted earnings, the leverage is much higher and debt service looks thin (projection).
- **Evidence:**
  - Leverage of the 750.0 loan:
    - LTM company: 750.0 / 123.4 = 6.1x
    - Minimum case: 750.0 / 110.3 = 6.8x
    - FY2025 diligence-adjusted: 750.0 / 101.2 = 7.4x
    - LTM diligence-adjusted: 750.0 / 93.5 = 8.0x
    - LTM reported EBITDA: 750.0 / 68.1 = 11.0x
  - 6.0x of LTM diligence-adjusted EBITDA = 561.0, which is 189.0 below the commitment.
  - Illustrative debt service (projection): the current implied interest rate is 34.1 / ((405.9 + 421.8) / 2) = 34.1 / 413.9 = 8.2%. Applied to 750.0, that gives 61.8 of interest a year. LTM diligence-adjusted EBITDA / interest = 93.5 / 61.8 = 1.5x. (EBITDA - LTM capex 30.6) / interest = 62.9 / 61.8 = 1.0x, before taxes and working capital.
  - Current interest cover: LTM EBITDA / interest = 68.1 / 34.8 = 1.96x. LTM operating income / interest = (62.1 - 26.6 + 6.0) / 34.8 = 41.5 / 34.8 = 1.19x.
- **Source:** `adjusted_ebitda_reconciliation.csv`. `balance_sheet.csv`, debt rows. `cash_flow.csv`, capex row. `income_statement.csv`, interest expense. `deal-brief.md`, section 3.
- **Severity:** High. It is financing-related and needs re-sizing or re-pricing. It is not a pre-closing default.
- **Confidence:** High for leverage. Medium for interest cover, which assumes the new loan carries the current rate.
- **Deal impact:** Financing and post-closing.
- **Cross-check:** The term loan B pricing, its covenants, and whether the bank group's diligence accepted the add-backs.

#### FIN-08: Biopharma growth comes entirely from Veltrane Therapeutics; the rest of biopharma shrank, and bookings collapsed in H1 2026
- **Finding:** Veltrane is the #2 customer overall and 51.2% of biopharma revenue. Biopharma revenue excluding Veltrane fell 7.1% in FY2025. The backlog fell 5.9% in H1 2026 with a book-to-bill of 0.7. The model assumes the backlog "including the Veltrane programs" converts on its historical schedule.
- **Evidence:**
  - Veltrane revenue: 38.0 to 50.5, up 12.5 (+32.9%).
  - Veltrane share of biopharma: FY2025 50.5 / 98.6 = 51.2%. FY2024 38.0 / 89.8 = 42.3%.
  - Biopharma excluding Veltrane: FY2024 89.8 - 38.0 = 51.8. FY2025 98.6 - 50.5 = 48.1 (-7.1%).
  - Total biopharma growth was 8.8, less than Veltrane's 12.5.
  - Backlog: 246.0 to 231.4, down 14.6. Implied H1 2026 bookings = 0.7 x 48.9 = 34.2, and 34.2 - 48.9 = -14.7, consistent with the backlog decline.
  - Backlog / LTM biopharma revenue = 231.4 / (98.6 - 47.6 + 48.9) = 231.4 / 99.9 = 2.3 years. Veltrane's share of the backlog is not disclosed.
- **Source:** `revenue_by_customer.csv`, row 2. `income_statement.csv`, row "Revenue: Biopharma services". `kpis.csv`, rows "backlog" and "book-to-bill".
- **Severity:** High
- **Confidence:** High for the arithmetic. It assumes, on the reasonable basis of its name, that Veltrane is a biopharma client.
- **Deal impact:** Valuation and post-closing.
- **Cross-check:** News, filings and court records on Veltrane: trial halts, contract termination, disputes, its financial health. Also whether the Q4 2025 spike included Veltrane milestone revenue.

#### FIN-09: Claim denials are rising fast while the price concession reserve lags; DSO is up 16 days since FY2024
- **Finding:** Over the period, the initial claim denial rate nearly doubled and DSO rose sharply. Receivables grew 3.5 times faster than revenue in FY2025. The implicit price concession reserve rose only 4.3 points. At the same time, payer denial write-offs are added back to Adjusted EBITDA. The risk is that clinical revenue (recognized at the amount Corvane expects to collect) is overstated, with the shortfall pushed into add-backs.
- **Evidence:**
  - Denial rate: 8.9% (FY2023), 10.7%, 13.4%, 16.2% (H1 2026).
  - DSO on net AR:
    - FY2023: 55.8 / 348.0 x 365 = 58.5 days
    - FY2024: 66.3 / 386.0 x 365 = 62.7 days
    - FY2025: 93.3 / 431.0 x 365 = 79.0 days
    - Q2 2026: 90.2 / 406.8 x 365 = 80.9 days (annualized H1), or 90.2 / 429.2 x 365 = 76.7 days (LTM)
  - DSO including contract assets: FY2025 103.1 / 431.0 x 365 = 87.3 days. Q2 2026 101.8 / 406.8 x 365 = 91.3 days.
  - Gross DSO: FY2024 87.6 / 386.0 x 365 = 82.8 days. FY2025 124.6 / 431.0 x 365 = 105.5 days.
  - Net AR growth FY2025: 93.3 / 66.3 = +40.7%, vs revenue +11.7%.
  - Reserve as % of gross AR: 16.1 / 71.9 = 22.4%, 21.3 / 87.6 = 24.3%, 31.3 / 124.6 = 25.1%, 32.9 / 123.1 = 26.7%.
  - Contract assets: 6.1, 7.4, 9.8, 11.6 (+18.4% in H1 2026).
  - Sensitivity: each 1 point of reserve on Q2 2026 gross AR = 1.2 of revenue and pre-tax income (123.1 x 1%). A reserve at 30% would be 36.9, which is 4.0 more than booked.
  - Note: FY2025 cash flow AR change (29.4) equals the full balance sheet change. This implies the acquired lab brought no receivables, or the acquired AR is classified differently. Question for management.
- **Source:** `balance_sheet.csv`, AR, contract assets and memo rows. `kpis.csv`, row "Initial claim denial rate". `cash_flow.csv`, row "Change in accounts receivable". `adjusted_ebitda_reconciliation.csv`, row "Payer denial".
- **Severity:** High. It needs a reserve true-up in the price, or a specific protection.
- **Confidence:** High for the ratios. Medium for whether the reserve is too low, which is a judgment.
- **Deal impact:** Valuation and post-closing.
- **Cross-check:** The 10-K critical accounting estimates (collection-rate model, changes in estimate), any Medicare recoupment, MAC or RAC audits, or payer disputes in the news or court records. Auditor comments or critical audit matters on revenue.

#### FIN-10: Cash conversion is weak and falling; free cash flow is negative and is funded by the revolver
- **Finding:** Only 18.2% of LTM Adjusted EBITDA turned into operating cash flow. LTM free cash flow is -8.2. The revolver has risen from 0.0 to 35.0 since FY2023. FY2025 cash was also supported by a one-time sale-leaseback (18.5 of proceeds).
- **Evidence:**
  - OCF / Adjusted EBITDA: 33.4% (FY2023), 32.1%, 22.7% (FY2025), 14.4% (H1 2026). LTM 22.4 / 123.4 = 18.2%, where LTM OCF = 28.4 - 13.8 + 7.8 = 22.4.
  - OCF / net income: FY2025 28.4 / 26.4 = 1.08x. H1 2026 not meaningful (net loss).
  - Free cash flow: FY2023 3.5, FY2024 5.1, FY2025 -5.1, H1 2026 -4.3. LTM = -5.1 - (-1.2) + (-4.3) = -8.2.
  - FY2025 funding:
    - Uses: FCF -5.1, acquisition -31.0, term loan repayments -4.1, other financing -2.0.
    - Sources: sale-leaseback +18.5, revolver +20.0, cash drawdown 3.7.
    - Net: -5.1 - 31.0 + 18.5 + 20.0 - 4.1 - 2.0 = -3.7, matching the change in cash.
  - Revolver: 0.0, 10.0, 30.0, 35.0. Cash at June 30, 2026: 28.8.
  - Cash runway (projection): the H1 2026 cash need was 4.3 + 2.1 + 0.6 = 7.0 per half-year. Cash of 28.8 alone covers about 4 half-years, about 2 years, before revolver availability, which is not disclosed.
- **Source:** `cash_flow.csv`, all rows. `balance_sheet.csv`, cash and revolver rows.
- **Severity:** High
- **Confidence:** High. Computed directly.
- **Deal impact:** Financing, post-closing, and the reliability of the Adjusted EBITDA.
- **Cross-check:** Revolver commitment size and availability, and the springing covenant in the 10-K credit agreement description.

#### FIN-11: Net debt of US$391.0 million is at December 31, 2025, but the US$424.7 million repayment matches June 30, 2026 debt; there are also unquantified debt-like items
- **Finding:** The brief's EV uses net debt at Dec 31, 2025 (391.0). The repayment of 424.7 equals gross debt at June 30, 2026. On a consistent June 30, 2026 basis, net debt is 395.9, which is 4.9 higher. Debt-like items are not in either figure: the sale-leaseback lease liability, other liabilities of 107.4 (unexplained), any prepayment or breakage costs, and possible acquisition earn-outs.
- **Evidence:**
  - Dec 31, 2025: 30.0 + 391.8 = 421.8 gross debt, less 30.8 cash = 391.0 (ties to the brief).
  - June 30, 2026: 35.0 + 389.7 = 424.7 gross debt (ties to the repayment), less 28.8 cash = 395.9.
  - Mixed-basis gap: 395.9 - 391.0 = 4.9.
  - Trend to closing (projection): the revolver rose 5.0 in each of H1 2025 and H1 2026, and term loan amortization is 2.1 per half.
  - Sale-leaseback: other non-current assets rose 47.0 to 64.6 (+17.6) and other liabilities rose 108.7 to 122.0 (+13.3) in FY2025. This is consistent with a lease asset and liability being recognized (inference).
- **Source:** `balance_sheet.csv`, rows 2, 10, 16, 17 and 18. `cash_flow.csv`, sale-leaseback rows. `deal-brief.md`, sections 2 and 3.
- **Severity:** Medium. The amount is small relative to EV, but the net debt definition needs fixing in the merger agreement.
- **Confidence:** High for the reconciliation. Low for the debt-like items, which are not broken out.
- **Deal impact:** Valuation (the equity bridge) and financing.
- **Cross-check:** 10-K/10-Q debt and lease notes (lease liability, prepayment premium, change-of-control terms), and acquisition contingent consideration.

#### FIN-12: Medicare is 24.2% of revenue, and Medicare-paid hereditary cancer panels are about 17.7%, against a model assumption of flat Medicare rates to 2030
- **Finding:** Medicare fee-for-service is the #1 payer. The hereditary cancer panel's Medicare share keeps rising, so a Medicare rate change hits revenue and EBITDA almost dollar for dollar (inference).
- **Evidence:**
  - Medicare: 92.6 (24.0%) to 104.3 (24.2%), growth +12.6%.
  - Panel revenue FY2025: 44% x 314.8 = 138.5. Medicare-paid panel revenue: 55% x 138.5 = 76.2, which is 76.2 / 431.0 = 17.7% of total revenue and 76.2 / 104.3 = 73.0% of Medicare revenue.
  - H1 2026: 45% x 146.0 = 65.7 panel revenue, of which 56% = 36.8 is Medicare-paid.
  - Sensitivity (projection, assuming 100% flow-through): a 10% Medicare panel rate cut = 7.6 of revenue and EBITDA, which is 7.6 / 125.3 = 6.1% of FY2025 Adjusted EBITDA and 7.6 / 93.5 = 8.1% of LTM diligence-adjusted EBITDA.
- **Source:** `revenue_by_customer.csv`, row 2. `kpis.csv`, rows 4 and 5. `income_statement.csv`, clinical revenue.
- **Severity:** Medium. It becomes higher if other sources show a pending rate change or a coverage action.
- **Confidence:** High for the exposure. Medium for the sensitivity.
- **Deal impact:** Valuation.
- **Cross-check:** CMS fee schedule or local coverage determination news, MolDX coverage, and any recoupment or audit matters.

#### FIN-13: FY2025 includes non-organic and one-time items: a US$31.0 million acquisition and a US$6.8 million sale-leaseback gain
- **Finding:**
  - The acquisition added 22.3 of goodwill and 2 labs. Its revenue and EBITDA contribution is not disclosed, so organic growth cannot be measured.
  - The sale-leaseback gain inflated FY2025 net income. Correctly, it is excluded from EBITDA. The leaseback creates new rent, which will reduce future EBITDA (inference).
- **Evidence:**
  - Goodwill: 298.6 to 320.9, up 22.3.
  - Labs: 5 to 7.
  - Other income: 7.2, of which 6.8 is the gain.
  - Net income excluding the gain (inference, at the FY2025 effective tax rate of 8.8 / 35.2 = 25.0%): 26.4 - 6.8 x 0.75 = 26.4 - 5.1 = 21.3.
- **Source:** `cash_flow.csv`, rows 5, 10 and 11. `balance_sheet.csv`, row 8. `income_statement.csv`, row 13. `kpis.csv`, row 12.
- **Severity:** Medium
- **Confidence:** High for the amounts. Medium for the effects.
- **Deal impact:** Valuation (organic growth) and post-closing (rent).
- **Cross-check:** The 10-K business combination note (acquired revenue, purchase price allocation) and the sale-leaseback terms (rent, lease term).

#### FIN-14: Lab informatics is shrinking slightly
- **Finding:** ARR fell 2.3% and gross revenue retention slipped to 95%. The segment is small (4.2% of H1 2026 revenue). It does not support a growth story, but the effect on value is small.
- **Evidence:**
  - ARR: 17.4 to 17.0, so 17.0 / 17.4 - 1 = -2.3%.
  - Gross revenue retention: 96% to 95%.
  - Segment revenue: 8.5 vs 8.7 (-2.3%). Share of H1 2026 revenue: 8.5 / 203.4 = 4.2%.
- **Source:** `kpis.csv`, rows 9 and 10. `income_statement.csv`, row 4.
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (minor).
- **Cross-check:** Customer churn disclosures and whether the cyber incident affected informatics customers.

#### FIN-15: Goodwill and intangibles are 401.1, nearly four times book equity; the impairment test date is not in the financial data
- **Finding:** Goodwill (320.9) plus intangibles (80.2) = 401.1 at June 30, 2026, against equity of 102.0. The financial files do not give the date or result of the last impairment test, or reporting-unit headroom. The only market data point I have is the July 31, 2026 close of US$18.10 from the brief. That implies a diluted market value of 52.4 x 18.10 = 948.4, still well above book equity at the consolidated level. A biopharma reporting unit tied to Veltrane could be at risk (inference).
- **Evidence:** 320.9 + 80.2 = 401.1. 401.1 / 102.0 = 3.9x. 52.4 x 18.10 = 948.4.
- **Source:** `balance_sheet.csv`, rows 8, 9 and 20. `deal-brief.md`, section 2.
- **Severity:** Low. It becomes higher if the SEC filings show a test date before a large share price fall, or thin reporting-unit headroom.
- **Confidence:** Low. Key data is missing.
- **Deal impact:** Post-closing (purchase accounting) and disclosure.
- **Cross-check:** The 10-K goodwill note (test date, reporting units, headroom) and the share price history since that date (news or market data).

### Payer and client list (task 4)

Source: `revenue_by_customer.csv`, ranked by FY2025 revenue. US$ millions.

| Rank | Payer / client | FY2024 | Share | FY2025 | Share | YoY |
|---|---|---|---|---|---|---|
| 1 | Medicare (traditional fee-for-service) | 92.6 | 24.0% | 104.3 | 24.2% | +12.6% |
| 2 | Veltrane Therapeutics | 38.0 | 9.8% | 50.5 | 11.7% | +32.9% |
| 3 | Orvia Health Plan | 44.0 | 11.4% | 48.7 | 11.3% | +10.7% |
| 4 | Brightwater Mutual Insurance | 28.9 | 7.5% | 30.2 | 7.0% | +4.5% |
| 5 | State Medicaid managed care plans (aggregated) | 20.1 | 5.2% | 21.5 | 5.0% | +7.0% |
| 6 | Halcrest Oncology Network | 11.0 | 2.8% | 12.4 | 2.9% | +12.7% |
| 7 | Sunmere BioPharma | 9.9 | 2.6% | 10.8 | 2.5% | +9.1% |
| 8 | Ferrow Health | 9.1 | 2.4% | 9.6 | 2.2% | +5.5% |
| 9 | Lakeline Pharmaceuticals | 7.8 | 2.0% | 8.1 | 1.9% | +3.8% |
| 10 | Eastgate Physicians Alliance | 6.1 | 1.6% | 6.4 | 1.5% | +4.9% |
| | All other | 118.5 | 30.7% | 128.5 | 29.8% | +8.4% |
| | **Top 10** | 267.5 | 69.3% | 302.5 | 70.2% | +13.1% |

- **Genaro Biosciences is not in the top 10.** If it is a client, its FY2025 revenue is below US$6.4 million (rank 10) and sits within "All other". The file cannot confirm whether it is a client at all.
- Orvia Health Plan moved from #2 in FY2024 to #3 in FY2025, behind Veltrane. Note that 2024 shares are unranked in the file; this is inferred from the amounts.
- The top 3 together are 203.5 / 431.0 = 47.2% of revenue.
- Top 10 check: 104.3 + 50.5 + 48.7 + 30.2 + 21.5 + 12.4 + 10.8 + 9.6 + 8.1 + 6.4 = 302.5, and 302.5 / 431.0 = 70.2%.

### Positive or mitigating points

- The data pack ties internally: every bridge, LTM and quarterly sum recomputes, and the brief's equity value, EV, 13.2x and premium recompute.
- The cyber (6.1) and transaction (2.3) add-backs look genuinely one-off, and SBC is a market-standard add-back. These are accepted in my diligence-adjusted figure.
- The reserve as a share of gross AR is moving in the right direction (22.4% to 26.7%), and DSO eased slightly in H1 2026 (net AR 93.3 to 90.2).
- The company's leverage fell from 4.55x (FY2023) to 3.12x (FY2025) on its own Adjusted EBITDA. The 6.0x loan sizing reconciles exactly (750.0 / 125.3 = 5.99x).
- The backlog still covers about 2.3 years of biopharma revenue (231.4 / 99.9). Revenue is diversified beyond the top 3, with 52.8% coming from outside them.
- Informatics gross revenue retention is still 95%.
- Current LTM Adjusted EBITDA (123.4) does pass the 110.0 floor today.

### Gaps and questions for management

1. What caused the Q4 2025 revenue of 120.5? Please give the amount and nature of any one-time item (collection-rate true-up, milestone, catch-up billing) and its EBITDA effect. The lead should send me any amount disclosed in the filings.
2. Revenue and EBITDA of the FY2025 acquisition (pre- and post-acquisition), its closing date, and the acquired receivables.
3. General ledger detail on the payer denial and recoupment write-offs: which line they are booked in, why they are "non-recurring", and the expected FY2026 amount.
4. Billing system transition: start date, expected end date, and the total remaining spend.
5. The collection-rate model: history of changes in estimate, the AR aging by payer, and the denial-rate trend by payer (Medicare, Orvia, Brightwater).
6. Veltrane: its share of the backlog, contract terms, termination rights, and the H1 2026 bookings and cancellations by client.
7. The credit agreement's "Consolidated EBITDA" definition and the covenant compliance certificates. The commitment letter's exact definition and test date for the 110.0 floor.
8. Revolver commitment size and availability. Breakage costs or prepayment premium at repayment. The sale-leaseback lease liability. A breakdown of "Other liabilities" (107.4).
9. Q3 2026 results and current FY2026 guidance (the brief is dated October 12, 2026; my data ends June 30, 2026).
10. The date and result of the last goodwill impairment test, the reporting units and their headroom, and the share price since the test date.
11. Insurance recoveries for the cyber incident, and any revenue lost during it.
12. Clinical test volumes for H1 2025, so H1 2026 can be compared like for like.

Files used are in `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/financials/`.
