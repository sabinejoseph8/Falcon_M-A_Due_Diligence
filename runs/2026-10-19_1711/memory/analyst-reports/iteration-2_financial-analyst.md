# Iteration 2: financial-analyst report (follow-up)

Saved unedited by the lead agent.

---

## Financial analyst: findings (Project Heron, iteration 2)

### Files reviewed
- `targets/heron/data/deal-brief.md` (Sections 1, 3, 4)
- `targets/heron/data/financials/README.md`
- `targets/heron/data/financials/income_statement.csv`
- `targets/heron/data/financials/balance_sheet.csv`
- `targets/heron/data/financials/cash_flow.csv`
- `targets/heron/data/financials/adjusted_ebitda_reconciliation.csv`
- `targets/heron/data/financials/revenue_by_customer.csv`
- `targets/heron/data/financials/revenue_quarterly.csv`
- `targets/heron/data/financials/kpis.csv`

Facts from other sources, used as the lead gave them: 10-K FY2025 Notes 11, 14 and 15, MD&A and FX sensitivity; 10-Q Q2 2026 Notes 7, 9, 10 and 12, MD&A and Liquidity; 8-K of May 14, 2026; Utility Programs West (Jul 22, 2026); Monterrey Economia (Sep 15, 2026, anonymous bankers, so an allegation); litigation LIT-002 and LIT-004; proxy (NEO severance).

From iteration 1 I used the Case B LTM Adjusted EBITDA of US$115.4m as the lead gave it. I re-derived the iteration-1 debt-like total of US$270.1m: pension 151.0 + payables stretch 57.1 + utility prepayments 34.0 + uncertain tax positions (UTP) 14.2 + environmental 8.7 + field action 5.1 = 270.1. I also re-derived the payables stretch: AP 160.0 less 238.8 / 181 x 78 = 102.9, which gives 57.1. I could not rebuild the 15.0 gap between 130.4 and 115.4 from the files alone. **The lead should confirm Case B does not already deduct peso or Gulf Horizon effects.** Otherwise FIN-049 and FIN-052 would be double counted.

No instruction-like text was found in any file.

### Key metrics table

| Metric (US$m) | FY2023 | FY2024 | FY2025 | H1 2026 / LTM Q2 2026 |
|---|---|---|---|---|
| Total revenue | 687.0 | 738.0 | 786.0 | H1 394.0 / LTM 807.0 |
| Devices revenue | 471.0 | 489.0 | 503.0 | H1 238.0 / LTM 505.0 |
| Utility Programs revenue | 112.0 | 128.0 | 141.0 | H1 72.0 / LTM 144.0 |
| WSEA revenue (rank 1) | n/a | 88.0 | 96.0 | not in files |
| WSEA as % of Utility Programs | n/a | 68.8% | 68.1% | not derivable |
| Utility Programs excluding WSEA | n/a | 40.0 | 45.0 | not derivable |
| Gulf Horizon revenue (rank 4) | n/a | 4.1 | 38.6 | not in files |
| Revenue excluding Gulf Horizon | n/a | 733.9 | 747.4 | not derivable |
| Gross margin (reported) | 41.0% | 41.8% | 42.5% | H1 39.4% / LTM 41.1% |
| EBITDA (reported) | 80.2 | 102.5 | 116.1 | LTM 100.2 |
| Adjusted EBITDA (company) | 100.5 | 121.7 | 133.7 | LTM 130.4 |
| Adjusted EBITDA, Case B (iteration 1) | n/a | n/a | n/a | LTM 115.4 |
| Accounts payable / DPO (days) | 84.0 / 76 | 89.0 / 76 | 96.0 / 78 | 160.0 / 121 |
| Utility program prepayments | 6.0 | 6.5 | 7.0 | 41.0 |
| Cash | 96.4 | 54.5 | 59.4 | 160.4 |
| Long-term debt | 455.0 | 470.0 | 440.0 | 420.0 |
| Net debt (reported) | 358.6 | 415.5 | 380.6 | 259.6 |
| Pension and postretirement liability | 171.0 | 162.0 | 154.5 | 151.0 |
| MXN per US$ (average) | 17.7 | 18.3 | 19.4 | 17.2 |
| Peso share of cost of revenue | 58% | 60% | 62% | 63% |
| MXN hedge cover, next 12 months | 70% | 72% | 0% | 0% |

Adjusted figures (mine, not company-reported): rebuilt net debt plus debt-like items before contingencies is **US$720.8m** (FIN-065). Rebased value is **US$12.32 per share** on Case B and **US$5.81** on Case B less WSEA (FIN-066).

### Findings

#### FIN-046: WSEA contract loss puts EBITDA worth more than 10% of EV at risk
- **Finding:** WSEA was the largest customer at US$96.0m (12.2% of FY2025 revenue). It ends on Dec 31, 2026 and the 2027 program went to Thermiq. Any contribution margin above 13.6% on that revenue makes the value loss larger than 10% of EV.
- **Evidence:**
  - WSEA share of Utility Programs = 96.0 / 141.0 = 68.1%. H1 2026 WSEA revenue is not in the files. A pro-rata estimate is 72.0 x 68.1% = 49.0 (estimate only).
  - Check of the multiple: EV / Adjusted EBITDA = 1,543.4 / 130.4 = 11.84x.
  - Threshold: 10% of EV = 154.3. EBITDA loss needed = 154.3 / 11.84 = 13.0. Margin needed = 13.0 / 96.0 = 13.6%.
  - Contribution-margin cases (projection):

    | Margin | EBITDA lost | Value at 11.84x | % of EV |
    |---|---|---|---|
    | 20% | 19.2 | 227.3 | 14.7% |
    | 30% (base, assumption) | 28.8 | 341.0 | 22.1% |
    | 40% | 38.4 | 454.7 | 29.5% |

  - The company gross margin was 42.5% in FY2025. Segment margins are not in the files.
- **Source:** `revenue_by_customer.csv` row 1 (rank 1); `income_statement.csv` rows "Revenue: Utility Programs", "Total revenue"; `kpis.csv` row "Gross margin (%)"; the contract end and award are from the lead (10-Q MD&A; Utility Programs West, Jul 22, 2026).
- **Severity:** Critical. Test: more than 10% of value. The loss is 227.3 to 454.7 (14.7% to 29.5% of EV) at any margin from 20% to 40%. The break-even margin of 13.6% is far below the 42.5% gross margin.
- **Confidence:** Medium. The contract end is a stated fact, but the margin is an assumption.
- **Deal impact:** Valuation. It also breaks deal-brief thesis 3, which assumes WSEA renews on similar terms.
- **Cross-check:** WSEA board minutes and award notice; any 10-Q risk-factor wording; whether Delmora can bid on other WSEA programs; segment profitability data from management.

#### FIN-047: Utility Programs revenue from 2027 without WSEA versus the deal brief
- **Finding:** Without WSEA, Utility Programs falls to a base of about US$45.0m. The deal brief implies about US$158.4m in 2027.
- **Evidence:**
  - FY2025: 141.0 - 96.0 = 45.0. FY2024: 128.0 - 88.0 = 40.0. Growth excluding WSEA = 45.0 / 40.0 - 1 = 12.5%.
  - Deal brief at 6% a year: 141.0 x 1.06 x 1.06 = 158.4 in 2027 (projection).
  - Without WSEA at the same 6%: 45.0 x 1.06 x 1.06 = 50.6 (projection). The gap is 107.9 of 2027 revenue.
  - Cascadia Power & Light (rank 5, 23.5) is probably in this residual. That is an assumption, which would leave about 21.5 from all other utilities.
- **Source:** `revenue_by_customer.csv` rows 1 and 5; `income_statement.csv` row "Revenue: Utility Programs"; deal-brief Section 4 / thesis 3.
- **Severity:** High. Supports FIN-046, which carries the value impact.
- **Confidence:** Medium. It assumes all WSEA revenue sits in Utility Programs.
- **Deal impact:** Valuation and revenue durability (IC question 5).
- **Cross-check:** 10-Q segment note; Utility Programs West reporting on other program renewals.

#### FIN-048: The US$34.0m WSEA advance unwinds before a Q1 2027 close
- **Finding:** The June 2026 advance pays for H2 2026 program incentives, and the contract ends Dec 31, 2026. So it should be spent by year end, with no 2027 advance to replace it. Cash at a Q1 2027 close would be about US$34.0m lower than the June 30 figure.
- **Evidence:**
  - Prepayments rose from 7.0 to 41.0, an increase of 34.0. The cash flow line shows +34.0 in H1 2026.
  - H1 2026 operating cash flow excluding the prepayment and payables inflows = 134.1 - 34.0 - 64.0 = 36.1, against 34.9 in H1 2025.
  - Whether the 7.0 baseline also relates to WSEA is not in the files. If it does, a further 7.0 unwinds.
- **Source:** `balance_sheet.csv` row "Utility program customer prepayments"; `cash_flow.csv` rows "Change in utility program customer prepayments", "Change in accounts payable", "Net cash from operating activities"; 10-Q MD&A Liquidity (from the lead).
- **Severity:** High. It directly reduces the cash behind the US$100.0m company-cash source.
- **Confidence:** High on the amount, Medium on the timing (projection).
- **Deal impact:** Financing and closing funds flow.
- **Cross-check:** WSEA contract payment schedule; customer split of the 7.0 baseline prepayment.

#### FIN-049: Gulf Horizon revenue and EBITDA at risk after the shipment suspension
- **Finding:** Gulf Horizon was US$38.6m of FY2025 revenue and 93.7% of international distributor revenue. Shipments stopped in June 2026, so H2 2026 revenue is likely nil (projection). H1 2026 Gulf Horizon revenue is not in the files.
- **Evidence:**
  - Share of distributor revenue = 38.6 / 41.2 = 93.7%.
  - FY2025 revenue excluding Gulf Horizon = 786.0 - 38.6 = 747.4. LTM, assuming Gulf Horizon's LTM revenue equals FY2025 = 807.0 - 38.6 = 768.4 (assumption).
  - EBITDA estimate at the 42.5% FY2025 gross margin (assumed contribution) = 16.4, worth 16.4 x 11.84 = 194.2, or 12.6% of EV.
  - At a 30% margin: 11.6, worth 137.3, or 8.9% of EV. The margin needed to exceed 10% of EV = 13.0 / 38.6 = 33.8%.
  - Case B less Gulf Horizon = 115.4 - 16.4 = 99.0 (projection).
- **Source:** `revenue_by_customer.csv` row 4; `income_statement.csv` "Total revenue"; `kpis.csv` "Gross margin (%)"; 10-K MD&A and 10-Q Note 12 (from the lead).
- **Severity:** High. Not Critical: the value impact crosses 10% only at margins above 33.8%, and the margin is not in the files.
- **Confidence:** Medium. It depends on the margin and on H1 2026 revenue.
- **Deal impact:** Valuation; possible trade-compliance exposure on past revenue.
- **Cross-check:** BIS subpoena scope; Gulf Horizon receivable at June 30, 2026; end-user certificates; any OFAC or BIS voluntary disclosure.

#### FIN-050: FY2025 growth excluding Gulf Horizon is 1.8%, and Devices shrank
- **Finding:** Reported FY2025 growth of 6.5% falls to 1.8% without Gulf Horizon. If Gulf Horizon sits in Devices (assumption), Devices excluding Gulf Horizon fell 4.2%.
- **Evidence:**
  - Reported growth: 786.0 / 738.0 - 1 = 6.5%. Excluding Gulf Horizon: 747.4 / 733.9 - 1 = 1.8%.
  - Gulf Horizon's increase of 38.6 - 4.1 = 34.5 is more than Devices growth of 503.0 - 489.0 = 14.0.
  - Devices excluding Gulf Horizon: 464.4 / 484.9 - 1 = -4.2%.
- **Source:** `revenue_by_customer.csv` rows 4 and Total; `income_statement.csv` rows "Revenue: Devices", "Total revenue".
- **Severity:** Medium. The value impact is in FIN-049. This card is about growth quality and deal-brief thesis 4.
- **Confidence:** High on the totals, Medium on the segment mapping.
- **Deal impact:** Valuation multiple; growth narrative.
- **Cross-check:** 10-K geographic revenue disclosure.

#### FIN-051: Thermostat share of Devices not found; Calder royalty upper bound
- **Finding:** No financial file splits Devices into thermostats, sensors and hubs. Using all of Devices revenue as an upper bound, a 4% royalty is up to US$20.2m a year, plus back royalties of up to US$86.1m for FY2022 to H1 2026. FY2019 to FY2021 Devices revenue is not in the files.
- **Evidence:**
  - LTM Devices revenue = 503.0 - 236.0 + 238.0 = 505.0. Annual royalty = 505.0 x 4% = 20.2, worth 239.2 at 11.84x, or 15.5% of EV (upper bound, projection).
  - Back royalties: Devices revenue of 452.0 + 471.0 + 489.0 + 503.0 + 238.0 = 2,153.0, x 4% = 86.1.
  - Illustrative FY2019 to FY2021 figure: if each year was at or below FY2022 (an assumption; Devices grew every year from FY2022 to FY2025), at most 3 x 452.0 x 4% = 54.2. That makes a total upper bound of about 140.3 (projection).
- **Source:** `income_statement.csv` row "Revenue: Devices" (FY2022 to H1 2026); claim from litigation LIT-002 (via the lead).
- **Severity:** High. Not Critical: it is a disputed claim on an upper-bound base.
- **Confidence:** Low. This is an allegation, and the thermostat share is unknown.
- **Deal impact:** Valuation, a possible special indemnity or price adjustment, and technology ownership (IC question 3).
- **Cross-check:** Calder agreement terms; court docket; thermostat unit and revenue split from management.

#### FIN-052: Peso strengthening, run-rate cost and the part already in LTM
- **Finding:** On the company's own sensitivity, the move from 19.4 to 17.2 costs about US$35.8m a year. About US$17.1m of that is already in LTM, which leaves about US$17.0m to US$18.7m of run-rate cost not yet in LTM (projection). There is no hedge cover.
- **Evidence:**
  - Check of the sensitivity: FY2025 peso cost = 451.9 x 62% = 280.2. 10% of that = 28.0, which matches the 10-K figure.
  - Size of the move: 19.4 / 17.2 - 1 = 12.8%. Cost = 28.0 x 1.28 = 35.8. On the alternative measure, (19.4 - 17.2) / 19.4 = 11.3%, the cost is 31.8.
  - Already in LTM: H1 2026 peso cost = 238.8 x 63% = 150.4. At 19.4 it would have been 150.4 x 17.2 / 19.4 = 133.4. The H1 impact is 17.1, which assumes H2 2025 was at the FY average of 19.4 (assumption).
  - Run-rate on the current cost base = 2 x 17.1 = 34.1. Not yet in LTM: 34.1 - 17.1 = 17.0 to 35.8 - 17.1 = 18.7.
  - Value at 11.84x: 201.3 to 221.4, or 13.0% to 14.3% of EV.
  - Hedge cover is 0% for FY2025 and Jun 2026.
- **Source:** `income_statement.csv` row "Cost of revenue"; `kpis.csv` rows "Share of cost of revenue denominated in Mexican pesos", "Average MXN per US$", "MXN cost hedge coverage"; 10-K MD&A Foreign currency (from the lead).
- **Severity:** High. It reaches the more-than-10%-of-value level only if the peso stays at 17.2, there are no pricing offsets, and Case B does not already deduct it. These assumptions are not verified, so it is not rated Critical.
- **Confidence:** Medium. It depends on the H2 2025 rate assumption and on the FX path.
- **Deal impact:** Valuation; stale gross-margin assumption (FIN-053).
- **Cross-check:** H1 and H2 2025 average rates; hedging policy after the program lapsed; 10-Q FX sensitivity update.

#### FIN-053: The deal brief's 42% gross margin from 2027 is not supported at current FX
- **Finding:** H1 2026 gross margin was 39.4%, down from 42.3% in H1 2025. Adding the peso cost not yet in LTM gives a run-rate of about 38.8%, before any loss of WSEA mix.
- **Evidence:**
  - H1 2026: 155.2 / 394.0 = 39.4%. H1 2025: 157.8 / 373.0 = 42.3%.
  - LTM gross profit = 334.1 - 157.8 + 155.2 = 331.5. LTM margin = 331.5 / 807.0 = 41.1%.
  - Less 18.7: (331.5 - 18.7) / 807.0 = 38.8% (projection).
- **Source:** `income_statement.csv` rows "Gross profit", "Total revenue"; `kpis.csv` "Gross margin (%)"; deal-brief Section 4.
- **Severity:** Medium.
- **Confidence:** Medium. This is a projection.
- **Deal impact:** Valuation model inputs.
- **Cross-check:** Management's 2027 cost plan; contract manufacturer pricing.

#### FIN-054: Pittock pension termination shortfall triggered by the change of control
- **Finding:** The change of control requires funding on a termination basis within 120 days. The shortfall is US$230.5m, against the accounting deficit of US$154.5m (FY2025). The termination shortfall replaces the accounting deficit in the bridge rather than adding to it.
- **Evidence:**
  - Termination shortfall: 522.0 - 291.5 = 230.5, or 14.9% of EV (230.5 / 1,543.4).
  - Accounting deficit: 446.0 - 291.5 = 154.5. This ties exactly to the FY2025 balance sheet line of 154.5, which confirms there is no separate hidden pension liability.
  - Increase over the accounting deficit: 76.0 at Dec 2025, or 79.5 over the Q2 2026 balance of 151.0.
  - The deal brief has no debt-like adjustment for the pension.
- **Source:** `balance_sheet.csv` row "Pension and postretirement benefit obligations" (FY2025, Q2_2026); `cash_flow.csv` row "Pension contributions in excess of expense"; 10-K Note 11 (from the lead); deal-brief Section 4.
- **Severity:** Critical. Test: more than 10% of value. 230.5 is 14.9% of EV and 18.0% of equity value (230.5 / 1,283.8).
- **Confidence:** High. Primary-source amounts, recomputed.
- **Deal impact:** Valuation, financing (a use of funds within 120 days of closing) and post-closing cash.
- **Cross-check:** Trust agreement wording; annuity insurer quotes at current rates; PBGC notice requirements.

#### FIN-055: Nimbus earn-out accelerates to US$90.0m cash on a change of control
- **Finding:** The May 12, 2026 amendment makes the full US$90.0m payable within 10 business days of any change of control. The amount is carried at US$8.0m, so the cash call is US$82.0m above the carrying value.
- **Evidence:**
  - 90.0 - 8.0 = 82.0. As shares of EV: 90.0 is 5.8% and 82.0 is 5.3%.
  - The carrying value fell from 14.5 to 8.0 in FY2025, with a 6.5 non-cash gain.
  - The amendment came after the Strategic Review Committee was formed in March 2026 (inference on timing).
- **Source:** `balance_sheet.csv` row "Contingent consideration (Nimbus earn-out)"; `cash_flow.csv` row "Change in fair value of contingent consideration"; 8-K May 14, 2026 and 10-Q Note 9 (from the lead).
- **Severity:** High. It needs to be in closing funds flow and price.
- **Confidence:** High.
- **Deal impact:** Valuation and closing funds.
- **Cross-check:** Board approval of the amendment while the sale process was running; who the beneficiaries are (any insiders).

#### FIN-056: The deal brief's EV excludes the US$8.0m Nimbus carrying value
- **Finding:** The deal brief says the earn-out is treated as debt-like at US$8.0m, but its EV does not include it.
- **Evidence:** 1,283.8 + 259.6 = 1,543.4. The 8.0 is not in the sum.
- **Source:** deal-brief Sections 1 and 4; `balance_sheet.csv` Nimbus row.
- **Severity:** Low. It is superseded by FIN-055.
- **Confidence:** High.
- **Deal impact:** Valuation (minor).
- **Cross-check:** The deal model itself.

#### FIN-057: NEO change-of-control severance
- **Finding:** Severance is US$21.6m at US$18.70 (proxy). The amount at US$24.50 is not given. It may be higher if any part is equity-linked.
- **Evidence:** 21.6, or 1.4% of EV (21.6 / 1,543.4).
- **Source:** proxy (from the lead). No financial file holds it.
- **Severity:** Medium.
- **Confidence:** Medium. The figure is at the wrong share price.
- **Deal impact:** Closing funds.
- **Cross-check:** Proxy golden-parachute table recomputed at US$24.50; 280G gross-ups.

#### FIN-058: Payables stretch matches the contract manufacturer's term change; unwind risk is higher
- **Finding:** The iteration-1 payables stretch of US$57.1m matches the move from 60 to 120 days with the main contract manufacturer from April 1, 2026. The counterparty appears to be Ensamble Norte, which is reported (anonymous source) to have missed a loan payment. That raises the risk that the terms reverse (inference).
- **Evidence:**
  - AP rose 160.0 - 96.0 = 64.0 in H1 2026, matching the cash flow line of 64.0. DPO rose from 78 to 121 days.
  - Normal AP at 78 days = 238.8 / 181 x 78 = 102.9. Excess = 57.1.
- **Source:** `balance_sheet.csv` "Accounts payable"; `cash_flow.csv` "Change in accounts payable"; `kpis.csv` "Days payable outstanding"; 10-Q MD&A; Monterrey Economia (allegation).
- **Severity:** High.
- **Confidence:** High on the numbers, Medium on the link to Ensamble's distress.
- **Deal impact:** Working-capital peg and closing cash.
- **Cross-check:** AP owed to Ensamble at June 30, 2026 (related-party note); whether Delmora set the term change while it guarantees Ensamble's loan.

#### FIN-059: Ensamble Norte loan guarantee
- **Finding:** Delmora guarantees US$64.0m of Ensamble's term loan and has recorded only US$0.6m. A missed payment of about US$5.7m on Aug 31, 2026 is reported by anonymous sources (allegation).
- **Evidence:** Unrecorded exposure = 64.0 - 0.6 = 63.4, or 4.1% of EV.
- **Source:** 10-K Note 14 (from the lead); `balance_sheet.csv` row "Equity-method investment (Ensamble Norte)"; Monterrey Economia (Sep 15, 2026).
- **Severity:** High. A guarantee call could fall due before closing, and supply depends on Ensamble.
- **Confidence:** Medium. The guarantee is primary-source; the default is an allegation.
- **Deal impact:** Financing, closing risk and supply continuity.
- **Cross-check:** Lender notices; Ensamble's financial statements; cross-default terms in Delmora's credit agreement.

#### FIN-060: Carrying value of the Ensamble equity-method investment
- **Finding:** The investment is carried at US$20.4m and could be impaired if Ensamble is in distress. This is a non-cash item.
- **Evidence:** 18.0 (FY2023), 19.2, 20.1, 20.4 (Q2 2026).
- **Source:** `balance_sheet.csv` row "Equity-method investment (Ensamble Norte)".
- **Severity:** Low.
- **Confidence:** Medium.
- **Deal impact:** Post-closing accounting.
- **Cross-check:** Q3 2026 impairment assessment.

#### FIN-061: IRS proposed adjustment (NOPA) on the 2019 Irish IP transfer
- **Finding:** The proposed tax plus penalty is US$121.1m, before interest. The recorded uncertain tax position (UTP) liability is US$14.2m.
- **Evidence:**
  - Penalty: 86.5 x 40% = 34.6. Tax plus penalty = 121.1.
  - Excess over the reserve = 121.1 - 14.2 = 106.9 (high case; assumes the whole UTP relates to this matter). Low case is 0. Interest is not quantified.
  - 106.9 is 6.9% of EV.
- **Source:** `balance_sheet.csv` row "Liability for uncertain tax positions"; 10-Q Note 10 (from the lead).
- **Severity:** High.
- **Confidence:** Medium. The outcome is uncertain.
- **Deal impact:** Valuation; tax protection or R&W insurance exclusion.
- **Cross-check:** NOPA document; IRS appeals status; interest computation.

#### FIN-062: Pittock and Marlow environmental exposure
- **Finding:** The accrual is at the low end of a US$9.0m to US$71.0m range. Off-site TCE has been confirmed, and a residents' suit claims US$45.0m.
- **Evidence:**
  - Unaccrued range = 71.0 - 9.0 = 62.0. Adding the claim gives 107.0 (high case), or 6.9% of EV. This assumes the claim sits outside the remediation range (assumption).
  - Low case is 0. Off-site confirmation makes a zero increase less plausible (inference).
  - The reserve is now 8.7.
- **Source:** `balance_sheet.csv` row "Environmental remediation reserve"; 10-K Note 15; LIT-004 (from the lead).
- **Severity:** High.
- **Confidence:** Medium.
- **Deal impact:** Valuation; specific protection.
- **Cross-check:** Ohio EPA orders; updated remediation estimate after the Sept 2026 confirmation.

#### FIN-063: EC Statement of Objections, fine cap
- **Finding:** The fine cap is 10% of worldwide turnover: US$78.6m on FY2025 revenue, or US$80.7m on LTM revenue. The actual fine is unknown.
- **Evidence:**
  - 786.0 x 10% = 78.6, or 5.1% of EV. 807.0 x 10% = 80.7.
  - The group turnover used for the cap could include a new parent after closing (inference; legal check needed).
- **Source:** `income_statement.csv` "Total revenue"; 10-Q Note 12 (from the lead).
- **Severity:** High.
- **Confidence:** Medium. The cap is a ceiling, not an estimate.
- **Deal impact:** Valuation, post-closing, and exposure of the sponsor's group.
- **Cross-check:** Text of the Statement of Objections; EC precedent fines; parental liability advice.

#### FIN-064: Aura refund exposure is uninsured
- **Finding:** A refund for 1.62m units at US$119 is US$192.8m at full uptake. Insurance excludes units made before 2024. The reserve left is US$5.1m.
- **Evidence:**
  - 1.62 x 119 = 192.8. At 25% uptake: 48.2. At 50%: 96.4.
  - Net of the reserve: 43.1 and 91.3 (2.8% and 5.9% of EV).
  - Reserve: 6.0 charged less 0.9 used = 5.1.
  - Replacement-unit and logistics costs are not included.
- **Source:** `balance_sheet.csv` row "Product field action reserve"; `cash_flow.csv` row "Change in product field action reserve"; `adjusted_ebitda_reconciliation.csv` "Detail: Aura" row; 10-Q Note 7 (from the lead).
- **Severity:** High.
- **Confidence:** Medium. Uptake is an assumption.
- **Deal impact:** Valuation and possible MAE debate. The 6.0 add-back also contradicts management's "contained" description.
- **Cross-check:** CPSC correspondence; the company's response; historical uptake rates.

#### FIN-065: Rebuilt net debt and debt-like bridge
- **Finding:** Net debt plus debt-like items before contingencies is US$720.8m, against US$259.6m in the deal brief. Contingent exposures add US$43.1m to US$447.2m.
- **Evidence:**

  | Item | US$m |
  |---|---|
  | Reported net debt (420.0 - 160.4) | 259.6 |
  | (a) Pension termination shortfall (replaces the 151.0 accounting deficit) | 230.5 |
  | (a) Nimbus at full cash (8.0 carrying + 82.0 above it) | 90.0 |
  | (a) NEO severance (at US$18.70) | 21.6 |
  | **(a) subtotal** | **342.1** |
  | (b) Payables stretch | 57.1 |
  | (b) WSEA advance | 34.0 |
  | **(b) subtotal** | **91.1** |
  | (d) Recorded: UTP 14.2 + environmental 8.7 + field action 5.1 | 28.0 |
  | **Total before (c)** | **720.8** |
  | (c) IRS (0 to 106.9) | |
  | (c) Environmental (0 to 107.0) | |
  | (c) EC (0 to 78.6) | |
  | (c) Ensamble (0 to 63.4) | |
  | (c) Aura net (43.1 at 25% to 91.3 at 50%) | |
  | **(c) total** | **43.1 to 447.2** |

  - Reconciliation to iteration 1 (259.6 + 270.1 = 529.7): pension +79.5, Nimbus +90.0, severance +21.6, total +191.1, giving 720.8.
  - (a) plus (b) = 433.2, or 28.1% of EV.
  - Calder (FIN-051) and peso (FIN-052) are left out of the (c) total and shown as sensitivities.
- **Source:** `balance_sheet.csv` Q2_2026 rows as cited; FIN-054 to FIN-064.
- **Severity:** Critical. Test: more than 10% of value. (a) plus (b) is 433.2, or 28.1% of EV.
- **Confidence:** Medium for the total, which mixes recomputed figures with lead-supplied amounts and stated assumptions.
- **Deal impact:** Valuation and financing.
- **Cross-check:** Each underlying card.

#### FIN-066: Rebased value per share at 11.84x (projection)
- **Finding:** On Case B with the full bridge deducted, value is US$12.32 per share. Without WSEA it is US$5.81. Both are far below the US$24.50 offer and below the US$18.70 unaffected price.
- **Evidence:** All cases use 52.4m shares and deduct 720.8 (narrow-basis rows deduct 692.8).

  | Case | EBITDA | EV at 11.84x | Equity | Per share | Vs US$24.50 | Vs US$18.70 |
  |---|---|---|---|---|---|---|
  | (i) Case B | 115.4 | 1,366.3 | 645.5 | 12.32 | -49.7% | -34.1% |
  | (i) with (c) low / high | | | 602.4 / 198.3 | 11.50 / 3.78 | | |
  | (ii) Case B less WSEA at 30% (115.4 - 28.8) | 86.6 | 1,025.3 | 304.5 | 5.81 | -76.3% | -68.9% |
  | (ii) with (c) low / high | | | 261.4 / -142.7 | 4.99 / nil | | |
  | Narrow basis, (a) and (b) only: (i) | | | 673.5 | 12.85 | | |
  | Narrow basis, (a) and (b) only: (ii) | | | 332.5 | 6.35 | | |

  - Stress case: Case B less WSEA less Gulf Horizon = 70.2. EV = 831.2, equity = 110.4, or 2.11 per share.
  - Applying 11.84x to a smaller, more concentrated base is generous (inference).
- **Source:** FIN-046, FIN-065; deal-brief Section 1.
- **Severity:** Critical. Test: more than 10% of value. Rebased value is 49.7% below the offer even on Case B.
- **Confidence:** Medium. This is a projection that relies on margin and uptake assumptions.
- **Deal impact:** Valuation (IC question 6).
- **Cross-check:** The deal model rerun with these inputs.

#### FIN-067: Sources and uses do not fund the change-of-control cash calls
- **Finding:** Adding the (a) items lifts uses from US$1,703.8m to US$2,045.9m. Sponsor equity would rise 48.6%, from US$703.8m to US$1,045.9m.
- **Evidence:**

  | | Deal brief | Rebuilt |
  |---|---|---|
  | Uses: equity | 1,283.8 | 1,283.8 |
  | Uses: refinance debt | 420.0 | 420.0 |
  | Uses: Nimbus | | 90.0 |
  | Uses: pension funding (within 120 days) | | 230.5 |
  | Uses: severance | | 21.6 |
  | **Total uses** | **1,703.8** | **2,045.9** |
  | Sources: TLB | 900.0 | 900.0 |
  | Sources: company cash | 100.0 | 100.0 |
  | Sources: sponsor equity | 703.8 | 1,045.9 |

  - Fees are not in the files.
  - Sponsor equity share of total funding: 41.3% in the deal brief, 51.1% rebuilt.
- **Source:** deal-brief Section 1; FIN-054, FIN-055, FIN-057.
- **Severity:** High. It can be cured with more equity or a lower price.
- **Confidence:** High on the arithmetic.
- **Deal impact:** Financing.
- **Cross-check:** TLB commitment letter conditions (leverage, EBITDA definitions).

#### FIN-068: Leverage on each EBITDA case
- **Finding:** TLB leverage is 6.9x on the company's figure, 7.8x on Case B and 10.4x without WSEA. It is higher still if the cash calls are funded with debt.
- **Evidence:**

  | EBITDA case | TLB 900.0 | 1,242.1 (TLB plus (a), if debt-funded) |
  |---|---|---|
  | Company Adjusted EBITDA, 130.4 | 6.90x | 9.53x |
  | Reported EBITDA, 100.2 | 8.98x | |
  | Case B, 115.4 | 7.80x | 10.76x |
  | Case B less WSEA, 86.6 | 10.39x | 14.34x |
  | Stress case, 70.2 | 12.82x | |

  - Current interest cover: 130.4 / 21.4 = 6.1x, and 100.2 / 21.4 = 4.7x.
  - Interest cover after closing cannot be calculated because TLB pricing is not in the files.
- **Source:** `adjusted_ebitda_reconciliation.csv` LTM column (EBITDA, Adjusted EBITDA, Interest expense); deal-brief Section 1.
- **Severity:** High.
- **Confidence:** High on the arithmetic, Medium on the EBITDA cases.
- **Deal impact:** Financing; risk that the commitment is repriced.
- **Cross-check:** Lender EBITDA definition; any market-flex terms.

#### FIN-069: Company cash after the US$100.0m use
- **Finding:** Cash left after the US$100.0m use is US$60.4m on June 30 figures. That falls to US$26.4m after the WSEA advance unwinds, and to -US$30.7m if payables return to 78 days. This is before H2 2026 operating cash, which is not projected here.
- **Evidence:**
  - 160.4 - 100.0 = 60.4. Less 34.0 = 26.4. Less 57.1 = -30.7.
  - For reference only, H2 2025 free cash flow = (86.6 - 34.9) - (29.5 - 13.8) = 51.7 - 15.7 = 36.0.
  - No revolver appears in the files.
- **Source:** `balance_sheet.csv` Cash; `cash_flow.csv` FY2025 and H1_2025 operating cash flow and capex; FIN-048, FIN-058.
- **Severity:** High.
- **Confidence:** Medium. This is a projection.
- **Deal impact:** Financing and liquidity after closing.
- **Cross-check:** Revolver availability in the new financing; minimum-cash covenant.

### Positive or mitigating points
- The pension accounting deficit (446.0 - 291.5 = 154.5) ties exactly to the FY2025 balance sheet. There is no hidden second pension liability, and the bridge uses the termination shortfall without double counting (FIN-054).
- The FY2025 Nimbus fair-value gain of US$6.5m sits in other income, which is correctly excluded from EBITDA. LTM other income is 0.0 (`adjusted_ebitda_reconciliation.csv`).
- Utility Programs excluding WSEA grew 12.5% in FY2025, from 40.0 to 45.0 (FIN-047).
- Subscription gross revenue retention is steady at 93.0% to 93.4%. Insights revenue rose from 3.1 (FY2025) to 11.8 (H1 2026) (`kpis.csv`).
- The company's peso sensitivity reconciles to the data pack (280.2 x 10% = 28.0), which supports the reliability of that disclosure (FIN-052).
- Long-term debt fell from 470.0 to 420.0 between FY2024 and Q2 2026.

### Gaps and questions for management
1. H1 2026 revenue by customer, especially WSEA and Gulf Horizon. Also the Gulf Horizon receivable at June 30, 2026.
2. Utility Programs and WSEA contribution margins, segment EBITDA, and whether program incentives are passed through in revenue.
3. Customer split of the 7.0 baseline utility prepayment.
4. Thermostat revenue within Devices, and Devices revenue for FY2019 to FY2021.
5. Average MXN rates for H1 and H2 2025, and the hedging plan.
6. AP owed to Ensamble at June 30, 2026; Ensamble's loan status and cross-default terms.
7. NEO severance recomputed at US$24.50; transaction fees.
8. Annuity buyout quotes and timing for the pension; interest accrued on the IRS NOPA.
9. TLB pricing, the lender EBITDA definition, and revolver capacity.
10. For the lead: the components of Case B (115.4), so the peso (FIN-052) and Gulf Horizon (FIN-049) adjustments are not double counted.

The source files are in `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/financials/`, and the deal brief is `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/deal-brief.md`.
