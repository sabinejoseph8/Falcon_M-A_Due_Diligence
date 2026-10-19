## Financial analyst: findings (Iteration 2, Project Kestrel / Corvane Diagnostics)

### Files reviewed

All files are in `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/`:
- `financials/README.md`
- `financials/income_statement.csv`
- `financials/adjusted_ebitda_reconciliation.csv`
- `financials/balance_sheet.csv`
- `financials/cash_flow.csv`
- `financials/kpis.csv`
- `financials/revenue_quarterly.csv`
- `financials/revenue_by_customer.csv`
- `deal-brief.md` (context only)

I also used the facts the lead agent passed on: the 10-K covenant definition, the 14.2 change in estimate, the Aug 5 2026 8-K guidance, the CMS 0419U rate, the 10-Q 40% commercial linkage, the Veltrane terms and halt, and the deal-brief financing condition. I cite each where I use it. None of the files contained instruction-like text.

### Key metrics table

US$ millions. "Diligence" rows are my adjustments, not company-reported figures.

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 / LTM Q2 2026 |
|---|---|---|---|---|
| Total revenue (reported) | 348.0 | 386.0 | 431.0 | H1 203.4 / LTM 429.2 |
| Revenue growth (reported) | 11.4% | 10.9% | 11.7% | H1 -0.9% |
| Revenue excluding the Q4 2025 14.2 one-off (diligence) | 348.0 | 386.0 | 416.8 (growth 8.0%) | LTM 415.0 |
| Operating income (reported) | 39.1 | 48.7 | 62.1 | H1 6.0 / LTM 41.5 |
| Adjusted EBITDA, company definition (reported) | 82.4 | 99.9 | 125.3 | H1 54.1 / LTM 123.4 |
| Adjusted EBITDA margin (reported) | 23.7% | 25.9% | 29.1% | H1 26.6% / LTM 28.8% |
| Adjusted EBITDA excluding the 14.2 one-off (diligence) | 82.4 | 99.9 | 111.1 | LTM 109.2 |
| Consolidated EBITDA, covenant definition (diligence) | 76.5 | 92.1 | 111.9 | LTM 90.2 |
| Net debt (balance sheet) | 375.0 | 371.4 | 391.0 | 395.9 |
| Consolidated Net Leverage Ratio (diligence) | 4.90x | 4.03x | 3.49x | 4.39x |
| Operating income / interest | 1.15x | 1.40x | 1.82x | LTM 1.19x |
| Free cash flow (reported memo) | 3.5 | 5.1 | -5.1 | H1 -4.3 |
| Revolver drawn | 0.0 | 10.0 | 30.0 | 35.0 |

Workings:
- LTM revenue = 431.0 - 205.2 + 203.4 = 429.2. Quarterly check: 105.3 + 120.5 + 102.6 + 100.8 = 429.2.
- LTM operating income = 62.1 - 26.6 + 6.0 = 41.5.
- Net debt = revolver + term loan - cash. FY2023: 0.0 + 400.0 - 25.0 = 375.0. FY2024: 10.0 + 395.9 - 34.5 = 371.4. FY2025: 30.0 + 391.8 - 30.8 = 391.0. Q2 2026: 35.0 + 389.7 - 28.8 = 395.9.
- The covenant EBITDA build is in FIN-16. FY2023 and FY2024 are built the same way in FIN-24.

---

### Findings

#### FIN-16: Covenant EBITDA at June 30, 2026 is 90.2. Net leverage is 4.39x against a 4.50x limit, and the pass depends on the 14.2 one-off
- **Finding:** On the 10-K definition, LTM Consolidated EBITDA at June 30, 2026 is 90.2. Net leverage is 4.39x, which passes 4.50x by only 2.2 of EBITDA (2.4%). Leverage is already above the 4.00x limit that applies from Sep 30, 2026. If the Q4 2025 14.2 change in estimate is removed, the ratio is 5.36x, a breach.
- **Evidence:**
  - Pre-add-back base (LTM) = operating income 41.5 + D&A (25.4 - 12.4 + 13.6 = 26.6) + SBC (9.8 - 4.8 + 5.3 = 10.3) = 78.4.
  - SBC is non-cash. The cash flow statement adds it back as a non-cash item (row 4: 9.8 in FY2025, 5.3 in H1 2026), in the same amounts as the reconciliation (row 8).
  - Sale-leaseback gain is excluded. The 6.8 gain (cash flow row 5) sits outside operating income. Operating income FY2025 = 189.2 - 104.6 - 17.3 - 5.2 = 62.1, which matches row 11, so the gain must be in "Other income" (7.2). Using operating income as the base excludes the gain and the other non-operating income, as the covenant requires.
  - Add-backs I treat as cash costs (LTM): restructuring 7.6, billing system transition 5.0, new lab start-up 4.2, legal and regulatory 6.7, cybersecurity 6.1, transaction 2.3. Total 31.9.
  - Excluded: payer denial and recoupment write-offs, 13.1. These are write-offs of receivables, not cash costs. They have also grown every year (4.2, 5.9, 7.8, 10.6), so they are a normal operating cost.
  - Cap = 15% x 78.4 = 11.76. Eligible add-backs of 31.9 exceed the cap, so the cap binds.
  - Consolidated EBITDA = 78.4 + 11.76 = 90.16, rounded to 90.2.
  - Ratio = 395.9 / 90.16 = 4.39x.
  - EBITDA needed at 4.50x = 395.9 / 4.50 = 88.0. Cushion = 90.16 - 87.98 = 2.2 (2.4%).
  - EBITDA needed at 4.00x = 395.9 / 4.00 = 99.0. Shortfall = 99.0 - 90.2 = 8.8. Alternatively, net debt would have to fall to 4.00 x 90.16 = 360.6, a reduction of 35.3.
  - Sensitivity 1, only restructuring counts (7.6, below the cap): 78.4 + 7.6 = 86.0. Ratio = 395.9 / 86.0 = 4.60x, a breach of 4.50x. If cybersecurity also counts (7.6 + 6.1 = 13.7, above the cap), the cap binds again and the ratio is back to 4.39x.
  - Sensitivity 2, the 14.2 removed: base 78.4 - 14.2 = 64.2. Consolidated EBITDA = 64.2 x 1.15 = 73.83. Ratio = 395.9 / 73.83 = 5.36x.
  - Dec 31, 2025 check: base 62.1 + 25.4 + 9.8 = 97.3. Cap = 15% x 97.3 = 14.6. Eligible cash add-backs = 5.2 + 4.4 + 3.9 + 3.1 + 0.0 + 0.8 = 17.4, so the cap binds. Consolidated EBITDA = 111.9. Ratio = 391.0 / 111.9 = 3.49x.
- **Source:** `financials/income_statement.csv` rows 10, 11, 13, 17. `financials/adjusted_ebitda_reconciliation.csv` rows 8 to 17. `financials/cash_flow.csv` rows 4, 5. `financials/balance_sheet.csv` rows 2, 16, 17. Covenant definition from the 10-K FY2025 Item 7, via the lead agent.
- **Severity:** High. June 30 passes, so there is no default at that date. But the pass depends on how the lenders read "cash costs" and on the 14.2 estimate change.
- **Confidence:** High for the arithmetic. Medium for which add-backs qualify as "non-recurring or unusual cash costs", which is an interpretation.
- **Deal impact:** Financing and closing risk, because covenant headroom before signing is thin.
- **Cross-check:** Get the June 30, 2026 compliance certificate (due by Aug 14, 2026) from the 10-Q exhibits or management. Confirm which add-backs Corvane claimed, and whether the credit agreement treats the 14.2 change in estimate as Consolidated EBITDA.

#### FIN-17: A covenant breach at the Sep 30, 2026 test looks likely before signing (projection)
- **Finding (projection):** Under every case I tested, leverage at Sep 30, 2026 is 4.48x to 5.01x, above the new 4.00x limit. At Dec 31, 2026 it is 5.64x to 7.72x. A breach is an event of default. The Sep 30 compliance certificate is due by about Nov 14, 2026 (45 days after Sep 30), which is before the mid-December signing.
- **Evidence:**
  - Assumption A: split the H2 2025 base between Q3 and Q4 2025. H2 2025 base = 97.3 - (26.6 + 12.4 + 4.8 = 43.8) = 53.5. Excluding the 14.2, that leaves 39.3, split by revenue excluding the one-off. Q3 2025 = 39.3 x 105.3 / (105.3 + 106.3) = 19.56. Q4 2025 = 19.74 + 14.2 = 33.94.
  - Assumption B: H2 2026 Adjusted EBITDA implied by guidance = (100 to 106) - 54.1 = 45.9 to 51.9, midpoint 48.9. Each quarter is half of H2.
  - Assumption C: H2 2026 add-backs equal H1 2026 (4.6 + 24.6 = 29.2), central case. The low case uses the H2 2025 level: (5.2 + 22.8) - (2.2 + 10.0) = 15.8. The cap binds in every case: H1 2026 eligible cash add-backs of 21.8 alone exceed 15% of any half-year base. So Consolidated EBITDA = 1.15 x base.
  - Case 1, guidance midpoint with H1-level add-backs (central): H2 2026 base = 48.9 - 29.2 = 19.7, so Q3 2026 = 9.85.
    - Sep LTM base = 33.94 + 24.9 + 9.85 = 68.69. Roll check: 78.4 - 19.56 + 9.85 = 68.69.
    - Consolidated EBITDA = 68.69 x 1.15 = 79.0. Ratio = 395.9 / 79.0 = 5.01x.
    - Dec 31 (FY2026) base = 24.9 + 19.7 = 44.6. Consolidated EBITDA = 44.6 x 1.15 = 51.3. Ratio = 7.72x.
  - Case 2, H1 2026 run rate: Q3 2026 base = 12.45.
    - Sep base = 33.94 + 24.9 + 12.45 = 71.29. Consolidated EBITDA = 71.29 x 1.15 = 82.0. Ratio = 4.83x.
    - Dec base = 49.8. Consolidated EBITDA = 49.8 x 1.15 = 57.3. Ratio = 6.91x.
  - Case 3, best case (top of guidance with low add-backs): H2 2026 base = 51.9 - 15.8 = 36.1, so Q3 2026 = 18.05.
    - Sep base = 76.89. Consolidated EBITDA = 76.89 x 1.15 = 88.4. Ratio = 4.48x.
    - Dec base = 61.0. Consolidated EBITDA = 61.0 x 1.15 = 70.2. Ratio = 5.64x.
  - EBITDA needed at 4.00x = 99.0. Sep shortfall: 20.0 (central), 17.0 (run rate), 10.6 (best case). Dec shortfall: 47.7, 41.7, 28.8.
  - Net debt trend: in H1 2026 net debt rose 4.9 (391.0 to 395.9; FCF -4.3, term loan repayments 2.1). Trending at the same pace gives Sep 30 net debt of about 398.4, so the central Sep ratio becomes 398.4 / 79.0 = 5.04x. Dec 31 is about 400.8, so 7.81x. At Dec 31 the 4.00x limit then needs 100.2 of EBITDA.
  - The 14.2 one-off is still in the Sep 30 LTM. It drops out at Dec 31, 2026.
- **Source:** Same rows as FIN-16, plus `financials/revenue_quarterly.csv` rows 8 and 9, and `financials/cash_flow.csv` rows 14 and 20. Guidance from the 8-K of Aug 5, 2026 and the covenant step-down from the 10-K Item 7, via the lead agent.
- **Severity:** Critical. Test met: a default before signing. The calibration rule says a covenant problem that causes a default before signing or closing is Critical. Projected Sep 30 leverage of 4.48x to 5.01x is above 4.00x in every case tested.
- **Confidence:** Medium. This is a projection. It rests on the Q3/Q4 split and an even H2 phasing, because there is no quarterly P&L below revenue. The breach still holds in the most favorable case.
- **Deal impact:** Closing risk and financing. Lenders could accelerate the debt or block revolver draws. Corvane may need a waiver or amendment before signing, which gives lenders leverage over the deal.
- **Cross-check:** Look for a Q3 2026 10-Q, an 8-K (Item 2.04 or 1.01 for an amendment or waiver), or news of lender talks. Ask management for the Q3 2026 compliance certificate and any waiver request.

#### FIN-18: The 2027 Medicare cut for 0419U removes about 29.0 to 30.3 of annual revenue and EBITDA, worth about 23% to 24% of the EV (projection)
- **Finding (projection):** The 30% cut to OncoTrace pricing, with the 40% commercial linkage, takes about 29.0 to 30.3 a year off revenue and EBITDA. At 13.2x that is 383.0 to 400.4, or 23.2% to 24.3% of the 1,648.6 EV.
- **Evidence:**
  - Rate change = (1,505 - 2,150) / 2,150 = -30.0%.
  - FY2025 mix:
    - Panel revenue = 314.8 x 44% = 138.5. Medicare = 138.5 x 55% = 76.2. Non-Medicare = 62.3.
    - Direct Medicare impact = 76.2 x 30% = 22.9. Linked commercial impact = 62.3 x 40% x 30% = 7.5.
    - Total = 30.3 a year.
  - H1 2026 mix:
    - Panel revenue = 146.0 x 45% = 65.7. Medicare = 65.7 x 56% = 36.8. Non-Medicare = 28.9.
    - Direct = 36.8 x 30% = 11.0. Linked = 28.9 x 40% x 30% = 3.5.
    - H1 total = 14.5, which annualizes to 29.0.
  - Flow-through assumption: 100%. This is a price-only change with no change in volume or cost, so the full revenue loss reaches EBITDA. Any cost actions would reduce the effect.
  - LTM Adjusted EBITDA at a June 30, 2027 closing date: the cut is effective Jan 1, 2027, so H1 2027 carries about 14.5. A closing tested at Mar 31, 2027 would carry about 7.3 (one quarter).
  - Value: 29.0 x 13.2 = 383.0, which is 383.0 / 1,648.6 = 23.2% of EV, or 7.31 per share (383.0 / 52.4). On the FY2025 mix: 30.3 x 13.2 = 400.4, which is 24.3% of EV, or 7.64 per share.
- **Source:** `financials/income_statement.csv` row 2. `financials/kpis.csv` rows 4 and 5. CMS rate from Healthcare Policy Daily (Jul 30, 2026). 40% linkage from the 10-Q Q2 2026. Both came via the lead agent.
- **Severity:** Critical. Test met: more than 10% of value (23.2% to 24.3% of EV).
- **Confidence:** Medium. This is a projection. It assumes the KPI "Medicare share" means traditional Medicare paid at the 0419U rate, 100% flow-through, and no change in volume or payer mix.
- **Deal impact:** Valuation, plus the financing condition (see FIN-22). It is not in the Aug 5 guidance.
- **Cross-check:** Check whether Medicare Advantage revenue is in the 56% (the KPI definition), the contract terms of the linked commercial contracts, and whether Corvane has filed for reconsideration or appealed. Look for an 8-K or press release quantifying the cut.

#### FIN-19: Without the 14.2 one-off, LTM Adjusted EBITDA is 109.2, already below the 110.0 financing condition, and the price at 13.2x is about 20 per share
- **Finding:** Removing the Q4 2025 change in estimate gives diligence-adjusted EBITDA of 111.1 for FY2025 and 109.2 LTM. That makes the deal 14.8x to 15.1x, and the price at 13.2x is 19.95 to 20.43 per share against the 24.00 offer.
- **Evidence:**
  - Company basis: FY2025 = 125.3. LTM = 125.3 - 56.0 + 54.1 = 123.4.
  - Excluding the one-off: FY2025 = 125.3 - 14.2 = 111.1. LTM = 123.4 - 14.2 = 109.2.
  - Second-tier view, also removing payer denial write-offs as a normal operating cost: FY2025 = 111.1 - 10.6 = 100.5. LTM = 109.2 - 13.1 = 96.1.
  - EV / EBITDA at 1,648.6:

    | EBITDA basis | EBITDA | Multiple |
    |---|---|---|
    | FY2025, company | 125.3 | 13.16x |
    | LTM, company | 123.4 | 13.36x |
    | FY2025, excluding one-off | 111.1 | 14.84x |
    | LTM, excluding one-off | 109.2 | 15.10x |
    | FY2025, second tier | 100.5 | 16.40x |
    | LTM, second tier | 96.1 | 17.16x |
    | FY2026 guidance midpoint | 103.0 | 16.01x |

  - Price at 13.2x with June 30 net debt of 395.9 and 52.4 million shares:

    | EBITDA basis | EBITDA | Price per share |
    |---|---|---|
    | FY2025, company | 125.3 | 24.01 |
    | LTM, company | 123.4 | 23.53 |
    | FY2025, excluding one-off | 111.1 | 20.43 |
    | LTM, excluding one-off | 109.2 | 19.95 |
    | FY2025, second tier | 100.5 | 17.76 |
    | LTM, second tier | 96.1 | 16.65 |
    | FY2026 guidance midpoint | 103.0 | 18.39 |

  - Example working, FY2025 excluding the one-off: (13.2 x 111.1 - 395.9) / 52.4 = (1,466.5 - 395.9) / 52.4 = 20.43.
  - Value of the one-off alone = 14.2 x 13.2 = 187.4, which is 11.4% of the 1,648.6 EV.
  - At 24.00 per share with June 30 net debt, EV = 1,257.6 + 395.9 = 1,653.5. The brief uses Dec 31 net debt (391.0), so it understates EV by 4.9.
  - The term loan B at 750.0 is 6.0x the reported 125.3. On 109.2 it is 750.0 / 109.2 = 6.87x.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv` rows 11 and 12 (FY2025, H1 2025, H1 2026, LTM). `financials/balance_sheet.csv` rows 2, 16, 17. `deal-brief.md` sections 2 and 3. The 14.2 is from the 10-K Item 7, via the lead agent.
- **Severity:** Critical. Two tests met. First, value: the one-off alone is 11.4% of EV, and the price at 13.2x falls from 24.01 to 20.43 (-14.9%). Second, closing: 109.2 is below the 110.0 condition.
- **Confidence:** High. The figures come straight from the company data and the 10-K amount, and the arithmetic is shown.
- **Deal impact:** Valuation and financing.
- **Cross-check:** Check the commitment letter's definition of "LTM Adjusted EBITDA (as Corvane defines it)". It matters whether the 14.2 stays in, since the company definition does not remove it. It drops out of LTM after Q4 2026 anyway.

#### FIN-20: The Q4 2025 one-off is 11.8% of Q4 revenue. Underlying FY2025 growth is 8.0%, not 11.7%
- **Finding:** The 14.2 is 11.8% of Q4 2025 revenue. Without it, Q4 2025 grew 5.4% year over year, and FY2025 grew 8.0% against the reported 11.7% in the investment thesis. This supports FIN-03 and FIN-19.
- **Evidence:**
  - Share of Q4 revenue = 14.2 / 120.5 = 11.8%.
  - Q4 2025 excluding the one-off = 106.3. Growth versus Q4 2024 = 106.3 / 100.9 - 1 = 5.4%, against 19.4% reported (120.5 / 100.9). Sequential growth = 106.3 / 105.3 - 1 = 0.9%.
  - FY2025 excluding the one-off = 431.0 - 14.2 = 416.8. Growth = 416.8 / 386.0 - 1 = 8.0%.
  - Comparison with FIN-03: my iteration-1 report is outside the files I can read, so I have not quoted the FIN-03 figure. A trend-based estimate of the Q4 excess is 11.6 to 13.2, the range FIN-03 would have come from:
    - Q4 2025 at the 2024 Q4/Q3 uplift: 105.3 x (100.9 / 97.6) = 108.9, which leaves an excess of 11.6.
    - At the average 2025 sequential step: Q1 to Q2 was +2.6 and Q2 to Q3 was +1.4, an average of +2.0. That gives 107.3 and an excess of 13.2.
    - The disclosed 14.2 sits just above that range, which fits a one-off on top of a slightly soft underlying quarter.
  - The lead agent should compare this with the FIN-03 card in the iteration-1 report.
- **Source:** `financials/revenue_quarterly.csv` rows 5, 8, 9. `financials/income_statement.csv` row 5.
- **Severity:** Medium on its own. It supports FIN-19, which carries the value impact.
- **Confidence:** High.
- **Deal impact:** Valuation. The thesis point 1 growth rate is stale.
- **Cross-check:** Check the 10-K Item 7 revenue discussion, to see whether the 11.7% is presented with or without a note on the estimate change.

#### FIN-21: Veltrane is 51% of biopharma revenue, and all of the segment's FY2025 growth came from it. The halt puts about 50.5 of revenue and about 14.7 of EBITDA at risk (projection)
- **Finding:** Veltrane brought in 50.5 in FY2025, which is 11.7% of total revenue and 51.2% of biopharma services. Without Veltrane, the segment shrank 7.1%. If the ATLAS-3 revenue is lost in full, about 13.4 to 14.7 of EBITDA (the range depends on which margin is used) is at risk, worth about 194.0 at 13.2x (11.8% of EV).
- **Evidence:**
  - Revenue: FY2024 = 38.0, FY2025 = 50.5, growth 32.9%. The customer file has no quarterly or half-year breakdown by customer.
  - Share of segment = 50.5 / 98.6 = 51.2%. This assumes all Veltrane revenue is in biopharma services.
  - Biopharma excluding Veltrane: 89.8 - 38.0 = 51.8 in FY2024 and 98.6 - 48.1... more precisely 98.6 - 50.5 = 48.1 in FY2025. Growth = 48.1 / 51.8 - 1 = -7.1%. The segment as a whole grew 9.8%.
  - Backlog: Veltrane is 61.0 of 231.4 = 26.4% of backlog. Book-to-bill in H1 2026 was 0.7 and backlog fell from 246.0 to 231.4. Both are signs of weakness.
  - EBITDA at risk (projection, at the average company Adjusted EBITDA margin):
    - FY2025 margin = 125.3 / 431.0 = 29.1%, so 50.5 x 29.1% = 14.7.
    - H1 2026 margin = 54.1 / 203.4 = 26.6%, so 50.5 x 26.6% = 13.4.
    - The average margin probably understates the loss, because central lab fixed costs stay. The real contribution margin is likely higher (inference).
  - Value: 14.7 x 13.2 = 194.0, which is 11.8% of 1,648.6.
  - Critical threshold: 10% of EV = 164.9, which is 12.5 of EBITDA, or 42.9 of revenue at 29.1%. That is 85% of Veltrane's FY2025 revenue. "Mostly ATLAS-3" may be below 85%.
  - H1 2027 phasing (projection): quarterly run rate = 50.5 / 4 = 12.6.
    - Central case: Q1 2027 at half rate during close-out and nothing in Q2. Revenue loss = 6.3 + 12.6 = 18.9, so EBITDA loss = 18.9 x 29.1% = 5.5.
    - Full loss across H1 2027: revenue 25.3, EBITDA 7.3.
- **Source:** `financials/revenue_by_customer.csv` row 3. `financials/income_statement.csv` row 3. `financials/kpis.csv` rows 7 and 8. The halt and the 90-day termination right are from the news of Aug 27, 2026 and the 10-K/10-Q, via the lead agent.
- **Severity:** High. It crosses the 10% Critical test only if 85% or more of Veltrane revenue is lost, and I cannot show that from this data.
- **Confidence:** Medium. I do not have the share of Veltrane revenue that is ATLAS-3, the close-out timing or the contribution margin.
- **Deal impact:** Valuation. It also contradicts deal-brief assumption 5 (the backlog converts on its historical schedule, including the Veltrane programs) and thesis point 3.
- **Cross-check:** Get the Veltrane work orders and any termination notices. Check Corvane's 8-K or 10-Q subsequent-events note for the termination. Check whether Veltrane is a 10% customer in the 10-K concentration note.

#### FIN-22: Projected LTM Adjusted EBITDA at June 30, 2027 is about 83.0 (range 78.2 to 91.5), well below the 110.0 financing condition (projection)
- **Finding (projection):** The financing condition is projected to fail on the company's own definition. FY2026 guidance alone (103.0 at the midpoint) is already below 110.0. After the 0419U cut and the Veltrane wind-down, LTM at June 30, 2027 is about 83.0, a shortfall of about 27.0.
- **Evidence:**
  - Step 1 (projection), H2 2026 from guidance: (100 to 106) - 54.1 = 45.9 to 51.9, midpoint 48.9.
  - Step 2 (projection), H1 2027 base at the H1 2026 run rate: 54.1.
  - Step 3 (projection), 0419U cut in H1 2027: -14.5 (FIN-18, 100% flow-through).
  - Step 4 (projection), Veltrane in H1 2027: -5.5 central, -7.3 full loss, 0.0 if close-out revenue runs at the full rate (FIN-21).
  - Step 5 (projection), H1 2027 = 54.1 - 14.5 - 5.5 = 34.1 central. Low case = 32.3. High case = 39.6.
  - LTM June 30, 2027:
    - Central = 48.9 + 34.1 = 83.0, a shortfall of 27.0 against 110.0.
    - Low = 45.9 + 32.3 = 78.2, a shortfall of 31.8.
    - High = 51.9 + 39.6 = 91.5, a shortfall of 18.5.
  - Without 0419U or Veltrane: 48.9 + 54.1 = 103.0, still 7.0 short.
  - The deal model assumed FY2026 at 137.0. The guidance midpoint is 103.0, a gap of 34.0 (24.8%).
  - The term loan B of 750.0 on the central 83.0 is 9.0x.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv` row 11 (H1 2026). Guidance from the 8-K of Aug 5, 2026. The 110.0 condition is from `deal-brief.md` section 3. FIN-18 and FIN-21 are inputs.
- **Severity:** Critical. Test met: it would block closing. The financing condition (110.0) fails in every case tested (78.2 to 91.5).
- **Confidence:** Medium. This is a projection, and it depends on guidance, the run rate and the assumptions in FIN-18 and FIN-21. The guidance-only shortfall needs no assumption beyond the 8-K.
- **Deal impact:** Closing risk and financing. It needs a renegotiated debt package or a price change.
- **Cross-check:** Get the commitment letter's definition and test date for "LTM at closing". Check for any lender MAE or flex terms. Look for Q3 2026 results.

#### FIN-23: The data does not give the revolver commitment or availability. Liquidity depends on revolver draws while free cash flow is negative
- **Finding:** The revolver balance went from 0.0 to 35.0 over FY2023 to June 30, 2026, funding negative free cash flow and term loan repayments. The data pack has no commitment size, availability, maturity or pricing.
- **Evidence:**
  - Revolver balance: 0.0 (FY2023), 10.0 (FY2024), 30.0 (FY2025), 35.0 (June 30, 2026).
  - Net draws: 10.0, 20.0, and 5.0 in H1 2026.
  - H1 2026: FCF -4.3, term loan repayments -2.1 and other -0.6, so the 5.0 draw left cash down 2.0 at 28.8.
  - Interest cover (LTM): operating income / interest = 41.5 / 34.8 = 1.19x. Consolidated EBITDA / interest = 90.2 / 34.8 = 2.59x.
  - If an event of default happens (FIN-17), lenders may be able to stop further draws (inference). On-balance-sheet cash is only 28.8.
- **Source:** `financials/balance_sheet.csv` rows 2 and 16. `financials/cash_flow.csv` rows 13, 14, 17, 19, 20. `financials/income_statement.csv` row 12.
- **Severity:** Medium. It becomes High if availability is small relative to cash burn. That cannot be shown from this data.
- **Confidence:** High for the figures. Availability is unknown.
- **Deal impact:** Liquidity before closing.
- **Cross-check:** Check the credit agreement exhibit to the 10-K for the commitment, maturity and draw conditions (no default as a condition precedent). Check the 10-Q liquidity section for availability.

#### FIN-24: Leverage computed on the covenant definition was 4.90x at FY2023, above today's 4.50x maximum. The covenant history is unclear
- **Finding:** Applying the 10-K definition to FY2023 gives 4.90x and FY2024 gives 4.03x. Either the covenant level was higher before, or it was amended, or the add-back treatment was different.
- **Evidence:**
  - FY2023: base = 39.1 + 20.5 + 7.1 = 66.7. Cap = 10.0. Eligible = 3.4 + 3.1 + 2.4 + 0.9 = 9.8. Consolidated EBITDA = 76.5. Ratio = 375.0 / 76.5 = 4.90x.
  - FY2024: base = 48.7 + 23.0 + 8.4 = 80.1. Cap = 12.0. Eligible = 4.0 + 3.6 + 3.0 + 1.4 = 12.0. Consolidated EBITDA = 92.1. Ratio = 371.4 / 92.1 = 4.03x.
- **Source:** `financials/income_statement.csv` rows 11 and 17. `financials/adjusted_ebitda_reconciliation.csv` rows 8 to 17. `financials/balance_sheet.csv` rows 2, 16, 17.
- **Severity:** Low.
- **Confidence:** Medium. I do not have the historical covenant levels.
- **Deal impact:** Disclosure and history of covenant relief.
- **Cross-check:** Look for credit agreement amendments in the 8-K and 10-K exhibit lists for 2023 and 2024.

### Positive or mitigating points
- Net debt matches the deal brief at Dec 31, 2025 (391.0). The June 30 total debt of 424.7 equals the brief's repayment amount, so the use of funds is internally consistent.
- At closing, the existing credit agreement is repaid. A covenant default cured by that refinancing would on its own be High, not Critical. The FIN-17 rating is Critical only because the breach is projected before signing.
- Lab informatics is stable: ARR 17.0 and retention 95%.
- The FY2025 cash add-backs I accepted (17.4) exceed the cap (14.6), so the cap, not the add-back debate, drives the covenant figure.

### Gaps and questions for management
1. Covenant compliance certificates for Q4 2025, Q1 2026 and Q2 2026, with the add-backs claimed and their treatment of the 14.2.
2. The Q3 2026 covenant forecast, and any waiver or amendment talks with lenders.
3. Revolver commitment, availability, maturity and draw conditions.
4. Quarterly P&L below revenue for Q3 2025, Q4 2025, Q1 2026 and Q2 2026, to replace my Q3/Q4 2025 split assumption.
5. H2 2026 forecast of add-backs, by category.
6. Veltrane revenue by quarter, the share from ATLAS-3, close-out terms, any termination notice and the contribution margin.
7. Whether the KPI "Medicare share" includes Medicare Advantage, and the list of commercial contracts priced off the Medicare rate.
8. Where in the P&L the payer denial and recoupment write-offs are recorded (revenue, cost of revenue or SG&A).
9. Historical covenant levels and amendments, to explain the 4.90x at FY2023.
