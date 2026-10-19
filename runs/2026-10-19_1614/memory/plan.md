# Diligence plan

Status: Drafted 2026-10-19 15:03. Awaiting Checkpoint 1 approval.

**Target:** kestrel (Corvane Diagnostics, Inc., NASDAQ: CRVD). Fictional.
**Deal:** Halvard Ridge Fund IV take-private at US$24.00 per share, equity value US$1,257.6m, EV US$1,648.6m, 13.2x FY2025 Adjusted EBITDA of US$125.3m. New term loan B of US$750.0m (6.0x), conditioned on no MAE and LTM Adjusted EBITDA of at least US$110.0m at closing. Signing mid-December 2026, closing Q2 2027.
**Source folder:** `targets/kestrel/data/`

## 1. IC questions and who answers them

| # | IC question | Lead analysts | Supporting |
|---|---|---|---|
| Q1 | Quality of earnings: are revenue and Adjusted EBITDA real, recurring and large enough for the price and a 6.0x term loan? | financial-analyst | sec-filings-analyst (EBITDA definition, revenue recognition), news-media-analyst (guidance cut, short report) |
| Q2 | Reimbursement and compliance: exposure to Medicare pricing, payer behavior and fraud and abuse risk | litigation-analyst (qui tam, DOJ), news-media-analyst (CMS fee schedule, DOJ probe) | financial-analyst (payer mix), sec-filings-analyst (risk factors) |
| Q3 | Legal and regulatory: matters that could block or delay closing, change value or need protection | litigation-analyst | sec-filings-analyst (legal proceedings note), news-media-analyst (FDA, ransomware) |
| Q4 | Capital structure: balance sheet, covenants, liquidity and change-of-control provisions between now and closing | financial-analyst, sec-filings-analyst | none |
| Q5 | Disclosure, controls and governance: disclosures, internal controls, incentives, related parties | sec-filings-analyst | news-media-analyst (compliance chief exit), litigation-analyst (whistleblower), financial-analyst |
| Q6 | Price and structure: does US$24.00 still make sense, and what protections are needed? | lead agent (synthesis) | all four |

## 2. Hypotheses to test

- **H1:** Reported FY2025 Adjusted EBITDA of US$125.3m overstates recurring earnings (aggressive add-backs, one-off revenue), and LTM Adjusted EBITDA is trending toward the US$110.0m financing condition after the August 2026 guidance cut.
- **H2:** The deal brief's base case is stale: flat Medicare rates, guidance midpoint of US$137.0m and full conversion of the Veltrane backlog no longer hold after July to August 2026 events.
- **H3:** Corvane has legal, regulatory or cyber exposure (qui tam / DOJ probe, patent case, data breach, FDA action) that its filings understate or disclose late, and that needs a specific protection.
- **H4:** Controls and governance are weaker than disclosed (compliance officer departure, internal control issues, incentive design tied to Adjusted EBITDA, related-party arrangements).

## 3. Task lists

### sec-filings-analyst (`sec-filings/`)
1. Adjusted EBITDA definition and reconciliation as disclosed; any change in definition between the 10-K and the Q2 10-Q.
2. Revenue recognition: variable consideration, implicit price concessions, payer reserves, biopharma backlog definition and any one-off items.
3. Credit agreement: maturities, covenants (definition, levels, headroom), change-of-control and prepayment terms.
4. Legal proceedings and contingencies disclosed, with dates. Compare with what the 8-Ks and 10-Q say.
5. Internal controls (material weaknesses, ICFR conclusions), auditor matters, impairment tests and other dated judgments.
6. Proxy: executive pay metrics, related-party transactions, board independence, change-of-control payments.
7. The two 8-Ks: what was disclosed, when, and what was left out (network disruption, Q2 guidance).
8. Customer and payer concentration as disclosed; segment results.

### news-media-analyst (`news/`)
1. Review all 13 articles, rate each source's reliability, and separate facts from allegations.
2. Short seller report: specific claims, which are verifiable.
3. DOJ probe, compliance chief exit, ransomware attack, FDA enforcement, CMS fee schedule, Veltrane trial halt, reagent tariffs, guidance cut, take-private talks: key facts, dates and numbers.
4. Flag timing: events reported before a related filing that may not mention them.
5. Note any irrelevant or low-value items as Low findings.

### litigation-analyst (`litigation/`)
1. Each docket matter: parties, court, claims, posture, key upcoming dates, exposure estimates, injunction risk.
2. The qui tam (Whitcomb): relator, allegations, government intervention status, damages theory (trebling, per-claim penalties).
3. Genaro patent matter: injunction risk to OncoTrace or other products.
4. Data security litigation: class size, claims, insurance.
5. Hollis matter: nature and exposure.
6. Recent docket changes and timing relative to Corvane filings.

### financial-analyst (`financials/`)
1. Rebuild FY2025 and LTM Adjusted EBITDA from the reconciliation; test each add-back for recurrence.
2. Quarterly revenue trend; identify one-offs; underlying growth vs. reported 11.7%.
3. LTM Adjusted EBITDA vs. the US$110.0m financing condition and 6.0x leverage; covenant headroom.
4. Payer and client concentration from `revenue_by_customer.csv` (Medicare, Veltrane, Orvia and others), with ranks and amounts.
5. Cash flow quality: cash conversion, DSO, working capital, capex.
6. Balance sheet: net debt, liquidity, debt maturities; reconcile to brief's US$391.0m net debt and US$424.7m repayment.
7. KPIs: test volumes, price per test, backlog, retention.
8. Valuation: implied multiples on adjusted and LTM figures.

## 4. Iteration budget and stop conditions

- At most **3** Act/Observe iterations.
- Stop when all six IC questions are answered with cited evidence, or the budget is used up.
- Loop again only if a Critical or High question can still be answered from available data.
