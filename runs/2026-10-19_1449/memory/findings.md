# Findings register

Verification complete (2026-10-19): 97 checked, 68 Verified, 29 Partially verified (rows rewritten with the verifier's wording), 0 Rejected; 3 Low findings not verified. Verifier reports: `analyst-reports/verify_*.md`.

Target: kestrel (Corvane Diagnostics). Never delete a finding; change its status. Full cards are in the linked analyst reports. Severity and confidence are as reported by the analyst unless a later note says otherwise.

Report links: [SEC i1](analyst-reports/iteration-1_sec-filings-analyst.md), [NEWS i1](analyst-reports/iteration-1_news-media-analyst.md), [LIT i1](analyst-reports/iteration-1_litigation-analyst.md), [FIN i1](analyst-reports/iteration-1_financial-analyst.md).

## SEC filings (iteration 1)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| SEC-01 | Q4 2025 change in estimate (implicit price concessions) added US$14.2m to FY2025 revenue and operating income; Adj. EBITDA excl. it is 111.1; growth 8.0% not 11.7% | SEC | Critical | High | 10-K Item 7 change in estimate; Item 9A; 10-Q results ([SEC i1](analyst-reports/iteration-1_sec-filings-analyst.md)) | Verified |
| SEC-02 | FY2026 Adj. EBITDA guidance cut Aug 5, 2026 to 100-106 (from 134-140), below the 110.0 financing condition; excludes 2027 0419U rate | SEC | Critical | High | 8-K 2026-08-05 Item 7.01; 10-Q | Verified |
| SEC-03 | Covenant max net leverage steps down from 4.50x to 4.00x at Sep 30, 2026; headroom never disclosed; 15% add-back cap | SEC | High | Medium | 10-K Item 7 financial covenant; 10-Q liquidity | Verified |
| SEC-04 | DOJ CID received Feb 11, 2026; 10-K filed Mar 5, 2026 does not mention it and says not aware of material investigation | SEC | High | High | 10-Q Part II Item 1; 10-K Item 3, Note 15 | Verified |
| SEC-05 | CMS set new 2027 rate for 0419U (OncoTrace) Jul 29, 2026; 10-Q does not quantify; about 40% of non-Medicare OncoTrace revenue priced off Medicare | SEC | High | High | 10-Q Reimbursement; 10-K Clinical testing, Payer contracts | Verified |
| SEC-06 | Material weakness and adverse ICFR opinion (Brannock & Lyle) on the collection-rate estimate; not remediated at Jun 30, 2026; completion still expected within 2026, now stated as by year end; reserve 21.3 to 31.3 | SEC | High | High | 10-K Item 9A, Note 2; 10-Q Part I Item 4 | Partially verified |
| SEC-07 | Apr 27 8-K (Item 8.01) called ransomware a "network disruption", "no evidence at this time" of exfiltration, no material impact expected; 10-Q later: ransomware, about 412,300 notified Jun 2026, response costs 6.1, estimated lost revenue about 4.0, 10.0 policy limit, class actions, OCR inquiry | SEC | High | High | 8-K 2026-04-27 Item 8.01; 10-Q Cybersecurity incident | Partially verified |
| SEC-08 | Goodwill test Oct 1, 2025: Clinical unit (241.5) 14% headroom; assumptions since broken; share price down 34.9% to Jul 31 | SEC | High | Medium | 10-K Critical accounting estimates: goodwill; 10-Q; deal brief | Verified |
| SEC-09 | Orvia Health Plan (11.3% of revenue) may terminate on 60 days' notice on change of control | SEC | High | High | 10-K Payer contracts | Verified |
| SEC-10 | Veltrane (11.7% of revenue, #2 at 50.5) work orders terminable for convenience on 90 days' notice, paying only for work performed; mostly ATLAS-3; VLT-220 backlog 61.0 of 231.4 (26.4%); total Veltrane backlog not disclosed | SEC | High | High | 10-K Biopharma services; 10-Q Biopharma services | Partially verified |
| SEC-11 | Biopharma backlog fell 246.0 to 231.4 in H1 2026; book-to-bill 0.7 | SEC | Medium | High | 10-Q Biopharma services; 8-K 2026-08-05 | Verified |
| SEC-12 | Gap between operating income and Adj. EBITDA widened by 18.7 in H1 2026; only 6.1 explained | SEC | High | Medium | 10-Q results; Cybersecurity incident | Verified |
| SEC-13 | CCO Daniel Pruitt left Jan 2026, before the CID; 10-K still describes CCO oversight; first disclosed in the filings provided in the proxy (Apr 10); Q1 2026 10-Q not in the folder; news reported the exit Jan 15 | SEC | Medium | High | DEF 14A Executive officers; 10-K Compliance program; 10-Q Item 1A | Partially verified |
| SEC-14 | CEO change-of-control benefits 41.6 (single-trigger equity 31.4, 280G gross-up 3.5); all executives 56.4 | SEC | Medium | High | DEF 14A Change-in-control arrangements | Verified |
| SEC-15 | FY2025 bonus paid at 150%; Committee did not adjust for the 14.2 one-off (excl. it, 111.1 vs 118.0 target) | SEC | Medium | High | DEF 14A FY2025 annual bonus; 10-K Item 7 | Verified |
| SEC-16 | CEO-owned HQ lease extended to 2040 at 4.8 vs appraised 3.6 market rent (+33.3%) | SEC | Medium | High | DEF 14A Related transactions; 10-K Note 12 | Verified |
| SEC-17 | Genaro patent suit seeks injunction on OncoTrace method; no accrual; wording unchanged 10-K to 10-Q | SEC | High | Medium | 10-K Item 3; 10-Q Part II Item 1 | Verified |
| SEC-18 | Pell Ridge acquired May 2025 (31.0) but goodwill "added after" Oct 1 test date; acquisition in FY2025 growth | SEC | Medium | Medium | 10-K Item 1 Overview; goodwill estimate | Verified |
| SEC-19 | Initial denial rate rose 13.4% to 16.2%; two commercial payers added prior authorization | SEC | Medium | High | 10-Q results | Verified |
| SEC-20 | Change of control is an event of default under existing credit agreement; cured by repayment at closing | SEC | Low | High | 10-K, 10-Q Liquidity | Verified |

## News and media (iteration 1)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| NEWS-01 | FY2026 Adj. EBITDA guidance cut to 100-106 (from 134-140), below the 110.0 LTM financing condition (deal brief); the condition is tested on LTM at closing (Q2 2027), so it is at risk (inference); guidance excludes the 0419U cut | News | Critical | High | news/2026-08-06_capital-street-wire_guidance-cut.md ([NEWS i1](analyst-reports/iteration-1_news-media-analyst.md)) | Partially verified |
| NEWS-02 | Premium stale: US$24.00 is 83.2% over unaffected Oct 2 close of US$13.10 (92.8% over US$12.45) | News | High | High | news/2026-10-05 take-private talks; 2026-08-06 guidance cut | Verified |
| NEWS-03 | CMS 2027 rate for 0419U cut from US$2,150 to US$1,505 (-30.0%) from Jan 1, 2027 | News | High | High | news/2026-07-30 CMS lab fee schedule; 2026-08-06 | Verified |
| NEWS-04 | CFO declined to give leverage figure for Sep 30 tighter covenant test | News | High | Medium | news/2026-08-06 guidance cut | Verified |
| NEWS-05 | Veltrane halted ATLAS-3 for futility Aug 27, 2026; sites close by Q1 2027; winding down vendor contracts | News | High | High | news/2026-08-27 Veltrane halts ATLAS-3 | Verified |
| NEWS-06 | Compliance cluster: CCO exit (fact, confirmed by DEF 14A), CCO concerns (rumor), DOJ CID (rumor at the time, since confirmed Feb 11 by 10-Q and court record), Bearhaven kickback claims (allegation). Corvane denied Bearhaven's claims, declined to comment on the CCO, did not respond on the DOJ report | News | High | Low | news/2026-01-15; 2026-02-20; 2026-05-19 | Partially verified |
| NEWS-07 | Q4 2025 record revenue 120.5; CFO cited unquantified "refinement of our collection estimates" | News | High | Medium | news/2026-03-06; 2026-05-19 | Verified |
| NEWS-08 | Ransomware from Apr 18; attacker claimed 1.1 TB incl. patient test results on Apr 21 (unverified) | News | High | Medium | news/2026-04-22 ransomware attack | Verified |
| NEWS-09 | Durham lab start-up costs reported outside Adj. EBITDA, as for earlier openings | News | Medium | Medium | news/2025-11-06 Durham lab opening | Verified |
| NEWS-10 | Share price US$27.80 a year ago to US$13.10 on Oct 2, 2026 (-52.9%) | News | Medium | High | news 2026-03-06, 05-19, 08-06, 10-05 | Verified |
| NEWS-11 | 25% reagent tariff from Oct 1, 2026; analysts estimate reagents are 15-25% of test cost; Helixor contract fixes prices incl. duties through 2028 (company statement; 10-K agrees) | News | Medium | Medium | news/2026-09-17 reagent tariffs | Partially verified |

## Litigation (iteration 1)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| LIT-01 | US intervened Aug 18, 2026 in Whitcomb FCA qui tam (Counts I and II, OncoTrace Medicare claims); complaint-in-intervention due Oct 30, 2026 | Litigation | Critical | High (dates); Low (amount) | litigation/LIT-001 docket 2026-08-18, 2026-08-21; docket_index.csv ([LIT i1](analyst-reports/iteration-1_litigation-analyst.md)) | Verified |
| LIT-02 | FCA exposure: Count I (medical necessity) alleges about 41,200 claims, single damages 96.4 (relator's estimate), trebled 289.2 before per-claim penalties; Count II kickback damages not quantified (3.2 speaker fees to 61 physicians). Supporting ID under LIT-01 | Litigation | Critical | Low | litigation/LIT-001 complaint summary | Partially verified |
| LIT-03 | CID served Feb 11, 2026 (court record); qui tam under seal Mar 18, 2024 to Aug 21, 2026 | Litigation | High | High | litigation/LIT-001 docket 2026-03-02 | Verified |
| LIT-04 | Genaro: PTAB denied institution of Corvane's IPR petition (Dec 15, 2025); Aug 12, 2026 order adopted Genaro's construction of both disputed terms; Genaro's damages expert claims 9% royalty, 68.0 past damages through Jun 30, 2026, plus ongoing royalty or permanent injunction (plaintiff's claim); trial Feb 8, 2027 | Litigation | High | High (rulings); Low (amount) | litigation/LIT-002 docket | Partially verified |
| LIT-05 | OncoTrace v3 redesign launch expected mid-2027 subject to NY approval, after the trial (injunction gap) | Litigation | High | High | litigation/LIT-002 docket 2026-10-02 | Verified |
| LIT-06 | Class plaintiffs allege forensic firm found exfiltration Apr 24, 2026, three days before the Apr 27 8-K said "no evidence" (allegation) | Litigation | High | Low | litigation/LIT-003 consolidated complaint | Verified |
| LIT-07 | Seven breach cases consolidated Aug 14, 2026; motion to dismiss due Nov 30, 2026 | Litigation | Medium | High | litigation/LIT-003 docket | Verified |
| LIT-08 | HHS OCR HIPAA compliance review opened Jul 8, 2026; response due Oct 30, 2026 | Litigation | Medium | High | docket_index.csv LIT-005 | Verified |
| LIT-09 | Deal brief assumption "no material litigation beyond the 10-K" is out of date | Litigation | High | Medium | docket_index.csv; LIT-001 to LIT-003 | Verified |

Low-relevance matters noted by the litigation analyst (no separate ID): Hollis v. Corvane (LIT-004 file) dismissed with prejudice, no payment; NC DEQ notice (docket index LIT-006) penalty US$0.18m. Recorded in the appendix as Low.

## Financial analysis (iteration 1)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| FIN-01 | Four add-back categories recur every year; diligence-adjusted EBITDA 101.2 (FY2025) and 93.5 (LTM Q2 2026) vs 125.3 / 123.4 | Financial | Critical | High (math); Medium (judgment) | financials/adjusted_ebitda_reconciliation.csv ([FIN i1](analyst-reports/iteration-1_financial-analyst.md)) | Verified |
| FIN-02 | At US$24.00 the deal pays 16.3x FY2025 and 17.6x LTM diligence-adjusted EBITDA; 13.2x on LTM adjusted implies about US$16.00/share | Financial | Critical | Medium | deal-brief; adjusted_ebitda_reconciliation.csv; balance_sheet.csv | Verified |
| FIN-03 | Q4 2025 revenue 120.5 (+19.4% YoY) includes the 14.2 disclosed one-off (10-K Item 7); 9M 2025 growth 8.9%; Q1 2026 +1.3%, Q2 2026 -3.0%; labs 5 to 7 via Pell Ridge acquisition (31.0) and the Durham build | Financial | High | Medium | revenue_quarterly.csv; kpis.csv | Partially verified |
| FIN-04 | H1 2026 broad deterioration: revenue -0.9%, gross margin 43.0% to 38.0%, EBITDA -49.7%, backlog, ARR, headcount down | Financial | High | High | income_statement.csv; kpis.csv | Verified |
| FIN-05 | Model's FY2026 137.0 needs H2 2026 up 19.6% on H2 2025 | Financial | High | High | adjusted_ebitda_reconciliation.csv | Verified |
| FIN-06 | LTM Adj. EBITDA 123.4 is 13.4 above the 110.0 floor; excl. the disclosed 14.2 it is 109.2; H1 run-rate projection gives 108.2 at closing. Supporting ID under FIN-22 | Financial | High | Medium | adjusted_ebitda_reconciliation.csv | Partially verified |
| FIN-07 | Term loan B of 750.0 is 7.4x to 8.0x diligence-adjusted EBITDA, not 6.0x | Financial | High | High | adjusted_ebitda_reconciliation.csv; balance_sheet.csv | Verified |
| FIN-08 | Veltrane is #2 customer (50.5, 11.7%); 51.2% of biopharma; biopharma excl. Veltrane fell 7.1% | Financial | High | High | revenue_by_customer.csv row 2; income_statement.csv; kpis.csv | Verified |
| FIN-09 | Denial rate 8.9% to 16.2%; DSO 62.7 to 79.0 days; net AR +40.7% vs revenue +11.7% in FY2025 | Financial | High | High (ratios) | balance_sheet.csv; kpis.csv | Verified |
| FIN-10 | LTM OCF only 18.2% of Adj. EBITDA; LTM FCF -8.2; revolver 0 to 35.0 drawn on a 100.0 facility (65.0 undrawn at Jun 30, 2026; 10-K, 10-Q); FY2025 helped by 18.5 sale-leaseback proceeds | Financial | High | High | cash_flow.csv; balance_sheet.csv | Partially verified |
| FIN-11 | Net debt 391.0 is Dec 31, 2025; repayment 424.7 is Jun 30, 2026 debt; Jun 30 net debt 395.9; debt-like items unquantified | Financial | Medium | High (reconciliation) | balance_sheet.csv; cash_flow.csv | Verified |
| FIN-12 | Medicare #1 payer (104.3, 24.2%); Medicare-paid hereditary cancer panel about 76.2 (17.7% of revenue) | Financial | Medium | High | revenue_by_customer.csv; kpis.csv | Verified |
| FIN-13 | FY2025 includes the Pell Ridge acquisition (31.0, one lab, goodwill 22.3; revenue undisclosed) and a 6.8 sale-leaseback gain (in other income, excluded from EBITDA); the second new lab is the Durham build | Financial | Medium | High | cash_flow.csv; balance_sheet.csv; income_statement.csv | Partially verified |
| FIN-14 | Lab informatics ARR -2.3%, retention 95% | Financial | Low | High | kpis.csv | Not verified (Low) |
| FIN-15 | Goodwill and intangibles 401.1 vs equity 102.0; 10-K gives the Oct 1, 2025 test (US$27.80, 14% Clinical headroom) whose assumptions have since failed. Severity raised to Medium; parent is X-09 | Financial | Medium | Low | balance_sheet.csv | Partially verified |

## Iteration 2 findings

Report links: [SEC i2](analyst-reports/iteration-2_sec-filings-analyst.md), [LIT i2](analyst-reports/iteration-2_litigation-analyst.md), [FIN i2](analyst-reports/iteration-2_financial-analyst.md).

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| SEC-21 | 10-K omits the Dec 15, 2025 IPR denial; 10-K and 10-Q call Genaro claims "without merit"; no filing covers Markman loss | SEC | High | High | 10-K Item 3, Note 15; 10-Q Part II Item 1 ([SEC i2](analyst-reports/iteration-2_sec-filings-analyst.md)) | Verified |
| SEC-22 | 10-K said no material government investigation 22 days after the CID; in the filings provided the CID is first disclosed in the 10-Q of Aug 5, 2026 (175 days); no filing names Whitcomb | SEC | High | High | 10-K Item 3, 1A; 10-Q Part II Item 1 | Partially verified |
| SEC-23 | 10-K describes compliance program overseen by a CCO who had left; calls speaker program AKS-compliant after the CID targeted it | SEC | Medium | High | 10-K Compliance program; DEF 14A; 10-Q Item 1A | Verified |
| SEC-24 | 10-K Item 1: about 40% of non-Medicare OncoTrace revenue priced off the 0419U Medicare rate; 10-Q gives no amount; with the -30.0% news rate and the 55% Medicare share (kpis.csv), about 30.3 a year (inference, full flow-through), 24.3% of EV at 13.2x; lower bound 16.6 (13.3% of EV) | SEC | Critical | Medium | 10-K Payer contracts, 1A; 10-Q Reimbursement; 8-K Item 7.01 | Partially verified |
| SEC-25 | Cyber 8-K filed under Item 8.01 (whether Item 1.05 was required is an inference); no amendment in the filings provided; response costs 6.1 plus estimated lost revenue about 4.0 = 10.1, about equal to the 10.0 policy limit, before litigation and OCR outcomes | SEC | High | High | 8-K 2026-04-27; 10-Q Cybersecurity incident | Partially verified |
| SEC-26 | Revolver US$100.0m, US$65.0m available at Jun 30, 2026; lenders may stop revolving loans after a default | SEC | High | High | 10-K, 10-Q Liquidity | Verified |
| SEC-27 | 10-K states the US$27.80 share price at the Oct 1, 2025 goodwill test (14% headroom); 10-Q silent on impairment | SEC | High | High | 10-K goodwill estimate; 10-Q | Verified |
| SEC-28 | Filings do not name the two payers that added prior authorization (Orvia not named) or disclose speaker spend | SEC | Medium | High | 10-Q results; 10-K Payer contracts | Verified |
| SEC-29 | No filing discloses the ATLAS-3 halt; 10-Q still counts 61.0 of VLT-220 backlog; backlog ex-VLT-220 170.4 | SEC | High | High | 10-Q, 10-K Biopharma services | Verified |
| SEC-30 | On Corvane's definition LTM Adj. EBITDA at Jun 30, 2026 is 123.4 (meets 110.0 today); excl. the 14.2 it is 109.2 (inference); the 14.2 leaves LTM after Q4 2026; FY2026 guidance 100-106 implies the condition would not be met (projection); 85.2 of TLB rests on the one-off | SEC | Critical | High | 10-K Results, Financial covenant; 10-Q; 8-K Item 7.01 | Partially verified |
| SEC-31 | Bonus scale threshold 110.0 / target 118.0 / max 129.0 paid 150% on 125.3; no special committee disclosed in filings | SEC | Medium | High | DEF 14A FY2025 annual bonus | Verified |
| LIT-10 | Relator Dana Whitcomb, Regional Sales Director (Southeast) 2017-2023, alleges (Count III) she was demoted and then terminated in 2023 after raising concerns; government declined Count III; Pruitt not mentioned in the litigation records | Litigation | Medium | High (role) | LIT-001 complaint summary; docket 2026-08-18 ([LIT i2](analyst-reports/iteration-2_litigation-analyst.md)) | Partially verified |
| LIT-11 | Complaint speaker fees: 3.2 to 61 physicians over 2019-2025, about US$7,500 per physician per year vs Bearhaven's US$40,000 | Litigation | Medium | Medium | LIT-001 Count II | Verified |
| LIT-12 | Genaro: 9% royalty on 138.5 = 12.5 a year; with 68.0 past damages and capitalized royalty, 232.5 (14.1% of EV) (projection) | Litigation | High | Medium | LIT-002 docket 2026-09-25, 2026-10-02 | Verified |
| LIT-13 | Genaro seeks a permanent injunction; no preliminary injunction motion; trial Feb 8, 2027 before closing | Litigation | High | High | LIT-002 Claims; docket | Verified |
| LIT-14 | Breach plaintiffs' alleged timeline: Apr 24 forensic findings, Apr 27 8-K "no evidence", Jun 12 notices; no MFA (allegation) | Litigation | High | Low | LIT-003 consolidated complaint | Verified |
| LIT-15 | No securities, derivative or SEC matter in the litigation records | Litigation | Low | High | docket_index.csv | Not verified (Low) |
| LIT-16 | No docket entry mentions Veltrane, Orvia, recoupment or payer audits | Litigation | Low | High | litigation folder | Verified |
| LIT-17 | Government status report Mar 2, 2026 called the investigation "active", 3 days before the 10-K | Litigation | High | High | LIT-001 docket 2026-03-02 | Verified |
| LIT-18 | Table of court events after the last filing (Markman, intervention, unsealing, damages report) to check against disclosure | Litigation | Medium | High | docket_index.csv; LIT-001 to LIT-003 | Verified |
| FIN-16 | Covenant Consolidated EBITDA at Jun 30, 2026 = 90.2; net leverage 4.39x vs 4.50x (cushion 2.2); 5.36x excl. the 14.2 | Financial | High | High (math) | income_statement.csv; adjusted_ebitda_reconciliation.csv; cash_flow.csv; balance_sheet.csv ([FIN i2](analyst-reports/iteration-2_financial-analyst.md)) | Verified |
| FIN-17 | Projected Consolidated Net Leverage at Sep 30, 2026 is 4.48x to 5.01x in all three cases tested, above the 4.00x limit (projection); Dec 31, 2026 5.64x-7.72x; breach is an event of default and lenders may stop revolver draws (10-K) | Financial | Critical | Medium | same, plus revenue_quarterly.csv | Partially verified |
| FIN-18 | 0419U cut removes 29.0-30.3 a year of revenue and EBITDA; 383.0-400.0 at 13.2x = 23.2%-24.3% of EV (projection, 100% flow-through, no volume or mix change); 40% linkage cited from 10-K Item 1 Payer contracts | Financial | Critical | Medium | kpis.csv; income_statement.csv | Partially verified |
| FIN-19 | Excl. the 14.2: FY2025 111.1, LTM 109.2 (an indicator below 110.0, not a failure of the closing condition, which is projected in FIN-22); 13.2x implies US$19.95-20.43 a share; one-off worth 187.4 (11.4% of EV) | Financial | Critical | High | adjusted_ebitda_reconciliation.csv; balance_sheet.csv | Partially verified |
| FIN-20 | One-off is 11.8% of Q4 2025 revenue; FY2025 growth 8.0% excl. it | Financial | Medium | High | revenue_quarterly.csv | Verified |
| FIN-21 | Veltrane 50.5 revenue at risk; 13.4-14.7 EBITDA at average margin (projection); 11.8% of EV only if fully lost | Financial | High | Medium | revenue_by_customer.csv; income_statement.csv; kpis.csv | Verified |
| FIN-22 | Projected LTM Adj. EBITDA at Jun 30, 2027 about 83.0 (78.2-91.5) vs 110.0 (projection) | Financial | Critical | Medium | adjusted_ebitda_reconciliation.csv; FIN-18; FIN-21 | Verified |
| FIN-23 | Revolver draws 0 to 35.0 fund negative FCF; facility 100.0, maturing Oct 2028, 65.0 undrawn at Jun 30, 2026 (10-K, 10-Q); lenders may stop revolving loans after a default (10-K) | Financial | Medium | High | balance_sheet.csv; cash_flow.csv | Partially verified |
| FIN-24 | Covenant-basis leverage was 4.90x at FY2023, above today's limit; covenant history unclear | Financial | Low | Medium | income_statement.csv; balance_sheet.csv | Verified |

## Cross-source findings (X-)

Each X- finding passed the self-check: no absolute or predictive words unless quoted; ranks, dates and counts from cited sources; numbers recomputed; inferences and projections labeled; severity set by its own combined evidence. Supporting findings keep their own severity.

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| X-01 | Earnings quality: FY2025 Adj. EBITDA of 125.3 includes a 14.2 Q4 one-off and 24.1 of add-backs that appear in each period FY2022 to H1 2026. Excl. the one-off: 111.1 (FY2025), 109.2 (LTM). Excl. both: 87.0 (FY2025), 79.3 (LTM). At 13.2x, 79.3 implies US$12.42 a share | Cross-source | Critical | Medium | Parent. Supporting: SEC-01, SEC-06, SEC-12, SEC-18, SEC-19, SEC-30, NEWS-07, NEWS-09, FIN-01, FIN-02, FIN-03, FIN-04, FIN-09, FIN-13, FIN-19, FIN-20 | Verified |
| X-02 | Financing condition: FY2026 guidance (100-106) is below the 110.0 LTM condition; guidance excludes the 0419U cut and predates the Veltrane halt; projected LTM at Jun 30, 2027 about 83.0 (78.2-91.5) | Cross-source | Critical | Medium | Parent. Supporting: SEC-02, NEWS-01, FIN-05, FIN-06, FIN-22 | Verified |
| X-03 | Covenant default before signing (projection): Jun 30 leverage 4.39x passes 4.50x only with the 14.2 one-off; Sep 30 limit 4.00x needs 99.0 of Consolidated EBITDA vs projected 79.0-88.4; certificate due about Nov 14, 2026 | Cross-source | Critical | Medium | Parent. Supporting: SEC-03, SEC-20, SEC-26, NEWS-04, FIN-16, FIN-17, FIN-23, FIN-24 | Verified |
| X-04 | 2027 Medicare cut for OncoTrace (0419U, -30.0%) plus 40% Medicare-linked commercial pricing: 29.0-30.3 a year (projection), 23.2%-24.3% of EV; not in the model, the Aug 5 guidance or the goodwill test | Cross-source | Critical | Medium | Parent. Supporting: NEWS-03, SEC-05, SEC-24, FIN-12, FIN-18 | Verified |
| X-05 | FCA exposure: US intervened (Aug 18, 2026) on Medicare OncoTrace claims; relator alleges 96.4 single damages, 289.2 trebled (allegation, 17.5% of EV) plus per-claim penalties; exclusion risk named in 10-K; Medicare is the #1 payer (104.3). Bearhaven's US$40,000 a year vs about US$7,500 a year derived from the complaint (inference; may not cover the same physicians or years) | Cross-source | Critical | Medium | Parent. Supporting: LIT-01, LIT-02, LIT-10, LIT-11, NEWS-06 | Partially verified |
| X-06 | Disclosure reliability: 10-K omitted the Feb 11 CID, the Dec 15 IPR denial and the CCO's January exit; Apr 27 8-K said "no evidence" of exfiltration 6 days after the attacker's public claim; the folder has no filing after Aug 5, 2026, so disclosure of the Markman order and intervention is an open question | Cross-source | High | High | Parent. Supporting: SEC-04, SEC-13, SEC-21, SEC-22, SEC-23, SEC-25, LIT-03, LIT-06, LIT-14, LIT-17, LIT-18, NEWS-08 | Partially verified |
| X-07 | Genaro patent case against OncoTrace (32.1% of revenue): IPR denied, Markman lost, permanent injunction sought, trial Feb 8, 2027 before closing; redesign only mid-2027 subject to NY approval; claimed 68.0 plus 9% royalty (12.5 a year) | Cross-source | High | Medium | Parent. Supporting: SEC-17, LIT-04, LIT-05, LIT-12, LIT-13 | Verified |
| X-08 | Veltrane: #2 customer (50.5, 11.7%), VLT-220 backlog 61.0 (26.4%), 90-day termination for convenience; ATLAS-3 halted Aug 27, 2026, after the Aug 5 filings; Veltrane did not name Corvane and no termination notice is in the sources; backlog would be 170.4 if VLT-220 is fully lost (inference) vs 246.0 in the thesis | Cross-source | High | High | Parent. Supporting: SEC-10, SEC-11, SEC-29, NEWS-05, FIN-08, FIN-21 | Partially verified |
| X-09 | Dated judgments and stale price: goodwill test Oct 1, 2025 at US$27.80 with 14% headroom on stable Medicare and 9% growth; share price US$13.10 on Oct 2, 2026 (-52.9%); US$24.00 is an 83.2% premium to the unaffected price | Cross-source | High | High | Parent. Supporting: SEC-08, SEC-27, NEWS-02, NEWS-10, FIN-15 | Verified |
| X-10 | Orvia Health Plan (#3, 48.7, 11.3%) may terminate on 60 days' notice on change of control; whether it is one of the two prior-authorization payers is not stated | Cross-source | High | High | Parent. Supporting: SEC-09, SEC-28 | Verified |
| X-11 | Cyber incident exposure: response costs 6.1 plus estimated lost revenue about 4.0 = 10.1 vs a 10.0 policy limit (filings do not say whether lost revenue is covered); 412,300 notified; seven consolidated class actions; OCR review open (response due Oct 30, 2026) | Cross-source | High | Medium | Parent. Supporting: SEC-07, LIT-07, LIT-08 | Partially verified |
| X-12 | Financing package: the 750.0 term loan B is 6.87x LTM Adj. EBITDA excl. the one-off, 9.0x projected Jun 2027 LTM (projection); LTM FCF -8.2; OCF 18.2% of Adj. EBITDA | Cross-source | High | Medium | Parent. Supporting: FIN-07, FIN-10 | Verified |
| X-13 | Incentives and related parties: FY2025 bonus paid at 150% on EBITDA incl. the one-off (about 56.9% excl., inference); CEO is Chair and landlord at 1.2 a year above appraised rent to 2040; single-trigger equity and 280G gross-up, 56.4 for executives | Cross-source | Medium | High | Parent. Supporting: SEC-14, SEC-15, SEC-16, SEC-31 | Verified |
| X-14 | Deal brief base case: all six model assumptions are challenged by the sources, four by events after the Jun 30 model date (guidance cut, CMS rate, Veltrane halt, Aug 2026 court rulings and OCR review) and two by data the model did not reflect (the 14.2 one-off in the 10-K; H1 2026 revenue -0.9% vs 9% assumed growth) | Cross-source | High | High | Parent. Supporting: LIT-09. Draws on X-01, X-02, X-04, X-05, X-07, X-08 | Partially verified |
| X-15 | Equity bridge: Jun 30, 2026 net debt 395.9 vs 391.0 in the brief (+4.9); change-in-control benefits 56.4 (proxy), of which CEO cash items are 10.2; whether equity acceleration is already in the diluted shares and whether the 47.7 of fees covers cash items is not stated | Cross-source | Medium | Medium | Parent. Supporting: FIN-11, SEC-14, SEC-20 | Partially verified |
| X-16 | Named parties and look-alike entity: Genaro is not a listed customer; Corvane Laboratories Pty Ltd (FDA warning letter) is unaffiliated; Helixor is a supplier with duties borne by Helixor through 2028 (10-K and news agree) | Cross-source | Low | High | Supporting: NEWS-11, FIN payer list, LIT-16 | Not verified (Low) |

## Finding cards

Full cards for SEC-, NEWS-, LIT- and FIN- findings are in the linked analyst reports. X- finding cards are below.

### X-01: Earnings quality (Critical, Medium)
- **Combined evidence:** The 10-K discloses a Q4 2025 change in estimate that added 14.2 to revenue and operating income (SEC-01), 11.8% of Q4 2025 revenue of 120.5 (FIN-20). The CFO called it "a refinement of our collection estimates" without an amount (NEWS-07). The same estimate carries a material weakness and an adverse ICFR opinion (SEC-06). The estimate assumed better collections, but the denial rate rose from 10.7% (FY2024) to 13.4% (FY2025) and 16.2% (H1 2026) and DSO from 62.7 to 79.0 days (FIN-09, SEC-19). Four add-back categories (payer denial write-offs 10.6, billing transition 4.4, lab start-up 3.9, restructuring 5.2; total 24.1 in FY2025, 29.9 LTM) appear in each period FY2022 to H1 2026 (FIN-01); the company has said lab start-up costs are reported outside Adjusted EBITDA "as it has done for earlier lab openings" (NEWS-09). FY2025 growth also includes the Pell Ridge acquisition (SEC-18, FIN-13), revenue not disclosed.
- **Numbers (recomputed):** FY2025: 125.3 - 14.2 = 111.1; 111.1 - 24.1 = 87.0. LTM Q2 2026: 123.4 - 14.2 = 109.2; 109.2 - 29.9 = 79.3. Growth excl. one-off: 416.8 / 386.0 - 1 = 8.0% (vs 11.7%). EV / 79.3 = 20.8x. Price at 13.2x: (13.2 x 109.2 - 395.9) / 52.4 = US$19.95; (13.2 x 79.3 - 395.9) / 52.4 = US$12.42.
- **Severity test:** more than 10% of value. The one-off alone is 14.2 x 13.2 = 187.4, 11.4% of the 1,648.6 EV.
- **Confidence:** Medium. The one-off and the add-back history are primary data (High); treating the four add-backs as recurring is a judgment.

### X-02: Financing condition (Critical, Medium)
- **Combined evidence:** On Aug 5, 2026 Corvane cut FY2026 Adjusted EBITDA guidance from 134-140 to 100-106 (8-K; SEC-02; NEWS-01). The commitment letter needs LTM Adjusted EBITDA (Corvane definition) of at least 110.0 at closing (deal brief). The guidance "does not include any effect of the final 2027 Medicare rate for code 0419U" (8-K) and was issued before the Aug 27 Veltrane halt (news). The model uses 137.0, which needs H2 2026 up 19.6% on H2 2025 (FIN-05).
- **Numbers:** Guidance shortfall to 110.0 = 4.0 to 10.0. Projected LTM at Jun 30, 2027 (projection): H2 2026 48.9 (guidance midpoint less H1 54.1) plus H1 2027 34.1 (54.1 less 0419U 14.5 less Veltrane 5.5) = 83.0; range 78.2 to 91.5 (FIN-22).
- **Severity test:** block closing. Guided FY2026 Adjusted EBITDA of 100-106 is below the 110.0 condition.
- **Confidence:** Medium. Guidance is primary; the closing-date LTM is a projection.

### X-03: Covenant default before signing (Critical, Medium)
- **Combined evidence:** The 10-K covenant: Consolidated EBITDA = operating income + D&A + non-cash SBC + restructuring and other non-recurring cash costs, add-backs capped at 15%; maximum 4.50x through Jun 30, 2026, 4.00x from Sep 30, 2026; breach is an event of default; certificate due 45 days after quarter end (SEC-03). The 10-Q says only "in compliance" at Jun 30 (SEC-03). On the call the CFO declined to give a leverage figure for the end-September test (NEWS-04). After a default lenders "may stop further revolving loans" (SEC-26); cash was 28.8 and revolver availability 65.0 at Jun 30 (SEC-26), with LTM FCF of -8.2 (FIN-10).
- **Numbers:** Jun 30, 2026: base 41.5 + 26.6 + 10.3 = 78.4; cap 11.8; Consolidated EBITDA 90.2; 395.9 / 90.2 = 4.39x vs 4.50x. Excl. the 14.2: 5.36x (FIN-16). Sep 30, 2026 (projection): 4.48x to 5.01x vs 4.00x; 99.0 needed vs 79.0 to 88.4 (FIN-17).
- **Severity test:** default before signing. The Sep 30 certificate is due about Nov 14, 2026, before the mid-December 2026 signing, and the projected ratio exceeds 4.00x in each case tested. Under the calibration rule a default before signing is Critical.
- **Confidence:** Medium. The definition and debt are primary; the Sep 30 ratio is a projection, and which add-backs count as "cash costs" is an interpretation.

### X-04: 2027 Medicare cut for OncoTrace (Critical, Medium)
- **Combined evidence:** CMS final 2027 rate for 0419U falls from US$2,150 to US$1,505, -30.0%, from Jan 1, 2027 (NEWS-03). The 10-Q mentions "a new rate" without the amount (SEC-05). The 10-K says about 40% of non-Medicare OncoTrace revenue is priced off the 0419U Medicare rate (SEC-24). Medicare is the #1 payer (104.3, 24.2%) and Medicare-paid panel revenue was 76.2 in FY2025 (FIN-12). The deal model assumes flat Medicare rates through 2030 (deal brief). The Oct 1, 2025 goodwill test assumed "stable Medicare reimbursement for OncoTrace" (SEC-27).
- **Numbers (projection, 100% flow-through):** FY2025 mix: 76.2 x 30% + 62.3 x 40% x 30% = 22.9 + 7.5 = 30.3 a year. H1 2026 mix annualized: 29.0. At 13.2x: 383.0 to 400.4, 23.2% to 24.3% of EV (FIN-18). H1 2027 effect in the closing LTM: about 14.5.
- **Severity test:** more than 10% of value (23.2% to 24.3% of EV).
- **Confidence:** Medium. The rate is a published final rate (High); the revenue effect is a projection on KPI mix.

### X-05: False Claims Act exposure (Critical, Medium)
- **Combined evidence:** US ex rel. Whitcomb v. Corvane was filed under seal Mar 18, 2024; the US intervened in part on Aug 18, 2026 on Counts I (medical necessity) and II (kickbacks) for Medicare OncoTrace claims; complaint-in-intervention due Oct 30, 2026 (LIT-01). The relator, a former Regional Sales Director (Southeast) employed 2017 to 2023, alleges single damages of 96.4 on about 41,200 claims from 2019 to 2025 and 3.2 of speaker fees to 61 physicians (LIT-02, LIT-10). News reported a DOJ CID (rumor at the time) and Bearhaven alleged speaker-fee kickbacks (allegation) (NEWS-06). Bearhaven's US$40,000 a year per physician does not match the complaint's about US$7,500 a year (LIT-11; conflict recorded).
- **Numbers:** Treble: 96.4 x 3 = 289.2 (allegation), 17.5% of EV, before per-claim penalties (amount not in the records). Medicare revenue FY2025: 104.3 (#1 payer).
- **Severity test:** more than 10% of value: the trebled claim of 289.2 is 17.5% of EV. Exclusion from Medicare, named in the 10-K risk factors, could stop the deal.
- **Confidence:** Medium. The intervention and dates are court record (High); the damages are the relator's allegation (Low).

### X-06: Disclosure reliability (High, High)
- **Combined evidence:** CID served Feb 11, 2026 (10-Q; court status report); the government reported the investigation "active" on Mar 2 (LIT-17); the 10-K filed Mar 5 says Corvane is "not aware of any pending government investigation that we expect to be material" (SEC-04, SEC-22). First disclosure: 10-Q on Aug 5, 2026, 175 days after service. PTAB denied Corvane's IPR on Dec 15, 2025; the 10-K omits it and calls the claims "without merit" (SEC-21). The 10-K describes a compliance program "overseen by our Chief Compliance Officer", who had left in January 2026 (SEC-13, SEC-23). The Apr 27 8-K, filed under Item 8.01, said "no evidence at this time that patient information was exfiltrated" (SEC-25), 6 days after an attacker publicly claimed 1.1 TB including patient test results (NEWS-08, allegation) and 3 days after plaintiffs allege the forensic firm reported exfiltration (LIT-06, LIT-14, allegation). No filing in the folder covers the Aug 12 Markman order or the Aug 18 intervention (LIT-18; SEC-22).
- **Severity:** High. It needs specific representations, a disclosure-related indemnity and a bring-down litigation search. No single number meets the Critical test.
- **Confidence:** High for the dates and quotes; the Apr 24 forensic finding is an allegation.

### X-07: Genaro patent case against OncoTrace (High, Medium; lowered from Critical at verification)
- **Combined evidence:** Genaro alleges OncoTrace infringes U.S. Patent No. 11,604,318 and seeks a permanent injunction (SEC-17, LIT-13). PTAB denied Corvane's IPR (Dec 15, 2025) and the court adopted Genaro's claim construction (Aug 12, 2026) (LIT-04). Genaro's expert claims 68.0 past damages through Jun 30, 2026 and a 9% royalty (LIT-04). Jury trial Feb 8, 2027, before the Q2 2027 closing; Corvane's redesign (OncoTrace v3) is expected mid-2027 subject to New York State approval (LIT-05). OncoTrace revenue was 138.5 in FY2025, 32.1% of total (kpis.csv; SEC-21).
- **Numbers:** 9% x 138.5 = 12.5 a year. Claimed past damages 68.0 = 4.1% of EV. With a capitalized royalty at 13.2x (projection): 68.0 + 164.5 = 232.5, 14.1% of EV (LIT-12). With a one-year royalty to a mid-2027 v3 launch: 68.0 + 12.5 = 80.5, 4.9% of EV (projection).
- **Severity (after verification):** High. The only figure above 10% of EV (232.5, 14.1%) assumes a royalty paid indefinitely, which conflicts with the mid-2027 v3 date in the court record; with a one-year royalty the figure is 80.5 (4.9%). The injunction is sought, not granted. Escalate to Critical on an adverse verdict, an injunction, or a slip in v3 approval. The trial falls between signing and closing.
- **Confidence:** Medium. Rulings and dates are court record; damages are plaintiff's expert figures; injunction outcome unknown.

### X-08: Veltrane and the backlog (High, High)
- **Combined evidence:** Veltrane is the #2 customer, 50.5 in FY2025 (11.7%), 51.2% of biopharma services; biopharma excl. Veltrane fell 7.1% (FIN-08). Veltrane backlog is 61.0 of 231.4 (26.4%) and its work orders are terminable on 90 days' notice, "paying only for work performed" (SEC-10, SEC-29). Veltrane halted ATLAS-3 for futility on Aug 27, 2026 and will "wind down vendor contracts" (NEWS-05). No filing in the folder discloses the halt (SEC-29). H1 2026 book-to-bill was 0.7 (SEC-11).
- **Numbers:** Backlog ex-VLT-220: 231.4 - 61.0 = 170.4, -30.7% vs the 246.0 in the thesis. EBITDA at risk if fully lost (projection): 13.4 to 14.7, 194.0 at 13.2x (11.8% of EV). The 10% test is met only if 85% or more of Veltrane revenue is lost (FIN-21), which the data does not show.
- **Severity:** High. Rating it Critical would need the share of Veltrane revenue tied to ATLAS-3.
- **Confidence:** High for the facts; the revenue loss is inference.

### X-09: Dated judgments and stale price (High, High)
- **Combined evidence:** The 10-K goodwill test (Oct 1, 2025) showed about 14% headroom in Clinical testing (241.5 of goodwill), assumed stable OncoTrace Medicare rates and 9% growth, and states the share price was US$27.80 at the test date (SEC-27). Since then: 0419U -30.0% (X-04), H1 2026 clinical revenue -1.9%, guidance midpoint -24.8% (SEC-08), share price US$13.10 on Oct 2, 2026 (NEWS-10). The 10-Q is silent on an interim test. The deal brief premium of 32.6% uses the Jul 31 close of US$18.10, before the Aug 5 guidance cut (NEWS-02).
- **Numbers:** 13.10 / 27.80 - 1 = -52.9%. 24.00 / 13.10 - 1 = 83.2%. Market value at US$13.10: 52.4 x 13.10 = 686.4.
- **Severity:** High. The impairment is non-cash; whether it reduces covenant EBITDA depends on the credit agreement reading (inference).
- **Confidence:** High for the facts; impairment is inference.

### X-10: Orvia change-of-control right (High, High)
- **Combined evidence:** Orvia is the #3 payer at 48.7 (11.3%) (revenue_by_customer.csv) and may terminate on 60 days' notice if Corvane undergoes a change of control (10-K; SEC-09). The 10-Q says two commercial payers added prior authorization but does not name them (SEC-28). No litigation entry mentions Orvia (LIT-16).
- **Severity:** High. Needs an Orvia consent or waiver as a closing condition, or price protection.

### X-11: Cyber incident exposure (High, Medium)
- **Combined evidence:** Response costs 6.1 plus lost revenue about 4.0 against a 10.0 insurance limit; about 412,300 people notified Jun 2026; HHS OCR inquiry (SEC-07). Seven class actions consolidated Aug 14, 2026; motion to dismiss due Nov 30 (LIT-07). OCR compliance review opened Jul 8, response due Oct 30, 2026 (LIT-08). Plaintiffs allege no MFA on a remote-access account (LIT-14, allegation).
- **Numbers:** 6.1 + 4.0 = 10.1 > 10.0 limit before litigation or OCR outcomes. Class damages not stated.
- **Severity:** High. Needs a specific indemnity; amount not quantifiable.

### X-12: Financing package (High, Medium)
- **Combined evidence and numbers:** 750.0 / 109.2 = 6.87x LTM excl. the one-off; 750.0 / 79.3 = 9.5x on X-01's diligence view; 750.0 / 83.0 = 9.0x on projected Jun 2027 LTM (projection). LTM FCF -8.2; OCF / Adj. EBITDA 18.2% (FIN-10). FIN-07.
- **Severity:** High. The loan needs re-sizing or re-pricing; it is not a pre-closing default by itself.

### X-13: Incentives and related parties (Medium, High)
- **Combined evidence:** Bonus 100% on Adjusted EBITDA; threshold 110.0, target 118.0, max 129.0; paid 150% on 125.3; the Committee "did not adjust" for the change in estimate (SEC-15, SEC-31). The CEO is Board Chair and co-owns the HQ landlord; the lease was extended to 2040 at 4.8 vs an appraised 3.6 (SEC-16). CEO change-of-control benefits 41.6 incl. single-trigger equity 31.4 and a 280G gross-up 3.5; all executives 56.4 (SEC-14).
- **Numbers:** Excl. the one-off: 111.1, payout about 56.9% (inference, linear interpolation). Rent premium 1.2 a year (33.3%).

### X-14: Stale deal brief base case (High, High)
- Starting EBITDA 125.3 vs 109.2 LTM excl. one-off (X-01). FY2026 137.0 vs guidance 100-106 (X-02). Growth 9% a year vs H1 2026 -0.9% and Q2 2026 -3.0% (FIN-04, FIN-05). Medicare flat vs 0419U -30.0% (X-04). Backlog converts incl. Veltrane vs ATLAS-3 halted (X-08). No litigation beyond the 10-K vs FCA intervention, Markman loss, breach class actions and OCR review (LIT-09, X-05, X-07, X-11). Thesis point 1 (11.7% growth) is 8.0% excl. the one-off; thesis point 3 (growing backlog) is a 5.9% decline.

### X-15: Equity bridge (Medium, Medium)
- Jun 30, 2026 net debt 395.9 vs 391.0 used in the brief (+4.9) (FIN-11). Repayment 424.7 equals Jun 30 gross debt (SEC-20). Executive change-of-control payments 56.4 (SEC-14); whether the 47.7 of fees covers them is not stated. Sale-leaseback lease liability and other liabilities not broken out (FIN-11).

### X-16: Named parties and look-alike entity (Low, High)
- Payer ranks (revenue_by_customer.csv, FY2025): Medicare #1 (104.3), Veltrane #2 (50.5), Orvia #3 (48.7), Brightwater #4 (30.2). Genaro Biosciences is not a listed customer (not in the top 10). Corvane Laboratories Pty Ltd, subject of a Sep 3, 2026 FDA warning letter, is "not affiliated" per the article; excluded from findings (news analyst). Helixor is a supplier, not a listed customer; the 10-K says Helixor bears "all import duties and tariffs" through Dec 31, 2028, which corroborates the company statement in the Sep 17 article (NEWS-11). Bearhaven, Halvard, Whitcomb and Ellery Property Holdings are not listed customers.
