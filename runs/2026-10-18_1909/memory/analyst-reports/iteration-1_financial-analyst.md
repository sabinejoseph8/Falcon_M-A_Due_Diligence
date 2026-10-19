<!-- Iteration 1, saved unedited by the lead agent on 2026-10-18. -->

## Financial analyst: findings

### Files reviewed

All files are in `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/`.

- `data/deal-brief.md` (context only)
- `data/financials/README.md`
- `data/financials/income_statement.csv`
- `data/financials/revenue_quarterly.csv`
- `data/financials/balance_sheet.csv`
- `data/financials/cash_flow.csv`
- `data/financials/adjusted_ebitda_reconciliation.csv`
- `data/financials/revenue_by_customer.csv`
- `data/financials/kpis.csv`

**Integrity checks (all passed):**
- Quarterly revenue adds to the annual and H1 totals. FY2024 = 421.7, FY2025 = 502.3, H1 2025 = 226.5, H1 2026 = 222.6.
- Every balance sheet balances.
- EBITDA = operating income + D&A in every period. For example FY2025: 37.3 + 26.8 = 64.1.
- LTM = FY2025 - H1 2025 + H1 2026 for every reconciliation row.
- Cash flow working capital lines tie to the balance sheet. For example the H1 2026 receivables change is 118.9 - 104.2 = 14.7.
- H1 2026 equity roll-forward ties: -8.9 net loss + 8.9 SBC - 1.5 net share settlement = -1.5, and 93.5 - 1.5 = 92.0.

**Embedded instructions:** I found no text in any financial file that tries to instruct the reader or an AI. There is nothing to record as a finding.

**Not in the financial data:** credit agreement terms, revolver size, covenant definitions, impairment test dates and share price history.

### Key metrics table

These are reported figures unless marked "adjusted" (my calculation). US$ millions.

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 / LTM Q2 2026 |
|---|---|---|---|---|
| Total revenue | 368.9 | 421.7 | 502.3 | H1 222.6 / LTM 498.4 |
| Revenue growth YoY | 18.1% | 14.3% | 19.1% | H1 -1.7% |
| Hardware growth | 15.1% | 11.0% | 15.1% | H1 -12.9% |
| FieldOS software growth | 29.1% | 25.9% | 27.1% | H1 14.6% |
| Services growth | 16.7% | 11.6% | 23.4% | H1 14.4% |
| Gross margin | 40.1% | 40.8% | 41.1% | H1 38.0% (H1 2025: 40.8%) |
| EBITDA (reported) | 42.2 | 52.3 | 64.1 | H1 10.4 / LTM 48.2 |
| Adjusted EBITDA (company) | 60.4 | 74.8 | 98.8 | H1 29.9 / LTM 89.7 |
| Adjusted EBITDA margin (company) | 16.4% | 17.7% | 19.7% | H1 13.4% / LTM 18.0% |
| Add-backs as % of Adjusted EBITDA | 30.1% | 30.1% | 35.1% | H1 65.2% / LTM 46.3% |
| Diligence-adjusted EBITDA (adjusted, SBC added back) | 55.8 | 68.8 | 84.7 | H1 22.5 / LTM 72.6 |
| Operating cash flow | 30.8 | 40.8 | 9.7 | H1 -4.2 / LTM -6.9 |
| Free cash flow | 16.2 | 24.6 | -10.1 | H1 -13.0 / LTM -26.4 |
| OCF / EBITDA | 73.0% | 78.0% | 15.1% | LTM negative |
| DSO (receivables, days) | 60.4 | 63.5 | 86.4 | 85.4 (H1 annualized) |
| DSO incl. contract assets (days) | 68.4 | 72.4 | 104.3 | 101.4 |
| Allowance / gross receivables | 3.9% | 3.8% | 2.1% | 3.2% |
| Inventory days (on cost of revenue) | 91.2 | 93.4 | 87.9 | 111.1 |
| Cash | 54.8 | 48.3 | 41.6 | 33.9 |
| Total debt (revolver + term loan) | 120.0 | 200.0 | 220.0 | 227.5 |
| Net debt | 65.2 | 151.7 | 178.4 | 193.6 |
| Net debt / company Adjusted EBITDA | 1.08x | 2.03x | 1.81x | 2.16x (LTM) |
| Net debt / EBITDA | 1.55x | 2.90x | 2.78x | 4.02x (LTM) |
| EBITDA / interest | 5.70x | 5.34x | 4.71x | LTM 3.23x / H1 1.32x |
| Top customer (Norvale) share | n/a | 28.0% | 31.1% | n/a |
| Top 10 share | n/a | 59.2% | 61.5% | n/a |
| FieldOS ARR | 86.0 | 109.5 | 139.2 | 146.8 |
| Software net revenue retention | 121% | 119% | 118% | 111% |
| Hardware backlog | 142.0 | 168.0 | 131.0 | 118.0 |
| Full-time employees | 1,180 | 1,390 | 1,452 | 1,405 |

### Findings

#### FIN-001: The deal model's FY2026E management case is not supported by H1 2026 actuals
- **Finding:** H1 2026 delivered only 25.3% of the $118.0 million FY2026E Adjusted EBITDA target and 39.8% of the $560.0 million revenue target. The 11.5x headline multiple is about 15.1x on LTM Adjusted EBITDA and about 22.6x on the H1 annualized run-rate.
- **Evidence:**
  - **EV check:**
    - Equity value = 24.00 x 48.3 = 1,159.2.
    - Net debt at June 30, 2026 = 45.0 + 182.5 - 33.9 = 193.6.
    - EV = 1,159.2 + 193.6 = 1,352.8.
    - EV / 118.0 = 11.46x. This matches the brief.
  - **Progress against the plan:**
    - H1 Adjusted EBITDA: 29.9 / 118.0 = 25.3%. Simple run-rate = 29.9 x 2 = 59.8.
    - Seasonality-adjusted (H1 2025 was 39.0 / 98.8 = 39.5% of FY2025): 29.9 / 0.395 = 75.7.
    - The plan needs H2 2026 Adjusted EBITDA of 118.0 - 29.9 = 88.1. That is 88.1 / 59.8 = +47.3% on H2 2025, at an implied H2 margin of 88.1 / 337.4 = 26.1%. The best full-year margin ever reported was 19.7%.
    - The plan needs H2 2026 revenue of 560.0 - 222.6 = 337.4. That is +22.3% on H2 2025 (121.4 + 154.4 = 275.8), after H1 grew -1.7%.
  - **Multiples at the $24.00 price (EV 1,352.8):**
    - FY2025 Adjusted EBITDA 98.8: 13.7x
    - LTM Adjusted EBITDA 89.7: 15.1x
    - Seasonality-adjusted FY2026E 75.7: 17.9x
    - LTM diligence-adjusted 72.6: 18.6x
    - H1 annualized 59.8: 22.6x
    - LTM EBITDA 48.2: 28.1x
    - EV / LTM revenue 498.4: 2.71x
  - **Implied price at the deal's own 11.46x multiple** (equity = 11.46x EBITDA basis - 193.6, divided by 48.3):

    | EBITDA basis | Implied price per share |
    |---|---|
    | 118.0 (management case) | $24.00 |
    | 98.8 (FY2025 Adjusted) | $19.44 |
    | 89.7 (LTM Adjusted) | $17.28 |
    | 75.7 (seasonality-adjusted FY2026E) | $13.96 |
    | 72.6 (LTM diligence-adjusted) | $13.22 |

- **Source:** `data/financials/adjusted_ebitda_reconciliation.csv` (Adjusted EBITDA row, all columns); `data/financials/income_statement.csv` (Total revenue); `data/financials/balance_sheet.csv` (Cash, Revolving credit facility, Term loan, Q2_2026); `data/deal-brief.md`.
- **Severity:** Critical. The value gap is well over 10%.
- **Confidence:** High for the reported-basis arithmetic. Medium for the run-rate and seasonality estimates, which assume the H2 pattern.
- **Deal impact:** Valuation. The deal model (v3, September 2026) still uses a March 2026 case even though H1 actuals were available.
- **Cross-check:**
  - Q1 and Q2 2026 10-Qs and earnings releases: did management withdraw or cut FY2026 guidance?
  - News: analyst estimate revisions and the share price reaction to the Q2 results.

#### FIN-002: The Q4 2025 revenue spike breaks the trend, and its size matches Norvale's growth
- **Finding:** Q4 2025 revenue of 154.4 was 32.4% above Q4 2024. Q1 to Q3 2025 grew 13% to 14%. Revenue then fell 29.0% in Q1 2026. The Q4 increase is almost exactly equal to Norvale's FY2025 increase.
- **Evidence:**
  - **Year-over-year growth by quarter:** Q1 2025 13.2%, Q2 14.4%, Q3 14.4%, Q4 32.4% (154.4 / 116.6), Q1 2026 0.7%, Q2 2026 -4.0% (112.9 / 117.6).
  - **Quarter-on-quarter:** Q4 2025 vs Q3 = +27.2%. Q1 2026 vs Q4 2025 = 109.7 / 154.4 - 1 = -29.0%.
  - **Share of the year in Q4:** 27.6% in FY2024 (116.6 / 421.7) vs 30.7% in FY2025 (154.4 / 502.3).
  - **Q4 share of FY2025 growth:** 37.8 / 80.6 = 46.9%.
  - **Excess over trend:** at the Q3 rate, 116.6 x 1.144 = 133.4, so the excess is 154.4 - 133.4 = 21.0. FY2025 growth without the excess = (502.3 - 21.0) / 421.7 - 1 = 14.1%, against 19.1% reported.
  - **Norvale match:** Norvale's increase was 156.2 - 118.1 = 38.1, against a Q4 increase of 37.8.
  - **Supporting signals in Q4:**
    - Receivables rose 45.5 and contract assets rose 14.5 at year end.
    - Hardware revenue per robot fell (see FIN-009).
    - Backlog fell 37.0.
  - Together these point to possible pull-forward, bill-and-hold or a large one-off delivery.
- **Source:** `data/financials/revenue_quarterly.csv` (all rows); `data/financials/revenue_by_customer.csv` (Norvale row); `data/financials/balance_sheet.csv` (Accounts receivable net, Contract assets).
- **Severity:** High.
- **Confidence:** High for the growth arithmetic. Medium for the link to Norvale, which is inferred and not shown by customer and quarter.
- **Deal impact:** Valuation. FY2025 is the base year behind the management case.
- **Cross-check:**
  - 10-K FY2025 and Q4 earnings release: any one-off Norvale order, bill-and-hold terms, or a revenue recognition change.
  - News: Norvale rollout announcements.
  - Lead agent: if a filing gives a one-off revenue amount, apply it to Q4 2025.

#### FIN-003: Revenue reversed in H1 2026, led by a 12.9% fall in hardware
- **Finding:** H1 2026 revenue fell 1.7%, and Q2 2026 fell 4.0% year over year. Hardware fell 12.9%. Software and services slowed to about 14% to 15% growth.
- **Evidence:**
  - Hardware: 116.9 / 134.2 - 1 = -12.9%.
  - Software: 67.5 / 58.9 - 1 = +14.6%, against +27.1% in FY2025.
  - Services: 38.2 / 33.4 - 1 = +14.4%.
  - Hardware share of revenue: 64.0% FY2023, 62.1% FY2024, 60.0% FY2025, 52.5% H1 2026.
  - The mix shift is mostly a hardware decline, not an acceleration in software.
- **Source:** `data/financials/income_statement.csv` (three revenue segment rows, all columns).
- **Severity:** High.
- **Confidence:** High. Calculated directly.
- **Deal impact:** Valuation. This answers IC question 1: reported FY2025 growth is not sustaining.
- **Cross-check:** Q1 and Q2 2026 10-Q MD&A explanations; news on order delays or customer pauses.

#### FIN-004: Heavy customer concentration in Norvale Retail Group, and rising
- **Finding:** Norvale was 31.1% of FY2025 revenue, up from 28.0%. It accounted for 47.3% of FY2025 revenue growth. Revenue from all other customers grew only 14.0%.
- **Evidence:**
  - Norvale share = 156.2 / 502.3 = 31.1%. Its growth was 32.3% (156.2 / 118.1).
  - Norvale share of FY2025 growth = 38.1 / 80.6 = 47.3%.
  - Revenue excluding Norvale: 303.6 in FY2024 and 346.1 in FY2025, so growth was 14.0%.
  - Top 3 share: 42.5% FY2024 (179.4 / 421.7), 45.1% FY2025 (226.3 / 502.3).
  - Top 10 share: 59.2% FY2024 (249.6 / 421.7), 61.5% FY2025 (308.8 / 502.3).
  - Norvale is 3.8x the number 2 customer (156.2 / 41.2).
  - "All other customers" grew 12.4% (193.5 / 172.1).
  - **Full ranked list (FY2025 rank; FY2025 revenue and share; FY2024 revenue and share). The FY2024 ranking order is the same.**

    | Rank | Customer | FY2025 revenue | FY2025 share | FY2024 revenue | FY2024 share |
    |---|---|---|---|---|---|
    | 1 | Norvale Retail Group | 156.2 | 31.1% | 118.1 | 28.0% |
    | 2 | Quillon Logistics | 41.2 | 8.2% | 36.0 | 8.5% |
    | 3 | Ardent Parcel Co. | 28.9 | 5.8% | 25.3 | 6.0% |
    | 4 | Pinecrest Distribution | 17.4 | 3.5% | 16.2 | 3.8% |
    | 5 | Harbor & Vine Grocers | 15.1 | 3.0% | 12.4 | 2.9% |
    | 6 | Meridale Pharmacy Supply | 12.6 | 2.5% | 10.1 | 2.4% |
    | 7 | Cobalt Home Goods | 11.0 | 2.2% | 9.6 | 2.3% |
    | 8 | Westfork Apparel | 9.8 | 2.0% | 8.8 | 2.1% |
    | 9 | Sunreach Auto Parts | 8.7 | 1.7% | 7.0 | 1.7% |
    | 10 | Tidewell Foods | 7.9 | 1.6% | 6.1 | 1.4% |
    | | All other customers | 193.5 | 38.5% | 172.1 | 40.8% |

  - Any party not in this list was below 7.9 of FY2025 revenue (under 1.6%). Other customers number 276 - 10 = 266, averaging 0.73 each.
- **Source:** `data/financials/revenue_by_customer.csv` (all rows); `data/financials/kpis.csv` (Active customers).
- **Severity:** High. Loss or repricing of Norvale would remove up to 31% of revenue.
- **Confidence:** High.
- **Deal impact:** Valuation and post-closing. Consider a closing condition or bring-down on the Norvale contract, and a change-of-control review.
- **Cross-check:**
  - 10-K: material contract with Norvale, its term, termination and change-of-control clauses.
  - News and litigation: any Norvale dispute, insourcing or competing vendor.
  - No customer data is given for H1 2026. Request it.

#### FIN-005: Adjusted EBITDA relies on recurring and operating add-backs
- **Finding:** Add-backs were 35.1% of FY2025 Adjusted EBITDA and 65.2% of H1 2026 Adjusted EBITDA. Several "non-recurring" items recur or look like normal operating costs. My diligence-adjusted LTM EBITDA is 72.6, against 89.7 reported.
- **Evidence:**
  - **Add-backs as a share of Adjusted EBITDA:**
    - FY2025: (98.8 - 64.1) / 98.8 = 35.1%
    - H1 2026: (29.9 - 10.4) / 29.9 = 65.2%
    - LTM: 41.5 / 89.7 = 46.3%
  - **Restructuring:** added back in every period. FY2022 to FY2025: 3.1, 4.6, 5.2, 7.9. H1 2026: 4.4. Cumulative 25.2. This is a recurring cost.
  - **"Other non-recurring":** present every year and growing. FY2022 to FY2025: 1.2, 2.0, 3.4, 9.6. H1 2026: 6.2.
  - **"Customer implementation delays":** 4.1 in FY2025 and 3.3 LTM. This looks like an ordinary cost of delivery.
  - **Vantor patent litigation:** 0.8, 2.1, then 3.0 in H1 2026 alone. The cost is rising and the case is ongoing.
  - **Diligence-adjusted EBITDA** removes restructuring, implementation delays and Vantor litigation. It keeps SBC, the auditor transition, the CFO search, the cybersecurity response, and Lumora, ERP and offering costs.
    - FY2025: 98.8 - 7.9 - 4.1 - 2.1 = 84.7 (margin 16.9%)
    - LTM: 89.7 - 9.7 - 3.3 - 4.1 = 72.6 (margin 14.6%)
    - H1 2026: 29.9 - 4.4 - 3.0 = 22.5 (margin 10.1%)
    - FY2024: 74.8 - 5.2 - 0.8 = 68.8
    - FY2023: 60.4 - 4.6 = 55.8
  - **If SBC is also treated as a cost** (cash pay would replace equity after the deal):
    - FY2025: 84.7 - 17.2 = 67.5
    - LTM: 72.6 - 17.8 = 54.8
- **Source:** `data/financials/adjusted_ebitda_reconciliation.csv` (rows EBITDA through Detail: Cybersecurity incident response, all columns).
- **Severity:** High.
- **Confidence:** High for the arithmetic. Medium for the classification, which is analyst judgment pending a quality of earnings report.
- **Deal impact:** Valuation. Each 1.0 of EBITDA is worth about 11.5 of EV at the deal multiple. The LTM gap of 17.1 is worth about 196 of EV, or about $4.06 per share.
- **Cross-check:**
  - 10-K non-GAAP reconciliation and restructuring footnote: what the programs are and whether they are complete.
  - Litigation records: Vantor case status and expected defense costs.
  - Commission a quality of earnings report.

#### FIN-006: Margins compressed sharply in H1 2026 while operating costs grew
- **Finding:** Gross margin fell 2.8 points and Adjusted EBITDA fell 23.3% in H1 2026. Operating expenses grew 11.6% while revenue fell and headcount was cut.
- **Evidence:**
  - **Gross margin:** H1 2025 92.4 / 226.5 = 40.8%; H1 2026 84.6 / 222.6 = 38.0%. Cost of revenue rose 2.9% (138.0 / 134.1) while revenue fell 1.7%.
  - **Adjusted EBITDA:** 29.9 / 39.0 - 1 = -23.3%. Margin fell from 17.2% to 13.4%.
  - **Reported EBITDA:** 10.4 / 26.3 - 1 = -60.5%. Margin 4.7%.
  - **Operating result:** operating income was -3.7 and the net loss was -8.9.
  - **Operating expenses:** 88.3 / 79.1 - 1 = +11.6%. G&A +22.2% (19.8 / 16.2), after +26.4% in FY2025 (36.4 / 28.8).
  - **Headcount:** 1,452 to 1,405, down 3.2%.
- **Source:** `data/financials/income_statement.csv` (H1_2025, H1_2026 columns); `data/financials/kpis.csv` (Full-time employees).
- **Severity:** High.
- **Confidence:** High.
- **Deal impact:** Valuation and synergy case. Part of the $35.0 million synergy assumption may already be needed just to restore margins.
- **Cross-check:** 10-Q MD&A for the drivers behind G&A (legal, auditor, CFO transition, cyber). News on pricing pressure.

#### FIN-007: Receivables and contract assets surged while the bad-debt allowance was cut
- **Finding:** FY2025 DSO jumped to 86.4 days from 63.5. Contract assets grew 142%. The allowance for credit losses fell to 2.1% of gross receivables, from 3.8%. This flattered FY2025 earnings by about 2.0.
- **Evidence:**
  - **DSO (year-end receivables / revenue x 365):**
    - FY2023: 61.0 / 368.9 x 365 = 60.4
    - FY2024: 73.4 / 421.7 x 365 = 63.5
    - FY2025: 118.9 / 502.3 x 365 = 86.4
    - H1 2026: 104.2 / 222.6 x 182.5 = 85.4
  - **Q4-based DSO**, which strips out the Q4 spike, still rose:
    - FY2024: 73.4 / 116.6 x 92 = 57.9
    - FY2025: 118.9 / 154.4 x 92 = 70.8
    - Q2 2026: 104.2 / 112.9 x 91 = 84.0
  - **Growth:** receivables rose 62.0% against revenue growth of 19.1%. Contract assets went from 10.2 to 24.7 (+142.2%), or from 2.4% to 4.9% of revenue.
  - **DSO including contract assets:** 72.4 FY2024, 104.3 FY2025, 101.4 H1 2026.
  - **Allowance / gross receivables:** 3.9% (2.5 / 63.5), 3.8% (2.9 / 76.3), 2.1% (2.6 / 121.5), 3.2% (3.4 / 107.6).
  - **Under-reserve:** at the FY2024 rate of 3.8%, the FY2025 allowance would be 121.5 x 0.038 = 4.6. The shortfall is 4.6 - 2.6 = 2.0.
- **Source:** `data/financials/balance_sheet.csv` (Accounts receivable net, Contract assets, Memo AR gross, Memo Allowance); `data/financials/revenue_quarterly.csv`; `data/financials/income_statement.csv` (Total revenue).
- **Severity:** High.
- **Confidence:** High.
- **Deal impact:** Valuation and working capital peg. Possible revenue recognition risk.
- **Cross-check:**
  - 10-K: revenue recognition and contract asset footnotes, the receivables aging, and the allowance roll-forward.
  - Whether the receivables are concentrated in Norvale.
  - Any auditor comments, given the auditor transition (FIN-013).

#### FIN-008: Cash conversion collapsed and free cash flow turned negative
- **Finding:** Operating cash flow fell from 40.8 to 9.7 in FY2025 and was -4.2 in H1 2026. LTM free cash flow is -26.4. Deferred revenue also fell 6.7 in H1 2026.
- **Evidence:**
  - **OCF / net income:** 2.68x FY2023 (30.8 / 11.5), 2.68x FY2024 (40.8 / 15.2), 0.52x FY2025 (9.7 / 18.6).
  - **OCF / EBITDA:** 73.0%, 78.0%, 15.1% (9.7 / 64.1). OCF / Adjusted EBITDA FY2025 = 9.8%.
  - **LTM OCF** = 9.7 - 12.4 + (-4.2) = -6.9.
  - **LTM capex** = 19.8 - 9.1 + 8.8 = 19.5.
  - **LTM FCF** = -6.9 - 19.5 = -26.4. Free cash flow by period: 16.2, 24.6, -10.1, and -13.0 in H1 2026.
  - **Working capital outflow FY2025:** -51.7, against -10.8 in FY2024.
  - **Deferred revenue (current + non-current):** 38.1, 48.0, 56.9, then 50.2 at June 2026 (-11.8%), even though ARR rose.
- **Source:** `data/financials/cash_flow.csv` (all rows); `data/financials/balance_sheet.csv` (Deferred revenue rows).
- **Severity:** High.
- **Confidence:** High.
- **Deal impact:** Valuation, working capital peg and financing.
- **Cross-check:** 10-Q cash flow commentary; billing terms for FieldOS (annual upfront vs monthly), which would explain whether the deferred revenue fall is seasonal.

#### FIN-009: KPIs contradict the reported growth (backlog, retention, pricing, shipments)
- **Finding:** Hardware backlog fell 22.0% in FY2025, even as hardware revenue rose 15.1%. Book-to-bill was below 1.0. Net revenue retention fell to 111%. Revenue per robot fell 11.7%. H1 2026 shipments are running about 24% below FY2025.
- **Evidence:**
  - **Backlog:** 142.0, 168.0, 131.0, 118.0. FY2025 change: 131 / 168 - 1 = -22.0%. H1 2026 change: -9.9%.
  - **Implied hardware book-to-bill** (orders = revenue + change in backlog):
    - FY2024: (261.9 + 26.0) / 261.9 = 1.10
    - FY2025: (301.4 - 37.0) / 301.4 = 0.88
    - H1 2026: (116.9 - 13.0) / 116.9 = 0.89
  - **Net revenue retention:** 121%, 119%, 118%, 111%.
  - **ARR:** +27.3% in FY2024 and +27.1% in FY2025. H1 2026 growth was only 146.8 / 139.2 - 1 = 5.5%, about 11.2% annualized.
  - **ARR per installed robot ($ thousands):** 8.78, 8.36, 8.00, 7.71.
  - **Hardware revenue per robot shipped ($ thousands):**
    - FY2023: 236.0 / 3,020 = 78.1
    - FY2024: 79.4
    - FY2025: 70.1 (-11.7%)
    - H1 2026: 71.3
  - **Units shipped:** +30.3% in FY2025 (4,300 / 3,300). H1 2026 annualized: 1,640 x 2 = 3,280, which is 23.7% below FY2025.
  - **Active customers added:** +36 in FY2024, +28 in FY2025, +5 in H1 2026.
- **Source:** `data/financials/kpis.csv` (all rows); `data/financials/income_statement.csv` (Revenue: Hardware).
- **Severity:** High.
- **Confidence:** High for the calculations. Medium for book-to-bill, which assumes backlog is hardware only and is consumed only through hardware revenue.
- **Deal impact:** Valuation. FY2025 hardware growth appears to have come from discounted volume and running down the backlog.
- **Cross-check:** 10-K backlog definition; whether the FY2025 Norvale deal was priced at a discount; news on competitor pricing.

#### FIN-010: Leverage is rising, the company depends on its revolver, and covenant headroom is unknown
- **Finding:** Net debt reached 193.6 at June 30, 2026. That is 4.02x LTM EBITDA but only 2.16x the company's LTM Adjusted EBITDA. The revolver went from 0.0 to 45.0 in 18 months. Interest cover on EBITDA was 1.32x in H1 2026.
- **Evidence:**
  - **Net debt:** 65.2 (0 + 120.0 - 54.8), 151.7, 178.4, then 193.6 (45.0 + 182.5 - 33.9).
  - **Net debt / LTM EBITDA:** 193.6 / 48.2 = 4.02x.
  - **Net debt / LTM Adjusted EBITDA:** 193.6 / 89.7 = 2.16x.
  - **Net debt / diligence-adjusted EBITDA:** 193.6 / 72.6 = 2.67x.
  - **Total debt / LTM EBITDA:** 227.5 / 48.2 = 4.72x.
  - **Interest cover:**
    - LTM EBITDA / interest: 48.2 / 14.9 = 3.23x
    - H1 2026 EBITDA / interest: 10.4 / 7.9 = 1.32x
    - LTM EBIT / interest: (37.3 - 13.3 - 3.7) / 14.9 = 20.3 / 14.9 = 1.36x
  - **Implied interest rate:** 7.9 x 2 / ((220.0 + 227.5) / 2) = 7.1%.
  - **Revolver use:** 0.0, 10.0, 35.0, 45.0.
  - **Cash runway:** cash fell 54.8, 48.3, 41.6, 33.9. H1 2026 outflow before the revolver draw = 7.7 + 10.0 = 17.7. Runway without further draws = 33.9 x 6 / 17.7 = 11.5 months.
  - **Covenants:** no definitions in the data, so headroom cannot be computed.
- **Source:** `data/financials/balance_sheet.csv` (Cash, Revolving credit facility, Term loan); `data/financials/adjusted_ebitda_reconciliation.csv` (EBITDA, Adjusted EBITDA, Interest expense); `data/financials/cash_flow.csv` (Revolver, Net change in cash).
- **Severity:** High. Debt is likely to be refinanced at closing. This becomes Critical if a covenant is breached or close to breach before closing. That is plausible if the covenant uses EBITDA with limited add-backs and a maximum around 4.0x.
- **Confidence:** High for the ratios. Low for the covenant risk until the definitions are provided.
- **Deal impact:** Financing and closing risk. Payoff amount, revolver capacity and change-of-control prepayment terms are needed.
- **Cross-check:** The lead agent should send the credit agreement from the 10-K or an 8-K: the leverage and interest cover definitions, permitted add-backs and caps, maximum levels, test dates, revolver commitment, maturity, and any amendments or waivers in 2026.

#### FIN-011: Inventory is building while hardware sales and backlog fall
- **Finding:** Inventory rose 17.8% in H1 2026 to 84.0. Inventory days rose from 87.9 to 111.1, while hardware revenue fell 12.9% and backlog fell 9.9%.
- **Evidence:**
  - Inventory: 84.0 / 71.3 - 1 = +17.8%.
  - Inventory days, FY2025: 71.3 / 296.0 x 365 = 87.9.
  - Inventory days, H1 2026: 84.0 / 138.0 x 182.5 = 111.1.
  - Cash impact in H1 2026: -12.7.
- **Source:** `data/financials/balance_sheet.csv` (Inventory); `data/financials/income_statement.csv` (Cost of revenue); `data/financials/cash_flow.csv` (Change in inventory).
- **Severity:** Medium.
- **Confidence:** High.
- **Deal impact:** Valuation (obsolescence write-down risk) and working capital peg.
- **Cross-check:** 10-Q inventory footnote (raw materials vs finished goods, reserves); news on supplier or product transitions.

#### FIN-012: Share buybacks funded with debt while free cash flow was negative
- **Finding:** The company spent 13.3 on buybacks in FY2025, when free cash flow was -10.1 and the revolver draw was 25.0. Diluted shares still rose from 46.0 million to 47.8 million.
- **Evidence:**
  - Buybacks: 20.0, 25.0 and 13.3 in FY2023 to FY2025, total 58.3.
  - Diluted shares: 46.0, 46.9, 47.8, then 48.3 in H1 2026.
- **Source:** `data/financials/cash_flow.csv` (Repurchases, Revolver borrowings, Free cash flow); `data/financials/income_statement.csv` (Diluted shares).
- **Severity:** Medium.
- **Confidence:** High.
- **Deal impact:** Governance and capital allocation. It also explains part of the rise in net debt.
- **Cross-check:** Proxy statement and board minutes for the buyback authorization and timing relative to insider sales.

#### FIN-013: Governance and risk events are buried in the add-backs
- **Finding:** The Adjusted EBITDA detail shows four events that need confirming in other sources:
  - an auditor transition (2.3, FY2025);
  - an executive search and CFO transition (1.1 in FY2025 and 1.4 in H1 2026);
  - a cybersecurity incident (1.8, H1 2026);
  - rising Vantor patent litigation costs (5.9 cumulative).
- **Evidence:** These four items total 12.2 over FY2024 to H1 2026: 2.3 + 2.5 + 1.8 + 5.9 = 12.5, minus the FY2024 Vantor amount of 0.8 if only FY2025 onward is counted. LTM total = 2.3 + 2.5 + 1.8 + 4.1 = 10.7.
- **Source:** `data/financials/adjusted_ebitda_reconciliation.csv` (Detail rows for litigation, auditor transition, executive search and CFO transition, and cybersecurity).
- **Severity:** Medium on its own. It may be higher once combined with the SEC, news and litigation findings.
- **Confidence:** High that the costs exist. Low on the nature of the events, which is not described in the financial data.
- **Deal impact:** Closing risk and post-closing (internal controls, IC question 5).
- **Cross-check:**
  - 8-K Item 4.01 (auditor change, and any disagreements).
  - 8-K Item 5.02 (CFO departure).
  - 8-K Item 1.05 (cyber incident) and whether its timing matches the H1 2026 cost.
  - Court records for the Vantor case and any damages exposure.

#### FIN-014: Goodwill and intangibles exceed equity; impairment test date not in the data
- **Finding:** Goodwill (98.4) and intangibles (34.1) total 132.5, which is 144.0% of equity (92.0). Tangible equity is -40.5. Most of the goodwill comes from the 85.0 Lumora Vision acquisition in FY2024.
- **Evidence:**
  - Goodwill went from 41.0 to 98.4 in FY2024 (+57.4). The Lumora cash paid was 85.0.
  - Intangibles: 43.4, 37.2, 34.1.
  - Tangible equity = 92.0 - 132.5 = -40.5.
  - Market capitalization at $17.85 = 17.85 x 48.3 = 862.2, against book equity of 92.0. There is headroom at the company level, but reporting-unit headroom (for example Lumora) is unknown.
  - The impairment test date and share price history are not in the financial files.
- **Source:** `data/financials/balance_sheet.csv` (Goodwill, Intangible assets net, Total stockholders' equity); `data/financials/cash_flow.csv` (Acquisition of Lumora Vision).
- **Severity:** Medium.
- **Confidence:** High for the balances. Low for impairment risk, because the test data is missing.
- **Deal impact:** Post-closing (purchase accounting, possible impairment).
- **Cross-check:**
  - 10-K goodwill footnote: test date (usually Q4), reporting units, headroom.
  - News or SEC data for the TLFS share price since the last test.
  - Whether a triggering event was assessed in Q1 or Q2 2026, given the losses.

### Positive or mitigating points

- **Software is growing and is a larger share of revenue.** FieldOS revenue grew 14.6% in H1 2026, and software is now 30.3% of revenue (67.5 / 222.6), up from 21.8% in FY2023. ARR reached 146.8, and NRR is still above 100% at 111%.
- **Services revenue held up**, at +14.4% in H1 2026.
- **The installed base keeps growing.** It reached 19,040 robots, up from 9,800 in FY2023. Unit arithmetic ties exactly (9,800 + 3,300 = 13,100, and so on), which supports future service and software revenue.
- **Receivables collections improved in H1 2026.** Receivables fell by 14.7 and the allowance was rebuilt to 3.2%.
- **Leverage on the company's own Adjusted EBITDA is moderate**, at 2.16x. The debt is likely to be repaid at closing because Arbelion is financing the deal.
- **All statements reconcile internally**, with no arithmetic breaks found.

### Gaps and questions for management

1. Customer revenue by quarter for FY2025 and H1 2026, especially Norvale in Q4 2025. Are there bill-and-hold, extended payment or acceptance terms?
2. The Norvale contract: term, renewal date, pricing, termination and change-of-control clauses, and any 2026 volume changes.
3. Is the FY2026 guidance of $560.0 million revenue and $118.0 million Adjusted EBITDA still current? What is the H2 bridge?
4. Credit agreement: covenant definitions and add-back caps, test levels, compliance certificates for Q4 2025 to Q2 2026, revolver commitment and availability, maturity, and any waivers or amendments.
5. Receivables aging, contract asset roll-forward, and allowance methodology. Why did the allowance fall in FY2025?
6. Details of the restructuring programs and why they recur every year.
7. What "customer implementation delays" costs are, and which customers they relate to.
8. Vantor litigation: status, budget and any damages exposure.
9. Cybersecurity incident: scope, insurance, and whether customer or regulator claims are expected.
10. Reasons for the auditor and CFO transitions, and any related control deficiencies.
11. Backlog definition, order intake by quarter, and pricing per robot by customer.
12. Inventory composition and reserves.
13. Goodwill impairment test date, reporting units and headroom, and whether an interim test was done in 2026.
14. Billing terms for FieldOS, to explain the fall in deferred revenue.
15. A quality of earnings report. None has been received, per `data/financials/README.md`.
