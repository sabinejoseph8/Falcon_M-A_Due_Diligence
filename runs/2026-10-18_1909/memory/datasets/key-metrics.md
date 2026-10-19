# Key metrics (US$ millions unless stated)

Sources: `data/financials/*.csv` (financial analyst, iteration 1), SEC filings (SEC analyst), deal brief. "Computed" = analyst or lead agent calculation.

## Deal

| Metric | Value | Source |
|---|---|---|
| Offer price / diluted shares | $24.00 / 48.3m | deal brief |
| Equity value | 1,159.2 | computed |
| Net debt Jun 30, 2026 | 193.6 (revolver 45.0 + term loan 182.5 - cash 33.9) | balance_sheet.csv Q2_2026 |
| Enterprise value | 1,352.8 | computed |
| EV / mgmt FY2026E Adj. EBITDA 118.0 | 11.46x | computed |
| EV / Aug guidance midpoint 74.0 | 18.3x | computed |
| EV / LTM Adj. EBITDA 89.7 | 15.1x | computed |
| EV / diligence-adjusted LTM EBITDA 72.6 | 18.6x | computed |
| Price at 11.46x on 74.0 | about $13.55 | computed |
| Price at 11.46x on LTM Adj. 89.7 | $17.28 | FIN-001 |
| Undisturbed price (before Oct 2 leak, RUMOR-based) | about $15.36 | NEWS-010 |

## Income statement

| Metric | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 | LTM Q2 2026 |
|---|---|---|---|---|---|---|
| Revenue | 368.9 | 421.7 | 502.3 | 226.5 | 222.6 | 498.4 |
| Growth | 18.1% | 14.3% | 19.1% | | -1.7% | |
| Gross margin | 40.1% | 40.8% | 41.1% | 40.8% | 38.0% | |
| EBITDA (reported) | 42.2 | 52.3 | 64.1 | 26.3 | 10.4 | 48.2 |
| Adjusted EBITDA (company) | 60.4 | 74.8 | 98.8 | 39.0 | 29.9 | 89.7 |
| Diligence-adjusted EBITDA | 55.8 | 68.8 | 84.7 | | 22.5 | 72.6 |
| Net income | 11.5 | 15.2 | 18.6 | | -8.9 | |

Segments: FY2025 hardware 301.4, software 128.6, services 72.3. H1 2025 134.2 / 58.9 / 33.4. H1 2026 116.9 / 67.5 / 38.2.

## Quarterly revenue

| Q4 24 | Q1 25 | Q2 25 | Q3 25 | Q4 25 | Q1 26 | Q2 26 |
|---|---|---|---|---|---|---|
| 116.6 | 108.9 | 117.6 | 121.4 | 154.4 | 109.7 | 112.9 |

Q4 2025 bill-and-hold 31.8 (20.6% of Q4); Q4 ex bill-and-hold 122.6 (+5.1% YoY). FY2025 ex bill-and-hold 470.5 (+11.6%). Bill-and-hold returned in Q2 2026: 9.4.

## Guidance

| | Revenue | Adj. EBITDA |
|---|---|---|
| March 9, 2026 (deal model) | 555-565 (560.0) | 114-122 (118.0) |
| Aug 6, 2026 | 470-490 (480.0) | 70-78 (74.0) |

## Customers (FY2025)

| Rank | Customer | Revenue | Share |
|---|---|---|---|
| 1 | Norvale Retail Group | 156.2 | 31.1% |
| 2 | Quillon Logistics | 41.2 | 8.2% |
| 3 | Ardent Parcel Co. | 28.9 | 5.8% |
| 4 | Pinecrest Distribution | 17.4 | 3.5% |
| 5 | Harbor & Vine Grocers | 15.1 | 3.0% |
| 6-10 | Meridale, Cobalt, Westfork, Sunreach, Tidewell | 12.6 / 11.0 / 9.8 / 8.7 / 7.9 | |
| | Top 10 | 308.8 | 61.5% |

Norvale 38% of gross AR (about 46.2). Norvale bill-and-hold 24.6.

## Balance sheet, cash and KPIs

| Metric | FY2024 | FY2025 | Jun 2026 |
|---|---|---|---|
| Cash | 48.3 | 41.6 | 33.9 |
| Total debt | 200.0 | 220.0 | 227.5 |
| Net debt | 151.7 | 178.4 | 193.6 |
| DSO (days) | 63.5 | 86.4 | 85.4 |
| Allowance / gross AR | 3.8% | 2.1% | 3.2% |
| Inventory days | 93.4 | 87.9 | 111.1 |
| Operating cash flow | 40.8 | 9.7 | -4.2 (H1) |
| Free cash flow | 24.6 | -10.1 | -13.0 (H1); LTM -26.4 |
| Hardware backlog | 168.0 | 131.0 | 118.0 |
| FieldOS ARR | 109.5 | 139.2 | 146.8 |
| NRR | 119% | 118% | 111% |

## Covenant

| Item | Value | Source |
|---|---|---|
| Max Total Net Leverage | 3.50x to Jun 30, 2026; 3.00x from Sep 30, 2026 | 10-K Note 9 |
| Reported ratio Jun 30, 2026 | 2.26x | 10-Q |
| Cash netting cap | 25.0 | 10-K Note 9 |
| Permitted add-back cap | 15% of Consolidated EBITDA before add-backs | 10-K Note 9 |
| Revolver commitment / available | 75.0 / 25.8 | 10-Q |
| Covenant net debt Jun 30, 2026 | 202.5 (227.5 - 25.0 cap) | FIN-015 |
| EBITDA that reproduces 2.26x | 89.6 (= uncapped Adj. EBITDA 89.7) | FIN-015 |
| Covenant EBITDA as defined (LTM) / SBC / other add-backs | 48.6 / 17.8 / 23.7 | FIN-016 |
| Jun 30 ratio: Reading A (SBC outside cap) / Reading B (inside) | 2.65x / 3.62x (limit 3.50x) | FIN-016 |
| Sep 30 ratio Reading A (guidance proxy / run-rate) | 2.84x / 3.35x (limit 3.00x) | FIN-017 |
| Dec 31 ratio Reading A (guidance high / mid / low) | 3.06x / 3.29x / 3.56x (limit 3.00x) | FIN-018 |
| Dec 31 ratio Reading B (guidance mid) | 4.97x | FIN-018 |
| FY2025 hardware growth reported / ex bill-and-hold | 15.1% / 2.9% | FIN-020 |
| Implied price at 11.46x on guidance 70.0 / 74.0 / 78.0 | $12.60 / $13.55 / $14.50 | FIN-021 |

## Change of control and exposures

| Item | Value | Source |
|---|---|---|
| Executive CoC payments | 28.6 (17.6 single-trigger equity) | DEF 14A |
| Debt repayable on CoC | about 227.5 | 10-K Note 9; balance_sheet.csv |
| Vantor damages (Vantor expert / complaint floor) | 96.4 / at least 140.0 | LIT-001 |
| Gen-3 revenue at risk | about 211.0 (42.0%) | 10-K, computed |
| Pinecrest claim / contractual cap (company estimate) | 12.0 / about 1.4 | LIT-004 |
