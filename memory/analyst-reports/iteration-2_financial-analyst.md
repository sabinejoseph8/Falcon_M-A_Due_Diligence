<!-- Iteration 2, saved unedited by the lead agent on 2026-10-18. -->

## Financial analyst: findings (iteration 2)

### Files reviewed
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/adjusted_ebitda_reconciliation.csv`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/income_statement.csv`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/balance_sheet.csv`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/cash_flow.csv`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/revenue_quarterly.csv`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/revenue_by_customer.csv`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/kpis.csv`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/README.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md`

None of these files contains text that tries to instruct the agents.

The lead agent passed on these facts from the SEC filings. I used them as given and did not re-derive them:
- The covenant definition, from the 10-K FY2025 Note 9.
- The reported 2.26x ratio and the guidance cut, from the 10-Q Q2 2026.
- The $31.8m of bill-and-hold revenue ($24.6m from Norvale) and the $9.4m return, from 10-K Note 2 and the 10-Q.

### Key metrics table (focused on this iteration)

| Metric (US$m) | FY2023 | FY2024 | FY2025 | H1 2026 / LTM Q2 2026 |
|---|---|---|---|---|
| EBITDA (company row) | 42.2 | 52.3 | 64.1 | H1 10.4 / LTM 48.2 |
| Stock-based compensation (SBC) | 11.6 | 13.9 | 17.2 | H1 8.9 / LTM 17.8 |
| Restructuring + other non-recurring add-backs | 6.6 | 8.6 | 17.5 | H1 10.6 / LTM 23.7 |
| Adjusted EBITDA (company) | 60.4 | 74.8 | 98.8 | H1 29.9 / LTM 89.7 |
| All add-backs as % of EBITDA | 43.1% | 43.0% | 54.1% | LTM 86.1% |
| Total debt (revolver + term loan) | 120.0 | 200.0 | 220.0 | Jun 30: 227.5 |
| Cash | 54.8 | 48.3 | 41.6 | Jun 30: 33.9 |
| Covenant net debt (cash netting capped at 25.0) | n/a | n/a | n/a | 202.5 |
| Total Net Leverage, reported (10-Q) | n/a | n/a | n/a | 2.26x |
| Total Net Leverage, recomputed, Reading A | n/a | n/a | n/a | 2.65x |
| Total Net Leverage, recomputed, Reading B | n/a | n/a | n/a | 3.62x (limit 3.50x) |
| Hardware revenue growth, reported | n/a | 11.0% | 15.1% | H1 2026 vs H1 2025: -12.9% |
| Hardware revenue growth, excluding bill-and-hold (adjusted) | n/a | n/a | 2.9% | H1 2026 excluding the 9.4 return: -5.9% |

Workings for the table:
- Add-backs % of EBITDA, LTM: (89.7 - 48.2) / 48.2 = 41.5 / 48.2 = 86.1%.
- FY2025 equivalent: (98.8 - 64.1) / 64.1 = 54.1%.
- FY2024 hardware growth: 261.9 / 236.0 - 1 = 11.0%.

### Findings

#### FIN-015: The reported 2.26x covenant ratio only works with uncapped company Adjusted EBITDA
- **Finding:** The 2.26x in the 10-Q can be reproduced only by dividing capped net debt of 202.5 by the full company Adjusted EBITDA of 89.7. That figure includes 41.5 of add-backs, which is 86.1% of EBITDA. The credit agreement caps Permitted Add-backs at 15%. On the definition as given, the ratio is 2.65x or 3.62x, not 2.26x.
- **Evidence:**
  - Numerator: Total Debt = 45.0 revolver + 182.5 term loan = 227.5. Cash netting = min(33.9, 25.0) = 25.0. Covenant net debt = 227.5 - 25.0 = **202.5**.
  - EBITDA that gives 2.26x: 202.5 / 2.26 = **89.6**. This equals LTM company Adjusted EBITDA of 89.7, and 202.5 / 89.7 = 2.2575, which rounds to 2.26x.
  - Uncapped cash netting does not match: (227.5 - 33.9) / 89.7 = 193.6 / 89.7 = 2.16x. No EBITDA row in the file gives 2.26x with 193.6 as the numerator.
  - So the reported figure applies the 25.0 cash cap but not the 15% add-back cap.
- **Source:**
  - `balance_sheet.csv`: rows "Revolving credit facility", "Term loan" and "Cash and cash equivalents", column Q2_2026.
  - `adjusted_ebitda_reconciliation.csv`: rows "EBITDA" and "Adjusted EBITDA (company definition)", column LTM_Q2_2026.
  - The covenant text and the 2.26x come from the lead agent (10-K Note 9; 10-Q "Covenant compliance").
- **Severity:** High. The covenant disclosure appears overstated, which raises questions about the compliance certificates and the disclosure controls.
- **Confidence:** High on the arithmetic. Medium on the conclusion, because the full credit agreement and the compliance certificate have not been seen.
- **Deal impact:** Financing and closing risk. It also bears on the representations and warranties about SEC reports.
- **Cross-check:**
  - Get the Q2 2026 compliance certificate delivered to the agent bank, and the full credit agreement definitions, including whether "Total Debt" includes finance leases.
  - Read the 10-Q MD&A wording on how the ratio is calculated.
  - Check news for any lender amendment or waiver.

#### FIN-016: Recomputed Jun 30, 2026 leverage passes under Reading A (2.65x) but breaches under Reading B (3.62x vs 3.50x)
- **Finding:** The 15% cap binds under both readings, whichever way the individual add-backs are classified. If SBC counts inside the cap (Reading B), the company was already in breach at Jun 30, 2026.
- **Evidence (LTM_Q2_2026 column):**
  - Covenant EBITDA as defined = net income 4.4 + interest 14.9 + taxes 1.4 + D&A 27.9 = **48.6**.
    - The company's EBITDA row of 48.2 also deducts other income of 0.4. The definition as quoted does not deduct it.
    - Each LTM figure checks: FY2025 - H1 2025 + H1 2026. Net income 18.6 - 5.3 - 8.9 = 4.4. Interest 13.6 - 6.6 + 7.9 = 14.9. Taxes 5.6 - 1.6 - 2.6 = 1.4. D&A 26.8 - 13.0 + 14.1 = 27.9.
  - SBC: 17.8.
  - Classification of the other add-backs:

| Add-back (LTM) | Amount | Classification |
|---|---|---|
| Restructuring and other charges | 9.7 | Permitted (restructuring) |
| Auditor transition costs | 2.3 | Permitted (other non-recurring) |
| Executive search and CFO transition | 2.5 | Permitted (other non-recurring) |
| Cybersecurity incident response | 1.8 | Permitted (other non-recurring) |
| Litigation costs (Vantor patent case) | 4.1 | Doubtful: it has recurred for three years (0.8, 2.1, LTM 4.1) |
| Customer implementation delays | 3.3 | Doubtful: looks like a normal operating cost |
| **Total claimed, excluding SBC** | **23.7** | Clearly permitted items only: 16.3 |

  - **Reading A** (SBC outside the cap):
    - Cap base = 48.6 + 17.8 = 66.4. Cap = 15% x 66.4 = **9.96**.
    - Claimed add-backs are 23.7, or 16.3 if the doubtful items are excluded. Either way they exceed 9.96, so the cap binds.
    - Consolidated EBITDA = 66.4 + 9.96 = **76.36**.
    - Ratio = 202.5 / 76.36 = **2.65x**. That passes the 3.50x limit but is 0.39x above the reported 2.26x.
  - **Reading B** (SBC counts inside the cap):
    - Cap base = 48.6. Cap = 15% x 48.6 = **7.29**.
    - Claimed add-backs = 17.8 + 23.7 = 41.5. SBC alone (17.8) exceeds the cap, so the cap binds.
    - Consolidated EBITDA = 48.6 + 7.29 = **55.89**.
    - Ratio = 202.5 / 55.89 = **3.62x**. That **breaches 3.50x**.
  - Sensitivity using the company EBITDA row of 48.2:
    - Reading A: (48.2 + 17.8) x 1.15 = 75.9, so 202.5 / 75.9 = 2.67x.
    - Reading B: 48.2 x 1.15 = 55.43, so 202.5 / 55.43 = 3.65x.
- **Source:**
  - `adjusted_ebitda_reconciliation.csv`: rows 2 to 5, 8 to 10 and 16 to 20, column LTM_Q2_2026 (also FY2025, H1_2025 and H1_2026 for the LTM check).
  - `balance_sheet.csv`: rows 2, 16 and 17, column Q2_2026.
  - The covenant definition comes from the lead agent (10-K Note 9).
- **Severity:** Critical. Under Reading B there is an existing event of default before signing.
- **Confidence:** High on the calculation. Medium overall, because the result depends on the legal reading of whether "Permitted Add-backs" includes SBC. The quoted sentence lists SBC just before the parenthetical, so it is ambiguous.
- **Deal impact:** Closing risk and financing. A default before closing could allow acceleration of 227.5 of debt.
- **Cross-check:** Ask legal counsel for the full credit agreement text. Check the 10-K and 10-Q for any amendment, waiver or "equity cure" right. Check news for lender talks.

#### FIN-017: The Sep 30, 2026 test at the 3.00x step-down is marginal under Reading A and a clear breach under Reading B
- **Finding:** The Sep 30 test uses the tighter 3.00x limit. Reading A gives a projected 2.84x to 3.35x depending on the proxy, so it passes only on the guidance proxy. Reading B gives about 4.0x or more under every proxy.
- **Evidence:**
  - **Assumptions:**
    - Term loan amortizes 1.25 per quarter. Repayments were 5.0 in FY2025 and 2.5 in H1 2026, per `cash_flow.csv` row 15. So the term loan is 181.25 at Sep 30.
    - Revolver stays flat at 45.0. Cash stays at or above 25.0, so netting is 25.0.
    - Numerator = 226.25 - 25.0 = **201.25**.
    - SBC stays flat at an LTM of 17.8: Q3 2026 4.45 replaces Q3 2025 4.45, from H2 2025 SBC of 17.2 - 8.3 = 8.9.
  - **Q3 2025 EBITDA (no quarterly EBITDA data exists):**
    - H2 2025 EBITDA = 64.1 - 26.3 = 37.8.
    - Split by quarterly revenue: Q3 share = 121.4 / (121.4 + 154.4) = 44.0%, so Q3 2025 EBITDA = **16.6**.
    - Alternative even split: 18.9.
  - **Proxy 1, guidance:**
    - FY2026 Adjusted EBITDA midpoint 74.0 implies H2 2026 Adjusted EBITDA = 74.0 - 29.9 = 44.1.
    - Less H2 add-backs assumed equal to H1 (29.9 - 10.4 = 19.5) gives H2 EBITDA = 24.6, so Q3 2026 = 12.3.
    - LTM Sep EBITDA = 48.2 + 12.3 - 16.6 = **43.9** (41.6 with the even split).
    - Reading A: (43.9 + 17.8) x 1.15 = 70.96, so 201.25 / 70.96 = **2.84x** (even split: 68.31, giving 2.95x).
    - Reading B: 43.9 x 1.15 = 50.49, so 201.25 / 50.49 = **3.99x** (even split: 4.21x).
  - **Proxy 2, H1 run-rate:**
    - Q3 2026 EBITDA = 10.4 / 2 = 5.2.
    - LTM = 48.2 + 5.2 - 16.6 = 36.8.
    - Reading A: (36.8 + 17.8) x 1.15 = 62.79, so 201.25 / 62.79 = **3.21x (breach)**. With the even split it is 3.35x.
  - **Company method (uncapped Adjusted EBITDA), for comparison:**
    - H2 2025 Adjusted EBITDA = 98.8 - 39.0 = 59.8, so Q3 2025 = 59.8 x 44.0% = 26.3.
    - LTM = 89.7 + 22.05 - 26.3 = 85.45, so 201.25 / 85.45 = 2.36x. That passes.
  - The Q4 2025 bill-and-hold quarter is still inside the Sep 30 LTM.
- **Source:**
  - `adjusted_ebitda_reconciliation.csv`: rows "EBITDA", "Stock-based compensation" and "Adjusted EBITDA", columns FY2025, H1_2025, H1_2026 and LTM_Q2_2026.
  - `revenue_quarterly.csv`: rows Q3 2025 and Q4 2025.
  - `balance_sheet.csv`: rows 16 and 17, column Q2_2026.
  - `cash_flow.csv`: rows 15 and 16.
  - The guidance comes from the lead agent (10-Q).
- **Severity:** High under Reading A. It would be Critical under Reading B, because the test date falls before the Nov 6 IC meeting and the Nov 20 exclusivity expiry.
- **Confidence:** Medium. The quarterly EBITDA split and the H2 add-back level are my assumptions.
- **Deal impact:** Closing risk and financing.
- **Cross-check:** The Q3 2026 10-Q (due around early November), which should report the Sep 30 ratio. News on any amendment or waiver.

#### FIN-018: The Dec 31, 2026 test fails under Reading A across the whole guidance range, once the bill-and-hold quarter leaves the LTM
- **Finding:** At Dec 31, 2026 the LTM equals FY2026. Q4 2025, with its 31.8 of bill-and-hold revenue, drops out, but the 9.4 return stays in. Reading A gives 3.06x to 3.56x against the 3.00x limit, so the covenant fails even at the top of guidance. Reading B gives about 5.0x.
- **Evidence:**
  - **Assumptions:** numerator = (45.0 + 180.0) - 25.0 = **200.0**. FY2026 SBC = 8.9 x 2 = 17.8. H2 add-backs = 19.5.
  - **Guidance midpoint:**
    - FY2026 EBITDA = 10.4 + (44.1 - 19.5) = **35.0**.
    - Reading A: (35.0 + 17.8) x 1.15 = 60.72, so 200.0 / 60.72 = **3.29x**.
    - Reading B: 35.0 x 1.15 = 40.25, so 200.0 / 40.25 = **4.97x**.
  - **Guidance low (70.0):**
    - H2 Adjusted EBITDA = 40.1, so EBITDA = 31.0.
    - Reading A: 56.12, so 200.0 / 56.12 = **3.56x**.
  - **Guidance high (78.0):**
    - H2 Adjusted EBITDA = 48.1, so EBITDA = 39.0.
    - Reading A: 65.32, so 200.0 / 65.32 = **3.06x**.
  - **H1 run-rate:**
    - FY2026 EBITDA = 20.8.
    - Reading A: 44.39, so 200.0 / 44.39 = 4.51x.
    - Company method: 200.0 / 59.8 = 3.34x, which breaches even on the company's own basis.
  - **Guidance assumes a strong second half:**
    - H2 Adjusted EBITDA of 44.1 is 47.5% above H1's 29.9 (44.1 / 29.9 = 1.475).
    - The 9.4 return stays in the LTM until the Jun 30, 2027 test.
- **Source:**
  - `adjusted_ebitda_reconciliation.csv`: H1_2026 column, rows "EBITDA", "Stock-based compensation" and "Adjusted EBITDA".
  - `balance_sheet.csv`: Q2_2026 debt rows.
  - `cash_flow.csv`: row 15.
  - The guidance and bill-and-hold facts come from the lead agent (10-Q; 10-K Note 2).
- **Severity:** Critical. A one-step public merger is unlikely to close before Dec 31, 2026, so a default before closing is likely under Reading A unless the H2 ramp beats the top of guidance.
- **Confidence:** Medium. It is a projection based on guidance and my assumption about add-backs.
- **Deal impact:** Closing risk and financing. The buyer may face lender demands for waiver fees between signing and closing.
- **Cross-check:** The lender syndicate's view, any amendment discussions (news), and the FY2026 budget by quarter (management).

#### FIN-019: The cure amounts are large compared with liquidity
- **Finding:** Under Reading B, the Jun 30 breach could be cured on paper with 6.9 of debt paydown from cash above the 25.0 netting cap. Later tests need much more, while free cash flow is negative and cash is falling.
- **Evidence:** "Reduce debt" means repaying debt with cash above 25.0, or new equity. Each 1.0 of underlying EBITDA adds 1.15 to Consolidated EBITDA because the cap binds.

| Test date | Reading | Cons. EBITDA | Required for limit | Cushion (+) / shortfall (-) | Debt capacity (+) / debt cure needed (-) |
|---|---|---|---|---|---|
| Jun 30 (3.50x) | A | 76.36 | 202.5/3.5 = 57.86 | +18.5 (underlying +16.1) | 3.5 x 76.36 - 202.5 = +64.8 |
| Jun 30 (3.50x) | B | 55.89 | 57.86 | -1.97 (underlying -1.71) | 3.5 x 55.89 = 195.6, so -6.9 |
| Sep 30 (3.00x), guidance | A | 70.96 | 201.25/3 = 67.08 | +3.9 (even split: +1.2) | +11.6 (even split: +3.7) |
| Sep 30, run-rate | A | 62.79 | 67.08 | -4.3 | -12.9 |
| Sep 30, guidance | B | 50.49 | 67.08 | -16.6 | 3 x 50.49 = 151.5, so -49.8 |
| Dec 31, guidance mid | A | 60.72 | 200.0/3 = 66.67 | -5.95 (underlying -5.2) | 3 x 60.72 = 182.2, so -17.8 |
| Dec 31, guidance low / high | A | 56.12 / 65.32 | 66.67 | -10.5 / -1.35 | -31.6 / -4.0 |
| Dec 31, guidance mid | B | 40.25 | 66.67 | -26.4 | 3 x 40.25 = 120.75, so -79.25 |

  - Liquidity:
    - Excess cash above the netting cap at Jun 30 = 33.9 - 25.0 = **8.9**.
    - H1 2026 free cash flow = -13.0 and net change in cash = -7.7.
    - If that burn continues, cash at Dec 31 is about 33.9 - 7.7 = 26.2, leaving about 1.2 of excess.
    - LTM interest cover = EBITDA 48.2 / interest 14.9 = 3.23x.
  - Revolver capacity and availability are not in the data.
- **Source:**
  - `balance_sheet.csv`: rows 2, 16 and 17.
  - `cash_flow.csv`: rows 22 and 24, column H1_2026.
  - `adjusted_ebitda_reconciliation.csv`: LTM_Q2_2026 column.
- **Severity:** High. Under the calibration rule this rises to Critical if a default occurs before closing (see FIN-016 and FIN-018).
- **Confidence:** Medium, for the projection assumptions given in FIN-017 and FIN-018.
- **Deal impact:** Financing, and the price paid for the equity. Arbelion would refinance at closing anyway because a change of control is an event of default.
- **Cross-check:** Revolver commitment size and availability (10-K Note 9). Any equity-cure provision. Lender communications.

#### FIN-020: FY2025 hardware growth excluding bill-and-hold is about 2.9%, not 15.1%
- **Finding:** Removing the 31.8 of Q4 2025 bill-and-hold revenue cuts FY2025 hardware growth from 15.1% to 2.9%, and total growth from 19.1% to 11.6%. There is no quarterly segment data, so Q4 hardware cannot be isolated. At the total level, Q4 2025 excluding bill-and-hold grew 5.1%, against a reported 32.4%.
- **Evidence:**
  - Hardware:
    - Reported: 301.4 / 261.9 - 1 = **15.1%**.
    - Adjusted: (301.4 - 31.8) / 261.9 - 1 = 269.6 / 261.9 - 1 = **2.9%**.
  - Total revenue:
    - Reported: 502.3 / 421.7 - 1 = 19.1%.
    - Adjusted: 470.5 / 421.7 - 1 = **11.6%**.
  - Q4 total:
    - Reported: 154.4 / 116.6 - 1 = 32.4%.
    - Adjusted: (154.4 - 31.8) / 116.6 - 1 = 122.6 / 116.6 - 1 = **5.1%**.
  - Q2 2026 total:
    - Reported: 112.9 / 117.6 - 1 = -4.0%.
    - Adding back the 9.4 return: 122.3 / 117.6 - 1 = **+4.0%**.
  - H1 2026 hardware:
    - Reported: 116.9 / 134.2 - 1 = -12.9%.
    - Adding back 9.4: 126.3 / 134.2 - 1 = **-5.9%**.
  - Norvale:
    - Reported: 156.2 / 118.1 - 1 = 32.3%.
    - Excluding 24.6 of bill-and-hold: 131.6 / 118.1 - 1 = **11.4%**.
    - Adjusted Norvale share = 131.6 / 470.5 = 28.0%, against a reported 31.1%.
  - Guidance midpoint revenue of 480.0 is 4.4% below FY2025 reported (480.0 / 502.3 - 1). It is 2.0% above FY2025 excluding bill-and-hold (480.0 / 470.5 - 1).
- **Source:**
  - `income_statement.csv`: row 2 (Hardware) and row 5 (Total revenue), columns FY2024, FY2025, H1_2025 and H1_2026.
  - `revenue_quarterly.csv`: rows Q4 2024, Q2 2025, Q4 2025 and Q2 2026.
  - `revenue_by_customer.csv`: row 1 (Norvale).
  - The bill-and-hold amounts come from the lead agent (10-K Note 2; 10-Q).
- **Severity:** High.
- **Confidence:** High on the annual figures. Medium on the H1 2026 hardware figure, because I assume the 9.4 return was all hardware.
- **Deal impact:** Valuation.
- **Cross-check:** Quarterly segment revenue (management). Whether any further bill-and-hold units remain uncollected (10-Q). Norvale contract terms.

#### FIN-021: Valuation confirmed. 11.46x on guidance implies about $13.55 per share
- **Finding:** I confirm EV of 1,352.8 and 18.3x on the 74.0 guidance midpoint. Applying the deal model's 11.46x to 74.0 gives $13.55 per share. That is 43.5% below the $24.00 offer and 24.1% below the $17.85 market price.
- **Evidence:**
  - Equity value = 24.00 x 48.3 = 1,159.2. Net debt = 227.5 - 33.9 = 193.6. **EV = 1,352.8** (confirmed).
  - Deal model multiple: 1,352.8 / 118.0 = **11.46x** (confirmed).
  - On guidance midpoint: 1,352.8 / 74.0 = **18.28x, so 18.3x** (confirmed).
  - On LTM figures: 1,352.8 / 89.7 = 15.1x on Adjusted EBITDA, and 1,352.8 / 48.2 = 28.1x on EBITDA.
  - Implied value at 11.46x on 74.0:
    - EV = 11.46 x 74.0 = 848.0. Equity = 848.0 - 193.6 = 654.4. Per share = 654.4 / 48.3 = **$13.55**.
    - Guidance range: at 70.0, 802.2 - 193.6 = 608.6, or **$12.60**. At 78.0, 893.9 - 193.6 = 700.3, or **$14.50**.
  - Equity value gap = 1,159.2 - 654.4 = 504.8, which is 43.5% of the offer.
- **Source:**
  - `income_statement.csv`: row 19 (H1_2026 diluted shares 48.3).
  - `balance_sheet.csv`: rows 2, 16 and 17 (Q2_2026).
  - `adjusted_ebitda_reconciliation.csv`: LTM_Q2_2026 column.
  - Deal brief: price, the 118.0 and the $17.85.
  - Guidance comes from the lead agent (10-Q).
- **Severity:** Critical. The value change is well above 10%.
- **Confidence:** High on the arithmetic. Medium on the conclusion, because guidance could be revised again.
- **Deal impact:** Valuation.
- **Cross-check:** The deal model v3 inputs. Analyst consensus after Aug 6 (news). Whether the deal model's net debt should use a closing-date figure, which would be higher if cash burn continues.

#### FIN-022: Classifying the add-backs does not change the covenant result, but two items look like operating costs
- **Finding:** Vantor litigation (4.1) and customer implementation delays (3.3) look recurring or operational, but excluding them does not change the covenant result because the 15% cap binds anyway. For valuation, removing them lowers LTM Adjusted EBITDA from 89.7 to 82.3. "Total Debt" may also include finance leases, which are not in the debt rows.
- **Evidence:**
  - Vantor litigation costs: 0.8 in FY2024, 2.1 in FY2025, 4.1 LTM.
  - Customer implementation delays: 4.1 in FY2025, 3.3 LTM.
  - Clearly permitted items alone are 16.3, already more than the Reading A cap of 9.96.
  - Adjusted EBITDA excluding both items = 89.7 - 4.1 - 3.3 = 82.3. EV / 82.3 = 16.4x.
  - Finance lease payments of 0.7 in H1 2026 (`cash_flow.csv` row 20) suggest lease liabilities exist, probably within "Other liabilities" of 6.5 (`balance_sheet.csv` row 18). That amount is not quantified.
- **Source:**
  - `adjusted_ebitda_reconciliation.csv`: rows 16 and 17.
  - `cash_flow.csv`: row 20.
  - `balance_sheet.csv`: row 18.
- **Severity:** Medium.
- **Confidence:** Medium. Classifying the add-backs is a judgment call.
- **Deal impact:** Valuation and financing.
- **Cross-check:** The litigation workstream on the Vantor case status. A quality of earnings report, which has not been received yet. The credit agreement definition of "Total Debt".

### Positive or mitigating points
- At Jun 30, 2026, Reading A shows compliance at 2.65x, with 18.5 of Consolidated EBITDA cushion and 64.8 of debt capacity (FIN-016, FIN-019).
- The Jun 30 breach under Reading B is small: 6.9 of debt paydown would cure it, and 8.9 of cash sits above the netting cap.
- The change-of-control default means Arbelion would refinance at closing anyway. Any existing default mainly affects risk between signing and closing, not the long-term structure.
- Excluding bill-and-hold, revenue still grew 11.6% in FY2025, and Q2 2026 grew 4.0% after adding back the return. The underlying business is growing, just slowly (FIN-020).
- FieldOS ARR rose from 139.2 to 146.8 in H1 2026 (`kpis.csv` row 2), although net revenue retention fell from 118% to 111%.

### Gaps and questions for management
1. Provide the full credit agreement, including the definitions of "Total Debt", "Consolidated EBITDA" and "Permitted Add-backs", any equity-cure right, and all amendments and waivers.
2. Provide the Q2 2026 compliance certificate and covenant calculation. Explain how 2.26x was computed and why the 15% cap was not applied.
3. Provide the Q3 2026 covenant calculation (Sep 30, 3.00x test) and the forecast ratio at Dec 31, 2026.
4. Provide quarterly EBITDA, add-backs and segment revenue for Q1 2024 to Q2 2026. Only total quarterly revenue is in `revenue_quarterly.csv`.
5. Provide the FY2026 H2 bridge: which drivers support the 47.5% step-up in H2 Adjusted EBITDA over H1?
6. Provide the revolver commitment, current availability, letters of credit and any finance lease liabilities.
7. Confirm that the 9.4 return was entirely hardware, and whether any other bill-and-hold arrangements are open.
8. Explain the nature of the "Customer implementation delays" add-back, and the expected end date and total cost of the Vantor litigation.
