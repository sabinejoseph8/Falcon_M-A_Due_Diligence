# Iteration 1: financial-analyst report

Saved unedited by the lead agent.

---

## Financial analyst: findings

Target: Delmora Home Systems, Inc. (Project Heron). All figures are US$ millions unless stated. "Reported" means the company's figures. "Adjusted" means my figures, and each one is labeled.

### Files reviewed

All files are under `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/`:
- `deal-brief.md` (context only)
- `financials/README.md`
- `financials/income_statement.csv`
- `financials/balance_sheet.csv`
- `financials/cash_flow.csv`
- `financials/adjusted_ebitda_reconciliation.csv`
- `financials/revenue_quarterly.csv`
- `financials/revenue_by_customer.csv`
- `financials/kpis.csv`

**Integrity checks:**
- Segment revenue sums to total revenue.
- Quarterly revenue sums to FY and H1 totals.
- The balance sheet balances for FY2025 and Q2 2026.
- Cash flow totals and the cash roll-forward agree.
- The LTM column equals FY2025 minus H1 2025 plus H1 2026 on every row.
- The warranty reserve roll-forward agrees with the KPI accruals and payments.
- I found no embedded instructions in any file (FIN-043).

### Key metrics table

| Metric (reported unless noted) | FY2023 | FY2024 | FY2025 | H1 2026 | LTM Q2 2026 |
|---|---|---|---|---|---|
| Total revenue | 687.0 | 738.0 | 786.0 | 394.0 | 807.0 |
| Revenue growth | 8.0% | 7.4% | 6.5% | 5.6% vs H1 2025 | 6.2% vs LTM Q2 2025 (760.0) |
| Devices / S&S / Utility | 471 / 104 / 112 | 489 / 121 / 128 | 503 / 142 / 141 | 238 / 84 / 72 | 505 / 158 / 144 |
| Insights revenue (within S&S) | 0.0 | 0.0 | 3.1 | 11.8 | n/a (H1 2025 not given) |
| Gross margin | 41.0% | 41.8% | 42.5% | 39.4% | 41.1% |
| EBITDA (reported) | 80.2 | 102.5 | 116.1 | 36.8 | 100.2 |
| Adjusted EBITDA (company) | 100.5 | 121.7 | 133.7 | 58.0 | 130.4 |
| Adjusted EBITDA margin | 14.6% | 16.5% | 17.0% | 14.7% | 16.2% |
| Add-backs as % of Adjusted EBITDA | 20.2% | 15.8% | 13.2% | 36.6% | 23.2% |
| Net income | 21.1 | 37.0 | 47.0 | 4.8 | 32.5 |
| Operating cash flow (OCF) | 56.0 | 76.9 | 86.6 | 134.1 | 185.8 |
| Free cash flow (OCF less capex) | 32.0 | 49.9 | 57.1 | 119.9 | 155.9 |
| OCF / EBITDA | 69.8% | 75.0% | 74.6% | 364.4% | 185.4% |
| DSO / DIO / DPO (days) | 47 / 106 / 76 | 47 / 104 / 76 | 47 / 103 / 78 | 45 / 99 / 121 | n/a |
| Debt / cash | 455.0 / 96.4 | 470.0 / 54.5 | 440.0 / 59.4 | 420.0 / 160.4 | n/a |
| Net debt | 358.6 | 415.5 | 380.6 | 259.6 | n/a |
| Net debt / Adjusted EBITDA | 3.57x | 3.41x | 2.85x | n/a | 1.99x |
| Adjusted EBITDA / interest | 4.67x | 5.29x | 6.08x | 5.47x | 6.09x |
| Pension obligation | 171.0 | 162.0 | 154.5 | 151.0 | n/a |
| Top customer (WSEA) share | n/a | 11.9% | 12.2% | n/a | n/a |
| Care subscribers (thousands) / gross retention | 1,020 / 92.8% | 1,180 / 93.1% | 1,370 / 93.4% | 1,465 / 93.0% | n/a |
| Warranty claim rate (annualized) | 1.9% | 2.2% | 3.4% | 4.7% | n/a |
| **My adjusted LTM Adjusted EBITDA (FIN-001, Case B)** | | | | | **115.4** |

### How the key numbers are calculated

- **LTM figures:** FY2025 minus H1 2025 plus H1 2026.
  - Revenue: 786.0 - 373.0 + 394.0 = 807.0. The quarters agree: 196 + 217 + 186 + 208 = 807.0.
  - OCF: 86.6 - 34.9 + 134.1 = 185.8.
  - Capex: 29.5 - 13.8 + 14.2 = 29.9.
- **Prior LTM revenue:** 738.0 - (169 + 182) + 373.0 = 760.0.
- **Gross margin:** H1 2026 = 155.2 / 394.0 = 39.4%. LTM gross profit = 334.1 - 157.8 + 155.2 = 331.5, and 331.5 / 807.0 = 41.1%.
- **Days metrics (formulas in README):**
  - DSO H1 2026 = 99.0 / 394.0 x 181 = 45.5. DSO FY2025 = 100.2 / 786.0 x 365 = 46.5.
  - DPO H1 2026 = 160.0 / 238.8 x 181 = 121.3. DPO FY2025 = 96.0 / 451.9 x 365 = 77.5.
  - DIO H1 2026 = 130.4 / 238.8 x 181 = 98.8. DIO FY2025 = 127.0 / 451.9 x 365 = 102.6.
- **H1 2026 interest cover:** 58.0 / 10.6 = 5.47x.

### Findings

#### FIN-001: LTM Adjusted EBITDA of US$130.4m overstates the earnings base
- **Finding:** I removed two add-backs that look like operating costs and normalized the warranty accrual. On that basis LTM Adjusted EBITDA is about 115.4, not 130.4 (11.5% lower). Reported EBITDA, before any add-backs, is 100.2.
- **Evidence:**
  - Company bridge: EBITDA 100.2 + SBC 17.6 + acquisition costs 3.4 + other non-recurring 9.2 = 130.4.
  - Case A (high confidence): 130.4 - Calder legal fees 3.2 (FIN-004) - Aura field action 6.0 (FIN-002) = 121.2.
  - Case B (medium confidence): 121.2 - warranty normalization 5.8 (FIN-003) = 115.4.
  - Case C: 115.4 - SBC 17.6 (FIN-006) = 97.8.
  - Value effect at the deal multiple of 11.84x (1,543.4 / 130.4):
    - Case A: -9.2 x 11.84 = -108.9, which is 7.1% of EV.
    - Case B: -15.0 x 11.84 = -177.5, which is 11.5% of EV.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, rows 7 to 14, column LTM_Q2_2026; `financials/kpis.csv`, rows 10 to 12
- **Severity:** Critical. Test met: more than 10% of value. Case B lowers EV at the deal multiple by 177.5, or 11.5% of 1,543.4.
- **Confidence:** Medium. The arithmetic is exact, but the 5.8 warranty normalization is an estimate. Case A alone (7.1%) would be High severity.
- **Deal impact:** Valuation and financing (the debt is sized on 130.4).
- **Cross-check:** Check the 10-Q for the Adjusted EBITDA definition and the Aura and Calder disclosures. Check litigation records for the expected duration of the Calder case.

#### FIN-002: Aura field action (US$6.0m add-back) is a product quality cost, not an isolated one-off
- **Finding:** The 6.0 repair kit program is added back as non-recurring. However, warranty claims more than doubled over the same period, so the field action is part of a wider quality trend. Also, only 0.9 of the 6.0 has been spent, so the claim that the matter is "contained" is untested.
- **Evidence:**
  - Add-back of 6.0 in H1 2026.
  - Field action reserve at Q2 2026 is 5.1 (cash flow change +5.1). Spent so far: 6.0 - 5.1 = 0.9.
  - Warranty claim rate: 2.2% (FY2024), 3.4% (FY2025), 4.7% (H1 2026). 4.7 / 2.2 = 2.14x.
  - The add-back equals 4.6% of LTM Adjusted EBITDA (6.0 / 130.4).
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, row 13; `financials/balance_sheet.csv`, row 17; `financials/cash_flow.csv`, row 13; `financials/kpis.csv`, row 9
- **Severity:** High
- **Confidence:** High on the numbers. Medium on whether costs will recur.
- **Deal impact:** Valuation; post-closing (indemnity or escrow for product issues).
- **Cross-check:** Check SEC filings for the field action scope and number of units, news and regulator (CPSC) material for recall risk, and litigation records for Aura product claims.

#### FIN-003: Warranty accrual cut while warranty claims rise
- **Finding:** Warranty expense fell from 15.0 to 9.6 in FY2025, even though the claim rate rose from 2.2% to 3.4%. Claims paid have been higher than accruals for six quarters. This flatters FY2025 gross margin and Adjusted EBITDA.
- **Evidence:**
  - Accrual as % of device revenue: FY2024 15.0 / 489 = 3.07%; FY2025 9.6 / 503 = 1.91%; H1 2026 4.1 / 238 = 1.72%.
  - Claims paid minus accrued: FY2025 12.5 - 9.6 = 2.9; H1 2026 4.9 - 4.1 = 0.8.
  - Reserve fell from 15.1 to 11.4. Reserve as % of trailing device revenue fell from 3.1% to 2.3%.
  - At the FY2024 rate, FY2025 warranty expense would be 503 x 3.07% = 15.4, or 5.8 more than booked. H1 2026 would be 238 x 3.07% = 7.3, or 3.2 more.
  - Range for FY2025 understatement: 2.9 (cash basis) to 5.8 (FY2024 rate). The claim rate has since doubled, so the FY2024 rate may itself be too low.
  - FY2025 gross margin with 5.8 more cost: (334.1 - 5.8) / 786.0 = 41.8%, against 42.5% reported. FY2025 Adjusted EBITDA growth would be 5.1% (127.9 / 121.7), against 9.9% reported.
- **Source:** `financials/kpis.csv`, rows 9 to 12; `financials/balance_sheet.csv`, row 16; `financials/cash_flow.csv`, row 12
- **Severity:** High
- **Confidence:** Medium. The normalization rate is my assumption. H1 2025 warranty expense is not given, so LTM cannot be rebuilt exactly.
- **Deal impact:** Valuation; post-closing reserve true-up.
- **Cross-check:** Check the 10-K warranty footnote and critical accounting estimates, and any auditor comment. Check news for Aura failure reports.

#### FIN-004: Calder Institute litigation legal fees (US$3.2m) added back
- **Finding:** Legal fees for an active lawsuit are an ongoing operating cost until the case ends. They are not normally an EBITDA add-back.
- **Evidence:** Add-back of 3.2 in H1 2026. G&A rose from 28.5 to 37.5 (+9.0, +31.6%). Calder Institute is not a listed customer in `revenue_by_customer.csv`.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, row 14; `financials/income_statement.csv`, row 10
- **Severity:** Medium (3.2 x 11.84 = 37.9, or 2.5% of EV)
- **Confidence:** High
- **Deal impact:** Valuation. The underlying case may affect IC Question 3 (technology and data rights).
- **Cross-check:** Litigation analyst: the nature of the claim (IP or data?), its stage and the damages sought.

#### FIN-005: "Acquisition, integration and transaction-related costs" recur every period
- **Finding:** This add-back appears in FY2024 (4.2), FY2025 (1.1) and H1 2026 (2.9), even though there were no acquisitions in FY2025 or 2026. The H1 2026 amount is probably costs of the strategic review (inference). That would be a legitimate add-back, but the breakdown is not given.
- **Evidence:** LTM 3.4, or 2.6% of LTM Adjusted EBITDA. Cash flow row "Acquisitions" is 0.0 in FY2025 and H1 2026.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, row 9; `financials/cash_flow.csv`, row 20
- **Severity:** Medium
- **Confidence:** Medium. The cause is inferred.
- **Deal impact:** Valuation (minor)
- **Cross-check:** Check the 10-Q for the composition of the H1 2026 costs and the date the Strategic Review Committee was formed.

#### FIN-006: Stock-based compensation is the largest add-back
- **Finding:** SBC of 17.6 is 13.5% of LTM Adjusted EBITDA. It is a recurring economic cost that has grown every year.
- **Evidence:** SBC: 13.5 (FY2023), 15.0 (FY2024), 16.5 (FY2025), 9.1 (H1 2026, against 8.0 in H1 2025). 17.6 / 130.4 = 13.5%.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, row 8
- **Severity:** Medium. Adding back SBC is market practice, but under private ownership it will be replaced by a cash or equity management incentive plan.
- **Confidence:** High
- **Deal impact:** Valuation; check how lenders define EBITDA.
- **Cross-check:** Check the proxy statement for equity plans and treatment of awards on a change of control.

#### FIN-007: Reno distribution center restructuring (FY2023, US$6.8m) is a one-off outside the LTM period
- **Finding:** This is a single restructuring charge in FY2023. It has not recurred and does not affect LTM.
- **Evidence:** 6.8 in FY2023 and 0.0 in every other period.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, row 12
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** The 410 unionized Reno employees (FIN-040).

#### FIN-008: Nimbus earn-out remeasurement gain correctly excluded from EBITDA
- **Finding:** The FY2025 non-cash gain of 6.5 is booked in other income, which sits below operating income, and is reversed in operating cash flow. It does not inflate EBITDA. This risk is neutralized by the accounting treatment.
- **Evidence:**
  - Earn-out liability fell from 14.5 to 8.0 (-6.5). Cash flow row "Change in fair value of contingent consideration" is -6.5.
  - EBITDA = operating income + D&A: 80.6 + 35.5 = 116.1, which matches the reconciliation.
- **Source:** `financials/balance_sheet.csv`, row 20; `financials/cash_flow.csv`, row 6; `financials/README.md` notes
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None to EBITDA. See FIN-024 for what the gain implies about Insights.
- **Cross-check:** Check the 10-K fair value footnote.

#### FIN-009: H1 2026 operating cash flow of US$134.1m is mostly working capital timing
- **Finding:** 98.0 of the 134.1 (73.1%) comes from two unusual inflows: the payables stretch (64.0) and utility customer prepayments (34.0). Excluding them, OCF is 36.1, close to H1 2025's 34.9. The thesis claim ("more than all of FY2025") is true as arithmetic but does not show underlying cash generation.
- **Evidence:**
  - Bridge: net income 4.8 + D&A 18.6 + SBC 9.1 + deferred tax -1.5 = 31.0.
  - Working capital and other items = +103.1, made up of: AR +1.2, inventory -3.4, prepaids -1.2, AP +64.0, accrued liabilities +3.5, warranty -0.8, field action +5.1, deferred revenue +3.5, utility prepayments +34.0, pension -3.5, other +0.7.
  - Total: 31.0 + 103.1 = 134.1.
  - If the two items had moved as they did in H1 2025 (AP +3.5, prepayments +0.2): 134.1 - 64.0 + 3.5 - 34.0 + 0.2 = 39.8.
  - Underlying H1 FCF: 36.1 - 14.2 = 21.9, against 119.9 reported.
- **Source:** `financials/cash_flow.csv`, rows 2 to 19, column H1_2026 (and H1_2025 for comparison)
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation and financing. It also undermines the "falls quickly" deleveraging claim.
- **Cross-check:** Check the 10-Q MD&A liquidity discussion and supplier news (payment delays, supplier disputes).

#### FIN-010: Payables stretched from 78 to 121 days
- **Finding:** Accounts payable rose from 96.0 to 160.0 in six months, against cost of revenue that grew only 11.0%. About 57.1 of payables is above the normal level and should be treated as debt-like.
- **Evidence:**
  - DPO = 160.0 / 238.8 x 181 = 121.3 days, against 77.5 at FY2025 and 76 at FY2024 and FY2023.
  - Normal AP at 78 days = 78 / 181 x 238.8 = 102.9. Excess = 160.0 - 102.9 = 57.1.
  - H1 cost of revenue growth: 238.8 / 215.2 = +11.0%.
- **Source:** `financials/balance_sheet.csv`, row 14; `financials/income_statement.csv`, row 6; `financials/kpis.csv`, row 15
- **Severity:** High
- **Confidence:** High on the size. Medium on whether 78 days is the right "normal" level.
- **Deal impact:** Financing and valuation (working capital peg, debt-like item).
- **Cross-check:** Check the 10-Q for supplier financing or reverse factoring programs, and news on Monterrey suppliers. Ask for AP aging.

#### FIN-011: Utility program customer prepayments jumped from US$7.0m to US$41.0m
- **Finding:** Prepayments rose 34.0 in H1 2026, against +0.2 in H1 2025 and +0.5 a year before that. This cash is owed back as services or refunds, and its cause is unexplained. It may be linked to the WSEA program before its end-2026 renewal (inference).
- **Evidence:**
  - Prepayments of 41.0 cover 41.0 / (72.0 / 181) = 103 days of Utility revenue, against 7.0 / 141.0 x 365 = 18.1 days at FY2025.
  - Excess over FY2025: 34.0.
- **Source:** `financials/balance_sheet.csv`, row 19; `financials/cash_flow.csv`, row 15
- **Severity:** High
- **Confidence:** High on the numbers. Low on the cause.
- **Deal impact:** Financing (it inflates the cash used to fund the deal) and debt-like adjustment.
- **Cross-check:** Check the 10-Q for program terms, and SEC filings and news on WSEA renewal terms and any refund obligation.

#### FIN-012: Pittock pension obligation of US$151.0m is not in the deal model's net debt
- **Finding:** The balance sheet shows a pension and postretirement obligation of 151.0. The deal brief makes no debt-like adjustment for it. The company has paid 7.5 to 9.0 a year above pension expense, which is a cash cost outside EBITDA.
- **Evidence:**
  - Obligation: 171.0, 162.0, 154.5, 151.0.
  - Contributions above expense: 8.0 (FY2023), 9.0 (FY2024), 7.5 (FY2025), 3.5 (H1 2026).
  - Pre-tax, 151.0 is 9.8% of EV and 11.8% of equity value (151.0 / 1,283.8). Taxed at the brief's 23%: 151.0 x 0.77 = 116.3, which is 7.5% of EV and 9.1% of equity.
  - Per share: 151.0 / 52.4 = US$2.88.
- **Source:** `financials/balance_sheet.csv`, row 23; `financials/cash_flow.csv`, row 16
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation (net debt). Possible financing impact if lenders count it.
- **Cross-check:** Check the 10-K pension footnote (funded status, discount rate, PBGC exposure on a leveraged buyout) and whether management's "no ERISA minimum before 2029" claim holds.

#### FIN-013: Adjusted net debt bridge (all debt-like items)
- **Finding:** The model's net debt of 259.6 leaves out about 270.1 of debt-like items, more than doubling net debt to 529.7. At an unchanged EV, this reduces equity value by US$5.15 per share.
- **Evidence (US$m):**

  | Item | Amount |
  |---|---|
  | Reported net debt (420.0 - 160.4) | 259.6 |
  | Nimbus earn-out (already in the model per the brief, not in this figure) | 8.0 |
  | Pension, pre-tax (FIN-012) | 151.0 |
  | Excess payables (FIN-010) | 57.1 |
  | Excess utility prepayments (FIN-011) | 34.0 |
  | Uncertain tax positions (FIN-035) | 14.2 |
  | Environmental reserve (FIN-036) | 8.7 |
  | Field action reserve (FIN-002) | 5.1 |
  | **Additional items** (151.0 + 57.1 + 34.0 + 14.2 + 8.7 + 5.1) | **270.1** |

  - 270.1 is 17.5% of EV and 21.0% of equity value. 270.1 / 52.4 = US$5.15 per share.
  - Operating leases of 41.0 are excluded from the bridge (FIN-037).
- **Source:** `financials/balance_sheet.csv`, rows 2, 14, 17, 19 to 25, column Q2_2026
- **Severity:** Critical. Test met: more than 10% of value (270.1 = 17.5% of EV).
- **Confidence:** Medium. The amounts are exact, but whether each item is debt-like (and whether to tax-effect the pension) is a judgment.
- **Deal impact:** Valuation (price and the working capital peg)
- **Cross-check:** Check SEC filings on the pension, tax and environmental reserves, and litigation records for environmental sites (Pittock).

#### FIN-014: The plan to use US$100.0m of Delmora cash relies on cash that is owed to others
- **Finding:** Of the 160.4 cash at June 30, 2026, about 91.1 comes from stretched payables and utility prepayments. Underlying cash is about 69.3, which is less than the 100.0 the financing plan uses.
- **Evidence:**
  - Underlying cash: 160.4 - 57.1 - 34.0 = 69.3.
  - After the 100.0 is used: 160.4 - 100.0 = 60.4.
  - If payables and prepayments normalize, the business needs 91.1, leaving a shortfall of 60.4 - 91.1 = -30.7 (projection).
  - Revolver availability is not in the data.
- **Source:** `financials/balance_sheet.csv`, rows 2, 14, 19; `deal-brief.md` section 1
- **Severity:** High
- **Confidence:** Medium. The projection depends on the timing of normalization.
- **Deal impact:** Financing and closing (sources and uses). This becomes Critical only if a revolver or liquidity gap appears before closing, which the data does not show.
- **Cross-check:** Check the 10-Q for the revolver size and draws, and the TLB commitment for a minimum cash condition.

#### FIN-015: Leverage at close is higher than the 6.9x headline
- **Finding:** The US$900.0m TLB is 6.9x the company's Adjusted EBITDA, but 7.8x my adjusted base and 9.0x reported EBITDA. Including the pension, it is above 9x.
- **Evidence (900.0 divided by):**
  - Company Adjusted EBITDA 130.4: 6.90x
  - Case A 121.2: 7.43x
  - Case B 115.4: 7.80x
  - Reported EBITDA 100.2: 8.98x
  - Case C 97.8: 9.20x
  - Case B including the pension: (900.0 + 151.0) / 115.4 = 9.11x
  - Net of the 60.4 cash left after closing: 839.6 / 130.4 = 6.44x
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, rows 7 and 11; `deal-brief.md` section 1
- **Severity:** High. This is a financing structure issue, not a pre-closing default.
- **Confidence:** High on the arithmetic. Medium on Case B.
- **Deal impact:** Financing (sizing, covenants), valuation
- **Cross-check:** Check how the TLB commitment letter defines EBITDA and whether it allows add-backs.

#### FIN-016: Valuation multiples on adjusted earnings
- **Finding:** The offer is 11.8x the company's Adjusted EBITDA but 13.4x my adjusted base and 15.4x reported EBITDA. Applying both the earnings adjustments and the net debt adjustments at the deal multiple gives an implied value per share below the unaffected price (projection).
- **Evidence:**
  - Recomputed deal terms: 52.4 x 24.50 = 1,283.8 equity; plus net debt 259.6 = 1,543.4 EV; / 130.4 = 11.84x. These confirm the brief.
  - EV / 115.4 = 13.37x. EV / 100.2 = 15.40x.
  - Illustration (projection): 11.84x x 115.4 = 1,365.9 EV, less 259.6 net debt, less 270.1 debt-like items = 836.2 equity. 836.2 / 52.4 = US$15.96 per share, against the US$18.70 unaffected price and the US$24.50 offer.
- **Source:** As FIN-001 and FIN-013; `deal-brief.md` section 1
- **Severity:** High. The underlying Critical items are FIN-001 and FIN-013.
- **Confidence:** Medium
- **Deal impact:** Valuation
- **Cross-check:** Compare peer trading multiples, and check SEC filings for basic versus diluted share counts.

#### FIN-017: Gross margin is falling, which tests the 42% assumption for 2027
- **Finding:** Gross margin fell from 42.3% (H1 2025) to 39.4% (H1 2026). LTM gross margin is 41.1%. FY2025's 42.5% peak benefited from a weak peso and a low warranty accrual.
- **Evidence:**
  - H1 2025: 157.8 / 373.0 = 42.3%. H1 2026: 155.2 / 394.0 = 39.4%.
  - H1 2026 excluding the field action, if it was booked in cost of revenue (the line is not given): 161.2 / 394.0 = 40.9%.
  - Gap to 42% on LTM revenue of 807.0: 1.1 to 2.6 points, or 8.9 to 21.0 of gross profit.
  - FY2025 margin with normalized warranty: 41.8% (FIN-003).
- **Source:** `financials/income_statement.csv`, rows 5 to 7; `financials/kpis.csv`, row 8
- **Severity:** High
- **Confidence:** High on history. Medium on the forward view.
- **Deal impact:** Valuation (model assumption)
- **Cross-check:** Check the 10-Q gross margin commentary and news on tariffs and costs.

#### FIN-018: The Mexican peso cost exposure is unhedged
- **Finding:** 63% of cost of revenue is in pesos. Hedge coverage fell from 72% to 0%. The peso strengthened from 19.4 to 17.2 per US$ (11.3%), which I estimate cost about 17.1 of H1 2026 gross profit.
- **Evidence:**
  - Peso-denominated H1 2026 cost: 238.8 x 63% = 150.4. At the FY2025 average rate it would have cost 150.4 x 17.2 / 19.4 = 133.4. Headwind: 17.1 (estimate; the H1 2025 rate is not given).
  - Sensitivity: LTM cost of revenue 475.5 (451.9 - 215.2 + 238.8) x 63% = 299.6. Each 1% peso appreciation costs about 3.0 a year, or 2.3% of LTM Adjusted EBITDA.
  - H2 2025 run-rate (projection): 236.7 x 62% = 146.8 of H2 2025 peso costs. If the peso stays at 17.2, the extra cost is 146.8 x (19.4 / 17.2 - 1) = 18.8. This is not in the LTM figure.
- **Source:** `financials/kpis.csv`, rows 16 to 18; `financials/income_statement.csv`, row 6
- **Severity:** High
- **Confidence:** Medium. Period-average rates are used and hedge gains or losses are unknown.
- **Deal impact:** Valuation; post-closing hedging policy.
- **Cross-check:** Check the 10-K market risk section (Item 7A) for why hedging stopped, and news on the peso.

#### FIN-019: Revenue growth is slowing, and Insights drives over half of H1 2026 growth
- **Finding:** Annual growth slowed from 8.0% to 7.4% to 6.5%, and H1 2026 grew 5.6%. Q1 2026 grew 4.5%, the weakest quarter in the dataset. Insights provided 11.8 of the 21.0 of H1 growth (56.2%), assuming Insights revenue was zero in H1 2025 (it launched in September 2025). Excluding Insights, H1 growth is 2.5%.
- **Evidence:**
  - Quarterly year-on-year growth: Q1 2025 5.3%, Q2 2025 7.1%, Q3 2025 6.5%, Q4 2025 6.9%, Q1 2026 4.5% (186 / 178), Q2 2026 6.7% (208 / 195).
  - Excluding Insights: (394.0 - 11.8) / 373.0 = +2.5%.
  - Devices growth: 4.2%, 3.8%, 2.9%, then 0.8% in H1 2026 (238 / 236).
- **Source:** `financials/revenue_quarterly.csv`; `financials/income_statement.csv`, rows 2 to 5; `financials/kpis.csv`, row 7
- **Severity:** Medium
- **Confidence:** High. The assumption about H1 2025 Insights revenue is stated.
- **Deal impact:** Valuation
- **Cross-check:** Check 10-Q segment commentary.

#### FIN-020: Gulf Horizon Trading FZE accounts for most of FY2025 growth
- **Finding:** Gulf Horizon (rank 4) grew from 4.1 to 38.6 (+841%) and supplied 71.9% of FY2025 revenue growth. Excluding it, FY2025 growth was 1.8%. This single distributor is the "Middle East growth" in the thesis. If it buys devices (inference), Devices revenue from all other customers fell 4.2%.
- **Evidence:**
  - Increase: 38.6 - 4.1 = 34.5. 34.5 / 48.0 = 71.9% of FY2025 growth.
  - Growth excluding Gulf Horizon: (786.0 - 38.6) / (738.0 - 4.1) = 747.4 / 733.9 = +1.8%. Also excluding Insights: 744.3 / 733.9 = +1.4%.
  - Devices excluding Gulf Horizon: 464.4 / 484.9 = -4.2% (inference).
  - Share of revenue: 4.9%.
  - No regional revenue split is in the data.
- **Source:** `financials/revenue_by_customer.csv`, row 5; `financials/income_statement.csv`, row 2
- **Severity:** High
- **Confidence:** High on the numbers. Low on the cause (real demand, channel loading or re-export).
- **Deal impact:** Valuation and post-closing. Possible trade or export-control exposure for IC Question 4.
- **Cross-check:** Check news and SEC filings on Gulf Horizon (ownership, end markets, sanctions or transshipment issues), its receivables and sell-through, and its H1 2026 revenue.

#### FIN-021: Western States Energy Alliance concentration and the end-2026 renewal
- **Finding:** WSEA is the largest customer: rank 1, 96.0 in FY2025 (12.2% of revenue), up from 88.0 (11.9%) in FY2024. If all of its revenue is in Utility Programs (inference), it is 68.1% of that segment. The thesis assumes renewal on similar terms at the end of 2026.
- **Evidence:**
  - 96.0 / 786.0 = 12.2%. 96.0 / 141.0 = 68.1% of Utility Programs. WSEA plus Cascadia: 119.5 / 141.0 = 84.8%.
  - Illustrative impact of non-renewal (inference): 96.0 x 42.5% FY2025 gross margin = 40.8 of gross profit, or 31% of LTM Adjusted EBITDA.
- **Source:** `financials/revenue_by_customer.csv`, rows 2 and 6; `financials/income_statement.csv`, row 4
- **Severity:** High
- **Confidence:** High on the concentration. Low on renewal (no contract data).
- **Deal impact:** Valuation; possible closing condition (renewal signed) or price adjustment.
- **Cross-check:** Check news, SEC filings and public agency records on the WSEA tender or renewal status, and any link to the prepayment surge (FIN-011).

#### FIN-022: Utility Programs growth is below the 6% model assumption
- **Finding:** Segment growth slowed from 16.7% to 14.3% to 10.2%, then to 4.3% in H1 2026, which is below the 6% the model assumes.
- **Evidence:** 112 / 96 = +16.7%; 128 / 112 = +14.3%; 141 / 128 = +10.2%; H1 72 / 69 = +4.3%.
- **Source:** `financials/income_statement.csv`, row 4
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation
- **Cross-check:** Check SEC segment commentary and news on utility program budgets.

#### FIN-023: Insights trajectory against the US$60.0m 2028 target and US$310m of EV
- **Finding:** Insights is growing fast, but its H1 2026 run-rate of 23.6 would have to grow about 59% a year to reach 60.0 by 2028. The thesis puts 20.1% of EV on it.
- **Evidence:**
  - Run-rate: 11.8 x 2 = 23.6. Required growth: (60.0 / 23.6)^(1/2) = 1.594, or 59.4% a year.
  - EV share: 310 / 1,543.4 = 20.1%. That is 13.1x run-rate revenue (310 / 23.6).
  - Enrolled households: 2.3m of a 7.1m installed base (32.4%).
  - Insights margin is not given.
- **Source:** `financials/kpis.csv`, rows 2, 6, 7; `deal-brief.md` section 3
- **Severity:** Medium (financial view only; data rights may raise it)
- **Confidence:** Medium
- **Deal impact:** Valuation
- **Cross-check:** Check SEC filings, litigation records (Calder?) and news on data consent and licensing rights. See FIN-024.

#### FIN-024: The Nimbus earn-out was cut by 44.8%, which conflicts with Insights optimism
- **Finding:** In FY2025 the company cut the expected earn-out for Nimbus, the business that became Insights, from 14.5 to 8.0. That means management lowered its own forecast of Nimbus milestones in the same year the deal thesis treats Insights as the growth engine.
- **Evidence:** 6.5 / 14.5 = 44.8% reduction. Nimbus consideration: 98.0 cash + 14.5 earn-out = 112.5. Goodwill rose 62.0 in FY2024 (436 to 498).
- **Source:** `financials/balance_sheet.csv`, rows 8 and 20; `financials/cash_flow.csv`, rows 6 and 20
- **Severity:** Medium
- **Confidence:** High on the numbers. Medium on what they mean.
- **Deal impact:** Valuation; goodwill (FIN-034)
- **Cross-check:** Check the 10-K for the earn-out milestones and fair value inputs.

#### FIN-025: Delmora Care revenue growth is slowing and implied revenue per subscriber is falling
- **Finding:** Subscriptions & Services revenue excluding Insights grew 14.8% in FY2025 but only 6.2% in H1 2026, even though subscribers grew 16.1%. Implied revenue per subscriber is falling (inference: the segment may include other services).
- **Evidence:**
  - Excluding Insights: FY2025 (142.0 - 3.1) / 121.0 = +14.8%. H1 2026 (84.0 - 11.8) / 68.0 = +6.2%.
  - Implied annual revenue per subscriber:
    - FY2024: 121.0 / avg subscribers 1,100k = US$110.0
    - FY2025: 138.9 / 1,275k = US$108.9
    - H1 2026 annualized: 144.4 / 1,417.5k = US$101.9
  - Subscribers: 1,180k to 1,370k (+16.1%).
- **Source:** `financials/income_statement.csv`, row 3; `financials/kpis.csv`, rows 4 and 7
- **Severity:** Medium
- **Confidence:** Medium. H1 2025 Insights revenue is assumed to be zero, and seasonality is unknown.
- **Deal impact:** Valuation
- **Cross-check:** Check SEC filings for pricing changes or promotions.

#### FIN-026: Subscription gross retention is stable at about 93%
- **Finding:** Gross revenue retention of 92.8% to 93.4%, then 93.0% in H1 2026, supports the durability of Care revenue. The small dip in 2026 is worth watching.
- **Evidence:** Retention: 92.8 (FY2023), 93.1 (FY2024), 93.4 (FY2025), 93.0 (H1 2026).
- **Source:** `financials/kpis.csv`, row 5
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Mitigant
- **Cross-check:** Check how the 10-K defines retention.

#### FIN-027: Overall customer concentration
- **Finding:** The top 3 customers are a steady 31.4% of revenue. The top 8 rose from 39.6% to 44.1%, driven by Gulf Horizon. Revenue from customers outside the top 8 fell 1.3%.
- **Evidence:**
  - Top 3: 246.5 / 786.0 = 31.4% (FY2024: 231.5 / 738.0 = 31.4%).
  - Top 8: 346.3 / 786.0 = 44.1% (FY2024: 292.3 / 738.0 = 39.6%).
  - All other customers: 445.7 to 439.7 (-1.3%).
  - The data lists 8 customers, so a top-10 figure is not available.
- **Source:** `financials/revenue_by_customer.csv`, all rows
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Context for FIN-020 and FIN-021
- **Cross-check:** Check 10-K concentration disclosure.

#### FIN-028: Bellmark Mutual Insurance is a new customer
- **Finding:** Bellmark (rank 8) had 1.9 of FY2025 revenue and none in FY2024. An insurer buying from Delmora may be an Insights data licensee (inference). If so, it is 61% of FY2025 Insights revenue (1.9 / 3.1).
- **Evidence:** 0.0 to 1.9 (0.2% of revenue).
- **Source:** `financials/revenue_by_customer.csv`, row 9
- **Severity:** Low
- **Confidence:** Low on the link to Insights.
- **Deal impact:** Relevant to data rights (IC Question 3)
- **Cross-check:** Check news and litigation records for Bellmark and consumer data sharing.

#### FIN-029: Ranks of the other named customers
- **Finding:** These are the remaining named customers, listed for the lead agent's lookups. Northway is the only one that declined.
- **Evidence (FY2025, rank):**
  - 2: HomeCrest Stores, 84.0 (10.7%), +1.8%
  - 3: Parcelline Marketplace, 66.5 (8.5%), +9.0%
  - 5: Cascadia Power & Light, 23.5 (3.0%), +11.9%
  - 6: Vierhaus Elektro GmbH, 19.0 (2.4%), +4.4%
  - 7: Northway Electronics, 16.8 (2.1%), -4.0%
  - Any party not in this file (for example Calder Institute or Ensamble Norte) is not a listed customer.
- **Source:** `financials/revenue_by_customer.csv`, rows 3, 4, 6 to 8
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None directly
- **Cross-check:** Check news on retailer relationships.

#### FIN-030: DSO is stable to lower, and the data does not cover factoring
- **Finding:** DSO has held at about 47 days and fell to 45 in H1 2026, which released about 3.3 of cash. The financial data has no factoring or receivables-sale disclosure, so factoring cannot be ruled out.
- **Evidence:**
  - DSO: 46.8, 46.8, 46.5, then 45.5 days.
  - Receivables at 47 days would be 47 / 181 x 394.0 = 102.3, against 99.0 actual. Difference: 3.3.
  - The allowance for credit losses is not given.
- **Source:** `financials/balance_sheet.csv`, row 3; `financials/kpis.csv`, row 13
- **Severity:** Low
- **Confidence:** Medium, because factoring data is missing.
- **Deal impact:** Working capital
- **Cross-check:** Check the 10-Q for receivables sales or factoring.

#### FIN-031: Inventory days are improving
- **Finding:** DIO fell from 106 to 99 days. Inventory rose only 3.4 in H1 2026.
- **Evidence:** DIO: 105.4 (FY2023), 104.1 (FY2024), 102.6 (FY2025), 98.8 (H1 2026).
- **Source:** `financials/balance_sheet.csv`, row 4; `financials/kpis.csv`, row 14
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** Check for slow-moving Aura inventory linked to the field action.

#### FIN-032: Deferred revenue growth is consistent with subscription growth
- **Finding:** Deferred revenue rose from 41.0 to 55.5, steady growth of 3.5 to 6.0 a period. This movement is normal.
- **Evidence:** 41.0, 46.0, 52.0, 55.5.
- **Source:** `financials/balance_sheet.csv`, row 18; `financials/cash_flow.csv`, row 14
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** None needed.

#### FIN-033: G&A rose US$9.0m in H1 2026
- **Finding:** Most of the increase is probably the Calder legal fees (3.2) and transaction costs (2.9), both added back (inference). About 2.9 is unexplained.
- **Evidence:** G&A: 28.5 to 37.5 (+9.0). 9.0 - 3.2 - 2.9 = 2.9.
- **Source:** `financials/income_statement.csv`, row 10; `financials/adjusted_ebitda_reconciliation.csv`, rows 9 and 14
- **Severity:** Low
- **Confidence:** Medium. The line where each item is booked is not given.
- **Deal impact:** Valuation (minor)
- **Cross-check:** Request the G&A breakdown.

#### FIN-034: Goodwill and intangibles are 48% of total assets, and there is a Nimbus impairment indicator
- **Finding:** Goodwill (498.0) and intangibles (111.0) total 609.0, which is 48.0% of assets and 2.4x book equity. The impairment test date is not in the financial data. The 44.8% earn-out cut is an indicator for the Nimbus/Insights reporting unit.
- **Evidence:**
  - 609.0 / 1,267.8 = 48.0%. 609.0 / 256.8 = 2.37x.
  - Market capitalization at the unaffected price: 18.70 x 52.4m diluted shares = 979.9, against book equity of 256.8. The company as a whole is well above book value; this is not tested by reporting unit.
- **Source:** `financials/balance_sheet.csv`, rows 8, 9, 13, 28
- **Severity:** Medium
- **Confidence:** Medium
- **Deal impact:** Post-closing accounting
- **Cross-check:** Check the 10-K impairment test date and reporting units, and compare share price moves since that date.

#### FIN-035: Liability for uncertain tax positions is growing
- **Finding:** The liability rose from 11.0 to 14.2. It is a debt-like item; I included it in FIN-013.
- **Evidence:** 11.0, 12.6, 13.8, 14.2.
- **Source:** `financials/balance_sheet.csv`, row 24
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Net debt; tax indemnity
- **Cross-check:** Check the 10-K tax footnote and open audits.

#### FIN-036: Environmental remediation reserve of US$8.7m
- **Finding:** The reserve is declining slowly (10.2 to 8.7). It is probably related to Pittock (inference) and is a debt-like item; I included it in FIN-013.
- **Evidence:** 10.2, 9.6, 9.0, 8.7.
- **Source:** `financials/balance_sheet.csv`, row 25
- **Severity:** Low
- **Confidence:** High on the amount
- **Deal impact:** Net debt
- **Cross-check:** Check litigation and regulatory records for sites and the adequacy of the estimate.

#### FIN-037: Operating lease liabilities of US$41.0m
- **Finding:** The lease liability is stable. By convention it is excluded from net debt when EBITDA is struck after rent; I excluded it from FIN-013.
- **Evidence:** 41.0, 44.0, 42.5, 41.0.
- **Source:** `financials/balance_sheet.csv`, row 22
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Depends on the lenders' definition
- **Cross-check:** Check the TLB definitions.

#### FIN-038: Ensamble Norte equity-method investment
- **Finding:** Delmora holds a 20.4 equity-method stake in Ensamble Norte. The name suggests a Mexican assembly partner (inference), which could make it a related-party supplier.
- **Evidence:** 18.0, 19.2, 20.1, 20.4.
- **Source:** `financials/balance_sheet.csv`, row 10
- **Severity:** Low
- **Confidence:** Low on the nature of the relationship
- **Deal impact:** Possible related-party or supply dependence
- **Cross-check:** Check SEC related-party and supplier disclosures.

#### FIN-039: Field action reserve versus "fully reserved"
- **Finding:** The reserve is adequate only if the 6.0 estimate is right. The rising claim rate (FIN-003) puts the estimate in doubt. This is a separate topic from the add-back in FIN-002.
- **Evidence:** 6.0 charged, 0.9 used, 5.1 remaining at Q2 2026.
- **Source:** `financials/balance_sheet.csv`, row 17
- **Severity:** Medium
- **Confidence:** Medium
- **Deal impact:** Post-closing; specific indemnity
- **Cross-check:** Check SEC filings for the unit count and kit cost.

#### FIN-040: Headcount and the Reno union
- **Finding:** Headcount grew 2.9% in FY2025 and 2.4% in H1 2026, in line with revenue. 410 Reno employees are under collective bargaining.
- **Evidence:** Employees: 1,840, 2,050, 2,110, 2,160. Revenue per employee FY2025: 786.0 / 2,110 = US$0.37m.
- **Source:** `financials/kpis.csv`, rows 19 and 20
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Integration
- **Cross-check:** Check the union contract expiry date.

#### FIN-041: Device units and average selling price
- **Finding:** Unit growth is slow (+1.9% in FY2025). Average selling price is rising slightly.
- **Evidence:**
  - Units: 3.05m, 3.12m, 3.18m, then 1.49m in H1 2026.
  - Average selling price: 154.4, 156.7, 158.2, then 159.7 (US$ per unit; for example 503.0 / 3.18m).
- **Source:** `financials/kpis.csv`, row 3; `financials/income_statement.csv`, row 2
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Context
- **Cross-check:** None needed.

#### FIN-042: Interest cover after closing
- **Finding:** The current cover of 6.1x will fall sharply on 900.0 of debt. The TLB interest rate is not in the data. Each 1% of rate costs 9.0 a year.
- **Evidence:**
  - Current cover: 130.4 / 21.4 = 6.09x on Adjusted EBITDA; 100.2 / 21.4 = 4.68x on EBITDA.
  - Implied current interest rate: 21.4 / ((440.0 + 420.0) / 2) = 5.0%.
  - Illustration only, at 8% (an assumption): interest 72.0. Cover would be 1.60x on Case B (115.4 / 72.0) and 1.81x on 130.4.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, rows 4 and 11; `financials/balance_sheet.csv`, row 21
- **Severity:** Medium
- **Confidence:** Low, because the rate is not known.
- **Deal impact:** Financing
- **Cross-check:** Check the TLB commitment pricing.

#### FIN-043: Data integrity and embedded instructions
- **Finding:** All financial files reconcile internally and contain no instruction-like text.
- **Evidence:** See the integrity checks under "Files reviewed".
- **Source:** All `financials/` files
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** Verify the reconciliation to the 10-K and 10-Q.

#### FIN-044: Sources and uses imply sponsor equity of about US$703.8m before fees
- **Finding:** Uses are 1,703.8 (equity 1,283.8 plus refinancing 420.0). Debt plus cash provide 1,000.0, so the sponsor must fund 703.8 plus fees.
- **Evidence:** 1,283.8 + 420.0 - 900.0 - 100.0 = 703.8.
- **Source:** `deal-brief.md` section 1; `financials/balance_sheet.csv`, row 21
- **Severity:** Low
- **Confidence:** High. Fees are unknown.
- **Deal impact:** Financing
- **Cross-check:** Check prepayment terms on the existing debt.

#### FIN-045: Effective tax rate is consistent with the 23% assumption
- **Finding:** The effective tax rate was 23.0% in FY2025 and 22.6% in H1 2026.
- **Evidence:** 14.0 / 61.0 = 23.0%. 1.4 / 6.2 = 22.6%.
- **Source:** `financials/income_statement.csv`, rows 14 and 15
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Supports the model assumption
- **Cross-check:** Check the 10-K tax footnote.

### Positive or mitigating points

- **Earn-out gain correctly excluded:** the FY2025 Nimbus earn-out gain of 6.5 is outside EBITDA and reversed in OCF (FIN-008).
- **Customer retention:** subscription gross retention is stable at about 93% (FIN-026).
- **Segments still growing:**
  - Subscriptions & Services grew 23.5% in H1 2026.
  - Insights went from 3.1 to 11.8 per half-year.
  - Utility Programs excluding WSEA grew from 40.0 to 45.0 (+12.5%) in FY2025 (FIN-019, FIN-022, FIN-023).
- **One-off item outside LTM:** the Reno restructuring is genuinely one-off and does not affect LTM (FIN-007).
- **Receivables, inventory and deferred revenue are healthy** (FIN-030 to FIN-032).
- **Debt reduced:** debt fell from 470.0 to 420.0 since FY2024. Pre-deal leverage is 2.0x (259.6 / 130.4).
- **Tax rate assumption is supported** (FIN-045).
- **Not in the financial data:** debt maturity schedules and supply or price protection contracts.

### Gaps and questions for management

1. H1 2025 Insights revenue and warranty expense, so LTM can be rebuilt exactly.
2. The cost line where the Aura 6.0 and Calder 3.2 are booked; affected unit count and the cost per kit.
3. Composition of the 2.9 H1 2026 "acquisition, integration and transaction" costs.
4. AP aging, supplier terms, and any supply chain finance program. Why DPO reached 121 days.
5. Contract terms behind the utility prepayments of 41.0 (which customer, and refund obligations). WSEA renewal status.
6. Gulf Horizon: end markets, sell-through, receivables, H1 2026 revenue, and export compliance checks.
7. Revenue by region and segment gross margins (neither is in the data).
8. Revolver size and usage, debt maturities, and any receivables factoring.
9. Pension funding status, ERISA minimum contribution projections, and PBGC considerations.
10. Why hedging stopped after FY2024 and the current hedge policy. Hedge gains and losses in FY2025.
11. Nimbus earn-out milestones and the assumptions behind the 6.5 cut. Goodwill impairment test date and reporting units.
12. Allowance for credit losses, the Ensamble Norte relationship, and Insights margin and contract terms.
13. Pricing of the TLB commitment and its EBITDA definition.
