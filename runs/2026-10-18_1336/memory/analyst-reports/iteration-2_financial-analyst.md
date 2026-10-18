# Iteration 2: financial-analyst (full report, unedited)

## Financial analyst: findings (iteration 2, narrow follow-up)

### Files reviewed
- `data/deal-brief.md` (price, shares, deal model v3 assumptions)
- `data/financials/income_statement.csv`
- `data/financials/revenue_quarterly.csv`
- `data/financials/adjusted_ebitda_reconciliation.csv`
- `data/financials/balance_sheet.csv`
- `data/financials/cash_flow.csv`
- `data/financials/kpis.csv`
- `data/financials/revenue_by_customer.csv`
- `data/financials/README.md` (no quality of earnings report received yet)

The lead agent supplied these facts, and I used them as given: the bill-and-hold amounts ($31.8M in Q4 2025, of which Norvale $24.6M), the May 2026 reversal of $9.4M, the $22.4M delivered by June 30, 2026, the $2.3M of SLA credits, and FY2026 guidance (from the 10-K FY2025 Note 2 and the 10-Q Q2 2026). I also used the covenant terms from 10-K Note 9, as summarized by the SEC analyst. That text is still being re-checked, so every covenant result below depends on it.

No file content tried to give instructions.

I did not read the iteration-1 reports because they are outside my scope. Below, "confirms / corrects / adds to" refers to iteration-1 topics. The lead should map each one to the register IDs.

### Key metrics table (updated, US$M)

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 / LTM Q2 2026 |
|---|---|---|---|---|
| Total revenue, reported | 368.9 | 421.7 | 502.3 | H1 222.6 |
| Revenue growth, reported | n/a | 14.3% | 19.1% | H1 -1.7% |
| Revenue ex bill-and-hold (B&H) (FY25 -31.8; H1 26 +9.4) | 368.9 | 421.7 | 470.5 | H1 232.0 |
| Growth ex B&H | n/a | 14.3% | 11.6% | H1 +2.4% (+3.4% with SLA add-back) |
| Hardware revenue, reported / ex B&H | 236.0 | 261.9 | 301.4 / 269.6 | H1 116.9 / 126.3 |
| Hardware growth, reported / ex B&H | n/a | 11.0% | 15.1% / 2.9% | H1 -12.9% / -5.9% |
| Gross margin, reported | 40.1% | 40.8% | 41.1% | H1 38.0% |
| Adj. EBITDA, reported (company) | 60.4 | 74.8 | 98.8 | H1 29.9 / LTM 89.7 |
| Adj. EBITDA ex B&H (at 41.1% GM) | 60.4 | 74.8 | 85.7 | H1 33.8 (36.1 with SLA) / LTM 80.5 |
| Adj. EBITDA margin ex B&H | 16.4% | 17.7% | 18.2% | H1 14.6% |
| Hardware revenue per robot shipped ($000) | 78.1 | 79.4 | 70.1 (62.7 ex B&H) | H1 71.3 (77.0 adj.) |
| Covenant net debt (cash netting capped at $25.0M) | n/a | n/a | n/a | 202.5 |
| EV / normalized run-rate EBITDA (80.5) | n/a | n/a | n/a | 16.8x (deal model 11.5x) |

The FY2024 growth figure is 421.7 / 368.9 - 1 = 14.3%.

### Findings

#### FIN-15: Bill-and-hold accounts for about 40% of FY2025 growth and 84% of Q4 2025 growth; underlying hardware growth is 2.9%
- **Finding:** Without the $31.8M of Q4 2025 bill-and-hold, FY2025 growth falls from 19.1% to 11.6%, Q4 2025 growth falls from 32.4% to 5.1%, and FY2025 hardware growth falls from 15.1% to 2.9%. This confirms and quantifies the iteration-1 finding that the Q4 2025 spike breaks the trend.
- **Evidence:**
  - FY2025 reported growth: (502.3 - 421.7) / 421.7 = 80.6 / 421.7 = 19.1%.
  - FY2025 ex B&H: 502.3 - 31.8 = 470.5. Growth = 48.8 / 421.7 = 11.6%.
  - Share of FY2025 growth that is B&H: 31.8 / 80.6 = 39.5%.
  - Q4 2025 reported growth: (154.4 - 116.6) / 116.6 = 37.8 / 116.6 = 32.4%.
  - Q4 2025 ex B&H: 154.4 - 31.8 = 122.6. Growth = 6.0 / 116.6 = 5.1%, and only +1.0% over Q3 2025 (122.6 / 121.4). Q3 2025 grew 14.4% (121.4 / 106.1).
  - Share of Q4 growth that is B&H: 31.8 / 37.8 = 84.1%.
  - FY2025 hardware reported growth: (301.4 - 261.9) / 261.9 = 39.5 / 261.9 = 15.1%.
  - FY2025 hardware ex B&H: 301.4 - 31.8 = 269.6. Growth = 7.7 / 261.9 = 2.9%.
  - Other segments had no B&H: software (FieldOS) grew 27.4 / 101.2 = 27.1% and services grew 13.7 / 58.6 = 23.4%.
- **Source:** `revenue_quarterly.csv` rows Q3 2024, Q4 2024, Q3 2025, Q4 2025; `income_statement.csv` rows "Revenue: Hardware", "Revenue: Software (FieldOS)", "Revenue: Services", "Total revenue" (FY2024, FY2025); B&H amount from 10-K Note 2 (via the lead).
- **Severity:** Critical. Hardware is 60% of revenue (301.4 / 502.3), and the growth story behind the $560M FY2026E collapses to low single digits in hardware.
- **Confidence:** High. The B&H amount comes from a primary filing and every step is recomputed.
- **Deal impact:** Valuation.
- **Cross-check:** Revenue recognition policy and B&H criteria in 10-K Note 2. Auditor communications (the auditor changed in FY2025). Any SEC comment letters. News on Norvale orders and the investor-day guidance.

#### FIN-16: H1 2026 underlying growth is +2.4% to +3.4%, and hardware is still declining
- **Finding:** H1 2026 is -1.7% as reported. Adding back the $9.4M reversal gives +2.4%. Also adding back the $2.3M of SLA credits gives +3.4%. Hardware is -5.9% even after the add-back. This adds to iteration-1 by quantifying the normalized H1 2026.
- **Evidence:**
  - Q2 2026 reported: (112.9 - 117.6) / 117.6 = -4.0%.
  - Q2 2026 plus 9.4 = 122.3: 4.7 / 117.6 = +4.0%.
  - Q2 2026 plus 2.3 more = 124.6: 7.0 / 117.6 = +6.0%.
  - Q1 2026: 109.7 / 108.9 = +0.7%.
  - H1 2026 reported: (222.6 - 226.5) / 226.5 = -1.7%.
  - H1 2026 plus 9.4 = 232.0: 5.5 / 226.5 = +2.4%.
  - H1 2026 plus 9.4 plus 2.3 = 234.3: 7.8 / 226.5 = +3.4%.
  - H1 hardware reported: (116.9 - 134.2) / 134.2 = -12.9%.
  - H1 hardware plus 9.4 = 126.3: -7.9 / 134.2 = -5.9%. I assume the SLA credits sit in software or services, not hardware; the filing does not say which.
  - Sensitivity (my construction, not requested): on a delivery basis, the $22.4M delivered by June 30, 2026 would be H1 2026 revenue. That gives H1 2026 = 232.0 + 22.4 = 254.4 (+12.3%) and hardware 148.7 (+10.8%). This moves the same revenue between periods; it is not new demand. Note that 31.8 - 9.4 = 22.4, so every B&H dollar was either delivered or returned.
  - Guidance check: FY2026 revenue of 470 to 490 implies H2 2026 of 247.4 to 267.4. Against H2 2025 ex B&H of 244.0 (275.8 - 31.8), that is +1.4% to +9.6%.
- **Source:** `revenue_quarterly.csv` rows Q1 2025, Q2 2025, Q1 2026, Q2 2026; `income_statement.csv` columns H1_2025, H1_2026; 10-Q Q2 2026 facts (via the lead).
- **Severity:** High.
- **Confidence:** High for the requested views. Medium for the segment allocation of the SLA credits.
- **Deal impact:** Valuation.
- **Cross-check:** The 10-Q segment note (which line took the $9.4M and the $2.3M). News on the April outage and on customer churn.

#### FIN-17: Inference: the 2025 robots-shipped KPI probably counts the undelivered bill-and-hold units, and the installed base includes robots still in Talonfield warehouses
- **Finding:** This is an inference, not a disclosed fact. Unit growth of +30.3% does not fit underlying hardware revenue growth of +2.9%. The installed base also rolls forward by exactly the shipment count. The most likely explanation is that roughly 400 B&H robots were counted as "shipped" and "installed" at December 31, 2025. This adds to iteration-1.
- **Evidence:**
  - Hardware revenue per robot: FY2023 236.0 / 3,020 = $78.1k; FY2024 261.9 / 3,300 = $79.4k; FY2025 301.4 / 4,300 = $70.1k, which is -11.7% year over year.
  - If the 4,300 excluded the B&H units, the revenue tied to physically shipped units would be 269.6 / 4,300 = $62.7k per robot. That is a 21% price drop with no disclosed explanation, which is less plausible. A count that includes the B&H units fits better.
  - Implied B&H units at the FY2024 price: 31.8 / 0.0794 = about 400 robots. Physical shipments would then be about 3,900, growth of 18.2% (3,900 / 3,300). The leftover price decline cannot be fully explained, and quarterly unit data would resolve it.
  - Installed-base roll-forward: 13,100 + 4,300 = 17,400 (FY2025 exact); 17,400 + 1,640 = 19,040 (H1 2026 exact); 9,800 + 3,300 = 13,100 (FY2024 exact). There are no retirements, so units go into the installed base when "shipped". The 10-K says the B&H products were still in Talonfield warehouses at year-end.
  - H1 2026 check: adjusted hardware 126.3 / 1,640 = $77.0k, close to FY2024's $79.4k. This suggests the 2026 count is on a normal basis, and that the 22.4M delivered in 2026 was not counted again.
  - Backlog: FY2025 implied hardware bookings = 301.4 + (131.0 - 168.0) = 264.4, against FY2024 261.9 + (168.0 - 142.0) = 287.9. That is -8.2%, so demand fell while units "rose" 30%.
- **Source:** `kpis.csv` rows "Robots shipped in period", "Installed base of robots", "Hardware order backlog"; `income_statement.csv` row "Revenue: Hardware".
- **Severity:** Medium. It goes to the reliability of KPIs and disclosure controls (IC question 5).
- **Confidence:** Low to Medium. The conclusion is inferred, there are no quarterly unit counts, and hardware revenue may include non-robot items.
- **Deal impact:** Valuation (KPI reliability) and post-closing (controls).
- **Cross-check:** The KPI definitions in the 10-K MD&A and in investor-day materials. Ask management for quarterly shipments, with B&H units shown separately.

#### FIN-18: FY2025 Adjusted EBITDA ex bill-and-hold is about $85.7M (18.2% margin), not $98.8M (19.7%)
- **Finding:** The B&H revenue inflated FY2025 Adjusted EBITDA by about $13.1M (13%), using the company gross margin. This corrects the FY2025 margin trend from iteration-1: underlying margin expansion was 0.5 points, not 2.0 points.
- **Evidence:**
  - Segment gross margin is not disclosed, so I cannot compute a hardware gross margin. Assumption: the company FY2025 gross margin, 206.3 / 502.3 = 41.1%, and no variable opex.
  - Gross profit on B&H: 31.8 x 41.07% = 13.1.
  - Adj. EBITDA ex B&H: 98.8 - 13.1 = 85.7. Margin = 85.7 / 470.5 = 18.2%, against 17.7% in FY2024 and 19.7% reported.
  - EBITDA ex B&H: 64.1 - 13.1 = 51.0.
  - Sensitivity: at a 30% hardware gross margin, the effect is 9.5 and the result is 89.3. At 50%, the effect is 15.9 and the result is 82.9.
  - H1 2026 normalized:
    - Reversal gross profit: 9.4 x 41.07% = 3.9.
    - Adj. EBITDA: 29.9 + 3.9 = 33.8 (14.6% of 232.0). With the SLA credits at 100% margin: 36.1 (15.4% of 234.3).
    - Gross margin: (84.6 + 3.9 + 2.3) / 234.3 = 38.7%, still below the 40.8% of H1 2025 (92.4 / 226.5).
  - Gross margin trend: 40.1% (147.9 / 368.9), 40.8% (172.1 / 421.7), 41.1%, then H1 2026 38.0% (84.6 / 222.6).
- **Source:** `income_statement.csv` rows "Gross profit", "Total revenue", "Revenue: Hardware"; `adjusted_ebitda_reconciliation.csv` rows "EBITDA", "Adjusted EBITDA" (FY2025, H1_2026).
- **Severity:** High.
- **Confidence:** Medium. It depends on the margin assumption, and the range is shown.
- **Deal impact:** Valuation.
- **Cross-check:** Segment gross margin from the 10-K, or from a quality of earnings provider. Pricing of the Norvale B&H order.

#### FIN-19: The reported 2.26x covenant ratio implies the 15% add-back cap was not applied; capped, the ratio is 2.61x to 3.57x at June 30, 2026
- **Finding:** The reported 2.26x is consistent only with uncapped company Adjusted EBITDA. LTM non-recurring add-backs are 26.4% of Adjusted EBITDA (46.3% if stock-based compensation, SBC, counts), well over the 15% cap as summarized. If the cap applies as described, covenant compliance may be misstated. This depends on the exact Note 9 text. It adds a new point to iteration-1.
- **Evidence:**
  - Gross debt: 45.0 + 182.5 = 227.5. Cash 33.9, capped at 25.0. Covenant net debt = 202.5. Uncapped net debt = 193.6.
  - Implied covenant EBITDA = 202.5 / 2.26 = 89.6, which matches LTM Adj. EBITDA of 89.7 (202.5 / 89.7 = 2.26x).
  - Add-backs as a share of LTM Adj. EBITDA:
    - Restructuring 9.7 + other non-recurring 14.0 = 23.7. Share = 23.7 / 89.7 = 26.4%.
    - With SBC 17.8: 41.5. Share = 41.5 / 89.7 = 46.3%.
  - Reading A (SBC is not capped). Base = EBITDA 48.2 + SBC 17.8 = 66.0.
    - Cap at 15% of the final Consolidated EBITDA: allowed add-backs = 66.0 x 0.15 / 0.85 = 11.6. Consolidated EBITDA = 77.6. Ratio = 202.5 / 77.6 = 2.61x.
    - Cap at 15% of the pre-add-back base: 66.0 x 1.15 = 75.9. Ratio = 2.67x.
  - Reading B (SBC is capped too). Base = 48.2. Consolidated EBITDA = 48.2 / 0.85 = 56.7. Ratio = 3.57x, which breaches even the current 3.50x. On the pre-add-back basis: 48.2 x 1.15 = 55.4, ratio 3.65x.
- **Source:** `balance_sheet.csv` rows "Cash and cash equivalents", "Revolving credit facility", "Term loan" (Q2_2026); `adjusted_ebitda_reconciliation.csv` column LTM_Q2_2026, rows EBITDA, SBC, Restructuring, Other non-recurring, Adjusted EBITDA; covenant terms from 10-K Note 9 (SEC analyst summary, via the lead).
- **Severity:** High. It becomes Critical if Reading B is the correct reading of the text.
- **Confidence:** Medium. The arithmetic is High, but the definition is not yet confirmed.
- **Deal impact:** Financing and closing risk. Possible misreported compliance is also a disclosure and controls concern.
- **Cross-check:** The full credit agreement (the definitions of Consolidated EBITDA and of which add-backs are capped), the Q2 2026 compliance certificate, and any lender amendments or waivers in 8-Ks.

#### FIN-20: Forward covenant headroom is thin on the company basis and breached on the capped basis by December 31, 2026
- **Finding:** On the company basis, the December 31, 2026 ratio is 2.60x to 2.89x against a 3.00x test. At low guidance that is only $2.5M (3.6%) of EBITDA cushion. Under capped Reading A the ratio is 3.03x to 3.53x, a breach at every point of the guidance range. Under Reading B it is 4.41x to 5.55x. September 30 passes on all readings except B. This adds to iteration-1.
- **Method:**
  - December 31: LTM = FY2026 = guidance of 70, 74 or 78 (low, mid, high).
  - FY2026 add-backs are estimated as H1 2026 doubled: SBC 8.9 x 2 = 17.8; non-recurring (4.4 + 6.2) x 2 = 21.2.
  - September 30: LTM = 89.7 - Q3 2025 estimate + Q3 2026 estimate.
    - Q3 2025 estimate = 121.4 x H2 2025 ex-B&H margin. H2 2025 Adj. EBITDA = 98.8 - 39.0 = 59.8; less 13.1 = 46.7; divided by H2 revenue ex B&H of 275.8 - 31.8 = 244.0 gives 19.1%. So Q3 2025 = 23.2.
    - Q3 2026 estimate = half of the H2 2026 EBITDA implied by guidance: (70, 74 or 78 - 29.9) / 2 = 20.1, 22.1 or 24.1.
  - LTM add-backs at September 30 are assumed equal to LTM Q2 (41.5).
  - Debt base case: covenant net debt stays at 202.5. Downside at December 31 is 208.8. That assumes H1 2026 cash use of 17.7 repeats (7.7 net cash decline + 10.0 revolver draw), cash falls to the 25.0 netting cap, and the revolver funds the remaining 8.8. Term loan after amortization = 180.0. 180.0 + 53.8 = 233.8, less 25.0 = 208.8.
- **Results:**

| Basis | Sept 30, 2026 (low / mid / high LTM 86.6 / 88.6 / 90.6) | Dec 31, 2026 (FY26 guidance 70 / 74 / 78) |
|---|---|---|
| Company (uncapped) | 2.34x / 2.29x / 2.24x | 2.89x / 2.74x / 2.60x (downside debt, low: 208.8 / 70 = 2.98x) |
| Reading A, capped | (45.1 + 17.8) / 0.85 = 74.0, so 2.74x / 2.65x / 2.57x | (31.0 + 17.8) / 0.85 = 57.4, so 3.53x; 62.1, so 3.26x; 66.8, so 3.03x |
| Reading B, capped | 3.82x / 3.65x / 3.51x | 5.55x / 4.92x / 4.41x |

- **Minimum EBITDA to stay at or below 3.00x:** covenant EBITDA of 202.5 / 3.00 = 67.5 (69.6 in the debt downside).
  - Company basis: FY2026 Adj. EBITDA of at least 67.5. That requires H2 2026 of at least 37.6, which is 25.8% above H1 2026's 29.9.
  - Reading A: EBITDA + SBC must be at least 0.85 x 67.5 = 57.4. That means company Adj. EBITDA of at least 57.4 + 21.2 = 78.6, which is above the top of guidance (78).
  - Reading B: EBITDA must be at least 57.4. That means Adj. EBITDA of at least 96.4.
- **Source:** As for FIN-19, plus `income_statement.csv`, `revenue_quarterly.csv` Q3 2025, and `cash_flow.csv` H1_2026 rows "Net change in cash" and "Revolver borrowings".
- **Severity:** Critical. Change of control is an event of default, so the debt must be refinanced at closing in any case. A breach between signing and closing (from the December 31 test) would hit the target's liquidity and its MAC and interim-covenant position, and would need lender waivers.
- **Confidence:** Medium. It relies on the guidance, the quarterly split, the add-back run rate and the unconfirmed definition.
- **Deal impact:** Financing and closing risk.
- **Cross-check:** Q3 2026 actuals and the September 30 compliance certificate. Q3 2026 has already ended, so these should exist. Any amendment or waiver discussions with lenders, and the debt payoff mechanics in the merger agreement.

#### FIN-21: Normalized run-rate Adjusted EBITDA is about $80.5M; EV is 16.8x that, against 11.5x in the deal model
- **Finding:** On normalized earnings the deal model's 11.5x multiple is stale. The $1,352.8M EV is 16.3x to 16.8x normalized LTM, 17.3x to 19.3x FY2026 guidance, and 18.7x to 20.0x the annualized normalized H1 2026. This corrects and updates the iteration-1 valuation check.
- **Evidence:**
  - EV check: 24.00 x 48.3 = 1,159.2, plus net debt (227.5 - 33.9) 193.6 = 1,352.8.
  - Run rate:
    - H2 2025 ex B&H = 46.7 (FIN-20 method).
    - H1 2026 normalized = 33.8 (FIN-18).
    - Total = 80.5, or 82.8 with the SLA add-back. Cross-check: 89.7 - 13.1 + 3.9 = 80.5.
  - Further quality-of-earnings view (my judgment): also remove the add-backs that look operating. Restructuring 9.7 recurs every year (3.1, 4.6, 5.2, 7.9). Vantor litigation 4.1 is ongoing. Customer implementation delays 3.3 is an operating cost. 80.5 - 17.1 = 63.4.
  - Multiples on EV 1,352.8:

| Measure | EBITDA | EV multiple |
|---|---|---|
| Deal model FY2026E | 118.0 | 11.5x |
| LTM reported | 89.7 | 15.1x |
| Normalized run-rate, with SLA add-back | 82.8 | 16.3x |
| Normalized run-rate | 80.5 | 16.8x |
| FY2026 guidance, high | 78.0 | 17.3x |
| FY2026 guidance, mid | 74.0 | 18.3x |
| FY2026 guidance, low | 70.0 | 19.3x |
| Annualized H1 2026 normalized, with SLA add-back | 72.2 | 18.7x |
| Annualized H1 2026 normalized (33.8 x 2) | 67.6 | 20.0x |
| Quality-of-earnings view | 63.4 | 21.3x |

  - Stale assumptions: the FY2026E revenue of 560 is 80.0 (14.3%) above the guidance midpoint of 480. The FY2026E EBITDA of 118 is 44.0 (37.3%) above the guidance midpoint of 74.
  - Illustrative only (not a valuation): the deal model's 11.46x on 80.5 gives EV 922.9 and equity 729.3, which is $15.10 per share. The unaffected price of $17.85 implies EV of 862.2 + 193.6 = 1,055.8, which is 13.1x run-rate and 14.3x guidance midpoint.
  - Interest cover (LTM interest 14.9): Adj. EBITDA 6.0x, normalized 5.4x, EBITDA 3.2x.
- **Source:** `deal-brief.md`; `adjusted_ebitda_reconciliation.csv` (all columns); `balance_sheet.csv` Q2_2026; guidance from the 10-Q (via the lead).
- **Severity:** Critical. The value gap is more than 10%.
- **Confidence:** High for the arithmetic. Medium for the normalization (it relies on the gross margin assumption).
- **Deal impact:** Valuation.
- **Cross-check:** The August 6, 2026 guidance press release against the March 2026 investor-day deck. Analyst consensus in the news.

#### FIN-22: Without bill-and-hold, Norvale grew 11.4% (not 32.3%) and its FY2025 share is 28.0% (not 31.1%)
- **Finding:** Of the B&H, 77.4% was with Norvale, and B&H explains 64.6% of Norvale's reported FY2025 growth. Concentration is still very high, but the "deepening relationship" signal is mostly the B&H. This corrects the iteration-1 concentration trend.
- **Evidence:**
  - Norvale reported growth: (156.2 - 118.1) / 118.1 = 32.3%.
  - Norvale ex B&H: 156.2 - 24.6 = 131.6. Growth = 13.5 / 118.1 = 11.4%. Share = 131.6 / 470.5 = 28.0% (FY2024: 28.0%).
  - Norvale share of the B&H: 24.6 / 31.8 = 77.4%. B&H share of Norvale's growth: 24.6 / 38.1 = 64.6%.
  - Other customers ex B&H: 502.3 - 156.2 - 7.2 = 338.9. Growth = 35.3 / 303.6 = 11.6%.
- **Source:** `revenue_by_customer.csv` rows Norvale Retail Group, Total; 10-K Note 2 (via the lead).
- **Severity:** High.
- **Confidence:** High.
- **Deal impact:** Valuation and post-closing (customer risk).
- **Cross-check:** The 10-K concentration disclosure, news on Norvale's automation plans, and any Norvale disputes in the litigation records.

#### FIN-23: The returned bill-and-hold units explain about 43% of the H1 2026 inventory build
- **Finding:** Inventory rose $12.7M in H1 2026 while revenue fell. At cost, the $9.4M of returned product is about $5.5M of that increase. This adds a working-capital point.
- **Evidence:**
  - Inventory: 84.0 - 71.3 = 12.7.
  - Returned units at cost: 9.4 x (1 - 41.07%) = 5.5. Share of the build = 5.5 / 12.7 = 43%.
  - The returned robots now sit in inventory and may need a valuation reserve.
- **Source:** `balance_sheet.csv` row Inventory (FY2025, Q2_2026); `cash_flow.csv` row "Change in inventory" H1_2026 (-12.7).
- **Severity:** Low.
- **Confidence:** Medium, because the cost ratio is assumed.
- **Deal impact:** Post-closing.
- **Cross-check:** The 10-Q inventory note and reserves. Whether the returned units were resold.

### Positive or mitigating points
- On net, the B&H reverses within the LTM Q2 2026 window: +31.8 in Q4 2025 and -9.4 in Q2 2026, a net of 22.4, all of it delivered by June 30, 2026. So LTM revenue is not overstated on a delivery basis, and the LTM gross-up affects only the timing of margin, not the total.
- Software stays strong: FY2025 +27.1%, H1 2026 +14.6% (67.5 / 58.9). ARR rose from 139.2 to 146.8.
- On the company basis, September 30, 2026 headroom looks adequate (about 2.3x).
- The term loan amortizes, and cash above the $25.0M netting cap gives a small buffer before the revolver has to fund the cash burn.

### Gaps and questions for management
1. The exact credit agreement definitions: which add-backs are capped, whether SBC is included, the basis of the 15% cap, and the Q2 2026 compliance certificate showing the calculation behind 2.26x.
2. Q3 2026 actuals and the September 30, 2026 covenant certificate, which should already exist.
3. Quarterly Adjusted EBITDA and quarterly robot shipments for 2025 to 2026, with B&H units shown separately.
4. The KPI definitions for "robots shipped" and "installed base".
5. Segment gross margin, needed to replace the 41.1% assumption.
6. Pricing and margin on the Norvale B&H order, and why $9.4M was returned.
7. Where the $2.3M of SLA credits sit (software or services), and whether more credits are expected.
8. The bridge from the March investor-day case ($560M / $118M) to the August guidance ($470M to $490M / $70M to $78M).
9. Any B&H arrangements in H1 2025 or in FY2026.
10. A quality of earnings report, which has not been received yet (`data/financials/README.md`).

Files used: /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/ (all 8 files) and /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md.
