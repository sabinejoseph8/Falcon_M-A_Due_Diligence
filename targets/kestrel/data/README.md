# Simulated data sources (fictional)

> Everything in this folder is FICTIONAL and was created for a portfolio demonstration. Corvane Diagnostics, Halvard Ridge Capital Partners, Veltrane Therapeutics, Orvia Health Plan, Genaro Biosciences and every other company, person, court case, article and number are invented. Any resemblance to real entities is coincidental.

Each folder stands in for one of the "tools" in the architecture:

| Folder | Simulates | Specialist subagent |
|---|---|---|
| `sec-filings/` | SEC Filing Search (EDGAR) | sec-filings-analyst |
| `news/` | News & Media API | news-media-analyst |
| `litigation/` | Litigation Database (court dockets and regulatory matters) | litigation-analyst |
| `financials/` | Financial data (statements, KPIs, payer and client data) | financial-analyst |
| `deal-brief.md` | The deal team's brief and the Investment Committee's questions | lead agent |

Conventions: US$ millions unless stated. Fiscal year = calendar year. Negative numbers use a leading minus sign. Corvane is a clinical laboratory, so in `financials/revenue_by_customer.csv` a "customer" is a payer (for example Medicare or a health plan) or a biopharma client.
