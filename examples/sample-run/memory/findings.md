# Findings register

Single source of truth for every finding. Never delete a finding; change its status. Full analyst cards are in `memory/analyst-reports/`. Cross-source (`X-`) findings created by the lead agent have full cards at the end of this file.

Abbreviations: 10-K = `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`; 10-Q = `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`; DEF 14A = `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`; IS, BS, CF = income statement, balance sheet and cash flow CSVs in `data/financials/`; recon = `adjusted_ebitda_reconciliation.csv`.

## Iteration 1: analyst findings

### SEC filings analyst (full cards: `analyst-reports/iteration-1_sec-filings-analyst.md`)

| ID | Finding | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|
| SEC-01 | FY2026 guidance cut on Aug 6, 2026 to $470M to $490M revenue and $70M to $78M Adj EBITDA; deal model still uses the superseded March case ($560M / $118M) | Critical | High | 10-Q Part I Item 2; 10-K Item 7; deal brief | Verified |
| SEC-02 | Norvale (31.1% of revenue, 38% of gross AR) can terminate its MSA on 90 days' notice after a change of control; no minimum volumes; MSA expires Sep 30, 2027 | Critical | High | 10-K Items 1 and 1A, Notes 2 and 13 | Verified |
| SEC-03 | $31.8M of Q4 2025 hardware revenue was bill-and-hold (20.6% of Q4; $24.6M from the largest customer); excluding it, FY2025 growth is 11.6% and Q4 growth 5.1% | High | High | 10-K Note 2, Item 7 | Verified |
| SEC-04 | $9.4M of the bill-and-hold products were returned and credited in Q2 2026 under a contract amendment, booked as a 2026 revenue reduction rather than a 2025 correction | High | High (facts) | 10-Q Part I Item 2; 10-K Note 2 | Verified |
| SEC-05 | Auditor dismissed in Nov 2025 after flagging a material weakness and the need for expanded Q4 procedures; adverse internal control opinion; still unremediated at Jun 30, 2026 | High | High | 8-K 2025-11-14; 10-K Item 9A; 10-Q Part I Item 4 | Verified |
| SEC-06 | CFO resigned Jan 2026 with a $900,000 separation payment and release; interim CFO since February | High | High | 8-K 2026-01-21; 10-K Note 18; 10-Q | Verified |
| SEC-07 | Securities class action (Jun 2026) on revenue and internal control statements, filed 22 days after the May 12, 2026 short-seller report; the complaint names that report and the Nov 14, 2025 8-K as corrective disclosures; no accrual disclosed | High | High | 10-Q Part II Item 1 | Partially verified |
| SEC-08 | Vantor patent suit seeks an injunction on Gen-3 (about 70% of hardware revenue, about $211M or 42% of FY2025 revenue); no accrual; trial Mar 2027 | High | High | 10-K Items 1, 1A, 3; 10-Q Part II Item 1 | Verified |
| SEC-09 | Covenant maximum steps down to 3.00x from Sep 30, 2026; the reported 2.26x ties only to uncapped Adj EBITDA (about 2.65x if the 15% add-back cap applies as summarized in Note 9; see FIN-17); change of control is an event of default (about $227.5M to repay) | High | High (terms) / Medium (forecast) | 10-K Note 9; 10-Q Part I Item 2 | Partially verified |
| SEC-10 | Gross AR up 59% vs revenue up 19%; operating cash flow down 76%; allowance cut to 2.1% of gross AR | Medium | High | 10-K Notes 5 and 13, Item 7 | Open |
| SEC-11 | 2025 bonuses paid at 142% of target; without the $31.8M bill-and-hold revenue, revenue would be $470.5M, $0.5M above the threshold and $19.5M below target | Medium | High (plan) / Medium (counterfactual) | DEF 14A; 10-K Note 2 | Partially verified |
| SEC-12 | Single-trigger equity vesting; $28.6M of change-in-control payments, $17.6M of it equity acceleration | Medium | High | DEF 14A | Open |
| SEC-13 | CEO-family landlord can reset HQ rent to "fair market value" (landlord-chosen appraiser) on a change in control; no lead independent director | Medium | High | DEF 14A | Verified |
| SEC-14 | April 2026 cyber incident judged "not material" despite $1.8M of costs, $2.3M of credits and a $12.0M customer suit; risk factors called unchanged | Medium | High (facts) / Medium (view) | 10-Q | Open |
| SEC-15 | Single-source LiDAR supplier in China; no qualified second source | Medium | High | 10-K Items 1 and 1A | Open |
| SEC-16 | 10-Q recasts Q4 "deliveries" as "pull-forward"; ARR and retention no longer disclosed; no remediation timetable | Medium | Medium | 10-K Item 7, 9A; 10-Q | Open |
| SEC-17 | Goodwill ($98.4M, of which $57.4M Lumora) last tested Oct 1, 2025, before the guidance cut | Low | Medium | 10-K Note 15 | Open |
| SEC-18 | Ruiz $3.2M settlement accrued | Low | High | 10-K Item 3; 10-Q | Open |

### Litigation analyst (full cards: `analyst-reports/iteration-1_litigation-analyst.md`)

| ID | Finding | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|
| LIT-01 | Vantor case has turned against Talonfield: Jul 22, 2026 claim construction order adopted Vantor's construction on 3 of 4 terms, including "localization map"; Gen-3 Plus added; stay denied; PTAB refused to review the '557 patent | Critical | High (rulings) | LIT-001 docket 2025-05-15, 2026-07-22, 2026-08-14, 2026-09-25 | Verified |
| LIT-02 | Vantor will seek a permanent injunction against Gen-3 robot sales | Critical | High (that it is sought) | LIT-001 docket 2026-09-04 | Verified |
| LIT-03 | Vantor damages: $96.4M (plaintiff expert, through trial) to "not less than $140 million" (complaint), plus possible enhanced damages for willfulness; no contractual limit appears in the record; enhancement can reach three times actual damages (counsel to confirm) | Critical | High (party figures) | LIT-001 header, 2026-09-04 | Partially verified |
| LIT-04 | Stated amounts in open matters total $101.0M to $155.2M (8.7% to 13.4% of equity value), before enhancement, injunction effects and the securities case | Critical | Medium | LIT-001 to LIT-004; deal brief | Verified |
| LIT-05 | Court dates cluster around the IC and exclusivity (Nov 5 to Nov 20, 2026); depending on the closing timeline (not in the deal brief), the Vantor trial (Mar 8, 2027) could fall between signing and closing | High | High | docket index; LIT-001 to LIT-004 | Partially verified |
| LIT-06 | Securities class action: institutional lead plaintiff appointed; names CEO and former CFO; amended complaint due Nov 9, 2026 | High | High | LIT-003 | Verified |
| LIT-07 | Securities complaint alleges improper 2025 bill-and-hold revenue, including sales the customer did not request (untested allegation) | High | Low | LIT-003 allegations | Verified |
| LIT-08 | The deal model's March 2026 basis predates every adverse 2026 legal development | High | High | deal brief; LIT-001, LIT-003, LIT-004 | Verified |
| LIT-09 | Pinecrest seeks $12.0M vs a contractual cap of about $1.4M; argues gross negligence; hearing Nov 5, 2026 | Medium | High | LIT-004 | Verified |
| LIT-10 | Court events since mid-2026 must be tested against Talonfield's SEC disclosures | Medium | High | LIT-001, LIT-003, LIT-004 | Open |
| LIT-11 | Ruiz wage-and-hour settlement of $3.2M; final approval hearing Nov 13, 2026 | Low | High | LIT-002 | Open |
| (low relevance) | LIT-005 Delmarco (closed, $0.4M) and REG-001 OSHA (closed, $48 thousand): reviewed, Low | Low | High | docket index | Open |

### Financial analyst (full cards: `analyst-reports/iteration-1_financial-analyst.md`)

| ID | Finding | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|
| FIN-01 | Deal model's FY2026E case is stale: at $24.00 the offer is 15.1x LTM Adj EBITDA, not 11.5x; at a constant 11.46x on LTM, value is $17.27 per share | Critical | High (math) | deal brief; IS; recon; BS | Verified |
| FIN-02 | FY2025 growth relied on one abnormal quarter: Q4 2025 grew 32.4% (13% to 14% in other quarters) and included $31.8M of bill-and-hold; without it, FY2025 grew 11.6% and Q4 5.1%; reported revenue fell 29.0% sequentially in Q1 2026 | High | High (math) / Medium (trend) | revenue_quarterly; IS | Partially verified |
| FIN-03 | DSO rose from 63.5 to 86.4 days; contract assets up 142%; allowance cut from 3.8% to 2.1% of gross AR; about $31.5M of excess AR | High | High | BS; IS | Verified |
| FIN-04 | Operating cash flow fell from 78% to 15% of EBITDA; free cash flow has been negative for the last 12 months (LTM -$26.4M; -$10.1M in FY2025 and -$13.0M in H1 2026) | High | High | CF; recon | Partially verified |
| FIN-05 | Add-backs were 35% of FY2025 Adj EBITDA and 65% in H1 2026; restructuring every year; diligence-adjusted LTM EBITDA $72.6M vs $89.7M reported | High | High (math) / Medium (judgment) | recon; IS; kpis | Verified |
| FIN-06 | Norvale was 31.1% of reported FY2025 revenue (28.0% excluding its Q4 2025 bill-and-hold); top 10 customers 61.5% | High | High | revenue_by_customer | Partially verified |
| FIN-07 | Net debt $193.6M is 2.2x Adj EBITDA but 4.0x EBITDA before add-backs; cash down four periods; revolver drawn $45.0M of $75.0M ($25.8M available after letters of credit); covenant headroom in FIN-17 | High | High (ratios) / Medium (runway) | BS; recon; CF | Partially verified |
| FIN-08 | KPIs have turned: retention 118% to 111%, net new ARR halved, backlog down 22% in FY2025 and 30% from peak, book-to-bill below 0.9x | Medium | High (KPIs) / Medium (orders) | kpis; IS | Open |
| FIN-09 | ARR is not converting to software revenue at the historical rate (1.03x to 0.94x); $2.3M of Q2 2026 outage credits explain part of the gap | Medium | Medium | kpis; IS | Partially verified |
| FIN-10 | H1 2026 gross margin fell from 40.8% to 38.0% despite a richer mix; opex up 11.6% while revenue fell | Medium | High | IS; kpis | Open |
| FIN-11 | Inventory up 17.8% in H1 2026 to $84.0M while hardware revenue fell 12.9% | Medium | High (build) / Medium (write-down risk) | BS; IS; kpis; CF | Open |
| FIN-12 | Add-back labels show an auditor change, CFO turnover and a cyber incident in the same period as the revenue anomalies | Medium | High (events) / Low (meaning) | recon | Open |
| FIN-13 | Buybacks and share-settlement taxes ($68.7M, FY2023 to FY2025) exceeded free cash flow ($30.7M); FY2025 buybacks funded by the revolver | Medium | High | CF; IS | Open |
| FIN-14 | Equity bridge incomplete: 48.3M diluted shares come from a loss period (likely understated); debt-like items missing | Medium | Medium | IS; CF; deal brief | Open |
| FIN-15 | Revenue per robot fell about 12% in FY2025 ($79.4 thousand to $70.1 thousand) | Medium | Medium | kpis; IS | Open |
| FIN-16 | Goodwill plus intangibles ($132.5M) exceed equity ($92.0M); Lumora goodwill ($57.4M) exposed | Low | High (balances) / Low (impairment) | BS; CF | Open |

### News and media analyst (full cards: `analyst-reports/iteration-1_news-media-analyst.md`)

| ID | Finding | Claim type | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| NEWS-01 | Guidance cut on Aug 7, 2026 to $470M to $490M revenue and $70M to $78M Adj EBITDA; the deal model still uses the March case | Fact | Critical | High | news 2026-08-07, 2026-03-10; deal brief | Verified |
| NEWS-02 | Short seller Greyfin alleges Q4 2025 bill-and-hold sales were used to hit 2025 targets: "hundreds" of robots still in the warehouse in Feb 2026, customer did not ask, bonus target would have been missed | Allegation | Critical | Medium (existence) / Low (scale, motive) | news 2026-05-12 | Verified |
| NEWS-03 | Company confirmed a $9.4M credit for robots returned after a late-2025 bill-and-hold sale, three months after denying the short report | Fact | High | High | news 2026-08-07 | Verified |
| NEWS-04 | Record Q4 2025 beat consensus by about $26.4M, with an analyst flagging a jump in receivables and operating cash flow under $10M | Fact (analyst unnamed) | High | Medium | news 2026-03-10 | Verified |
| NEWS-05 | Auditor replaced after flagging a material weakness and warning of expanded Q4 work; the replacement audits fewer than ten listed companies and gave an adverse opinion | Fact | High | High | news 2025-11-18, 2026-03-10 | Verified |
| NEWS-06 | Two anonymous sources say the CFO left after tension with the CEO over booking Q4 2025 orders; the 8-K says the resignation was "not the result of any disagreement with the Company" and shows a $900,000 payment | Rumor (clash) / Fact (filing, payment) | High | Low (clash) / High (facts) | news 2026-01-23, 2026-08-07 | Partially verified |
| NEWS-07 | Norvale bought Kinetic Aisle to "reduce our dependence on any single vendor" and will pilot its own robots at 5 sites in 2027 | Fact | High | High | news 2026-06-24, 2026-08-20 | Verified |
| NEWS-08 | FieldOS outage stopped 40+ customer sites for up to 3 days; ransomware group claims data theft; no 8-K Item 1.05 filed as of Apr 14 | Fact / Rumor (data theft) | High | High (outage, filing status) / Low (theft) | news 2026-04-14, 2026-08-07 | Verified |
| NEWS-09 | Pinecrest's COO on record: forced to manual picking during its biggest promotion, "reviewing our options" | Fact | Medium | High | news 2026-04-14 | Open |
| NEWS-10 | Fourth restructuring since 2022 (about 60 jobs); costs excluded from Adj EBITDA every year | Fact | Medium | High | news 2026-07-30 | Open |
| NEWS-11 | Proposed LiDAR tariff increase from 7.5% to 25% (decision Q1 2027) hits Talonfield's single China supplier; 2 to 3 point hardware margin hit estimated | Fact / estimate | Medium | Medium | news 2026-09-15 | Open |
| NEWS-12 | The 34% premium is measured from a price already lifted 12% by the Oct 2 sale leak (pre-leak close about $15.36) | Rumor (process) / Fact (prices) | Medium | Medium | news 2026-10-02, 2026-05-12; deal brief | Verified |
| NEWS-13 | Market growing about 15% a year; Talonfield third with about 11% share; retailers building robots in-house | Fact (third-party research) | Low | Medium | news 2026-08-20 | Open |
| NEWS-14 | FieldOS 5 launched; software targeted at more than a third of revenue; new features need Gen-3 or newer robots | Fact (claims) | Low | Medium | news 2026-02-10 | Open |
| (no relevance) | Scholarship program article reviewed and set aside | Fact | n/a | High | news 2026-03-28 | Open |

## Iteration 2: follow-up findings

### SEC filings analyst, follow-ups F4 and F5 (full cards: `analyst-reports/iteration-2_sec-filings-analyst.md`)

| ID | Finding | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|
| SEC-19 | Exact Vantor wording: neither filing gives a damages amount; the 10-Q keeps "without merit" and "no accrual" but drops the 10-K's statement on whether a loss is probable or estimable | Medium | High (wording) | 10-K Items 1A and 3; 10-Q Part II Item 1 | Open |
| SEC-20 | The 10-Q (filed Aug 6, 2026) leaves out the Jul 22, 2026 claim construction order issued 15 days earlier, repeats "without merit", and calls the risk factors unchanged | High | High (excerpt) / Medium (full filing) | 10-Q Part II Items 1 and 1A; 10-K Item 3 | Verified |
| SEC-21 | Neither filing discloses the May 15, 2025 PTAB outcome (review of the '557 patent denied) | Medium | High (excerpt) | 10-K Item 3; 10-Q Part II Item 1 | Open |
| SEC-22 | No filing covers the Aug to Sep 2026 Vantor events, and neither discloses the complaint's demand of not less than $140M or the willfulness claim; Gen-3 is about $211.0M (42.0%) of FY2025 revenue; $96.4M equals $2.00 per share and 2.8x June cash ($140M equals $2.90) | High | High | 10-K Items 1 and 7; 10-Q; deal brief | Partially verified |
| SEC-23 | No 8-K of any kind about the April 2026 incident; the 10-Q, 117 days later, is the first filing to mention it | Medium | High (this filing set) | 8-Ks; 10-Q | Open |
| SEC-24 | The 10-Q says nothing about the ransomware group's data theft claim, and its cyber risk factor still describes as hypothetical what had already happened | High | High (what is said) / Low (the claim itself) | 10-Q; 10-K Item 1A | Verified |
| SEC-25 | The 10-Q never names Norvale, says nothing about its in-house robot plans, and leaves the concentration risk factor unchanged | High | High (excerpt) | 10-Q; 10-K Items 1, 1A, Note 2 | Verified |
| SEC-26 | Pattern: "no material changes" to risk factors despite four relevant developments, while the same officers certify that disclosure controls were not effective | Medium | Medium | 10-Q header, Part I Item 4, Part II Item 1A | Open |

### Financial analyst, follow-ups F1 to F3 (full cards: `analyst-reports/iteration-2_financial-analyst.md`)

| ID | Finding | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|
| FIN-17 | The reported 2.26x leaves out the credit agreement's 15% add-back cap; on the Note 9 definition the Jun 30, 2026 ratio is 2.65x, and the cushion against 3.00x is only 8.9 of covenant EBITDA (11.6%) | High | Medium | recon LTM; BS Q2 2026; 10-K Note 9; 10-Q | Verified |
| FIN-18 | On revised guidance and the Note 9 definition, the Dec 31, 2026 ratio is 3.05x to 3.55x against a 3.00x maximum if H2 add-backs repeat H1; on the company's uncapped basis it passes (2.56x to 2.86x) | High | Medium | recon; IS; CF; BS; 10-Q outlook | Partially verified |
| FIN-19 | As a sensitivity without bill-and-hold, FY2025 growth is 11.6% (hardware 2.9%) and Q4 2025 growth 5.1%; on a delivery basis H1 2026 grew 12.3% and LTM revenue ($498.4M) is unchanged | High | High (math) | revenue_quarterly; IS; 10-K Note 2; 10-Q | Partially verified |
| FIN-20 | Without its $24.6M of bill-and-hold, Norvale grew 11.4% (not 32.3%) and its share is flat at 28.0%; bill-and-hold explains all of the rise in concentration | High | High (math) | revenue_by_customer; 10-K Note 2 | Verified |
| FIN-21 | Bill-and-hold was probably decisive for the 142% bonus: without it, revenue clears the threshold by $0.5M and Adjusted EBITDA misses its threshold at any gross margin above 34.0% (reported margins 38% to 41%) | High | Medium | IS; recon; DEF 14A; 10-K Note 2 | Verified |
| FIN-22 | Pinecrest (customer #4, $17.4M in FY2025) claims $12.0M, 69.0% of a year's revenue from it | Medium | High (math) | revenue_by_customer; LIT-004 | Verified |
| FIN-23 | At the deal model's own 11.46x, value is $12.60 to $14.50 per share on revised guidance and $13.22 on diligence-adjusted LTM EBITDA ($72.6M; $14.19 if Vantor defense costs are one-off); treating Vantor as debt-like removes another $2.00 to $2.90 per share | Critical | High (math) / Medium (bases) | deal brief; BS; recon; 10-Q | Partially verified |

## Iteration 1: cross-source findings (lead agent)

| ID | Cross-source finding | Severity | Confidence | Built from | Status |
|---|---|---|---|---|---|
| X-01 | Reported growth was flattered by Q4 2025 bill-and-hold revenue ($31.8M, 20.6% of Q4). As a sensitivity excluding it, FY2025 growth is 11.6% (not 19.1%) and Q4 growth 5.1%; $22.4M of it was delivered in H1 2026 and $9.4M was returned and credited, so on a delivery basis LTM revenue ($498.4M) is unaffected | High | High | SEC-03, SEC-04, FIN-02, FIN-08, FIN-19, NEWS-03, NEWS-04 | Verified |
| X-02 | Filed disclosures lag the facts: the Aug 6, 2026 10-Q says the Vantor case "is in discovery" (with the trial date and "without merit") but does not mention the adverse Jul 22 claim construction order; neither filing excerpt mentions the PTAB outcome; the 10-Q excerpt does not mention the ransomware group's unverified data claim or Norvale's in-house robot plans; risk factors are called unchanged; and the certifying officers say disclosure controls are not effective | High | High (limited to the excerpts) | LIT-01, LIT-10, SEC-08, SEC-20, SEC-21, SEC-24, SEC-25, SEC-26, NEWS-07, NEWS-08 | Partially verified |
| X-03 | The Vantor patent case is a Critical exposure: adverse ruling, $96.4M to $140M+ claimed, an injunction sought on robots behind about 42% of FY2025 revenue, no accrual, trial likely before or around closing | Critical | High | LIT-01 to LIT-05, SEC-08, SEC-22 | Verified |
| X-04 | Norvale is both the biggest growth driver and the biggest risk: 31.1% of revenue, can terminate after a change of control, underlying growth about 11% once its bill-and-hold is removed, returned $9.4M of product in 2026, and is now building its own robots | Critical | High | SEC-02, SEC-04, SEC-25, FIN-06, FIN-20, NEWS-07 | Verified |
| X-05 | The valuation rests on a withdrawn forecast: the deal model uses the March 2026 case that the Aug 6, 2026 10-Q replaced. At $24.00 the offer is 15.1x LTM Adjusted EBITDA ($89.7M) and 17.3x to 19.3x revised guidance, not 11.5x; on diligence-adjusted LTM EBITDA of $72.6M (89.7 less restructuring 9.7, implementation delays 3.3 and Vantor defense costs 4.1; recon LTM column) it is 18.6x. At the model's own 11.46x the shares are worth $12.60 to $14.50 | Critical | High | SEC-01, FIN-01, FIN-05, FIN-23, NEWS-01, LIT-08 | Partially verified |
| X-06 | Earnings are converting poorly into cash: net receivables +62.0% vs revenue +19.1%, DSO 63.5 to 86.4 days, allowance cut from 3.8% to 2.1% of gross receivables, contract assets +142% (balance_sheet.csv); free cash flow negative for the last 12 months (LTM -$26.4M; cash_flow.csv); add-backs 35.1% of FY2025 and 65.2% of H1 2026 Adjusted EBITDA including stock-based compensation (17.7% and 35.5% without it) | High | High | FIN-03, FIN-04, FIN-05, SEC-10, NEWS-04, NEWS-10 | Verified |
| X-07 | A control and governance pattern around Q4 2025: the auditor was dismissed in Q4 2025 after flagging a material weakness and saying arrangements with these terms would need extra Q4 procedures; $31.8M of bill-and-hold was booked that quarter; without it, revenue would have cleared the bonus threshold by only $0.5M and missed target by $19.5M (bonuses paid at 142%); the CFO left with a $900,000 payment while the 8-K says his resignation was "not the result of any disagreement with the Company"; a short seller and a securities suit allege improper bill-and-hold | High | Medium (pattern) / High (each fact) | SEC-05, SEC-06, SEC-07, SEC-11, LIT-06, LIT-07, FIN-12, FIN-21, NEWS-02, NEWS-05, NEWS-06 | Verified |
| X-08 | Covenant headroom is overstated on the 10-K Note 9 definition (a summary): with the 15% add-back cap, Jun 30, 2026 leverage is 2.65x, not the reported 2.26x (2.67x if other income is deducted; 3.62x if stock-based compensation sits inside the cap); on revised guidance it reaches 3.05x to 3.55x at Dec 31, 2026 against a 3.00x maximum, while the company's uncapped basis passes (2.56x to 2.86x); a change of control is an event of default ($227.5M plus $4.2M of letters of credit) | High | Medium (depends on the full credit agreement) | SEC-09, FIN-07, FIN-17, FIN-18 | Verified |
| X-09 | The April 2026 cyber incident was judged "not material" and no Item 1.05 8-K was filed, yet robots at at least 40 customer sites stopped for up to three days, credits and response costs total $4.1M, a ransomware group claimed (unverified) to have taken data, and Pinecrest (customer #4, $17.4M) sued for $12.0M against a cap Talonfield estimates at about $1.4M | High | High (facts) / Medium (materiality view) | SEC-14, SEC-23, SEC-24, LIT-09, FIN-22, NEWS-08, NEWS-09 | Verified |
| X-10 | The litigation and covenant calendar collides with the deal timeline: Pinecrest hearing Nov 5, IC Nov 6, amended securities complaint Nov 9, PTAB decision on the '812 patent only in November, exclusivity and expert discovery end Nov 20, Vantor mediation in December, trial Mar 8, 2027 | High | High | LIT-05, SEC-09 | Verified |
| X-11 | Change-of-control costs and conflicts: $28.6M of estimated executive payments ($17.6M single-trigger equity; $9.6M double-trigger cash severance), an option for the CEO's family landlord to reset headquarters rent, no lead independent director, and a CEO who is a named defendant | Medium | High | SEC-12, SEC-13, LIT-06 | Verified |
| X-12 | Single-source LiDAR supplier in China meets a proposed tariff increase to 25%, with 12 to 18 months to qualify a second source | Medium | Medium | SEC-15, NEWS-11 | Verified |
| X-13 | Goodwill impairment risk: $98.4M last tested Oct 1, 2025, before the share price fell about 44% from its high and guidance was cut | Low | Medium | SEC-17, FIN-16, NEWS timeline | Open |
| X-14 | The headline premium flatters the offer: $17.85 includes the sale-leak bounce, and $24.00 is above the value implied by the model's own multiple on current earnings | Medium | Medium | NEWS-12, FIN-01 | Verified |
| X-15 | Positive: the strategic asset is real. FieldOS ARR $139.2M (+27% in FY2025), software 25.6% of revenue, top-3 position in a market growing about 15% a year; but retention fell from 118% to 111% and ARR growth slowed in H1 2026 | Positive | High | FIN key metrics, FIN-08, NEWS-13, 10-K Item 7 | Open |


## Verification (Step 4)

61 findings checked by four citation-verifier runs in parallel (all 52 Critical and High findings plus 9 Medium findings: SEC-11, SEC-13, FIN-09, FIN-22, LIT-09, NEWS-12, X-11, X-12, X-14; X-13 (Low) and X-15 (positive) were not sent): **44 verified, 17 partially verified, 0 not supported**. Full results: `verification/batch-1_sec-filings.md`, `batch-2_financial.md`, `batch-3_litigation-news.md`, `batch-4_cross-source.md`.

| Batch | Checked | Verified | Partially verified | Not supported |
|---|---|---|---|---|
| 1. SEC filings | 15 | 11 | 4 | 0 |
| 2. Financial | 15 | 7 | 8 | 0 |
| 3. Litigation and news | 18 | 15 | 3 | 0 |
| 4. Cross-source | 13 | 11 | 2 | 0 |
| **Total** | **61** | **44** | **17** | **0** |

Corrections applied (wording and precision; no finding was rejected):

- Bill-and-hold: present the ex-bill-and-hold figures as a sensitivity. $22.4M was delivered in H1 2026, so on a delivery basis LTM revenue is unaffected (FIN-19, FIN-23, X-01).
- Free cash flow has been negative for the last 12 months, not 18 (FIN-04, X-06).
- Diligence-adjusted LTM EBITDA is $72.6M (FIN-05); $76.7M is the sensitivity that treats Vantor defense costs as one-off (FIN-23, X-05).
- The covenant breach case depends on the 15% cap applying as summarized in 10-K Note 9 (FIN-17, FIN-18, SEC-09, X-08).
- Bonus: without bill-and-hold, revenue clears the threshold by $0.5M and misses target by $19.5M; the EBITDA miss is possible, not shown (SEC-11, FIN-21, X-07).
- The CFO 8-K says the resignation was "not the result of any disagreement with the Company"; it does not deny that a disagreement existed (NEWS-06, X-07).
- No source gives a closing timeline, so the Vantor trial "could" fall between signing and closing (LIT-05).
- No contractual cap on Vantor damages appears in the record; enhanced damages can reach three times actual damages, counsel to confirm (LIT-03).
- The securities suit's alleged corrective disclosures are in the file set: the Nov 14, 2025 8-K and the May 12, 2026 short seller report (SEC-07).
- Severity notes: FIN-06 and NEWS-07 are consolidated into X-04 (Critical); SEC-08 and LIT-01 to LIT-04 into X-03 (Critical), counted once among the red flags.
