> **FICTIONAL DATA.** Invented for a training exercise. Corvane Home Systems, Inc. does not exist.

# Corvane Home Systems: financial data pack

Source: company management accounts, reconciled to the FY2025 Form 10-K and Q2 2026 Form 10-Q. Unaudited for H1 periods. US$ millions unless stated.

| File | Contents | Columns |
|---|---|---|
| `income_statement.csv` | Income statement with revenue by segment | FY2022 to FY2025, H1_2025, H1_2026 |
| `balance_sheet.csv` | Balance sheet. Assets are the rows above "Total assets"; liabilities are the rows between "Total assets" and "Total liabilities" | FY2023, FY2024, FY2025 (December 31), Q2_2026 (June 30, 2026) |
| `cash_flow.csv` | Cash flow statement (indirect method) | FY2023 to FY2025, H1_2025, H1_2026 |
| `adjusted_ebitda_reconciliation.csv` | Net income to EBITDA, then the company's adjustments to Adjusted EBITDA. Rows starting "Add:" are company adjustments; rows starting "Detail:" break down the "Other non-recurring items" adjustment | FY2022 to FY2025, H1_2025, H1_2026, LTM_Q2_2026 |
| `revenue_quarterly.csv` | Total revenue by quarter | Q1 2023 to Q2 2026 |
| `revenue_by_customer.csv` | Largest customers, FY2024 and FY2025 | Ranked by FY2025 revenue |
| `kpis.csv` | Operating metrics | FY2023 to FY2025, and H1 2026 or June 30, 2026 |

Notes from management:

- Adjusted EBITDA is the company's own definition, as used in its earnings releases.
- LTM_Q2_2026 = FY2025 minus H1_2025 plus H1_2026.
- Days metrics use period-end balances and 365 days (181 days for H1 2026). Days payable and days inventory use cost of revenue.
- "Change in fair value of contingent consideration" in the cash flow is the non-cash gain on remeasuring the Nimbus earn-out, booked in other income.
- Warranty claim rate is claims received as a percentage of units under warranty, annualized.
- Corvane Insights revenue is reported inside the Subscriptions & Services segment.
