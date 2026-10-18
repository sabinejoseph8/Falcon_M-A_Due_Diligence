## Financial analyst: findings

### Files reviewed

- `data/deal-brief.md` (context only)
- `data/financials/README.md`
- `data/financials/income_statement.csv`
- `data/financials/revenue_quarterly.csv`
- `data/financials/balance_sheet.csv`
- `data/financials/cash_flow.csv`
- `data/financials/adjusted_ebitda_reconciliation.csv`
- `data/financials/revenue_by_customer.csv`
- `data/financials/kpis.csv`

I checked all eight files for embedded instructions or prompt-injection text and found none. I also checked that the files agree with each other, and they do:
- Quarterly revenue sums to the annual and H1 totals.
- EBITDA and Adjusted EBITDA recompute exactly in every period, including LTM.
- Balance sheet movements match the cash flow working capital lines.
- The equity roll-forward ties. For FY2025: 74.3 + 18.6 + 17.2 - 13.3 - 4.1 + 0.8 = 93.5.
- Cash ties in every period.

The only small gap is in the H1 2026 "payables, accrued liabilities, deferred revenue and other" line. Balance sheet movements give -22.9 against -22.6 reported, a 0.3 difference. That is not material.

No external facts were provided by the lead agent. I had no covenant definition or one-off revenue amount from the SEC filings, so where those matter I state my own definition or estimate.

US$ millions unless stated. LTM = twelve months to June 30, 2026, computed as FY2025 - H1 2025 + H1 2026.

### Key metrics table

**Reported figures (company basis)**

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 | LTM Q2 2026 |
|---|---|---|---|---|---|
| Total revenue | 368.9 | 421.7 | 502.3 | 222.6 | 498.4 |
| Revenue growth | 18.1% | 14.3% | 19.1% | -1.7% vs H1 2025 | 11.0% vs LTM Q2 2025 (449.2) |
| Hardware revenue (growth) | 236.0 (15.1%) | 261.9 (11.0%) | 301.4 (15.1%) | 116.9 (-12.9%) | n/a |
| Software, FieldOS (growth) | 80.4 (29.1%) | 101.2 (25.9%) | 128.6 (27.1%) | 67.5 (14.6%) | n/a |
| Services (growth) | 52.5 (16.7%) | 58.6 (11.6%) | 72.3 (23.4%) | 38.2 (14.4%) | n/a |
| Gross margin | 40.1% | 40.8% | 41.1% | 38.0% (H1 2025: 40.8%) | 39.8% |
| EBITDA (margin) | 42.2 (11.4%) | 52.3 (12.4%) | 64.1 (12.8%) | 10.4 (4.7%) | 48.2 (9.7%) |
| Adjusted EBITDA, company (margin) | 60.4 (16.4%) | 74.8 (17.7%) | 98.8 (19.7%) | 29.9 (13.4%) | 89.7 (18.0%) |
| Add-backs as % of Adjusted EBITDA | 30.1% | 30.1% | 35.1% | 65.2% | 46.3% |
| Net income | 11.5 | 15.2 | 18.6 | -8.9 | 4.4 |
| Operating cash flow | 30.8 | 40.8 | 9.7 | -4.2 | -6.9 |
| Free cash flow (OCF - capex) | 16.2 | 24.6 | -10.1 | -13.0 | -26.4 |
| OCF / EBITDA | 73.0% | 78.0% | 15.1% | -40.4% | -14.3% |
| DSO, net AR (days) | 60.4 | 63.5 | 86.4 | 85.4 (H1 annualized) | 76.3 (LTM revenue) |
| Allowance / gross AR | 3.9% | 3.8% | 2.1% | 3.2% | n/a |
| Contract assets | 8.1 | 10.2 | 24.7 | 19.5 | n/a |
| Inventory | 55.2 | 63.9 | 71.3 | 84.0 | n/a |
| Cash | 54.8 | 48.3 | 41.6 | 33.9 | n/a |
| Total debt (revolver + term loan) | 120.0 | 200.0 | 220.0 | 227.5 | n/a |
| Net debt | 65.2 | 151.7 | 178.4 | 193.6 | n/a |
| Net debt / Adjusted EBITDA | 1.08x | 2.03x | 1.81x | n/a | 2.16x |
| Net debt / EBITDA | 1.55x | 2.90x | 2.78x | n/a | 4.02x |
| Adjusted EBITDA / interest | 8.16x | 7.63x | 7.26x | 3.78x | 6.02x |
| EBITDA / interest | 5.70x | 5.34x | 4.71x | 1.32x | 3.23x |
| FieldOS ARR (period end) | 86.0 | 109.5 | 139.2 | 146.8 | n/a |
| Software NRR (TTM) | 121% | 119% | 118% | 111% | n/a |
| Hardware backlog | 142.0 | 168.0 | 131.0 | 118.0 | n/a |
| Hardware book-to-bill (my calculation) | n/a | 1.10 | 0.88 | 0.89 | n/a |
| Robots shipped (units) | 3,020 | 3,300 | 4,300 | 1,640 | n/a |
| Employees | 1,180 | 1,390 | 1,452 | 1,405 | n/a |
| Top customer (Norvale) share | n/a | 28.0% | 31.1% | not provided | n/a |
| Top 10 share | n/a | 59.2% | 61.5% | not provided | n/a |

**Diligence-adjusted figures (my adjustments, see FIN-04)**

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 | LTM Q2 2026 |
|---|---|---|---|---|---|
| Diligence-adjusted EBITDA A (SBC still added back) | 55.8 | 68.8 | 84.7 | 22.5 | 72.6 |
| Margin | 15.1% | 16.3% | 16.9% | 10.1% | 14.6% |
| Diligence-adjusted EBITDA B (A less SBC) | 44.2 | 54.9 | 67.5 | 13.6 | 54.8 |
| Net debt / adjusted EBITDA A | n/a | n/a | 2.11x | n/a | 2.67x |

How the key metrics are calculated:
- LTM revenue = 502.3 - 226.5 + 222.6 = 498.4.
- LTM gross profit = 206.3 - 92.4 + 84.6 = 198.5, so LTM gross margin = 198.5 / 498.4 = 39.8%.
- LTM operating cash flow = 9.7 - 12.4 + (-4.2) = -6.9.
- LTM capex = 19.8 - 9.1 + 8.8 = 19.5, so LTM free cash flow = -6.9 - 19.5 = -26.4. This matches the free cash flow memo: -10.1 - 3.3 - 13.0 = -26.4.
- LTM Q2 2025 revenue = 421.7 - (96.2 + 102.8) + 226.5 = 449.2.
- H1 2026 interest cover: 29.9 / 7.9 = 3.78x on Adjusted EBITDA, and 10.4 / 7.9 = 1.32x on EBITDA.
- Diligence-adjusted EBITDA B: FY2023 55.8 - 11.6 = 44.2; FY2024 68.8 - 13.9 = 54.9; H1 2026 22.5 - 8.9 = 13.6.

### Findings

#### FIN-01: The management case behind the deal multiple is stale; the real multiple is about 15x LTM, not 11.5x
- **Finding:** The deal model's 11.5x multiple depends on FY2026E Adjusted EBITDA of $118.0m. H1 2026 actuals are already far behind that, so the price is about 15.1x LTM company-defined Adjusted EBITDA and 18.6x diligence-adjusted LTM EBITDA.
- **Evidence:**
  - **Price and enterprise value:**
    - Equity value = 24.00 x 48.3 = 1,159.2.
    - Net debt at June 30, 2026 = (45.0 + 182.5) - 33.9 = 193.6.
    - EV = 1,159.2 + 193.6 = 1,352.8.
  - **Multiples at that EV:**
    - EV / FY2026E Adjusted EBITDA = 1,352.8 / 118.0 = 11.46x. This confirms the brief's 11.5x.
    - EV / FY2026E revenue = 1,352.8 / 560.0 = 2.42x.
    - EV / FY2025 Adjusted EBITDA = 1,352.8 / 98.8 = 13.7x.
    - EV / LTM Adjusted EBITDA = 1,352.8 / 89.7 = 15.1x.
    - EV / LTM diligence-adjusted EBITDA A = 1,352.8 / 72.6 = 18.6x.
    - EV / LTM diligence-adjusted EBITDA B (after SBC) = 1,352.8 / 54.8 = 24.7x.
    - EV / LTM EBITDA = 1,352.8 / 48.2 = 28.1x.
    - EV / LTM revenue = 1,352.8 / 498.4 = 2.71x.
  - **Revenue needed in H2 2026 to reach the management case:**
    - Required H2 2026 revenue = 560.0 - 222.6 = 337.4.
    - That is 337.4 / 275.8 = +22.3% on H2 2025 (121.4 + 154.4 = 275.8), and 337.4 / 222.6 = +51.6% on H1 2026.
    - H1 2026 itself was -1.7% year over year.
  - **Adjusted EBITDA needed in H2 2026 to reach the management case:**
    - Required H2 2026 Adjusted EBITDA = 118.0 - 29.9 = 88.1.
    - That is 88.1 / 59.8 = +47.3% on H2 2025 (98.8 - 39.0 = 59.8).
    - It implies an H2 margin of 88.1 / 337.4 = 26.1%, against 13.4% in H1 2026 and 19.7% in FY2025.
  - **My FY2026 run-rate range for revenue:**
    - Low: H2 2025 excluding the estimated Q4 spike (see FIN-02) is 275.8 - 21.0 = 254.8. At the H1 trend of -1.7% that gives 250.4, so FY2026 = 473.0.
    - High: H2 2026 flat on H2 2025 gives FY2026 = 498.4.
    - Shortfall against 560.0 is 61.6 to 87.0, or 11.0% to 15.5%.
  - **My FY2026 run-rate range for Adjusted EBITDA:**
    - H1 2026 annualized = 29.9 x 2 = 59.8.
    - H2 2026 flat on H2 2025 gives FY2026 = 29.9 + 59.8 = 89.7.
    - Shortfall against 118.0 is 28.3 to 58.2, or 24% to 49%.
  - **Value at the deal's own 11.5x on actual earnings:**
    - LTM Adjusted EBITDA: 89.7 x 11.5 = 1,031.6 EV. Less net debt of 193.6 gives equity of 838.0, or $17.35 per share.
    - Diligence-adjusted EBITDA A: 72.6 x 11.5 = 834.9 EV. Less net debt gives equity of 641.3, or $13.28 per share.
  - **Market check:**
    - Unaffected equity = 17.85 x 48.3 = 862.2, plus net debt 193.6 = EV of 1,055.8.
    - That is 1,055.8 / 89.7 = 11.8x LTM Adjusted EBITDA.
    - The market already prices Talonfield at about the deal multiple on actual LTM earnings, not on the FY2026E case.
  - **Synergies:** EV / (LTM Adjusted EBITDA 89.7 + 35.0 synergies) = 1,352.8 / 124.7 = 10.8x. Even fully credited, the synergies do not close the gap to 11.5x on diligence-adjusted EBITDA: 1,352.8 / (72.6 + 35.0) = 12.6x.
- **Source:** `data/financials/adjusted_ebitda_reconciliation.csv` (Adjusted EBITDA row, all columns); `income_statement.csv` (Total revenue, Diluted shares); `revenue_quarterly.csv` (Q3 2025, Q4 2025); `balance_sheet.csv` (Cash, Revolver, Term loan, Q2_2026); `data/deal-brief.md` (price, shares, management case).
- **Severity:** Critical. The EBITDA base is overstated by more than 10%. At 11.5x, the implied value gap is 1,352.8 - 1,031.6 = 321.2, or 23.7% of EV, before any diligence adjustments.
- **Confidence:** High for the recomputed multiples and the H2 gap, which are calculated directly. Medium for the run-rate range, which depends on scenario assumptions.
- **Deal impact:** Valuation (price), financing (lender sizing on EBITDA).
- **Cross-check:** Any guidance update or reaffirmation of the $560.0m / $118.0m case since March 2026 in the 10-Q or 8-K filings. Analyst and news commentary on the H1 2026 miss.

#### FIN-02: Reported FY2025 growth depends on one unusual quarter, Q4 2025, which matches the growth at the top customer
- **Finding:** Q4 2025 revenue jumped 32.4% year over year, against about 14% in each of Q1 to Q3 2025. That one quarter supplied 46.9% of FY2025 revenue growth. The size of the jump is almost the same as Norvale's revenue increase, which suggests a large one-off or pulled-forward Norvale delivery. Excluding the estimated spike, FY2025 growth is about 14.1%, not 19.1%.
- **Evidence:**
  - **Year-over-year growth by quarter:**
    - Q1 2025: 108.9 / 96.2 = +13.2%.
    - Q2 2025: 117.6 / 102.8 = +14.4%.
    - Q3 2025: 121.4 / 106.1 = +14.4%.
    - Q4 2025: 154.4 / 116.6 = +32.4%.
    - Q1 2026: 109.7 / 108.9 = +0.7%.
    - Q2 2026: 112.9 / 117.6 = -4.0%.
  - **Q4 against Q3:** Q4 2025 was +27.2% on Q3 2025 (154.4 / 121.4). The same comparison in 2024 was +9.9% (116.6 / 106.1).
  - **Q4 share of growth:**
    - FY2025 increase = 502.3 - 421.7 = 80.6.
    - Q4 increase = 154.4 - 116.6 = 37.8, which is 46.9% of the total.
    - Q4 2025 was 30.7% of the year's revenue (154.4 / 502.3), against 27.6% in FY2024 (116.6 / 421.7).
  - **My estimate of the spike:**
    - Normal Q4 = Q4 2024 grown at the Q1 to Q3 2025 rate: 116.6 x 1.144 = 133.4. Using the 2024 Q3-to-Q4 pattern gives the same figure: 121.4 x 1.099 = 133.4.
    - Excess = 154.4 - 133.4 = 21.0.
    - Underlying FY2025 revenue = 502.3 - 21.0 = 481.3, so underlying growth = 481.3 / 421.7 = +14.1%.
  - **Link to Norvale:**
    - Norvale's increase = 156.2 - 118.1 = 38.1. That is 47.3% of FY2025 growth and almost equal to the Q4 increase of 37.8.
    - Revenue excluding Norvale grew 14.0%: (502.3 - 156.2) / (421.7 - 118.1) = 346.1 / 303.6.
  - **Supporting signals in the same period:**
    - Contract assets (unbilled) rose 142%, from 10.2 to 24.7.
    - The receivables allowance fell (see FIN-05).
    - Hardware backlog fell 22.0%, from 168.0 to 131.0.
    - Units shipped rose 30.3% while hardware revenue per unit fell (see FIN-12).
    - A $4.1m "customer implementation delays" add-back appears in FY2025.
- **Source:** `revenue_quarterly.csv` (all rows); `revenue_by_customer.csv` (Norvale, Total); `balance_sheet.csv` (Contract assets); `kpis.csv` (Hardware order backlog, Robots shipped).
- **Severity:** High
- **Confidence:** Medium. The quarterly growth figures are calculated directly. The size of the one-off ($21.0m) and its link to Norvale are inferences, because no quarterly customer or segment data was provided.
- **Deal impact:** Valuation (growth narrative and run-rate). Possible revenue recognition and accounting risk.
- **Cross-check:**
  - SEC filings: the 10-K or 10-Q revenue recognition note, any disclosed one-off or large Q4 2025 order, bill-and-hold or acceptance terms, and the Norvale contract.
  - News: Norvale rollout, pull-forward or contract renegotiation.
  - If the SEC analyst finds a disclosed one-off amount, it should replace my $21.0m estimate.

#### FIN-03: H1 2026 revenue is falling, led by hardware, and the order book is shrinking
- **Finding:** H1 2026 revenue fell 1.7%. Hardware fell 12.9%. Hardware orders are running below revenue (book-to-bill below 1.0 for six quarters), so further hardware decline is likely.
- **Evidence:**
  - **Hardware revenue:** H1 2026 vs H1 2025 = 116.9 / 134.2 = -12.9%.
  - **Hardware book-to-bill:** orders = hardware revenue + change in backlog. This assumes the backlog is hardware only, as labelled.
    - FY2024: 261.9 + (168.0 - 142.0) = 287.9; book-to-bill 287.9 / 261.9 = 1.10.
    - FY2025: 301.4 + (131.0 - 168.0) = 264.4; book-to-bill 0.88.
    - H1 2026: 116.9 + (118.0 - 131.0) = 103.9; book-to-bill 0.89.
    - H1 2026 orders annualized = 207.8, which is -21.4% against FY2025 orders of 264.4.
  - **Backlog:** 168.0 at December 2024 to 118.0 at June 2026 = -29.8%.
  - **Units:** H1 2026 shipments of 1,640 annualize to 3,280, -23.7% against 4,300.
  - **Active customers:** added only 5 in H1 2026 (276 to 281), against 28 in FY2025.
- **Source:** `income_statement.csv` (Revenue: Hardware, H1 columns); `kpis.csv` (backlog, robots shipped, active customers); `revenue_quarterly.csv` (Q1 to Q2 2026).
- **Severity:** High
- **Confidence:** High for the figures, which are calculated directly. Medium for book-to-bill, which assumes how the backlog is defined.
- **Deal impact:** Valuation, post-closing performance.
- **Cross-check:** The backlog definition in the 10-K or 10-Q. Management commentary on order delays. News on lost deals, competitor wins or customer pauses (especially Norvale).

#### FIN-04: Adjusted EBITDA add-backs are large, growing and partly recurring; diligence-adjusted LTM EBITDA is $72.6m against $89.7m reported
- **Finding:** Add-backs rose from 30.1% of Adjusted EBITDA in FY2023 to 46.3% in LTM and 65.2% in H1 2026. Restructuring has been added back in every period since FY2022. Litigation costs recur. "Customer implementation delays" is a normal operating cost.
- **Evidence:**
  - **Add-backs as a share of Adjusted EBITDA** (add-backs = Adjusted EBITDA - EBITDA):
    - FY2023: 18.2 / 60.4 = 30.1%.
    - FY2024: 22.5 / 74.8 = 30.1%.
    - FY2025: 34.7 / 98.8 = 35.1%.
    - H1 2026: 19.5 / 29.9 = 65.2%.
    - LTM: 41.5 / 89.7 = 46.3%.
  - **Restructuring "and other charges":**
    - 3.1 (FY2022), 4.6, 5.2, 7.9 (FY2025), 4.4 (H1 2026). Cumulative 25.2.
    - The amount rises every year. I treat it as recurring.
  - **Vantor patent litigation costs:**
    - 0.8 (FY2024), 2.1 (FY2025), 3.0 (H1 2026), 4.1 LTM.
    - The cost is ongoing and rising while the case is live. I treat it as recurring until the case resolves.
  - **Customer implementation delays:**
    - 4.1 in FY2025, 3.3 in LTM.
    - Delivery delays with customers are part of operating cost. I do not accept this add-back.
  - **Accepted as plausibly one-off** (subject to checking the facts):
    - Auditor transition 2.3.
    - Executive search / CFO transition 1.1 (FY2025) and 1.4 (H1 2026).
    - Cybersecurity incident 1.8.
    - Lumora deal costs 2.6, ERP 2.0, secondary offering 1.2.
    - Note that the "one-off" category recurs: a new item appears every year.
  - **Diligence-adjusted EBITDA A:**
    - FY2025: 98.8 - 7.9 - 4.1 - 2.1 = 84.7.
    - LTM: 89.7 - 9.7 - 3.3 - 4.1 = 72.6.
    - H1 2026: 29.9 - 4.4 - 0.0 - 3.0 = 22.5.
    - FY2024: 74.8 - 5.2 - 0.8 = 68.8.
    - FY2023: 60.4 - 4.6 = 55.8.
  - **Diligence-adjusted EBITDA B (also treating SBC as a real cost):** FY2025 84.7 - 17.2 = 67.5; LTM 72.6 - 17.8 = 54.8.
  - **Sensitivity:** if the estimated $21.0m Q4 2025 excess revenue (FIN-02) is removed at the FY2025 gross margin of 41.1%, LTM A falls by about 8.6, to about 64.0. This is an estimate and assumes no related operating costs.
- **Source:** `adjusted_ebitda_reconciliation.csv` (all rows and columns); `income_statement.csv` (Restructuring and other charges, Memo: SBC).
- **Severity:** High
- **Confidence:** High for the arithmetic. Medium for which add-backs to reject, which is a judgment call pending a quality of earnings report (none has been received, per `data/financials/README.md`).
- **Deal impact:** Valuation (the EBITDA base for the multiple). Financing (covenant EBITDA definitions).
- **Cross-check:**
  - SEC filings: the non-GAAP reconciliation and how the company explains each item.
  - Litigation records: Vantor case status and likely duration.
  - News and SEC filings: the cybersecurity incident, the CFO departure and the auditor change. Was each one disclosed, and when (8-K Item 1.05, 5.02, 4.01)?

#### FIN-05: Receivables and unbilled contract assets jumped in FY2025 while the credit-loss reserve fell
- **Finding:** DSO rose from 63.5 to 86.4 days in FY2025. Contract assets more than doubled. The allowance for credit losses fell from 3.8% to 2.1% of gross receivables. This pattern fits aggressive revenue recognition or slower collections, and receivables may be under-reserved.
- **Evidence:**
  - **DSO** (net AR / revenue x 365):
    - FY2023: 61.0 / 368.9 x 365 = 60.4.
    - FY2024: 73.4 / 421.7 x 365 = 63.5.
    - FY2025: 118.9 / 502.3 x 365 = 86.4.
    - June 2026: 104.2 / (222.6 x 2) x 365 = 85.4 on H1 annualized, or 76.3 on LTM revenue of 498.4.
  - **DSO including contract assets:**
    - FY2024: 83.6 / 421.7 x 365 = 72.4.
    - FY2025: 143.6 / 502.3 x 365 = 104.3.
    - June 2026: 123.7 / 445.2 x 365 = 101.4.
  - **Growth in FY2025:** AR plus contract assets grew 71.8% (83.6 to 143.6), against revenue growth of 19.1%.
  - **Allowance / gross AR:** FY2023 2.5 / 63.5 = 3.9%; FY2024 2.9 / 76.3 = 3.8%; FY2025 2.6 / 121.5 = 2.1%; June 2026 3.4 / 107.6 = 3.2%.
    - In FY2025, gross AR rose 59.2% while the allowance fell 10.3%.
    - Holding the FY2024 rate of 3.8% gives a reserve of 121.5 x 3.8% = 4.6 at FY2025, so the shortfall is about 2.0. At June 2026 the shortfall is 107.6 x 3.8% - 3.4 = 0.7.
  - **Contract assets:** 10.2 to 24.7 (+142.2%). As a share of revenue, 2.4% to 4.9%.
  - **Partial reversal in H1 2026:** 14.7 of AR and 5.2 of contract assets were collected or billed. Both are still far above FY2024 levels.
- **Source:** `balance_sheet.csv` (AR net, Contract assets, Memo: AR gross, Memo: Allowance); `income_statement.csv` (Total revenue); `cash_flow.csv` (Change in AR, Change in contract assets).
- **Severity:** High
- **Confidence:** High for the arithmetic. Medium for what it means, because no AR aging or customer-level AR was provided.
- **Deal impact:** Valuation, closing working capital peg, possible accounting restatement risk.
- **Cross-check:**
  - SEC filings: credit-loss policy changes, contract asset disclosures, and any auditor critical audit matter on revenue.
  - Whether the Norvale balance makes up most of AR.
  - Whether the auditor change relates to revenue or AR issues.

#### FIN-06: Cash conversion collapsed; free cash flow is negative in FY2025, H1 2026 and LTM
- **Finding:** Operating cash flow fell from 78% of EBITDA in FY2024 to 15% in FY2025 and turned negative in H1 2026. LTM free cash flow is -$26.4m.
- **Evidence:**
  - **OCF / EBITDA:** FY2023 30.8 / 42.2 = 73.0%; FY2024 40.8 / 52.3 = 78.0%; FY2025 9.7 / 64.1 = 15.1%; H1 2026 -4.2 / 10.4 = -40.4%.
  - **OCF / Adjusted EBITDA:** FY2024 54.5%; FY2025 9.8%; H1 2026 -14.0%.
  - **OCF / net income:** FY2023 2.68x; FY2024 2.68x; FY2025 9.7 / 18.6 = 0.52x.
  - **Free cash flow:** 16.2, 24.6, -10.1, then -13.0 in H1 2026 (against +3.3 in H1 2025). LTM -26.4.
  - **Why H1 2026 OCF was negative even after 19.9 of AR and contract asset inflow:**
    - Inventory was a 12.7 outflow.
    - Payables, accruals and deferred revenue were a 22.6 outflow. On the balance sheet: AP 46.2 to 38.6, accrued liabilities 38.5 to 30.5, and total deferred revenue 56.9 to 50.2.
- **Source:** `cash_flow.csv` (all rows); `adjusted_ebitda_reconciliation.csv` (EBITDA, Adjusted EBITDA); `balance_sheet.csv`.
- **Severity:** High
- **Confidence:** High, calculated directly.
- **Deal impact:** Valuation (cash-based value), financing, post-closing funding need.
- **Cross-check:** The liquidity discussion in the 10-Q MD&A. Any going-concern or liquidity risk factor language.

#### FIN-07: Debt and revolver use are rising while cash and earnings fall; LTM net debt / EBITDA is 4.0x
- **Finding:** The revolver went from 0.0 to 45.0 in 30 months. Cash fell to 33.9. Leverage is 2.16x on company-defined Adjusted EBITDA but 4.02x on EBITDA. EBIT covers interest only 1.36x on an LTM basis.
- **Evidence:**
  - **Net debt:** FY2023 65.2; FY2024 151.7; FY2025 178.4; June 2026 193.6.
  - **Leverage at June 2026:**
    - Net debt / LTM Adjusted EBITDA = 193.6 / 89.7 = 2.16x.
    - Net debt / LTM EBITDA = 193.6 / 48.2 = 4.02x.
    - Gross debt / LTM EBITDA = 227.5 / 48.2 = 4.72x.
    - Net debt / LTM diligence-adjusted EBITDA A = 193.6 / 72.6 = 2.67x.
    - Gross debt / LTM diligence-adjusted EBITDA A = 227.5 / 72.6 = 3.13x.
  - **Interest cover (LTM interest 14.9 = 13.6 - 6.6 + 7.9):**
    - Adjusted EBITDA: 89.7 / 14.9 = 6.02x.
    - EBITDA: 48.2 / 14.9 = 3.23x.
    - EBIT: LTM operating income = 37.3 - 13.3 + (-3.7) = 20.3, so 20.3 / 14.9 = 1.36x.
    - H1 2026 EBIT of -3.7 does not cover interest of 7.9.
  - **Implied interest rate:** 14.9 / average debt of (220.0 + 227.5) / 2 = 6.7%.
  - **Interest expense trend:** H1 2026 vs H1 2025 = 7.9 / 6.6 = +19.7%.
  - **Runway:**
    - Cash runway: 33.9 / (13.0 / 6) = 15.6 months of H1 2026 free cash flow burn.
    - Including term loan amortization of 2.5 per half: 33.9 / ((13.0 + 2.5) / 6) = 13.1 months, before any further revolver draws.
    - Revolver capacity is not in the data, so headroom cannot be computed.
  - **Covenant ratios:** no covenant definitions were provided. The definitions I used: total debt = revolver + term loan; net debt = total debt - cash; EBITDA as in the company's reconciliation file. Finance lease liabilities may exist (a 0.7 finance lease payment appears in H1 2026) but are not separately shown. If the credit agreement uses company Adjusted EBITDA, the ratio is about 2.2x. On EBITDA it is about 4.0x. The difference is the whole question for covenant headroom.
- **Source:** `balance_sheet.csv` (Cash, Revolving credit facility, Term loan); `cash_flow.csv` (financing rows, Memo FCF); `income_statement.csv` (Interest expense, Operating income); `adjusted_ebitda_reconciliation.csv`.
- **Severity:** High
- **Confidence:** High for the ratios. Low for covenant headroom, because the definition and limits are missing.
- **Deal impact:** Financing, closing risk (a covenant breach before closing), and debt to repay or assume at closing.
- **Cross-check:**
  - SEC filings (10-K debt note and credit agreement exhibit): covenant definition, maximum leverage, revolver size, maturity, change-of-control prepayment and any amendments or waivers in 2026.
  - The lead agent should send me the covenant definition so I can compute headroom.

#### FIN-08: One customer, Norvale, is 31.1% of revenue and supplied 47% of FY2025 growth
- **Finding:** Norvale's share rose from 28.0% to 31.1%. The top 10 rose from 59.2% to 61.5%. Excluding Norvale, growth was 14.0%. No 2026 customer data was provided, so any decline at Norvale in H1 2026 cannot be measured.
- **Evidence:**
  - **Norvale:** 118.1 to 156.2, +32.3% (156.2 / 118.1).
  - **Top 10:** FY2024 249.6 / 421.7 = 59.2%; FY2025 308.8 / 502.3 = 61.5%.
  - **Top 3 in FY2025:** (156.2 + 41.2 + 28.9) / 502.3 = 45.1%.
  - **Customers ranked 2 to 10:** share fell from 31.2% (131.5) to 30.4% (152.6). Each of them grew in dollars but grew more slowly than Norvale.
    - Pinecrest grew the least: +7.4% (17.4 / 16.2), with share down from 3.8% to 3.5%.
    - Quillon: +14.4%, share 8.5% to 8.2%.
    - Ardent: +14.2%, share 6.0% to 5.8%.
  - No top-10 customer fell in dollar terms in FY2025.
- **Source:** `revenue_by_customer.csv` (all rows).
- **Severity:** High. Critical if other sources show the Norvale relationship is at risk.
- **Confidence:** High for concentration, calculated directly. Low for any H1 2026 trend (no data).
- **Deal impact:** Valuation, post-closing (change-of-control clauses), closing condition.
- **Cross-check:**
  - SEC filings: the concentration risk factor, whether the Norvale contract has been filed, and its term, renewal and change-of-control terms.
  - News: Norvale vendor reviews, insourcing or a competitor pilot.
  - Litigation records: any dispute with Norvale.

#### FIN-09: FieldOS software is still growing, but retention and new ARR are slowing sharply
- **Finding:** Software is the best part of the business (+14.6% in H1 2026). However, NRR fell 7 points to 111% in six months, and net new ARR in H1 2026 was about half the FY2025 pace. Software does not support a re-acceleration case.
- **Evidence:**
  - **ARR growth:** FY2024 109.5 / 86.0 = +27.3%; FY2025 139.2 / 109.5 = +27.1%; H1 2026 146.8 / 139.2 = +5.5%, about 11.2% annualized (1.055 x 1.055 - 1).
  - **Net new ARR:** FY2024 23.5; FY2025 29.7; H1 2026 7.6, against a half-year pace of 29.7 / 2 = 14.9 (51% of pace).
  - **NRR:** 121% to 119% to 118% to 111%.
  - **Software revenue growth:** FY2025 +27.1%; H1 2026 +14.6% (67.5 / 58.9).
  - **Deferred revenue:** total fell from 56.9 to 50.2 (-11.8%) in H1 2026 while ARR rose. This may be billing seasonality, but no June 2025 balance sheet was provided to test that.
  - Churn and gross retention are not provided.
- **Source:** `kpis.csv` (ARR, NRR); `income_statement.csv` (Revenue: Software); `balance_sheet.csv` (Deferred revenue rows).
- **Severity:** Medium
- **Confidence:** High for the figures. Medium for the deferred revenue reading.
- **Deal impact:** Valuation (the recurring revenue premium).
- **Cross-check:** ARR and NRR definitions in the filings. News on FieldOS customer losses, pricing or competition.

#### FIN-10: Margins compressed in H1 2026; operating costs grew while headcount fell
- **Finding:** Gross margin fell 2.8 points to 38.0%. Operating expenses rose 11.6% on falling revenue, so Talonfield made an operating loss in H1 2026.
- **Evidence:**
  - **Gross margin:**
    - FY2022 39.0%; FY2023 40.1%; FY2024 40.8%; FY2025 41.1%.
    - H1 2025: 92.4 / 226.5 = 40.8%. H1 2026: 84.6 / 222.6 = 38.0%.
  - **Operating expenses:** 79.1 to 88.3 = +11.6%.
    - G&A: 16.2 to 19.8 = +22.2%.
    - R&D: +6.6%. Sales and marketing: +6.0%.
    - Headcount fell 3.2% (1,452 to 1,405) over the same period.
  - **Operating margin:** FY2025 37.3 / 502.3 = 7.4%; H1 2026 -3.7 / 222.6 = -1.7%.
  - **EBITDA margin:** H1 2025 11.6%; H1 2026 4.7%.
  - Segment gross margins are not provided, so I cannot tell whether hardware pricing or software mix is driving the decline.
- **Source:** `income_statement.csv` (all rows); `kpis.csv` (Full-time employees).
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation, post-closing (synergy base).
- **Cross-check:** The 10-Q MD&A explanation of gross margin (pricing, warranty, freight, mix). What drives G&A, for example legal, audit, cyber or CFO transition costs.

#### FIN-11: Inventory is building while hardware sales and backlog fall
- **Finding:** Inventory rose 17.8% in H1 2026 to $84.0m, while hardware revenue fell 12.9% and backlog fell 9.9%. Days inventory rose to about 111. This points to obsolescence or write-down risk.
- **Evidence:**
  - **Inventory:** 71.3 to 84.0 (84.0 / 71.3 = +17.8%).
  - **DIO** (inventory / cost of revenue x 365):
    - FY2023: 55.2 / 221.0 x 365 = 91.2.
    - FY2024: 63.9 / 249.6 x 365 = 93.4.
    - FY2025: 71.3 / 296.0 x 365 = 87.9.
    - June 2026: 84.0 / (138.0 x 2) x 365 = 111.1.
  - **Backlog:** 131.0 to 118.0.
  - **Cash effect:** the inventory build was a 12.7 cash outflow in H1 2026.
- **Source:** `balance_sheet.csv` (Inventory); `income_statement.csv` (Cost of revenue); `kpis.csv` (backlog); `cash_flow.csv` (Change in inventory).
- **Severity:** Medium
- **Confidence:** High for the figures. Medium for the write-down risk, because no inventory aging or reserve was provided.
- **Deal impact:** Valuation, working capital peg.
- **Cross-check:** The inventory reserve policy and any write-downs in the 10-Q. Supplier or component news, for example a product transition that would make stock obsolete.

#### FIN-12: Hardware revenue per robot fell about 12% in FY2025, despite a 30% unit surge
- **Finding:** FY2025 units rose 30.3%, but hardware revenue rose only 15.1%. This suggests discounting or large-customer pricing, possibly linked to the Norvale rollout and the Q4 spike.
- **Evidence:**
  - **Hardware revenue per unit:**
    - FY2023: 236.0 / 3,020 = $78.1k.
    - FY2024: 261.9 / 3,300 = $79.4k.
    - FY2025: 301.4 / 4,300 = $70.1k (-11.7%).
    - H1 2026: 116.9 / 1,640 = $71.3k.
  - **Installed base:** reconciles each year (e.g. 13,100 + 4,300 = 17,400). This implies no units retired.
- **Source:** `kpis.csv` (Robots shipped, Installed base); `income_statement.csv` (Revenue: Hardware).
- **Severity:** Medium
- **Confidence:** Medium. Hardware revenue may include items other than robots.
- **Deal impact:** Valuation (price and margin sustainability).
- **Cross-check:** Norvale contract pricing terms. Any volume rebates disclosed. News on price competition.

#### FIN-13: Share buybacks were funded with debt while free cash flow was negative
- **Finding:** In FY2025 Talonfield repurchased $13.3m of stock and paid $4.1m of taxes on net share settlement. Free cash flow was -$10.1m that year, and the revolver was drawn by $25.0m. The FY2024 buyback of $25.0m was made in the same year as $80.0m of new borrowing.
- **Evidence:**
  - FY2025 financing: -5.0 + 25.0 - 13.3 - 4.1 + 0.8 = 3.4.
  - FY2025 cash outflows: free cash flow -10.1 plus buybacks and withholding taxes of 17.4 = 27.5. This was largely funded by the net 20.0 debt increase and a 6.7 fall in cash.
  - No repurchases were made in H1 2026.
- **Source:** `cash_flow.csv` (Repurchases, Revolver, Term loan, Memo FCF).
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Governance (capital allocation), financing.
- **Cross-check:** Board buyback authorizations in the filings. Insider share sales around the buybacks (Form 4). Proxy statement compensation metrics tied to EPS.

#### FIN-14: The add-back schedule points to events that need a disclosure check
- **Finding:** The Adjusted EBITDA detail lists a cybersecurity incident ($1.8m, H1 2026), a CFO transition ($1.1m FY2025 and $1.4m H1 2026), an auditor transition ($2.3m, FY2025) and Vantor patent litigation ($5.9m cumulative). Each is a governance or legal signal, not only a cost item.
- **Evidence:**
  - Vantor litigation cumulative: 0.8 + 2.1 + 3.0 = 5.9.
  - The other amounts are taken directly from the detail rows.
- **Source:** `adjusted_ebitda_reconciliation.csv` (Detail rows 16 to 20).
- **Severity:** Medium. This may be raised once the other workstreams report.
- **Confidence:** High that the costs exist. Low on the underlying facts from this data.
- **Deal impact:** Closing risk, indemnity, internal controls.
- **Cross-check:**
  - 8-K Item 1.05 (cyber), Item 5.02 (CFO) and Item 4.01 (auditor change, including any reported disagreements or material weakness), and their timing against the events.
  - Court records for Vantor (claimed damages, injunction risk).

#### FIN-15: Tangible equity is negative, and goodwill from the Lumora deal is exposed to impairment
- **Finding:** Goodwill plus intangibles of $132.5m exceed equity of $92.0m. The H1 2026 loss and falling backlog raise the risk of a goodwill impairment test. Lumora's revenue contribution to FY2024 and FY2025 growth is not disclosed in the data, so organic growth cannot be isolated.
- **Evidence:**
  - Goodwill plus intangibles at June 2026 = 98.4 + 34.1 = 132.5. Tangible equity = 92.0 - 132.5 = -40.5.
  - Lumora was bought for 85.0 in FY2024. Goodwill rose 57.4 that year (41.0 to 98.4).
- **Source:** `balance_sheet.csv` (Goodwill, Intangibles, Equity); `cash_flow.csv` (Acquisition of Lumora Vision).
- **Severity:** Low
- **Confidence:** High for the figures. Low for impairment.
- **Deal impact:** Accounting and purchase price allocation (PPA). The organic growth picture.
- **Cross-check:** Lumora purchase price allocation and revenue contribution in the 10-K acquisition note. Impairment testing disclosures.

#### FIN-16: The D&A roll-forward does not reconcile, and capitalized costs are not disclosed
- **Finding:** Depreciation implied by the PP&E and intangibles movements is about $5.7m less than reported D&A in FY2025, and about $3.3m less in H1 2026. Capitalized software or other assets may sit outside the visible lines. There is no data on capitalized development costs.
- **Evidence:**
  - **FY2025:**
    - Implied PP&E depreciation = 47.1 + 19.8 - 52.0 = 14.9.
    - Intangible amortization = 43.4 - 37.2 = 6.2.
    - Sum 21.1 against reported D&A of 26.8, a gap of 5.7.
  - **H1 2026:**
    - Implied depreciation = 52.0 + 8.8 - 53.1 = 7.7.
    - Amortization = 3.1.
    - Sum 10.8 against reported D&A of 14.1, a gap of 3.3.
  - **Caveats:** disposals, leases and capitalized items may explain the gap.
  - **Capex intensity:** stable at about 4% of revenue (FY2025 19.8 / 502.3 = 3.9%).
- **Source:** `balance_sheet.csv` (PP&E, Intangibles); `cash_flow.csv` (Capex, D&A); `income_statement.csv` (Memo D&A).
- **Severity:** Low
- **Confidence:** Medium, because the cause of the gap is unknown.
- **Deal impact:** Earnings quality (capitalization inflates EBITDA).
- **Cross-check:** The capitalized software policy and the fixed-asset roll-forward in the 10-K.

#### FIN-17: The 48.3m diluted share count may understate dilution at $24.00
- **Finding:** H1 2026 diluted shares (48.3m) are reported in a loss period, so they probably exclude dilutive awards. At a $24.00 cash price, in-the-money options and RSUs could add to the equity value. The size is unknown.
- **Evidence:**
  - Diluted EPS -8.9 / 48.3 = -0.18, which matches the reported figure.
  - FY2025 diluted shares were 47.8m. SBC of 17.2 a year suggests a meaningful pool of awards.
- **Source:** `income_statement.csv` (Diluted shares, Diluted EPS, Memo SBC).
- **Severity:** Low
- **Confidence:** Low, directional only.
- **Deal impact:** Valuation (equity value bridge).
- **Cross-check:** The equity award table in the 10-K or proxy. Treasury-method dilution at $24.00.

### Positive or mitigating points

- **Software and services are growing.** FieldOS revenue rose 14.6% and services 14.4% in H1 2026. ARR reached $146.8m, and software is now 30.3% of revenue (67.5 / 222.6), up from 26.0% in H1 2025 (58.9 / 226.5).
- **Recurring revenue base.** Software ARR of $146.8m plus services gives a base that does not depend on hardware orders. NRR of 111% is still above 100%.
- **Collections started in H1 2026.** AR fell by $14.7m and contract assets by $5.2m from the December 2025 peak.
- **Leverage is moderate on the company's own measure.** Net debt / LTM Adjusted EBITDA is 2.16x, and the term loan is amortizing (190.0 to 182.5).
- **The data is internally consistent.** Every statement reconciles (see Files reviewed), and no embedded instructions were found.
- **Cost action under way.** Headcount fell 47 in H1 2026, which may support H2 margins.
- **The deal model's net debt figure is current.** My EV of 1,352.8 reproduces the brief's 11.5x. The problem is the EBITDA base, not the debt figure.

### Gaps and questions for management

1. Quarterly revenue by segment and by customer for Q4 2025 to Q2 2026. What made up the $154.4m in Q4 2025, and how much was Norvale? Were there any bill-and-hold, early delivery or acceptance-waiver arrangements?
2. Norvale H1 2026 revenue, the contract term, renewal date, change-of-control and termination clauses, and its AR balance at December 2025 and June 2026.
3. AR aging at December 2025 and June 2026. What drives contract assets? Why was the allowance cut in FY2025?
4. The credit agreement: covenant definitions (which EBITDA), maximum leverage and minimum interest cover, revolver commitment and availability, maturities, any 2026 amendments or waivers, and change-of-control terms.
5. An updated FY2026 forecast against the March 2026 case of $560.0m / $118.0m. What supports H2 revenue of $337.4m (+22.3% year over year)?
6. Backlog definition, order intake by quarter, and cancellations.
7. Segment gross margins, and what drove the gross margin fall to 38.0%.
8. Support for each Adjusted EBITDA add-back. Why are restructuring and "customer implementation delays" treated as non-recurring? What is the budget for Vantor litigation costs until the case ends?
9. Inventory aging, reserves, and the reason for the H1 2026 build.
10. ARR, NRR, gross retention and churn definitions, and logo churn by quarter.
11. Lumora revenue and EBITDA contribution in FY2024 and FY2025 (organic growth).
12. The capitalized software and development cost policy and amounts, and a fixed-asset and D&A roll-forward.
13. The June 30, 2025 balance sheet, for year-over-year working capital and deferred revenue comparisons.
14. The full equity award schedule (options, RSUs, PSUs) for a fully diluted share count at $24.00.
15. Lease liabilities and other debt-like items (earn-outs, litigation accruals) for the EV bridge.
16. A quality of earnings report (not yet received, per `data/financials/README.md`).

Source files: all in `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/financials/`, plus `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md`.
