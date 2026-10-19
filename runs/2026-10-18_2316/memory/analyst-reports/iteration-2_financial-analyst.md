<!-- Iteration 2, financial-analyst. Full report as returned by the analyst, saved unedited by the lead agent. -->

## Financial analyst: findings (iteration 2)

### Files reviewed
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md`
- `.../data/financials/income_statement.csv`
- `.../data/financials/adjusted_ebitda_reconciliation.csv`
- `.../data/financials/balance_sheet.csv`
- `.../data/financials/cash_flow.csv`
- `.../data/financials/revenue_quarterly.csv`
- `.../data/financials/revenue_by_customer.csv`
- `.../data/financials/kpis.csv`
- `.../data/financials/README.md`

The lead agent also gave me facts from the 10-K FY2025 (Note 9, Note 2, the Gen-3 mix) and the 10-Q Q2 2026 (2.26x, guidance, the $9.4M return, the $2.3M credits). I cite these as "10-K (via lead)" or "10-Q (via lead)". None of the financial files contain text that tries to instruct the agents.

**How I treated the covenant (applies to FIN-14 and FIN-15):**
- **Base EBITDA:** I used the company's EBITDA line (reconciliation row 7). This line deducts other income. The literal Note 9 wording (net income + interest + taxes + D&A) gives LTM 48.6 instead of 48.2. That is shown as a sensitivity.
- **Stock-based compensation:** I treated it as a separate add-back that sits outside the 15% cap. In the Note 9 wording, the parenthetical "Permitted Add-backs" follows the restructuring list, not SBC.
- **Permitted Add-backs:** Restructuring (row 9) plus all "Other non-recurring items" (row 10, detail rows 16 to 20). This is the most generous reading. The cap binds either way.

### Key metrics table (reported unless marked adjusted)

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 / LTM Q2 2026 |
|---|---|---|---|---|
| Total revenue | 368.9 | 421.7 | 502.3 | H1 222.6 / LTM 498.4 |
| Revenue growth | 18.1% | 14.3% | 19.1% | H1 -1.7% |
| Adjusted: revenue excl. bill-and-hold and Q2 credits | n/a | n/a | 470.5 (+11.6%) | H1 234.3 (+3.4%) |
| Gross margin | 40.1% | 40.8% | 41.1% | H1 38.0% |
| EBITDA (company line) | 42.2 | 52.3 | 64.1 | LTM 48.2 |
| Adjusted EBITDA (company) | 60.4 | 74.8 | 98.8 | LTM 89.7 |
| All add-backs / Adj. EBITDA | 30.1% | 30.1% | 35.1% | LTM 46.3% |
| Permitted Add-backs / pre-add-back base | 12.3% | 13.0% | 21.5% | LTM 35.9% |
| Adjusted: capped Consolidated EBITDA | 60.4 | 74.8 | 93.5 | LTM 75.9 |
| Total debt (revolver + term loan) | 120.0 | 200.0 | 220.0 | 227.5 |
| Covenant net debt (cash netting capped at 25.0) | 95.0 | 175.0 | 195.0 | 202.5 |
| Adjusted: Total Net Leverage, capped | 1.57x | 2.34x | 2.09x | 2.67x (limit 3.50x) |
| Total Net Leverage, as reported (uncapped) | n/a | n/a | 1.97x | 2.26x (10-Q) |
| Interest cover (EBITDA / interest) | 5.7x | 5.3x | 4.7x | LTM 3.2x |
| Operating cash flow / free cash flow | 30.8 / 16.2 | 40.8 / 24.6 | 9.7 / -10.1 | H1 -4.2 / -13.0 |
| Norvale share of revenue | n/a | 28.0% | 31.1% (adj. 28.0%) | n/a |
| Hardware revenue | 236.0 | 261.9 | 301.4 (adj. 269.6) | H1 116.9 (-12.9%) |
| Hardware backlog | 142.0 | 168.0 | 131.0 | 118.0 |

**Workings for the table:**
- **Revenue growth:** 56.5/312.4 = 18.1%; 52.8/368.9 = 14.3%; 80.6/421.7 = 19.1%; H1 (222.6 - 226.5)/226.5 = -1.7%.
- **LTM figures:** LTM revenue = 502.3 - 226.5 + 222.6 = 498.4. H1 gross margin = 84.6/222.6 = 38.0%.
- **Add-backs / Adj. EBITDA:** FY2023 (11.6+4.6+2.0)/60.4; FY2024 (13.9+5.2+3.4)/74.8; FY2025 (17.2+7.9+9.6)/98.8; LTM (17.8+9.7+14.0)/89.7.
- **Permitted / pre-add-back base:** FY2023 6.6/(42.2+11.6) = 6.6/53.8; FY2024 8.6/66.2; FY2025 17.5/81.3; LTM 23.7/66.0.
- **Capped Consolidated EBITDA, FY2025:** 81.3 + min(17.5, 0.15 x 81.3 = 12.2) = 93.5.
- **Capped leverage:** FY2023 95.0/60.4; FY2024 175.0/74.8; FY2025 195.0/93.5. FY2025 uncapped = 195.0/98.8 = 1.97x.
- **Interest cover:** 42.2/7.4; 52.3/9.8; 64.1/13.6; LTM 48.2/14.9.

### Findings

#### FIN-14: The reported 2.26x leverage ignores the 15% add-back cap. The capped ratio is 2.67x.
- **Finding:** I can reproduce the reported 2.26x exactly only by using the company's uncapped Adjusted EBITDA of 89.7. With the Note 9 cap applied, the ratio at June 30, 2026 is 2.67x. That still complies with the 3.50x limit, but headroom is much thinner than the 10-Q implies. Permitted Add-backs were 35.9% of the pre-add-back base, against a 15% cap. They first went over the cap in FY2025 (21.5%).
- **Evidence (LTM Q2 2026, capped):**
  - LTM EBITDA = 4.4 + 14.9 + 1.4 + 27.9 - 0.4 = 48.2.
    - Cross-check of the inputs: net income 18.6 - 5.3 - 8.9 = 4.4; SBC 17.8 = 17.2 - 8.3 + 8.9.
  - Pre-add-back base = 48.2 + 17.8 = 66.0.
  - Permitted Add-backs = 9.7 restructuring + 14.0 other non-recurring = 23.7.
    - The 14.0 is Vantor litigation 4.1, customer implementation delays 3.3, auditor transition 2.3, CFO search 2.5 and cyber 1.8.
  - Cap = 15% x 66.0 = 9.9. Capped Consolidated EBITDA = 66.0 + 9.9 = 75.9. Disallowed add-backs = 23.7 - 9.9 = 13.8.
  - Total Debt = 45.0 revolver + 182.5 term loan = 227.5. Cash 33.9, netting capped at 25.0. Covenant net debt = 202.5.
  - **Capped ratio** = 202.5 / 75.9 = **2.67x**. Limit 3.50x. EBITDA cushion = 75.9 - 202.5/3.50 (57.9) = 18.0, or 23.7%.
  - **Uncapped ratio** = 202.5 / 89.7 = **2.26x**. This matches the 10-Q. With full cash netting it would be 193.6/89.7 = 2.16x, so the company did apply the $25.0M cash cap but not the add-back cap.
  - **Sensitivity, literal EBITDA (48.6):** base 66.4, cap 9.96, capped 76.4, ratio 2.65x. Uncapped 90.1 gives 2.25x.
  - **Sensitivity, stricter reading (SBC inside the cap):** base 48.2, cap 7.2, capped 55.4, ratio 202.5/55.4 = **3.65x. That would be a breach at June 30.**
- **Source:** `adjusted_ebitda_reconciliation.csv` rows 2 to 11, column LTM_Q2_2026; `balance_sheet.csv` rows 2, 16, 17, column Q2_2026. Note 9 definition and the 2.26x figure from the 10-K and 10-Q (via lead).
- **Severity:** High. There is no breach at June 30 on my primary reading. But the company's compliance statement does not follow the definition as quoted. That points to a disclosure or controls issue and overstates headroom.
- **Confidence:** High for the arithmetic, since 2.26x reproduces exactly. The legal reading of the cap (and whether SBC sits inside it) needs counsel to confirm against the full credit agreement.
- **Deal impact:** Financing, closing risk, and governance (IC Q4 and Q5).
- **Cross-check:**
  - Read the full credit agreement exhibit in SEC filings for the exact cap wording and how SBC is treated.
  - Get the compliance certificates delivered to lenders.
  - Check the 10-Q covenant note for how the ratio was computed.
  - Look for any lender amendment or waiver (8-K).

#### FIN-15: Projected breach of the 3.00x step-down at September 30 and December 31, 2026 (projection)
- **Finding (projection):** On the capped definition, the Q3 2026 test is close to the limit at 2.99x to 3.09x in the base case. The December 31, 2026 test breaches 3.00x across the whole guidance range, at 3.10x to 3.61x even with flat net debt. On the company's uncapped method, both dates comply except the low end of guidance with continued cash burn (3.08x).
- **Evidence:**

  **Assumptions (projection):**
  - **Q3 2025, which drops out of the LTM:**
    - Q3 2025 EBITDA is about 12.4, solved from (H2 2025 EBITDA 37.8 - bill-and-hold GP 13.1) / 2. H2 2025 EBITDA = 64.1 - 26.3 = 37.8. Q4 revenue excluding bill-and-hold (122.6) is close to Q3 (121.4).
    - Q3 2025 SBC is 4.45 (H2 8.9 / 2). Q3 2025 add-backs are 6.55 ((5.3 + 7.8) / 2).
    - So the LTM base excluding Q3 2025 = 66.0 - 16.85 = 49.15.
  - **Q3 2026, Scenario A (run rate):** EBITDA 5.2 (H1 2026 10.4 / 2), SBC 4.45, add-backs 5.3.
  - **Q3 2026, Scenario B (guidance pace):** Q3 Adjusted EBITDA = half of the implied H2 of (74.0 - 29.9) = 22.05, so EBITDA = 22.05 - 4.45 - 5.3 = 12.3.
  - **Net debt:** flat at 202.5, or 209.0 if Q3 free cash flow is -6.5 (half of H1's -13.0) and funded by the revolver.
  - The cap binds in every case.

  **September 30, 2026 (limit 3.00x):**

  | Case | LTM base | Capped EBITDA | Capped ratio | Uncapped ratio |
  |---|---|---|---|---|
  | A, flat debt | 49.15 + 9.65 = 58.80 | 67.6 | 202.5/67.6 = **2.99x** | 202.5/81.25 = 2.49x |
  | A, debt 209.0 | 58.80 | 67.6 | 209.0/67.6 = **3.09x** | 2.57x |
  | B, flat / 209.0 | 49.15 + 16.75 = 65.90 | 75.8 | 2.67x / 2.76x | 2.29x / 2.37x |
  | A, sensitivity with Q3 2025 EBITDA 16.6 (revenue-proportional split) | 54.60 | 62.8 | 3.23x / 3.33x | n/a |

  - Uncapped LTM for Scenario A = 89.7 - 23.4 + 14.95 = 81.25.

  **December 31, 2026 (LTM = FY2026, limit 3.00x):**
  - FY2026 SBC is assumed at 17.8 (8.9 x 2). Add-backs are assumed at 21.2 ((4.4 + 6.2) x 2).
  - Implied reported EBITDA = guidance Adjusted EBITDA - 17.8 - 21.2:
    - low 70.0 gives 31.0;
    - midpoint 74.0 gives 35.0;
    - high 78.0 gives 39.0.

  | Guidance | Base (EBITDA + SBC) | Capped (x1.15) | Ratio, net debt 202.5 | Ratio, net debt 215.5 | Uncapped, 202.5 / 215.5 |
  |---|---|---|---|---|---|
  | Low 70 | 48.8 | 56.1 | **3.61x** | 3.84x | 2.89x / 3.08x |
  | Mid 74 | 52.8 | 60.7 | **3.33x** | 3.55x | 2.74x / 2.91x |
  | High 78 | 56.8 | 65.3 | **3.10x** | 3.30x | 2.60x / 2.76x |

  - Net debt of 215.5 assumes H2 free cash flow of -13.0, funded by debt.

  **Breach thresholds at 3.00x:**
  - **Capped:**
    - With net debt 202.5: capped EBITDA must be at least 67.5, so EBITDA + SBC at least 67.5/1.15 = 58.7, so LTM EBITDA at least 40.9 (with SBC 17.8). That is equivalent to company Adjusted EBITDA of at least 79.9 at 21.2 of add-backs, which is above the top of guidance (78).
    - With net debt 215.5: EBITDA at least 44.7, equivalent to Adjusted EBITDA of 83.7.
  - **Uncapped:** Adjusted EBITDA must be at least 67.5 (net debt 202.5) or 71.8 (net debt 215.5).
  - **Q3 2026 alone:** to pass the September 30 test (capped), Q3 2026 EBITDA needs to be at least 5.1 with flat debt, or at least 7.0 at 209.0. The H1 2026 average was 5.2 per quarter. If Q3 2025 EBITDA was 16.6, the requirement rises to 9.3 or 11.2.
  - **Guidance requires a steep H2:** H2 implied Adjusted EBITDA of 44.1 against 29.9 in H1, an increase of 47.5%.
- **Source:** `adjusted_ebitda_reconciliation.csv` rows 7 to 11 (FY2025, H1_2025, H1_2026, LTM); `income_statement.csv` row 22; `cash_flow.csv` row 24; `revenue_quarterly.csv` rows 8 and 9; `balance_sheet.csv` rows 2, 16, 17. Guidance, limits and definition from the 10-Q and 10-K (via lead).
- **Severity:** Critical.
  - **Test met:** default before signing or closing, under the calibration rule.
  - **Supporting numbers:**
    - The September 30, 2026 test date has already passed and falls before the November 6 IC. The base case projects 2.99x to 3.09x against 3.00x.
    - The December 31, 2026 projection is 3.10x to 3.61x even at flat net debt, across the whole guidance range. On the November 20 exclusivity timetable, that test date probably falls before closing (inference).
  - **When to downgrade:** if Q3 2026 results show the capped ratio below 3.00x, or if counsel confirms a reading under which the cap does not bind, the lead should downgrade September to High. If closing is expected before the December test certificate is due, the change-of-control refinancing cures it and the rubric gives High.
- **Confidence:** Medium. These are projections, and the Q3 2025 quarterly EBITDA is estimated. The December breach is robust to guidance level, but not to the cap interpretation.
- **Deal impact:** Financing and closing risk.
  - Talonfield may need a lender waiver or amendment between signing and closing.
  - Change of control is itself an event of default, so the full 227.5 must be refinanced at closing in any case.
- **Cross-check:**
  - The Q3 2026 10-Q or earnings release (likely around the IC date).
  - Quarterly EBITDA for Q3 and Q4 2025 in the 10-Q filings.
  - 8-K filings for any credit agreement amendment.
  - News on lender talks.
  - Revolver commitment size, which is not in `data/financials`.

#### FIN-16: Bill-and-hold drove FY2025 growth and margin expansion (estimate)
- **Finding:** Without the $31.8M of Q4 2025 bill-and-hold:
  - FY2025 growth falls from 19.1% to 11.6%.
  - Q4 2025 growth falls from 32.4% to 5.1%.
  - Hardware growth falls from 15.1% to 2.9%.
  - About 13.1 of FY2025 EBITDA (estimate) came from these units.
- **Evidence:**
  - **Total revenue:** FY2025 excluding bill-and-hold = 502.3 - 31.8 = 470.5. Growth = 48.8/421.7 = 11.6%, against 80.6/421.7 = 19.1% reported.
  - **Q4 2025:** (154.4 - 31.8) = 122.6. Against 116.6 in Q4 2024, that is 6.0/116.6 = 5.1%. Reported: 37.8/116.6 = 32.4%.
  - **Hardware:** 301.4 - 31.8 = 269.6. Against 261.9, that is 7.7/261.9 = 2.9%. Reported: 39.5/261.9 = 15.1%.
  - **Gross profit (estimate):** `data/financials` does not split cost of revenue by segment, so I cannot compute a FY2025 hardware gross margin. As a proxy I used consolidated gross margin of 206.3/502.3 = 41.1%. Estimated GP = 31.8 x 41.1% = 13.1. The range at 30% to 50% margin is 9.5 to 15.9.
  - **EBITDA and Adjusted EBITDA (estimate, assuming no incremental opex):**
    - EBITDA excluding bill-and-hold is about 64.1 - 13.1 = 51.0.
    - Adjusted EBITDA is about 98.8 - 13.1 = 85.7.
    - The adjusted margin is 85.7/470.5 = 18.2%, against 19.7% reported. That is below FY2024's 17.7% + 0.5 pt, so most of the reported FY2025 margin expansion disappears.
  - **Reversal:** $9.4M (29.6% of 31.8) was returned in May 2026. The estimated GP reversal is 9.4 x 41.1% = 3.9.
- **Source:** `income_statement.csv` rows 2, 5, 7; `revenue_quarterly.csv` rows 5 and 9; `adjusted_ebitda_reconciliation.csv` rows 7 and 11. Bill-and-hold facts from the 10-K Note 2 and 10-Q (via lead).
- **Severity:** High. It is material to the revenue quality story and to the deal model's base, and it needs revenue-recognition diligence and possibly an indemnity.
- **Confidence:** High for the revenue math. Medium for the GP and EBITDA effect, because hardware gross margin is not available.
- **Deal impact:** Valuation.
- **Cross-check:**
  - 10-K revenue recognition and critical audit matter.
  - Auditor change (the 2.3 auditor transition add-back).
  - Whether FY2024 also had bill-and-hold.
  - SEC comment letters.

#### FIN-17: Norvale's growth and share look much lower without bill-and-hold
- **Finding:** Norvale (rank 1) grew 32.3% as reported but 11.4% excluding its $24.6M of bill-and-hold. Its share of revenue goes from 31.1% to 28.0%, flat with FY2024. Norvale accounts for 77.4% of the bill-and-hold revenue (24.6/31.8).
- **Evidence:**
  - Reported growth: (156.2 - 118.1)/118.1 = 32.3%.
  - Excluding bill-and-hold: 156.2 - 24.6 = 131.6. Growth = 13.5/118.1 = 11.4%. Share = 131.6/470.5 = 28.0%, against 31.1% reported and 28.0% in FY2024.
  - Other customers' bill-and-hold = 31.8 - 24.6 = 7.2.
  - Which customer returned the $9.4M is not stated. If it was Norvale, its net bill-and-hold falls to 15.2.
- **Source:** `revenue_by_customer.csv` row 2 (FY2024 and FY2025 revenue and share), row 13 (totals); 10-K Note 2 and 10-Q (via lead).
- **Severity:** High. 28% to 31% concentration in one customer, plus a partial return of bill-and-hold goods, raises the relationship risk behind IC Q3.
- **Confidence:** High. Computed directly from the stated figures.
- **Deal impact:** Valuation and post-closing.
- **Cross-check:** The identity of the returning customer (10-Q), the Norvale contract term and renewal date, and any news on Norvale vendor diversification.

#### FIN-18: Q2 2026 revenue excluding the one-off credits
- **Finding:** Q2 2026 revenue was -4.0% year over year as reported. Adding back the $9.4M return and the $2.3M outage credits gives +6.0%, and H1 goes from -1.7% to +3.4%. Underlying trading is still positive but much slower than the 19.1% FY2025 headline.
- **Evidence:**
  - Q2 2026 reported: (112.9 - 117.6)/117.6 = -4.0%.
  - Excluding both credits: 112.9 + 9.4 + 2.3 = 124.6, so 7.0/117.6 = +6.0%.
  - Excluding the outage credits only: 115.2, so -2.0%.
  - H1: 222.6 + 11.7 = 234.3 against 226.5, so +3.4%.
  - Software alone: H1 67.5 against 58.9, so +14.6%. Hardware: 116.9 against 134.2, so -12.9%.
  - I assume the $9.4M credit reduced Q2 revenue, based on the word "credited" (via lead).
- **Source:** `revenue_quarterly.csv` rows 7 and 11; `income_statement.csv` rows 2, 3, 5 (H1 columns); 10-Q (via lead).
- **Severity:** Medium.
- **Confidence:** High for the math. Medium on how the credit was booked.
- **Deal impact:** Valuation (the run-rate base).
- **Cross-check:** The 10-Q revenue note, to confirm whether the return was booked as a revenue reversal.

#### FIN-19: Gen-3 revenue at risk from the Vantor injunction request is about 211.0 (42.0% of FY2025 revenue)
- **Finding:** If an injunction stopped Talon Gen-3 sales, about 211.0 of FY2025 revenue and about 81.8 of H1 2026 revenue would be at risk. The estimated gross profit on that revenue (86.7) is larger than FY2025 EBITDA (64.1).
- **Evidence:**
  - FY2025: 70% x 301.4 = 211.0, which is 211.0/502.3 = 42.0% of revenue. Excluding bill-and-hold: 70% x 269.6 = 188.7.
  - H1 2026: 70% x 116.9 = 81.8, assuming the 2025 mix held. That is 81.8/222.6 = 36.8% of revenue, or about 163.7 annualized.
  - Estimated GP at the 41.1% proxy margin: 211.0 x 41.1% = 86.7.
  - Hardware backlog at June 30, 2026 is 118.0. At a 70% mix, about 82.6 would be Gen-3 (assumption).
  - Software and services attached to Gen-3 units are not quantified.
- **Source:** `income_statement.csv` rows 2, 5, 7 (FY2025, H1_2026); `kpis.csv` row 6; 70% from the 10-K (via lead).
- **Severity:** Critical.
  - **Test met:** could change value by more than 10%.
  - **Number:** 42.0% of revenue and estimated GP above total EBITDA, if the injunction is granted.
- **Confidence:** Medium. The 70% is approximate, the H1 2026 mix is assumed, and the size and likelihood of any injunction, and any design-around, are for the litigation analyst.
- **Deal impact:** Valuation and closing risk. Consider a closing condition, a specific indemnity or escrow, or a reverse termination right tied to the injunction ruling.
- **Cross-check:** The court docket (injunction hearing date and scope), the 10-K legal proceedings note, and news on the case.

#### FIN-20: Restated valuation bridge. At current trading, $24.00 implies 15.1x to 20.0x, not 11.5x.
- **Finding:** At $24.00 the implied EV is 1,352.8.
  - That is 18.3x guidance-midpoint Adjusted EBITDA, 15.1x LTM Adjusted, 20.0x my LTM analyst-adjusted figure, and 17.8x covenant-capped EBITDA.
  - At the deal model's 11.5x, these bases support only $12.06 to $17.35 per share. Every case is below the $17.85 unaffected price.
  - The deal model's FY2026E Adjusted EBITDA of $118M is 37.3% above the guidance midpoint ((118 - 74)/118). Its revenue of $560M is 15.2% above the midpoint ((560 - 480)/560 = 15.2%; guidance midpoint 480).
- **Evidence:**
  - **Bridge:**
    - Equity value = 24.00 x 48.3 = 1,159.2.
    - Net debt at June 30, 2026 = 227.5 - 33.9 = 193.6.
    - EV = 1,352.8. Check against the deal brief: 1,352.8/118 = 11.5x.
  - **Analyst-adjusted LTM, case (c):**
    - Start from 89.7.
    - Subtract restructuring 9.7, which recurs every year (3.1, 4.6, 5.2, 7.9).
    - Subtract customer implementation delays 3.3, an operating cost.
    - Subtract the net bill-and-hold GP in the LTM window: (31.8 - 9.4) x 41.1% = 9.2.
    - Result: 67.5. SBC is kept as an add-back. If SBC is also deducted, the result is 49.7.

  | EBITDA basis | EBITDA | EV / EBITDA at $24.00 | EV at 11.5x | Equity (EV - 193.6) | Price per share (/48.3) |
  |---|---|---|---|---|---|
  | Deal model FY2026E (reference) | 118.0 | 11.46x | 1,357.0 | 1,163.4 | 24.09 |
  | (a) Guidance midpoint | 74.0 | 18.28x | 851.0 | 657.4 | **13.61** |
  | (a) low / high | 70.0 / 78.0 | 19.33x / 17.34x | 805.0 / 897.0 | 611.4 / 703.4 | 12.66 / 14.56 |
  | (b) LTM Adjusted (company) | 89.7 | 15.08x | 1,031.6 | 838.0 | **17.35** |
  | (c) LTM analyst-adjusted | 67.5 | 20.04x | 776.3 | 582.7 | **12.06** |
  | (d) LTM covenant-capped Consolidated EBITDA | 75.9 | 17.82x | 872.9 | 679.3 | **14.06** |

  - On the guidance midpoint, 11.5x implies a price 43.3% below $24.00 ((24.00 - 13.61)/24.00).
- **Source:** `data/deal-brief.md` lines 13 to 25; `balance_sheet.csv` rows 2, 16, 17 (Q2_2026); `adjusted_ebitda_reconciliation.csv` rows 9 to 11, 17 (LTM); guidance from the 10-Q (via lead).
- **Severity:** Critical.
  - **Test met:** value changes by more than 10%.
  - **Number:** at the model's own 11.5x, every current EBITDA basis gives 12.06 to 17.35 per share, 27.7% to 49.8% below $24.00.
- **Confidence:** High for the arithmetic. Medium for case (c), which reflects my judgment on which add-backs to exclude.
- **Deal impact:** Valuation. The deal model v3 assumptions are stale.
- **Cross-check:** Investor day materials (March 2026) against the Q2 10-Q guidance cut, and analyst consensus in news.

### Positive or mitigating points
- **June 30 compliance holds:** on my primary reading, the capped ratio at June 30, 2026 (2.67x) still complies with the 3.50x limit, with about 18.0 of EBITDA cushion (FIN-14).
- **Underlying revenue is still growing:** excluding one-off credits, Q2 2026 is +6.0% and H1 is +3.4% (FIN-18). Software revenue grew 14.6% in H1 2026, and ARR rose from 139.2 to 146.8 (`kpis.csv` row 2).
- **Cash is above the netting cap:** cash of 33.9 exceeds the 25.0 cap, so modest cash burn does not immediately raise covenant net debt.
- **Concentration is not rising:** Norvale's share excluding bill-and-hold is flat at 28.0% (FIN-17).
- **Change-of-control refinancing:** all 227.5 of debt is refinanced at closing, which cures post-closing covenant risk if closing happens before a default (FIN-15).

### Gaps and questions for management
1. Segment cost of revenue and FY2025 hardware gross margin. These are needed to firm up the bill-and-hold and Gen-3 profit estimates.
2. Quarterly EBITDA, SBC and add-backs for Q3 and Q4 2025. These drive the September 30 projection, which ranges from 2.99x to 3.33x depending on this split.
3. Q3 2026 results and the September 30, 2026 compliance certificate (capped calculation).
4. The full credit agreement: exact add-back cap wording, whether SBC is inside the cap, and which items qualify as "non-recurring".
5. Revolver commitment and availability. Only the 45.0 drawn amount is in the data.
6. Any finance leases or other debt included in Total Debt. `cash_flow.csv` row 20 shows 0.7 of finance lease payments, but there is no separate lease liability line. Also whether any cash is restricted.
7. Which customer returned the $9.4M, and whether any of the remaining $22.4M of bill-and-hold is at risk of return.
8. Whether FY2024 or earlier years included bill-and-hold revenue.
9. The H1 2026 Gen-3 share of hardware revenue, Gen-3 backlog, and design-around options.
10. The H2 2026 bridge: what drives a 47.5% step-up in Adjusted EBITDA from H1 (29.9) to the implied H2 (44.1).