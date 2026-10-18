# Findings register

Status: Verification done (2026-10-18). 66 findings checked: 46 Verified, 20 Partially verified (rows rewritten with the verifier's corrected wording), 0 Rejected. Findings still Open were not sent for verification (Medium and Low) and are labeled "not verified" in the report. Never delete a finding; change its status.

Notes:
- Litigation finding IDs (LIT-01 to LIT-10) are a separate series from the court case IDs (case LIT-001 to LIT-005, REG-001).
- Full finding cards are in the linked analyst reports. Report files: [SEC it.1](analyst-reports/iteration-1_sec-filings-analyst.md), [NEWS it.1](analyst-reports/iteration-1_news-media-analyst.md), [LIT it.1](analyst-reports/iteration-1_litigation-analyst.md), [FIN it.1](analyst-reports/iteration-1_financial-analyst.md), [SEC it.2](analyst-reports/iteration-2_sec-filings-analyst.md), [FIN it.2](analyst-reports/iteration-2_financial-analyst.md).
- US$ millions unless stated.

## Cross-source findings (lead agent)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| X-01 | Q4 2025 revenue recognition cluster (a sequence of events, not a proven cause): $31.8 of Q4 2025 bill-and-hold revenue (20.6% of Q4; $24.6 with Norvale) sat in Talonfield warehouses at Dec 31, 2025. The outgoing auditor flagged a material weakness in Q3 2025, said Q4 arrangements "expected" with these terms would need more audit work, and was dismissed Nov 10, 2025 (the 8-K reports no disagreements and gives no reason). The CFO resigned Jan 20, 2026 with a $0.9 payment. The material weakness behind the adverse ICFR opinion was still unremediated at June 30, 2026. $9.4 was returned and credited in May 2026 ($22.4 delivered by June 30). FY2025 AR rose 62.0% and contract assets 142.2% against revenue +19.1%. A class action and a short seller allege improper recognition (allegations); the 10-K warehouse statement is consistent with, but does not confirm, Greyfin's claim about February 2026. | Cross-source | Critical | High (facts); allegations Low | SEC-02, SEC-04, SEC-05, SEC-06, SEC-19, SEC-25, FIN-01, FIN-04, FIN-17, LIT-05, NEWS-02, NEWS-03, NEWS-05, NEWS-14 | Partially verified |
| X-02 | The deal model is stale. Model v3 (Sept 2026) and the brief (Oct 17, 2026) use the March 2026 case ($560.0 revenue, $118.0 Adj. EBITDA), but guidance was cut on Aug 6, 2026 to $470.0-490.0 and $70.0-78.0. EV of $1,352.8 is 18.3x the $74.0 midpoint (17.3x-19.3x) and 15.1x LTM Adj. EBITDA of $89.7. It is 16.8x a diligence-normalized LTM Adj. EBITDA of about $80.5 (LTM less estimated gross profit on Q4 2025 bill-and-hold, plus that lost to the Q2 2026 credit, at a 41.1% margin; not a company figure). Illustratively, the model's 11.46x on the $74.0 midpoint gives $13.55 per share (not a fair value). | Cross-source | Critical | High | SEC-01, SEC-26, NEWS-01, FIN-02, FIN-21, deal-brief.md | Partially verified |
| X-03 | Reported FY2025 growth is overstated. Excluding bill-and-hold, FY2025 revenue was $470.5 (+11.6% vs reported +19.1%), Q4 2025 $122.6 (+5.1% vs +32.4%) and FY2025 hardware +2.9% (vs +15.1%). Bill-and-hold was 39.5% of FY2025 growth and 84.1% of Q4 growth. Adding back the $9.4 credit, H1 2026 was $232.0 (+2.4%); if the $22.4 delivered in H1 2026 is instead re-timed into 2026, H1 2026 growth would be about 12.3%. FY2025 Adj. EBITDA excluding bill-and-hold is about $85.7, assuming the FY2025 average gross margin of 41.1%. | Cross-source | Critical | High (recomputed from filing and financial data; EBITDA effect Medium) | SEC-02, SEC-19, FIN-01, FIN-15, FIN-16, FIN-18, revenue_quarterly.csv, 10-Q | Partially verified |
| X-04 | Business is weakening on every forward measure: H1 2026 revenue -1.7%, hardware -12.9%, gross margin 40.8% to 38.0%, reported EBITDA margin 11.6% to 4.7%, backlog 168.0 to 118.0 (-29.8% in 18 months), NRR 118% to 111%, LTM FCF -26.4, guidance midpoint -4.4% for FY2026. Market grows about 15% a year (single third-party estimate). Offsets: H1 2026 software +14.6%, services +14.4%, ARR $139.2 to $146.8. | Cross-source | Critical | High | FIN-01, FIN-05, FIN-08, FIN-09, SEC-01, NEWS-11 | Verified |
| X-05 | Norvale relationship is at risk on several fronts: 31.1% of FY2025 revenue ($156.2) and 38% of gross AR ($46.2); MSA lets Norvale terminate on 90 days' notice on a change of control, no minimum volume, expires Sept 30, 2027; Norvale returned $9.4 of bill-and-hold robots in May 2026; it was reported on June 24, 2026 to have bought Kinetic Aisle to "reduce our dependence on any single vendor" with a 2027 pilot. Underlying share was 28.0% and underlying growth 11.4% excluding its bill-and-hold. The Aug 6, 2026 10-Q excerpts, filed 43 days after the Kinetic Aisle deal, does not mention it and gives no updated Norvale share. | Cross-source | Critical | High | SEC-07, SEC-02, SEC-19, SEC-20, FIN-07, FIN-22, NEWS-06 | Verified |
| X-06 | Vantor patent case: the 10-Q filed Aug 6, 2026 gives the March 2027 trial date, says the claims are without merit and records no accrual, but does not mention the adverse July 22, 2026 Markman order (Vantor's construction adopted on 3 of 4 terms), the complaint's "not less than $140 million" demand, the injunction request or any loss estimate, and it drops the 10-K's "cannot reasonably estimate" sentence. Later events: Gen-3 Plus added Aug 14; Vantor's expert put royalty damages at $96.4 on Sept 4; stay denied Sept 25; mediation ordered Oct 5 for December 2026. Vantor-claimed damages of $96.4 to $140.0+ are 8.3% to 12.1% of equity value, plus possible enhanced damages for alleged willfulness. Vantor will seek an injunction (none granted) aimed at Gen-3, about 70% of hardware (about $211.0, 42.0% of FY2025 revenue). | Cross-source | Critical | High | SEC-10, SEC-18, LIT-01, LIT-02, LIT-03, LIT-09 | Partially verified |
| X-07 | April 2026 FieldOS incident is treated as "not material" despite 40+ sites down for up to 3 days, $2.3 credits, $1.8 response cost (added back to Adj. EBITDA), a $12.0 Pinecrest suit alleging an unpatched known vulnerability (gross negligence, to break a $1.4 cap; hearing Nov 5, 2026), and an unverified ransomware data-theft claim. No 8-K Item 1.05 as of April 14, 2026 per news, and none in data/. The 10-Q says only "some customers" were affected, and the 10-K excerpts (filed before the incident) have no Item 1C. | Cross-source | High | Medium | SEC-11, SEC-21, NEWS-07, LIT-07, LIT-08, FIN-12 | Verified |
| X-08 | Change of control triggers at closing: credit agreement event of default (repay about $227.5), Norvale termination right, single-trigger vesting of $17.6 executive equity (total package $28.6, of which $9.6 cash severance is double-trigger; proxy amounts assume a Dec 31, 2025 change of control), and the CEO-family landlord's right to reset HQ rent to "fair market value" by its own appraiser. | Cross-source | High | High | SEC-07, SEC-08, SEC-14, FIN-06 | Verified |
| X-09 | Covenant and liquidity (diligence estimates based on the 10-K's summary of the credit agreement). Max leverage steps down to 3.00x from Sept 30, 2026. Covenant net debt is about $202.5 (term loan $182.5 + revolver $45.0, cash netting capped at $25.0). The reported 2.26x equals 202.5 / LTM Adj. EBITDA 89.7, which is consistent with the 15% Permitted Add-back cap not being applied (LTM capped-type add-backs $23.7). Applying the cap gives about 2.6x-2.7x at June 30 if SBC is outside the cap, or about 3.65x (above the 3.50x maximum) if SBC is inside it. Assuming flat net debt and add-backs of $21.2 a year, FY2026 guidance implies a Dec 31, 2026 ratio of 2.60x-2.89x uncapped and about 3.0x-3.6x capped: at or above 3.00x, breach likely. The Sept 30 test is unreported. LTM FCF is -26.4, cash $33.9, revolver $25.8 available. | Cross-source | High | Medium (terms are a 10-K summary of the credit agreement; cap basis and SBC treatment ambiguous) | SEC-08, SEC-09, SEC-22, FIN-05, FIN-06, FIN-19, FIN-20 | Partially verified |
| X-10 | Governance and incentives: 2025 bonuses paid at 142% of target. Excluding bill-and-hold, revenue of $470.5 would have missed the $490.0 target and cleared the $470.0 threshold by only $0.5; on the X-03 estimate, Adj. EBITDA of about $85.7 would have missed its $88.0 threshold. This is consistent with, but does not prove, the short seller's allegation that the bonus target depended on these sales. Also: Chairman-CEO with 14.2% and no lead independent director, an HQ lease from the CEO's family entity, and an interim CFO who was the controller. | Cross-source | High | Medium (numbers high; motive is inference) | SEC-13, SEC-14, SEC-06, NEWS-03 | Partially verified |
| X-11 | Adjusted EBITDA quality: add-backs are 46.3% of LTM Adj. EBITDA ($41.5 of $89.7); restructuring is added back every year from FY2022 to H1 2026 (the July 2026 program is the fourth since 2022 per news). A diligence-adjusted LTM EBITDA of $72.6 (removing restructuring $9.7, Vantor litigation $4.1 and customer implementation delays $3.3; a diligence estimate, before any bill-and-hold normalization) gives EV / EBITDA of 18.6x. | Cross-source | High | High | FIN-03, NEWS-08 | Partially verified |
| X-12 | The 34% premium is measured against a price that may have been lifted by an Oct 2, 2026 press report citing unnamed sources about a sale process (+12% to $17.20; the company declined to comment). The implied prior close is about $15.36, so $24.00 is about 56% above it. That the Oct 16 price was lifted by the report is an inference. | Cross-source | Medium | Medium (price move reported; leak itself is an anonymous report) | NEWS-12, deal-brief.md | Verified |

## Analyst findings: SEC filings (iterations 1 and 2)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| SEC-01 | Aug 6, 2026 10-Q cut FY2026 outlook to revenue $470-490 and Adj. EBITDA $70-78; deal model still uses $560.0 / $118.0 | SEC | Critical | High | 10-Q "Updated 2026 outlook"; 10-K Item 7 | Verified |
| SEC-02 | $31.8 bill-and-hold in Q4 2025 (20.6% of Q4), $24.6 Norvale; $9.4 returned and credited May 2026 | SEC | Critical | High | 10-K Note 2; 10-Q "Bill-and-hold amendment" | Verified |
| SEC-03 | 10-K credited Q4 to "strong hardware deliveries"; 10-Q later says orders were "pulled forward" | SEC | High | High (wording) | 10-K Item 7; 10-Q "Revenue" | Verified |
| SEC-04 | Auditor dismissed Nov 10, 2025 after flagging a material weakness and wider Q4 procedures | SEC | High | High (facts) | 8-K 2025-11-14 Item 4.01; 10-K Item 9A | Verified |
| SEC-05 | Adverse ICFR opinion; material weakness unremediated and disclosure controls not effective at June 30, 2026 | SEC | High | High | 10-K Item 9A; 10-Q Part I Item 4 | Verified |
| SEC-06 | CFO resigned Jan 20, 2026 with $0.9 payment and release; interim CFO is the former controller; CFO named in class action | SEC | High | High (facts) | 8-K 2026-01-21 Item 5.02; 10-Q | Verified |
| SEC-07 | Norvale 31.1% of revenue, 38% of AR; change-of-control termination on 90 days' notice; no minimum volume; MSA ends Sept 30, 2027 | SEC | Critical | High | 10-K Item 1, Item 1A, Note 13 | Verified |
| SEC-08 | Change of control is an event of default; covenant steps down to 3.00x from Sept 30, 2026; $25.0 cash netting cap; 15% add-back cap | SEC | High | High (terms) | 10-K Note 9; 10-Q "Covenant compliance" | Verified |
| SEC-09 | OCF fell from $40.8 to $9.7 (2025) and -$4.2 (H1 2026); cash down, revolver up; allowance fell to 2.1% of AR | SEC | Medium | High | 10-K Item 7, Note 5; 10-Q Liquidity | Verified |
| SEC-10 | Vantor patent case threatens Gen-3 (about 42% of revenue); trial March 2027; no accrual; 10-Q drops "cannot reasonably estimate" | SEC | High | High | 10-K Item 3; 10-Q Part II Item 1 | Verified |
| SEC-11 | 10-Q discloses a securities class action (June 3, 2026) against the company, CEO and former CFO and a $12.0 Pinecrest breach-of-contract suit (June 17, 2026) over the April 11 incident; no accrual or loss range is disclosed for either; the incident is described as "not material" | SEC | High | High (facts) | 10-Q "April 2026 service disruption", Part II Item 1 | Partially verified |
| SEC-12 | 10-Q says "no material changes" to risk factors except one addition | SEC | Medium | Medium | 10-Q Part II Item 1A | Open |
| SEC-13 | 2025 bonuses paid at 142%; revenue ex bill-and-hold ($470.5) only just above $470.0 threshold (hypothetical; also below the $490.0 target) | SEC | Medium | High (numbers) | DEF 14A "2025 annual incentive plan"; 10-K Note 2 | Verified |
| SEC-14 | All unvested executive equity vests single-trigger on a change of control ($17.6); total estimated package $28.6 includes $9.6 of double-trigger cash severance (CEO $11.8); HQ and main assembly facility leased from Hale Family Properties LLC, which may reset rent to fair market value set by a landlord-selected appraiser on a change of control; Hale is Chairman and CEO with 14.2%; no lead independent director | SEC | Medium | High | DEF 14A sections | Partially verified |
| SEC-15 | 10-Q excerpts lack Norvale update, goodwill impairment discussion, ARR/NRR update, CFO search update | SEC | Medium | Medium | 10-Q (absence); 10-K Note 15 | Open |
| SEC-16 | Single-source LiDAR supplier in China, no qualified second source | SEC | Medium | High | 10-K Item 1 "Suppliers", Item 1A | Open |
| SEC-17 | Ruiz $3.2 settlement accrued; preliminary approval May 20, 2026 | SEC | Low | High | 10-K Item 3; 10-Q Part II Item 1 | Open |
| SEC-18 | The 10-Q filed Aug 6, 2026 describes Vantor only as in discovery with a March 2027 trial and no accrual; it does not mention the adverse July 22, 2026 Markman order, the complaint's "not less than $140 million" demand, the injunction request or any loss estimate, and drops the 10-K's "cannot reasonably estimate" sentence (the $96.4 damages report came later, Sept 4, 2026) | SEC | High | High | 10-K Item 3, Item 1A; 10-Q Part II Item 1, Item 1A | Partially verified |
| SEC-19 | Full 10-Q text of the May 2026 bill-and-hold amendment with the largest customer; $9.4 returned (implied 38.2% of Norvale's bill-and-hold); no reason given | SEC | High | High | 10-Q MD&A "Bill-and-hold amendment", "Revenue"; 10-K Note 2 | Verified |
| SEC-20 | 10-Q excerpts silent on Norvale's Kinetic Aisle deal (43 days earlier); no updated Norvale share or AR | SEC | High | High | 10-Q Item 1A and MD&A (absence); 10-K Item 1A, Note 13 | Verified |
| SEC-21 | Cyber: 10-Q says "some customers", up to three days, "not material"; no Item 1C in 10-K excerpts; $1.8 cost added back | SEC | Medium | High | 10-K Item 1A; 10-Q MD&A "April 2026 service disruption" | Open |
| SEC-22 | 10-K Note 9's summary of the credit agreement: term loan $185.0 and revolver $35.0 at Dec 31, 2025 ($75.0 commitment, both mature August 2029); net leverage = (Total Debt minus cash, netting capped at $25.0) / Consolidated EBITDA; Permitted Add-backs capped at 15% of pre-add-back Consolidated EBITDA; 3.50x stepping to 3.00x from Sept 30, 2026; CoC is an event of default. At June 30, 2026 revolver $45.0 drawn, $4.2 letters of credit, $25.8 available | SEC | High | High (terms) / Medium (headroom) | 10-K Note 9; 10-Q "Covenant compliance", "Liquidity" | Partially verified |
| SEC-23 | ARR and NRR undefined and dropped from the 10-Q; no KPI definitions | SEC | Medium | High | 10-K Item 1, Item 7; 10-Q (absence) | Open |
| SEC-24 | Lumora revenue undisclosed; Lumora is $57.4 of $98.4 goodwill; no interim impairment test after guidance cut | SEC | Medium | High | 10-K Item 1, Note 15; 10-Q (absence) | Open |
| SEC-25 | No financial statement audit opinion or critical audit matter in the 10-K excerpts | SEC | Medium | High | 10-K Item 9A; 8-K 2025-11-14 | Open |
| SEC-26 | Deal model out of date vs filed 10-Q guidance (restates SEC-01) (duplicate of SEC-01; count once) | SEC | Critical | High | 10-Q "Updated 2026 outlook" | Verified |

## Analyst findings: News and media (iteration 1)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| NEWS-01 | Guidance cut Aug 7, 2026 to $470-490 revenue and $70-78 Adj. EBITDA; model case stale | News | Critical | High | 2026-08-07 guidance-cut, para 1, 3; 2026-03-10 record-q4, para 2 | Verified |
| NEWS-02 | Bill-and-hold existed; $9.4 credit in Q2 2026 after a customer returned robots | News | Critical | High (credit) | 2026-08-07 guidance-cut, para 2 | Verified |
| NEWS-03 | Greyfin short seller allegations (allegation): robots still in warehouse, customer did not request bill-and-hold, bonus target | News | Critical | Low to Medium | 2026-05-12 short-seller-report | Verified |
| NEWS-04 | Auditor switch to small firm after material weakness and warning on Q4 deals | News | High | High | 2025-11-18 auditor-switch; 2026-03-10 record-q4, para 5 | Partially verified |
| NEWS-05 | Two unnamed sources say CFO Okafor clashed with CEO Hale over how to book large Q4 2025 hardware orders, and one said Okafor wanted recognition deferred until delivery in 2026 (rumor, unconfirmed); the filing says there was no disagreement; $900,000 separation payment | News | High | Low (clash) / High (payment) | 2026-01-23 cfo-exit | Partially verified |
| NEWS-06 | Norvale bought Kinetic Aisle to reduce vendor dependence; 2027 in-house pilot | News | High | Medium | 2026-06-24 norvale-buys-kinetic-aisle, para 2, 3 | Verified |
| NEWS-07 | April 2026 FieldOS incident stopped robots at at least 40 customer sites for up to three days; a ransomware group's data-theft claim is unverified; as of April 14, 2026 no Item 1.05 8-K had been filed and the company called the incident not material; it later issued $2.3 of service credits | News | High | Medium to High | 2026-04-14 fieldos-outage; 2026-08-07 guidance-cut, para 2 | Partially verified |
| NEWS-08 | Fourth restructuring since 2022, each excluded from Adj. EBITDA | News | Medium | Medium | 2026-07-30 layoffs | Verified |
| NEWS-09 | Receivables jumped and FY2025 OCF under $10.0 (unnamed analyst) | News | High | Medium (single unnamed analyst; figures consistent with financials) | 2026-03-10 record-q4, para 4 | Partially verified |
| NEWS-10 | Single-source China LiDAR; proposed tariff 7.5% to 25%; 2-3 pt margin hit (analyst estimate) | News | Medium | Medium | 2026-09-15 lidar-tariffs | Open |
| NEWS-11 | Market about +15% a year; Talonfield guiding revenue down (share loss inferred) | News | Medium | Medium | 2026-08-20 market-report | Open |
| NEWS-12 | Sale process leak Oct 2, 2026 (anonymous); Arbelion and two PE firms named; shares +12% | News | Medium | Low | 2026-10-02 sale-exploration | Open |
| NEWS-13 | FieldOS 5 needs Gen-3 or newer; software target is promotional | News | Low | Medium | 2026-02-10 fieldos-5-launch | Open |
| NEWS-14 | Six news items point to Q4 2025 hardware revenue recognition | News | Critical | Medium | Files 1, 2, 4, 7, 10 | Verified |

## Analyst findings: Litigation (iteration 1)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| LIT-01 | Vantor seeks a permanent injunction against Gen-3 sales; Gen-3 Plus added to infringement contentions Aug 14, 2026 (record does not say the injunction request covers it); trial March 8, 2027 | Litigation | Critical | Medium | LIT-001 file, entries 2026-08-14, 2026-09-04 | Verified |
| LIT-02 | Vantor damages: complaint "not less than $140 million" plus enhanced; Vantor's own expert figure $96.4 through trial (8.3% to 12.1% of equity value) | Litigation | Critical | Medium | LIT-001 file, header, entry 2026-09-04 | Verified |
| LIT-03 | Adverse rulings: Markman 3 of 4 terms for Vantor (July 22, 2026), stay denied (Sept 25), mediation ordered (Oct 5) | Litigation | High | Medium | LIT-001 file, entries 2025-05-15 to 2026-10-05 | Verified |
| LIT-04 | Key patent dates near deal timeline: expert discovery closes Nov 20, 2026 (exclusivity end), PTAB '812 decision Nov 2026, mediation Dec 2026 | Litigation | High | High | LIT-001 file, Upcoming dates; docket_index.csv | Verified |
| LIT-05 | Securities class action alleges improper 2025 bill-and-hold revenue (allegation); CEO and former CFO named | Litigation | High | Low (substance) / High (procedure) | LIT-003 file, Allegations, entries 2026-06-03, 2026-09-10 | Verified |
| LIT-06 | Consolidated amended complaint due Nov 9, 2026, after the IC | Litigation | Medium | High (dates) | LIT-003 file | Open |
| LIT-07 | Pinecrest claims $12.0; Talonfield says cap about $1.4; hearing Nov 5, 2026 | Litigation | High | Medium | LIT-004 file | Verified |
| LIT-08 | Outage allegedly caused by failure to patch a known vulnerability (allegation) | Litigation | Medium | Low | LIT-004 file, Key facts | Verified |
| LIT-09 | Court-record dates to compare with filings (disclosure check) | Litigation | High | High | All LIT files; docket_index.csv | Verified |
| LIT-10 | No change-of-control, anti-assignment or merger-injunction issues in litigation records | Litigation | Low | Medium | All LIT files | Open |

## Analyst findings: Financial analysis (iterations 1 and 2)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| FIN-01 | Q4 2025 revenue $154.4 (+32.4%) far above trend; Q1 2026 -29.0% QoQ; H1 2026 -1.7%, Q2 -4.0% | Financial | Critical | High | revenue_quarterly.csv; income_statement.csv | Verified |
| FIN-02 | Model case stale; EV $1,352.8 is 15.1x LTM Adj. EBITDA, 18.6x diligence-adjusted, 28.1x reported | Financial | Critical | High | deal-brief.md; balance_sheet.csv; adjusted_ebitda_reconciliation.csv | Verified |
| FIN-03 | Add-backs 46.3% of LTM Adj. EBITDA; recurring restructuring; diligence-adjusted LTM $72.6 | Financial | High | High (arithmetic) | adjusted_ebitda_reconciliation.csv | Verified |
| FIN-04 | AR +62.0%, contract assets +142.2% vs revenue +19.1%; DSO 63.5 to 86.4; allowance 3.8% to 2.1% | Financial | High | High | balance_sheet.csv; cash_flow.csv | Verified |
| FIN-05 | OCF/EBITDA 78.0% to 15.1%; LTM FCF -26.4; FY2025 buybacks $17.4 while drawing revolver | Financial | High | High | cash_flow.csv; adjusted_ebitda_reconciliation.csv | Verified |
| FIN-06 | Net debt $193.6; 2.16x LTM Adj. EBITDA, 4.02x reported; interest cover 3.2x LTM (not the covenant ratio) | Financial | High | High | balance_sheet.csv; adjusted_ebitda_reconciliation.csv; income_statement.csv | Verified |
| FIN-07 | Norvale 31.1% of FY2025 revenue, 47.3% of FY2025 growth; top 10 61.5% | Financial | High | High | revenue_by_customer.csv | Verified |
| FIN-08 | NRR 118% to 111%; backlog -22.0% then -9.9%; book-to-bill 0.88; revenue per robot -11.7% | Financial | High | High (trends) | kpis.csv; income_statement.csv | Verified |
| FIN-09 | H1 2026 gross margin 40.8% to 38.0%; reported EBITDA margin 4.7%; operating loss | Financial | High | High | income_statement.csv | Verified |
| FIN-10 | Inventory +17.8% in H1 2026 to $84.0; DIO 111.1 days | Financial | Medium | High (ratios) | balance_sheet.csv; cash_flow.csv | Verified |
| FIN-11 | Deferred revenue -11.8% in H1 2026 while ARR +5.5% | Financial | Medium | Medium | balance_sheet.csv; kpis.csv | Open |
| FIN-12 | Add-back detail shows auditor transition, CFO transition, cyber incident, rising Vantor costs | Financial | Medium | High (existence) | adjusted_ebitda_reconciliation.csv | Open |
| FIN-13 | Lumora Vision acquisition (FY2024, $85.0) contribution not disclosed; organic growth unknown | Financial | Medium | High (amounts) | cash_flow.csv; balance_sheet.csv | Open |
| FIN-14 | Installed base equals cumulative shipments, no retirements | Financial | Low | High | kpis.csv | Open |
| FIN-15 | Bill-and-hold is 39.5% of FY2025 growth and 84.1% of Q4 2025 growth; FY2025 hardware growth ex bill-and-hold 2.9% | Financial | Critical | High | revenue_quarterly.csv; income_statement.csv; 10-K Note 2 | Verified |
| FIN-16 | Adding back the $9.4 credit, Q2 2026 revenue would be $122.3 (+4.0%) and H1 2026 $232.0 (+2.4%), or $234.3 (+3.4%) also excluding $2.3 of SLA credits; assuming the credit was booked against hardware, H1 2026 hardware would be $126.3 (-5.9%) | Financial | High | High | revenue_quarterly.csv; income_statement.csv; 10-Q | Partially verified |
| FIN-17 | Installed base rolls forward exactly by shipments (no retirements shown); whether 2025 shipments of 4,300 include roughly 400 to 450 bill-and-hold robots still in Talonfield warehouses cannot be determined from the data and should be asked of management | Financial | Medium | Low | kpis.csv; income_statement.csv | Partially verified |
| FIN-18 | FY2025 Adj. EBITDA ex bill-and-hold about $85.7 (18.2%), not $98.8 (19.7%), at 41.1% gross margin | Financial | High | Medium | income_statement.csv; adjusted_ebitda_reconciliation.csv | Verified |
| FIN-19 | The reported 2.26x equals 202.5 / 89.7, consistent with the company using full Adj. EBITDA and not applying the 15% Permitted Add-back cap; applying the cap gives about 2.61x to 2.67x if SBC is outside the cap, or about 3.65x (above the 3.50x maximum) if SBC is inside it | Financial | High | Medium | balance_sheet.csv; adjusted_ebitda_reconciliation.csv; 10-K Note 9 | Partially verified |
| FIN-20 | Assuming covenant net debt stays at $202.5 and add-backs run at $21.2 a year, FY2026 guidance implies a Dec 31, 2026 ratio of 2.60x-2.89x without the cap and about 3.03x-3.61x with the cap (SBC outside it), which would exceed the 3.00x maximum that applies from Sept 30, 2026 | Financial | Critical | Medium | as FIN-19; revenue_quarterly.csv; cash_flow.csv | Partially verified |
| FIN-21 | On a conservative basis excluding all Q4 2025 bill-and-hold gross profit (including the $22.4 delivered by June 2026), LTM Adj. EBITDA is about $80.5, implying 16.8x EV; illustratively, at the model's 11.46x this supports about $15.10 per share (not a valuation) | Financial | Critical | High (arithmetic) / Medium (normalization) | adjusted_ebitda_reconciliation.csv; balance_sheet.csv; income_statement.csv; 10-K Note 2; 10-Q | Partially verified |
| FIN-22 | Norvale ex bill-and-hold grew 11.4% (not 32.3%); share 28.0% (not 31.1%) | Financial | High | High | revenue_by_customer.csv; 10-K Note 2 | Verified |
| FIN-23 | Returned bill-and-hold units about 43% of H1 2026 inventory build | Financial | Low | Medium | balance_sheet.csv; cash_flow.csv | Open |

## Finding cards

Analyst finding cards are in the linked analyst reports (unedited). X- finding cards follow.

### X-01: Q4 2025 revenue recognition cluster
- **Claim:** One issue sits behind many findings: Q4 2025 hardware revenue recognized under bill-and-hold. Sequence: Q3 2025 old auditor flags a material weakness on non-standard hardware contracts and says Q4 arrangements "expected" with these terms would need more audit work (8-K Item 4.01). Nov 10, 2025: auditor dismissed. Q4 2025: $31.8 of bill-and-hold revenue booked, $24.6 with Norvale, goods kept in Talonfield warehouses (10-K Note 2). Jan 20, 2026: CFO resigns with a $0.9 payment and release (8-K). Mar 2026: new auditor gives an adverse ICFR opinion. May 2026: $9.4 returned to inventory and credited (10-Q). June 3, 2026: class action alleges improper bill-and-hold (allegation). Financials show FY2025 AR +62.0% and contract assets +142.2% against revenue +19.1%.
- **Sources:** SEC-02, SEC-03, SEC-04, SEC-05, SEC-06, FIN-01, FIN-04, LIT-05, NEWS-02, NEWS-03, NEWS-05, NEWS-14.
- **Corroboration:** The short seller's core claim (allegation) that robots booked as sales were still in the warehouse matches the 10-K's own statement that the products "remained in our warehouses." The CFO-clash rumor matches the timing but stays a rumor.
- **Why it matters:** Restatement risk, inherited securities liability, and reliability of the revenue base used for price.

### X-02: Stale valuation basis
- **Claim:** Model v3 (Sept 2026) and the deal brief (Oct 17, 2026) still use the March 2026 investor day case, though the company withdrew it on Aug 6, 2026. EV = $1,159.2 equity + $193.6 net debt (June 30, 2026) = $1,352.8. EV / guidance midpoint $74.0 = 18.3x (17.3x at $78.0, 19.3x at $70.0). Holding the model's 11.46x on $74.0 gives EV $848.1, equity $654.5, $13.55 per share.
- **Sources:** SEC-01, NEWS-01, FIN-02, deal-brief.md.

### X-03: Underlying growth (one-off combined with quarterly data)
- **Claim:** Applying the 10-K's $31.8 bill-and-hold to the quarterly data and the 10-Q's $9.4 reversal to Q2 2026: FY2025 $470.5 (+11.6%), Q4 2025 $122.6 (+5.1%), hardware FY2025 $269.6 (+2.9%). Q2 2026 $122.3 (+4.0% vs $117.6), H1 2026 $232.0 (+2.4% vs $226.5), H1 2026 hardware $126.3 (-5.9% vs $134.2). The $22.4 of bill-and-hold robots delivered in 2026 bring no 2026 revenue, because it was booked in 2025.
- **Sources:** SEC-02, FIN-01, `data/financials/revenue_quarterly.csv`, `data/financials/income_statement.csv`, 10-K Note 2, 10-Q.

### X-04: Weakening trend
- **Claim:** Revenue, margins, backlog, retention and cash all weakening at once (see register row). Third-party market growth of about 15% a year suggests share loss (inference).
- **Sources:** FIN-01, FIN-05, FIN-08, FIN-09, SEC-01, NEWS-11.

### X-05: Norvale at risk
- **Claim:** See register row. The change-of-control right means this deal itself gives Norvale a free exit, three months after Norvale started building an in-house alternative.
- **Sources:** SEC-07, SEC-02, FIN-07, NEWS-06.

### X-06: Vantor disclosure gap and exposure
- **Claim:** See register row. Timing gap: the Markman order (July 22, 2026) predates the 10-Q (Aug 6, 2026). Confirmed by SEC-18 in iteration 2.
- **Sources:** SEC-10, LIT-01, LIT-02, LIT-03, LIT-09.

### X-07: Cyber incident
- **Sources:** SEC-11, NEWS-07, LIT-07, LIT-08, FIN-12.

### X-08: Change of control triggers
- **Sources:** SEC-07, SEC-08, SEC-14, FIN-06.

### X-09: Covenant and liquidity
- **Conflict resolved:** SEC analyst assumed a term loan of $185.0 (10-K balance); balance_sheet.csv shows $182.5 at June 30, 2026. Use $182.5. Covenant net debt 227.5 - 25.0 = 202.5; 202.5 / 2.26 = $89.6 implied covenant EBITDA, matching LTM Adj. EBITDA $89.7.
- **Sources:** SEC-08, SEC-09, FIN-05, FIN-06.

### X-10: Governance and incentives
- **Sources:** SEC-13, SEC-14, SEC-06, NEWS-03.

### X-11: Adjusted EBITDA quality
- **Sources:** FIN-03, NEWS-08.

### X-12: Premium on a disturbed price
- **Claim:** 17.20 / 1.12 = 15.36 implied prior close; 24.00 / 15.36 - 1 = 56.3%.
- **Sources:** NEWS-12, deal-brief.md.

### X-09 update after iteration 2
- Covenant text (10-K Note 9, via SEC-22): Consolidated EBITDA = net income + interest, taxes, D&A, + non-cash SBC, + restructuring, integration and other non-recurring charges ("Permitted Add-backs"); Permitted Add-backs may not exceed 15% of Consolidated EBITDA calculated before including them.
- Lead reading: SBC is listed before the defined term, so SBC is likely not capped. On that reading, June 30, 2026: base 48.2 + 17.8 = 66.0; capped 75.9; ratio 202.5 / 75.9 = 2.67x vs reported 2.26x. Dec 31, 2026 on guidance (non-recurring add-backs run-rate 21.2): 3.61x / 3.34x / 3.10x at $70 / 74 / 78 (pre-add-back cap basis); FIN-20 shows 3.53x / 3.26x / 3.03x on a final-EBITDA cap basis. Both breach 3.00x.
- Caveat: Note 9 says the definitions are "summarized from the credit agreement". The full agreement is not in the data.
