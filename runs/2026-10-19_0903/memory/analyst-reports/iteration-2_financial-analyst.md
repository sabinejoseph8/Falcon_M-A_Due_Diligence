## Financial analyst: findings (iteration 2)

I picked the task up where it stopped and finished all five parts. Main results:

- **Covenant, June 30, 2026:** the company reported a leverage ratio of 2.26x. That figure only works if the 15% cap on Permitted Add-backs is ignored. With the cap applied, I get **2.65x**. That is still within the 3.50x maximum.
- **Covenant, December 31, 2026 (projection):** on the guidance in Fact B, the ratio is **3.06x to 3.56x against a 3.00x maximum**, so a breach before closing is likely. The result depends on one unknown: how much more restructuring and one-off cost the company adds back in H2 2026.
- **Bill-and-hold:** without the Q4 2025 bill-and-hold revenue, Q4 2025 growth falls from 32.4% to **5.1%** and FY2025 growth from 19.1% to **11.6%**.

### Files reviewed
- `data/financials/adjusted_ebitda_reconciliation.csv`, `income_statement.csv`, `balance_sheet.csv`, `cash_flow.csv`, `revenue_quarterly.csv`, `revenue_by_customer.csv`, `kpis.csv`, `README.md`
- `data/deal-brief.md` (context)
- Facts A, B and C from the lead agent. They come from `data/sec-filings/TLFS_10-K_FY2025_excerpts.md` (Notes 2, 9, 13, Item 1) and `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`. I used them as given and did not read those files.
- None of the financial files contain text that tries to instruct the agents.

**How I built the LTM figures:** LTM to June 30, 2026 = FY2025 − H1 2025 + H1 2026. My recomputed figures match iteration 1:
- Net income 18.6 − 5.3 + (−8.9) = 4.4
- Interest 13.6 − 6.6 + 7.9 = 14.9
- Tax 5.6 − 1.6 + (−2.6) = 1.4
- D&A 26.8 − 13.0 + 14.1 = 27.9
- SBC 17.2 − 8.3 + 8.9 = 17.8
- Restructuring 7.9 − 2.6 + 4.4 = 9.7
- Other non-recurring 9.6 − 1.8 + 6.2 = 14.0

**One definitional note:** the covenant EBITDA in Fact A is net income + interest + taxes + D&A. It does not deduct other income, so it gives 48.6 for LTM against 48.2 in the company reconciliation. The 0.4 difference does not change any conclusion.

### Key metrics table
US$ millions. **Reported** means the figure as the company presents it. **Adjusted** means my recalculation under the covenant definition in Fact A. Total debt does not include letters of credit (FIN-14 gives the sensitivity).

| Metric | FY2023 | FY2024 | FY2025 | LTM Jun 30, 2026 |
|---|---|---|---|---|
| Total revenue (reported) | 368.9 | 421.7 | 502.3 | 498.4 (502.3 − 226.5 + 222.6) |
| Revenue without bill-and-hold, net of the Q2 2026 return (adjusted) | 368.9 | 421.7 | 470.5 | 476.0 (498.4 − 31.8 + 9.4) |
| Covenant EBITDA (NI + interest + tax + D&A) | 43.1 | 53.0 | 64.6 | 48.6 |
| SBC (not capped) | 11.6 | 13.9 | 17.2 | 17.8 |
| Base before Permitted Add-backs | 54.7 | 66.9 | 81.8 | 66.4 |
| Permitted Add-backs (restructuring + other non-recurring) | 6.6 | 8.6 | 17.5 | 23.7 |
| Permitted Add-backs as % of base | 12.1% | 12.9% | 21.4% | 35.7% |
| 15% cap | 8.2 | 10.0 | 12.3 | 10.0 |
| Consolidated EBITDA with cap (adjusted) | 61.3 | 75.5 | 94.1 | 76.4 |
| Adjusted EBITDA, company definition (reported) | 60.4 | 74.8 | 98.8 | 89.7 |
| Total debt (term loan + revolver) | 120.0 | 200.0 | 220.0 | 227.5 |
| Cash | 54.8 | 48.3 | 41.6 | 33.9 |
| Covenant net debt (cash netting capped at 25.0) | 95.0 | 175.0 | 195.0 | 202.5 |
| Net leverage, cap applied (adjusted) | 1.55x | 2.32x | 2.07x | 2.65x |
| Net leverage, no cap (company method) | 1.57x | 2.34x | 1.97x | 2.26x (company reported 2.26x) |
| Covenant maximum | 3.50x | 3.50x | 3.50x | 3.50x (3.00x from Sep 30, 2026) |
| Liquidity (cash + revolver availability) | n/a | n/a | n/a | 59.7 |

### Findings

#### FIN-14: The company's reported 2.26x appears to ignore the 15% add-back cap. With the cap, leverage is 2.65x
- **Finding:** The reported 2.26x matches the uncapped company Adjusted EBITDA of 89.7. With the 15% cap in Fact A applied, Consolidated EBITDA is 76.4 and the ratio is 2.65x. The company is still within the 3.50x maximum at June 30, 2026. Its stated ratio understates leverage by about 0.39x, and Permitted Add-backs exceed the cap by 13.7.
- **Evidence, June 30, 2026 (LTM):**
  - Which add-backs are which:
    - SBC 17.8 is separate and not capped.
    - Permitted Add-backs = restructuring 9.7 + other non-recurring 14.0 = 23.7. That 14.0 is litigation (Vantor) 4.1, customer implementation delays 3.3, auditor transition 2.3, CFO transition 2.5 and cyber response 1.8.
  - Base before Permitted Add-backs = 48.6 + 17.8 = 66.4.
  - Cap = 15% x 66.4 = 9.96. Allowed add-backs = min(23.7, 9.96) = 9.96. Disallowed = 23.7 − 9.96 = 13.74.
  - Consolidated EBITDA = 66.4 + 9.96 = 76.36.
  - Net debt = (182.5 + 45.0) − min(33.9, 25.0) = 227.5 − 25.0 = 202.5.
  - Ratio = 202.5 / 76.36 = **2.65x**. Using the reconciliation EBITDA of 48.2 instead: (48.2 + 17.8) x 1.15 = 75.9, and 202.5 / 75.9 = 2.67x.
  - Uncapped: 202.5 / 89.7 = 2.26x, which equals the reported figure.
  - EBITDA implied by 2.26x = 202.5 / 2.26 = 89.6. A ratio that rounds to 2.26x means EBITDA between 202.5 / 2.265 = 89.4 and 202.5 / 2.255 = 89.8. That brackets 89.7.
  - If the company had netted all of its cash instead: (227.5 − 33.9) / 2.26 = 85.7. That matches no figure in the data.
  - Conclusion: the 2.26x appears to use uncapped Adjusted EBITDA with the cash netting cap applied.
- **Evidence, December 31, 2025 (FY2025):**
  - Covenant EBITDA = 18.6 + 13.6 + 5.6 + 26.8 = 64.6. Base = 64.6 + 17.2 = 81.8.
  - Permitted Add-backs = 7.9 + 9.6 = 17.5. Cap = 15% x 81.8 = 12.27, so 5.23 is disallowed.
  - Consolidated EBITDA = 81.8 + 12.27 = 94.07.
  - Net debt = (185.0 + 35.0) − 25.0 = 195.0.
  - Ratio = 195.0 / 94.07 = **2.07x**, against 195.0 / 98.8 = 1.97x uncapped.
  - The cap did not bind in FY2023 (6.6 against a cap of 8.2) or FY2024 (8.6 against 10.0). **FY2025 is the first year it binds.**
- **Sensitivities:**
  - **(a) Letters of credit.** If Total Debt includes the 4.2 of letters of credit, June 30 net debt is 206.7 and the ratio is 206.7 / 76.36 = 2.71x.
  - **(b) Narrower reading of the cap.** If the base excludes SBC (SBC still not capped), the cap is 15% x 48.6 = 7.29. Consolidated EBITDA = 48.6 + 17.8 + 7.29 = 73.7, and the ratio is 202.5 / 73.7 = 2.75x.
  - Under every reading, the ratio stays within 3.50x at June 30, 2026.
- **Source:** `adjusted_ebitda_reconciliation.csv` rows 2 to 11 and 16 to 20 (FY2025, H1_2025, H1_2026, LTM_Q2_2026), and FY2023/FY2024 rows 2 to 5 and 8 to 10. `balance_sheet.csv` rows 2, 16 and 17. Facts A and B.
- **Severity:** High. There is no breach at June 30. However, the company's public compliance figure appears to misapply the credit agreement, and this sets up FIN-15. A price or terms protection is needed: a representation on covenant calculations, and lender compliance certificates as a diligence deliverable.
- **Confidence:** Medium. The arithmetic is High confidence. Two things are unconfirmed: the exact legal definition (Fact A is a summary) and what the lenders actually received.
- **Deal impact:** Financing and closing risk. It also raises a question about disclosure controls.
- **Cross-check:**
  - Get the compliance certificates for Q4 2025, Q1 2026 and Q2 2026, and any amendments or waivers.
  - Read the full credit agreement definition, including whether letters of credit count as debt.
  - Check whether the 10-Q describes its ratio as calculated "per the credit agreement".
  - Look in the news for lender or rating agency commentary.

#### FIN-15: Projected breach of the 3.00x step-down at December 31, 2026 under most assumptions (projection)
- **Finding (projection):** Using FY2026 Adjusted EBITDA guidance of 70 to 78 and H1 2026 add-back levels, capped Consolidated EBITDA for FY2026 is 56.1 to 65.3. Against net debt of 200.0, the ratio is 3.06x to 3.56x, above the 3.00x maximum across the whole guidance range. The September 30, 2026 test has already passed and is borderline at 2.84x to 3.04x. Under the company's apparent uncapped method, the same inputs give 2.56x to 2.86x, which would look compliant.
- **Assumptions (projection):**
  1. FY2026 Adjusted EBITDA (company definition) equals guidance of 70 to 78 (Fact B).
  2. H2 2026 SBC and Permitted Add-backs equal H1 2026 (SBC 8.9; restructuring 4.4 + other 6.2 = 10.6). That makes FY2026 SBC 17.8 and Permitted Add-backs 21.2.
  3. The term loan amortizes 1.25 per quarter (2.5 repaid in H1 2026, `cash_flow.csv` row 15). The revolver stays at 45.0. Cash stays at or above 25.0, so netting stays at the cap.
- **Evidence, December 31, 2026:**
  - Net debt = (182.5 − 2.5) + 45.0 − 25.0 = 200.0.
  - EBITDA = Adjusted EBITDA − 17.8 − 21.2, giving 31.0 (low end) to 39.0 (high end).
  - Base = EBITDA + 17.8, giving 48.8 to 56.8.
  - The cap binds (21.2 is more than 15% of the base), so Consolidated EBITDA = 1.15 x base:
    - Low end: 1.15 x 48.8 = 56.12. Ratio 200.0 / 56.12 = **3.56x**.
    - Midpoint: base 52.8, Consolidated EBITDA 60.72, ratio **3.29x**.
    - High end: 1.15 x 56.8 = 65.32. Ratio 200.0 / 65.32 = **3.06x**.
  - Break-even Consolidated EBITDA = 200.0 / 3.00 = **66.7**.
  - Headroom (negative means a breach):
    - High end: 65.32 − 66.67 = **−1.4 (−2.0%)**.
    - Low end: 56.12 − 66.67 = **−10.5 (−15.8%)**.
  - Maximum net debt allowed at 3.00x = 3 x 65.32 = 196.0 (high end) or 3 x 56.12 = 168.4 (low end). Net debt would need to fall by 4.0 to 31.6.
  - In guidance terms: Consolidated EBITDA = 1.15 x (Adjusted EBITDA − Permitted Add-backs), so compliance needs Adjusted EBITDA − Permitted Add-backs ≥ 66.67 / 1.15 = 57.97.
    - At 70 of Adjusted EBITDA, FY2026 Permitted Add-backs must stay at or below 12.0. That leaves only **1.4 for H2** (12.0 − 10.6 already used in H1).
    - At 78, they must stay at or below 20.0, which leaves **9.4 for H2**.
    - For comparison, H2 2025 Permitted Add-backs were (7.9 − 2.6) + (9.6 − 1.8) = **13.1**.
- **Downside case:** H2 2026 cash flow repeats H1 2026. Before the revolver draw, H1 cash fell by 17.7. Cash would end at 33.9 − 17.7 = 16.2 against debt of 225.0, so net debt = 208.8. The ratio would be 3.20x to 3.72x.
- **Upside case:** no further Permitted Add-backs in H2. FY2026 Permitted Add-backs = 10.6, so the base is 59.4 to 67.4 and Consolidated EBITDA is 68.3 to 77.5. The ratio is 2.93x to 2.58x, which is compliant but tight at the low end.
- **September 30, 2026 (rough projection):** I interpolated LTM Consolidated EBITDA in a straight line between June 30 (76.36) and December 31 (56.12 to 65.32), which gives 66.2 to 70.8.
  - Net debt = 181.25 + 45.0 − 25.0 = 201.25.
  - Ratio = 201.25 / 70.84 = 2.84x to 201.25 / 66.24 = 3.04x.
  - Break-even = 201.25 / 3.00 = 67.1. Headroom is +3.8 (+5.6%) to −0.8 (−1.3%).
  - I have no quarterly EBITDA, so this is directional only.
- **Source:** `adjusted_ebitda_reconciliation.csv` rows 8 to 10 (H1_2026), `balance_sheet.csv` rows 2, 16 and 17, `cash_flow.csv` rows 15, 16 and 22. Facts A and B.
- **Severity:** Critical. Test met: **a default before signing or closing**. The September 30, 2026 test date has passed. The December 31, 2026 test falls before any realistic closing (inference: the IC meets November 6 and exclusivity runs to November 20, 2026). The base case breaches across the whole guidance range (3.06x to 3.56x against 3.00x). A default would expose 227.5 of debt against 59.7 of liquidity (FIN-19). If management can show that H2 2026 Permitted Add-backs will be small, as in the upside case, this falls to High.
- **Confidence:** Medium. It is a projection that depends on the add-back mix, quarterly phasing and the legal definition.
- **Deal impact:** Closing risk, financing, and valuation (a cost to amend or waive the covenant, possibly a cure or equity injection).
- **Cross-check:**
  - Q3 2026 10-Q or 8-K and the Q3 compliance certificate, if filed.
  - Any amendment or waiver 8-K.
  - News on lender talks or a ratings action.
  - Ask management for Q3 2026 actuals and the H2 add-back forecast.

#### FIN-16: Bill-and-hold drove most of the reported FY2025 growth, and underlying Q4 2025 growth was 5.1% (revises iteration 1's $21.0m trend excess)
- **Finding:** Without the 31.8 of Q4 2025 bill-and-hold revenue:
  - Q4 2025 growth falls from 32.4% to 5.1%.
  - FY2025 growth falls from 19.1% to 11.6%.
  - Hardware growth falls from 15.1% to 2.9%.
  - Norvale growth falls from 32.3% to 11.4%.

  The disclosed bill-and-hold (31.8) is 10.8 larger than my trend-based excess of 21.0. **The slowdown therefore started in Q4 2025, not in 2026.**
- **Evidence:**
  - **Q4 2025:**
    - Reported growth: 154.4 / 116.6 − 1 = 32.4%.
    - Without bill-and-hold: 154.4 − 31.8 = 122.6, and 122.6 / 116.6 − 1 = **5.1%**.
    - Q3 2025 growth was 121.4 / 106.1 − 1 = 14.4%.
  - **Iteration 1 trend excess, reproduced:** trend Q4 2025 = 116.6 x 1.144 = 133.4, so the excess was 154.4 − 133.4 = 21.0.
    - The disclosed 31.8 exceeds this by 10.8. Revenue without bill-and-hold (122.6) is 10.8 below that trend.
    - **Revision:** the iteration 1 figure of 21.0 understated the pull-forward. Use 31.8.
  - **FY2025:**
    - Reported growth: 502.3 / 421.7 − 1 = 19.1%.
    - Without bill-and-hold: 470.5 / 421.7 − 1 = **11.6%**.
  - **Hardware:**
    - Reported growth: 301.4 / 261.9 − 1 = 15.1%.
    - Without bill-and-hold: 269.6 / 261.9 − 1 = **2.9%**.
  - **Norvale:**
    - FY2025 revenue without bill-and-hold: 156.2 − 24.6 = 131.6.
    - Growth falls from 156.2 / 118.1 − 1 = 32.3% to 131.6 / 118.1 − 1 = **11.4%**.
    - Share of revenue falls from 31.1% to 131.6 / 470.5 = 28.0%.
    - Norvale accounts for 24.6 / 31.8 = 77.4% of the bill-and-hold revenue.
    - Norvale's increase of 38.1 was 47.3% of the company's total increase of 80.6.
- **Source:** `revenue_quarterly.csv` rows 4, 5, 8 and 9. `income_statement.csv` rows 2 and 5. `revenue_by_customer.csv` row 2. Fact C (10-K Note 2).
- **Severity:** High. It undermines the growth premise behind the management case (FY2026E revenue of 560, per `deal-brief.md`). Price and terms are affected. I rated it High rather than Critical because the valuation gap is covered under the guidance and valuation findings.
- **Confidence:** High. Calculated directly, using amounts disclosed in the 10-K.
- **Deal impact:** Valuation. It also needs a revenue recognition representation and possibly an indemnity.
- **Cross-check:**
  - 10-K Note 2 for the bill-and-hold criteria (customer request, title transfer, separately identified goods).
  - Whether the auditor flagged revenue recognition as a critical audit matter.
  - Whether the auditor transition (2.3 add-back) is connected.
  - News on Norvale's capacity plans.

#### FIN-17: 29.6% of the Q4 2025 bill-and-hold revenue was returned within six months. Without the credits, Q2 2026 growth is +6.0% against −4.0% reported
- **Finding:** The 9.4 return in Q2 2026 reversed 29.6% of the Q4 2025 bill-and-hold revenue. That raises doubt about whether the remaining 22.4 will hold. Adding back the 9.4 return and the 2.3 of SLA credits gives Q2 2026 growth of +6.0%, against −4.0% reported. Underlying growth is low single digits, not negative.
- **Evidence:**
  - Share returned: 9.4 / 31.8 = 29.6%. Remaining bill-and-hold: 31.8 − 9.4 = 22.4.
  - **Q2 2026:**
    - Reported growth: 112.9 / 117.6 − 1 = −4.0%.
    - Adding back 9.4: 122.3 / 117.6 − 1 = +4.0%.
    - Adding back 9.4 + 2.3 = 11.7: 124.6 / 117.6 − 1 = **+6.0%**.
  - **Q1 2026:** 109.7 / 108.9 − 1 = +0.7%.
  - **H1 2026:**
    - Reported growth: 222.6 / 226.5 − 1 = −1.7%.
    - Adding back the credits: 234.3 / 226.5 − 1 = +3.4%.
  - **The two views meet:**
    - Q4 2025 without bill-and-hold grew 5.1% and Q2 2026 normalized grew 6.0%. Both point to growth of about 5% to 6%, against the 15.6% implied by the management case (560 / 484.6 − 1 is not right, since FY2025 revenue is 502.3).
    - Correct calculation: 560 / 502.3 − 1 = 11.5% on the reported base, and 560 / 470.5 − 1 = 19.0% on the base without bill-and-hold.
  - The 10-Q does not name the customer that returned the products. I have not assumed it was Norvale.
- **Source:** `revenue_quarterly.csv` rows 6, 7, 10 and 11. `income_statement.csv` row 5. `deal-brief.md` "Valuation basis". Fact C (10-Q).
- **Severity:** High. A bill-and-hold reversal suggests the revenue was recognized before it was earned, and further returns could follow. An indemnity or escrow for revenue recognition is warranted.
- **Confidence:** High for the arithmetic. Medium for the conclusion about the remaining 22.4, which is an inference.
- **Deal impact:** Valuation, and an indemnity for further returns after closing.
- **Cross-check:**
  - The 10-Q for which customer returned the products and why (the product quality news on Gen-3).
  - Whether any of the remaining 22.4 has been delivered, paid or disputed.
  - Any SEC comment letters on revenue recognition.

#### FIN-18: Norvale makes up 38% of gross receivables, with an implied DSO of about 108 days against about 79 for all other customers
- **Finding:** Norvale's receivable at December 31, 2025 was about 46.2, which is 1.4x the June 30, 2026 cash balance. Norvale's implied DSO is 28.5 days longer than for the rest of the customer base. The allowance (2.6, or 2.1% of gross receivables) looks thin for that concentration.
- **Evidence:**
  - Norvale receivable = 38% x 121.5 = 46.2.
  - Norvale DSO = 46.2 / 156.2 x 365 = **107.9 days**. Using revenue without bill-and-hold: 46.2 / 131.6 x 365 = 128.1 days.
  - Everyone else: receivables 121.5 − 46.2 = 75.3; revenue 502.3 − 156.2 = 346.1; DSO = 75.3 / 346.1 x 365 = **79.4 days**.
  - Allowance = 2.6 / 121.5 = 2.1%.
  - Comparison with cash: 46.2 / 33.9 = 1.4x.
  - If the 24.6 of Norvale bill-and-hold were still unpaid at year end, it would be 24.6 / 46.2 = 53% of the Norvale receivable. This is unverified.
- **Source:** `balance_sheet.csv` rows 2, 22 and 23. `revenue_by_customer.csv` row 2. Fact C (10-K Note 13).
- **Severity:** Medium. Collection timing needs follow-up. There is no evidence of a loss.
- **Confidence:** Medium. Norvale's receivable is derived from a rounded percentage, and I do not know how much of the bill-and-hold amount is unpaid.
- **Deal impact:** Valuation (working capital peg) and post-closing credit risk.
- **Cross-check:**
  - Norvale aging schedule at June 30, 2026.
  - Norvale's payment terms on bill-and-hold contracts.
  - News on Norvale's financial health or vendor disputes.

#### FIN-19: Liquidity is 59.7 with about 20 months of runway, but covenant headroom effectively limits it
- **Finding:** Total liquidity at June 30, 2026 was 59.7. At the H1 2026 burn rate, that is about 20 months of runway. Only 8.9 of cash sits above the 25.0 netting cap. Once that is gone, each dollar of burn adds a dollar to covenant net debt, and FIN-15 already projects no headroom at December 31, 2026.
- **Evidence:**
  - Revolver availability = 75.0 − 45.0 − 4.2 = 25.8, which matches Fact B.
  - Liquidity = 33.9 + 25.8 = **59.7**.
  - **Burn rate:** H1 2026 cash fell by 7.7, which includes a 10.0 revolver draw. Before the draw, cash fell by 17.7. That equals free cash flow (−13.0) − term loan repayment (2.5) − taxes paid on net share settlement (1.5) − finance lease payments (0.7) = −17.7. Monthly burn = 17.7 / 6 = 2.95.
  - **Runway:**
    - Total liquidity: 59.7 / 2.95 = **20.2 months**.
    - Cash only: 33.9 / 2.95 = 11.5 months.
    - Free cash flow basis: 59.7 / (13.0 / 6) = 27.6 months.
  - **Cash above the netting cap:** 33.9 − 25.0 = 8.9, which is about 3.0 months of burn.
  - **Room under 3.00x at June 30 levels:** 3.00 x 76.36 − 202.5 = 26.6. At the December 2026 high case: 196.0 − 200.0 = −4.0.
  - H2 2025 had a similar burn: free cash flow was −10.1 − 3.3 = −13.4.
- **Source:** `balance_sheet.csv` rows 2 and 16. `cash_flow.csv` rows 11, 12, 15 to 18, 20, 22 and 24. Facts A and B.
- **Severity:** High. On its own, the liquidity is adequate. Combined with FIN-15, a covenant default could block revolver draws (inference: typical draw-stop) and accelerate 227.5 of debt. Because change of control is an event of default (Fact A), all debt will be refinanced at closing in any case.
- **Confidence:** High for the calculations. Medium for the inference about how the covenant constrains liquidity.
- **Deal impact:** Financing. The interim operating covenants in the merger agreement should limit revolver draws and add-backs.
- **Cross-check:**
  - The credit agreement's conditions for drawing the revolver.
  - Cash and revolver balances in the Q3 2026 10-Q.
  - The 13-week cash forecast from management.

#### FIN-20: Name-check against `revenue_by_customer.csv`
- **Finding:** Vantor Robotics, Delmarco Electrical Contractors, Kinetic Aisle and Greyfin Research are not among the top 10 customers. Vantor appears in the financial files only as a litigation add-back. The named customers rank as follows:

  | Customer | FY2025 rank | FY2024 revenue | FY2025 revenue | FY2025 share | Growth |
  |---|---|---|---|---|---|
  | Norvale Retail Group | 1 | 118.1 | 156.2 | 31.1% | 32.3% (11.4% without bill-and-hold) |
  | Pinecrest Distribution | 4 | 16.2 | 17.4 | 3.5% | 1.2 / 16.2 = 7.4% |
  | Harbor & Vine Grocers | 5 | 12.4 | 15.1 | 3.0% | 2.7 / 12.4 = 21.8% |

- **Evidence:**
  - Searching all of `data/financials/` for the four names finds only "Litigation costs (Vantor patent case)". That line was 0.8 in FY2024, 2.1 in FY2025, 3.0 in H1 2026 and 4.1 for LTM.
  - The file lists only the top 10. "All other customers" (193.5) is not broken down. Any of the four names that is a customer earned less than 7.9 (rank 10, Tidewell Foods). Whether they are customers at all cannot be confirmed from this data.
- **Source:** `revenue_by_customer.csv` rows 2, 5, 6, 11 and 12. `adjusted_ebitda_reconciliation.csv` row 16.
- **Severity:** Low. Reference information.
- **Confidence:** High for the top 10 status. Low for whether the four names are customers outside the top 10.
- **Deal impact:** Feeds the litigation and customer cross-source work.
- **Cross-check:** The full customer list from management. Litigation records for the Vantor case's exposure beyond legal costs.

#### FIN-21: Gen-3 robots made up about 42% of FY2025 total revenue
- **Finding:** Gen-3 hardware revenue was about 211.0 in FY2025, which is 42.0% of total revenue. Any product issue with Gen-3 (returns, SLA credits, warranty) affects a large part of the revenue base.
- **Evidence:** 70% x 301.4 = 211.0. Share of total revenue = 211.0 / 502.3 = 42.0%.
- **Source:** `income_statement.csv` rows 2 and 5. Fact C (10-K Item 1).
- **Severity:** Medium.
- **Confidence:** Medium. The 70% is approximate ("about").
- **Deal impact:** Post-closing (warranty reserves, product risk).
- **Cross-check:**
  - News or litigation about Gen-3 defects.
  - Warranty reserve movements in the 10-Q.
  - Whether the 9.4 return involved Gen-3 units.

**Revisions to iteration 1 cards:**
1. The trend-based Q4 2025 excess of 21.0 is replaced by the disclosed bill-and-hold amount of 31.8 (FIN-16).
2. Any iteration 1 leverage figure based on uncapped Adjusted EBITDA should be read together with FIN-14, which gives 2.65x on the covenant basis.

**Valuation context:**
- Implied enterprise value = 24.00 x 48.3 + (227.5 − 33.9) = 1,159.2 + 193.6 = 1,352.8.
- Multiples:
  - Deal model basis: 1,352.8 / 118 = 11.5x, which matches the brief.
  - LTM company Adjusted EBITDA: 1,352.8 / 89.7 = 15.1x.
  - Guidance midpoint: 1,352.8 / 74 = 18.3x.
  - LTM covenant EBITDA: 1,352.8 / 76.4 = 17.7x.

### Positive or mitigating points
- No covenant breach at June 30, 2026 under any reading: 2.65x to 2.75x against 3.50x (FIN-14).
- If H2 2026 adds back no further restructuring or one-off costs, the December 2026 ratio is 2.58x to 2.93x, which is compliant (FIN-15 upside case).
- Underlying growth is still positive: +6.0% in Q2 2026 after the credits (FIN-17).
- Under the deal structure, all debt will be refinanced at closing because change of control is an event of default. That makes the covenant mostly a risk between signing and closing.
- Pinecrest grew 7.4% and Harbor & Vine 21.8% in FY2025.

### Gaps and questions for management
1. Compliance certificates for Q4 2025 to Q2 2026, plus the Q3 2026 certificate or a draft. Ask for a reconciliation to the 2.26x and an explanation of how the 15% cap was applied.
2. The full credit agreement definitions: whether letters of credit count as Total Debt, the base for the add-back cap, the equity cure rights, and the revolver draw conditions.
3. Q3 2026 actuals: revenue, EBITDA, add-backs, cash and revolver. Also quarterly EBITDA for Q3 2025 to Q2 2026 so the LTM can be projected properly.
4. The H2 2026 forecast of restructuring and one-off costs that make up the bill between guidance and covenant EBITDA.
5. Bill-and-hold detail: contracts, delivery and payment status of the remaining 22.4, the identity of the customer behind the 9.4 return, and the risk of further returns.
6. The Norvale receivables aging and payment terms at June 30, 2026.
7. The full customer list, to confirm whether Vantor, Delmarco, Kinetic Aisle or Greyfin are customers below the top 10.
8. The Gen-3 share of H1 2026 hardware revenue, and warranty claims.
