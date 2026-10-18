## Financial analyst: findings

### Files reviewed

- `data/deal-brief.md`: deal terms ($24.00 per share, 48.3M diluted shares, about $1,159M equity value, 34% premium to $17.85), the March 2026 management case (FY2026E revenue $560.0M, Adjusted EBITDA $118.0M), "about 11.5x" EV / FY2026E Adjusted EBITDA on June 30, 2026 net debt.
- `data/financials/README.md`: units and periods. It notes that no quality of earnings (QoE) report has been received.
- `data/financials/income_statement.csv`: FY2022 to FY2025, H1 2025, H1 2026.
- `data/financials/revenue_quarterly.csv`: Q1 2024 to Q2 2026.
- `data/financials/balance_sheet.csv`: Dec 31, 2023, 2024, 2025 and Jun 30, 2026.
- `data/financials/cash_flow.csv`: FY2023 to FY2025, H1 2025, H1 2026. The H1 2025 working capital components are blank; only the total of -13.7 is given.
- `data/financials/adjusted_ebitda_reconciliation.csv`: FY2022 to FY2025, H1 2025, H1 2026, LTM Q2 2026.
- `data/financials/revenue_by_customer.csv`: top 10 customers, FY2024 and FY2025.
- `data/financials/kpis.csv`: FY2023 to Jun 30, 2026.

**Integrity checks (all pass):**
- Segment revenue sums to the total in every period, and the quarters sum to FY2024, FY2025, H1 2025 and H1 2026.
- Income statement subtotals recompute. Balance sheets balance, and net AR = gross AR - allowance.
- Operating, investing and financing cash flows recompute. Cash roll-forwards tie to the balance sheet.
- Term loan, revolver and equity roll-forwards tie to the cash flows.
- EBITDA, Adjusted EBITDA, margins and every LTM figure in the reconciliation recompute exactly.
- The lead agent supplied no facts from other sources for this task.

**Conventions:**
- US$ millions unless stated.
- LTM Q2 2026 = FY2025 - H1 2025 + H1 2026.
- "EBITDA" = the company's EBITDA line before add-backs (operating income + D&A).
- "Company Adj EBITDA" = Adjusted EBITDA as the company reports it.
- "Diligence-adjusted EBITDA" = my adjusted view (see FIN-05).

### Key metrics table

Reported figures are as the company presents them. Diligence-adjusted rows are my figures.

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 or LTM Q2 2026 (basis shown) |
|---|---|---|---|---|
| Total revenue (reported) | 368.9 | 421.7 | 502.3 | H1 222.6; LTM 498.4 |
| Revenue growth YoY | 18.1% | 14.3% | 19.1% | H1 -1.7%; LTM 11.0% |
| Hardware revenue (YoY) | 236.0 (+15.1%) | 261.9 (+11.0%) | 301.4 (+15.1%) | H1 116.9 (-12.9%) |
| Software (FieldOS) revenue (YoY) | 80.4 (+29.1%) | 101.2 (+25.9%) | 128.6 (+27.1%) | H1 67.5 (+14.6%) |
| Services revenue (YoY) | 52.5 (+16.7%) | 58.6 (+11.6%) | 72.3 (+23.4%) | H1 38.2 (+14.4%) |
| Q4 YoY growth / Q4 share of annual growth | n/a | n/a | +32.4% / 46.9% | Q1 2026 +0.7%; Q2 2026 -4.0% |
| Gross margin | 40.1% | 40.8% | 41.1% | H1 38.0% (H1 2025: 40.8%); LTM 39.8% |
| Operating income | 21.3 | 28.8 | 37.3 | H1 -3.7; LTM 20.3 |
| Net income | 11.5 | 15.2 | 18.6 | H1 -8.9; LTM 4.4 |
| EBITDA before add-backs (margin) | 42.2 (11.4%) | 52.3 (12.4%) | 64.1 (12.8%) | H1 10.4 (4.7%); LTM 48.2 (9.7%) |
| Company Adj EBITDA (margin), reported | 60.4 (16.4%) | 74.8 (17.7%) | 98.8 (19.7%) | H1 29.9 (13.4%); LTM 89.7 (18.0%) |
| Add-backs as % of company Adj EBITDA | 30.1% | 30.1% | 35.1% | H1 65.2%; LTM 46.3% |
| Diligence-adjusted EBITDA (margin), analyst view | 55.8 (15.1%) | 68.8 (16.3%) | 84.7 (16.9%) | H1 22.5 (10.1%); LTM 72.6 (14.6%) |
| DSO, days (net AR / revenue x 365) | 60.4 | 63.5 | 86.4 | 76.3 on LTM revenue; 84.2 on Q2 annualized |
| AR + contract assets, days | 68.4 | 72.4 | 104.3 | 90.6 LTM; 100.0 Q2 annualized |
| Contract assets (unbilled) | 8.1 | 10.2 | 24.7 | 19.5 |
| Allowance / gross AR | 3.9% | 3.8% | 2.1% | 3.2% |
| Inventory (DIO, days) | 55.2 (91.2) | 63.9 (93.4) | 71.3 (87.9) | 84.0 (102.2 LTM; 111.1 H1 annualized) |
| Operating cash flow (OCF) | 30.8 | 40.8 | 9.7 | H1 -4.2; LTM -6.9 |
| OCF / EBITDA | 73.0% | 78.0% | 15.1% | H1 -40.4%; LTM -14.3% |
| OCF / net income | 2.68x | 2.68x | 0.52x | H1 n/m (both negative); LTM -1.57x |
| Free cash flow (OCF - capex) | 16.2 | 24.6 | -10.1 | H1 -13.0; LTM -26.4 |
| Cash | 54.8 | 48.3 | 41.6 | 33.9 |
| Revolver + term loan = total debt | 0.0 + 120.0 = 120.0 | 10.0 + 190.0 = 200.0 | 35.0 + 185.0 = 220.0 | 45.0 + 182.5 = 227.5 |
| Net debt | 65.2 | 151.7 | 178.4 | 193.6 |
| Net debt / company Adj EBITDA | 1.08x | 2.03x | 1.81x | LTM 2.16x |
| Net debt / EBITDA before add-backs | 1.55x | 2.90x | 2.78x | LTM 4.02x |
| Total debt / EBITDA before add-backs | 2.84x | 3.82x | 3.43x | LTM 4.72x |
| EBITDA / interest (Adj EBITDA / interest) | 5.7x (8.2x) | 5.3x (7.6x) | 4.7x (7.3x) | H1 1.3x (3.8x); LTM 3.2x (6.0x) |
| Top customer (Norvale) share | not provided | 28.0% | 31.1% | not provided |
| Top 10 customers share | not provided | 59.2% | 61.5% | not provided |
| FieldOS ARR (growth) | 86.0 | 109.5 (+27.3%) | 139.2 (+27.1%) | 146.8 (+5.5% in 6 months) |
| Software net revenue retention | 121% | 119% | 118% | 111% |
| Hardware backlog (implied book-to-bill) | 142.0 (n/a) | 168.0 (1.10x) | 131.0 (0.88x) | 118.0 (H1 0.89x) |
| Robots shipped (units) | 3,020 | 3,300 | 4,300 | H1 1,640 |
| Active customers | 212 | 248 | 276 | 281 |
| Full-time employees | 1,180 | 1,390 | 1,452 | 1,405 |
| EV at $24.00 / company Adj EBITDA | n/a | n/a | 13.7x | LTM 15.1x (deal model: 11.5x on FY2026E 118.0) |

### Findings

#### FIN-01: The deal model's FY2026E management case is stale; on current trading the offer is about 15x, not 11.5x
- **Finding:** The deal model values Talonfield at 11.5x the March 2026 FY2026E Adjusted EBITDA of $118.0M. That case predates both Q1 and Q2 2026 results. To reach it after H1 2026 ($222.6M revenue, $29.9M Adj EBITDA), H2 2026 would need record results that no earlier period supports. On actual earnings the $24.00 offer is 13.7x FY2025 and 15.1x LTM company Adj EBITDA.
- **Evidence:**
  - **Deal brief arithmetic is correct.**
    - Equity = 24.00 x 48.3 = 1,159.2.
    - Net debt at Jun 30, 2026 = 45.0 revolver + 182.5 term loan - 33.9 cash = 193.6.
    - EV = 1,159.2 + 193.6 = 1,352.8.
    - EV / 118.0 = 11.46x ("about 11.5x").
    - Premium = 24.00 / 17.85 - 1 = 34.5%.
  - **Revenue H2 2026 must deliver:** 560.0 - 222.6 = 337.4.
    - That is +22.3% vs H2 2025 (502.3 - 226.5 = 275.8) and +51.6% vs H1 2026.
    - It is 168.7 per quarter: 9.3% above the record Q4 2025 (154.4) and 49.4% above Q2 2026 (112.9).
  - **Adj EBITDA H2 2026 must deliver:** 118.0 - 29.9 = 88.1.
    - That is +47.3% vs H2 2025 (98.8 - 39.0 = 59.8).
    - Implied H2 margin = 88.1 / 337.4 = 26.1%, vs 21.7% in H2 2025 and 13.4% in H1 2026.
  - **H1 2026 is far behind the usual seasonal share.**
    - H1 2026 is 222.6 / 560.0 = 39.8% of FY2026E revenue and 29.9 / 118.0 = 25.3% of FY2026E Adj EBITDA.
    - In FY2025, H1 was 45.1% of revenue (226.5 / 502.3) and 39.5% of Adj EBITDA (39.0 / 98.8). In FY2024, H1 was 47.2% of revenue (199.0 / 421.7).
  - **FY2026 run-rate estimates (Medium confidence):**
    - At FY2025 seasonality: revenue 222.6 / 45.1% = 493.7 (11.8% below 560.0) and Adj EBITDA 29.9 / 39.5% = 75.7 (35.8% below 118.0).
    - If H2 2026 only repeats H2 2025: revenue 498.4 and Adj EBITDA 89.7 (24.0% below 118.0).
  - **Constant multiple:** at the model's 11.46x on LTM company Adj EBITDA, EV = 11.46 x 89.7 = 1,028.4. Equity = 1,028.4 - 193.6 = 834.8, or $17.28 per share. That is 28.0% below $24.00 and below the $17.85 undisturbed price.
  - **The market does not price the management case either.** At $17.85, EV = 17.85 x 48.3 + 193.6 = 1,055.8. That is 11.8x LTM Adj EBITDA and 8.9x FY2026E. The 34% premium (1,159.2 - 862.2 = 297.0) sits on top of a price that already values LTM earnings at about the model's multiple.
  - **Synergies:** even if all $35M of year-3 run-rate synergies are credited to today's earnings, EV / (89.7 + 35.0) = 10.8x.
  - **LTM still includes Q4 2025.** Removing the estimated above-trend Q4 gross profit (about 8.8, see FIN-02) would lower LTM further.
- **Source:**
  - `data/deal-brief.md`: price, shares, management case.
  - `data/financials/income_statement.csv`: row "Total revenue" (FY2024, FY2025, H1_2025, H1_2026).
  - `data/financials/adjusted_ebitda_reconciliation.csv`: rows "EBITDA" and "Adjusted EBITDA (company definition)" (FY2025, H1_2025, H1_2026, LTM_Q2_2026).
  - `data/financials/balance_sheet.csv`: rows "Cash and cash equivalents", "Revolving credit facility", "Term loan" (Q2_2026).
  - `data/financials/revenue_quarterly.csv`: all rows.
- **Severity:** Critical. The EBITDA base is 24.0% (LTM) to 35.8% (seasonality estimate) below the model. At a constant multiple, equity value falls by 28% or more, far above the 10% threshold.
- **Confidence:** High for the recomputed multiples and the H2 2026 requirement (direct calculation). Medium for the FY2026 run-rate estimates, which assume FY2025 seasonality.
- **Deal impact:**
  - Valuation: re-base the price on LTM or on a forecast refreshed with Q3 2026 actuals before signing.
  - Financing: any Arbelion debt sized on $118.0M of target EBITDA is oversized.
- **Cross-check:**
  - SEC: Q1 and Q2 2026 10-Qs and earnings 8-Ks (Item 2.02). Did management reaffirm, cut or withdraw the March 2026 investor-day outlook (8-K Item 7.01)?
  - News: analyst estimate revisions after Q1 and Q2 2026, and the Q3 2026 earnings date relative to the Nov 6 IC.

**FIN-01 supporting table: the $24.00 offer (EV 1,352.8) on different earnings bases**

| Earnings basis | EBITDA | EV / EBITDA at $24.00 | Price per share at the model's 11.46x |
|---|---|---|---|
| FY2026E management case (deal model) | 118.0 | 11.5x | $24.00 |
| FY2025, company Adj EBITDA | 98.8 | 13.7x | $19.44 |
| LTM Q2 2026, company Adj EBITDA | 89.7 | 15.1x | $17.28 |
| FY2026 estimate at FY2025 seasonality (H1 29.9 / 39.5%) | 75.7 | 17.9x | $13.97 |
| LTM Q2 2026, diligence-adjusted (FIN-05) | 72.6 | 18.6x | $13.22 |
| FY2025, EBITDA before add-backs | 64.1 | 21.1x | n/a |
| LTM Q2 2026, EBITDA before add-backs | 48.2 | 28.1x | n/a |

Price per share = (11.46 x EBITDA - 193.6) / 48.3. This is constant-multiple arithmetic to size the gap, not a valuation opinion. Revenue multiples at the offer:
- EV / FY2026E revenue = 1,352.8 / 560.0 = 2.4x.
- EV / LTM revenue = 1,352.8 / 498.4 = 2.7x.

#### FIN-02: FY2025 growth depended on one abnormal quarter; underlying growth was about 14% and is now negative
- **Finding:** Q4 2025 revenue grew 32.4% YoY. Every other quarter from Q1 2025 to Q2 2026 grew between -4.0% and +14.4%. Q4 2025 alone produced 46.9% of FY2025's growth, and about $21M of it sits above the trend. Revenue then dropped 29.0% in Q1 2026. This fits a pull-forward pattern (inference).
- **Evidence:**
  - **Quarterly YoY:**
    - Q1 2025: 108.9 / 96.2 = +13.2%.
    - Q2 2025: 117.6 / 102.8 = +14.4%.
    - Q3 2025: 121.4 / 106.1 = +14.4%.
    - Q4 2025: 154.4 / 116.6 = +32.4%.
    - Q1 2026: 109.7 / 108.9 = +0.7%.
    - Q2 2026: 112.9 / 117.6 = -4.0%.
  - **Sequential:**
    - Q4 2025 / Q3 2025 = +27.2%, vs +9.9% for Q4 2024 / Q3 2024.
    - Q1 2026 / Q4 2025 = -29.0%, vs -6.6% for Q1 2025 / Q4 2024.
  - **Share of growth:** the FY2025 increase was 502.3 - 421.7 = 80.6. The Q4 increase was 154.4 - 116.6 = 37.8, so 37.8 / 80.6 = 46.9%.
  - **Trend estimate:**
    - Q1 to Q3 2025 grew 347.9 / 305.1 = +14.0%.
    - Trend Q4 2025 = 116.6 x 1.140 = 133.0. Using the FY2024 Q3-to-Q4 step-up instead: 121.4 x 116.6 / 106.1 = 133.4.
    - Above-trend revenue = 154.4 - 133.0 = 21.4 (21.0 on the second method).
    - FY2025 growth without it = (502.3 - 21.4) / 421.7 - 1 = 14.0%.
  - **Segment half-years:**
    - Hardware: H1 2025 134.2, H2 2025 167.2 (301.4 - 134.2), H1 2026 116.9. H1 2026 is -30.1% vs H2 2025 and -12.9% vs H1 2025.
    - Software and services were steadier. Software was 69.7 in H2 2025 and 67.5 in H1 2026.
  - **Consistent signals:**
    - AR and contract assets rose 45.5 + 14.5 = 60.0 in FY2025. That equals 74.4% of the 80.6 revenue increase (FIN-03).
    - The "customer implementation delays" add-back was 4.1 in FY2025. Of that, 4.1 - 0.8 = 3.3 fell in H2 2025.
    - Hardware backlog fell 37.0 in FY2025 (FIN-08).
  - **LTM growth is flattered:** 498.4 / 449.2 - 1 = 11.0%, but only because the LTM still contains Q4 2025. Even if all 21.4 had been booked in H1 2026, H1 2026 growth would be (222.6 + 21.4) / 226.5 - 1 = 7.7% (assumption).
  - **Estimated profit effect:** 21.4 x 41.1% FY2025 gross margin = 8.8, which is 8.9% of FY2025 Adj EBITDA. This is an estimate; the actual margin on these sales is unknown.
- **Source:**
  - `data/financials/revenue_quarterly.csv`: all rows.
  - `data/financials/income_statement.csv`: rows "Revenue: Hardware", "Revenue: Software (FieldOS)", "Revenue: Services", "Total revenue", "Gross profit".
  - `data/financials/cash_flow.csv`: rows "Change in accounts receivable", "Change in contract assets".
  - `data/financials/adjusted_ebitda_reconciliation.csv`: row "Detail: Customer implementation delays".
- **Severity:** High. Escalate to Critical if the Q4 2025 revenue involved bill-and-hold, early recognition or side terms that could force a restatement.
- **Confidence:** High for the growth calculations. Medium for the above-trend amount, which depends on the trend assumption.
- **Deal impact:** Valuation (FY2025 base and LTM overstated); closing risk (restatement); post-closing (revenue reversals or customer credits).
- **Cross-check:**
  - SEC: FY2025 10-K revenue recognition policy (point in time vs over time, bill-and-hold), critical audit matters and contract asset note. Q4 2025 earnings 8-K and Q1 2026 10-Q MD&A explanations of the Q4 spike and the Q1 drop.
  - News: reports of a large year-end order (possibly Norvale) or pull-forward commentary.
  - Court records: securities class actions or customer delivery and acceptance disputes.

#### FIN-03: Receivables and unbilled contract assets ballooned at FY2025 year-end while the credit-loss allowance was cut
- **Finding:** DSO jumped from 63.5 to 86.4 days in FY2025. Contract assets (unbilled) more than doubled, and the allowance fell from 3.8% to 2.1% of gross receivables. About $31.5M of year-end FY2025 receivables sit above the FY2024 collection pattern. DSO on current sales is still about 84 days.
- **Evidence:**
  - **DSO = net AR / revenue x 365:**
    - FY2023: 61.0 / 368.9 x 365 = 60.4 days.
    - FY2024: 73.4 / 421.7 x 365 = 63.5.
    - FY2025: 118.9 / 502.3 x 365 = 86.4.
    - Jun 30, 2026: 104.2 / 498.4 (LTM) x 365 = 76.3, or 104.2 / (112.9 x 4) x 365 = 84.2 on Q2 2026 annualized revenue.
  - **Quarter-based DSO (AR / last quarter revenue x days):**
    - Dec 2024: 73.4 / 116.6 x 92 = 57.9.
    - Dec 2025: 118.9 / 154.4 x 92 = 70.8.
    - Jun 2026: 104.2 / 112.9 x 91 = 84.0.
    - DSO lengthened even against the inflated Q4 2025 revenue.
  - **FY2025 growth:** net AR +62.0% (73.4 to 118.9) and gross AR +59.2% (76.3 to 121.5), vs revenue +19.1%. Excess AR at FY2024 DSO = 118.9 - (73.4 / 421.7 x 502.3 = 87.4) = 31.5.
  - **Contract assets:**
    - Balances: 8.1, 10.2, 24.7, 19.5. That is +142.2% in FY2025.
    - Days: 24.7 / 502.3 x 365 = 17.9, vs 8.8 in FY2024.
    - AR plus contract asset days: 68.4, 72.4, 104.3, then 90.6 (LTM).
  - **Allowance / gross AR:** 2.5 / 63.5 = 3.9%; 2.9 / 76.3 = 3.8%; 2.6 / 121.5 = 2.1%; 3.4 / 107.6 = 3.2%. At FY2024 coverage the FY2025 allowance would have been 2.9 / 76.3 x 121.5 = 4.6. That is 2.0 higher, a 2.0 pre-tax benefit to FY2025 if it ran through earnings.
  - **H1 2026:**
    - AR fell 14.7 and contract assets 5.2. That 19.9 is 33% of the 60.0 FY2025 build.
    - The allowance was raised 0.8 to 3.4.
    - Excess AR at Jun 30, 2026 is 17.4 on an LTM basis (104.2 - 73.4 / 421.7 x 498.4) and about 33.1 on a latest-quarter basis (104.2 - 73.4 / 116.6 x 112.9).
- **Source:**
  - `data/financials/balance_sheet.csv`: rows "Accounts receivable net", "Contract assets (unbilled receivables)", "Memo: Accounts receivable gross", "Memo: Allowance for credit losses".
  - `data/financials/income_statement.csv`: row "Total revenue".
  - `data/financials/revenue_quarterly.csv`: all rows.
  - `data/financials/cash_flow.csv`: rows "Change in accounts receivable", "Change in contract assets".
- **Severity:** High
- **Confidence:** High (direct calculation). Collectability of specific balances is unknown without an aging report.
- **Deal impact:** Valuation (write-offs, revenue reversals); closing risk (restatement); post-closing (collections).
- **Cross-check:**
  - SEC: 10-K allowance roll-forward (Schedule II or credit loss note), contract asset and AR disclosures, changes to customer payment terms and auditor critical audit matters. Q2 2026 10-Q liquidity discussion.
  - Court records: collection suits or customer disputes over delayed implementations.

#### FIN-04: Cash conversion collapsed; free cash flow has been negative for 18 months
- **Finding:** Operating cash flow fell from 78.0% of EBITDA in FY2024 to 15.1% in FY2025, then turned negative in H1 2026. Across FY2025 and H1 2026, the company reported $128.7M of Adjusted EBITDA but generated -$23.1M of free cash flow.
- **Evidence:**
  - **OCF / EBITDA:**
    - FY2023: 30.8 / 42.2 = 73.0%.
    - FY2024: 40.8 / 52.3 = 78.0%.
    - FY2025: 9.7 / 64.1 = 15.1%.
    - H1 2026: -4.2 / 10.4 = -40.4%.
    - LTM: -6.9 / 48.2 = -14.3% (LTM OCF = 9.7 - 12.4 - 4.2 = -6.9).
  - **OCF / net income:** 2.68x, 2.68x, then 0.52x in FY2025 (9.7 / 18.6). H1 2026 is not meaningful (both negative). LTM is -6.9 / 4.4 = -1.57x.
  - **FCF (OCF - capex):** 16.2, 24.6, -10.1, then -13.0 in H1 2026. LTM = -6.9 - 19.5 = -26.4. FCF / company Adj EBITDA: 26.8%, 32.9%, -10.2%, LTM -29.4%. Over 18 months: 98.8 + 29.9 = 128.7 Adj EBITDA vs FCF of -10.1 - 13.0 = -23.1.
  - **FY2025 bridge:** Adj EBITDA 98.8, less cash add-backs of 17.5 (restructuring 7.9 + other items 9.6), less interest 13.6, less tax and other 6.3 (5.6 + 1.2 - 0.5), less working capital 51.7 = OCF 9.7. The working capital outflow breaks down as AR 45.5, contract assets 14.5 and inventory 7.4, offset by +15.7 from payables and other.
  - **H1 2026 bridge:** Adj EBITDA 29.9, less cash add-backs of 10.6 (4.4 + 6.2), less interest 7.9, less net tax and other 0.2, less working capital 15.4 = -4.2. H1 working capital use was similar to H1 2025 (-13.7). The H1 2026 decline therefore comes mainly from lower EBITDA (10.4 vs 26.3) and higher interest (7.9 vs 6.6).
  - **Cash nature of add-backs:** restructuring and "other non-recurring" add-backs are not reversed as non-cash in the cash flow statement. They are real cash (or accrued) costs.
- **Source:**
  - `data/financials/cash_flow.csv`: rows "Net income (loss)", "Net cash from operating activities", "Capital expenditures", "Total change in working capital" and its components, "Memo: Free cash flow".
  - `data/financials/adjusted_ebitda_reconciliation.csv`: rows "EBITDA", "Adjusted EBITDA (company definition)", add-back rows.
- **Severity:** High
- **Confidence:** High
- **Deal impact:**
  - Valuation: a cash-flow value is far below an EBITDA-multiple value. Public-target mergers rarely carry a post-closing working capital adjustment, so this must be priced upfront.
  - Financing: the target needs funding until conversion recovers.
  - Post-closing: cash needs continue after closing.
- **Cross-check:**
  - SEC: Q2 2026 10-Q liquidity and capital resources section, any liquidity risk language, and supplemental cash interest and taxes paid.
  - News: commentary on cash burn or revolver use.

#### FIN-05: Adjusted EBITDA depends on growing and recurring "non-recurring" add-backs
- **Finding:** Add-backs were 35.1% of FY2025 Adjusted EBITDA and 65.2% in H1 2026. Larger add-backs explain half of FY2025's Adjusted EBITDA growth. Restructuring recurs every year. Customer implementation delays and multi-year patent litigation look like normal operating costs. My diligence-adjusted LTM EBITDA is $72.6M vs the company's $89.7M (-19.1%).
- **Evidence:**
  - **Add-backs = Adj EBITDA - EBITDA:**
    - FY2023: 60.4 - 42.2 = 18.2 (30.1% of Adj EBITDA).
    - FY2024: 22.5 (30.1%).
    - FY2025: 98.8 - 64.1 = 34.7 (35.1%).
    - H1 2026: 29.9 - 10.4 = 19.5 (65.2%).
    - LTM: 89.7 - 48.2 = 41.5 (46.3%).
  - **Add-backs drove half of FY2025 growth.** FY2025 Adj EBITDA rose 24.0 (74.8 to 98.8); 12.2 of that (34.7 - 22.5) came from larger add-backs, i.e. 50.8%. EBITDA before add-backs rose 22.6%; Adj EBITDA rose 32.1%.
  - **Restructuring is added back every year:** FY2022 3.1, FY2023 4.6, FY2024 5.2, FY2025 7.9, H1 2026 4.4 (25.2 cumulative). The FY2025 charge came while headcount still grew 4.5%. It is a recurring cost.
  - **"Other non-recurring items" keep growing:** 1.2 in FY2022, 9.6 in FY2025 (2.8x FY2024), and 6.2 in H1 2026 alone.
  - **Operating-type items:**
    - Customer implementation delays: 4.1 in FY2025.
    - Vantor patent litigation: 0.8 in FY2024, 2.1 in FY2025, 3.0 in H1 2026. It appears in three straight periods and is rising.
  - **SBC:** 17.2 in FY2025 (17.4% of Adj EBITDA) and 17.8 LTM (19.8%).
  - **Diligence-adjusted EBITDA** removes restructuring, implementation delays and litigation. It keeps SBC and the auditor, CFO and cyber items as add-backs.
    - LTM: 89.7 - 9.7 - 3.3 - 4.1 = 72.6 (margin 72.6 / 498.4 = 14.6%).
    - FY2025: 98.8 - 7.9 - 4.1 - 2.1 = 84.7 (16.9%).
    - FY2024: 74.8 - 5.2 - 0.8 = 68.8.
    - FY2023: 60.4 - 4.6 = 55.8.
  - **Sensitivities:** if litigation is accepted as one-off, LTM = 76.7. If SBC is also treated as a cost, LTM = 72.6 - 17.8 = 54.8.
  - **EV effect:** at the deal model multiple, the 17.1 LTM adjustment = 17.1 x 11.46 = 196.0 of EV (14.5% of 1,352.8).
- **Source:**
  - `data/financials/adjusted_ebitda_reconciliation.csv`: all rows, FY2022 to LTM_Q2_2026.
  - `data/financials/income_statement.csv`: row "Restructuring and other charges".
  - `data/financials/kpis.csv`: row "Full-time employees".
- **Severity:** High. It becomes Critical if the IC values the business on diligence-adjusted EBITDA (EV effect about 14.5% at the deal multiple).
- **Confidence:** High for the arithmetic. Medium for the adjusted figure, which depends on judgment about which items are truly one-off.
- **Deal impact:** Valuation; financing (covenant EBITDA definitions may cap add-backs).
- **Cross-check:**
  - SEC: non-GAAP definition and reconciliation in the 10-K and earnings 8-Ks (did add-back categories widen in FY2025?), SEC comment letters on non-GAAP measures, restructuring note (programs, cash vs non-cash), and proxy (DEF 14A) for whether executive bonuses are tied to Adjusted EBITDA.
  - Court records: Vantor docket, for the case stage and how long costs will run.

#### FIN-06: Customer concentration is high and rising: Norvale is 31.1% of revenue and drove 47% of FY2025 growth
- **Finding:** Norvale Retail Group grew 32.3% to $156.2M, 31.1% of revenue, and supplied 47.3% of FY2025 revenue growth. All other customers together grew 14.0%. The top 10 customers were 61.5% of revenue. There is no customer data for H1 2026.
- **Evidence:**
  - **Norvale:** 118.1 (28.0% of 421.7) to 156.2 (31.1% of 502.3). Growth = 156.2 / 118.1 - 1 = 32.3%. Its increase of 38.1 is 47.3% of the 80.6 total increase.
  - **Revenue excluding Norvale:** 346.1 / 303.6 - 1 = 14.0%.
  - **Other concentration measures:**
    - Top 10: 249.6 (59.2%) to 308.8 (61.5%).
    - Top 2: (156.2 + 41.2) / 502.3 = 39.3%, up from 36.5%.
    - Top 3: 42.5% to 45.1%.
    - Customers 2 to 10 grew 16.0%; all other customers grew 12.4%.
  - **Pattern (inference only):** Norvale's FY2025 increase (38.1) almost equals the Q4 2025 YoY increase (37.8), and ex-Norvale growth (14.0%) equals Q1 to Q3 2025 growth (14.0%). This is consistent with, but does not prove, a large Norvale order recognized in Q4 2025.
  - **H1 2026:** hardware revenue fell 17.3 (134.2 to 116.9). Whether Norvale drove this is unknown.
- **Source:**
  - `data/financials/revenue_by_customer.csv`: all rows.
  - `data/financials/revenue_quarterly.csv`: all rows.
  - `data/financials/income_statement.csv`: row "Revenue: Hardware".
- **Severity:** High. Escalate to Critical if other sources show Norvale cutting orders, dual-sourcing, disputing performance, or holding termination rights on change of control.
- **Confidence:** High for the concentration figures. Low for the Q4 2025 link, which is a pattern match only.
- **Deal impact:** Valuation; closing risk (change-of-control or assignment clauses in the Norvale contract); post-closing (retention).
- **Cross-check:**
  - SEC: 10-K major customer disclosure and material contract exhibits (Norvale agreement term, renewal and termination rights).
  - News: Norvale capex plans, its own restructuring, competitor pilots or public comments on Talonfield.
  - Court records: any Norvale-Talonfield dispute.

#### FIN-07: Leverage is much higher on EBITDA before add-backs, liquidity is tightening and covenant headroom is unknown
- **Finding:** Net debt rose to $193.6M at June 30, 2026. That is 2.2x company Adjusted EBITDA but 4.0x EBITDA before add-backs (total debt 4.7x). Cash has fallen four periods in a row while the revolver went from $0 to $45.0M. Interest cover on EBITDA before add-backs fell to 1.3x in H1 2026.
- **Evidence:**
  - **Total debt (revolver + term loan):** 120.0, 200.0, 220.0, 227.5. Net debt: 65.2, 151.7, 178.4, 193.6.
  - **Net debt / company Adj EBITDA:** 1.08x, 2.03x, 1.81x, then LTM 193.6 / 89.7 = 2.16x.
  - **Net debt / EBITDA:** 1.55x, 2.90x, 2.78x, then LTM 193.6 / 48.2 = 4.02x.
  - **Total debt / EBITDA:** 2.84x, 3.82x, 3.43x, then LTM 227.5 / 48.2 = 4.72x.
  - **Covenant sensitivity (definitions not in the data):** total debt / (EBITDA + SBC = 66.0) = 3.45x; / (EBITDA + SBC + restructuring = 75.7) = 3.01x; / diligence-adjusted 72.6 = 3.13x.
  - **EBITDA / interest:** 5.7x, 5.3x, 4.7x, then H1 2026 10.4 / 7.9 = 1.3x and LTM 48.2 / 14.9 = 3.2x.
  - **Adj EBITDA / interest:** 8.2x, 7.6x, 7.3x, then LTM 6.0x.
  - **EBIT / interest:** LTM 20.3 / 14.9 = 1.4x; negative in H1 2026.
  - **Implied interest rate (interest / average debt):**
    - FY2024: 9.8 / 160.0 = 6.1%.
    - FY2025: 13.6 / 210.0 = 6.5%.
    - H1 2026: 15.8 annualized / 223.8 = 7.1%.
    - This is an approximation. It may reflect a margin step-up or amendment fees.
  - **Liquidity:**
    - Cash: 54.8, 48.3, 41.6, 33.9.
    - H1 2026 cash use before revolver draws = FCF -13.0 + term loan amortization -2.5 + net share settlement -1.5 + finance lease and other -0.7 = -17.7, or 2.95 per month.
    - At that rate, 33.9 lasts about 11.5 months without new draws. Cash at Sep 30, 2026 would be about 25.0 with no new draws (estimate).
    - The revolver commitment and its availability are not in the data.
- **Source:**
  - `data/financials/balance_sheet.csv`: rows "Cash and cash equivalents", "Revolving credit facility", "Term loan".
  - `data/financials/adjusted_ebitda_reconciliation.csv`: rows "EBITDA", "Adjusted EBITDA (company definition)", "Interest expense", "Add: Stock-based compensation", "Add: Restructuring and other charges".
  - `data/financials/income_statement.csv`: rows "Interest expense", "Operating income (loss)".
  - `data/financials/cash_flow.csv`: financing rows and "Memo: Free cash flow".
- **Severity:** High
- **Confidence:** High for the ratios. Medium for the runway and implied interest rate, which are estimates. Headroom cannot be computed without the covenant terms.
- **Deal impact:**
  - Financing: refinancing at close, change-of-control repayment, prepayment costs.
  - Closing risk: a covenant breach or cash squeeze before closing could force a waiver or amendment and test the material adverse change (MAC) clause. Interim covenants should bar new debt and buybacks.
- **Cross-check:**
  - SEC: credit agreement and amendments (10-K exhibits, 8-K Items 1.01 and 2.03), covenant compliance statements in the 10-Qs, and revolver size and maturity in the debt note.
  - News: refinancing or lender discussions.
  - Lead agent: please send the covenant definition and threshold if the SEC analyst finds them, and I will compute headroom.

#### FIN-08: Operating KPIs have turned and contradict the management case
- **Finding:** Every forward-looking KPI weakened in H1 2026:
  - Net revenue retention fell 7 points to 111%.
  - Net new ARR roughly halved.
  - Backlog is 30% below its peak, and implied book-to-bill has been below 0.9x since FY2025.
  - Customer additions stalled and headcount fell.

  The KPIs supported software growth in FY2024 and FY2025, but FY2025 hardware growth came largely from drawing down backlog.
- **Evidence:**
  - **ARR:** 86.0, 109.5 (+27.3%), 139.2 (+27.1%), then 146.8 (+5.5% in six months, about 11% annualized).
  - **Net new ARR:** FY2024 23.5; FY2025 29.7 (14.85 per half-year); H1 2026 7.6 (-49%).
  - **NRR:** 121%, 119%, 118%, 111%.
  - **Hardware backlog:** 142.0, 168.0, 131.0 (-22.0%), then 118.0 (-9.9% in H1 2026 and -29.8% from Dec 2024). Backlog / LTM hardware revenue: 64.1% (168.0 / 261.9), 43.5%, then 41.5% (118.0 / 284.1).
  - **Implied hardware orders** = closing backlog - opening backlog + hardware revenue (assumes no cancellations):
    - FY2024: 168.0 - 142.0 + 261.9 = 287.9 (book-to-bill 1.10x).
    - FY2025: 131.0 - 168.0 + 301.4 = 264.4 (0.88x).
    - H1 2026: 118.0 - 131.0 + 116.9 = 103.9 (0.89x).
    - FY2025 hardware revenue grew 39.5, of which the backlog drawdown supplied 37.0.
    - H1 2026 annualized orders (207.8) are 21.4% below FY2025.
  - **Robots shipped:** 3,020, 3,300, 4,300 (+30.3%), then 1,640 in H1 2026 (3,280 annualized, -23.7%).
  - **Active customers:** 212, 248 (+36), 276 (+28), then 281 (+5 in H1 2026).
  - **Headcount:** 1,180, 1,390, 1,452, then 1,405 (-47, or -3.2%), alongside 4.4 of restructuring charges in H1 2026.
- **Source:**
  - `data/financials/kpis.csv`: all rows.
  - `data/financials/income_statement.csv`: row "Revenue: Hardware".
- **Severity:** Medium (the valuation effect is captured in FIN-01).
- **Confidence:** High for the reported KPIs. Medium for implied orders, since the backlog definition and cancellations are unknown.
- **Deal impact:** Valuation (forward revenue).
- **Cross-check:**
  - SEC: KPI definitions and any changes in the 10-K, 10-Qs and March 2026 investor-day materials (8-K Item 7.01), and the 10-K backlog disclosure.
  - News: order cancellations or customer deployment pauses.

#### FIN-09: ARR is not converting into software revenue at the historical rate
- **Finding:** In FY2024 and FY2025, software revenue ran about 3.5% above average ARR. In H1 2026 it ran 5.6% below. Software revenue also fell versus H2 2025 even though ARR rose 5.5%. ARR may include contracts that are not yet live, or FY2025 software revenue included non-recurring items.
- **Evidence:**
  - **Software revenue / average ARR:**
    - FY2024: 101.2 / ((86.0 + 109.5) / 2) = 1.035x.
    - FY2025: 128.6 / 124.35 = 1.034x.
    - H1 2026: (67.5 x 2) / ((139.2 + 146.8) / 2) = 135.0 / 143.0 = 0.944x.
  - **H1 2026 shortfall:** software revenue of 67.5 is 4.0 short of half of average ARR (71.5), or -5.6%. It is 2.1 short even of half of opening ARR (69.6).
  - **Sequential decline:** software revenue was 128.6 - 58.9 = 69.7 in H2 2025 and 67.5 in H1 2026 (-3.2%), while ARR rose from 139.2 to 146.8.
  - **ARR per installed robot:** 86.0 / 9,800 = $8,776; then $8,359 and $8,000; then 146.8 / 19,040 = $7,710. That is -12.1% since FY2023.
- **Source:**
  - `data/financials/kpis.csv`: rows "FieldOS ARR", "Installed base of robots".
  - `data/financials/income_statement.csv`: row "Revenue: Software (FieldOS)" (FY2024, FY2025, H1_2025, H1_2026).
- **Severity:** Medium
- **Confidence:** Medium. The ratio shift is calculated, but the ARR definition is unknown.
- **Deal impact:** Valuation (software is the premium-multiple part of the story).
- **Cross-check:**
  - SEC: ARR definition in the 10-K and investor-day materials (signed vs live, treatment of multi-year contracts) and any change in 2025 or 2026.
  - News: analyst commentary on ARR quality.

#### FIN-10: Margins compressed in H1 2026 despite a richer revenue mix
- **Finding:** Gross margin fell 2.8 points to 38.0% in H1 2026, even though higher-margin software rose to 30.3% of revenue. Operating expenses grew 11.6% while revenue fell. Operating income swung from +$13.3M to -$3.7M.
- **Evidence:**
  - **Gross margin:**
    - FY2023: 147.9 / 368.9 = 40.1%.
    - FY2024: 40.8%.
    - FY2025: 206.3 / 502.3 = 41.1%.
    - H1 2025: 92.4 / 226.5 = 40.8%.
    - H1 2026: 84.6 / 222.6 = 38.0%.
    - LTM: 198.5 / 498.4 = 39.8%.
    - At the H1 2025 margin, H1 2026 gross profit would have been 6.2 higher.
  - **Cost of revenue:** +2.9% (134.1 to 138.0) vs revenue -1.7%.
  - **Mix:** software share rose from 58.9 / 226.5 = 26.0% to 67.5 / 222.6 = 30.3%. Mix alone should lift gross margin, so hardware and/or services margins likely fell sharply. Segment cost data is not provided.
  - **Opex, H1 2026 vs H1 2025:**
    - R&D +6.6%; S&M +6.0%.
    - G&A +22.2% (16.2 to 19.8).
    - Restructuring +69.2% (2.6 to 4.4).
    - Total +11.6% (79.1 to 88.3), while headcount fell 3.2% from Dec 2025.
  - **Margins, H1 2025 to H1 2026:**
    - Operating margin: 5.9% to -1.7%.
    - EBITDA margin: 11.6% to 4.7%.
    - Company Adj EBITDA margin: 17.2% to 13.4%.
- **Source:**
  - `data/financials/income_statement.csv`: all rows, FY2023 to H1_2026.
  - `data/financials/kpis.csv`: row "Full-time employees".
- **Severity:** Medium (the valuation effect is captured in FIN-01).
- **Confidence:** High for the margins. Medium for the segment explanation.
- **Deal impact:** Valuation; post-closing (cost base and integration plan).
- **Cross-check:**
  - SEC: Q1 and Q2 2026 10-Q MD&A explanations of gross margin (pricing, component costs, warranty, under-absorption, inventory reserves).

#### FIN-11: Inventory is building while hardware demand falls
- **Finding:** Inventory rose 17.8% in H1 2026 to $84.0M while hardware revenue fell 12.9% and backlog fell 9.9%. Days of inventory rose to about 102 to 111 days.
- **Evidence:**
  - **Inventory:** 55.2, 63.9, 71.3, then 84.0. The +12.7 in H1 2026 was a 12.7 cash outflow.
  - **DIO = inventory / cost of revenue x 365:**
    - FY2023: 55.2 / 221.0 x 365 = 91.2.
    - FY2024: 93.4.
    - FY2025: 71.3 / 296.0 x 365 = 87.9.
    - Jun 2026: 84.0 / 299.9 (LTM) x 365 = 102.2, or 84.0 / (138.0 x 2) x 365 = 111.1.
  - **Inventory / LTM hardware revenue:** 24.4% (FY2024), 23.7% (FY2025), 29.6% (84.0 / 284.1).
- **Source:**
  - `data/financials/balance_sheet.csv`: row "Inventory".
  - `data/financials/income_statement.csv`: rows "Cost of revenue", "Revenue: Hardware".
  - `data/financials/kpis.csv`: row "Hardware order backlog".
  - `data/financials/cash_flow.csv`: row "Change in inventory".
- **Severity:** Medium
- **Confidence:** High for the build. Medium for the write-down risk (no reserve or aging data).
- **Deal impact:** Valuation (possible excess and obsolete write-downs); post-closing (working capital).
- **Cross-check:**
  - SEC: inventory note (reserves, raw materials vs finished goods), purchase obligations, and any product-generation change that could make stock obsolete.
  - News: product transitions and supplier commitments.

#### FIN-12: Add-back labels reveal an auditor change, CFO turnover and a cyber incident in the same period as the revenue and receivables anomalies
- **Finding:** The add-back detail shows four things:
  - auditor transition costs in FY2025;
  - CFO search and transition costs in FY2025 and H1 2026;
  - a cybersecurity incident in H1 2026;
  - rising patent litigation costs.

  These coincide with the Q4 2025 revenue spike (FIN-02), the receivables build and the allowance cut (FIN-03). They are warning signs for governance and internal control, not proof of a problem.
- **Evidence:**
  - Auditor transition: 2.3 (FY2025).
  - Executive search and CFO transition: 1.1 (FY2025) + 1.4 (H1 2026) = 2.5.
  - Cybersecurity incident response: 1.8 (H1 2026).
  - Vantor patent litigation: 0.8 (FY2024), 2.1 (FY2025), 3.0 (H1 2026). The H1 2026 figure alone exceeds all of FY2025.
  - The README states that no QoE report has been received.
- **Source:**
  - `data/financials/adjusted_ebitda_reconciliation.csv`: rows "Detail: Auditor transition costs", "Detail: Executive search and CFO transition", "Detail: Cybersecurity incident response", "Detail: Litigation costs (Vantor patent case)".
  - `data/financials/README.md`.
- **Severity:** Medium. Escalate to High if the auditor change was a resignation or involved disagreements or reportable events, or if a material weakness was disclosed.
- **Confidence:** High that these events occurred (they are labeled costs). Low on what they mean, which depends on other sources.
- **Deal impact:** Closing risk (restatement, investigation); post-closing (controls remediation, cyber liabilities).
- **Cross-check:**
  - SEC: 8-K Item 4.01 (auditor change, disagreements, reportable events, auditor's letter), 8-K Item 5.02 (CFO departure and reason), 8-K Item 1.05 (material cyber incident), 10-K Item 9A (internal control over financial reporting), and Form 4 insider sales from Q4 2025 to Q1 2026.
  - Court records: Vantor v. Talonfield docket (claims, damages sought, schedule).
  - News: coverage of the CFO exit, the auditor change and the cyber incident.

#### FIN-13: Share buybacks were funded with debt while free cash flow turned negative
- **Finding:** Talonfield spent $68.7M on buybacks and taxes on net share settlement from FY2023 to FY2025, more than double its $30.7M of free cash flow. In FY2025 it bought back $13.3M of stock while FCF was -$10.1M and it drew $25.0M on the revolver.
- **Evidence:**
  - **Buybacks + taxes on net share settlement, vs FCF:**
    - FY2023: 20.0 + 2.9 = 22.9 (FCF 16.2).
    - FY2024: 25.0 + 3.4 = 28.4 (FCF 24.6).
    - FY2025: 13.3 + 4.1 = 17.4 (FCF -10.1; revolver +25.0).
    - Total: 68.7 vs FCF of 16.2 + 24.6 - 10.1 = 30.7.
  - **Buybacks stopped in H1 2026:** 0.0, vs 6.0 in H1 2025.
  - **Diluted shares still rose:** 46.0, 46.9, 47.8, 48.3.
- **Source:**
  - `data/financials/cash_flow.csv`: rows "Repurchases of common stock", "Taxes paid on net share settlement of equity awards", "Revolver borrowings (repayments) net", "Memo: Free cash flow".
  - `data/financials/income_statement.csv`: row "Diluted shares (millions)".
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing (capital allocation). This is context for IC question 5 and explains part of the net debt increase.
- **Cross-check:**
  - SEC: issuer repurchase tables in the 10-K and 10-Qs, board buyback authorizations, Form 4 insider selling during buyback periods, and proxy disclosure of EPS-linked incentives.

#### FIN-14: The deal model's equity value and net debt bridge is incomplete
- **Finding:** The deal brief uses 48.3M diluted shares, which is the H1 2026 weighted average in a loss period. Loss periods normally exclude dilutive awards, so fully diluted shares at $24.00 are probably higher. Net debt also leaves out possible debt-like items, and it is rising about $2.5M a month.
- **Evidence:**
  - **Share count:** H1 2026 diluted EPS = -8.9 / 48.3 = -0.18. In a loss period, options and RSUs are anti-dilutive and excluded.
  - **Sensitivity:** each extra 1.0M shares adds 24.0 to equity value (2.1% of 1,159.2).
  - **Leases:** H1 2026 shows "Finance lease payments and other" of 0.7, so lease obligations exist. The balance sheet has no lease debt line.
  - **Net debt trend:** net debt rose 193.6 - 178.4 = 15.2 in H1 2026, about 2.5 per month.
  - **Possible debt-like items not in net debt:** Vantor litigation exposure, restructuring accruals, cyber incident costs, transaction and change-of-control payments, debt prepayment costs.
- **Source:**
  - `data/financials/income_statement.csv`: rows "Diluted shares (millions)", "Diluted EPS ($ per share)".
  - `data/financials/cash_flow.csv`: row "Finance lease payments and other".
  - `data/financials/balance_sheet.csv`: debt and cash rows.
  - `data/deal-brief.md`.
- **Severity:** Medium
- **Confidence:** Medium. The direction is clear; the amounts need the equity award and lease schedules.
- **Deal impact:** Valuation (headline equity value and EV understated).
- **Cross-check:**
  - SEC: latest 10-Q cover page (shares outstanding), equity award note (options with strike prices, RSUs, PSUs), proxy change-of-control tables, lease note, and credit agreement change-of-control and prepayment clauses.

#### FIN-15: FY2025 hardware growth was volume-led at about 12% lower revenue per robot
- **Finding:** Robots shipped rose 30.3% in FY2025, but hardware revenue rose only 15.1%. Revenue per robot fell from about $79,400 to $70,100. This points to discounting or a mix shift, possibly linked to the large Norvale volume (inference).
- **Evidence:**
  - **Hardware revenue / robots shipped:**
    - FY2023: 236.0 / 3,020 = $78,146.
    - FY2024: 261.9 / 3,300 = $79,364.
    - FY2025: 301.4 / 4,300 = $70,093 (-11.7%).
    - H1 2026: 116.9 / 1,640 = $71,280.
- **Source:**
  - `data/financials/kpis.csv`: row "Robots shipped in period (units)".
  - `data/financials/income_statement.csv`: row "Revenue: Hardware".
- **Severity:** Medium
- **Confidence:** Medium. Hardware revenue may include parts and upgrades, and the product mix is unknown.
- **Deal impact:** Valuation (sustainability of hardware pricing and margin).
- **Cross-check:**
  - SEC: MD&A price and volume commentary, and any new lower-priced models.
  - News: pricing pressure or competitive bids, especially at Norvale.

#### FIN-16: Goodwill and intangibles exceed equity; Lumora goodwill is exposed if performance keeps slipping
- **Finding:** Goodwill ($98.4M) plus intangibles ($34.1M) total $132.5M against equity of $92.0M, so tangible equity is -$40.5M. $57.4M of the goodwill arose with the FY2024 Lumora Vision acquisition. The H1 2026 operating loss raises an impairment-testing question.
- **Evidence:**
  - Tangible equity = 92.0 - 98.4 - 34.1 = -40.5.
  - Goodwill went from 41.0 to 98.4 (+57.4) in FY2024, when Lumora was acquired for 85.0.
  - Intangibles went from 21.1 to 43.4 in FY2024 and have since amortized to 34.1.
- **Source:**
  - `data/financials/balance_sheet.csv`: rows "Goodwill", "Intangible assets net", "Total stockholders' equity".
  - `data/financials/cash_flow.csv`: row "Acquisition of Lumora Vision (net of cash acquired)".
- **Severity:** Low
- **Confidence:** High for the balances. Low for the impairment likelihood (no Lumora results provided).
- **Deal impact:** Post-closing. An impairment is non-cash but would signal Lumora underperformance.
- **Cross-check:**
  - SEC: 10-K goodwill note (reporting units, headroom in the last test), the Lumora acquisition 8-K and purchase price allocation, and disclosures of Lumora's revenue contribution and organic growth.

### Positive or mitigating points

- **The data is internally consistent.** Every statement ties (see Files reviewed), and the deal brief's 11.46x is arithmetically correct. The problem is the input (FY2026E), not the math.
- **Underlying growth before 2026 was solid.** FY2025 growth was about 14% excluding either the Q4 2025 excess or Norvale. Software grew 27.1% and services 23.4% in FY2025.
- **The recurring mix is rising.** Software and services were 47.5% of H1 2026 revenue ((67.5 + 38.2) / 222.6) vs 40.8% in H1 2025, and both still grew about 14.5% in H1 2026. ARR reached 146.8, NRR is still above 100% (111%), and the installed base of 19,040 robots supports recurring revenue.
- **Part of the FY2025 receivables build has been collected.** In H1 2026, gross AR fell 13.9 (-11.4%) and contract assets fell 5.2, and the allowance was rebuilt to 3.2% of gross AR.
- **Leverage is moderate on the company's own definitions.** Net debt is 2.16x Adj EBITDA and interest cover is 6.0x. The term loan is amortizing (190.0 to 182.5).
- **Capex is light and steady** at about 4% of revenue (14.6, 16.2, 19.8; 8.8 in H1 2026).
- **The broader customer base grew in FY2025.** Customers 2 to 10 grew 16.0% and all other customers 12.4%.
- **Buybacks stopped in H1 2026,** which preserves cash.

### Gaps and questions for management

1. **Q3 2026 results:** P&L by segment, balance sheet, cash flow and KPIs, plus management's current FY2026 forecast. Has the March 2026 case been formally updated? This is needed before the Nov 6 IC.
2. **Quarterly revenue detail:** by segment and by top-10 customer, Q1 2024 to Q3 2026, including Norvale by quarter and H1 2026 customer revenue.
3. **Q4 2025 revenue detail:**
   - the largest contracts and shipments recognized in December 2025;
   - any bill-and-hold arrangements;
   - acceptance terms and extended payment terms;
   - credits, returns or concessions granted in 2026.
4. **Receivables:**
   - AR aging by customer at Dec 31, 2025, Jun 30, 2026 and the latest date;
   - subsequent collections, Norvale's balance and disputed items;
   - the allowance method, and why coverage fell to 2.1% in FY2025.
5. **Contract assets:** the roll-forward and the contracts behind the 24.7 balance, plus the status of the delayed implementations.
6. **Support for each add-back:**
   - restructuring programs by year (actions, cash vs non-cash, why "non-recurring");
   - customer implementation delays (nature, customers, related revenue);
   - Vantor litigation (budget, stage, exposure, any accrual);
   - auditor change (reason) and CFO transition;
   - cyber incident (scope, insurance recoveries, regulatory notices).
7. **Credit agreement:**
   - revolver commitment and availability, and maturities;
   - covenant definitions and levels, including add-back caps;
   - compliance certificates for the last four quarters, and any amendments or waivers;
   - pricing grid, change-of-control and prepayment terms;
   - cash interest paid.
8. **Fully diluted share count at $24.00:** shares outstanding, options (with strike prices), RSUs, PSUs and ESPP, plus change-of-control acceleration terms.
9. **Debt-like items:** finance and operating lease liabilities, accrued restructuring, litigation reserves, deferred compensation, accrued bonuses, transaction fees and tax exposures.
10. **ARR:** the definition and an ARR bridge (new, expansion, contraction, churn) reconciled to software revenue, plus gross retention and the NRR method.
11. **Backlog:** the definition, and bookings and cancellations by quarter.
12. **Segment margins:** gross margins for hardware, software and services, FY2023 to H1 2026, and warranty reserves.
13. **Inventory:** aging, the excess and obsolete reserve, purchase commitments and product transition plans.
14. **PP&E and intangibles roll-forwards.** Long-lived assets grew more than capex less D&A explains:
    - FY2025: (52.0 + 37.2) - (47.1 + 43.4) = -1.3, vs 19.8 - 26.8 = -7.0, a gap of 5.7.
    - H1 2026: a gap of 3.3.

    Identify the non-cash additions (finance leases, capitalized software or other capitalized costs that could flatter EBITDA).
15. **Lumora Vision:** revenue and EBITDA since acquisition, organic growth excluding Lumora for FY2024 and FY2025, and goodwill impairment test results.
16. **Seasonality baseline:** the Q2 2025 balance sheet and the H1 2025 working capital components (blank in `cash_flow.csv`). Without these, H1 2026 seasonality cannot be separated from deterioration. In H1 2026, deferred revenue fell 6.7 (56.9 to 50.2) and payables plus accruals fell 15.6.
17. **Quality of earnings:** no QoE report has been received (README). Recommend commissioning one before signing, focused on FIN-02 to FIN-05.
