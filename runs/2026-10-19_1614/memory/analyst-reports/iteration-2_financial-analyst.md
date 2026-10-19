## Financial analyst: findings

**Target:** Corvane Diagnostics, Inc. (Project Kestrel, fictional). Iteration 2 follow-up. All figures are US$ millions unless stated. New IDs run from FIN-049 to FIN-073. Projections and inferences are labeled.

### Files reviewed

Financials (all re-read):
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/financials/income_statement.csv`
- `.../financials/adjusted_ebitda_reconciliation.csv`
- `.../financials/balance_sheet.csv`
- `.../financials/revenue_quarterly.csv`
- `.../financials/revenue_by_customer.csv`
- `.../financials/kpis.csv`
- `.../financials/README.md`
- `.../targets/kestrel/data/deal-brief.md`

Cited files, read to confirm the lead's facts:
- `.../sec-filings/CRVD_10-K_FY2025_excerpts.md`
- `.../sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`
- `.../sec-filings/CRVD_8-K_2026-08-05_q2-results-guidance.md`
- `.../sec-filings/CRVD_DEF14A_2026_excerpts.md`
- `.../news/2026-07-30_healthcare-policy-daily_cms-lab-fee-schedule.md`
- `.../news/2026-08-27_pharma-pipeline-news_veltrane-halts-atlas-3.md`
- `.../litigation/LIT-002_genaro-v-corvane.md`

**Fact check of the lead's inputs.** All amounts match the sources, with three points to note:
1. The "about 40% of non-Medicare OncoTrace revenue priced off the Medicare rate" figure comes from the **10-K, Item 1, "Payer contracts"**, not the 10-Q "Reimbursement" section. The 10-Q section only says the rate takes effect Jan 1, 2027 and that Corvane "may seek reconsideration".
2. The covenant definition adds back "other non-recurring or unusual **cash** costs". "Cash" matters because some add-backs, such as denial write-offs, may not be cash costs. The 15% cap binds in every period I tested, so this does not change my numbers.
3. The 8-K adds one data point: Q2 2026 Adjusted EBITDA was 26.0, so Q1 2026 was 54.1 - 26.0 = 28.1.

The 10-K also confirms that OncoTrace is the "hereditary cancer panel" in `kpis.csv` rows 4 and 5. None of the files I read contains embedded instructions.

### Key metrics table

| Metric ("FA" = my adjusted figure) | FY2023 | FY2024 | FY2025 | H1 2026 / LTM Q2 2026 |
|---|---|---|---|---|
| Revenue, reported | 348.0 | 386.0 | 431.0 | LTM 429.2 |
| Revenue, FA normalized (less 14.2) | 348.0 | 386.0 | 416.8 | LTM 415.0 |
| Revenue growth, reported | 11.4% | 10.9% | 11.7% | H1 -0.9% |
| Revenue growth, FA normalized | n/a | 10.9% | 8.0% | LTM +2.8% (415.0/403.7) |
| Gross margin, reported / FA normalized | 42.0% | 42.5% | 43.9% / 42.0% | H1 38.0% |
| Adjusted EBITDA, company | 82.4 | 99.9 | 125.3 | LTM 123.4 |
| Adjusted EBITDA, FA normalized (less 14.2) | 82.4 | 99.9 | 111.1 | LTM 109.2 |
| Adj. EBITDA margin, FA normalized | 23.7% | 25.9% | 26.7% | LTM 26.3% |
| Consolidated EBITDA, FA est. (15% cap) | 76.7 | 92.1 | 111.9 | LTM 90.2 |
| Net debt | 375.0 | 371.4 | 391.0 | 395.9 |
| Net leverage, FA est. (covenant max 4.50x; 4.00x from Sep 30, 2026) | 4.89x | 4.03x | 3.49x | 4.39x |
| OncoTrace revenue (clinical x panel share) | 103.6 | 120.1 | 138.5 (FA 124.3) | H1 65.7 |
| Medicare OncoTrace revenue | 53.9 | 63.7 | 76.2 | H1 36.8 |
| Veltrane revenue / backlog | n/a | 38.0 / n/a | 50.5 / n/a | backlog 61.0 of 231.4 |
| FY2026 Adj. EBITDA guidance | | | | 100 to 106 (was 134 to 140) |
| LTM Adj. EBITDA at Q2 2027 closing, FA projection | | | | (a) 100.0 to 106.0; (b) 85.5 to 91.5; (c) 72.9 to 84.8 |
| Pro forma run-rate EBITDA, FA central (FIN-065) | | | | 54.8 (US$6.25/share at 13.2x) |

How the table rows are built:
- OncoTrace revenue = clinical revenue x panel share. FY2023: 252.6 x 41% = 103.6. FY2024: 279.4 x 43% = 120.1. FY2025: 314.8 x 44% = 138.5. H1 2026: 146.0 x 45% = 65.7.
- Medicare OncoTrace = OncoTrace revenue x Medicare share. FY2023: x 52%. FY2024: x 53%. FY2025: x 55%. H1 2026: x 56%.
- Consolidated EBITDA is my estimate of the covenant measure. The method is in FIN-055.

---

### Findings

#### FIN-049: The disclosed Q4 2025 estimate change of 14.2 replaces my trend estimate; underlying FY2025 growth was 8.0%
- **Finding:** The 10-K discloses 14.2 of Q4 2025 revenue from a change in the implicit price concession estimate. Removing it gives FY2025 growth of 8.0%, not 11.7%. Quarterly growth then slows steadily: +10.0%, +8.9%, +7.9%, +5.4%, +1.3%, -3.0%.
- **Evidence:**
  - Normalized FY2025 revenue = 431.0 - 14.2 = 416.8. Growth = 416.8 / 386.0 - 1 = 8.0%.
  - Normalized clinical revenue = 314.8 - 14.2 = 300.6. Growth = 300.6 / 279.4 - 1 = 7.6% (reported 12.7%).
  - Q4 2025 underlying revenue = 120.5 - 14.2 = 106.3. Year over year: 106.3 / 100.9 = +5.4%. Versus Q3 2025: +1.0.
  - Reconciliation to FIN-001: my trend estimate of the Q4 excess was 10.6 to 13.0. The disclosed 14.2 is 1.2 above the top of that range. Underlying Q4 (106.3) is below all three of my trend estimates (107.5 to 109.9), so underlying growth was already slowing in Q4 2025. FIN-001 is superseded. Its clinical-segment attribution is confirmed (the 10-K says the change relates to OncoTrace).
  - Normalized revenue per accession = 300.6 / 1,705 x 1,000 = US$176.3. That is down 1.6% from FY2024 (US$179.1), not up 3.1%.
  - Growth also includes Pell Ridge (acquired May 2025 for 31.0). Its revenue is not disclosed, so organic growth was below 8.0%.
- **Source:** `income_statement.csv` rows 2 and 5; `revenue_quarterly.csv` rows 5 to 11; `kpis.csv` row 2; 10-K Item 7 "Results" and Item 1 "Overview"
- **Severity:** High
- **Confidence:** High. The amount is disclosed and the arithmetic is shown.
- **Deal impact:** Valuation. Thesis point 1 (11.7% growth) is overstated by 3.7 points.
- **Cross-check:** Pell Ridge revenue in the 10-K business combination note; the auditor's critical audit matter on implicit price concessions.

#### FIN-050: Normalized Adjusted EBITDA is 111.1 for FY2025 and 109.2 for LTM Q2 2026, below 110.0; no overlap with the denial write-off add-back
- **Finding:**
  - The 14.2 sits in revenue and operating income, and company Adjusted EBITDA keeps it. Without it, FY2025 Adjusted EBITDA is 111.1, and LTM Q2 2026 is 109.2, which is below the 110.0 financing threshold today.
  - It does not overlap with the denial write-off add-back, so the two adjustments stack.
- **Evidence:**
  - FY2025: 125.3 - 14.2 = 111.1. Growth = 111.1 / 99.9 - 1 = 11.2% (reported 25.4%).
  - LTM Q2 2026 (Q4 2025 is inside the LTM window): 123.4 - 14.2 = 109.2. That is 0.8 below 110.0.
  - Add-backs as a share of normalized FY2025 Adjusted EBITDA = 37.8 / 111.1 = 34.0%.
  - Why there is no overlap:
    - The 14.2 raised revenue, through a lower implicit price concession estimate.
    - The denial write-offs (FY2025: 10.6; LTM: 13.1) are a separate line, added back to EBITDA in `adjusted_ebitda_reconciliation.csv` row 12.
    - Removing one leaves the other untouched. Combined, they would cut FY2025 to 125.3 - 14.2 - 10.6 = 100.5, and LTM to 109.2 - 13.1 = 96.1.
    - FA Scenario B (FIN-006) less 14.2: FY2025 106.4 - 14.2 = 92.2; LTM 101.1 - 14.2 = 86.9.
  - Value at 13.2x: 14.2 x 13.2 = 187.4, which is 187.4 / 1,648.6 = 11.4% of EV.
- **Source:** `adjusted_ebitda_reconciliation.csv` rows 11 and 12 (FY2025, H1 2025, H1 2026, LTM); 10-K Item 7 "Results"
- **Severity:** Critical. Test: more than 10% of value (187.4, or 11.4% of EV).
- **Confidence:** High. The amount is disclosed.
- **Deal impact:** Valuation and financing. The condition counts "as Corvane defines it", so the 14.2 counts toward 110.0 while Q4 2025 is in the LTM window. It drops out of the Q2 2027 window (FIN-054).
- **Cross-check:** Whether the commitment letter lets lenders exclude changes in estimates; any SEC comment letter on the non-GAAP measure.

#### FIN-051: On a normalized basis, FY2025 gross margin fell and Adjusted EBITDA margin rose only 0.8 points
- **Finding:** The FY2025 "margin expansion" (thesis point 2) comes mostly from the estimate change.
- **Evidence:**
  - Normalized gross margin = (189.2 - 14.2) / 416.8 = 42.0%, versus FY2024 164.0 / 386.0 = 42.5%. That is -0.5 points (reported: +1.4 points).
  - Normalized Adjusted EBITDA margin = 111.1 / 416.8 = 26.7%, versus 25.9%, so +0.8 points (reported: 29.1%, +3.2 points).
  - H1 2026 gross margin is 38.0%.
- **Source:** `income_statement.csv` rows 5 and 7; `adjusted_ebitda_reconciliation.csv` row 11
- **Severity:** Medium (the value effect is already counted in FIN-050)
- **Confidence:** High
- **Deal impact:** Valuation (thesis)
- **Cross-check:** 10-Q cost of revenue discussion.

#### FIN-052: The favorable estimate change conflicts with the collection data and sits under an unremediated material weakness
- **Finding:** Corvane released price concession estimates in Q4 2025, citing "improved collection experience". Every collection indicator in the data worsened over the same period. The material weakness concerns this exact estimate and is not remediated. That raises the risk of a reversal or restatement (inference).
- **Evidence:**
  - Initial denial rate: 10.7% (FY2024), 13.4% (FY2025), 16.2% (H1 2026).
  - Denial write-offs: 7.8, 10.6, LTM 13.1.
  - DSO: 62.7 days in FY2024 and 79.0 in FY2025. Normalized: (93.3 - 14.2) / 416.8 x 365 = 69.3 days, still up 6.6 days (inference: assumes the 14.2 sits in year-end receivables).
  - The 10-Q says H1 2026 clinical revenue fell on "lower collections on OncoTrace claims".
  - If the 14.2 lowered the year-end reserve, the reserve without it would be 31.3 + 14.2 = 45.5, or 45.5 / 124.6 = 36.5% of gross receivables, versus the reported 25.1% (inference).
  - Each 1 point of reserve on gross receivables of 123.1 = 1.2 of revenue and EBITDA.
  - 10-K Item 9A: adverse ICFR opinion on this estimate. 10-Q Item 4: "has not yet been remediated".
- **Source:** `kpis.csv` row 6; `adjusted_ebitda_reconciliation.csv` row 12; `balance_sheet.csv` rows 3, 22 and 23; 10-K Item 7, Item 9A and Note 2; 10-Q Item 2 and Item 4
- **Severity:** High
- **Confidence:** Medium. The direction is clear, but the collection-rate model is not provided.
- **Deal impact:** Valuation, closing risk (restatement) and financing (see FIN-056)
- **Cross-check:** Auditor critical audit matter; SEC comment letters; short-seller reports in the news folder on revenue recognition.

#### FIN-053: FY2025 bonuses were paid at 150% on the unadjusted figure; normalized, the payout would have been about 57%
- **Finding:** Bonuses are 100% based on Adjusted EBITDA. The Compensation Committee chose not to remove the 14.2.
- **Evidence:**
  - Bonus grid: threshold 110.0 pays 50%, target 118.0 pays 100%, maximum 129.0 pays 175%.
  - Linear interpolation reproduces the reported payout: 100% + (125.3 - 118.0) / 11.0 x 75% = 149.8%, rounded to 150%.
  - On normalized 111.1: 50% + (111.1 - 110.0) / 8.0 x 50% = 56.9% (assumes linear interpolation).
  - Mr. Ellery: 1.14 x 56.9% = 0.65, versus 1.71 paid. Excess = 1.06.
- **Source:** DEF 14A "FY2025 annual bonus"; `adjusted_ebitda_reconciliation.csv` row 11
- **Severity:** Medium
- **Confidence:** High for the facts. Medium for the interpolation.
- **Deal impact:** Governance. The financing test uses the same metric (see FIN-046).
- **Cross-check:** Full CD&A in the proxy; any clawback policy.

#### FIN-054: LTM Adjusted EBITDA at a Q2 2027 closing is below 110.0 in all three scenarios (supersedes FIN-016)
- **Finding:** On the company's own definition, LTM Adjusted EBITDA for Q3 2026 to Q2 2027 is 100.0 to 106.0 even before the 2027 rate cut. It falls to 72.9 to 84.8 with the 0419U cut and the loss of Veltrane.
- **Evidence (projections):**
  - **(a) Guidance:**
    - H2 2026 = (100 to 106) - 54.1 = 45.9 to 51.9.
    - H1 2027 is flat with H1 2026 at 54.1.
    - LTM = 100.0 to 106.0 (midpoint 103.0). Shortfall = 4.0 to 10.0.
    - Q2 2026 run-rate check: 26.0 x 4 = 104.0.
  - **(b) Plus the 0419U cut on Q1 and Q2 2027:** 14.5 for the half year (FIN-058). LTM = 85.5 to 91.5. Shortfall = 18.5 to 24.5.
  - **(c) Plus loss of Veltrane from Q1 2027:**
    - Lost half-year revenue = 50.5 / 2 = 25.3, using the FY2025 rate.
    - Flow-through of 26.6% (H1 2026 Adjusted EBITDA margin) to 50.0% (assumption) = 6.7 to 12.6. Central case at 38.0% (H1 2026 gross margin) = 9.6.
    - LTM = 72.9 to 84.8 (central 75.9 to 81.9). Shortfall = 25.2 to 37.1.
  - Guidance was issued Aug 5, 2026, before Veltrane halted ATLAS-3 on Aug 27. Any Q4 2026 wind-down is not in scenario (a) (inference).
  - Possible upside: H1 2026 included about 4.0 of lost revenue from the cyber incident (10-Q), which may not recur in H1 2027.
  - Not included: any Genaro injunction (FIN-060).
- **Source:** `adjusted_ebitda_reconciliation.csv` row 11 (H1 2026); `revenue_by_customer.csv` row 3; `income_statement.csv` rows 5 and 7; 8-K Item 7.01; deal-brief section 3
- **Severity:** Critical. Test: block closing. Every scenario is below the 110.0 condition in the committed term loan.
- **Confidence:** Medium. These are projections. Scenario (a) rests directly on the company's own guidance.
- **Deal impact:** Closing risk and financing. Without a waiver or re-cut, the financing may not fund.
- **Cross-check:** Commitment letter (test date, pro forma adjustments, cure rights); Q3 2026 results.

#### FIN-055: Estimated covenant position at Jun 30, 2026: 4.39x against 4.50x, headroom about 2.2 of EBITDA (0.11x)
- **Finding:** On my estimate of Consolidated EBITDA, Corvane passed at June 30 with very thin headroom. This is consistent with the 10-Q statement that it complied.
- **Evidence:**
  - LTM operating income = 62.1 - 26.6 + 6.0 = 41.5. LTM D&A = 26.6. LTM stock compensation = 10.3.
  - EBITDA before the capped add-backs = 41.5 + 26.6 + 10.3 = 78.4.
  - Cap = 15% x 78.4 = 11.8. Available add-backs = restructuring 7.6 + other non-recurring 37.4 = 45.0, so the cap binds.
  - Consolidated EBITDA = 78.4 + 11.8 = 90.2.
  - Net leverage = 395.9 / 90.2 = 4.39x.
  - Headroom against 4.50x: Consolidated EBITDA would have to fall to 395.9 / 4.50 = 88.0, so the EBITDA headroom is 90.2 - 88.0 = 2.2 (0.11x). The net debt headroom is 4.50 x 90.2 - 395.9 = 9.8.
  - Alternative reading (cap measured on 68.1, without stock compensation): cap = 10.2, Consolidated EBITDA = 88.6, leverage = 4.47x, headroom = 0.6 (0.03x).
  - Gains: the sale-leaseback gain sits in other income, below operating income, so it is already excluded.
  - Back-test of my method: Dec 2023 4.89x, Dec 2024 4.03x, Dec 2025 3.49x (FY2025: base 62.1 + 25.4 + 9.8 = 97.3; cap 14.6; Consolidated EBITDA 111.9; 391.0 / 111.9). The 4.89x for Dec 2023 is above 4.50x. Either a different level applied in 2023, or the full definition allows more adjustments than the 10-K excerpt shows. My estimates may therefore be conservative.
- **Source:** `income_statement.csv` row 11; `adjusted_ebitda_reconciliation.csv` rows 5, 8 to 10; `balance_sheet.csv` rows 2, 16 and 17; 10-K Item 7 "Financial covenant"; 10-Q "Liquidity"
- **Severity:** High
- **Confidence:** Medium. The definition is an excerpt, the reported ratio is not disclosed, and the Dec 2023 back-test does not reconcile.
- **Deal impact:** Financing
- **Cross-check:** Credit agreement and the Jun 30, 2026 compliance certificate.

#### FIN-056: Jun 30, 2026 covenant compliance depended on the Q4 2025 estimate change
- **Finding:** Without the 14.2, my estimate of net leverage at June 30 is 5.36x, above the 4.50x maximum. A reversal or restatement of the estimate, which is under the material weakness, could turn June 30 into a historical event of default (inference).
- **Evidence:**
  - Base without the 14.2 = 78.4 - 14.2 = 64.2. Consolidated EBITDA = 64.2 x 1.15 = 73.8.
  - Net leverage = 395.9 / 73.8 = 5.36x.
  - The estimate change adds 14.2 x 1.15 = 16.3 of Consolidated EBITDA, against headroom of only 2.2.
- **Source:** As FIN-055; 10-K Item 7 "Results" and Item 9A
- **Severity:** High. It would be Critical if the estimate is revised.
- **Confidence:** Medium
- **Deal impact:** Financing and closing risk
- **Cross-check:** Auditor's view on the Q4 2025 estimate; any restatement or SEC comment.

#### FIN-057: Projected breach of the 4.00x covenant at Sep 30, 2026, before signing
- **Finding:**
  - My central estimate of net leverage at Sep 30, 2026 is 4.83x against the 4.00x maximum. Every scenario I tested is between 4.39x and 5.17x.
  - The compliance certificate is due by Nov 14, 2026 (45 days after the quarter end), before the mid-December signing.
  - A breach is an event of default. Lenders could then stop revolver draws (65.0 undrawn) and accelerate the 424.7 outstanding.
- **Evidence (projection):**
  - Sep 30 LTM = Jun 30 LTM base (78.4) - Q3 2025 base + Q3 2026 base.
  - **Q3 2025 base** (operating income + D&A + stock compensation):
    - H2 2025 = 35.5 + 13.0 + 5.0 = 53.5.
    - Less the 14.2 that sits in Q4 = 39.3.
    - Split equally across Q3 and Q4 (assumption) = 19.7.
  - **Q3 2026 base:**
    - Q3 Adjusted EBITDA = half of the guidance-implied H2 midpoint (48.9) = 24.5.
    - Less capped-type add-backs at the LTM quarterly average (45.0 / 4 = 11.3) = 13.2.
  - **Central case:**
    - Base = 78.4 - 19.7 + 13.2 = 72.0. Consolidated EBITDA = 72.0 x 1.15 = 82.7.
    - Net debt = 395.9 + 3.5 = 399.4. The 3.5 is half of the H1 2026 cash outflow of 7.0, before revolver draws (assumption).
    - Ratio = 399.4 / 82.7 = 4.83x.
  - **Range:** Q3 2026 base of 8.4 (Adjusted EBITDA 23.0, add-backs at the H1 2026 rate of 14.6) to 18.1 (Adjusted EBITDA 26.0, add-backs at the H2 2025 rate of 7.9) gives 5.17x to 4.52x. With net debt flat at 395.9, the best case is 4.48x.
  - **Headroom (central case):** Consolidated EBITDA would have to be 399.4 / 4.00 = 99.9, a shortfall of 17.1 (0.83x). Alternatively, net debt would have to fall by 399.4 - 4.00 x 82.7 = 68.4.
  - **Break-even:** passing would need a Q3 2026 base of 28.1. That is above the top of guidance for Q3 Adjusted EBITDA (26.0) even with zero add-backs, and 2.3 times the H1 2026 quarterly base (24.9 / 2 = 12.5).
  - **Robustness:** with a Q3 2025 base as low as 12.5, the ratio is still 4.39x. Even Jun 30 LTM Consolidated EBITDA (90.2) gives 4.39x against 4.00x.
  - **What would make the breach certain:** Q3 results in line with guidance. Every guidance-consistent result breaches unless net debt falls by at least about 6.0, which only works with zero add-backs.
  - **What could avoid it:** a lender waiver or amendment, an equity cure (not disclosed), or definition adjustments not shown in the excerpt (see the FIN-055 back-test).
  - **At closing:** if the breach is waived, the 4.00x test applies again at Dec 31, 2026 and Mar 31, 2027. The 0419U cut then lowers earnings from Q1 2027, so the position worsens (projection).
- **Source:** `income_statement.csv` row 11; `adjusted_ebitda_reconciliation.csv` rows 5, 8 to 11; `balance_sheet.csv` rows 2, 16 and 17; `cash_flow.csv` (H1 2026 flows per FIN-022); 10-K Item 7 "Financial covenant"; 10-Q "Liquidity"; 8-K Item 7.01
- **Severity:** Critical. Test: block closing, because by the calibration rule a projected event of default before signing is Critical. The default is projected at the Sep 30, 2026 test, with the certificate due Nov 14, 2026, before the mid-December signing. It would also leave liquidity of only 28.8 of cash if the revolver is frozen.
- **Confidence:** Medium. These are projections on an excerpted definition. The conclusion holds under every assumption I tested.
- **Deal impact:** Closing risk, financing and liquidity before signing
- **Cross-check:** Q3 2026 10-Q and compliance certificate; any waiver or amendment 8-K; the cure provisions in the credit agreement. SEC analyst: check whether the 10-Q discloses any risk to the Sep 30 test (the excerpt does not).

#### FIN-058: The 2027 Medicare cut for 0419U removes about 29.0 a year of revenue and EBITDA (382.8 of EV, 23.2%)
- **Finding:** The 30% rate cut hits Medicare OncoTrace revenue and the share of commercial OncoTrace revenue priced off the Medicare rate. FY2026 guidance excludes it.
- **Evidence:**
  - Rate change: 1,505 / 2,150 - 1 = -30.0%.
  - Base, H1 2026 annualized:
    - OncoTrace = 146.0 x 45% = 65.7.
    - Medicare portion = 65.7 x 56% = 36.8.
    - Non-Medicare portion = 28.9, of which 40% is Medicare-linked = 11.6.
  - Half-year cut = (36.8 + 11.6) x 30% = 11.0 + 3.5 = 14.5. Annual = 29.0.
  - On the FY2025 mix: 138.5 x (55% x 30% + 45% x 40% x 30%) = 138.5 x 21.9% = 30.3. On normalized OncoTrace of 124.3: 27.2. Range = 27.2 to 30.3.
  - I assume 100% flow-through to EBITDA: a price cut with no cost change, unchanged volume, mix and collection rate.
  - The cut equals 7.1% of FY2026 guidance revenue (29.0 / 410) and 28.2% of guidance Adjusted EBITDA (29.0 / 103.0).
  - Value: 29.0 x 13.2 = 382.8, which is 23.2% of EV (US$7.31 per share). At 11.0x: 319.0.
- **Source:** `income_statement.csv` row 2; `kpis.csv` rows 4 and 5; 10-K Item 1 "Payer contracts"; news 2026-07-30; 8-K Item 7.01
- **Severity:** Critical. Test: more than 10% of value (23.2% of EV).
- **Confidence:** Medium. The inputs are primary-source, but flow-through and constant volume are assumptions. It is unclear whether the "Medicare share" includes Medicare Advantage.
- **Deal impact:** Valuation. It breaks the brief's "Medicare rates flat through 2030" assumption.
- **Cross-check:** Any CMS reconsideration request (the news says this is possible "only in limited circumstances"); the exact commercial contracts that reference the Medicare rate.

#### FIN-059: Genaro royalty of about 11.8 a year before the rate cut and 9.2 after
- **Finding:** A 9% royalty on OncoTrace net revenue is a recurring EBITDA cost until the v3 redesign launches. Corvane has recorded no accrual.
- **Evidence:**
  - OncoTrace H1 2026 annualized = 65.7 x 2 = 131.4. Royalty = 9% x 131.4 = 11.8 a year.
  - After the cut: (131.4 - 29.0) = 102.4, so the royalty is 9.2 a year.
  - Royalty through mid-2027 (projection): H2 2026 = 65.7 x 9% = 5.9; H1 2027 = (65.7 - 14.5) x 9% = 4.6. Total = 10.5.
  - Plus past damages claimed of 68.0, for a total cash exposure of 78.5 (4.8% of EV).
  - If v3 fails and the royalty becomes permanent: 9.2 x 13.2 = 121.4 (7.4% of EV), or 155.8 (9.5%) on the pre-cut base.
- **Source:** `income_statement.csv` row 2; `kpis.csv` row 4; LIT-002 docket entries 2026-09-25 and 2026-10-02; 10-K Item 3; 10-Q Part II Item 1
- **Severity:** High. It needs a specific escrow or indemnity. These are claimed amounts, not a judgment.
- **Confidence:** Medium. It is a claim, the outcome is uncertain and the v3 timing is projected.
- **Deal impact:** Valuation and post-closing
- **Cross-check:** Litigation analyst: the probability of success after the adverse Markman order and the denial of inter partes review.

#### FIN-060: A Genaro injunction would put about 102.4 to 131.4 of annual OncoTrace revenue at risk, inside the closing LTM window
- **Finding:** An injunction after the Feb 8, 2027 trial and before the mid-2027 v3 launch would stop sales of the product that brings in about 32% of revenue, during Q1 and Q2 2027.
- **Evidence:**
  - Annual OncoTrace revenue at risk: 131.4 before the cut (131.4 / 406.8 = 32.3% of H1 2026 annualized revenue), 102.4 after.
  - Illustrative 5 months at the post-cut rate: 102.4 x 5 / 12 = 42.7 of revenue (projection).
  - At an assumed 50% contribution margin, that is 21.3 of EBITDA. This would lower the FIN-054 scenarios further.
  - The v3 launch also depends on New York State approval.
- **Source:** As FIN-059
- **Severity:** High. It becomes Critical if an injunction issues without a stay.
- **Confidence:** Low. The injunction timing, any stay and the margin are all assumptions.
- **Deal impact:** Closing risk (110.0 condition, MAE) and valuation
- **Cross-check:** Litigation analyst: the likelihood of an injunction and the bond or stay practice in D. Del.

#### FIN-061: Genaro's 68.0 past damages do not reconcile with 9% of OncoTrace revenue in the data pack
- **Finding:** At 9%, 68.0 implies a royalty base of 755.6. OncoTrace revenue in my data from FY2023 to H1 2026 totals 427.9.
- **Evidence:**
  - 68.0 / 9% = 755.6.
  - OncoTrace revenue: 103.6 + 120.1 + 138.5 + 65.7 = 427.9. At 9%, that is 38.5. The gap is 29.5.
  - The gap may reflect earlier years (FY2022 share not given), a gross-charge base, or enhanced damages (inference).
- **Source:** `income_statement.csv` row 2; `kpis.csv` row 4; LIT-002 entry 2026-09-25
- **Severity:** Medium
- **Confidence:** Medium
- **Deal impact:** Sizing of the escrow
- **Cross-check:** Genaro's damages expert report (the royalty base and period).

#### FIN-062: Veltrane: 50.5 of revenue and 61.0 of backlog at risk, worth 10.8% to 15.4% of EV
- **Finding:** Veltrane halted ATLAS-3, which provides most of its revenue to Corvane. It can end work orders on 90 days' notice and pay only for work performed, so the 61.0 of backlog is not protected.
- **Evidence:**
  - Revenue: 50.5 (rank 2, 11.7% of FY2025 revenue; 51.2% of biopharma revenue).
  - Backlog: 61.0 / 231.4 = 26.4%. Backlog covers 61.0 / 50.5 = 1.2 years of Veltrane revenue.
  - Annual EBITDA at risk: 50.5 x 26.6% = 13.4 to 50.5 x 38.0% = 19.2 (assumed flow-through).
  - Value at 13.2x: 177.3 (10.8% of EV) to 253.3 (15.4% of EV).
  - Contract assets of 11.6 may include unbilled Veltrane work. Veltrane is cutting 40% of its staff, so there is also a collection risk (inference).
- **Source:** `revenue_by_customer.csv` row 3; `income_statement.csv` row 3; `balance_sheet.csv` row 4; 10-K Item 1 "Biopharma services"; 10-Q "Biopharma services"; news 2026-08-27
- **Severity:** Critical. Test: more than 10% of value (10.8% to 15.4% of EV, even at the low flow-through).
- **Confidence:** Medium. The revenue and backlog figures are primary-source. The flow-through and the absence of any replacement work are assumptions.
- **Deal impact:** Valuation and closing (the 110.0 condition, FIN-054)
- **Cross-check:** Any termination notice from Veltrane (8-K or Q3 10-Q); Veltrane's receivable balance; wind-down fees.

#### FIN-063: Excluding Veltrane, biopharma revenue was 48.1 and backlog 170.4; group growth excluding Veltrane and the estimate change was 5.3%
- **Finding:** Biopharma revenue excluding Veltrane shrank in FY2025.
- **Evidence:**
  - Biopharma excluding Veltrane: FY2024 89.8 - 38.0 = 51.8; FY2025 98.6 - 50.5 = 48.1 (-7.1%). This assumes all Veltrane revenue is biopharma, as the 10-K implies.
  - Backlog excluding Veltrane = 231.4 - 61.0 = 170.4. That is 170.4 / 48.1 = 3.5 years of revenue excluding Veltrane, which looks long. The burn schedule is needed.
  - Group revenue excluding Veltrane and the 14.2: (431.0 - 50.5 - 14.2) / (386.0 - 38.0) = 366.3 / 348.0 = +5.3%. This still includes Pell Ridge.
- **Source:** `revenue_by_customer.csv` row 3; `income_statement.csv` rows 3 and 5; 10-Q "Biopharma services"
- **Severity:** Medium
- **Confidence:** Medium. The segment mapping is assumed.
- **Deal impact:** Valuation (base growth rate)
- **Cross-check:** Backlog by client and expected conversion timing.

#### FIN-064: The FY2026 guidance cut supersedes the base case (updates FIN-018)
- **Finding:** Adjusted EBITDA guidance was cut by 34.0 (24.8%). The implied H2 2026 is weaker than H2 2025 even after normalization.
- **Evidence:**
  - Midpoints: revenue 460 to 410 (-10.9%); Adjusted EBITDA 137.0 to 103.0 (-24.8%).
  - Implied H2 2026 revenue = 410 - 203.4 = 206.6, versus normalized H2 2025 of 225.8 - 14.2 = 211.6 (-2.4%).
  - Implied H2 2026 Adjusted EBITDA = 48.9, versus normalized H2 2025 of 69.3 - 14.2 = 55.1 (-11.3%). Implied margin = 48.9 / 206.6 = 23.7%.
  - Quarterly Adjusted EBITDA: Q1 2026 28.1, Q2 2026 26.0.
  - At US$24.00 and June net debt: 1,653.5 / 103.0 = 16.1x.
- **Source:** 8-K Items 2.02 and 7.01; `adjusted_ebitda_reconciliation.csv` row 11; `income_statement.csv` row 5
- **Severity:** High (the value effect is quantified in FIN-065 and not counted again here)
- **Confidence:** High
- **Deal impact:** Valuation. The June 30 model is stale.
- **Cross-check:** Q3 2026 results; whether guidance is maintained after the Veltrane halt.

#### FIN-065: Rebased valuation: central pro forma run-rate EBITDA of 54.8 gives US$6.25 per share at 13.2x
- **Finding:** Each disclosed event since the model date lowers the earnings base. On a normalized, pro forma 2027 run-rate, company definition, 13.2x supports US$6.25 to US$7.71 per share, against the US$24.00 offer (projection).
- **Evidence:** Bridge, each step applied once. Net debt is 395.9 and there are 52.4m shares.

| Step | Adj. | EBITDA | Price at 13.2x | Price at 11.0x |
|---|---|---|---|---|
| FY2025 company Adjusted EBITDA | | 125.3 | 24.01 | 18.75 |
| 1. Remove the Q4 2025 estimate change (FIN-050) | -14.2 | 111.1 | 20.43 | 15.77 |
| 2. Current trading: FY2026 guidance midpoint, which has no 2025 one-off (FIN-064) | -8.1 | 103.0 | 18.39 | 14.07 |
| 3. 0419U cut, annual (FIN-058) | -29.0 | 74.0 | 11.09 | 7.98 |
| 4a. Loss of Veltrane at 26.6% flow-through (FIN-062) | -13.4 | 60.6 | 7.71 | 5.17 |
| 4b. Loss of Veltrane at 38.0% (central, instead of 4a) | -19.2 | 54.8 | 6.25 | 3.95 |
| Optional: rent cut to market (FIN-066) | +1.2 | 56.0 | 6.55 | 4.20 |

  - How each price is worked out, for example step 3 at 13.2x: 74.0 x 13.2 = 976.8; less 395.9 = 580.9; divided by 52.4 = US$11.09.
  - Even steps 1 and 2 alone give US$18.39, which is 23.4% below US$24.00.
  - Implied multiple of the US$24.00 offer (EV 1,653.5) on each base: 111.1 = 14.9x; 103.0 = 16.1x; 74.0 = 22.3x; 54.8 = 30.2x.
  - Not in the run-rate, to avoid double counting:
    - The Genaro royalty is temporary until v3, so treat it as escrow or a debt-like item. Past damages claimed of 68.0 would be US$1.30 per share if treated as debt.
    - The denial write-off add-back (LTM 13.1). The FA quality-of-earnings memo would give 54.8 - 13.1 = 41.7.
    - No mitigation is assumed: no CMS reconsideration, no replacement for Veltrane, no cost actions.
- **Source:** As the cited findings; `balance_sheet.csv` rows 2, 16 and 17; deal-brief section 2
- **Severity:** Critical. Test: more than 10% of value. Steps 1 and 2 alone cut the supportable price by 23.4%. The central case cuts it by 74%.
- **Confidence:** Medium. These are projections with stated assumptions. A 13.2x multiple may not apply to a re-based earnings stream.
- **Deal impact:** Valuation. The offer price is not supported on current information.
- **Cross-check:** Current share price after Aug 5 and Aug 27 (news); peer multiples. The Jul 31 reference price predates the guidance cut and the Veltrane halt.

#### FIN-066: Term loan of 750.0 equals 7.3x to 13.7x re-based EBITDA
- **Finding:** On re-based earnings, the planned debt cannot be serviced at the brief's sizing.
- **Evidence:**
  - Leverage: 750.0 / 103.0 = 7.28x; / 74.0 = 10.14x; / 54.8 = 13.69x.
  - Pro forma interest of 61.8 (FIN-017 projection) is covered 1.67x, 1.20x and 0.89x respectively.
- **Source:** deal-brief section 3; FIN-017; FIN-065
- **Severity:** High
- **Confidence:** Medium. The loan pricing is projected.
- **Deal impact:** Financing. Expect resizing, repricing or a lender walk.
- **Cross-check:** Commitment letter flex and MAE wording.

#### FIN-067: Related-party rent premium of 1.2 a year; renegotiating to market adds 1.2 of EBITDA (15.8 of EV)
- **Finding:** The HQ lease with Mr. Ellery's entity is 33% above the appraised market rent and was extended to 2040.
- **Evidence:**
  - 4.8 - 3.6 = 1.2. 4.8 / 3.6 - 1 = 33.3%.
  - Rent is an operating cost inside EBITDA, so a market rent adds +1.2. At 13.2x that is 15.8 (1.0% of EV, US$0.30 per share).
  - Total premium over 2026 to 2040 if both rents grow 3.5% a year: 1.2 x (1.035 + ... + 1.035^15) = 1.2 x 20.0 = 24.0, undiscounted (projection).
- **Source:** DEF 14A "Certain relationships and related transactions"; 10-K Note 12
- **Severity:** Medium (a governance and negotiation point; small in value)
- **Confidence:** High for the premium. Medium for the projection.
- **Deal impact:** Valuation (minor) and governance. Seek an amendment at signing.
- **Cross-check:** Whether the 3.5% escalator also applies to market rent; the appraisal report.

#### FIN-068: The Oct 1, 2025 goodwill test rested on assumptions that later events contradict
- **Finding:** The Clinical testing unit had about 14% headroom, based on stable OncoTrace Medicare rates and 9% growth. Both assumptions have since failed, and the share price has fallen 34.9% since the test date.
- **Evidence:**
  - Share price: 27.80 at the test date versus 18.10 on Jul 31, 2026 (-34.9%). The offer of 24.00 is 13.7% below the test-date price.
  - Market capitalization (52.4m diluted shares as a proxy): 1,456.7 to 948.4 (-508.3).
  - Clinical testing goodwill is 241.5. The 10-K says a 10% cut in projected cash flows "would eliminate most of the headroom".
  - The 0419U cut (29.0) is 9.9% of annualized clinical revenue (292.0), and a much larger share of the unit's cash flow because it is a price cut (inference).
  - The 22.3 of Pell Ridge goodwill was never tested.
  - The Oct 1, 2026 test date has passed, and the result is due in the Q3 10-Q.
  - If the credit agreement treats an impairment as a non-cash cost outside the add-backs, it could also affect Consolidated EBITDA (question for counsel).
- **Source:** 10-K "Critical accounting estimates: goodwill"; `balance_sheet.csv` row 8; deal-brief section 2
- **Severity:** High
- **Confidence:** Medium. Reporting-unit cash flows are not available.
- **Deal impact:** Disclosure, post-closing purchase accounting, possible covenant effect
- **Cross-check:** Q3 2026 10-Q goodwill note.

#### FIN-069: Orvia (rank 3, 48.7, 11.3% of revenue) can terminate on a change of control
- **Finding:** The take-private itself gives Orvia the right to terminate on 60 days' notice.
- **Evidence:**
  - Revenue at risk: 48.7.
  - At 26.6% to 38.0% flow-through (assumption): 13.0 to 18.5 of EBITDA, or 171.0 to 244.3 at 13.2x (10.4% to 14.8% of EV) if Orvia terminates.
  - Contract term otherwise runs to Dec 31, 2028.
- **Source:** `revenue_by_customer.csv` row 4; 10-K Item 1 "Payer contracts"
- **Severity:** High. This is a right, not an event, and calls for a consent or waiver as a closing condition.
- **Confidence:** Medium
- **Deal impact:** Closing condition and valuation
- **Cross-check:** Orvia agreement change-of-control definition; any Orvia disputes in the news or litigation records.

#### FIN-070: Helixor reagent prices are fixed and tariffs are borne by Helixor through 2028 (neutralized)
- **Finding:** Reagent tariff risk is carried by the supplier during the forecast period, so no EBITDA adjustment is needed.
- **Evidence:** Prices are fixed to Dec 31, 2028, "inclusive of all import duties and tariffs, which Helixor bears".
- **Source:** 10-K Item 1 "Suppliers"
- **Severity:** Low (neutralized by contract)
- **Confidence:** High
- **Deal impact:** None to 2028. Renewal risk after that.
- **Cross-check:** News 2026-09-17 on sequencing reagent tariffs (news analyst).

#### FIN-071: Hollis wage class action dismissed with prejudice (closed)
- **Finding:** No financial exposure remains.
- **Evidence:** Dismissed with prejudice on Jun 9, 2026.
- **Source:** 10-Q Part II Item 1
- **Severity:** Low (closed)
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** Docket, for any appeal window.

#### FIN-072: Cyber incident: about 4.0 of lost revenue not added back; insurance limit of 10.0
- **Finding:** Lost revenue is correctly left in Adjusted EBITDA, and the H1 2027 comparison will be easier. Insurance covers the 6.1 spent so far, leaving 3.9 of the limit for class actions and the HHS Office for Civil Rights inquiry.
- **Evidence:** 10.0 - 6.1 = 3.9.
- **Source:** 10-Q "Cybersecurity incident"; `adjusted_ebitda_reconciliation.csv` row 16
- **Severity:** Low
- **Confidence:** Medium. Claims beyond the limit cannot be estimated.
- **Deal impact:** Post-closing (indemnity)
- **Cross-check:** LIT-003 (litigation analyst).

#### FIN-073: Corrections to the iteration 2 input facts
- **Finding:**
  - The 40% Medicare-linked commercial pricing is disclosed in 10-K Item 1 "Payer contracts", not in the 10-Q.
  - The covenant add-back covers "cash" costs.
  - The 8-K gives Q2 2026 Adjusted EBITDA of 26.0.
- **Source:** As stated
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Citation accuracy
- **Cross-check:** None needed.

---

### Positive or mitigating points

- **Debt maturities:** the term loan matures Oct 2029 and the revolver Oct 2028, so there is no maturity before closing (10-K Item 7). Both are repaid at closing in the brief.
- **Supply or price protection:** Helixor bears tariffs and reagent prices are fixed through 2028 (FIN-070).
- **Items correctly excluded from adjusted metrics:** cyber lost revenue is not added back (FIN-072). The sale-leaseback gain is excluded (FIN-015).
- **Litigation closed:** Hollis was dismissed with prejudice (FIN-071).
- **No overlap:** the 14.2 adjustment and the denial write-off add-back do not overlap, so my normalization does not double count (FIN-050).
- **Possible upside in H1 2027:** cyber lost revenue of about 4.0 may not recur (FIN-054). A CMS reconsideration of 0419U is possible but limited (FIN-058). The rent could be renegotiated (+1.2, FIN-067).
- **Retention:** informatics gross revenue retention is stable at 95% to 96% (FIN-040).

### Gaps and questions for management

1. Credit agreement: the full Consolidated EBITDA definition, the covenant levels before 2026, equity cure rights, and the Jun 30, 2026 compliance certificate with the actual ratio (FIN-055 to FIN-057).
2. Q3 2026 results, the Sep 30 covenant calculation, and any waiver discussions with lenders (FIN-057).
3. Commitment letter: the LTM test definition, whether changes in estimates are allowed, and pro forma adjustments (FIN-050, FIN-054).
4. Veltrane: any termination notice, wind-down revenue, H1 2026 Veltrane revenue, and unbilled or receivable balances (FIN-062).
5. Backlog excluding Veltrane by client and conversion schedule (FIN-063).
6. OncoTrace payer mix: whether the Medicare share includes Medicare Advantage, and which commercial contracts reference 0419U (FIN-058).
7. The Q4 2025 collection-rate model and its validation, and the effect of the 14.2 on the reserve roll-forward (FIN-052).
8. Genaro: the expert damages base and period, and the v3 validation status and New York State filing (FIN-059 to FIN-061).
9. Pell Ridge revenue and EBITDA (FIN-049).
10. The Oct 1, 2026 goodwill impairment test result (FIN-068).
11. The Orvia change-of-control clause and any consent process (FIN-069).
12. Lease escalation terms and the market rent appraisal (FIN-067).
