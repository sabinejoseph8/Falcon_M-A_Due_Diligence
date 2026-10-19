# Corvane Diagnostics: financial data pack

> FICTIONAL. Prepared for a portfolio demonstration. All figures are invented.

Source: Corvane's audited financial statements for FY2022 to FY2025 and unaudited interim statements for H1 2025 and H1 2026 (six months to June 30), as provided to Halvard Ridge in the data room. US$ millions unless stated.

| File | Contents |
|---|---|
| `income_statement.csv` | Revenue by segment, costs, operating income and net income. FY2022 to FY2025, H1 2025, H1 2026. Depreciation and amortization is shown as a memo line; it is already included in cost of revenue and SG&A. |
| `balance_sheet.csv` | Year-end FY2023 to FY2025 and June 30, 2026. Memo lines show gross receivables and the implicit price concession reserve. |
| `cash_flow.csv` | FY2023 to FY2025, H1 2025, H1 2026. |
| `adjusted_ebitda_reconciliation.csv` | Bridge from net income to EBITDA and to Adjusted EBITDA as Corvane defines it, with detail of "other non-recurring items". LTM_Q2_2026 = FY2025 minus H1 2025 plus H1 2026. |
| `revenue_quarterly.csv` | Total revenue by quarter, Q1 2024 to Q2 2026. |
| `revenue_by_customer.csv` | Top 10 payers and biopharma clients by FY2025 revenue. |
| `kpis.csv` | Operating metrics. The last column is H1 2026 for flow metrics and June 30, 2026 for point-in-time metrics. |

Notes from management:

- Clinical testing revenue is recognized when the test result is delivered, at the amount Corvane expects to collect. Corvane estimates "implicit price concessions" (amounts it does not expect to collect from payers and patients) using a collection-rate model.
- Adjusted EBITDA is a non-GAAP measure defined by Corvane. It is used for management bonuses. It is not the same as "Consolidated EBITDA" in Corvane's credit agreement, which is defined in the 10-K.
- Average revenue per accession = clinical testing revenue / clinical test volume.
- Initial claim denial rate = claims denied on first submission / claims submitted.
