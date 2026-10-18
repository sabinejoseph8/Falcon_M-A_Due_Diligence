# Iteration 2: financial-analyst report (unedited)

- Saved by the lead agent: 2026-10-18 03:54 EST
- Task: Financial follow-ups, iteration 2
- Subagent ID: ab183365bc5af614e
- The report below is the subagent's final message exactly as returned. Only the harness's hand-back line and its two-space line indent were removed.

---

## Financial analyst: findings (iteration 2)

### Files reviewed

- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md (context)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/README.md
- .../data/financials/income_statement.csv
- .../data/financials/revenue_quarterly.csv
- .../data/financials/balance_sheet.csv
- .../data/financials/cash_flow.csv
- .../data/financials/adjusted_ebitda_reconciliation.csv
- .../data/financials/revenue_by_customer.csv
- .../memory/analyst-reports/iteration-1_financial-analyst.md (my iteration 1 report, for consistency)

I did not open the SEC, news or litigation files. Every fact from those sources was given to me by the lead agent, and I label each one "(lead agent, from <file>)". None of the financial files contain instruction-like text.

---

### Answers to follow-up questions

#### 1. Covenant test (Total Net Leverage Ratio)

**Inputs** (lead agent, from 10-K Note 9 and the Q2 2026 10-Q):
- Maximum ratio: 3.50x through June 30, 2026, then 3.00x from September 30, 2026.
- Unrestricted cash is netted only up to 25.0.
- Permitted Add-backs are capped at 15% of Consolidated EBITDA before those add-backs.

**Covenant net debt** = total debt less min(cash, 25.0). Source: `balance_sheet.csv`, lines 2, 16 and 17.
- Dec 31, 2025: (35.0 + 185.0) - min(41.6, 25.0) = 220.0 - 25.0 = **195.0**
- Jun 30, 2026: (45.0 + 182.5) - min(33.9, 25.0) = 227.5 - 25.0 = **202.5**
- Including the 4.2 of letters of credit (LCs) at June 30, 2026: 206.7. The Dec 31, 2025 LC balance is not in the pack.
- **Letters of credit:** I exclude them in the base case. The back-solve below shows the company also excludes them.

**EBITDA components.** Source: `adjusted_ebitda_reconciliation.csv`, lines 7 to 11.

| | FY2025 | LTM Q2 2026 |
|---|---|---|
| EBITDA | 64.1 | 48.2 |
| SBC | 17.2 | 17.8 |
| Restructuring + other non-recurring | 7.9 + 9.6 = 17.5 | 9.7 + 14.0 = 23.7 |
| Company Adjusted EBITDA | 98.8 | 89.7 |

**Covenant EBITDA in each case:**
- **(a) Full company Adjusted EBITDA, no cap:** 98.8 and 89.7.
- **(b) Cap applies, SBC is in the base:**
  - FY2025: base 64.1 + 17.2 = 81.3. Cap 15% x 81.3 = 12.2, which is below the actual 17.5, so the cap binds. Covenant EBITDA = 81.3 + 12.2 = **93.5**.
  - LTM: base 48.2 + 17.8 = 66.0. Cap 9.9, below the actual 23.7. Covenant EBITDA = **75.9**.
- **(c) Cap applies, SBC is itself a Permitted Add-back:**
  - FY2025: base 64.1. Cap 9.6, below the actual 34.7. Covenant EBITDA = **73.7**.
  - LTM: base 48.2. Cap 7.2, below the actual 41.5. Covenant EBITDA = **55.4**.

| Ratio | Dec 31, 2025 (limit 3.50x) | Jun 30, 2026 (limit 3.50x) | Jun 30, 2026 incl. LCs |
|---|---|---|---|
| (a) | 195.0 / 98.8 = **1.97x** | 202.5 / 89.7 = **2.26x** | 206.7 / 89.7 = 2.30x |
| (b) | 195.0 / 93.5 = **2.09x** | 202.5 / 75.9 = **2.67x** | 206.7 / 75.9 = 2.72x |
| (c) | 195.0 / 73.7 = **2.65x** | 202.5 / 55.4 = **3.65x, a breach** | 206.7 / 55.4 = 3.73x |

Under (c), compliance at June 30 needed EBITDA of 202.5 / 3.50 = 57.9. That is 2.4 more than 55.4. Put the other way, the maximum net debt was 3.50 x 55.4 = 194.0, against 202.5 actual.

**Back-solve of the reported 2.26x:**
- Implied EBITDA = 202.5 / 2.26 = **89.6**. The rounding band (2.255x to 2.265x) gives 89.4 to 89.8.
- This matches **case (a)** only: full company Adjusted EBITDA of 89.7, cash capped at 25.0, LCs excluded.
- Other combinations do not match:
  - Including LCs: 206.7 / 89.7 = 2.30x.
  - Netting all cash: 193.6 / 89.7 = 2.16x.
  - Case (b) gives 2.67x and case (c) gives 3.65x.
- **Conclusion:** the reported 2.26x appears to apply no 15% cap at all. Restructuring and other add-backs of 23.7 are more than double the largest possible cap of 9.9.

**Projection assumptions** (all mine):
- Company Adjusted EBITDA in H2 2026:
  - (i) guidance midpoint: 74.0 - 29.9 = 44.1
  - (ii) guidance low end: 70.0 - 29.9 = 40.1
  - (iii) H2 equal to H1: 29.9
- H2 2026 add-backs equal H1 2026: SBC 8.9; restructuring + other 4.4 + 6.2 = 10.6. So H2 EBITDA is 24.6, 20.6 and 10.4.
- Q3 2026 is half of H2 2026. If the guidance is weighted to Q4, September looks worse than shown.
- Q3 2025 is taken as H2 2025 times the Q3 revenue share, 121.4 / 275.8 = 44.0%:
  - H2 2025 = FY2025 - H1 2025: EBITDA 37.8, SBC 8.9, other add-backs 13.1, Adjusted EBITDA 59.8.
  - Q3 2025: EBITDA 16.6, SBC 3.9, other 5.8, Adjusted EBITDA 26.3.
- Guidance Adjusted EBITDA is assumed to use the company definition.
- **Net debt:** H2 2026 burn repeats H1, a reported net debt increase of 15.2 (7.6 a quarter). Term loan amortization is 1.25 a quarter.
  - Sep 30: cash 33.9 - 7.6 - 1.25 = 25.05 and debt 226.25. Covenant net debt = **201.2**.
  - Dec 31: cash would fall to 16.2, so a revolver draw of 8.8 restores it to 25.0. Revolver 53.8, total debt 233.8, covenant net debt = **208.8**. Revolver availability falls from 25.8 to 17.0.
- EBITDA needed at 3.00x: Sep 30, 201.2 / 3 = **67.1**. Dec 31, 208.8 / 3 = **69.6**.

**September 30, 2026** (LTM = LTM Q2 2026 - Q3 2025 + Q3 2026):

| Scenario | (a) EBITDA / ratio / headroom | (b) EBITDA / ratio / headroom | (c) EBITDA / ratio / headroom |
|---|---|---|---|
| (i) midpoint | 85.4 / 2.36x / +18.4 | (43.9 + 18.3) x 1.15 = 71.5 / 2.81x / +4.5 | 43.9 x 1.15 = 50.4 / 3.99x / -16.6 |
| (ii) low end | 83.4 / 2.41x / +16.4 | 60.2 x 1.15 = 69.2 / 2.91x / +2.2 | 41.9 x 1.15 = 48.1 / 4.18x / -18.9 |
| (iii) H2 = H1 | 78.3 / 2.57x / +11.3 | 55.1 x 1.15 = 63.4 / 3.18x / **-3.7** | 36.8 x 1.15 = 42.3 / 4.76x / -24.8 |

How the LTM inputs are built, scenario (i):
- Company Adjusted EBITDA = 89.7 - 26.3 + 22.1 = 85.4
- EBITDA = 48.2 - 16.6 + 12.3 = 43.9
- SBC = 17.8 - 3.9 + 4.45 = 18.3

**December 31, 2026** (FY2026; full-year add-backs SBC 17.8 and other 21.2):

| Scenario | (a) EBITDA / ratio / headroom | (b) EBITDA / ratio / headroom | (c) EBITDA / ratio / headroom |
|---|---|---|---|
| (i) midpoint | 74.0 / 2.82x / +4.4 | (35.0 + 17.8) x 1.15 = 60.7 / 3.44x / -8.9 | 35.0 x 1.15 = 40.3 / 5.19x / -29.4 |
| (ii) low end | 70.0 / 2.98x / +0.4 | 48.8 x 1.15 = 56.1 / 3.72x / -13.5 | 31.0 x 1.15 = 35.7 / 5.86x / -34.0 |
| (iii) H2 = H1 | 59.8 / **3.49x** / -9.8 | 38.6 x 1.15 = 44.4 / 4.70x / -25.2 | 20.8 x 1.15 = 23.9 / 8.73x / -45.7 |

**Sensitivity:** if net debt stays flat at 202.5, the EBITDA needed at Dec 31 is 67.5. The headroom becomes:
- (a)(ii) +2.5
- (a)(iii) -7.7
- (b)(i) -6.8
- (b)(ii) -11.4

So the conclusion does not depend on the burn assumption.

**Bottom line:**
- On the company's own uncapped basis, the Dec 31, 2026 headroom is 4.4 at the guidance midpoint, 0.4 at the low end, and a breach if H2 repeats H1.
- With the 15% cap, every guidance case breaches 3.00x at Dec 31, 2026.
- Case (c) is already in breach at June 30, 2026.
- The September 30, 2026 compliance result will probably be reported around the IC date. Confirm when the Q3 10-Q is filed.

#### 2. Restated revenue (bill-and-hold removed)

Inputs: 31.8 recognized in Q4 2025, 22.4 delivered by June 30, 2026, and 9.4 returned and booked as a Q2 2026 reduction (lead agent, from 10-K Note 2 and the Q2 2026 10-Q). Check: 22.4 + 9.4 = 31.8.

| | Reported | Restated | Underlying (bill-and-hold excluded entirely) |
|---|---|---|---|
| Q4 2025 | 154.4 (+32.4%) | 154.4 - 31.8 = **122.6** (122.6 / 116.6 = **+5.1%**) | 122.6 |
| FY2025 | 502.3 (+19.1%) | **470.5** (470.5 / 421.7 = **+11.6%**) | 470.5 |
| FY2025 hardware | 301.4 (+15.1%) | 269.6 (269.6 / 261.9 = **+2.9%**) | 269.6 |
| H1 2026 | 222.6 (-1.7%) | 222.6 + 22.4 + 9.4 = **254.4** (+12.3%, timing only) | 222.6 + 9.4 = 232.0 (**+2.4%**) |
| H1 2026 hardware | 116.9 (-12.9%) | 148.7 (+10.8%) | 126.3 (-5.9%) |
| LTM Q2 2026 | 498.4 (+11.0% vs 449.2) | 121.4 + 122.6 + 254.4 = **498.4** (+11.0%) | 498.4 - 22.4 = 476.0 (**+6.0%**) |

- **LTM is unchanged.** The net effect is -31.8 + 22.4 + 9.4 = 0. Reported LTM already contains the 22.4 net.
- **Quarterly growth without bill-and-hold:** Q1 2025 13.2%; Q2 2025 14.4%; Q3 2025 14.4%; **Q4 2025 5.1%**; Q1 2026 0.7%; **Q2 2026 4.0%** (112.9 + 9.4 = 122.3, against 117.6).
- The pack does not show which quarter the 22.4 was delivered in, so I left it out of the quarterly rates.
- **Q4 to Q3 uplift:** 122.6 / 121.4 - 1 = +1.0% in 2025, against +9.9% in 2024.
- **Q2 2026 without the 9.4 return and the 2.3 service credits:** 112.9 + 9.4 + 2.3 = **124.6**, up 124.6 / 117.6 - 1 = **6.0%**.
  - H1 2026 on the same basis: 234.3, up 3.4%.
  - This assumes the 2.3 of credits was booked as a revenue reduction (lead agent, from the Q2 2026 10-Q).
- **Against consensus** (lead agent, from the March 10, 2026 Capital Markets Wire article):
  - Restated Q4 2025 of 122.6 vs 128.0 consensus is a **miss of 5.4, or 4.2%**.
  - Reported 154.4 was a beat of 26.4, or 20.6%.
- **Norvale:**
  - FY2025 revenue without its 24.6: 156.2 - 24.6 = **131.6**.
  - Share: 131.6 / 470.5 = **28.0%**, against 31.1% reported and 28.0% in FY2024.
  - Growth: 131.6 / 118.1 - 1 = **11.4%**, against 32.3% reported.
  - Norvale delivered 13.5 / 48.8 = 27.7% of restated growth.
  - Revenue excluding Norvale: 470.5 - 131.6 = 338.9, up 338.9 / 303.6 - 1 = 11.6%. The other 7.2 of bill-and-hold (31.8 - 24.6) came from non-Norvale customers.
  - Restated top 10 share: 58.9% to 60.4%. The range depends on whether that 7.2 sat with a top 10 customer: (308.8 - 24.6 - 7.2) / 470.5, or (308.8 - 24.6) / 470.5.

#### 3. Bonus test (2025 plan; lead agent, from DEF 14A)

- **Margin assumption:** the bill-and-hold units earned the FY2025 company gross margin of 206.3 / 502.3 = 41.1%. I assume no offsetting variable operating costs.
- Gross profit removed = 31.8 x 41.07% = **13.1**.
- Restated Adjusted EBITDA = 98.8 - 13.1 = **85.7**.

| Metric | Threshold / Target | Reported | vs threshold / target | Restated | vs threshold / target |
|---|---|---|---|---|---|
| Revenue | 470.0 / 490.0 | 502.3 | +32.3 / +12.3 | 470.5 | **+0.5 / -19.5** |
| Adjusted EBITDA | 88.0 / 95.0 | 98.8 | +10.8 / +3.8 | 85.7 | **-2.3 / -9.3** |

- **Break-even margin:** EBITDA still clears the threshold only if the bill-and-hold margin was below (98.8 - 88.0) / 31.8 = **34.0%**.
- Hardware gross margin is not disclosed, and hardware is likely below the 41.1% blended margin. So the EBITDA miss is likely but not certain.
- If the 4.1 "customer implementation delays" add-back is also removed, restated EBITDA is 81.6.
- **Conclusion:** bill-and-hold moved revenue from barely at threshold to above target. At the blended margin, it also moved EBITDA from below threshold to above target. The plan paid 142% of target.
- The bonus pool size and payout curve are not in the pack, so I cannot quantify the excess payout.

#### 4. EV bridge and value range

| Item | US$ m | Status |
|---|---|---|
| Equity value (24.00 x 48.3) | 1,159.2 | |
| + Total debt, Jun 30, 2026 | 227.5 | balance_sheet.csv, lines 16 and 17 |
| - Cash | (33.9) | |
| **= Brief EV** | **1,352.8** | |
| + Change-of-control cash severance (double trigger, assumed all paid) | 9.6 | DEF 14A via lead agent |
| + Change-of-control other | 1.4 | DEF 14A via lead agent |
| + Ruiz settlement, if unpaid at closing | 3.2 | 10-K via lead agent; payment status unknown |
| + Letters of credit (contingent, included conservatively) | 4.2 | Q2 10-Q via lead agent |
| **= Adjusted EV, known items** | **1,371.2** | |
| Possible: single-trigger equity acceleration, if not already in the 48.3 | +17.6 | |
| Possible: Pinecrest (contract cap to claim) | +1.4 to +12.0 | litigation via lead agent |
| Possible: Vantor (expert to claim) | +96.4 to +140.0 | litigation via lead agent |
| Possible: cash burn to Dec 31, 2026 | +15.2 | my FIN-09 projection |

- **Unknown items:**
  - finance lease balance (0.7 paid in H1 2026)
  - restructuring accrual
  - transaction fees
  - accrued 2026 bonuses
  - debt breakage or refinancing fees (change of control is an event of default)
  - tax exposures
  - any working capital shortfall against the peg
- **Offer multiples on the adjusted EV of 1,371.2:**
  - Guidance midpoint (74.0): 1,371.2 / 74.0 = **18.5x**
  - Low end (70.0): 19.6x
  - LTM company Adjusted EBITDA (89.7): 15.3x
  - LTM analyst-adjusted EBITDA (72.6): 18.9x
- To justify US$24.00 at 11.5x, EBITDA would need to be 1,371.2 / 11.5 = **119.2**.

**Value per share.** Formula: (multiple x EBITDA - 212.0) / 48.3, where 212.0 = net debt 193.6 + known debt-like items 18.4.

| EBITDA base | 10.0x | 11.5x | 13.0x |
|---|---|---|---|
| (i) Guidance midpoint, 74.0 | (740.0 - 212.0) / 48.3 = **US$10.93** | 639.0 / 48.3 = **US$13.23** | 750.0 / 48.3 = **US$15.53** |
| (ii) LTM company Adjusted EBITDA, 89.7 | 685.0 / 48.3 = **US$14.18** | 819.6 / 48.3 = **US$16.97** | 954.1 / 48.3 = **US$19.75** |
| (iii) LTM analyst-adjusted EBITDA, 72.6 | 514.0 / 48.3 = **US$10.64** | 622.9 / 48.3 = **US$12.90** | 731.8 / 48.3 = **US$15.15** |

No cell reaches US$24.00. The highest, US$19.75, is 17.7% below the offer.

**Losing Norvale** (base: restated FY2025 revenue of 131.6):

| Margin assumption | Lost EBITDA | At 10.0x | At 11.5x | At 13.0x |
|---|---|---|---|---|
| FY2025 gross margin 41.1% (no cost savings) | 131.6 x 41.07% = 54.1 | -US$11.20 | -US$12.88 | -US$14.56 |
| FY2025 Adjusted EBITDA margin 19.7% (costs flex with volume) | 131.6 x 19.67% = 25.9 | -US$5.36 | -US$6.17 | -US$6.97 |

- At 11.5x on the guidance midpoint, the gross margin case leaves about US$13.23 - US$12.88 = US$0.35 per share.
- The pack has no H1 2026 Norvale revenue.

**Vantor payment:**
- 96.4 / 48.3 = **-US$2.00 per share** (8.3% of the offer).
- 140.0 / 48.3 = **-US$2.90 per share** (12.1% of the offer).
- These are pre-tax, before any tax deduction, and before any running royalty.

#### 5. Vantor royalty base (Gen-3 at about 70% of hardware; lead agent, from 10-K Item 1)

| Period | Hardware revenue | Gen-3 estimate (x 70%) |
|---|---|---|
| FY2025 reported | 301.4 | **211.0** |
| FY2025 restated (bill-and-hold removed) | 269.6 | 188.7 |
| H1 2026 reported | 116.9 | **81.8** |
| H1 2026 restated (with 22.4 delivered and 9.4 credit removed) | 148.7 | 104.1 |
| LTM Q2 2026 (301.4 - 134.2 + 116.9) | 284.1 | **198.9** (same on both bases) |

- Applying the FY2025 mix of 70% to H1 2026 is my assumption.
- **Royalty cost per point of rate:** each 1% royalty on LTM Gen-3 costs 2.0 of EBITDA a year. At 11.5x that is 23.0 of EV, or US$0.47 per share.
- **Size of the expert figure:** 96.4 equals 48.5% of one year's Gen-3 revenue, and 32.9% of FY2025 plus H1 2026 Gen-3 revenue (211.0 + 81.8 = 292.8). That points to a long damages period, a base wider than Gen-3, or a high rate. The litigation workstream should confirm which.

---

### Findings

#### FIN-17: The reported 2.26x leverage ratio appears to ignore the 15% add-back cap. On a capped basis, a covenant breach is likely by December 31, 2026 and possible already
- **Finding:** The reported 2.26x can only be reproduced with full company Adjusted EBITDA of 89.7 and no cap. With the cap, the June 30, 2026 ratio is 2.67x, or 3.65x if SBC is a Permitted Add-back. The 3.65x is above the 3.50x limit. At December 31, 2026 the capped ratio exceeds 3.00x in every guidance case. Even uncapped, the low-end case has only 0.4 of headroom.
- **Evidence:** See Answer 1. Back-solve: 202.5 / 2.26 = 89.6, against 89.7. Capped EBITDA is 75.9 or 55.4. Actual add-backs of 23.7 (or 41.5 with SBC) against a cap of 9.9 (or 7.2). Dec 31, 2026 ratios at the guidance midpoint: (a) 2.82x, (b) 3.44x, (c) 5.19x.
- **Source:**
  - `data/financials/adjusted_ebitda_reconciliation.csv`, lines 7 to 11
  - `data/financials/balance_sheet.csv`, lines 2, 16 and 17
  - Covenant terms, reported ratio and guidance (lead agent, from `data/sec-filings/TLFS_10-K_FY2025_excerpts.md` Note 9 and `TLFS_10-Q_Q2-2026_excerpts.md`)
- **Severity:** Critical. A pre-closing default would give lenders acceleration rights, with only 25.8 of revolver availability. It may also mean misstated compliance disclosure.
- **Confidence:** High for the June 30 math and the back-solve. Medium for the conclusion, because the cap wording is summarized second-hand, SBC treatment is pending, and the projections rest on my assumptions.
- **Deal impact:** Closing risk (default or waiver before closing, MAE arguments), financing (the facility must be refinanced at closing anyway because change of control is a default), disclosure and governance.
- **Cross-check:**
  - The full credit agreement definitions of Consolidated EBITDA, Permitted Add-backs and Indebtedness (whether LCs count).
  - The compliance certificates.
  - Any amendment or waiver 8-K (Items 1.01 and 2.04).
  - The Q3 2026 10-Q covenant disclosure.
  - News on lender talks.

#### FIN-18: Without bill-and-hold, FY2025 growth was 11.6%, hardware grew 2.9%, and Q4 2025 missed consensus
- **Finding:** Removing the 31.8 cuts FY2025 growth from 19.1% to 11.6% and Q4 2025 growth from 32.4% to 5.1%. Q4 2025 would have missed consensus by 5.4. Hardware growth falls from 15.1% to 2.9%. Underlying LTM growth, excluding the bill-and-hold units entirely, is 6.0%.
- **Evidence:** See Answer 2. 470.5 / 421.7 = 1.116; 122.6 / 116.6 = 1.051; 122.6 vs 128.0; 269.6 / 261.9 = 1.029; 476.0 / 449.2 = 1.060.
- **Source:**
  - `data/financials/revenue_quarterly.csv`, lines 2 to 11
  - `data/financials/income_statement.csv`, lines 2 and 5
  - Bill-and-hold amounts (lead agent, from the 10-K Note 2 and Q2 2026 10-Q)
  - Consensus (lead agent, from the news file)
- **Severity:** High. It feeds Critical findings FIN-01 and FIN-14.
- **Confidence:** High for the arithmetic. I assume FY2024 and H1 2025 contained no bill-and-hold revenue. That is unverified.
- **Deal impact:** Valuation (growth base), closing risk (revenue recognition, restatement) and post-closing.
- **Cross-check:**
  - Whether bill-and-hold also occurred in FY2024.
  - Whether the bill-and-hold criteria were met (customer request, fixed delivery schedule, units segregated).
  - Auditor critical audit matters.
  - Any SEC comment letter or securities suit about the Q4 2025 beat.
- **Changes earlier findings:**
  - **FIN-01:** the actual one-off was 31.8, not my estimated 21.4. Normalized FY2025 growth is 11.6%, not 14.0%. FIN-01 stays Critical with these revised numbers.
  - **FIN-11:** Norvale's underlying growth was 11.4% and its share 28.0%. All of the rise in concentration came from bill-and-hold. The level of concentration is still High.
  - **FIN-06:** if the bill-and-hold amount sat in receivables, FY2025 DSO excluding it is (118.9 - 31.8) / 470.5 x 365 = 67.6 days, against 86.4. This is illustrative, because the split between receivables and contract assets is unknown.
  - **FIN-07:** the 9.4 return probably came back into inventory at about 9.4 x (1 - 41.1%) = 5.5. That may explain part of the 12.7 H1 2026 inventory build.

#### FIN-19: Bill-and-hold lifted 2025 results over the bonus thresholds and targets
- **Finding:** Without bill-and-hold, FY2025 revenue of 470.5 only just clears the 470.0 threshold. Adjusted EBITDA of 85.7 misses the 88.0 threshold. The plan paid 142% of target.
- **Evidence:** See Answer 3. 98.8 - 31.8 x 41.07% = 85.7. The EBITDA threshold is cleared only if the bill-and-hold margin was below 34.0%.
- **Source:**
  - `data/financials/income_statement.csv`, lines 5 and 7
  - `data/financials/adjusted_ebitda_reconciliation.csv`, line 11
  - Bonus metrics (lead agent, from `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`)
- **Severity:** High. Governance and incentive integrity (IC question 5). It may require a clawback review and specific representations.
- **Confidence:** Medium. It depends on the margin assumption and on the plan's exact EBITDA definition.
- **Deal impact:** Governance, indemnity and R&W scope, retention and change-of-control design for management.
- **Cross-check:**
  - The plan's metric definitions and payout curve.
  - The compensation committee minutes.
  - The clawback policy (Dodd-Frank Rule 10D-1 applies if there is a restatement).
  - Form 4 insider sales after the Q4 2025 results.

#### FIN-20: On current earnings, fair value is US$10.64 to US$19.75 per share against a US$24.00 offer
- **Finding:** Adjusted EV including known debt-like items is 1,371.2. That is 18.5x the revised guidance midpoint and needs 119.2 of EBITDA to justify 11.5x. The 3 x 3 value grid gives US$10.64 to US$19.75. Losing Norvale would cost US$6.17 to US$12.88 per share at 11.5x.
- **Evidence:** See Answer 4.
- **Source:**
  - `data/deal-brief.md`
  - `data/financials/balance_sheet.csv`, lines 2, 16 and 17
  - `data/financials/adjusted_ebitda_reconciliation.csv`, line 11
  - `data/financials/revenue_by_customer.csv`, line 2
  - Debt-like items and guidance from the lead agent, as cited in Answer 4
- **Severity:** Critical. The value gap is more than 10% in every case.
- **Confidence:** High for the math. Medium for the scenarios.
- **Deal impact:** Valuation and price, and the IC decision.
- **Cross-check:**
  - Q3 2026 results.
  - Current analyst consensus.
  - Fully diluted shares at US$24.00, including the single-trigger 17.6.
  - Ruiz payment status.
  - The finance lease balance.
- **Changes FIN-14:**
  - The management case is now officially withdrawn. The brief's EV of 1,352.8 is 18.3x the guidance midpoint (1,352.8 / 74.0), not 11.5x.
  - FIN-14's US$17.35 per share (11.5x LTM) becomes US$16.97 once the debt-like items are included.

#### FIN-21: A Vantor payment would exceed Talonfield's available liquidity
- **Finding:**
  - A payment of 96.4 to 140.0 compares with June 30, 2026 liquidity of 33.9 cash + 25.8 revolver availability = 59.7. The shortfall would be 36.7 to 80.3.
  - The payment is worth US$2.00 to US$2.90 per share.
  - Each 1% running royalty on Gen-3 would cost about 2.0 of EBITDA a year, or US$0.47 per share at 11.5x.
- **Evidence:** See Answers 4 and 5. 96.4 / 48.3 = 2.00; 140.0 / 48.3 = 2.90; 198.9 x 1% = 2.0.
- **Source:**
  - `data/financials/balance_sheet.csv`, line 2
  - `data/financials/income_statement.csv`, line 2
  - Claim amounts (lead agent, from `data/litigation/`)
  - Revolver availability and Gen-3 share (lead agent, from the SEC filings)
- **Severity:** High. It needs a specific indemnity, escrow or price adjustment.
- **Confidence:** High for the arithmetic. Medium for the royalty base, because it assumes Gen-3 was 70% of hardware in H1 2026.
- **Deal impact:** Valuation, financing and post-closing.
- **Cross-check:**
  - The Vantor docket: damages period, royalty base and rate, injunction request and trial date.
  - Any ASC 450 accrual or disclosure in the 10-Q.

---

**Debt-like items and the Norvale sensitivity** are covered in FIN-20 and Answer 4 rather than as separate cards.

**Positive or mitigating:**
- LTM revenue is unchanged by the restatement (498.4).
- H1 2026 company Adjusted EBITDA excluding the 9.4 return and the 2.3 credits would be 29.9 + 9.4 x 41.07% + 2.3 = 36.1. That assumes the return reversed revenue at the blended margin.

**New questions for management:**
- The quarterly split of the 22.4 delivered in H1 2026.
- Whether any FY2024 revenue was bill-and-hold.
- Gross margin on the bill-and-hold units.
- The covenant compliance certificates for Q4 2025 to Q2 2026, and the add-back calculation behind 2.26x.
- The Q3 2026 covenant result.
- The finance lease balance and the Ruiz payment status.
- Whether the 48.3 diluted shares include the single-trigger awards.
- H1 2026 Norvale revenue.
- The Gen-3 launch date and Gen-3 revenue by period.
