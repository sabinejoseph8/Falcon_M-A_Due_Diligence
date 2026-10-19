# Key metrics (US$ millions unless stated)

Sources: `data/financials/*.csv` (via FIN- findings, recomputed by Agent Core where marked), `data/sec-filings/` (SEC-), `data/news/` (NEWS-), `data/deal-brief.md`.

## Deal

| Metric | Value | Source |
|---|---|---|
| Offer price | $24.00 per share | deal-brief.md |
| Diluted shares | 48.3m | deal-brief.md |
| Equity value | 24.00 x 48.3 = 1,159.2 | deal-brief.md; FIN-01 |
| Net debt Jun 30, 2026 | 182.5 + 45.0 - 33.9 = 193.6 | balance_sheet.csv Q2_2026 |
| Enterprise value | 1,352.8 | FIN-01 |
| Unaffected close Oct 16, 2026 | $17.85 (premium 34.5%) | deal-brief.md |
| Close Oct 2, 2026 after sale leak (+12%) | $17.20; implied pre-leak about $15.36 (premium about 56%) | NEWS-09 |
| March 2026 52-week high | $31.75 | NEWS-09 |

## Valuation multiples at $24.00 (EV 1,352.8)

| EBITDA basis | EBITDA | EV / EBITDA |
|---|---|---|
| Management case FY2026E (deal model) | 118.0 | 11.5x |
| FY2026 guidance midpoint (Aug 6, 2026) | 74.0 | 18.3x |
| LTM Adjusted (company) | 89.7 | 15.1x |
| LTM reported | 48.2 | 28.1x |
| 11.5x on LTM Adjusted, implied price | n/a | $17.35 per share |

## Revenue

| Metric | Value | Source |
|---|---|---|
| FY2024 / FY2025 revenue | 421.7 / 502.3 (+19.1%) | income_statement.csv |
| Q4 2024 / Q4 2025 | 116.6 / 154.4 (+32.4%) | revenue_quarterly.csv |
| Q4 2025 bill-and-hold revenue | 31.8 (24.6 largest customer) | 10-K Note 2 |
| FY2025 ex bill-and-hold | 470.5 (+11.6%) | Agent Core recompute |
| Q4 2025 ex bill-and-hold | 122.6 (+5.1%) | Agent Core recompute |
| Q1 2026 / Q2 2026 YoY | +0.7% / -4.0% | FIN-02 |
| Q2 2026 bill-and-hold return credit / SLA credits | 9.4 / 2.3 | 10-Q |
| H1 2026 revenue | 222.6 (-1.7%) | income_statement.csv |
| FY2026 guidance (Aug 6) | 470 to 490 (was 555 to 565) | 10-Q; NEWS-01 |

## Customers (FY2025)

| Rank | Customer | Revenue | Share |
|---|---|---|---|
| 1 | Norvale Retail Group | 156.2 | 31.1% |
| 2 | Quillon Logistics | 41.2 | 8.2% |
| 3 | Ardent Parcel Co. | 28.9 | 5.8% |
| 4 | Pinecrest Distribution | 17.4 | 3.5% |
| 5 | Harbor & Vine Grocers | 15.1 | 3.0% |
| Top 10 | | 308.8 | 61.5% |

Not listed customers: Vantor Robotics (litigant, competitor), Kinetic Aisle (Norvale-owned startup), Delmarco Electrical Contractors (litigant), Greyfin Research (short seller). Norvale ex its 24.6 bill-and-hold: 131.6, +11.4% vs 118.1.

## EBITDA and cash

| Metric | FY2025 | H1 2026 | LTM Jun 2026 |
|---|---|---|---|
| Reported EBITDA | 64.1 | 10.4 | 48.2 |
| Stock-based compensation | 17.2 | 8.9 | 17.8 |
| Restructuring | 7.9 | 4.4 | 9.7 |
| Other non-recurring | 9.6 | 6.2 | 14.0 |
| Adjusted EBITDA | 98.8 | 29.9 | 89.7 |
| Add-backs share of Adjusted EBITDA | 35.1% | 65.2% | 46.3% |
| Operating cash flow | 9.7 | -4.2 | -6.9 |
| Free cash flow | -10.1 | -13.0 | -26.4 |

## Debt and covenant

| Metric | Value | Source |
|---|---|---|
| Term loan / revolver Jun 30, 2026 | 182.5 / 45.0 (revolver commitment 75.0; 25.8 available after 4.2 LCs) | balance_sheet.csv; 10-K Note 9; 10-Q |
| Covenant max Total Net Leverage | 3.50x to Jun 30, 2026; 3.00x from Sep 30, 2026 | 10-K Note 9 |
| Company-reported ratio Jun 30, 2026 | 2.26x | 10-Q |
| Covenant net debt (cash netting capped at 25.0) | 227.5 - 25.0 = 202.5 | Agent Core recompute |
| Change of control | Event of default | 10-K Note 9 |

## KPIs

| Metric | FY2024 | FY2025 | Jun 30, 2026 |
|---|---|---|---|
| Backlog | 168.0 | 131.0 | 118.0 |
| FieldOS ARR | 109.5 | 139.2 | 146.8 |
| Software NRR | 119% | 118% | 111% |
| DSO (days) | 63.5 | 86.4 | 85.4 |
| Allowance / gross AR | 3.80% | 2.14% | 3.16% |

## Litigation exposure

| Matter | Amount | Source |
|---|---|---|
| Vantor claim | not less than 140.0 (12.1% of equity value) | LIT-001 |
| Vantor expert royalty through trial | 96.4 | LIT-001 docket 2026-09-04 |
| Gen-3 revenue at injunction risk | about 211.0 (70% of hardware 301.4) | 10-K Item 1 |
| Pinecrest claim / company cap estimate | 12.0 / about 1.4 | LIT-004 |
| Ruiz settlement | 3.2 (accrued) | LIT-002; 10-K |
| Change-in-control payouts | 28.6 (17.6 single-trigger equity) | DEF 14A |
