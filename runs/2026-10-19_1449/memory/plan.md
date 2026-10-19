# Diligence plan: Project Kestrel (Corvane Diagnostics, NASDAQ: CRVD)

Status: Approved at Checkpoint 1 (2026-10-19). Complete: 2 of 3 iterations used; report written.
Target: `kestrel`. Sources: `targets/kestrel/data/`.

## Deal in one paragraph

Halvard Ridge Capital Partners Fund IV proposes an all-cash take-private of Corvane Diagnostics at US$24.00 per share (equity US$1,257.6 million, EV US$1,648.6 million, 13.2x FY2025 Adjusted EBITDA of US$125.3 million). Financing is a US$750.0 million term loan B (6.0x FY2025 Adjusted EBITDA) plus US$980.0 million of fund equity. The commitment letter requires no MAE and LTM Adjusted EBITDA (Corvane definition) of at least US$110.0 million at closing. Signing is targeted for mid-December 2026 and closing for Q2 2027. The model was built as of June 30, 2026 and the premium is set against the July 31, 2026 price of US$18.10.

## The six IC questions and who answers them

| # | IC question | Primary analysts | Supporting |
|---|---|---|---|
| 1 | Quality of earnings: are revenue and Adjusted EBITDA real, recurring and large enough for the price and a 6.0x term loan? | financial-analyst | sec-filings-analyst, news-media-analyst |
| 2 | Reimbursement and compliance: Medicare pricing, payer behavior, fraud and abuse risk | litigation-analyst, news-media-analyst | financial-analyst, sec-filings-analyst |
| 3 | Legal and regulatory: matters that could block or delay closing, change value or need a protection | litigation-analyst | sec-filings-analyst, news-media-analyst |
| 4 | Capital structure: balance sheet stability to closing, covenants, liquidity, change of control | sec-filings-analyst, financial-analyst | none |
| 5 | Disclosure, controls and governance: disclosures, internal controls, incentives, related parties | sec-filings-analyst | news-media-analyst, litigation-analyst |
| 6 | Price and structure: does US$24.00 still make sense, and what protections are needed? | lead agent (synthesis) | all |

## Hypotheses to test

- **H1 (earnings quality):** FY2025 Adjusted EBITDA of US$125.3 million is inflated by aggressive add-backs or one-off revenue, and run-rate LTM Adjusted EBITDA in 2026 is falling toward the US$110.0 million financing floor. The FY2026 guidance midpoint of US$137.0 million used in the model is stale after the August 2026 guidance cut.
- **H2 (reimbursement and fraud and abuse):** Medicare and payer exposure (the CMS lab fee schedule change, the DOJ genetic-testing probe and the qui tam case) creates a material liability and a revenue headwind that filings understate or disclose late.
- **H3 (backlog and concentration):** The US$246.0 million biopharma backlog depends heavily on Veltrane Therapeutics, whose halted Atlas-3 trial makes part of the backlog unlikely to convert. The model still assumes conversion on the historical schedule.
- **H4 (balance sheet and disclosure):** Covenant headroom, the ransomware incident costs and change-of-control terms put the balance sheet under strain before closing, and some events (compliance chief exit, ransomware, litigation) were disclosed late, incompletely or inconsistently.

## Task lists

### sec-filings-analyst (`sec-filings/`)
1. Revenue recognition, segment results and any one-off or non-recurring revenue in the FY2025 10-K and Q2 2026 10-Q.
2. Internal controls: any material weakness, auditor change or control remediation; quality of disclosure controls.
3. Debt: the existing credit agreement, financial covenant definitions and levels, headroom, maturity, change-of-control and prepayment terms.
4. Legal proceedings, contingencies, reserves and government investigations as disclosed; dated judgments (reserve levels, impairment tests, materiality conclusions) and their dates.
5. Customer and payer concentration, biopharma backlog and Veltrane disclosures.
6. The two 8-Ks: ransomware disclosure timing and content; Q2 results and guidance change.
7. DEF 14A: compensation metrics (especially Adjusted EBITDA-linked pay), change-of-control payments, related-party transactions, board and compliance governance.
8. Changes in wording or numbers between the 10-K and the 10-Q.

### news-media-analyst (`news/`)
1. Rate each source's reliability; label rumors and allegations.
2. DOJ genetic-testing probe, compliance chief exit and Bearhaven short report: claims, evidence and company responses.
3. Ransomware attack: timing, operational impact and billing effects versus company statements.
4. CMS lab fee schedule change: rate impact on Corvane's tests and timing.
5. Guidance cut, Veltrane Atlas-3 halt, sequencing reagent tariffs and the take-private talks article.
6. Flag any article about a different entity with a similar name, and irrelevant items.

### litigation-analyst (`litigation/`)
1. Each matter: parties, court, posture, key upcoming dates, damages or exposure, injunction risk, recent changes.
2. Whitcomb qui tam: allegations, DOJ intervention status, False Claims Act exposure math (treble damages, penalties).
3. Genaro v. Corvane: any IP or injunction risk to OncoTrace or other products.
4. Data security litigation: class size, claims, insurance.
5. Hollis v. Corvane: nature and any links to compliance or whistleblower issues.
6. Docket dates compared with filing dates, so the lead agent can test disclosure timing.

### financial-analyst (`financials/`)
1. Revenue growth reported versus underlying (strip out one-offs and acquisitions); quarterly trend into 2026.
2. Adjusted EBITDA add-backs: test each one for being recurring or non-recurring; recompute a diligence-adjusted EBITDA for FY2025 and LTM Q2 2026.
3. LTM Adjusted EBITDA versus the US$110.0 million financing floor and the 6.0x leverage sizing.
4. Payer and client concentration in `revenue_by_customer.csv`, including Medicare, Veltrane and any named party.
5. Working capital: DSO, allowances for credit losses or implicit price concessions, cash conversion.
6. Net debt check versus the deal brief's US$391.0 million and the US$424.7 million repayment.
7. KPIs: test volumes, revenue per test, backlog, retention.

## Iteration budget and stop conditions

- At most 3 Act/Observe iterations.
- Stop when all six IC questions are answered with cited evidence, or the budget is used up.
- Loop again only if a Critical or High question can still be answered from the available data.
