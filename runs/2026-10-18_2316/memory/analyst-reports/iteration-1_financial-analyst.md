<!-- Iteration 1, financial-analyst. Full report as returned by the analyst, saved unedited by the lead agent. -->

## Financial analyst: findings

### Files reviewed

All read in full, read-only:
- `data/deal-brief.md` (context)
- `data/financials/README.md`
- `data/financials/income_statement.csv`
- `data/financials/revenue_quarterly.csv`
- `data/financials/balance_sheet.csv`
- `data/financials/cash_flow.csv`
- `data/financials/adjusted_ebitda_reconciliation.csv`
- `data/financials/revenue_by_customer.csv`
- `data/financials/kpis.csv`

No file contains text that tries to instruct the agents. No injection attempt was found.

**Integrity checks (all pass):**
- Quarterly revenue sums to the annual and H1 totals. FY2024: 96.2 + 102.8 + 106.1 + 116.6 = 421.7. FY2025: 108.9 + 117.6 + 121.4 + 154.4 = 502.3. H1 2026: 109.7 + 112.9 = 222.6.
- Assets equal liabilities plus equity in all four balance sheets. June 30, 2026: 353.3 + 92.0 = 445.3.
- The cash flow ties to the balance sheet cash: 41.6 - 7.7 = 33.9.
- The working capital lines in the cash flow match the balance sheet changes. FY2025 AR: 118.9 - 73.4 = 45.5.
- The equity roll-forward ties. FY2025: 74.3 + 18.6 + 17.2 - 13.3 - 4.1 + 0.8 = 93.5.
- The Adjusted EBITDA reconciliation rebuilds exactly for every period.
- LTM Q2 2026 = FY2025 + H1 2026 - H1 2025.
- LTM revenue = 502.3 + 222.6 - 226.5 = 498.4. This also equals Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026 = 121.4 + 154.4 + 109.7 + 112.9 = 498.4.

### Key metrics table

Reported figures are as the company presents them. Analyst-adjusted figures are labeled. US$ millions unless stated.

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 / LTM Q2 2026 |
|---|---|---|---|---|
| Total revenue | 368.9 | 421.7 | 502.3 | H1: 222.6 / LTM: 498.4 |
| Revenue growth (YoY) | 18.1% | 14.3% | 19.1% | H1: -1.7% |
| Hardware growth | 15.1% | 11.0% | 15.1% | H1: -12.9% |
| FieldOS software growth | 29.1% | 25.9% | 27.1% | H1: 14.6% |
| Services growth | 16.7% | 11.6% | 23.4% | H1: 14.4% |
| Gross margin | 40.1% | 40.8% | 41.1% | H1: 38.0% (H1 2025: 40.8%) |
| EBITDA (reported) | 42.2 | 52.3 | 64.1 | H1: 10.4 / LTM: 48.2 |
| Adjusted EBITDA (company) | 60.4 | 74.8 | 98.8 | H1: 29.9 / LTM: 89.7 |
| Adjusted EBITDA margin (company) | 16.4% | 17.7% | 19.7% | H1: 13.4% / LTM: 18.0% |
| Add-backs as % of Adjusted EBITDA | 30.1% | 30.1% | 35.1% | H1: 65.2% / LTM: 46.3% |
| Analyst-adjusted EBITDA (FIN-03) | n/a | n/a | 86.8 | LTM: 76.7 |
| Net income | 11.5 | 15.2 | 18.6 | H1: -8.9 / LTM: 4.4 |
| Operating cash flow | 30.8 | 40.8 | 9.7 | H1: -4.2 / LTM: -6.9 |
| Free cash flow | 16.2 | 24.6 | -10.1 | H1: -13.0 / LTM: -26.4 |
| OCF / EBITDA | 73.0% | 78.0% | 15.1% | LTM: -14.3% |
| DSO (year-end AR / revenue x 365) | 60.4 | 63.5 | 86.4 | Jun 30 on LTM: 76.3 |
| Allowance / gross AR | 3.9% | 3.8% | 2.1% | 3.2% |
| Contract assets | 8.1 | 10.2 | 24.7 | 19.5 |
| Inventory | 55.2 | 63.9 | 71.3 | 84.0 |
| Cash | 54.8 | 48.3 | 41.6 | 33.9 |
| Total debt (revolver + term loan) | 120.0 | 200.0 | 220.0 | 227.5 |
| Net debt | 65.2 | 151.7 | 178.4 | 193.6 |
| Net debt / Adjusted EBITDA (company) | 1.08x | 2.03x | 1.81x | LTM: 2.16x |
| Net debt / EBITDA (reported) | 1.55x | 2.90x | 2.78x | LTM: 4.02x |
| Adjusted EBITDA / interest | 8.16x | 7.63x | 7.26x | LTM: 6.02x |
| Revolver drawn | 0.0 | 10.0 | 35.0 | 45.0 |
| Top customer share (Norvale) | n/a | 28.0% | 31.1% | n/a |
| Top 10 share | n/a | 59.2% | 61.5% | n/a |
| FieldOS ARR | 86.0 | 109.5 | 139.2 | 146.8 |
| Software net revenue retention | 121% | 119% | 118% | 111% |
| Hardware backlog | 142.0 | 168.0 | 131.0 | 118.0 |
| Full-time employees | 1,180 | 1,390 | 1,452 | 1,405 |

### Findings

#### FIN-01: Deal model's FY2026E Adjusted EBITDA of $118.0m no longer matches current trading
- **Finding:** The deal model pays 11.5x a FY2026E Adjusted EBITDA of $118.0m. LTM Adjusted EBITDA on the company's own definition is $89.7m, and H1 2026 fell 23.3% year on year. At the same 11.5x multiple, the LTM figure supports about $17.35 per share, not $24.00.
- **Evidence:**
  - Equity value = 24.00 x 48.3 = 1,159.2.
  - Net debt at June 30, 2026 = (45.0 + 182.5) - 33.9 = 193.6.
  - EV = 1,159.2 + 193.6 = 1,352.8. EV / 118.0 = 11.46x, so the brief's 11.5x is confirmed.
  - EV against current trading:

    | EBITDA basis | Amount | EV / EBITDA |
    |---|---|---|
    | FY2025 Adjusted EBITDA (company) | 98.8 | 13.7x |
    | LTM Adjusted EBITDA (company) | 89.7 | 15.1x |
    | LTM analyst-adjusted (FIN-03) | 76.7 | 17.6x |
    | H1 2026 Adjusted EBITDA annualized (29.9 x 2) | 59.8 | 22.6x |
    | LTM reported EBITDA | 48.2 | 28.1x |

  - H1 Adjusted EBITDA: 29.9 vs 39.0 = -23.3%.
  - What the management case needs in H2 2026 (projection):
    - Revenue of 560.0 - 222.6 = 337.4. That is +22.3% on H2 2025 (121.4 + 154.4 = 275.8), after H1 was -1.7%.
    - Adjusted EBITDA of 118.0 - 29.9 = 88.1, a 26.1% H2 margin (88.1 / 337.4). H2 2025 was 21.7% ((98.8 - 39.0) / 275.8).
  - Price implied at 11.5x:
    - On LTM 89.7: 11.5 x 89.7 = 1,031.6; less 193.6 = 838.0; divided by 48.3 = $17.35.
    - On analyst-adjusted LTM 76.7: 882.1 - 193.6 = 688.5; divided by 48.3 = $14.25.
  - Size of the gap: (118.0 - 89.7) x 11.5 = 325.5 of EV, which is 24.1% of the 1,352.8 EV.
- **Source:** `adjusted_ebitda_reconciliation.csv` rows "Adjusted EBITDA (company definition)", "EBITDA" (FY2025, H1_2025, H1_2026, LTM_Q2_2026); `balance_sheet.csv` Q2_2026 rows "Cash and cash equivalents", "Revolving credit facility", "Term loan"; `revenue_quarterly.csv` Q3 2025 and Q4 2025; `data/deal-brief.md`.
- **Severity:** Critical. Test met: more than 10% of value. On the deal's own 11.5x multiple, the gap between the management case and LTM Adjusted EBITDA is 325.5 of EV (24.1%).
- **Confidence:** High for the recomputed multiples and the LTM figures. Medium for the H2 2026 requirement, which is a projection.
- **Deal impact:** Valuation.
- **Cross-check:** Look in the 10-Qs and 8-K earnings releases for any update or withdrawal of FY2026 guidance after the March 2026 investor day. Check news for analyst estimate cuts.

#### FIN-02: FY2025 growth depends on one quarter (Q4 2025) and one customer (Norvale)
- **Finding:** Q4 2025 revenue jumped 32.4% YoY. The other 2025 quarters grew about 14%, and revenue then fell 29.0% quarter on quarter in Q1 2026. Norvale alone accounts for 47.3% of FY2025 revenue growth. Excluding the Q4 spike, or excluding Norvale, underlying FY2025 growth is about 14.0%, not the 19.1% reported. H1 2026 revenue is down 1.7%.
- **Evidence:**
  - YoY growth by quarter: Q1 2025 +13.2%, Q2 +14.4%, Q3 +14.4%, Q4 +32.4% (154.4 / 116.6), Q1 2026 +0.7%, Q2 2026 -4.0% (112.9 / 117.6).
  - Quarter on quarter: Q4 2025 vs Q3 2025 = +27.2% (154.4 / 121.4), against +9.9% a year earlier. Q1 2026 vs Q4 2025 = -29.0%.
  - Q4 2025 delivered 154.4 - 116.6 = 37.8 of the 80.6 annual increase, or 46.9%.
  - Estimated Q4 excess (estimate). Q1 to Q3 2025 grew 347.9 / 305.1 = 14.0%. At that rate Q4 2025 would be 116.6 x 1.1403 = 133.0, so the excess is 154.4 - 133.0 = 21.4. FY2025 without it = 480.9, which is +14.0%.
  - Norvale grew 156.2 - 118.1 = 38.1, which is 47.3% of the 80.6 increase. Revenue excluding Norvale: 303.6 to 346.1 = +14.0%.
  - Segments in H1 2026: hardware -12.9% (116.9 vs 134.2), software +14.6%, services +14.4%.
  - The FY2024 Lumora acquisition (85.0 cash) means some reported growth may be inorganic. Lumora's revenue is not disclosed.
- **Source:** `revenue_quarterly.csv` all rows; `income_statement.csv` revenue rows; `revenue_by_customer.csv` Norvale row and Total row; `cash_flow.csv` row "Acquisition of Lumora Vision".
- **Severity:** High
- **Confidence:** High for the reported growth rates. Medium for the 21.4 excess, which assumes Q4 should have grown at the Q1 to Q3 rate.
- **Deal impact:** Valuation, and the quality of the base for forecasts.
- **Cross-check:** Look in the 10-K and Q4 2025 earnings materials for a large Q4 order, bill-and-hold sales or revenue recognized on contract assets (see FIN-04). If the lead agent has a one-off revenue amount from a filing, it can replace my 21.4 estimate. Check news on the Norvale relationship and any Q4 2025 Norvale rollout. Ask for Lumora's revenue contribution.

#### FIN-03: Adjusted EBITDA relies more and more on add-backs, and some are normal operating costs
- **Finding:** Add-backs are 65.2% of H1 2026 Adjusted EBITDA and 46.3% of LTM, up from 30.1% in FY2023 and FY2024. Restructuring has been added back every year since FY2022 and keeps growing. "Customer implementation delays" is a cost of delivery. Removing these two items gives analyst-adjusted LTM EBITDA of $76.7m, against $89.7m reported.
- **Evidence:**
  - Add-backs (Adjusted EBITDA minus EBITDA):

    | Period | Add-backs | Calculation | Share of Adjusted EBITDA |
    |---|---|---|---|
    | FY2023 | 18.2 | 60.4 - 42.2 | 30.1% |
    | FY2024 | 22.5 | 74.8 - 52.3 | 30.1% |
    | FY2025 | 34.7 | 98.8 - 64.1 | 35.1% |
    | H1 2026 | 19.5 | 29.9 - 10.4 | 65.2% |
    | LTM | 41.5 | 89.7 - 48.2 | 46.3% |

  - Restructuring: 3.1, 4.6, 5.2, 7.9 (FY2022 to FY2025) and 9.7 LTM. It recurs every year, totaling 20.8 over FY2022 to FY2025.
  - "Other non-recurring items" appear in every year from FY2022 and rise: 1.2, 2.0, 3.4, 9.6, then 14.0 LTM.
  - Vantor patent litigation costs have run for three periods: 0.8, 2.1, then 3.0 in H1 2026 alone. This is ongoing defense of core IP.
  - Stock-based compensation is a real cost. It is 17.4% of FY2025 Adjusted EBITDA (17.2 / 98.8).
  - Analyst-adjusted EBITDA (company Adjusted EBITDA less restructuring and customer implementation delays; SBC still added back so the figures compare with the company's):

    | Period | Calculation | Analyst-adjusted | Margin |
    |---|---|---|---|
    | FY2025 | 98.8 - 7.9 - 4.1 | 86.8 | 17.3% |
    | LTM | 89.7 - 9.7 - 3.3 | 76.7 | 15.4% |
    | H1 2026 | 29.9 - 4.4 - 0.0 | 25.5 | n/a |

  - Sensitivity (estimate, Low confidence). Also removing gross profit on the estimated Q4 excess (21.4 x 41.1% = 8.8) gives 67.9 LTM, which is 19.9x EV.
- **Source:** `adjusted_ebitda_reconciliation.csv` all rows and the Detail rows; `income_statement.csv` row "Restructuring and other charges".
- **Severity:** High
- **Confidence:** High for the add-back shares. Medium for the analyst adjustments, which are a judgment on which items recur.
- **Deal impact:** Valuation. This basis should be used for any EBITDA-linked price mechanism or covenant.
- **Cross-check:** Read the 10-K description of the restructuring programs (one program or several?). Check court records on the Vantor case for its status and how long it may last. A quality of earnings report has not been commissioned (README), so commission one.

#### FIN-04: Receivables and contract assets ballooned in FY2025, and reserves fell
- **Finding:** DSO rose from 63.5 to 86.4 days in FY2025. Contract assets grew 142%. Receivables grew 62.0% while revenue grew 19.1%. The allowance for credit losses fell to 2.1% of gross receivables, from 3.8%. Together with the Q4 spike (FIN-02), this pattern is consistent with aggressive Q4 revenue recognition (inference).
- **Evidence:**
  - DSO = AR / revenue x 365:
    - FY2023: 61.0 / 368.9 x 365 = 60.4 days
    - FY2024: 73.4 / 421.7 x 365 = 63.5 days
    - FY2025: 118.9 / 502.3 x 365 = 86.4 days
    - June 30, 2026: 104.2 / 498.4 (LTM) x 365 = 76.3 days. On Q2 2026 annualized revenue it is 104.2 / 451.6 x 365 = 84.2 days.
  - DSO including contract assets: FY2024 = 83.6 / 421.7 x 365 = 72.4 days. FY2025 = 143.6 / 502.3 x 365 = 104.3 days.
  - Contract assets: 10.2 to 24.7, up 2.42x. They rose from 2.4% to 4.9% of revenue.
  - Allowance / gross AR: 3.9%, 3.8%, 2.1% (2.6 / 121.5), then 3.2% (3.4 / 107.6). At the FY2024 rate, the FY2025 allowance would have been 121.5 x 3.80% = 4.6, so FY2025 was under-reserved by about 2.0 (estimate). The allowance then rose to 3.4 in H1 2026.
- **Source:** `balance_sheet.csv` rows "Accounts receivable net", "Contract assets (unbilled receivables)", "Memo: Accounts receivable gross", "Memo: Allowance for credit losses"; `income_statement.csv` "Total revenue".
- **Severity:** High
- **Confidence:** High for the ratios. Low for the revenue recognition inference.
- **Deal impact:** Valuation, a possible need for an indemnity, and post-closing collections.
- **Cross-check:** Check the 10-K revenue recognition policy and any change in it, and the auditor's critical audit matters. Ask for the FY2025 aged receivables, Norvale's receivable balance, and how much of the 24.7 contract assets relates to Q4 2025 contracts. The auditor transition in FY2025 (FIN-08) increases the importance of this check.

#### FIN-05: Cash conversion collapsed and free cash flow is negative; FY2025 buybacks were funded with revolver debt
- **Finding:** Operating cash flow was 15.1% of EBITDA in FY2025, against 73% to 78% before. It was negative for the LTM. LTM free cash flow is -$26.4m. In FY2025 the company bought back $13.3m of stock while free cash flow was -$10.1m and it drew $25.0m on the revolver.
- **Evidence:**

  | Ratio | FY2023 | FY2024 | FY2025 |
  |---|---|---|---|
  | OCF / EBITDA | 30.8 / 42.2 = 73.0% | 40.8 / 52.3 = 78.0% | 9.7 / 64.1 = 15.1% |
  | OCF / net income | 2.68x | 2.68x | 9.7 / 18.6 = 0.52x |

  - FY2025 OCF / Adjusted EBITDA = 9.7%.
  - LTM OCF = 9.7 - 4.2 - 12.4 = -6.9. LTM capex = 19.8 + 8.8 - 9.1 = 19.5. LTM FCF = -26.4, which matches -10.1 - 13.0 - 3.3.
  - FY2025 working capital outflow was -51.7, of which AR was -45.5 and contract assets -14.5.
  - H1 2026 working capital outflow was -15.4. AR collections of +14.7 were more than offset by inventory (-12.7) and payables and other (-22.6).
- **Source:** `cash_flow.csv` all rows; `adjusted_ebitda_reconciliation.csv` EBITDA row.
- **Severity:** High
- **Confidence:** High. Calculated directly.
- **Deal impact:** Valuation (the cash-based value is below the EBITDA-based value) and financing.
- **Cross-check:** Look for the board's buyback authorization and any statements on capital allocation in filings. Check news on management guidance about cash flow.

#### FIN-06: Leverage is rising, cash is falling and the revolver is drawn more each period; covenant headroom cannot be computed
- **Finding:** Net debt rose to $193.6m. That is 4.02x LTM reported EBITDA, or 2.16x on the company's Adjusted EBITDA. Cash fell for three straight years to $33.9m, and the revolver draw rose from $0 to $45.0m. At the H1 2026 cash outflow rate, cash lasts about 11.5 months without further revolver draws (projection).
- **Evidence:**
  - Total debt: 120.0, 200.0, 220.0, 227.5. Net debt: 65.2, 151.7, 178.4, 193.6.
  - Leverage at June 30, 2026 on LTM figures:
    - Total debt / LTM EBITDA = 227.5 / 48.2 = 4.72x
    - Net debt / LTM EBITDA = 193.6 / 48.2 = 4.02x
    - Net debt / LTM Adjusted EBITDA = 193.6 / 89.7 = 2.16x
    - Net debt / analyst-adjusted LTM = 193.6 / 76.7 = 2.52x
  - Interest cover (LTM): Adjusted EBITDA / interest = 89.7 / 14.9 = 6.02x. EBITDA / interest = 48.2 / 14.9 = 3.23x. EBIT / interest = 20.3 / 14.9 = 1.36x, where LTM EBIT = 37.3 - 3.7 - 13.3 = 20.3.
  - Runway (projection). H1 2026 cash fell 7.7 even after a 10.0 revolver draw, so the outflow before revolver draws was 17.7. That is FCF of -13.0, term loan amortization of -2.5 and other items of -2.2. At that rate, 33.9 / 17.7 x 6 = 11.5 months.
  - Covenant definition: none is available in `data/financials/`. I computed ratios on both the company's Adjusted EBITDA and reported EBITDA. Which one applies decides whether headroom is comfortable (about 2.2x) or tight (about 4.0x). Revolver capacity is also not disclosed.
- **Source:** `balance_sheet.csv` rows for cash, revolver and term loan (all periods); `cash_flow.csv` H1_2026 column; `adjusted_ebitda_reconciliation.csv` LTM column; `income_statement.csv` "Operating income (loss)".
- **Severity:** High. Under the calibration rule, a debt problem cured by refinancing at closing is High. It would become Critical only if a covenant breach or liquidity shortfall occurs before closing, and that cannot be tested without the covenant terms.
- **Confidence:** High for the ratios. Medium for the runway, which assumes the H1 burn rate continues.
- **Deal impact:** Financing and closing risk.
- **Cross-check:** The lead agent should send the covenant definitions (leverage and interest cover tests, EBITDA definition, add-back caps), the revolver commitment and the maturity dates from the 10-K or credit agreement. Check whether any waiver or amendment was filed on an 8-K.

#### FIN-07: Norvale concentration is high and rising
- **Finding:** Norvale Retail Group is 31.1% of FY2025 revenue, up from 28.0%. The top 3 customers are 45.1% and the top 10 are 61.5%, up from 59.2%. Losing or repricing Norvale would remove nearly a third of revenue.
- **Evidence:**
  - Top 10 FY2025 = 308.8 / 502.3 = 61.5%. Top 10 FY2024 = 249.6 / 421.7 = 59.2%.
  - Top 3 FY2025 = 226.3 / 502.3 = 45.1%.
  - Norvale grew 32.3% (156.2 / 118.1). All other customers grew 12.4% (193.5 / 172.1).
  - Full customer list for name matching (US$m; shares are of total revenue; rank is FY2025, and FY2024 order is the same by amount):

  | Rank FY2025 | Customer | FY2024 rev (share) | FY2025 rev (share) | YoY |
  |---|---|---|---|---|
  | 1 | Norvale Retail Group | 118.1 (28.0%) | 156.2 (31.1%) | +32.3% |
  | 2 | Quillon Logistics | 36.0 (8.5%) | 41.2 (8.2%) | +14.4% |
  | 3 | Ardent Parcel Co. | 25.3 (6.0%) | 28.9 (5.8%) | +14.2% |
  | 4 | Pinecrest Distribution | 16.2 (3.8%) | 17.4 (3.5%) | +7.4% |
  | 5 | Harbor & Vine Grocers | 12.4 (2.9%) | 15.1 (3.0%) | +21.8% |
  | 6 | Meridale Pharmacy Supply | 10.1 (2.4%) | 12.6 (2.5%) | +24.8% |
  | 7 | Cobalt Home Goods | 9.6 (2.3%) | 11.0 (2.2%) | +14.6% |
  | 8 | Westfork Apparel | 8.8 (2.1%) | 9.8 (2.0%) | +11.4% |
  | 9 | Sunreach Auto Parts | 7.0 (1.7%) | 8.7 (1.7%) | +24.3% |
  | 10 | Tidewell Foods | 6.1 (1.4%) | 7.9 (1.6%) | +29.5% |
  | n/a | All other customers | 172.1 (40.8%) | 193.5 (38.5%) | +12.4% |
  | n/a | Total | 421.7 | 502.3 | +19.1% |

  - Any named party not in this table (for example Vantor or Lumora) is not a listed top 10 customer.
  - H1 2026 revenue by customer is not provided.
- **Source:** `revenue_by_customer.csv` all rows.
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation and post-closing. A change-of-control consent may be needed for the closing condition.
- **Cross-check:** Look in the 10-K concentration disclosure and the Norvale contract terms (term, change of control, termination for convenience). Check news on Norvale's automation strategy or vendor reviews, and court records for any dispute with Norvale.

#### FIN-08: Several add-backs point to governance and control events
- **Finding:** FY2025 to H1 2026 add-backs include auditor transition costs ($2.3m), an executive search and CFO transition ($2.5m LTM), a cybersecurity incident response ($1.8m, H1 2026) and Vantor patent litigation ($4.1m LTM). Each one is an event the other workstreams should confirm and test for disclosure.
- **Evidence:** In the LTM column, 4.1 + 3.3 + 2.3 + 2.5 + 1.8 = 14.0, which equals "Other non-recurring items". The auditor and CFO changes both happened in the same period as the FY2025 DSO and contract asset build-up (FIN-04).
- **Source:** `adjusted_ebitda_reconciliation.csv` Detail rows, FY2025, H1_2026 and LTM_Q2_2026 columns.
- **Severity:** Medium. I am not raising it on the financial data alone. The SEC and litigation workstreams may raise it.
- **Confidence:** High that the costs exist. The nature of the events is not shown in the financials.
- **Deal impact:** Closing risk and post-closing (controls).
- **Cross-check:** Look for an 8-K Item 4.01 (auditor change and any disagreements), Item 5.02 (CFO departure) and Item 1.05 (cyber incident), and their timing against the events. Check the Vantor docket for the case stage and claimed damages.

#### FIN-09: Margins are compressing, and H1 2026 was an operating loss
- **Finding:** Gross margin fell from 40.8% to 38.0% in H1 2026. Adjusted EBITDA margin fell from 17.2% to 13.4%. Operating income swung from +$13.3m to -$3.7m. G&A rose 22.2%. This supports FIN-01.
- **Evidence:**
  - Gross margin H1 2025: 92.4 / 226.5 = 40.8%. H1 2026: 84.6 / 222.6 = 38.0%.
  - Annual gross margin was 40.1%, 40.8% and 41.1%.
  - Reported EBITDA margin: FY2025 12.8%, H1 2026 4.7% (10.4 / 222.6), LTM 9.7%.
  - G&A: 16.2 to 19.8 (+22.2%). Opex: 79.1 to 88.3 (+11.6%) while revenue fell 1.7%.
  - Hardware revenue per robot shipped:
    - FY2024: 261.9 / 3,300 = $79.4k
    - FY2025: 301.4 / 4,300 = $70.1k, which is -11.7%
    - H1 2026: 116.9 / 1,640 = $71.3k
  - This points to price or mix pressure (inference). It assumes hardware revenue tracks units shipped.
- **Source:** `income_statement.csv` H1_2025 and H1_2026 columns; `kpis.csv` "Robots shipped in period".
- **Severity:** Medium (supporting FIN-01)
- **Confidence:** High for the margins. Medium for the per-unit pricing.
- **Deal impact:** Valuation and synergy planning.
- **Cross-check:** Look in the MD&A of the H1 2026 10-Q for explanations of the gross margin. Check news on competitor pricing.

#### FIN-10: Operating KPIs are weakening and contradict the management case
- **Finding:** Net revenue retention fell from 118% to 111%. Hardware backlog is down 29.8% from its FY2024 peak. ARR growth slowed to about 11% annualized. Headcount fell. Implied hardware book-to-bill has been below 1.0 since FY2025.
- **Evidence:**
  - ARR: +27.3% in FY2024, +27.1% in FY2025, then +5.5% in H1 2026 (146.8 / 139.2), about 11.2% annualized. Net new ARR was 7.6 in H1 2026, against 29.7 in FY2025.
  - Net revenue retention: 121%, 119%, 118%, 111%.
  - Backlog: 168.0, then 131.0 (-22.0%), then 118.0 (-9.9%). That is -29.8% from the peak (118.0 / 168.0).
  - Implied hardware bookings = hardware revenue + change in backlog (estimate; assumes no cancellations and that backlog is hardware only):
    - FY2024: 261.9 + 26.0 = 287.9, book-to-bill 1.10
    - FY2025: 301.4 - 37.0 = 264.4, book-to-bill 0.88
    - H1 2026: 116.9 - 13.0 = 103.9, book-to-bill 0.89
  - Robots shipped in H1 2026: 1,640. Annualized that is 3,280, against 4,300 in FY2025 (-23.7%).
  - Headcount: 1,452 to 1,405 (-3.2%).
  - Active customers: +11.3% in FY2025 (276 / 248), then +1.8% in H1 2026 (281 / 276).
  - Total deferred revenue fell from 56.9 to 50.2 (-11.8%) while ARR rose. This may be seasonal billing, which is a question for management.
- **Source:** `kpis.csv` all rows; `income_statement.csv` hardware revenue; `balance_sheet.csv` deferred revenue rows.
- **Severity:** High. Falling backlog and retention directly undercut the 22.3% H2 2026 revenue ramp needed for FY2026E (FIN-01).
- **Confidence:** High for the KPI changes. Medium for bookings and book-to-bill, which are derived.
- **Deal impact:** Valuation.
- **Cross-check:** Check the backlog definition and cancellation policy in the 10-K. Check news for lost deals or customer churn, and whether the investor day presentation relied on a backlog figure.

#### FIN-11: Inventory is building while hardware sales fall
- **Finding:** Inventory rose 17.8% in H1 2026 to $84.0m. Over the same period hardware revenue fell 12.9% and backlog fell 9.9%. Days inventory rose to about 102 days. This creates a risk of obsolescence or write-down.
- **Evidence:**
  - 84.0 / 71.3 = +17.8%.
  - DIO = inventory / cost of revenue x 365:
    - FY2023: 55.2 / 221.0 x 365 = 91.2 days
    - FY2024: 93.4 days
    - FY2025: 71.3 / 296.0 x 365 = 87.9 days
    - June 30, 2026: 84.0 / 299.9 (LTM COGS = 296.0 + 138.0 - 134.1) x 365 = 102.2 days
  - Payables fell 7.6 (46.2 to 38.6), adding to the cash drain.
- **Source:** `balance_sheet.csv` "Inventory", "Accounts payable"; `income_statement.csv` "Cost of revenue"; `kpis.csv` backlog.
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation (net working capital peg) and post-closing.
- **Cross-check:** Ask for the inventory aging and reserves, and whether any product generation changes are coming. Check news for new model launches.

#### FIN-12: Goodwill and intangibles exceed book equity; the impairment test date is not in the data
- **Finding:** Goodwill ($98.4m) plus intangibles ($34.1m) equal $132.5m, which is more than total equity of $92.0m. Tangible equity is negative at -$40.5m. Most of it comes from the FY2024 Lumora deal. The financials do not show the last impairment test date or the share price history.
- **Evidence:**
  - Goodwill rose from 41.0 to 98.4 (+57.4) in FY2024. Intangibles rose from 21.1 to 43.4. Lumora cost 85.0 net of cash acquired.
  - 132.5 is 29.8% of total assets (445.3).
  - Market capitalization at $17.85 = 17.85 x 48.3 = 862.2, against book equity of 92.0. Consolidated headroom looks large, but headroom at the Lumora reporting unit is unknown.
  - Deal premium: 24.00 / 17.85 = +34.5%.
- **Source:** `balance_sheet.csv` "Goodwill", "Intangible assets net", "Total stockholders' equity"; `cash_flow.csv` Lumora row; `data/deal-brief.md`.
- **Severity:** Medium
- **Confidence:** High for the balances. The test date and share price history are missing.
- **Deal impact:** Post-closing (purchase price allocation, possible impairment).
- **Cross-check:** Check the 10-K critical accounting estimates for the impairment test date and the reporting units. Check news or market data for the share price trend since that date. Ask for Lumora's performance against its acquisition case.

#### FIN-13: The diluted share count used for equity value may be understated
- **Finding:** The brief uses 48.3 million shares. That is the H1 2026 weighted-average diluted count, and the H1 2026 period was a loss period. In a loss period, dilutive securities are normally excluded. At $24.00, in-the-money options and RSUs may add shares. This is an inference, because no option or RSU data is provided.
- **Evidence:** `income_statement.csv` "Diluted shares (millions)" H1_2026 = 48.3, and net loss of -8.9 gives EPS of -0.18. Diluted shares have grown every year: 45.2, 46.0, 46.9, 47.8.
- **Source:** `income_statement.csv` rows 18 to 20.
- **Severity:** Low
- **Confidence:** Low. This is directional; the equity award data is missing.
- **Deal impact:** Valuation (equity value per share).
- **Cross-check:** Use the 10-Q cover page share count and the equity award footnote to build a treasury-method fully diluted count at $24.00.

### Positive or mitigating points

- The financial statements are internally consistent. Every total, roll-forward and reconciliation recomputes exactly.
- FieldOS software is still growing: +14.6% in H1 2026 and ARR of $146.8m. It is now 30.3% of revenue (67.5 / 222.6), up from 21.8% in FY2023. Services grew 14.4%.
- Receivables came down from $118.9m to $104.2m in H1 2026 (+$14.7m collected). The allowance was rebuilt to 3.2%.
- The installed base grew to 19,040 robots, which supports recurring software and services revenue.
- Interest cover on the company's Adjusted EBITDA is still 6.0x LTM.
- Market capitalization ($862.2m at $17.85) is far above book equity, so goodwill headroom at the consolidated level looks large.
- Customer concentration outside Norvale is moderate. Customers ranked 2 to 10 grew 7.4% to 29.5% each.

### Gaps and questions for management

1. Covenant definitions (EBITDA definition, add-back caps, leverage and interest cover thresholds), revolver commitment and availability, and maturities. The lead agent should send these from the 10-K or credit agreement so headroom can be tested (FIN-06).
2. The nature of the Q4 2025 revenue spike. Ask for a contract-level bridge, bill-and-hold or contract asset terms, and how much relates to Norvale. Any one-off amount found in filings should replace my estimate (FIN-02, FIN-04).
3. H1 2026 revenue by customer, and Norvale's contract terms (term, change of control, termination rights) (FIN-07).
4. Lumora's revenue and EBITDA contribution in FY2024 to FY2026, to show organic growth (FIN-02, FIN-12).
5. Details of each restructuring program, and what the "customer implementation delays" costs were (FIN-03).
6. Aged receivables, the policy for contract assets, and the inventory aging and reserves (FIN-04, FIN-11).
7. An updated FY2026 forecast and the H2 2026 pipeline that supports +22.3% H2 growth (FIN-01).
8. The date and results of the last goodwill impairment test, and the reporting units (FIN-12).
9. A fully diluted share count at $24.00 (FIN-13).
10. The backlog definition, cancellations and bookings data, and why deferred revenue fell in H1 2026 (FIN-10).
11. Minor: in FY2025 the cash flow line "Change in payables accrued liabilities deferred revenue and other" (+15.7) does not match the balance sheet movement in those lines (about +21.7 net of prepaids). Ask for the bridge.
12. The deal team has not received a quality of earnings report. Commissioning one is recommended.