## Financial analyst: findings (iteration 2: FIN-17 to FIN-23)

### Files reviewed
- `data/financials/`: adjusted_ebitda_reconciliation.csv, income_statement.csv, revenue_quarterly.csv, balance_sheet.csv, cash_flow.csv, revenue_by_customer.csv, kpis.csv, README.md.
- `data/deal-brief.md`: offer $24.00, 48.3M diluted shares, deal model FY2026E Adjusted EBITDA of 118.0.
- Facts from other sources came from the lead and are cited as given: 10-K Note 9, Note 2 and Item 1; 10-Q Q2 2026; DEF 14A 2026; litigation records. I did not open those files.
- **FIN-05 caveat:** I am not allowed to read `memory/`, so I cannot see the FIN-05 figure from iteration 1. I recomputed LTM diligence-adjusted EBITDA as 76.7 (method in FIN-23). If the register shows a different FIN-05 figure, value changes by $0.24 per share for each $1.0M of EBITDA (11.46 / 48.3).

### Key numbers (US$ millions unless stated)

| Item | Value | Basis |
|---|---|---|
| Covenant Consolidated EBITDA, LTM Q2 2026 | 76.4 | Base 66.4 plus add-backs capped at 10.0 (23.7 claimed) |
| Covenant net debt, Jun 30, 2026 | 202.5 | Debt 227.5 less cash netting capped at 25.0 |
| Total Net Leverage Ratio, Jun 30, 2026 | 2.65x recomputed vs 2.26x reported | The 2.26x needs EBITDA of 89.6, which is company Adjusted EBITDA (89.7) with no cap |
| Cushion vs 3.00x | 8.9 of covenant EBITDA (11.6%) | Equal to a 7.7 fall in EBITDA before add-backs |
| Ratio at Dec 31, 2026: guidance low / mid / high | 3.55x / 3.28x / 3.05x | H2 add-backs equal H1; net debt 200.0 |
| Most H2 2026 add-backs that still pass 3.00x | 1.6 / 5.6 / 9.6 | H1 2026 actual: 10.6 |
| FY2025 growth: reported / without bill-and-hold | 19.1% / 11.6% | 502.3 and 470.5 vs 421.7 |
| Q4 2025 growth: reported / without bill-and-hold | 32.4% / 5.1% | 154.4 and 122.6 vs 116.6 |
| H1 2026 growth: reported / without 9.4 / without 9.4 and 2.3 | -1.7% / 2.4% / 3.4% | vs 226.5 |
| Norvale FY2025 share: reported / without its 24.6 | 31.1% / 28.0% | FY2024: 28.0% |
| Bonus test: revenue without bill-and-hold vs threshold | 470.5 vs 470.0 | Clears by 0.5 |
| Bonus test: bill-and-hold gross margin that sinks the 88.0 EBITDA threshold | above 34.0% | Reported gross margins 38.0% to 41.3% |
| Pinecrest claim vs its FY2025 revenue | 12.0 vs 17.4 (69.0%) | Rank 4, 3.5% share |
| Value per share at 11.46x: guidance low / mid / high | $12.60 / $13.55 / $14.50 | Offer is $24.00 |
| Value per share at 11.46x: LTM diligence-adjusted (76.7) | $14.19 | |
| Vantor as a debt-like item, pre-tax (96.4 / 140.0) | -$2.00 / -$2.90 per share | |

### Findings

#### FIN-17: The reported 2.26x leaves out the 15% add-back cap; on the Note 9 definition the ratio is 2.65x
- **Finding:** Under the definition, LTM Q2 2026 Consolidated EBITDA is 76.4. The reported 2.26x implies 89.6. On my main reading of the definition, Talonfield passed the 3.50x test at Jun 30, 2026. Its cushion against the 3.00x test that starts Sep 30, 2026 is only 8.9 (11.6%), not the 22.2 the company's basis suggests.
- **Evidence:**
  - LTM inputs: net income 4.4, interest 14.9, taxes 1.4, D&A 27.9, SBC 17.8, restructuring 9.7, other non-recurring 14.0.
  - EBITDA before Permitted Add-backs = 4.4 + 14.9 + 1.4 + 27.9 + 17.8 = 66.4. SBC is listed before the defined term. The definition does not deduct the 0.4 of other income.
  - Permitted Add-backs claimed = 9.7 + 14.0 = 23.7, which is 35.7% of 66.4. Cap = 15% x 66.4 = 9.96. Amount disallowed = 23.7 - 9.96 = 13.74.
  - Consolidated EBITDA = 66.4 + 9.96 = 76.36.
  - Total Debt = 45.0 revolver + 182.5 term loan = 227.5. Cash is 33.9, but netting is capped at 25.0. Net debt = 202.5.
  - Ratio = 202.5 / 76.36 = 2.65x.
  - **Reconciling to 2.26x:** 202.5 / 2.26 = 89.6, which is the company's LTM Adjusted EBITDA (202.5 / 89.7 = 2.2575, which rounds to 2.26x). No other basis rounds to 2.26x:
    - uncapped cash: 193.6 / 89.7 = 2.16x;
    - definition without the cap: 202.5 / (66.4 + 23.7 = 90.1) = 2.25x.
  - So the reported ratio applies the cash cap but not the add-back cap.
  - **Cushion at 3.00x:** minimum EBITDA = 202.5 / 3.00 = 67.5, so the cushion is 76.36 - 67.5 = 8.86. Because the cap binds, covenant EBITDA = 1.15 x base, so base EBITDA can fall only 66.4 - 67.5 / 1.15 = 66.4 - 58.70 = 7.70. Room for extra net debt at 3.00x = 3.00 x 76.36 - 202.5 = 26.6.
  - **Second reading (SBC counted inside the cap):** base 48.6, cap 7.29, Consolidated EBITDA 55.89, ratio 3.62x. That would have been a breach of 3.50x at Jun 30, 2026. The wording favors the first reading, but only the credit agreement can settle it.
- **Source:** `data/financials/adjusted_ebitda_reconciliation.csv`, LTM_Q2_2026 column, rows "Net income" to "Adjusted EBITDA"; `data/financials/balance_sheet.csv`, Q2_2026 column, rows "Cash and cash equivalents", "Revolving credit facility", "Term loan"; 10-K Note 9 and 10-Q Q2 2026 (supplied by lead).
- **Severity:** High
- **Confidence:** Medium. The math is direct, but the result depends on the credit agreement matching the Note 9 summary (how the cap works, how SBC is treated, and whether Total Debt includes leases or letters of credit).
- **Deal impact:** Financing and closing risk. It is also a disclosure and controls question, because the 10-Q ratio does not follow the definition as the 10-K summarizes it.
- **Cross-check:** The credit agreement and any amendments; the Jun 30, 2026 compliance certificate sent to lenders; how the 10-Q describes its calculation.

#### FIN-18: On revised guidance, breaching 3.00x at Dec 31, 2026 is more likely than not
- **Finding:** If H2 2026 add-backs run at the H1 rate, the Dec 31, 2026 ratio is 3.55x (low), 3.28x (mid) and 3.05x (high), above 3.00x across the whole guidance range. To pass, H2 restructuring and non-recurring charges must fall from 10.6 in H1 to at most 1.6 (low), 5.6 (mid) or 9.6 (high).
- **Assumptions:**
  1. LTM at Dec 31, 2026 = FY2026. Company Adjusted EBITDA = 70.0 / 74.0 / 78.0 (10-Q outlook).
  2. FY2026 Permitted Add-backs = 2 x H1 (4.4 + 6.2 = 10.6) = 21.2.
  3. FY2026 SBC = 2 x 8.9 = 17.8. It sits in both Adjusted EBITDA and the covenant base, so it cancels out.
  4. Other income = 2 x 0.1 = 0.2.
  5. Total Debt = 225.0: term loan 182.5 less a scheduled 2.5 H2 repayment (cash_flow.csv shows 2.5 per half-year), plus the revolver flat at 45.0. Cash stays above 25.0. Net debt = 200.0.
  6. No amendment, no pro forma add-backs, no litigation accruals.
- **Method:** base = Adjusted EBITDA - add-backs + other income. Consolidated EBITDA = base + the lower of (add-backs, 15% x base). Check on LTM Q2 2026: 89.7 - 23.7 + 0.4 = 66.4, which matches FIN-17.

| Guidance | Adj. EBITDA | Base | Capped add-backs | Consolidated EBITDA | Ratio, net debt 200.0 | Ratio, net debt 210.0 | Company basis (200.0 / Adj. EBITDA) |
|---|---|---|---|---|---|---|---|
| Low | 70.0 | 49.0 | 7.35 | 56.35 | 3.55x | 3.73x | 2.86x |
| Mid | 74.0 | 53.0 | 7.95 | 60.95 | 3.28x | 3.45x | 2.70x |
| High | 78.0 | 57.0 | 8.55 | 65.55 | 3.05x | 3.20x | 2.56x |

- **Evidence:**
  - The 210.0 column assumes the revolver draws another 10.0, as it did in H1 2026.
  - Best case, with no H2 add-backs at all (FY total 10.6): base 59.6 / 63.6 / 67.6, x 1.15 = 68.54 / 73.14 / 77.74, giving 2.92x / 2.73x / 2.57x.
  - **Break-even:** passing 3.00x needs 200.0 / 3.00 = 66.67 of Consolidated EBITDA, so a base of 66.67 / 1.15 = 57.97. Maximum FY add-backs = Adjusted EBITDA + 0.2 - 57.97 = 12.2 / 16.2 / 20.2. Less the 10.6 already booked in H1, that leaves 1.6 / 5.6 / 9.6 for H2. Vantor defense costs alone were 3.0 in H1 2026.
  - On the company's uncapped basis, the low case passes, but with only 70.0 - 66.67 = 3.3 of EBITDA to spare.
  - **Multiplier:** while the cap binds, each 1.0 of new charge (a settlement accrual, deal costs, restructuring) cuts Consolidated EBITDA by 1.15: the base falls 1.0 and the cap falls 0.15. A charge equal to the 12.0 Pinecrest claim would cut it by 13.8, more than the whole Jun 30 cushion.
  - **Sep 30, 2026** (first 3.00x test) cannot be computed because there is no quarterly EBITDA. Rough guide:
    - H2 2025 base = 66.4 - H1 2026 base (-8.9 + 7.9 - 2.6 + 14.1 + 8.9 = 19.4) = 47.0.
    - Guided H2 2026 base = (70.0 or 78.0) - 29.9 - 10.6 + 0.1 = 29.6 to 37.6.
    - If that decline were split evenly between Q3 and Q4, Sep 30 would come out at 3.05x (low) to 2.85x (high).
    - Q4 2025 held the bill-and-hold profit, so more of the decline should land in Q4. Dec 31 is the harder test.
- **Source:** `adjusted_ebitda_reconciliation.csv` (H1_2026 and LTM columns); `income_statement.csv` (H1_2026 SBC and other income); `cash_flow.csv` (term loan and revolver rows); `balance_sheet.csv` (Q2_2026); 10-K Note 9 and 10-Q outlook (supplied).
- **Severity:** High. It becomes Critical if the Sep 30 certificate applies the cap and fails.
- **Confidence:** Medium. The result is driven by the assumptions above; the break-even shows how sensitive it is.
- **Deal impact:** Closing and financing.
  - A breach between signing and closing is an event of default, so lenders could demand fees, tighter terms or repayment.
  - Change of control is a default anyway, so the risk sits in the period before closing.
  - Protections to ask for: a no-default representation that is confirmed again at closing, limits on new debt and charges before closing, and Arbelion standing ready to fund a waiver or refinancing.
- **Cross-check:** The Q3 2026 10-Q and Sep 30 compliance certificate; any 8-K on a credit amendment; management's H2 restructuring plan.

#### FIN-19: Without bill-and-hold, FY2025 growth is 11.6%, not 19.1%, and the slowdown began in Q4 2025
- **Finding:** Without the 31.8 of bill-and-hold revenue, Q4 2025 growth drops from 32.4% to 5.1%, against 14.4% in Q3 2025. FY2025 hardware grew only 2.9%. Without the 9.4 reversal, H1 2026 growth is +2.4% (+3.4% if the 2.3 of credits are also excluded), not -1.7%.

| Period | Reported | Adjustment | Normalized | Prior-year period | Reported growth | Normalized growth |
|---|---|---|---|---|---|---|
| Q4 2025 | 154.4 | -31.8 | 122.6 | 116.6 | 32.4% | 5.1% (6.0 / 116.6) |
| FY2025 | 502.3 | -31.8 | 470.5 | 421.7 | 19.1% | 11.6% (48.8 / 421.7) |
| FY2025 hardware | 301.4 | -31.8 | 269.6 | 261.9 | 15.1% | 2.9% (7.7 / 261.9) |
| Q2 2026 | 112.9 | +9.4 | 122.3 | 117.6 | -4.0% | 4.0% (4.7 / 117.6) |
| Q2 2026, also without SLA credits | 112.9 | +11.7 | 124.6 | 117.6 | -4.0% | 6.0% (7.0 / 117.6) |
| H1 2026 | 222.6 | +9.4 | 232.0 | 226.5 | -1.7% | 2.4% (5.5 / 226.5) |
| H1 2026, also without SLA credits | 222.6 | +11.7 | 234.3 | 226.5 | -1.7% | 3.4% (7.8 / 226.5) |
| H1 2026 hardware | 116.9 | +9.4 | 126.3 | 134.2 | -12.9% | -5.9% (-7.9 / 134.2) |

- **Evidence:**
  - Year-on-year growth in Q1 to Q3 2025 was 13.2%, 14.4% and 14.4% (108.9 / 96.2, 117.6 / 102.8, 121.4 / 106.1). Q1 2026 was +0.7% (109.7 / 108.9).
  - Bill-and-hold was 39.5% of FY2025 growth (31.8 / 80.6) and 20.6% of Q4 2025 revenue (31.8 / 154.4).
  - FY2026 guidance (470.0 to 490.0) vs normalized FY2025 (470.5) is -0.1% to +4.1%. With the 9.4 reversal also excluded from 2026 (479.4 to 499.4), it is +1.9% to +6.1%.
  - **Caveat:** these figures exclude the bill-and-hold from both years. If part of the 22.4 that was not returned (31.8 - 9.4) was delivered in H1 2026, H1 2026 revenue on a delivery basis would be higher by that amount, up to 254.4 (+12.3%).
  - I would not normalize the 2.3 SLA credits for valuation, because they are a cost of service failures.
- **Double count:** The 9.4 is part of the 31.8, not a separate item: the same goods were booked in Q4 2025 and reversed in Q2 2026.
  - Restating each period on its own, as the table does, does not double count. Q4 2025 loses the 31.8, which already contains the 9.4, and Q2 2026 loses the 9.4 reversal. Across the two periods the 9.4 nets to zero, just as it does in the reported figures. So I disagree slightly with the premise of the request.
  - The double count happens in two specific uses:
    - **(a) LTM to Jun 30, 2026.** This window already holds both the +9.4 and the -9.4, so its net bill-and-hold content is 22.4. The correct normalized LTM is 498.4 - 31.8 + 9.4 = 476.0. Removing 31.8 but keeping the reversal (466.6) takes the 9.4 out twice. Describing the problem as "31.8 overstated plus 9.4 understated" (41.2) counts the same goods twice.
    - **(b) Pull-forward view.** Treating the 31.8 as 2026 demand pulled into 2025, and also adding back the 9.4, credits 2026 twice for goods that went back to inventory and were never sold. At most 22.4 can be pulled-forward demand, and only once it is delivered.
  - Rule: remove the 9.4 once where it was booked (Q4 2025) and its reversal once where that was booked (Q2 2026). Never count it as 2026 demand.
- **Source:** `revenue_quarterly.csv` (all rows); `income_statement.csv` (revenue rows, FY2024, FY2025, H1_2025, H1_2026); 10-K Note 2 and 10-Q Q2 2026 (supplied).
- **Severity:** High
- **Confidence:** High for the math. Medium for comparability: the Q4 2024 bill-and-hold amount is unknown, and FY2025 includes Lumora (acquired in FY2024 per `cash_flow.csv`), so organic growth is lower still.
- **Deal impact:** Valuation (IC question 1). The model's revenue base should be 470.5, not 502.3.
- **Cross-check:** 10-K bill-and-hold criteria and evidence that the customer requested it; the 10-Q note on the return; the auditor's critical audit matters; whether there was any bill-and-hold in Q4 2024.

#### FIN-20: Norvale's growth was mostly bill-and-hold, and its normalized share is flat at 28.0%
- **Finding:** Without its 24.6 of bill-and-hold, Norvale's FY2025 revenue is 131.6. That is growth of 11.4%, not 32.3%, and a share of 28.0%, not 31.1%, the same as FY2024. All of the reported rise in concentration came from bill-and-hold, and so did 64.6% of Norvale's reported growth.
- **Evidence:**
  - 156.2 - 24.6 = 131.6. Growth = 13.5 / 118.1 = 11.4%, vs 38.1 / 118.1 = 32.3% reported.
  - Share = 131.6 / 470.5 = 28.0%. The denominator removes all 31.8, because the other 7.2 belongs to other customers.
  - 24.6 / 38.1 = 64.6% of Norvale's growth. 24.6 / 31.8 = 77.4% of all bill-and-hold.
  - Norvale's share of total growth: 47.3% reported (38.1 / 80.6) vs 27.7% normalized (13.5 / 48.8).
- **Source:** `revenue_by_customer.csv`, Norvale row and Total row; 10-K Note 2 and Item 1 (supplied).
- **Severity:** High. One customer still holds 28.0% of revenue, and that customer took 77.4% of the bill-and-hold.
- **Confidence:** High for the math. The supplied facts do not say whose products were returned in Q2 2026.
- **Deal impact:** Valuation and post-closing customer risk (IC question 3).
- **Cross-check:** Which customer was behind the 9.4 return (10-Q); Norvale's contract terms and renewal date; news on Norvale capex or destocking.

#### FIN-21: The bill-and-hold sales were probably decisive for the 142% bonus payout
- **Finding:** Without the bill-and-hold, FY2025 revenue (470.5) clears the 470.0 threshold by only 0.5. Adjusted EBITDA would fall below the 88.0 threshold if those sales carried a gross margin above 34.0%. Every gross margin in the data is higher than that.
- **Evidence:**
  - **Revenue:** 502.3 - 31.8 = 470.5, which is 0.5 (0.1%) above the threshold. The reported 502.3 sat between target (490.0) and maximum (510.0).
  - **EBITDA:** headroom = 98.8 - 88.0 = 10.8, so the break-even gross margin = 10.8 / 31.8 = 34.0%.
  - **Reported gross margins:** FY2023 147.9 / 368.9 = 40.1%; FY2024 172.1 / 421.7 = 40.8%; FY2025 206.3 / 502.3 = 41.1%; H2 2025 113.9 / 275.8 = 41.3%; H1 2026 84.6 / 222.6 = 38.0%.
  - At 41.1%, gross profit on the bill-and-hold is 13.1, so Adjusted EBITDA would be 85.7 (2.3 below threshold). At 38.0%, it is 12.1, giving 86.7.
  - Hardware-only margin is not in the data. It would have to be below 34.0% for the EBITDA measure to clear. Commissions or freight on those sales would lower the break-even further.
- **Source:** `income_statement.csv` (Total revenue and Gross profit rows); `adjusted_ebitda_reconciliation.csv` (FY2025 Adjusted EBITDA 98.8); DEF 14A and 10-K Note 2 (supplied).
- **Severity:** High (governance, IC question 5).
- **Confidence:** Medium. The hardware margin and the plan's payout at threshold were not available.
- **Deal impact:** Governance and post-closing: clawback, retention terms, and a reason to review Q4 2025 revenue recognition forensically. This is an incentive concern, not evidence of intent.
- **Cross-check:** The DEF 14A payout curve and any committee discretion; the clawback policy; audit committee minutes on bill-and-hold.

#### FIN-22: Pinecrest's 12.0 claim equals 69.0% of a year's revenue from it
- **Finding:** Pinecrest is the fourth-largest customer: 17.4 in FY2025, 3.5% of revenue, up 7.4%. Its claim equals 69.0% of a year's revenue from Pinecrest and about 1.7 years of the gross profit it generates. Talonfield's cap estimate (1.4) is 8.0% of that revenue. The relationship is at risk, not just the claim amount.
- **Evidence:**
  - 12.0 / 17.4 = 69.0%; 1.4 / 17.4 = 8.0%. The gap between claim and cap is 10.6.
  - Gross profit at 41.1% = 17.4 x 41.1% = 7.1, so 12.0 / 7.1 = 1.7 years.
  - The claim is 2.4% of FY2025 revenue (12.0 / 502.3), or $0.25 per share (12.0 / 48.3).
  - Share without bill-and-hold = 17.4 / 470.5 = 3.7%, assuming none of the 7.2 non-Norvale bill-and-hold was Pinecrest's.
  - A charge above the cap would cut covenant EBITDA by 10.6 x 1.15 = 12.2 (see FIN-18).
- **Source:** `revenue_by_customer.csv`, Pinecrest row (rank 4) and Total row; litigation records (supplied).
- **Severity:** Medium
- **Confidence:** High for the math; Medium for the relationship risk.
- **Deal impact:** Post-closing customer retention; a small valuation effect; adds to covenant risk.
- **Cross-check:** The contract's liability cap clause; Pinecrest's 2026 orders (my folder has no 2026 customer data).

#### FIN-23: At the deal model's own 11.46x, value is $12.60 to $14.50 per share before Vantor
- **Finding:** Applying 11.46x to revised guidance gives $12.60 to $14.50 per share. Applying it to LTM diligence-adjusted EBITDA gives $14.19. That is 39.6% to 47.5% below the $24.00 offer. Treating Vantor as debt-like takes off another $2.00 (at 96.4) or $2.90 (at 140.0), pre-tax.
- **Evidence:**
  - **Multiple:** equity at the offer = 24.00 x 48.3 = 1,159.2. Net debt = 227.5 - 33.9 = 193.6. EV = 1,352.8, and 1,352.8 / 118.0 = 11.46x.
  - Value per share = (11.46 x EBITDA - 193.6) / 48.3.

| EBITDA basis | EBITDA | EV at 11.46x | Equity | Per share | Less Vantor 96.4 | Less Vantor 140.0 | Offer EV / EBITDA |
|---|---|---|---|---|---|---|---|
| Deal model FY2026E (check) | 118.0 | 1,352.3 | 1,158.7 | $23.99 | $21.99 | $21.09 | 11.5x |
| Guidance high | 78.0 | 893.9 | 700.3 | $14.50 | $12.50 | $11.60 | 17.3x |
| Guidance mid | 74.0 | 848.0 | 654.4 | $13.55 | $11.55 | $10.65 | 18.3x |
| Guidance low | 70.0 | 802.2 | 608.6 | $12.60 | $10.60 | $9.70 | 19.3x |
| LTM company-defined (reference) | 89.7 | 1,028.0 | 834.4 | $17.27 | $15.28 | $14.38 | 15.1x |
| LTM diligence-adjusted (recomputed; check against FIN-05) | 76.7 | 879.0 | 685.4 | $14.19 | $12.19 | $11.29 | 17.6x |

  - **LTM diligence-adjusted EBITDA:** 89.7 less 9.7 of restructuring (charged every year from FY2022 to LTM, so recurring) less 3.3 of customer implementation delays (an operating cost) = 76.7. If FIN-05 also removed the 4.1 of Vantor defense costs, the figure is 72.6, or $13.22 per share.
  - **Vantor per share:** 96.4 / 48.3 = $2.00; 140.0 / 48.3 = $2.90. After tax at the FY2025 effective rate (5.6 / 24.2 = 23.1%), these become 74.1 and 107.6, or $1.53 and $2.23 per share.
  - **LTM bill-and-hold:** if the net 22.4 of bill-and-hold revenue in the LTM had not shipped by Jun 30, 2026, removing its gross profit at 41.1% (9.2) gives 67.5 of EBITDA and $12.01 per share.
  - Revised guidance is 33.9% to 40.7% below the model's 118.0.
  - The undisturbed price of $17.85 implies EV of 862.2 + 193.6 = 1,055.8, or 14.3x mid guidance. The market already pays more than 11.46x for current earnings.
- **Source:** `data/deal-brief.md` (price, shares, 118.0, about 11.5x); `balance_sheet.csv` Q2_2026 (debt, cash); `adjusted_ebitda_reconciliation.csv` LTM column; `income_statement.csv` FY2025 (tax and pre-tax income); 10-Q outlook and litigation figures (supplied).
- **Severity:** Critical
- **Confidence:** High for the arithmetic. Medium for the EBITDA bases: the guidance is management's, FIN-05 was recomputed, and the Vantor figures are the plaintiff's positions, not findings of liability.
- **Deal impact:** Price. At $24.00 the offer pays 17.3x to 19.3x revised guidance. Either the price comes down, or the IC has to accept a much higher multiple than the model uses.
- **Cross-check:** Q3 2026 results against guidance; trading comparables; whether the product accused in the Vantor case is Talon Gen-3. Gen-3 is about 70% of FY2025 hardware revenue per 10-K Item 1 as supplied, which is about 211.0, or 42.0% of total revenue.

### Positive or mitigating points
- Talonfield passes the Jun 30, 2026 test on the definition: 2.65x vs a 3.50x maximum.
- Norvale's normalized share is flat at 28.0%, so concentration did not actually rise.
- Underlying Q2 2026 revenue grew 4.0% before the reversal. FieldOS software grew 14.6% in H1 2026 (67.5 vs 58.9), or 18.5% before the 2.3 of credits.
- Change of control is a default anyway, so for Arbelion the covenant problem is mainly about the period before closing and about reporting quality.

### Gaps and questions for management
1. **Credit agreement:** the agreement, its amendments, and the Jun 30 and Sep 30, 2026 compliance certificates. Specifically:
   - how the 15% cap is applied, and whether SBC sits inside it;
   - whether Total Debt includes finance leases. H1 2026 cash flow shows 0.7 of "finance lease payments and other". If all 6.5 of other liabilities counted as debt, the Jun 30 ratio would be 209.0 / 76.36 = 2.74x;
   - equity cure rights;
   - revolver size and availability.
2. **H2 2026:** Q3 2026 results, and H2 plans for restructuring, non-recurring and deal costs, and revolver use.
3. **Bill-and-hold:**
   - whether the 22.4 that was not returned has been delivered and paid for, and when;
   - which customer's products made up the 9.4 return;
   - whether there was any bill-and-hold in Q4 2024;
   - the gross margin on the 31.8, and hardware gross margin generally.
4. **KPIs:** do FY2025 robots shipped (4,300) and the installed base (17,400) include bill-and-hold units? The Jun 30, 2026 installed base (19,040 = 17,400 + 1,640) shows no reduction for the returned products.
5. **Bonus plan:** the payout at threshold, any compensation committee discussion of bill-and-hold, and the clawback policy.
6. **Pinecrest:** revenue so far in 2026, and the liability cap clause.
7. **For the lead:** check the FIN-05 figure in the register against the 76.7 used here, and adjust FIN-23 at $0.24 per share per $1.0M if they differ.
