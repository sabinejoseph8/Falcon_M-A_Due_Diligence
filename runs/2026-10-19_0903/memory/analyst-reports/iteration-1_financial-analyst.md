## Financial analyst: findings

### Files reviewed

- `data/deal-brief.md` (context only)
- `data/financials/README.md`
- `data/financials/income_statement.csv`
- `data/financials/revenue_quarterly.csv`
- `data/financials/adjusted_ebitda_reconciliation.csv`
- `data/financials/balance_sheet.csv`
- `data/financials/cash_flow.csv`
- `data/financials/kpis.csv`
- `data/financials/revenue_by_customer.csv`

**Prompt injection check:** none of these files contains text that tries to instruct the agents.

**Internal consistency checks (all pass):**
- Quarterly revenue adds up to the annual and H1 totals: FY2024 = 421.7, FY2025 = 502.3, H1 2025 = 226.5, H1 2026 = 222.6.
- The EBITDA bridge, the Adjusted EBITDA bridge and the LTM columns all recompute exactly. LTM = FY2025 - H1 2025 + H1 2026.
- Both sides of the balance sheet balance.
- The equity roll-forwards for FY2025 and H1 2026 tie out.
- Cash roll-forwards tie out.

The README says the deal team has **not** received a quality of earnings report.

US$ millions unless stated. LTM means the twelve months to June 30, 2026 (LTM revenue = 502.3 - 226.5 + 222.6 = 498.4).

### Key metrics table

Figures are as reported by the company unless marked "analyst".

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 / Jun 30, 2026 / LTM |
|---|---|---|---|---|
| Total revenue | 368.9 | 421.7 | 502.3 | H1 222.6; LTM 498.4 |
| Revenue growth YoY | 18.1% | 14.3% | 19.1% | H1 -1.7% |
| Hardware / Software / Services growth | 15.1% / 29.1% / 16.7% | 11.0% / 25.9% / 11.6% | 15.1% / 27.1% / 23.4% | -12.9% / +14.6% / +14.4% |
| Gross margin | 40.1% | 40.8% | 41.1% | H1 38.0% (H1 2025: 40.8%) |
| EBITDA (reported) | 42.2 | 52.3 | 64.1 | H1 10.4; LTM 48.2 |
| EBITDA margin | 11.4% | 12.4% | 12.8% | H1 4.7%; LTM 9.7% |
| Adjusted EBITDA (company) | 60.4 | 74.8 | 98.8 | H1 29.9; LTM 89.7 |
| Adjusted EBITDA margin | 16.4% | 17.7% | 19.7% | H1 13.4%; LTM 18.0% |
| Add-backs as % of Adjusted EBITDA | 30.1% | 30.1% | 35.1% | H1 65.2%; LTM 46.3% |
| Net income | 11.5 | 15.2 | 18.6 | H1 -8.9; LTM 4.4 |
| Operating cash flow | 30.8 | 40.8 | 9.7 | H1 -4.2; LTM -6.9 |
| Free cash flow | 16.2 | 24.6 | -10.1 | H1 -13.0; LTM -26.4 |
| OCF / EBITDA | 73.0% | 78.0% | 15.1% | H1 -40.4% |
| DSO (days) | 60.4 | 63.5 | 86.4 | 85.4 (H1 annualized) |
| Allowance / gross AR | 3.94% | 3.80% | 2.14% | 3.16% |
| Contract assets | 8.1 | 10.2 | 24.7 | 19.5 |
| Inventory (days of cost of revenue) | 55.2 (91.2) | 63.9 (93.4) | 71.3 (87.9) | 84.0 (111.1) |
| Cash | 54.8 | 48.3 | 41.6 | 33.9 |
| Total debt (term loan + revolver) | 120.0 | 200.0 | 220.0 | 227.5 |
| Net debt | 65.2 | 151.7 | 178.4 | 193.6 |
| Net debt / Adjusted EBITDA | 1.08x | 2.03x | 1.81x | 2.16x LTM |
| Net debt / EBITDA (reported) | 1.55x | 2.90x | 2.78x | 4.02x LTM |
| Total debt / EBITDA (reported) | 2.84x | 3.82x | 3.43x | 4.72x LTM |
| EBITDA / interest | 5.70x | 5.34x | 4.71x | 3.23x LTM |
| Top customer (Norvale) share | n/a | 28.0% | 31.1% | n/a |
| Top 10 share | n/a | 59.2% | 61.5% | n/a |
| FieldOS ARR | 86.0 | 109.5 | 139.2 | 146.8 |
| Software NRR | 121% | 119% | 118% | 111% |
| Hardware backlog | 142.0 | 168.0 | 131.0 | 118.0 |
| Robots shipped | 3,020 | 3,300 | 4,300 | 1,640 (H1) |
| Employees | 1,180 | 1,390 | 1,452 | 1,405 |

FY2023 interest cover: 42.2 / 7.4 = 5.70x. FY2024: 52.3 / 9.8 = 5.34x.

### Findings

#### FIN-01: The $118M Adjusted EBITDA case behind the 11.5x multiple is stale; current trading supports a much higher multiple at $24.00
- **Finding:** At $24.00 the deal is about 15.1x LTM Adjusted EBITDA and 28.1x LTM reported EBITDA, not 11.5x. Hitting the management case would need H2 2026 Adjusted EBITDA of $88.1M. That is 2.9 times H1 2026.
- **Evidence:**
  - Equity value = 24.00 x 48.3 = 1,159.2.
  - Net debt at Jun 30, 2026 = term loan 182.5 + revolver 45.0 - cash 33.9 = 193.6.
  - **EV = 1,159.2 + 193.6 = 1,352.8.**

  | Basis | EBITDA | EV / EBITDA |
  |---|---|---|
  | Management case FY2026E Adjusted EBITDA | 118.0 | 1,352.8 / 118.0 = **11.46x** (matches the brief's "about 11.5x") |
  | FY2025 Adjusted EBITDA | 98.8 | 13.69x |
  | LTM Adjusted EBITDA (company) | 89.7 | **15.08x** |
  | FY2025 reported EBITDA | 64.1 | 21.10x |
  | LTM reported EBITDA | 48.2 | **28.07x** |
  | H1 2026 annualized Adjusted EBITDA | 29.9 x 2 = 59.8 | **22.62x** |
  | H1 2026 annualized reported EBITDA | 10.4 x 2 = 20.8 | 65.04x |
  | Analyst-normalized LTM, method A (see FIN-04) | 54.8 | 24.69x |
  | Analyst-normalized LTM, method B (see FIN-04) | 72.6 | 18.63x |
  | LTM Adjusted EBITDA plus full $35M synergies | 124.7 | 10.85x |

  - EV / revenue: LTM 1,352.8 / 498.4 = 2.71x. FY2026E 1,352.8 / 560 = 2.42x.
  - **What the management case needs in H2 2026:**
    - Revenue: 560.0 - 222.6 = 337.4, against H2 2025 of 502.3 - 226.5 = 275.8. That is +22.3% YoY, while H1 2026 was -1.7%.
    - Adjusted EBITDA: 118.0 - 29.9 = 88.1, against H2 2025 of 98.8 - 39.0 = 59.8. That is +47.3%.
    - Implied H2 margin: 88.1 / 337.4 = 26.1%, against 21.7% in H2 2025 and 13.4% in H1 2026.
  - **Seasonality test (projection):**
    - The 2024 H2/H1 revenue ratio was (106.1 + 116.6) / (96.2 + 102.8) = 222.7 / 199.0 = 1.119. Applied to 2026: FY2026E revenue = 222.6 x 2.119 = 471.7.
    - The 2025 ratio was 275.8 / 226.5 = 1.218. Applied to 2026: 222.6 x 2.218 = 493.7.
    - Both are well below 560.
  - **Value test (meets the >10% Critical test):**
    - 11.5x on LTM Adjusted EBITDA: EV = 11.5 x 89.7 = 1,031.6. Equity = 1,031.6 - 193.6 = 838.0. Per share = 838.0 / 48.3 = **$17.35**.
    - That is 27.7% below $24.00: (24.00 - 17.35) / 24.00. It is also below the $17.85 unaffected price.
- **Source:** `adjusted_ebitda_reconciliation.csv` (EBITDA, Adjusted EBITDA rows, all columns); `income_statement.csv` (Total revenue); `revenue_quarterly.csv` (Q1 2024 to Q2 2024, Q3 2024 to Q4 2024); `balance_sheet.csv` Q2_2026 (Cash, Revolving credit facility, Term loan); `data/deal-brief.md` (valuation basis).
- **Severity:** Critical. Value test: keeping the deal-model multiple but using LTM Adjusted EBITDA changes value per share by 27.7%, far above the 10% threshold.
- **Confidence:** High for the multiples, which are calculated directly. Medium for the H2 seasonality projection.
- **Deal impact:** Valuation.
- **Cross-check:** look for any guidance cut or reaffirmation after March 2026 in the Q1 and Q2 2026 10-Q and 8-K earnings releases, and in analyst or news coverage of the investor day targets. Confirm the diluted share count at $24.00 (treasury method, unvested RSUs) in the 10-Q equity note.

#### FIN-02: The Q4 2025 revenue spike breaks the trend, and revenue has fallen YoY since
- **Finding:** Q4 2025 revenue jumped 32.4% YoY. Growth then fell to +0.7% in Q1 2026 and -4.0% in Q2 2026. On a trend basis, Q4 2025 was about $21.0M above normal (inference). Without it, FY2025 growth is about 14.1%, not 19.1%.
- **Evidence:**

  | Quarter | YoY growth |
  |---|---|
  | Q1 2025 | 108.9 / 96.2 = +13.2% |
  | Q2 2025 | 117.6 / 102.8 = +14.4% |
  | Q3 2025 | 121.4 / 106.1 = +14.4% |
  | Q4 2025 | 154.4 / 116.6 = **+32.4%** |
  | Q1 2026 | 109.7 / 108.9 = +0.7% |
  | Q2 2026 | 112.9 / 117.6 = **-4.0%** |

  - Quarter on quarter: Q4 2025 vs Q3 2025 = +27.2% (154.4 / 121.4). Q4 2024 vs Q3 2024 was +9.9%. Q1 2026 vs Q4 2025 = -29.0%.
  - Trend Q4 2025 (inference): 116.6 x 1.144 = 133.4. Using the 2024 Q4/Q3 ratio gives the same: 121.4 x 1.099 = 133.4. Excess = 154.4 - 133.4 = 21.0.
  - FY2025 without the excess: 502.3 - 21.0 = 481.3. Growth = 481.3 / 421.7 = +14.1%.
  - Q4 alone gave 154.4 - 116.6 = 37.8 of the FY2025 increase of 80.6, which is 46.9%.
  - By segment, H1 2026 vs H1 2025: hardware -12.9% (116.9 vs 134.2), software +14.6%, services +14.4%.
  - Mix shift: hardware fell from 64.0% of revenue (FY2023) to 60.0% (FY2025) and 52.5% (H1 2026). This is because hardware is falling, not because software is accelerating.
- **Source:** `revenue_quarterly.csv` (all rows); `income_statement.csv` (Revenue: Hardware, Software, Services, Total revenue rows).
- **Severity:** High.
- **Confidence:** High for the reported growth rates. Medium for the $21.0M "excess", which assumes the Q1 to Q3 trend.
- **Deal impact:** Valuation (quality of revenue) and possible accounting or disclosure risk.
- **Cross-check:**
  - 10-K and 10-Q notes on revenue recognition, bill-and-hold, contract modifications, and any one-off or large Q4 2025 contract.
  - MD&A explanation of Q4.
  - News on a large Norvale order or deployment in Q4 2025.
  - The lead agent should pass any one-off revenue amount disclosed in filings so I can apply it to the quarterly data.

#### FIN-03: Norvale Retail Group is 31.1% of revenue and drove 47% of FY2025 growth
- **Finding:** Concentration is high and rising. Without Norvale, FY2025 growth was 14.0%.
- **Evidence:** every listed customer, ranked by FY2025 (the FY2024 ranking is in the same order):

  | Rank | Customer | FY2024 revenue | FY2024 share | FY2025 revenue | FY2025 share | Growth |
  |---|---|---|---|---|---|---|
  | 1 | Norvale Retail Group | 118.1 | 28.0% | 156.2 | 31.1% | +32.3% |
  | 2 | Quillon Logistics | 36.0 | 8.5% | 41.2 | 8.2% | +14.4% |
  | 3 | Ardent Parcel Co. | 25.3 | 6.0% | 28.9 | 5.8% | +14.2% |
  | 4 | Pinecrest Distribution | 16.2 | 3.8% | 17.4 | 3.5% | +7.4% |
  | 5 | Harbor & Vine Grocers | 12.4 | 2.9% | 15.1 | 3.0% | +21.8% |
  | 6 | Meridale Pharmacy Supply | 10.1 | 2.4% | 12.6 | 2.5% | +24.8% |
  | 7 | Cobalt Home Goods | 9.6 | 2.3% | 11.0 | 2.2% | +14.6% |
  | 8 | Westfork Apparel | 8.8 | 2.1% | 9.8 | 2.0% | +11.4% |
  | 9 | Sunreach Auto Parts | 7.0 | 1.7% | 8.7 | 1.7% | +24.3% |
  | 10 | Tidewell Foods | 6.1 | 1.4% | 7.9 | 1.6% | +29.5% |
  | | All other customers | 172.1 | 40.8% | 193.5 | 38.5% | +12.4% |
  | | Total | 421.7 | 100.0% | 502.3 | 100.0% | +19.1% |

  - Top 10: FY2024 = 249.6 (59.2%). FY2025 = 308.8 (61.5%).
  - Top 3: FY2025 = 156.2 + 41.2 + 28.9 = 226.3, which is 45.1% of 502.3.
  - Norvale's increase was 156.2 - 118.1 = 38.1, which is 47.3% of the total increase of 80.6.
  - Without Norvale: (502.3 - 156.2) / (421.7 - 118.1) = 346.1 / 303.6 = +14.0%.
  - Norvale's +38.1 is larger than the roughly 21.0 Q4 excess in FIN-02. Whether the Q4 spike was Norvale is an inference to test. Customer data by quarter and for H1 2026 is not provided.
- **Source:** `revenue_by_customer.csv` rows 1 to 10, "All other customers", "Total".
- **Severity:** High.
- **Confidence:** High.
- **Deal impact:** Valuation and post-closing (change of control and renewal risk).
- **Cross-check:**
  - 10-K major customer disclosure and risk factors.
  - Norvale contract terms (change of control clauses, termination for convenience, expiry dates).
  - News on Norvale strategy, insourcing, or a dispute.
  - Litigation records for any Norvale claim.
  - Look up any other named parties against this table. Vantor, from the add-backs, is not a listed top 10 customer.

#### FIN-04: Add-backs are 46.3% of LTM Adjusted EBITDA, and several "non-recurring" items recur
- **Finding:** Adjusted EBITDA depends more and more on add-backs: 30.1% of Adjusted EBITDA in FY2024, 35.1% in FY2025, 65.2% in H1 2026. Restructuring has been added back every year since FY2022. "Other non-recurring" items have grown eightfold since FY2022.
- **Evidence:**
  - **Add-backs as a share of Adjusted EBITDA** (add-backs = Adjusted EBITDA - EBITDA):

    | Period | Calculation | Share |
    |---|---|---|
    | FY2022 | 14.1 / 45.7 | 30.9% |
    | FY2023 | 18.2 / 60.4 | 30.1% |
    | FY2024 | 22.5 / 74.8 | 30.1% |
    | FY2025 | 34.7 / 98.8 | 35.1% |
    | H1 2026 | 19.5 / 29.9 | 65.2% |
    | LTM | 41.5 / 89.7 | 46.3% |

  - **Restructuring:** 3.1, 4.6, 5.2, 7.9 for FY2022 to FY2025, then 4.4 in H1 2026 (9.7 LTM). It recurs in all five periods. The cumulative total is 25.2.
  - **Other non-recurring items:** 1.2, 2.0, 3.4, 9.6 for FY2022 to FY2025, then 6.2 in H1 2026 (14.0 LTM).
  - **Vantor patent litigation:** 0.8 (FY2024), 2.1 (FY2025), 3.0 (H1 2026 alone). It is now in its third year and rising.
  - **"Customer implementation delays":** 4.1 in FY2025 (3.3 LTM). These look like normal costs of delivering contracts.
  - **Stock-based compensation:** 17.8 LTM, 3.4% of FY2025 revenue (17.2 / 502.3). It is a real, recurring cost.
  - **Analyst-normalized LTM EBITDA (analyst view):**
    - Method A removes SBC, restructuring, implementation delays and litigation: 89.7 - 17.8 - 9.7 - 3.3 - 4.1 = **54.8**. As a check, this equals 48.2 + auditor 2.3 + executive search 2.5 + cyber 1.8.
    - Method B keeps SBC as an add-back, which is common market practice: 89.7 - 9.7 - 3.3 - 4.1 = **72.6**.
    - FY2025 under Method B: 98.8 - 7.9 - 4.1 - 2.1 = 84.7.
- **Source:** `adjusted_ebitda_reconciliation.csv`, all rows and columns; `income_statement.csv` (Restructuring and other charges, Memo: Stock-based compensation).
- **Severity:** High.
- **Confidence:** High for the shares, which are calculated. Medium for the normalized figures, which rest on analyst judgment about which add-backs to remove.
- **Deal impact:** Valuation.
- **Cross-check:**
  - Commission a quality of earnings report (none has been received).
  - Compare the non-GAAP reconciliation in the 8-K earnings releases, and any SEC comment letters on non-GAAP measures.
  - Check the litigation file for the status of the Vantor case and its potential damages, which are not in the financial data.

#### FIN-05: Receivables and contract assets grew much faster than revenue while the allowance fell
- **Finding:** FY2025 receivables grew 62.0% and contract assets 142.2%, against 19.1% revenue growth. DSO rose from 63.5 to 86.4 days. The allowance fell from 3.80% to 2.14% of gross receivables. Together these are consistent with aggressive revenue recognition or collection problems around Q4 2025 (inference).
- **Evidence:**
  - **DSO:**

    | Period | Calculation | DSO (days) |
    |---|---|---|
    | FY2023 | 61.0 / 368.9 x 365 | 60.4 |
    | FY2024 | 73.4 / 421.7 x 365 | 63.5 |
    | FY2025 | 118.9 / 502.3 x 365 | 86.4 |
    | Jun 30, 2026 | 104.2 / (222.6 x 2) x 365 | 85.4 |

  - **DSO on Q4 annualized revenue** (to adjust for the Q4 spike): FY2024 = 73.4 / (116.6 x 4) x 365 = 57.4 days. FY2025 = 118.9 / (154.4 x 4) x 365 = 70.3 days. DSO is still rising.
  - **Receivables plus contract assets:**

    | Period | Calculation | Days |
    |---|---|---|
    | FY2023 | 69.1 / 368.9 x 365 | 68.4 |
    | FY2024 | 83.6 / 421.7 x 365 | 72.4 |
    | FY2025 | 143.6 / 502.3 x 365 | 104.3 |
    | Jun 30, 2026 | 123.7 / 445.2 x 365 | 101.4 |

  - **Growth:** net receivables 118.9 / 73.4 = +62.0%. Contract assets 24.7 / 10.2 = +142.2%.
  - **Allowance as % of gross receivables:**

    | Period | Calculation | Share |
    |---|---|---|
    | FY2023 | 2.5 / 63.5 | 3.94% |
    | FY2024 | 2.9 / 76.3 | 3.80% |
    | FY2025 | 2.6 / 121.5 | 2.14% |
    | Jun 30, 2026 | 3.4 / 107.6 | 3.16% |

  - At the FY2024 rate, the FY2025 allowance would have been 121.5 x 3.80% = 4.6, about 2.0 above the 2.6 booked. This is a pre-tax earnings benefit (inference).
  - Receivables fell only 14.7 in H1 2026, so DSO stays at about 85 days even with lower revenue.
- **Source:** `balance_sheet.csv` (Accounts receivable net, Contract assets, Memo: AR gross, Memo: Allowance); `income_statement.csv` (Total revenue); `revenue_quarterly.csv` (Q4 2024, Q4 2025); `cash_flow.csv` (Change in AR, Change in contract assets).
- **Severity:** High.
- **Confidence:** High for the ratios. Medium for the interpretation.
- **Deal impact:** Valuation, plus a possible accounting restatement risk.
- **Cross-check:**
  - Receivables aging by customer, especially Norvale.
  - 10-K credit loss and contract asset notes.
  - Any auditor critical audit matter on revenue.
  - The reason for the 2025 auditor change (an auditor transition cost of 2.3 is in the add-backs): check 8-K Item 4.01 for disagreements.

#### FIN-06: Cash conversion has collapsed, and LTM free cash flow is -$26.4M
- **Finding:** Operating cash flow fell from 78.0% of EBITDA in FY2024 to 15.1% in FY2025, and was negative in H1 2026. LTM free cash flow is -26.4, against company LTM Adjusted EBITDA of +89.7.
- **Evidence:**
  - **OCF / net income:** FY2023 30.8 / 11.5 = 2.68x. FY2024 40.8 / 15.2 = 2.68x. FY2025 9.7 / 18.6 = 0.52x. H1 2026: OCF -4.2 against net income -8.9.
  - **OCF / EBITDA:** 73.0%, 78.0%, 15.1% for FY2023 to FY2025. H1 2026: -4.2 / 10.4 = -40.4%.
  - **OCF / Adjusted EBITDA:** FY2024 40.8 / 74.8 = 54.5%. FY2025 9.7 / 98.8 = 9.8%.
  - **FCF:** 16.2, 24.6, -10.1 for FY2023 to FY2025. H1 2026 = -13.0.
  - **LTM:** OCF = 9.7 - 12.4 + (-4.2) = -6.9. Capex = 19.8 - 9.1 + 8.8 = 19.5. FCF = -6.9 - 19.5 = -26.4.
  - **Working capital outflow:** -51.7 in FY2025, of which receivables -45.5 and contract assets -14.5. -15.4 in H1 2026, of which inventory -12.7 and payables, accruals and deferred revenue -22.6.
- **Source:** `cash_flow.csv` (all rows); `adjusted_ebitda_reconciliation.csv` (EBITDA, Adjusted EBITDA rows).
- **Severity:** High.
- **Confidence:** High.
- **Deal impact:** Valuation and financing.
- **Cross-check:** liquidity discussion in the 10-Q MD&A, going concern language if any, and the Q3 2026 trading update if published.

#### FIN-07: Leverage on reported EBITDA is 4.72x total and 4.02x net; covenant headroom cannot be tested without the definition
- **Finding:** Leverage looks moderate on the company's Adjusted EBITDA (2.54x total, 2.16x net). On reported EBITDA it is 4.72x total and 4.02x net, up from 3.43x and 2.78x at FY2025. Liquidity is tightening: the revolver has been drawn more each period and cash has fallen.
- **Evidence:**
  - **Total debt at Jun 30, 2026:** 182.5 + 45.0 = 227.5. Net debt: 227.5 - 33.9 = 193.6.

    | Basis | EBITDA | Total debt / EBITDA | Net debt / EBITDA |
    |---|---|---|---|
    | LTM Adjusted (company) | 89.7 | 227.5 / 89.7 = **2.54x** | 193.6 / 89.7 = **2.16x** |
    | LTM reported | 48.2 | 227.5 / 48.2 = **4.72x** | 193.6 / 48.2 = **4.02x** |
    | Analyst method A | 54.8 | 4.15x | 3.53x |
    | FY2025 Adjusted | 98.8 | 220.0 / 98.8 = 2.23x | 178.4 / 98.8 = 1.81x |
    | FY2025 reported | 64.1 | 220.0 / 64.1 = 3.43x | 178.4 / 64.1 = 2.78x |
    | FY2024 Adjusted | 74.8 | 200.0 / 74.8 = 2.67x | 151.7 / 74.8 = 2.03x |
    | FY2024 reported | 52.3 | 200.0 / 52.3 = 3.82x | 151.7 / 52.3 = 2.90x |

  - **Interest cover:**
    - LTM EBITDA / interest = 48.2 / 14.9 = 3.23x. Adjusted: 89.7 / 14.9 = 6.02x.
    - LTM EBIT / interest = (37.3 - 13.3 - 3.7) / 14.9 = 20.3 / 14.9 = 1.36x.
    - H1 2026 operating income (-3.7) did not cover interest (7.9).
  - **Revolver drawn:** 0.0, 10.0, 35.0, then 45.0 at Jun 30, 2026.
  - **Cash runway (projection):** the H1 2026 cash change excluding the revolver draw was -7.7 - 10.0 = -17.7, about 2.95 a month. 33.9 / 2.95 gives about 11.5 months without further revolver draws. Revolver capacity is not in the data.
- **Source:** `balance_sheet.csv` (Cash, Revolving credit facility, Term loan, all columns); `adjusted_ebitda_reconciliation.csv` (EBITDA, Adjusted EBITDA, Interest expense); `income_statement.csv` (Operating income); `cash_flow.csv` (Revolver borrowings, Net change in cash).
- **Severity:** High. Under the calibration rule, debt is expected to be refinanced at closing. It would become Critical if the covenant definition shows a breach or near-breach before signing or closing. For example, a maximum net leverage of 4.0x on reported EBITDA would already be breached at 4.02x (hypothetical; the threshold is unknown).
- **Confidence:** High for the ratios. Low for covenant status, because the definition and threshold are not in my sources.
- **Deal impact:** Financing and closing risk.
- **Cross-check:**
  - The lead agent should provide the credit agreement covenant definition (EBITDA definition, add-back caps, threshold, test dates) and the revolver commitment size from the 10-K or 8-K exhibits.
  - Check for any covenant amendment or waiver in 8-K filings.
  - Check whether finance lease liabilities count as debt. H1 2026 shows 0.7 of "finance lease payments and other", but no lease liability line is shown on the balance sheet.

#### FIN-08: Leading KPIs point to slowing growth, against the management case
- **Finding:** Backlog fell 29.8% from its FY2024 peak. Net revenue retention dropped from 118% to 111% in six months. ARR growth slowed to about 11% annualized. Robots shipped in H1 2026 run about 24% below FY2025 on an annualized basis. Hardware revenue per robot fell 11.7% in FY2025, consistent with discounting or a volume push (inference).
- **Evidence:**
  - **Backlog:** 142.0, 168.0, 131.0, 118.0. The fall from the peak is (168.0 - 118.0) / 168.0 = 29.8%. FY2025 backlog fell 22.0% even though hardware revenue rose 15.1%, which suggests backlog was converted early.
  - **ARR growth:** FY2024 109.5 / 86.0 = +27.3%. FY2025 139.2 / 109.5 = +27.1%. H1 2026 146.8 / 139.2 = +5.5% in six months, about 10.9% annualized.
  - **NRR:** 121%, 119%, 118%, then 111%.
  - **Robots shipped:** 3,020, 3,300 (+9.3%), 4,300 (+30.3%). H1 2026 was 1,640, or 3,280 annualized (-23.7%). The installed base rolls forward exactly (17,400 + 1,640 = 19,040), which implies no retirements are recorded.
  - **Hardware revenue per robot:** FY2023 236.0 / 3,020 = $78.1k. FY2024 261.9 / 3,300 = $79.4k. FY2025 301.4 / 4,300 = $70.1k (-11.7%). H1 2026 116.9 / 1,640 = $71.3k.
  - **Active customers:** 276 to 281 (+5 in H1 2026, against +28 in FY2025). Employees fell 3.2% (1,452 to 1,405).
  - **Deferred revenue (current + non-current):** 56.9 at FY2025, 50.2 at Jun 30, 2026 (-11.8%), even though ARR rose.
- **Source:** `kpis.csv` (all rows); `income_statement.csv` (Revenue: Hardware); `balance_sheet.csv` (Deferred revenue rows).
- **Severity:** High.
- **Confidence:** High for the calculations. Medium for the interpretation of pricing.
- **Deal impact:** Valuation.
- **Cross-check:**
  - KPI definitions in the 10-K and investor day materials.
  - H1 2025 KPIs for a like-for-like comparison (not provided).
  - News on competitive pricing or lost deals.

#### FIN-09: Gross and Adjusted EBITDA margins compressed sharply in H1 2026
- **Finding:** Gross margin fell 2.8 points YoY to 38.0%. Adjusted EBITDA margin fell to 13.4%, against 17.2% in H1 2025 and the 26.1% the H2 management case needs.
- **Evidence:**
  - **Gross margin:** FY2022 121.8 / 312.4 = 39.0%. FY2023 40.1%, FY2024 40.8%, FY2025 41.1%. H1 2025 92.4 / 226.5 = 40.8%. H1 2026 84.6 / 222.6 = 38.0%.
  - **Operating costs, H1 2026 vs H1 2025:** G&A up 22.2% (19.8 vs 16.2). R&D up 6.6% (34.0 vs 31.9). S&M up 6.0% (30.1 vs 28.4). Revenue fell 1.7%.
  - **Operating result:** operating income turned negative (-3.7, against +13.3 in H1 2025).
- **Source:** `income_statement.csv` (Gross profit, Total revenue, opex rows, H1 columns); `adjusted_ebitda_reconciliation.csv` (Adjusted EBITDA margin).
- **Severity:** High.
- **Confidence:** High.
- **Deal impact:** Valuation.
- **Cross-check:** 10-Q MD&A on the reasons for margin decline (pricing, mix, warranty, supply costs) and any Q3 2026 update.

#### FIN-10: Inventory grew while hardware sales and backlog fell
- **Finding:** Inventory grew 17.8% in H1 2026 to 84.0. Hardware revenue fell 12.9% and backlog fell 9.9% over the same period. This raises obsolescence and write-down risk (inference).
- **Evidence:**
  - Inventory growth: 84.0 / 71.3 = +17.8%.
  - Days of cost of revenue: FY2025 71.3 / 296.0 x 365 = 87.9 days. H1 2026 84.0 / (138.0 x 2) x 365 = 111.1 days.
  - Inventory / backlog: 38.0% (FY2024), 54.4% (FY2025), 71.2% (Jun 30, 2026).
  - Payables plus accruals fell from 84.7 to 69.1 (-15.6) in H1 2026.
- **Source:** `balance_sheet.csv` (Inventory, Accounts payable, Accrued liabilities); `income_statement.csv` (Cost of revenue); `kpis.csv` (backlog).
- **Severity:** Medium.
- **Confidence:** High for the calculations. Medium for the write-down risk.
- **Deal impact:** Valuation (net working capital peg) and post-closing.
- **Cross-check:** 10-Q inventory note (raw materials vs finished goods, reserves); supplier news.

#### FIN-11: Goodwill and intangibles exceed equity; impairment test date not in financial data
- **Finding:** Goodwill (98.4) plus intangibles (34.1) total 132.5, which is 144% of stockholders' equity (92.0). Tangible equity is -40.5. Goodwill has stayed at 98.4 since the FY2024 Lumora acquisition, with no impairment.
- **Evidence:**
  - Tangible equity = 92.0 - 98.4 - 34.1 = -40.5.
  - Goodwill rose 57.4 in FY2024 (98.4 - 41.0) after the 85.0 Lumora acquisition.
  - Market cap at $17.85 = 17.85 x 48.3 = 862.2. This is well above book equity at company level. Reporting-unit headroom for Lumora is unknown.
  - The financial files do not contain the test date or the share price history.
- **Source:** `balance_sheet.csv` (Goodwill, Intangible assets net, Total stockholders' equity); `cash_flow.csv` (Acquisition of Lumora Vision).
- **Severity:** Medium.
- **Confidence:** Medium. The impairment test date and reporting-unit data are missing.
- **Deal impact:** Post-closing (purchase accounting) and valuation, if Lumora is underperforming.
- **Cross-check:** the lead agent should take the impairment test date and reporting units from the 10-K goodwill note, and the share price change since that date from news or market data. Also check Lumora's revenue contribution, because FY2024 organic growth is unknown.

#### FIN-12: Share buybacks funded while free cash flow was negative and the revolver was being drawn
- **Finding:** In FY2025 the company repurchased $13.3M of stock while free cash flow was -10.1 and it drew $25.0M on the revolver.
- **Evidence:**
  - Buybacks: 20.0 (FY2023), 25.0 (FY2024), 13.3 (FY2025), 58.3 in total.
  - FY2025 cash needs: buyback 13.3 + net share settlement 4.1 + term loan repayment 5.0 + negative FCF 10.1 = 32.5. These were funded by the revolver (+25.0) and by cash (-6.7) (calculation).
- **Source:** `cash_flow.csv` (Repurchases of common stock, Revolver borrowings, FCF memo, FY2025 column).
- **Severity:** Medium.
- **Confidence:** High.
- **Deal impact:** Governance.
- **Cross-check:** 10-K share repurchase disclosure (Item 5), board authorization dates, and executive trading or proxy disclosures.

#### FIN-13: The add-backs point to governance and event risk (auditor change, CFO transition, cyber incident, Vantor case)
- **Finding:** The FY2025 and H1 2026 add-backs show four events worth checking: an auditor transition (2.3, FY2025), executive search and CFO transition (1.1 in FY2025, 1.4 in H1 2026), a cybersecurity incident (1.8, H1 2026), and the Vantor patent litigation (5.9 in total since FY2024).
- **Evidence:**
  - Vantor litigation: 0.8 + 2.1 + 3.0 = 5.9.
  - "Customer implementation delays": 4.1 in FY2025, with 0.8 of it in H1 2025. These may point to delivery problems with customers.
- **Source:** `adjusted_ebitda_reconciliation.csv` (Detail rows).
- **Severity:** Medium (from the financial data alone; other sources may raise it).
- **Confidence:** High that the costs exist. Low on what they mean.
- **Deal impact:** Closing risk and post-closing.
- **Cross-check:**
  - 8-K Item 4.01 (auditor change and any disagreements) and Item 5.02 (CFO departure).
  - 8-K Item 1.05 or 10-Q risk factors on the cyber incident and when it was disclosed.
  - Litigation records for Vantor (claimed damages, injunction risk).
  - News on implementation problems at named customers.

### Positive or mitigating points

- Software keeps growing: revenue +14.6% in H1 2026 and ARR +5.5% in six months to 146.8. Software is now 30.3% of revenue (67.5 / 222.6), up from 21.8% in FY2023 (80.4 / 368.9).
- Services grew 14.4% in H1 2026, and the installed base reached 19,040 robots, which supports recurring service revenue.
- NRR is still above 100% (111%).
- Excluding Norvale, FY2025 growth was a steady 14.0%. The rest of the top 10 grew 7% to 30% each.
- Receivables fell 14.7 and contract assets fell 5.2 in H1 2026, so some of the FY2025 build has been collected.
- The term loan amortizes slowly (5.0 a year), and all debt is expected to be refinanced at closing under Arbelion financing.
- The financial data reconciles internally with no arithmetic breaks, and no embedded instructions were found.

### Gaps and questions for management

1. The credit agreement: covenant definitions, the EBITDA add-back caps, thresholds, test dates, revolver commitment and availability, and change of control clauses. I need these to test FIN-07.
2. Q4 2025 revenue by customer and contract, the reason for the +32.4% quarter, and any bill-and-hold or one-off items.
3. H1 2026 and quarterly revenue by customer (Norvale's run-rate in 2026). Also Norvale contract terms and expiry.
4. Receivables aging, the methodology behind the FY2025 allowance reduction, and contract asset billing schedules.
5. Support for every add-back, especially restructuring (five consecutive periods) and "customer implementation delays". A quality of earnings report is needed.
6. An updated FY2026 forecast and its bridge from H1 2026 (29.9) to the $118M case. Any Q3 2026 actuals.
7. The goodwill impairment test date, reporting units, Lumora's performance, and Lumora's revenue contribution in FY2024 and FY2025 (organic growth).
8. The diluted share count at $24.00 (options, RSUs, treasury method).
9. Debt-like items: finance leases (the 0.7 payment in H1 2026), the current portion of debt, and any earn-outs.
10. H1 2025 KPIs (backlog, ARR, NRR) for like-for-like comparison, and the KPI definitions.
11. Minor: the FY2025 "change in payables, accrued liabilities, deferred revenue and other" (15.7) does not fully reconcile to the balance sheet movements (about 20.2 by my calculation). This needs a management explanation (Low).
