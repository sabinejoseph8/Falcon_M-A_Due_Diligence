# Verification batch: financial

Full finding cards (claims, numbers, cited sections) are in `memory/` files named below, under the heading `#### <ID>` (analyst cards) or `### <ID>` (X- cards).

| ID | Claim (register wording) | Severity | Confidence | Cited sources | Full card |
|---|---|---|---|---|---|
| FIN-001 | LTM Adjusted EBITDA about US$115.4m, not US$130.4m | Critical | Medium | adjusted_ebitda_reconciliation.csv; kpis.csv (see X-004) | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-002 | Aura add-back US$6.0m is a quality cost | High | High | adjusted_ebitda_reconciliation.csv row 13 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-003 | Warranty accrual cut while claims rise | High | Medium | kpis.csv rows 9-12 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-004 | Calder legal fees US$3.2m added back | Medium | High | adjusted_ebitda_reconciliation.csv row 14 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-005 | Acquisition and transaction costs recur | Medium | Medium | adjusted_ebitda_reconciliation.csv row 9 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-006 | SBC US$17.6m largest add-back | Medium | High | adjusted_ebitda_reconciliation.csv row 8 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-007 | FY2023 restructuring one-off, outside LTM | Low | High | adjusted_ebitda_reconciliation.csv row 12 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-008 | Earn-out gain correctly excluded from EBITDA | Low | High | balance_sheet.csv row 20; cash_flow.csv row 6 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-009 | H1 OCF mostly working capital timing | High | High | cash_flow.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-010 | DPO 78 to 121 days; US$57.1m excess payables | High | High | balance_sheet.csv row 14 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-011 | Utility prepayments US$7.0m to US$41.0m | High | High | balance_sheet.csv row 19 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-012 | Pension obligation US$151.0m not in net debt | High | High | balance_sheet.csv row 23 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-013 | Debt-like items US$270.1m not in model | Critical | Medium | balance_sheet.csv (see X-018) | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-014 | Underlying cash US$69.3m vs US$100.0m to be used | High | Medium | balance_sheet.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-015 | Leverage at close 7.8x adjusted | High | High | adjusted_ebitda_reconciliation.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-016 | Multiples on adjusted earnings; illustrative US$15.96/share | High | Medium | as FIN-001, FIN-013 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-017 | Gross margin falling vs 42% assumption | High | High | income_statement.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-018 | Peso exposure unhedged | High | Medium | kpis.csv rows 16-18 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-019 | Revenue growth slowing; Insights over half of H1 growth | Medium | High | revenue_quarterly.csv; income_statement.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-020 | Gulf Horizon 71.9% of FY2025 growth | High | High | revenue_by_customer.csv row 5 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-021 | WSEA concentration 12.2%; 68.1% of Utility | High | High | revenue_by_customer.csv row 1 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-022 | Utility growth 4.3% below 6% assumption | Medium | High | income_statement.csv row 4 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-023 | Insights must grow 59% a year to reach US$60.0m | Medium | Medium | kpis.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-024 | Nimbus earn-out cut 44.8% | Medium | High | balance_sheet.csv row 20 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-025 | Care revenue per subscriber falling | Medium | Medium | income_statement.csv; kpis.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-026 | Subscription gross retention stable about 93% | Low | High | kpis.csv row 5 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-029 | Ranks of other named customers | Low | High | revenue_by_customer.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-034 | Goodwill and intangibles 48% of assets; Nimbus impairment indicator | Medium | Medium | balance_sheet.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-035 | UTP liability growing to US$14.2m | Low | High | balance_sheet.csv row 24 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-036 | Environmental reserve US$8.7m | Low | High | balance_sheet.csv row 25 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-039 | Field action reserve vs "fully reserved" | Medium | Medium | balance_sheet.csv row 17 | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-042 | Interest cover after closing | Medium | Low | adjusted_ebitda_reconciliation.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-044 | Sponsor equity about US$703.8m before fees | Low | High | deal-brief.md; balance_sheet.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-045 | Effective tax rate consistent with 23% | Low | High | income_statement.csv | memory/analyst-reports/iteration-1_financial-analyst.md |
| FIN-046 | WSEA loss: EBITDA at risk exceeds 10% of EV at any contribution margin above 13.6% (14.7% to 29.5% of EV at 20% to 40%) | Critical | Medium | revenue_by_customer.csv row 1; income_statement.csv (iteration 2; see X-003) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-047 | Utility Programs without WSEA about US$45.0m base; 2027 gap vs brief US$107.9m (projection) | High | Medium | revenue_by_customer.csv rows 1, 5; income_statement.csv (iteration 2) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-048 | WSEA advance US$34.0m unwinds before a Q1 2027 close | High | High | balance_sheet.csv; cash_flow.csv (iteration 2) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-049 | Gulf Horizon revenue and EBITDA at risk (about US$16.4m at 42.5%; >10% of EV only above 33.8% margin) | High | Medium | revenue_by_customer.csv row 4 (iteration 2) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-050 | FY2025 growth 1.8% excluding Gulf Horizon; Devices ex Gulf -4.2% | Medium | High | revenue_by_customer.csv; income_statement.csv (iteration 2) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-051 | Thermostat split not found; Calder royalty upper bound US$20.2m a year, back royalties up to US$86.1m (FY2022 to H1 2026) | High | Low | income_statement.csv Devices row (iteration 2; see X-009) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-052 | Peso move costs about US$35.8m a year; US$17.0m to US$18.7m not yet in LTM (projection) | High | Medium | kpis.csv; income_statement.csv (iteration 2; see X-016) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-053 | 42% gross margin unsupported; run-rate about 38.8% (projection) | Medium | Medium | income_statement.csv (iteration 2) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-054 | Pension termination shortfall US$230.5m replaces the accounting deficit; ties to balance sheet | Critical | High | balance_sheet.csv (iteration 2; see X-001) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-055 | Nimbus US$90.0m on CoC; US$82.0m above carrying value | High | High | balance_sheet.csv (iteration 2; see X-002) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-056 | Deal brief EV excludes the US$8.0m earn-out it calls debt-like | Low | High | deal-brief.md sections 1, 4 (iteration 2) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-057 | NEO severance US$21.6m at US$18.70 | Medium | Medium | Proxy (iteration 2; parent SEC-037) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-058 | Payables stretch matches contract manufacturer term change | High | High | balance_sheet.csv; cash_flow.csv (iteration 2; see X-005) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-059 | Ensamble guarantee US$63.4m unrecorded | High | Medium | 10-K Note 14 (iteration 2; see X-006) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-061 | IRS excess over reserve up to US$106.9m | High | Medium | balance_sheet.csv; 10-Q Note 10 (iteration 2; see X-013) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-062 | Environmental exposure up to US$107.0m above accrual | High | Medium | balance_sheet.csv (iteration 2; see X-012) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-063 | EC fine cap US$78.6m (FY2025) to US$80.7m (LTM) | High | Medium | income_statement.csv; 10-Q Note 12 (iteration 2; parent SEC-023) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-064 | Aura refund uninsured: US$43.1m to US$91.3m net of reserve at 25% to 50% uptake | High | Medium | balance_sheet.csv (iteration 2; see X-011) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-065 | Rebuilt net debt and debt-like items US$720.8m before contingencies (vs US$259.6m); contingencies US$43.1m to US$447.2m | Critical | Medium | balance_sheet.csv; FIN-054 to FIN-064 (iteration 2; see X-018) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-066 | Rebased value US$12.32/share (Case B) and US$5.81 (Case B less WSEA) at 11.84x (projection) | Critical | Medium | FIN-046, FIN-065 (iteration 2; see X-018) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-067 | Sources and uses rise to US$2,045.9m; sponsor equity US$1,045.9m (+48.6%) | High | High | deal-brief.md (iteration 2; see X-017) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-068 | Leverage 7.8x Case B, 10.4x without WSEA | High | High | adjusted_ebitda_reconciliation.csv (iteration 2; see X-017) | memory/analyst-reports/iteration-2_financial-analyst.md |
| FIN-069 | Cash after US$100.0m use: US$60.4m, US$26.4m after WSEA unwind, -US$30.7m if payables normalize | High | Medium | balance_sheet.csv; cash_flow.csv (iteration 2; see X-017) | memory/analyst-reports/iteration-2_financial-analyst.md |
