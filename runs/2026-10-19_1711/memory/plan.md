# Diligence plan

Status: Drafted, awaiting Checkpoint 1.
Target: heron (Project Heron). Delmora Home Systems, Inc. (NASDAQ: DLHS). Acquirer: Meridale Capital Partners Fund IV, take-private at US$24.50 per share (equity US$1,283.8m, EV US$1,543.4m, 11.8x LTM Q2 2026 Adjusted EBITDA of US$130.4m). Sign by November 30, 2026 (end of exclusivity); close Q1 2027.

Source folder: `targets/heron/data/`.

## The six IC questions and who answers them

| # | IC question | Primary analysts | Supporting |
|---|---|---|---|
| Q1 | Quality of earnings and cash flow: is LTM Adjusted EBITDA US$130.4m and H1 2026 operating cash flow a sound base for price and debt? Adjustments? | financial-analyst | sec-filings-analyst (non-GAAP reconciliation, revenue recognition, cash flow notes, controls) |
| Q2 | Inherited liabilities: contingent, off-balance-sheet, change-of-control; size versus price | sec-filings-analyst, financial-analyst | litigation-analyst (exposures), news-media-analyst |
| Q3 | Technology and data rights: ownership of AdaptiveComfort and core IP; right to use customer data for Insights and OEM licensing | litigation-analyst, sec-filings-analyst | news-media-analyst |
| Q4 | Regulatory, trade, product safety and legal: what could delay or block closing or impair the business | litigation-analyst, news-media-analyst | sec-filings-analyst |
| Q5 | Revenue durability: utility programs, subscriptions, distributors over the hold period | financial-analyst, news-media-analyst | sec-filings-analyst (concentration, contract terms) |
| Q6 | Price and protections: is US$24.50 supportable; price, structure, conditions, protections | Lead (synthesis) | all four |

## Hypotheses to test

- **H1 (earnings quality):** LTM Adjusted EBITDA of US$130.4m and H1 2026 operating cash flow overstate the sustainable base (aggressive add-backs, one-off revenue, working capital timing such as receivable sales or payables stretch).
- **H2 (inherited liabilities):** the model understates debt-like and contingent items: Pittock pension funding, Nimbus earn-out, the Aura field action beyond the US$6.0m reserve, change-of-control payments, tax exposures and litigation that management calls immaterial.
- **H3 (tech and data rights):** the Insights and OEM licensing plan (about US$310m of EV) rests on IP ownership and customer data consents that are contested or limited.
- **H4 (revenue durability):** Utility Programs (Western States Energy Alliance renewal), subscriptions and international distributor sales (Middle East) are less durable or less clean than the thesis assumes, including trade, tariff or export-control exposure.

## Task lists

### sec-filings-analyst (`targets/heron/data/sec-filings/`)
1. Revenue recognition by segment (Devices, Subscriptions & Services, Utility Programs, Insights); any one-off, bill-and-hold, distributor or multiple-element items; changes between the 10-K and 10-Q.
2. Non-GAAP: reconcile Adjusted EBITDA definitions and add-backs; changes in definition.
3. Debt: credit agreement terms, covenants, change-of-control provisions, maturities.
4. Contingencies and off-balance-sheet items: Pittock pension (funded status, assumptions, contributions), Nimbus earn-out, Aura field action and warranty reserves, guarantees, purchase commitments, tax reserves.
5. Risk factors and legal proceedings; compare with the litigation docket and with 8-K dates (anything filed after an event and not mentioning it).
6. IP and data: ownership of AdaptiveComfort, licenses, privacy policy and data consent disclosures for Insights.
7. Customer and segment concentration, utility contract terms (WSEA renewal), distributor terms.
8. Internal controls, auditor matters, the two 8-Ks (May 14 and July 28, 2026).
9. Proxy: change-of-control payments, golden parachutes, related-party transactions, governance.
10. Dated accounting judgments (goodwill or impairment test dates, reserve levels, materiality conclusions) with their dates.

### news-media-analyst (`targets/heron/data/news/`)
1. All 14 articles: summary, reliability rating, interested parties.
2. Product safety (Aura thermostat), recalls, regulator attention.
3. Data privacy and Insights; AdaptiveComfort IP disputes.
4. Utility customers (WSEA renewal), subscriptions churn, Middle East distributors, trade and tariff matters (Mexico assembly, export controls).
5. Management, short sellers, employee or whistleblower claims; any market or share price data after filing dates.
6. Dates of each event, for comparison with filing dates.

### litigation-analyst (`targets/heron/data/litigation/`)
1. All 7 docket matters, including the 3 without case files: posture, next dates, exposure, injunction risk, recent changes.
2. IP and ownership disputes over core technology; data privacy class actions or regulatory inquiries.
3. Product safety (CPSC or similar) matters; trade, customs or export-control matters; utility contract or government matters.
4. Pension, earn-out or employment disputes.
5. Matters that could delay or block closing; dismissed, settled or closed matters (give them their own IDs).
6. Filing and event dates.

### financial-analyst (`targets/heron/data/financials/`)
1. Rebuild LTM Q2 2026 Adjusted EBITDA from the data; test each add-back; flag one-offs and recurring "non-recurring" items.
2. Cash flow quality: H1 2026 operating cash flow drivers (receivables, factoring, payables, inventory, deferred revenue, customer prepayments).
3. Net debt and debt-like items: pension, earn-out, leases, reserves, working capital normalization.
4. Segment trends: Devices, Subscriptions & Services, Insights, Utility Programs; margins; gross margin path versus 42% assumption.
5. Customer concentration from `revenue_by_customer.csv`: top customers, WSEA share, distributor growth by region (Middle East).
6. KPIs: subscribers, churn, ARPU, device units, returns or warranty claims.
7. Leverage at close (US$900.0m TLB) on reported and adjusted EBITDA; valuation checks.

## Iteration budget and stop conditions

- At most **3** Act/Observe iterations.
- Stop when all six IC questions have cited evidence, or when the budget is used up.
- Loop again only if a Critical or High question can still be answered from the data room.
