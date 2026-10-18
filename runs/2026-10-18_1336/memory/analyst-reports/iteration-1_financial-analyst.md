# Iteration 1: financial-analyst (full report, unedited)

## Financial analyst: findings

Talonfield's FY2025 results look much better than the business really is. The FY2025 jump comes mostly from an unusual Q4 2025. Revenue then fell in H1 2026, while margins, cash flow and the forward KPIs all got worse. The management case in the deal model (FY2026E revenue $560.0M, Adjusted EBITDA $118.0M) needs H2 2026 Adjusted EBITDA 47.3% above H2 2025. Nothing in the data supports that. On reported LTM Adjusted EBITDA, the $24.00 price is 15.1x, not 11.5x. On my diligence-adjusted LTM figure it is 18.6x.

### Files reviewed

- `data/deal-brief.md` (context only)
- `data/financials/README.md`
- `data/financials/income_statement.csv`
- `data/financials/revenue_quarterly.csv`
- `data/financials/adjusted_ebitda_reconciliation.csv`
- `data/financials/balance_sheet.csv`
- `data/financials/cash_flow.csv`
- `data/financials/revenue_by_customer.csv`
- `data/financials/kpis.csv`

Integrity checks I ran:
- Quarterly revenue adds up to the annual and H1 totals.
- The balance sheets balance.
- Equity rolls forward correctly. FY2025: 74.3 + 18.6 + 17.2 - 13.3 - 4.1 + 0.8 = 93.5.
- The cash flow statements reconcile to cash.
- Reported EBITDA (operating income + D&A) and Adjusted EBITDA recompute exactly for every period, including LTM.
- Net AR = gross AR - allowance in every period.

No embedded instructions or prompt-injection text was found in any file.

No other sources were provided by the lead agent. No covenant definition is available, so I show leverage on both bases.

### Key metrics table

US$ millions. **Reported** = company presentation. **Adjusted** = my diligence figures. "LTM" = twelve months to June 30, 2026 (LTM = FY2025 - H1 2025 + H1 2026).

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 | LTM Q2 2026 |
|---|---|---|---|---|---|
| Total revenue (reported) | 368.9 | 421.7 | 502.3 | 222.6 | 498.4 |
| Revenue growth YoY | 18.1% | 14.3% | 19.1% | -1.7% | n/a |
| Hardware growth | 15.1% | 11.0% | 15.1% | -12.9% | n/a |
| Software (FieldOS) growth | 29.1% | 25.9% | 27.1% | 14.6% | n/a |
| Services growth | 16.7% | 11.6% | 23.4% | 14.4% | n/a |
| Gross margin | 40.1% | 40.8% | 41.1% | 38.0% (H1 2025: 40.8%) | n/a |
| EBITDA (reported, unadjusted) | 42.2 | 52.3 | 64.1 | 10.4 | 48.2 |
| EBITDA margin | 11.4% | 12.4% | 12.8% | 4.7% | 9.7% |
| Adjusted EBITDA (company) | 60.4 | 74.8 | 98.8 | 29.9 | 89.7 |
| Adjusted EBITDA margin (company) | 16.4% | 17.7% | 19.7% | 13.4% | 18.0% |
| Add-backs as % of company Adj. EBITDA | 30.1% | 30.1% | 35.1% | 65.2% | 46.3% |
| Diligence-adjusted EBITDA (mine) | 55.8 | 68.8 | 84.7 | 22.5 | 72.6 |
| Diligence-adjusted margin | 15.1% | 16.3% | 16.9% | 10.1% | 14.6% |
| Net income | 11.5 | 15.2 | 18.6 | -8.9 | 4.4 |
| Operating cash flow | 30.8 | 40.8 | 9.7 | -4.2 | -6.9 |
| Free cash flow (OCF - capex) | 16.2 | 24.6 | -10.1 | -13.0 | -26.4 |
| OCF / EBITDA | 73.0% | 78.0% | 15.1% | -40.4% | -14.3% |
| DSO (net AR, days) | 60.4 | 63.5 | 86.4 | 85.4 (H1 annualized) | 76.3 (LTM basis) |
| Allowance / gross AR | 3.9% | 3.8% | 2.1% | 3.2% | n/a |
| Contract assets | 8.1 | 10.2 | 24.7 | 19.5 | n/a |
| Inventory (DIO, days) | 55.2 (91.2) | 63.9 (93.4) | 71.3 (87.9) | 84.0 (111.1) | n/a |
| Deferred revenue (total) | 38.1 | 48.0 | 56.9 | 50.2 | n/a |
| Total debt | 120.0 | 200.0 | 220.0 | 227.5 | n/a |
| Cash | 54.8 | 48.3 | 41.6 | 33.9 | n/a |
| Net debt | 65.2 | 151.7 | 178.4 | 193.6 | n/a |
| Net debt / company Adj. EBITDA | 1.08x | 2.03x | 1.81x | n/a | 2.16x |
| Net debt / reported EBITDA | 1.55x | 2.90x | 2.78x | n/a | 4.02x |
| EBITDA / interest | 5.70x | 5.34x | 4.71x | 1.32x | 3.23x |
| Top customer (Norvale) share | n/a | 28.0% | 31.1% | not provided | n/a |
| Top 10 share | n/a | 59.2% | 61.5% | not provided | n/a |
| FieldOS ARR (period end) | 86.0 | 109.5 | 139.2 | 146.8 | n/a |
| Software NRR (TTM) | 121% | 119% | 118% | 111% | n/a |
| Hardware backlog | 142.0 | 168.0 | 131.0 | 118.0 | n/a |
| Robots shipped | 3,020 | 3,300 | 4,300 | 1,640 | n/a |
| Hardware revenue per robot shipped ($000) | 78.1 | 79.4 | 70.1 | 71.3 | n/a |
| Full-time employees | 1,180 | 1,390 | 1,452 | 1,405 | n/a |

How some rows were built:
- **Diligence-adjusted EBITDA:**
  - It accepts as add-backs stock-based compensation (SBC) and clearly one-off items: ERP, Lumora deal costs, auditor transition, executive search and CFO transition, and the cybersecurity incident.
  - It rejects recurring restructuring, customer implementation delays and the ongoing Vantor litigation costs.
  - See FIN-03 for the working.
- **SBC-burdened view:** if SBC is also treated as a cost, diligence-adjusted EBITDA is 67.5 for FY2025 (84.7 - 17.2) and 54.8 for LTM (72.6 - 17.8).

### Findings

#### FIN-01: FY2025 growth depends on one abnormal quarter (Q4 2025), and revenue then fell in H1 2026
- **Finding:** Q4 2025 revenue of $154.4M is far above trend. It is up 32.4% YoY, while Q1 to Q3 2025 grew 13% to 14%. Q1 2026 then fell 29.0% from Q4. H1 2026 revenue fell 1.7% YoY, and Q2 2026 fell 4.0%.
- **Evidence:**
  - Quarterly YoY growth:
    - Q1 2025: 108.9 / 96.2 - 1 = 13.2%
    - Q2 2025: 117.6 / 102.8 - 1 = 14.4%
    - Q3 2025: 121.4 / 106.1 - 1 = 14.4%
    - Q4 2025: 154.4 / 116.6 - 1 = 32.4%
    - Q1 2026: 109.7 / 108.9 - 1 = 0.7%
    - Q2 2026: 112.9 / 117.6 - 1 = -4.0%
  - Quarter on quarter: Q4 2025 vs Q3 2025 = 154.4 / 121.4 - 1 = 27.2%. The same step a year earlier was 116.6 / 106.1 - 1 = 9.9%. Q1 2026 vs Q4 2025 = 109.7 / 154.4 - 1 = -29.0%.
  - Q4 share of the year: Q4 2025 = 154.4 / 502.3 = 30.7%. Q4 2024 = 27.7%.
  - Q1 to Q3 2025 growth = 347.9 / 305.1 - 1 = 14.0%. Q4 alone supplied 37.8 of the 80.6 FY2025 increase (46.9%).
  - Estimate: if Q4 2025 had grown at the Q3 rate (14.4%), it would have been 116.6 x 1.144 = 133.4. The excess is 154.4 - 133.4 = 21.0. Normalized FY2025 = 481.3, which is growth of 14.1% instead of the reported 19.1%.
  - By segment, H1 2026 vs H1 2025: hardware 116.9 / 134.2 - 1 = -12.9%; software +14.6%; services +14.4%.
- **Source:** `data/financials/revenue_quarterly.csv` (all rows); `data/financials/income_statement.csv` (Revenue rows, FY2024, FY2025, H1_2025, H1_2026)
- **Severity:** Critical
- **Confidence:** High for the recomputed growth rates. Medium for the 21.0 "excess" estimate, which assumes trend growth.
- **Deal impact:** Valuation. The run-rate the price is based on is overstated. This also raises a revenue recognition question (possible pull-forward or bill-and-hold; see FIN-04).
- **Cross-check:**
  - SEC filings: 10-K FY2025 and 10-Q Q1/Q2 2026 MD&A for an explanation of Q4 2025. Look for any one-off or large contract, bill-and-hold, a revenue recognition policy change, or a disclosed one-off revenue amount.
  - Check whether the Q4 spike is tied to Norvale (Norvale's revenue grew 38.1 in FY2025).
  - News: Q4 2025 or Q1 2026 earnings coverage, and analyst commentary on a "pull-forward".

#### FIN-02: The deal model's FY2026E management case is stale; real multiples are far higher than 11.5x
- **Finding:** The 11.5x multiple reconciles arithmetically. But it rests on FY2026E figures that H1 2026 results do not support. On actual LTM earnings, the price is 15.1x company Adjusted EBITDA, 18.6x diligence-adjusted EBITDA and 28.1x reported EBITDA.
- **Evidence:**
  - Equity value = 24.00 x 48.3 = 1,159.2.
  - Net debt at June 30, 2026 = (45.0 + 182.5) - 33.9 = 193.6.
  - Enterprise value (EV) = 1,159.2 + 193.6 = 1,352.8. This excludes leases and other debt-like items, which are not provided.
  - EV multiples:

    | Basis | EBITDA used | EV / EBITDA |
    |---|---|---|
    | FY2026E Adjusted EBITDA (management case) | 118.0 | 11.46x (reconciles to "about 11.5x") |
    | FY2025 company Adjusted EBITDA | 98.8 | 13.69x |
    | FY2025 diligence-adjusted | 84.7 | 15.97x |
    | LTM company Adjusted EBITDA | 89.7 | 15.08x |
    | LTM diligence-adjusted | 72.6 | 18.63x |
    | LTM reported EBITDA | 48.2 | 28.07x |
    | H1 2026 Adjusted EBITDA annualized (29.9 x 2 = 59.8; seasonality caveat) | 59.8 | 22.62x |

  - EV / revenue: FY2026E = 1,352.8 / 560.0 = 2.42x. LTM = 1,352.8 / 498.4 = 2.71x.
  - What the management case requires in H2 2026:
    - Revenue: 560.0 - 222.6 = 337.4. That is +22.3% vs H2 2025 (121.4 + 154.4 = 275.8), and 51.6% above H1 2026.
    - H2 would be 337.4 / 560.0 = 60.3% of the year. H2 was 54.9% in FY2025 and 52.8% in FY2024.
    - Adjusted EBITDA: 118.0 - 29.9 = 88.1. That is +47.3% vs H2 2025 (98.8 - 39.0 = 59.8).
    - Implied H2 Adjusted EBITDA margin = 88.1 / 337.4 = 26.1%. H2 2025 was 21.7% and H1 2026 was 13.4%.
  - Price sensitivity (illustrative), keeping the 11.46x model multiple:
    - On LTM company Adjusted EBITDA: EV = 89.7 x 11.464 = 1,028.3. Equity = 834.7, or $17.28 per share (-28.0% vs $24.00).
    - On LTM diligence-adjusted EBITDA: EV = 832.3. Equity = 638.7, or $13.22 per share.
- **Source:** `data/deal-brief.md` (Valuation basis); `data/financials/balance_sheet.csv` (Cash, Revolving credit facility, Term loan, Q2_2026); `data/financials/adjusted_ebitda_reconciliation.csv` (EBITDA and Adjusted EBITDA rows, LTM_Q2_2026, H1_2026, FY2025); `data/financials/revenue_quarterly.csv`
- **Severity:** Critical (the value gap is more than 10% on any reasonable basis)
- **Confidence:** High for the recomputed multiples. Medium for the per-share sensitivity, which assumes a constant multiple.
- **Deal impact:** Valuation. The model needs to be rebased to LTM or to a re-underwritten FY2026E before the November 6 IC meeting.
- **Cross-check:**
  - SEC filings: Q2 2026 10-Q or 8-K for whether FY2026 guidance was reaffirmed, cut or withdrawn after the March 2026 investor day.
  - News: guidance changes, and the share price fall to $17.85.
  - Confirm the diluted share count under the treasury method at $24.00. The H1 2026 figure of 48.3M is a loss-period count.

#### FIN-03: Adjusted EBITDA relies on growing, recurring add-backs, some of which are normal operating costs
- **Finding:** Add-backs grew from 30.1% of company Adjusted EBITDA in FY2023 to 65.2% in H1 2026 and 46.3% LTM. "Restructuring" appears every year from FY2022 to H1 2026. "Customer implementation delays" and the multi-year Vantor litigation costs look like normal operating costs.
- **Evidence:**
  - Add-backs, defined as Adjusted EBITDA minus EBITDA:
    - FY2023: 18.2 / 60.4 = 30.1%
    - FY2024: 22.5 / 74.8 = 30.1%
    - FY2025: 34.7 / 98.8 = 35.1%
    - H1 2026: 19.5 / 29.9 = 65.2%
    - LTM: 41.5 / 89.7 = 46.3%
  - Restructuring by year: 3.1, 4.6, 5.2, 7.9, then 4.4 in H1 2026 (9.7 LTM). It recurs and is rising.
  - "Other non-recurring" by year: 1.2, 2.0, 3.4, 9.6, then 6.2 in H1 2026. A new category appears almost every year.
  - Vantor litigation: 0.8 (FY2024), 2.1 (FY2025), 3.0 (H1 2026 alone). It is ongoing and accelerating.
  - Customer implementation delays: 4.1 in FY2025. This is a cost of serving customers. It may also relate to the Q4 2025 revenue (see FIN-01).
  - Diligence adjustments to company Adjusted EBITDA:
    - FY2025: 98.8 - 7.9 (restructuring) - 4.1 (implementation) - 2.1 (Vantor) = 84.7.
    - LTM: 89.7 - 9.7 - 3.3 - 4.1 = 72.6.
    - H1 2026: 29.9 - 4.4 - 3.0 = 22.5.
    - FY2024: 74.8 - 5.2 - 0.8 = 68.8.
    - FY2023: 60.4 - 4.6 = 55.8.
  - Accepted one-offs: ERP 2.0; Lumora 2.6; auditor transition 2.3; executive search and CFO transition 1.1 + 1.4; cybersecurity incident 1.8.
  - SBC was kept as an add-back to match market practice, but it is a real and rising cost: 11.6, 13.9, 17.2, then 8.9 in H1 2026. SBC-burdened LTM = 54.8.
  - The detail lines in the reconciliation add up to the "other non-recurring" total in every period.
- **Source:** `data/financials/adjusted_ebitda_reconciliation.csv` (rows: EBITDA, Add SBC, Add Restructuring, Add Other non-recurring, all Detail rows, all columns); `data/financials/income_statement.csv` (Restructuring and other charges, Memo SBC)
- **Severity:** High
- **Confidence:** High for the arithmetic. Medium for which items to reject, which is a judgment call pending a quality of earnings (QoE) review.
- **Deal impact:** Valuation (about 14.1 off FY2025 and 17.1 off LTM EBITDA), and financing if lender definitions follow the company's definition.
- **Cross-check:**
  - SEC filings: the 10-K non-GAAP reconciliation and any SEC comment letters on non-GAAP measures; the Vantor case status (litigation analyst).
  - The credit agreement's EBITDA definition: are these add-backs permitted or capped?
  - Commission a QoE report (none has been received yet).

#### FIN-04: Receivables and contract assets jumped far faster than revenue, while the bad-debt allowance fell
- **Finding:** In FY2025, net AR rose 62.0% and contract assets 142% against 19.1% revenue growth. DSO rose from 63.5 to 86.4 days. The allowance fell to 2.1% of gross AR from 3.8%. Together with the Q4 spike, this suggests revenue booked ahead of billing or collection, and possibly too small an allowance.
- **Evidence:**
  - DSO:
    - FY2023: 61.0 / 368.9 x 365 = 60.4 days
    - FY2024: 73.4 / 421.7 x 365 = 63.5 days
    - FY2025: 118.9 / 502.3 x 365 = 86.4 days
    - June 2026: 104.2 / (222.6 x 2) x 365 = 85.4 days (H1 annualized), or 104.2 / 498.4 x 365 = 76.3 days (LTM basis)
  - Net AR change FY2025 = 118.9 - 73.4 = 45.5, or +62.0%. Contract assets: 24.7 / 10.2 - 1 = +142.2%. Contract assets as a share of revenue: 2.4% in FY2024, 4.9% in FY2025.
  - AR plus contract assets rose 143.6 - 83.6 = 60.0, which equals 74.4% of the FY2025 revenue increase (80.6). Combined days rose from 72.4 to 104.3.
  - Year-end AR vs Q4 revenue: 118.9 / 154.4 = 77.0% (FY2024: 73.4 / 116.6 = 63.0%).
  - Allowance / gross AR: 2.5 / 63.5 = 3.9%; 2.9 / 76.3 = 3.8%; 2.6 / 121.5 = 2.1%; 3.4 / 107.6 = 3.2%. Gross AR grew 59.2% in FY2025 but the allowance fell by 0.3.
  - Estimate: at the FY2024 ratio, the FY2025 allowance would be 121.5 x 3.8% = 4.6, about 2.0 higher. That would have reduced FY2025 pre-tax income by about 2.0.
  - The allowance was then raised to 3.4 by June 2026.
- **Source:** `data/financials/balance_sheet.csv` (Accounts receivable net, Contract assets, Memo AR gross, Memo Allowance); `data/financials/income_statement.csv` (Total revenue); `data/financials/cash_flow.csv` (Change in AR, Change in contract assets)
- **Severity:** High
- **Confidence:** High for the ratios. Medium for the allowance shortfall estimate.
- **Deal impact:** Valuation and closing risk (possible revenue recognition issue). This calls for a specific indemnity or representation, and a closing working capital peg.
- **Cross-check:**
  - SEC filings: 10-K revenue recognition and contract asset notes, a critical audit matter on revenue, and why the auditor changed (FY2025 auditor transition costs of 2.3).
  - An AR aging by customer at Dec 31, 2025, especially Norvale.
  - Litigation records: any collection disputes.

#### FIN-05: Cash conversion collapsed; free cash flow is negative and buybacks were funded with debt
- **Finding:** OCF/EBITDA fell from 78.0% (FY2024) to 15.1% (FY2025) and was negative in H1 2026. LTM free cash flow is -26.4. In FY2025 the company still spent 17.4 on buybacks and share settlement while drawing 25.0 on the revolver.
- **Evidence:**
  - OCF / EBITDA: 30.8 / 42.2 = 73.0%; 40.8 / 52.3 = 78.0%; 9.7 / 64.1 = 15.1%; H1 2026: -4.2 / 10.4 = -40.4%.
  - OCF / net income: 2.68x (FY2023), 2.68x (FY2024), 0.52x (FY2025).
  - OCF / company Adjusted EBITDA, FY2025: 9.7 / 98.8 = 9.8%.
  - FCF: 16.2, 24.6, -10.1, then -13.0 in H1 2026. LTM FCF = -10.1 - 3.3 + (-13.0) = -26.4. LTM OCF = 9.7 - 12.4 - 4.2 = -6.9.
  - FY2025 working capital outflow was -51.7: AR -45.5, contract assets -14.5, inventory -7.4, payables and other +15.7.
  - H1 2026 working capital: -15.4. AR collections (+14.7) were offset by payables and accruals and deferred revenue (-22.6) and inventory (-12.7).
  - Shareholder returns: buybacks 20.0 + 25.0 + 13.3 = 58.3 over FY2023 to FY2025. FY2025 buybacks and net share settlement = 13.3 + 4.1 = 17.4, against FCF of -10.1 and a revolver draw of +25.0.
- **Source:** `data/financials/cash_flow.csv` (all rows, FY2023 to H1_2026); `data/financials/adjusted_ebitda_reconciliation.csv` (EBITDA)
- **Severity:** High
- **Confidence:** High (directly calculated)
- **Deal impact:** Valuation (earnings are not turning into cash), financing, and the working capital peg.
- **Cross-check:**
  - SEC filings: 10-Q liquidity discussion and board buyback authorizations.
  - News: commentary on cash burn.
  - Note: the H1 2025 working capital components are blank in the file, so the H1 2025 vs H1 2026 split cannot be compared.

#### FIN-06: Net debt is rising, leverage is about 4x on reported EBITDA, and liquidity depends on the revolver
- **Finding:** Net debt rose from 65.2 (FY2023) to 193.6 (June 2026). LTM net leverage is 2.16x on company Adjusted EBITDA, 2.67x on diligence-adjusted EBITDA and 4.02x on reported EBITDA. Interest cover on reported EBITDA fell to 3.2x LTM and 1.3x in H1 2026. Cash fell to 33.9 while the revolver rose to 45.0.
- **Evidence:**
  - Total debt: 120.0, 200.0, 220.0, 227.5. Net debt: 65.2, 151.7, 178.4, 193.6.
  - LTM net leverage: 193.6 / 89.7 = 2.16x; 193.6 / 72.6 = 2.67x; 193.6 / 48.2 = 4.02x.
  - LTM gross leverage: 227.5 / 89.7 = 2.54x; 227.5 / 48.2 = 4.72x.
  - EBITDA / interest: 42.2 / 7.4 = 5.70x; 52.3 / 9.8 = 5.34x; 64.1 / 13.6 = 4.71x; LTM 48.2 / 14.9 = 3.23x; H1 2026 10.4 / 7.9 = 1.32x.
  - LTM EBIT / interest = (37.3 - 13.3 - 3.7) / 14.9 = 20.3 / 14.9 = 1.36x.
  - Implied interest rate: FY2025 13.6 / ((200 + 220) / 2) = 6.5%. H1 2026 annualized: 15.8 / 223.75 = 7.1%.
  - Revolver: 0.0, 10.0, 35.0, 45.0.
  - Runway estimate: H1 2026 burn = FCF -13.0 plus term loan amortization -2.5 = 15.5 per half, or about 2.6 per month. Cash of 33.9 lasts about 13 months without more revolver draws.
- **Source:** `data/financials/balance_sheet.csv` (Cash, Revolving credit facility, Term loan); `data/financials/cash_flow.csv` (Term loan, Revolver, FCF memo); `data/financials/income_statement.csv` (Interest expense, Operating income); `data/financials/adjusted_ebitda_reconciliation.csv` (LTM column)
- **Severity:** High
- **Confidence:** High for leverage and coverage. Medium for runway, which assumes the H1 2026 burn continues.
- **Deal impact:** Financing and closing. Arbelion needs to know about change-of-control and prepayment terms and the debt payoff at closing. Covenant headroom is unknown.
- **Cross-check:**
  - SEC filings: the credit agreement (exhibit to the 10-K or 8-K) for the leverage covenant definition (which EBITDA basis and add-back caps), the revolver size and availability, maturities, and change-of-control clauses.
  - Any covenant amendment or waiver 8-Ks in 2025 or 2026.
  - The facility size and maturity dates are not in my folder.

#### FIN-07: Heavy and rising dependence on Norvale Retail Group, which drove about half of FY2025 growth
- **Finding:**
  - Norvale was 31.1% of FY2025 revenue (156.2), up from 28.0%.
  - Norvale supplied 47.3% of the FY2025 revenue increase.
  - The top 10 customers were 61.5% of revenue (59.2% in FY2024).
  - Without Norvale, FY2025 growth was 14.0%.
- **Evidence:**
  - Norvale: 118.1 / 421.7 = 28.0% in FY2024; 156.2 / 502.3 = 31.1% in FY2025. Its revenue grew 38.1, or +32.3%. Share of the total FY2025 increase: 38.1 / 80.6 = 47.3%.
  - Top 10 total: FY2024 = 249.6 (59.2%); FY2025 = 308.8 (61.5%). Top 3: 42.5% to 45.1%.
  - Excluding Norvale: 346.1 / 303.6 - 1 = 14.0%. "All other customers" grew 193.5 / 172.1 - 1 = 12.4%.
  - Illustrative revenue at risk: 156.2 of revenue, about 64.2 of gross profit at the FY2025 gross margin of 41.1%.
  - No customer data is given for H1 2026.
- **Source:** `data/financials/revenue_by_customer.csv` (all rows)
- **Severity:** High. Upgrade to Critical if other sources show the Norvale relationship is under strain, being renegotiated or tied to the Q4 2025 spike.
- **Confidence:** High (directly calculated)
- **Deal impact:** Valuation and post-closing. Consider requiring Norvale's consent or a contract extension as a closing condition.
- **Cross-check:**
  - SEC filings: 10-K major customer disclosure, Norvale contract terms, change-of-control and termination for convenience rights.
  - News and litigation: any Norvale dispute, insourcing, a competing vendor, or reduced orders in 2026.
  - Check whether Norvale's FY2025 increase was concentrated in Q4 2025.

#### FIN-08: Forward KPIs are weakening (NRR, backlog, book-to-bill, price per robot, headcount)
- **Finding:** Software NRR fell 7 points in six months to 111%. Hardware backlog fell 22.0% in FY2025 and a further 9.9% in H1 2026. Hardware revenue per robot fell 11.7% in FY2025. The forward indicators contradict both the reported FY2025 growth and the FY2026E case.
- **Evidence:**
  - NRR: 121%, 119%, 118%, then 111% at June 2026.
  - ARR: 86.0, 109.5 (+27.3%), 139.2 (+27.1%), then 146.8. That is +5.5% in six months, about 11.2% annualized (1.0546^2).
  - Backlog: 142.0, 168.0, 131.0, 118.0. FY2025: 131 / 168 - 1 = -22.0%. H1 2026: 118 / 131 - 1 = -9.9%.
  - Implied hardware book-to-bill. This assumes orders = hardware revenue + change in backlog:
    - FY2024: (261.9 + 26.0) / 261.9 = 1.10
    - FY2025: (301.4 - 37.0) / 301.4 = 0.88
    - H1 2026: (116.9 - 13.0) / 116.9 = 0.89
  - Hardware revenue per robot shipped: 236.0 / 3,020 = $78.1k; 261.9 / 3,300 = $79.4k; 301.4 / 4,300 = $70.1k (-11.7%); 116.9 / 1,640 = $71.3k. FY2025 units rose 30.3% but hardware revenue rose only 15.1%. This suggests discounting or a large low-price order.
  - H1 2026 units: 1,640, which is 23.7% below the FY2025 half-year average of 2,150.
  - Active customers: net adds of +36, +28, then +5 in H1 2026.
  - Headcount: 1,452 to 1,405 (-3.2%) in H1 2026.
  - Illustrative FY2026E coverage:
    - H2 2026 needs 337.4 of revenue.
    - Software at the ARR run-rate gives about 73.4 (146.8 / 2).
    - Services at H2 2025 plus 14.4% gives about 44.5.
    - That leaves about 219.5 of hardware, which is +31.3% vs H2 2025 hardware (167.2). Backlog of 118.0 covers only 53.8% of that.
- **Source:** `data/financials/kpis.csv` (all rows); `data/financials/income_statement.csv` (Revenue: Hardware, Software, Services)
- **Severity:** High
- **Confidence:** High for the KPI trends. Medium for book-to-bill and the coverage estimate (they assume backlog converts to hardware revenue and estimate the segment run-rates).
- **Deal impact:** Valuation. FY2026E and the out-year growth assumptions are not supported.
- **Cross-check:**
  - SEC filings: the 10-Q backlog definition and any cancellations; whether NRR is disclosed consistently.
  - News: competitor pricing pressure, customer churn, and layoff reports (the headcount fall plus rising restructuring).

#### FIN-09: Margins compressed in H1 2026 despite a richer software mix
- **Finding:**
  - Gross margin fell from 40.8% to 38.0% YoY in H1 2026, even though higher-margin software rose from 26.0% to 30.3% of revenue.
  - Opex rose to 39.7% of revenue.
  - Reported EBITDA margin fell to 4.7%, and the company swung to an operating loss of -3.7.
- **Evidence:**
  - Gross margin: 147.9 / 368.9 = 40.1%; 172.1 / 421.7 = 40.8%; 206.3 / 502.3 = 41.1%; H1 2025: 92.4 / 226.5 = 40.8%; H1 2026: 84.6 / 222.6 = 38.0%.
  - Software mix: 58.9 / 226.5 = 26.0% in H1 2025; 67.5 / 222.6 = 30.3% in H1 2026.
  - Opex / revenue: 79.1 / 226.5 = 34.9% in H1 2025; 88.3 / 222.6 = 39.7% in H1 2026. G&A rose from 16.2 to 19.8 (+22.2%).
  - EBITDA margin: 26.3 / 226.5 = 11.6% in H1 2025; 10.4 / 222.6 = 4.7% in H1 2026.
  - Net income: 5.3 in H1 2025; -8.9 in H1 2026.
- **Source:** `data/financials/income_statement.csv` (all rows, H1_2025 and H1_2026)
- **Severity:** High
- **Confidence:** High (directly calculated). Segment gross margins are not provided.
- **Deal impact:** Valuation and synergy case. The $35.0M synergy target should be tested against a shrinking cost base that already includes restructuring.
- **Cross-check:**
  - SEC filings: 10-Q MD&A on the drivers of gross margin (pricing, warranty, component costs, or the cost of the cyber incident).
  - Segment gross margin disclosure.

#### FIN-10: Inventory is building while hardware sales and backlog fall
- **Finding:** Inventory rose 17.8% in H1 2026 to 84.0, and inventory days rose to 111.1. Over the same period hardware revenue fell 12.9% and backlog fell 9.9%. This creates obsolescence or write-down risk.
- **Evidence:**
  - Inventory: 71.3 to 84.0, which is +12.7 (matches the cash flow line of -12.7), or +17.8%.
  - DIO: FY2023 55.2 / 221.0 x 365 = 91.2; FY2024 93.4; FY2025 71.3 / 296.0 x 365 = 87.9; H1 2026 84.0 / (138.0 x 2) x 365 = 111.1 days.
- **Source:** `data/financials/balance_sheet.csv` (Inventory); `data/financials/cash_flow.csv` (Change in inventory); `data/financials/income_statement.csv` (Cost of revenue)
- **Severity:** Medium
- **Confidence:** High for the ratios. Medium on the risk interpretation.
- **Deal impact:** Valuation (possible write-down) and the working capital peg.
- **Cross-check:** 10-Q inventory note (raw materials vs finished goods, reserves); purchase commitments; any product transition news.

#### FIN-11: Deferred revenue fell in H1 2026 while ARR rose
- **Finding:** Total deferred revenue fell 11.8%, from 56.9 to 50.2, in H1 2026, even though ARR rose 5.5%. Billings may be weakening, or this may be seasonal annual billing. It needs explaining.
- **Evidence:**
  - Current deferred revenue: 44.8 to 39.4. Non-current: 12.1 to 10.8. Total: 56.9 to 50.2, a fall of 6.7 (6.7 / 56.9 = 11.8%).
  - Prior year-end totals: 38.1 (FY2023) and 48.0 (FY2024).
  - No June 2025 balance is provided to test seasonality.
- **Source:** `data/financials/balance_sheet.csv` (Deferred revenue current and non-current); `data/financials/kpis.csv` (FieldOS ARR)
- **Severity:** Medium
- **Confidence:** Medium (no prior-year interim balance)
- **Deal impact:** Valuation (software quality) and the working capital peg.
- **Cross-check:** 10-Q remaining performance obligations (RPO); billing terms (annual vs monthly); June 30, 2025 balance sheet.

#### FIN-12: The add-backs show governance and control events that other workstreams should investigate
- **Finding:** The add-back detail reveals four events. Other workstreams should match each one to filings and news.
- **Evidence:**
  - Auditor transition costs: 2.3 in FY2025.
  - Executive search and CFO transition: 1.1 in FY2025 and 1.4 in H1 2026.
  - Cybersecurity incident response: 1.8 in H1 2026.
  - Rising Vantor patent litigation costs: 0.8, 2.1, then 3.0 in H1 2026.
  - An auditor change and a CFO change in the same year as an unusual Q4 and a jump in AR and contract assets is a pattern that needs explaining.
- **Source:** `data/financials/adjusted_ebitda_reconciliation.csv` (Detail rows: Auditor transition, Executive search and CFO transition, Cybersecurity incident response, Litigation costs Vantor)
- **Severity:** Medium on its own. It may be upgraded depending on the SEC and litigation findings.
- **Confidence:** High that the items exist. Low on what they mean.
- **Deal impact:** Closing risk and post-closing (internal controls, IP, cyber liability).
- **Cross-check:**
  - SEC filings: 8-K Item 4.01 (auditor change: disagreements, reportable events); 8-K Item 5.02 (CFO departure); 8-K Item 1.05 (material cyber incident) and its timing vs the incident; 10-K internal control assessment (material weaknesses).
  - Litigation: the Vantor patent case status, damages claimed, injunction risk.
  - News: coverage of all four events.

#### FIN-13: FY2024 and FY2025 growth includes the Lumora Vision acquisition, but its contribution is not disclosed
- **Finding:** Talonfield bought Lumora Vision in FY2024 for 85.0 net of cash, funded with a 70.0 term loan increase and a 10.0 revolver draw. Lumora's revenue contribution and timing are not given, so organic growth for FY2024 and FY2025 cannot be isolated.
- **Evidence:**
  - Acquisition outflow: 85.0.
  - Goodwill: 41.0 to 98.4 (+57.4). Intangibles: 21.1 to 43.4 (+22.3). Total +79.7.
  - Intangibles then amortize at about 6.2 a year (43.4 to 37.2).
  - Lumora deal costs added back: 2.6.
- **Source:** `data/financials/cash_flow.csv` (Acquisition of Lumora Vision, Term loan, Revolver FY2024); `data/financials/balance_sheet.csv` (Goodwill, Intangible assets); `data/financials/adjusted_ebitda_reconciliation.csv` (Lumora acquisition costs)
- **Severity:** Medium
- **Confidence:** High for the amounts. The growth impact cannot be determined.
- **Deal impact:** Valuation (organic growth may be below the reported 14.3% and 19.1%) and goodwill impairment risk if performance stays weak.
- **Cross-check:** 10-K business combination note (closing date, revenue contributed, pro forma revenue); goodwill impairment testing disclosures.

#### FIN-14: Installed base equals cumulative shipments, with no retirements
- **Finding:** Installed base rises by exactly the number of units shipped each period. The metric is cumulative shipments, not active robots, so it may overstate the base for services and software.
- **Evidence:** 9,800 + 3,300 = 13,100; 13,100 + 4,300 = 17,400; 17,400 + 1,640 = 19,040.
- **Source:** `data/financials/kpis.csv` (Robots shipped; Installed base)
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (quality of KPIs)
- **Cross-check:** How the 10-K or investor day defines the KPI; any decommissioning data.

### Positive or mitigating points

- Software keeps growing. FieldOS revenue rose 14.6% YoY in H1 2026 and ARR reached 146.8 at June 2026. NRR is still above 100% (111%), though falling. Services also grew 14.4% in H1 2026.
- The financial statements are internally consistent. They balance and reconcile, equity rolls forward, and the company's EBITDA arithmetic is correct. The problem is the definitions, not math errors.
- AR fell 14.7 and contract assets fell 5.2 in H1 2026. This is consistent with part of the Q4 2025 billing being collected. The allowance was raised back to 3.2% of gross AR.
- Leverage on company Adjusted EBITDA (2.16x net LTM) is moderate. Interest is still covered on the company's Adjusted EBITDA (6.0x LTM).
- Underlying growth was about 14% in FY2025, excluding the Q4 excess or excluding Norvale. That is still a growing business.
- No embedded instructions or manipulation attempts were found in any financial file.

### Gaps and questions for management

1. What explains Q4 2025 revenue of 154.4? Give the size and nature of any large, one-off, bill-and-hold or pulled-forward contracts, and how much relates to Norvale.
2. Quarterly revenue by segment and by customer (especially Norvale) for Q4 2025, Q1 2026 and Q2 2026.
3. An AR aging and contract asset roll-forward at Dec 31, 2025 and June 30, 2026, plus the allowance methodology and why the FY2025 ratio fell.
4. Is FY2026 guidance ($560.0M revenue, $118.0M Adjusted EBITDA) still current? Provide the latest forecast and the H2 2026 bridge (backlog conversion, new bookings, pricing).
5. Credit agreement: the covenant EBITDA definition and add-back caps, the leverage and coverage covenant levels, revolver size and availability, maturities, and change-of-control and prepayment terms.
6. Lease liabilities and other debt-like items (needed for the EV bridge). The diluted share count under the treasury method at $24.00.
7. Support for each add-back. Why restructuring recurs every year. What "customer implementation delays" covers and which P&L line it sits in. Vantor litigation status and expected costs.
8. Lumora Vision: closing date, revenue and EBITDA contributed in FY2024 and FY2025, and organic growth by segment.
9. Segment gross margins and the drivers of the H1 2026 gross margin decline.
10. The inventory breakdown and reserves; the backlog definition and any cancellations; definitions of NRR, ARR and installed base.
11. The H1 2025 working capital components (blank in `cash_flow.csv`) and the June 30, 2025 balance sheet.
12. Customer concentration for H1 2026, and Norvale contract terms (expiry, termination rights, change of control).
13. The basis for the $35.0M synergy target, given the H1 2026 cost base and the restructuring already underway (not testable from the financial data).
14. A quality of earnings report has not been received. I recommend commissioning one before signing.
