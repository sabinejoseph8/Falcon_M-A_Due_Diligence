## Financial analyst: findings (iteration 2, narrow follow-up)

### Files reviewed
- `data/deal-brief.md` (context only)
- `data/financials/README.md`
- `data/financials/income_statement.csv`
- `data/financials/revenue_quarterly.csv`
- `data/financials/balance_sheet.csv`
- `data/financials/cash_flow.csv`
- `data/financials/adjusted_ebitda_reconciliation.csv`
- `data/financials/revenue_by_customer.csv`
- `data/financials/kpis.csv`

Facts supplied by the lead agent are labeled "[lead: 10-K Note 9]", "[lead: 10-Q Q2 2026]", "[lead: 10-K Note 2]", "[lead: DEF 14A]" and "[lead: court records]". I did not read those source files myself.

None of the financial files contained text that tried to instruct the agents. There is no prompt-injection finding.

### Key metrics table

Reported figures are as the company presents them. Rows marked "adj" are my diligence adjustments.

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 / LTM Q2 2026 |
|---|---|---|---|---|
| Total revenue (reported) | 368.9 | 421.7 | 502.3 | H1 222.6 / LTM 498.4 |
| Revenue growth (reported) | 18.1% | 14.3% | 19.1% | H1 -1.7% |
| Revenue excl. $31.8m bill-and-hold (adj) | n/a | n/a | 470.5 | n/a |
| Revenue growth excl. bill-and-hold (adj) | n/a | n/a | 11.6% | n/a |
| Gross margin | 40.1% | 40.8% | 41.1% | H1 38.0% |
| EBITDA | 42.2 | 52.3 | 64.1 | LTM 48.2 |
| Adjusted EBITDA (company) | 60.4 | 74.8 | 98.8 | LTM 89.7 |
| Adj EBITDA excl. bill-and-hold at 41.1% margin (adj) | n/a | n/a | 85.7 | n/a |
| Add-backs as % of Adj EBITDA | 30.1% | 30.1% | 35.1% | LTM 46.3% |
| Net debt (full cash) | 65.2 | 151.7 | 178.4 | 193.6 |
| Net debt / Adj EBITDA | 1.08x | 2.03x | 1.81x | 2.16x |
| Net debt / EBITDA | 1.55x | 2.90x | 2.78x | 4.02x |
| Covenant ratio, reading (a) / (b) / (c) (adj) | n/a | n/a | n/a | 2.26x / 3.65x / 2.67x |
| Operating cash flow | 30.8 | 40.8 | 9.7 | H1 -4.2 |
| Free cash flow | 16.2 | 24.6 | -10.1 | H1 -13.0 |
| Hardware backlog (period end) | 142.0 | 168.0 | 131.0 | 118.0 |

**Workings for the table**
- Growth: FY2023 = 368.9/312.4 - 1 = 18.1%. FY2024 = 421.7/368.9 - 1 = 14.3%. FY2025 = 502.3/421.7 - 1 = 19.1%. H1 2026 = 222.6/226.5 - 1 = -1.7%.
- LTM revenue = 121.4 + 154.4 + 109.7 + 112.9 = 498.4. Cross-check: 502.3 + 222.6 - 226.5 = 498.4.
- Gross margin: 147.9/368.9 = 40.1%; 172.1/421.7 = 40.8%; 206.3/502.3 = 41.1%; 84.6/222.6 = 38.0%.
- Add-backs (SBC + restructuring + other):
  - FY2023: (11.6 + 4.6 + 2.0) = 18.2, and 18.2/60.4 = 30.1%.
  - FY2024: 22.5/74.8 = 30.1%.
  - FY2025: 34.7/98.8 = 35.1%.
  - LTM: (17.8 + 9.7 + 14.0) = 41.5, and 41.5/89.7 = 46.3%.
- Net debt (term loan + revolver - cash):
  - FY2023: 120.0 - 54.8 = 65.2.
  - FY2024: 200.0 - 48.3 = 151.7.
  - FY2025: 220.0 - 41.6 = 178.4.
  - June 2026: 227.5 - 33.9 = 193.6.
- Net debt / EBITDA at June 2026 = 193.6/48.2 = 4.02x.
- I checked each LTM line in the reconciliation as FY2025 + H1 2026 - H1 2025:
  - EBITDA: 64.1 + 10.4 - 26.3 = 48.2.
  - SBC: 17.2 + 8.9 - 8.3 = 17.8.
  - Restructuring: 7.9 + 4.4 - 2.6 = 9.7.
  - Other: 9.6 + 6.2 - 1.8 = 14.0.
  - Adj EBITDA: 98.8 + 29.9 - 39.0 = 89.7.
  - All match the file.

### Findings

#### FIN-18: The reported 2.26x covenant ratio only works if every add-back is allowed in full, which seems to ignore the 15% cap
- **Finding:** The company's 2.26x is reproduced exactly only by reading (a): full company Adjusted EBITDA, with no cap on add-backs. If the 15% cap applies to all add-backs (reading b), the ratio at June 30, 2026 is 3.65x. That is a breach of today's 3.50x limit. If SBC is uncapped and other add-backs are capped (reading c), the ratio is 2.67x.
- **Evidence:**
  - Covenant net debt:
    - Gross debt = revolver 45.0 + term loan 182.5 = 227.5.
    - Cash 33.9, but netting is capped at 25.0.
    - Covenant net debt = 227.5 - 25.0 = 202.5.
    - For comparison, net debt with all cash netted = 193.6.
  - LTM inputs: EBITDA 48.2, SBC 17.8, restructuring 9.7, other non-recurring 14.0. Total add-backs 41.5.
  - (a) Full company Adjusted EBITDA: 202.5 / 89.7 = **2.26x**. This matches the 10-Q. With all cash netted it would be 193.6/89.7 = 2.16x, so the company does apply the cash cap.
  - (b) All add-backs capped:
    - Cap = 15% x 48.2 = 7.23. Covenant EBITDA = 48.2 + 7.23 = 55.43.
    - Ratio = 202.5 / 55.43 = **3.65x**, above the 3.50x limit.
    - To comply, covenant EBITDA would need to be 202.5/3.50 = 57.86.
  - (c) SBC uncapped, other add-backs capped:
    - Base = 48.2 + 17.8 = 66.0. Cap = 15% x 66.0 = 9.90, which is below the 23.7 of other add-backs, so the cap binds.
    - Covenant EBITDA = 75.9. Ratio = 202.5 / 75.9 = **2.67x**.
  - Under reading (a), add-backs are 41.5/48.2 = 86.1% of EBITDA, against a 15% cap.
- **Implication:** Reading (a) only works if base Consolidated EBITDA already includes SBC, restructuring and the "other non-recurring" items, so that the 15% cap never applies to them. That would make the cap almost meaningless. Otherwise the company is overstating covenant EBITDA. Under reading (b), the company may already be in default and its 10-Q compliance statement would be wrong.
- **Source:**
  - `data/financials/balance_sheet.csv`, rows "Cash and cash equivalents", "Revolving credit facility" and "Term loan", column Q2_2026.
  - `data/financials/adjusted_ebitda_reconciliation.csv`, rows "EBITDA" and "Add:" lines (8 to 11), column LTM_Q2_2026.
  - [lead: 10-K Note 9]; [lead: 10-Q Q2 2026].
- **Severity:** High. It becomes Critical if the credit agreement confirms reading (b): that would mean a current default and a misstated 10-Q.
- **Confidence:** Medium. The arithmetic is High confidence, but the definition of base Consolidated EBITDA is still unconfirmed.
- **Deal impact:** Closing risk (default before signing or closing, lender consent), financing, and disclosure or controls.
- **Cross-check:** Obtain the full credit agreement definition of "Consolidated EBITDA" and "Permitted Add-backs" (10-K exhibit 10.x). Obtain the compliance certificate for Q2 2026. Look for any 8-K amendment or waiver, and news of lender talks.

#### FIN-19: The 3.00x step-down is at risk from September 30, 2026, and reading (c) breaches at December 31 even at the top of guidance
- **Finding:**
  - Under reading (a), the company stays in compliance through December 31, 2026. However, the low end of guidance combined with the H1 debt trend lands exactly on 3.00x.
  - Under reading (c), the ratio is 2.71x to 2.94x at September 30. It is then 3.10x to 3.74x at December 31, a breach at every guidance point.
  - Under reading (b), the company is in breach throughout.
- **Assumptions:**
  - H2 2026 Adj EBITDA = guidance minus H1 2026 (29.9), so 40.1 / 44.1 / 48.1 at the low / mid / high points. Q3 2026 = half of H2.
  - Q3 2025 Adj EBITDA is H2 2025 (98.8 - 39.0 = 59.8) allocated by revenue: 121.4/275.8 = 44.0%, giving 26.3.
  - Add-backs in each 2026 quarter run at the H1 2026 rate: SBC 4.45 and other 5.30 per quarter, so FY2026 add-backs are 39.0. Q3 2025 add-backs are half of H2 2025: SBC 4.45 and other 6.55.
  - "Flat" debt case: covenant net debt stays at 202.5.
  - "Trend" case: H1 2026 continues (revolver +10.0 and term loan -2.5 per half), so covenant net debt is 206.25 at September 30 and 210.0 at December 31. Cash runs from 33.9 down to about 26.2 (H1 change -7.7), so the 25.0 netting cap still binds.
- **Evidence (low / mid / high guidance):**
  - **Sept 30 LTM inputs:**
    - Adj EBITDA = 89.7 - 26.3 + (20.05 / 22.05 / 24.05) = 83.45 / 85.45 / 87.45.
    - EBITDA = 48.2 - 15.3 + (10.3 / 12.3 / 14.3) = 43.2 / 45.2 / 47.2. Here Q3 2025 EBITDA = 26.3 - 11.0 = 15.3, and Q3 2026 EBITDA = Q3 Adj - 9.75.
    - SBC = 17.8. Other add-backs = 23.7 - 6.55 + 5.30 = 22.45.
  - **Sept 30 (a):** flat 202.5/83.45 = 2.43x, /85.45 = 2.37x, /87.45 = 2.32x. Trend 206.25 gives 2.47x / 2.41x / 2.36x.
  - **Sept 30 (b):** covenant EBITDA = 1.15 x EBITDA = 49.68 / 51.98 / 54.28. Flat gives 4.08x / 3.90x / 3.73x. Trend gives 4.15x / 3.97x / 3.80x. **Breach.**
  - **Sept 30 (c):** covenant EBITDA = 1.15 x (EBITDA + SBC) = 1.15 x (61.0 / 63.0 / 65.0) = 70.15 / 72.45 / 74.75. Flat gives 2.89x / 2.80x / 2.71x. Trend gives 2.94x / 2.85x / 2.76x.
  - **Dec 31 inputs (LTM = FY2026):** Adj EBITDA 70.0 / 74.0 / 78.0. EBITDA = Adj - 39.0 = 31.0 / 35.0 / 39.0.
  - **Dec 31 (a):** flat 2.89x / 2.74x / 2.60x. Trend 3.00x / 2.84x / 2.69x.
  - **Dec 31 (b):** covenant EBITDA 35.65 / 40.25 / 44.85. Flat 5.68x / 5.03x / 4.52x. Trend 5.89x / 5.22x / 4.68x. **Breach.**
  - **Dec 31 (c):** covenant EBITDA = 1.15 x (48.8 / 52.8 / 56.8) = 56.12 / 60.72 / 65.32. Flat 3.61x / 3.34x / 3.10x. Trend 3.74x / 3.46x / 3.22x. **Breach.**
  - **Breach thresholds (3.00x requires covenant EBITDA of at least 202.5/3.00 = 67.5 with flat debt):**
    - (a) Dec 31: breach if FY2026 Adj EBITDA is below 67.5. That is 6.5 (8.8%) below the 74.0 midpoint and 2.5 below the low end. Debt headroom at the midpoint = 3.00 x 74.0 - 202.5 = 19.5. In the trend case, the low end of 70.0 gives exactly 3.00x.
    - (a) Sept 30 midpoint: an Adj EBITDA cushion of 85.45 - 67.5 = 17.95 (21.0%). Debt headroom = 53.9.
    - (c) Sept 30 midpoint: covenant cushion 72.45 - 67.5 = 4.95, which is an EBITDA decline of only 4.95/1.15 = 4.3. Debt headroom = 3.00 x 72.45 - 202.5 = 14.9.
    - (c) Dec 31: compliance needs EBITDA + SBC of 67.5/1.15 = 58.7. That means EBITDA of 40.9, or Adj EBITDA of about 79.9, which is above the top of guidance. Alternatively, covenant net debt would have to fall by 202.5 - 3.00 x 60.72 = 20.3 at the midpoint.
  - **Liquidity:**
    - Cash 33.9 + revolver availability 25.8 = 59.7 [lead: 10-Q].
    - Implied facility size = 45.0 + 25.8 + 4.2 = 75.0.
    - H1 2026 free cash flow was -13.0. In the trend case, a further 10.0 draw leaves about 15.8 of availability.
- **Source:**
  - `adjusted_ebitda_reconciliation.csv`, all rows, columns FY2025, H1_2025, H1_2026 and LTM_Q2_2026.
  - `revenue_quarterly.csv`, Q3 2025 and Q4 2025.
  - `cash_flow.csv`, rows 15, 16, 22 and 24, column H1_2026.
  - `balance_sheet.csv`, column Q2_2026.
  - [lead: 10-K Note 9; 10-Q guidance].
- **Severity:** High
- **Confidence:** Medium. The quarterly EBITDA split and the add-back run-rate are my estimates. The December 31 case uses guidance directly.
- **Deal impact:** Closing risk and financing. A breach between signing and closing would need a lender waiver or amendment, and may count as a material adverse effect or breach interim operating covenants. The change of control is itself an event of default, so the full 227.5 plus 4.2 of letters of credit must be refinanced at closing in any case.
- **Cross-check:** Obtain the Q3 2026 10-Q (due around early November, before the IC meeting) and its compliance certificate. Check for any credit agreement amendment 8-K. Check news of revolver draws.

#### FIN-20: The $31.8m bill-and-hold accounts for 39.5% of FY2025 growth and nearly all of Q4 2025's growth spike
- **Finding:**
  - Without the bill-and-hold, FY2025 revenue growth falls from 19.1% to 11.6%.
  - Q4 2025 year-over-year growth falls from 32.4% to 5.1%, breaking the 13% to 14% trend of Q1 to Q3 2025 on the downside.
  - Hardware growth falls from 15.1% to 2.9%.
- **Evidence:**
  - Q4 2025 adjusted revenue = 154.4 - 31.8 = 122.6.
    - Reported year-over-year: 154.4/116.6 - 1 = 32.4%. Adjusted: 122.6/116.6 - 1 = 5.1%.
    - Quarter-over-quarter, reported Q4 2025 was 154.4/121.4 - 1 = +27.2%, against +9.9% in Q4 2024 (116.6/106.1).
  - Other 2025 quarters, year-over-year: Q1 108.9/96.2 = +13.2%; Q2 117.6/102.8 = +14.4%; Q3 121.4/106.1 = +14.4%.
  - FY2025:
    - Adjusted revenue = 502.3 - 31.8 = 470.5, and 470.5/421.7 - 1 = 11.6%.
    - Bill-and-hold share of growth = 31.8/(502.3 - 421.7 = 80.6) = 39.5%.
  - Hardware: (301.4 - 31.8) = 269.6, and 269.6/261.9 - 1 = 2.9%. Reported: 301.4/261.9 - 1 = 15.1%.
  - EBITDA effect:
    - No segment gross margin is disclosed, so I use the FY2025 total gross margin: 206.3/502.3 = 41.1%. Hardware margin is probably below the blended rate because software is higher-margin, so this may overstate the hit.
    - Removed = 31.8 x 41.1% = 13.1. Adjusted FY2025 Adj EBITDA = 98.8 - 13.1 = 85.7, a margin of 85.7/470.5 = 18.2%.
    - Sensitivity: at 30% the removed amount is 9.5 (Adj EBITDA 89.3); at 50% it is 15.9 (Adj EBITDA 82.9).
  - In the LTM to June 2026, the 31.8 recognized in Q4 2025 is offset by the 9.4 reversal in Q2 2026, and the 22.4 was delivered inside the window. So LTM revenue is not overstated by the timing itself. The risk is the comparison: Q4 2026 has to be measured against 154.4.
  - Backlog fell from 168.0 to 131.0 (-22.0%) in FY2025 and to 118.0 at June 2026. This fits demand being pulled forward.
- **Source:**
  - `revenue_quarterly.csv`, all rows.
  - `income_statement.csv`, rows "Revenue: Hardware", "Total revenue" and "Gross profit".
  - `adjusted_ebitda_reconciliation.csv`, row "Adjusted EBITDA".
  - `kpis.csv`, row "Hardware order backlog".
  - [lead: 10-K Note 2].
- **Severity:** Critical. The growth story underpins a deal model that assumes $560m of FY2026 revenue.
- **Confidence:** High for revenue. Medium for EBITDA, because of the margin assumption.
- **Deal impact:** Valuation and post-closing (revenue recognition and audit risk).
- **Cross-check:** Review the 10-K revenue recognition policy and whether the bill-and-hold criteria were met (customer request, separately identified goods, ready for transfer). Check auditor communications, given the auditor transition costs. Check any SEC comment letters.

#### FIN-21: Without the bill-and-hold, the FY2025 Adjusted EBITDA bonus metric misses threshold, yet bonuses were paid at 142% of target
- **Finding:**
  - Excluding the $31.8m, revenue is 470.5, just 0.5 above the 470.0 threshold.
  - Adjusted EBITDA is 85.7, below the 88.0 threshold.
  - Even removing only the $9.4m later returned takes Adjusted EBITDA to 94.9, below the 95.0 target.
- **Evidence:**
  - Reported: revenue 502.3 (between target 490.0 and max 510.0) and Adj EBITDA 98.8 (between target 95.0 and max 102.0).
  - Full adjustment: revenue 470.5 and Adj EBITDA 98.8 - 13.1 = 85.7, below the 88.0 threshold.
  - Break-even flow-through margin for the threshold: (98.8 - 88.0)/31.8 = 34.0%. Any margin above 34.0% fails the EBITDA threshold.
  - Returned goods only: revenue 502.3 - 9.4 = 492.9, still above target. Adj EBITDA 98.8 - 9.4 x 41.1% (3.9) = 94.9, below the 95.0 target.
  - Separately, the "Customer implementation delays" add-back of 4.1 looks like an operating cost. Without it, Adj EBITDA is 98.8 - 4.1 = 94.7, below target.
- **Source:**
  - `income_statement.csv`, rows "Total revenue" and "Gross profit", column FY2025.
  - `adjusted_ebitda_reconciliation.csv`, rows "Adjusted EBITDA" and "Detail: Customer implementation delays", column FY2025.
  - [lead: DEF 14A]; [lead: 10-K Note 2].
- **Severity:** High
- **Confidence:** Medium. The margin is assumed. The payout curve is not available, so I cannot compute the dollar overpayment.
- **Deal impact:** Post-closing, governance and possible clawback. The timing incentive behind the Q4 bill-and-hold also bears on the credibility of management's forecasts.
- **Cross-check:**
  - Check whether the proxy's bonus definition of Adjusted EBITDA matches the reconciliation.
  - Review the clawback policy (Dodd-Frank Rule 10D-1). A revenue restatement would trigger a mandatory recovery analysis.
  - Look for whistleblower or short-seller news about the Q4 2025 shipments.

#### FIN-22: Norvale's FY2025 growth falls from 32.3% to 11.4% without its $24.6m of bill-and-hold revenue
- **Finding:** Norvale's reported FY2025 growth depends heavily on bill-and-hold. Excluding it, Norvale grew 11.4% and its share falls from 31.1% to 28.0%. Norvale alone was 47.3% of the company's reported FY2025 revenue growth.
- **Evidence:**
  - Reported: 156.2/118.1 - 1 = 32.3%.
  - Adjusted: (156.2 - 24.6) = 131.6, and 131.6/118.1 - 1 = 11.4%.
  - Bill-and-hold share of Norvale growth = 24.6/(156.2 - 118.1 = 38.1) = 64.6%.
  - Adjusted share = 131.6/470.5 = 28.0%.
  - Norvale share of company growth = 38.1/80.6 = 47.3%.
  - Non-Norvale bill-and-hold = 31.8 - 24.6 = 7.2. The customers are not identified.
- **Source:** `revenue_by_customer.csv`, row 1 (Norvale) and the Total row, FY2024 and FY2025 revenue columns. [lead: 10-K Note 2].
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation (customer concentration and quality of growth) and post-closing retention risk.
- **Cross-check:** Ask whether the $9.4m returned in Q2 2026 was Norvale's. Check news on Norvale's capex plans or a vendor review. Check whether the Norvale contract has change-of-control or termination-for-convenience clauses (10-K material contracts).

#### FIN-23: On a clean basis, H1 2026 is low single-digit to mid single-digit growth, not the decline reported or the double digits that delivery timing suggests
- **Finding:**
  - Reported growth: Q1 2026 +0.7%, Q2 2026 -4.0%.
  - Adding back the $9.4m return reversal and the $2.3m outage credits gives Q2 2026 growth of +6.0%.
  - On a physical delivery basis (adding the $22.4m delivered in H1 2026), H1 grows 13.3%. But that is already-booked Q4 2025 demand, not new orders, and backlog keeps falling.
- **Evidence:**
  - Reported:
    - Q1: 109.7/108.9 - 1 = +0.7%.
    - Q2: 112.9/117.6 - 1 = -4.0%.
    - H1: 222.6/226.5 - 1 = -1.7%.
  - One-off normalized:
    - Q2 = 112.9 + 9.4 + 2.3 = 124.6, and 124.6/117.6 - 1 = +6.0%.
    - H1 = 233.9, and 233.9/226.5 - 1 = +3.3%.
    - This assumes the $9.4m credit reduced Q2 2026 revenue rather than a refund liability set up earlier. Please confirm.
  - Delivery basis:
    - H1 = 222.6 + 9.4 + 2.3 + 22.4 = 256.7, and 256.7/226.5 - 1 = +13.3%.
    - The quarterly split of the 22.4 is unknown. With an illustrative even split of 11.2 per quarter: Q1 120.9 (+11.0% against 108.9) and Q2 135.8 (+15.5% against 117.6).
    - The comparable Q4 2025 on this basis is 122.6 (+5.1%).
  - By segment, H1 2026 against H1 2025:
    - Hardware reported: 116.9/134.2 = -12.9%. Adding back 9.4: -5.9%. Delivery basis (+22.4 + 9.4 = 148.7): +10.8%.
    - Software reported: 67.5/58.9 = +14.6%. Adding back 2.3: +18.5%.
    - Services: 38.2/33.4 = +14.4%.
  - Contradicting KPIs:
    - Backlog fell from 131.0 to 118.0.
    - Net revenue retention fell from 118% to 111%.
    - Headcount fell from 1,452 to 1,405.
    - Robots shipped in H1 2026 were 1,640, against 4,300 for FY2025. That is an annualized 3,280, which is -23.7%.
- **Source:**
  - `revenue_quarterly.csv`.
  - `income_statement.csv`, segment revenue rows, columns H1_2025 and H1_2026.
  - `kpis.csv`, all rows.
  - [lead: 10-K Note 2].
- **Severity:** High. A clean growth rate of about 3% to 6% is far below the deal model's FY2026E of $560m, which is +11.5% on FY2025 reported (560/502.3).
- **Confidence:** Medium. It depends on how the $9.4m was booked and how the $22.4m is phased.
- **Deal impact:** Valuation.
- **Cross-check:** Check the 10-Q Q2 2026 revenue footnote (contract liabilities, refund liabilities) and the FieldOS outage disclosure. Check news about the outage and any customer churn.

#### FIN-24: Litigation reserves are not visible in the financial data, and the $1.4m Pinecrest cap looks low against Pinecrest's revenue
- **Finding:**
  - There is no litigation reserve line in the balance sheet, and Ruiz does not appear in the Adjusted EBITDA add-backs. The $3.2m Ruiz accrual, if it was booked, must sit inside accrued liabilities (30.5) or other liabilities (6.5). I cannot confirm it from these files.
  - Pinecrest's $12.0m claim is 69.0% of its FY2025 revenue.
  - The $1.4m cap (12 months of subscription fees) implies only 8.0% of Pinecrest revenue is subscription, against a 25.6% software mix company-wide.
- **Evidence:**
  - Accrued liabilities fell from 38.5 to 30.5 between December 2025 and June 2026, so a 3.2 accrual is not obvious.
  - G&A rose in H1 2026, from 16.2 to 19.8 (+3.6). Restructuring and other charges rose from 2.6 to 4.4. The only litigation add-back is Vantor (H1 2026: 3.0).
  - If the Ruiz charge sits in "Restructuring and other charges", it is being added back to Adjusted EBITDA.
  - Pinecrest:
    - Revenue was 17.4 in FY2025 and 16.2 in FY2024 (3.5% of total).
    - 12.0/17.4 = 69.0%. 1.4/17.4 = 8.0%.
    - At the company software mix (128.6/502.3 = 25.6%), Pinecrest subscription would be 17.4 x 25.6% = 4.5. So a 12-month cap would be about 4.5, not 1.4. This is an estimate, because the customer-level segment split is not provided.
    - Average FieldOS ARR per customer is 139.2/276 = 0.50, so 1.4 is about 2.8x the average.
  - Exposure range for Pinecrest is 1.4 to 12.0. The high end equals 13.4% of LTM Adj EBITDA (12.0/89.7).
- **Source:**
  - `balance_sheet.csv`, rows "Accrued liabilities" and "Other liabilities".
  - `income_statement.csv`, rows "General and administrative" and "Restructuring and other charges".
  - `adjusted_ebitda_reconciliation.csv`, rows 9 and 16.
  - `revenue_by_customer.csv`, row 4.
  - `kpis.csv`, rows "FieldOS ARR" and "Active customers".
  - [lead: court records].
- **Severity:** Medium
- **Confidence:** Low to Medium. Pinecrest's revenue split by segment is not available.
- **Deal impact:** Valuation (debt-like items) and indemnity.
- **Cross-check:**
  - Check the 10-Q commitments and contingencies note for the Ruiz accrual location and any Pinecrest accrual or "reasonably possible" range (ASC 450).
  - Get the Pinecrest contract to confirm the cap wording and whether it is 12 months of subscription fees only or all fees.
  - Check court filings for any claim that the cap is void (gross negligence or wilful misconduct carve-outs).

#### FIN-25: The $24.00 offer implies 18.3x FY2026 guidance EBITDA. At the deal model's 11.5x, value on current trading is $12.62 to $16.69 per share
- **Finding:**
  - The deal model's 11.5x was built on $118m of FY2026E Adjusted EBITDA. Current guidance is $70m to $78m.
  - At $24.00, EV of 1,352.8 is 15.1x LTM company Adjusted EBITDA, 18.3x the guidance midpoint, and 18.6x diligence-adjusted LTM.
  - No case in my grid, even 13x LTM company Adjusted EBITDA, reaches $24.00.
- **Evidence:**
  - **Offer:**
    - Equity value = 24.00 x 48.3 = 1,159.2. EV = 1,159.2 + 193.6 = 1,352.8.
    - On $118m: 1,352.8/118.0 = 11.46x, which matches the deal brief.
    - On current figures: 1,352.8/89.7 = 15.08x; /74.0 = 18.28x; /70.0 = 19.33x; /78.0 = 17.34x; /72.6 = 18.63x.
    - EBITDA needed at 11.5x = 1,352.8/11.5 = 117.6.
  - **Market:**
    - Market equity = 17.85 x 48.3 = 862.2. Market EV = 1,055.8.
    - That is 11.77x LTM Adj EBITDA and 14.27x the guidance midpoint.
  - **Diligence-adjusted LTM EBITDA:** 89.7 less customer implementation delays 3.3 (an operating cost), less restructuring 9.7 (recurs every year from FY2022 to H1 2026: 3.1, 4.6, 5.2, 7.9, 4.4), less Vantor litigation 4.1 (recurs from FY2024 and is ongoing), giving **72.6**. SBC is kept as an add-back. Without the SBC add-back it would be 72.6 - 17.8 = 54.8.
  - **Debt-like items:**
    - Ruiz 3.2 (accrued, a cash outflow) plus change-in-control payments 28.6 (proxy) = 31.8. That is 31.8/48.3 = $0.66 per share.
    - Not deducted, shown for sensitivity: Pinecrest 1.4 to 12.0 (contingent), letters of credit 4.2 (contingent), and any lender waiver or refinancing costs.

| Basis (EBITDA) | Multiple | EV | Equity (EV - 193.6) | Per share | Per share after 31.8 debt-like |
|---|---|---|---|---|---|
| (i) LTM company Adj 89.7 | 10.0x | 897.0 | 703.4 | 14.56 | 13.90 |
| | 11.5x | 1,031.6 | 838.0 | 17.35 | 16.69 |
| | 13.0x | 1,166.1 | 972.5 | 20.13 | 19.48 |
| (ii) FY2026 guide mid 74.0 | 10.0x | 740.0 | 546.4 | 11.31 | 10.65 |
| | 11.5x | 851.0 | 657.4 | 13.61 | 12.95 |
| | 13.0x | 962.0 | 768.4 | 15.91 | 15.25 |
| (iii) Diligence-adj LTM 72.6 | 10.0x | 726.0 | 532.4 | 11.02 | 10.36 |
| | 11.5x | 834.9 | 641.3 | 13.28 | 12.62 |
| | 13.0x | 943.8 | 750.2 | 15.53 | 14.87 |

  - Per share is equity divided by 48.3. For example, 657.4/48.3 = 13.61. The gap to the offer on the guidance midpoint at 11.5x is (24.00 - 13.61)/24.00 = 43.3%, or 46.0% after debt-like items.
  - Note: the 193.6 uses all cash. If roughly 25 of minimum operating cash is treated as trapped, net debt is effectively about 202.5 and each per-share value falls by about $0.18 ((202.5 - 193.6)/48.3).
- **Source:**
  - `adjusted_ebitda_reconciliation.csv`, column LTM_Q2_2026, rows 7 to 11, 16 and 17, plus the restructuring row across all years.
  - `balance_sheet.csv`, column Q2_2026.
  - `data/deal-brief.md`, sections "The deal" and "Valuation basis".
  - [lead: 10-Q guidance; DEF 14A; 10-Q Ruiz accrual].
- **Severity:** Critical
- **Confidence:** High for the arithmetic. Medium for the adjusted EBITDA base, which reflects my judgment on the add-backs.
- **Deal impact:** Valuation (price) and structure.
- **Cross-check:** Confirm the guidance date and figures in the August 6, 2026 8-K. Ask the deal team to rebase model v3. Check sell-side consensus in news. Get the proxy table of change-in-control payments (single or double trigger, cash or equity).

#### FIN-26: Debt-like items and cash needed at closing go well beyond the 193.6 of net debt
- **Finding:** At closing the buyer must repay or refinance 227.5 of gross debt, because a change of control is an event of default. It must also backstop 4.2 of letters of credit and fund 28.6 of change-in-control payments and the 3.2 Ruiz settlement. Total cash-like claims are about 263.5 before Pinecrest, against 33.9 of cash.
- **Evidence:**
  - 227.5 + 4.2 + 28.6 + 3.2 = 263.5. Net of cash: 263.5 - 33.9 = 229.6.
  - Adding the Pinecrest range gives 231.0 to 241.6.
  - H1 2026 free cash flow of -13.0 means cash is falling about 2.2 a month (13.0/6) until closing.
- **Source:** `balance_sheet.csv`, column Q2_2026; `cash_flow.csv`, row 24, column H1_2026; [lead: 10-K Note 9; 10-Q; DEF 14A; court records].
- **Severity:** High
- **Confidence:** High. The items are as given, but the change-in-control trigger terms are unconfirmed.
- **Deal impact:** Financing and valuation (the equity bridge).
- **Cross-check:** Check credit agreement prepayment terms (any make-whole or breakage). Get the proxy's golden parachute table. Check for 8-Ks on new executive agreements entered after the deal approach.

### Positive or mitigating points
- The company's stated 2.26x is arithmetically consistent with its own figures. It does apply the 25.0 cash cap: 202.5/89.7 = 2.26x.
- In the LTM to June 2026, the bill-and-hold nets out, because 9.4 was reversed and 22.4 delivered inside the window. LTM revenue of 498.4 is therefore not inflated by timing.
- Software and services grew about 14% to 15% in H1 2026: software 67.5 against 58.9, services 38.2 against 33.4. FieldOS ARR rose from 139.2 to 146.8.
- Receivables came down: AR net fell from 118.9 to 104.2 and contract assets from 24.7 to 19.5. This fits the bill-and-hold deliveries being collected (working capital inflow of +14.7 + 5.2).
- Because a change of control triggers default, the covenant question is mainly a risk before closing, or if the deal fails. The buyer refinances at closing anyway.

### Gaps and questions for management
1. Provide the full credit agreement definition of Consolidated EBITDA and Permitted Add-backs, plus the Q2 2026 compliance certificate showing the 2.26x build.
2. Provide quarterly EBITDA and add-backs for Q3 2025 through Q2 2026, and the Q3 2026 covenant forecast.
3. Explain how the $9.4m return was booked (revenue reversal in Q2 2026 or a refund liability) and which customer it relates to. Show how the $22.4m of deliveries split between Q1 and Q2 2026.
4. Provide the gross margin on the $31.8m bill-and-hold and hardware segment gross margin by year.
5. Provide the FY2025 bonus payout curve, the bonus definitions of revenue and Adjusted EBITDA, and the clawback policy.
6. State where the Ruiz $3.2m accrual is booked (balance sheet line and P&L line), whether it is in any add-back, and whether any Pinecrest accrual exists.
7. Provide Pinecrest revenue by segment (hardware, FieldOS subscription, services) and the contract's limitation-of-liability clause.
8. Provide the change-in-control payments by person: trigger type, cash or equity, and whether any are already in diluted shares.
9. Explain the restructuring charges that recur every year and the "customer implementation delays" add-back.
10. Confirm minimum operating cash, and whether there is any revolver draw after June 30, 2026.

Relevant files: `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/` (all CSVs listed above) and `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md`.
