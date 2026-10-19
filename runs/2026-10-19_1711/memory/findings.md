# Findings register

Status: Verified (Step 4). 151 checked: 98 Verified, 53 Partially verified (rows rewritten with the verifier wording), 0 Rejected; 22 Low not verified. Iterations 1 and 2 registered (SEC 43, NEWS 27, LIT 14, FIN 69, X 20). Iteration 2 report: [FIN iteration 2](analyst-reports/iteration-2_financial-analyst.md). Never delete a finding; change its status.

Full cards: analyst findings link to their saved report (`analyst-reports/iteration-1_<analyst>.md`, heading `#### <ID>`). `X-` cards are below. "Parent" means the row is the single place a fact appears in the report; supporting IDs are listed in the parent's Source(s) cell.

Report links: [SEC](analyst-reports/iteration-1_sec-filings-analyst.md) | [NEWS](analyst-reports/iteration-1_news-media-analyst.md) | [LIT](analyst-reports/iteration-1_litigation-analyst.md) | [FIN](analyst-reports/iteration-1_financial-analyst.md)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| X-001 | Change of control forces pension funding on a termination basis within 120 days: shortfall US$230.5m (14.9% of EV); model has no pension adjustment | Cross-source | Critical | High | Parent. 10-K Note 11; Reno Gazette 2026-10-06. Supporting: SEC-001, SEC-002, NEWS-018, FIN-012, FIN-054 | Verified |
| X-002 | Nimbus earn-out amended May 12, 2026, two months into the sale process: US$90.0m payable on change of control vs US$8.0m carried (gap US$82.0m) | Cross-source | High | High | Parent. 8-K 2026-05-14; 10-Q Note 9; Proxy. Supporting: SEC-003, SEC-004, SEC-005, FIN-024, FIN-055 | Verified |
| X-003 | WSEA (rank 1, US$96.0m, 12.2% of revenue) awarded its 2027-2031 program to Thermiq on Jul 21, 2026; the 10-Q filed Aug 6 still says "we expect to be selected"; at the company average margin the loss is US$183.7m (11.9% of EV) (inference) | Cross-source | Critical | High | Parent. Utility Programs West 2026-07-22; 10-Q MD&A; revenue_by_customer.csv row 1. Supporting: NEWS-010, SEC-028, FIN-021, FIN-022, FIN-046, FIN-047 | Partially verified |
| X-004 | LTM Adjusted EBITDA about US$115.4m, not US$130.4m: Aura and Calder add-backs removed and warranty normalized (estimate on FY2025 accruals); just over the 10% test (11.5% of EV) | Cross-source | Critical | Medium | Parent. Supporting: FIN-001, FIN-002, FIN-003, FIN-004, SEC-015, SEC-041, NEWS-024 | Partially verified |
| X-005 | H1 2026 operating cash flow US$134.1m includes US$98.0m of timing (supplier terms 60 to 120 days, US$34.0m WSEA advance); underlying US$36.1m; cash and net debt overstated | Cross-source | High | High | Parent. 10-Q MD&A Liquidity; cash_flow.csv; balance_sheet.csv. Supporting: SEC-017, SEC-029, FIN-009, FIN-010, FIN-011, FIN-014, FIN-058, NEWS-014 | Verified |
| X-006 | Ensamble Norte (49% JV, main assembler): Delmora guarantees US$64.0m of its loan; Delmora's April terms stretch may have moved cash strain onto the JV (inference); JV reportedly missed an Aug 31 payment (rumor); lenders set a Sep 30 deadline | Cross-source | High | Medium | Parent. 10-K Note 14; 10-Q MD&A; Monterrey Economia 2026-09-15. Supporting: SEC-018, SEC-019, NEWS-013, NEWS-015, FIN-038, FIN-059, FIN-060 | Partially verified |
| X-007 | Export controls: BIS subpoena (June 24, 2026) and suspended shipments to the UAE distributor; Gulf Horizon (rank 4, US$38.6m) supplied 71.9% of FY2025 growth; alleged diversion to Iran (rumor); Audit Committee review predates the 10-K "not aware of any violations" | Cross-source | High | Medium | Parent. 10-Q Note 12; 10-K MD&A, Item 1A; Proxy; revenue_by_customer.csv row 5; Gulf Trade Monitor 2026-06-11. Supporting: SEC-024, SEC-025, NEWS-011, NEWS-012, FIN-020, FIN-049, FIN-050 | Verified |
| X-008 | Insights data rights contested: opt-out enrollment vs a 2022 FTC order requiring consent for sharing beyond disclosed purposes; records re-identified; Colorado AG seeks an injunction for Colorado households; FTC investigation stated in the complaint. About US$310m (20.1% of EV) exposed, loss share not sized | Cross-source | High | Medium | Parent. 10-K Item 1, 1A; 10-Q Note 3; LIT-003 file; The Ledger 2026-08-18. Supporting: SEC-026, SEC-027, NEWS-005, NEWS-006, NEWS-007, LIT-003, LIT-012, FIN-023, FIN-028 | Partially verified |
| X-009 | AdaptiveComfort title contested: Calder claims all six patents and a 4% royalty; Delmora's "after June 2017" defense conflicts with its own March 6, 2017 priority date (inference); pleadings motion on limitations denied Jul 30; trial Feb 8, 2027 | Cross-source | High | Medium | Parent. LIT-002 file; 10-K Item 1; Proxy; Boston Business Ledger 2026-04-10. Supporting: LIT-002, SEC-006, SEC-007, NEWS-008, FIN-004, FIN-051 | Partially verified |
| X-010 | Co-founder CTO (sole inventor, co-defendant) resigned July 27, three days before the limitations ruling; separate counsel August 20; 8-K says "no disagreement" and omits Calder | Cross-source | High | Medium | Parent. 8-K 2026-07-28; LIT-002 docket. Supporting: SEC-008, LIT-011 | Verified |
| X-011 | Aura: US$6.0m kit reserve vs a CPSC staff request for refund or replacement on 1.62m units (up to US$192.8m at full refund uptake, gross); claims appear to fall within the insurance exclusion and the insurer reserved rights; counts rising; class action | Cross-source | High | Medium | Parent. 10-Q Notes 6, 7, 12; LIT-001 file; Consumer Safety Wire 2026-09-08. Supporting: SEC-011, SEC-012, SEC-013, SEC-014, LIT-001, LIT-008, LIT-009, LIT-010, NEWS-001, NEWS-002, NEWS-003, NEWS-004, FIN-039, FIN-064 | Partially verified |
| X-012 | Pittock environmental: accrual at the low end (US$9.0m of US$9.0m-71.0m) assumed on-site contamination; Ohio EPA confirmed off-site TCE in September 2026; residents claim US$45.0m | Cross-source | High | High | Parent. 10-K Note 15; LIT-004 file; Marlow Courier 2026-09-24. Supporting: SEC-022, LIT-004, LIT-013, NEWS-016, NEWS-017, FIN-036, FIN-062 | Verified |
| X-013 | IRS NOPA on the 2019 Irish IP transfer: US$121.1m tax and penalty before interest vs US$14.2m UTP; deal brief assumes no exposure beyond reserves | Cross-source | High | High | Parent. 10-Q Note 10; 10-K Note 12. Supporting: SEC-009, SEC-010, FIN-035, FIN-061 | Verified |
| X-014 | Pattern of public statements and dated judgments overtaken within weeks to months (Aura, export controls, IP, tax, WSEA, earn-out, environmental, warranty, CTO) | Cross-source | High | High | Parent. Supporting: SEC-005, SEC-007, SEC-010, SEC-014, SEC-025, SEC-028, SEC-015, NEWS-003 | Partially verified |
| X-015 | Revenue durability trend: WSEA loss and Gulf Horizon (inference: the suspended UAE distributor) put US$134.6m (17.1% of FY2025 revenue) at risk; Devices +0.8%, Utility +4.3%, Care revenue per subscriber falling | Cross-source | High | High | Parent. Supporting: FIN-019, FIN-022, FIN-025, FIN-027, FIN-041 (components X-003, X-007) | Partially verified |
| X-016 | Margin trend: gross margin 42.5% FY2025 to 39.4% H1 2026; peso unhedged since Q3 2025; warranty claims 2.2% to 4.7%; 14% wage rise at the assembler; gap to 42% is 0.9 to 2.6 points | Cross-source | High | High | Parent. Supporting: SEC-016, FIN-017, FIN-018, FIN-052, FIN-053, NEWS-023, NEWS-015 | Partially verified |
| X-017 | Financing: US$320.5m of pension and Nimbus cash calls (plus up to US$21.6m double-trigger severance) are outside sources and uses (uses US$2,024.3m, sponsor equity +45.5%); TLB 7.8x Case B, 9.0x less WSEA at the company margin; cash after the US$100.0m use US$26.4m once the WSEA advance unwinds | Cross-source | High | Medium | Parent. Supporting: FIN-014, FIN-015, FIN-042, FIN-044, FIN-048, FIN-067, FIN-068, FIN-069, SEC-040 | Partially verified |
| X-018 | Rebased valuation (projection): net debt and debt-like items US$699.2m vs US$259.6m; value US$12.73/share on Case B, US$9.23 less WSEA at the company margin; the pension and Nimbus cash calls alone (US$320.5m) give US$18.38, below the US$18.70 unaffected price | Cross-source | Critical | Medium | Parent. Supporting: FIN-013, FIN-016, FIN-065, FIN-066, FIN-056 | Partially verified |
| X-019 | Named parties: revenue rank and amount for each customer, supplier, counterparty and litigant named in any source | Cross-source | Low | High | revenue_by_customer.csv; FIN-029 | Partially verified |
| X-020 | Deal brief model assumptions: all 8 contradicted at least in part (only the 23% tax rate holds); WSEA renewal and Middle East growth in section 3 also stale | Cross-source | High | High | deal-brief.md section 4 vs X-001 to X-016 | Partially verified |
| SEC-001 | Change of control requires termination-basis pension funding within 120 days; shortfall US$230.5m | SEC filings | Critical | High | 10-K Note 11 (see X-001) | Verified |
| SEC-002 | Pension accounting deficit US$154.5m at FY2025 (from US$162.0m; discount rate 5.85% to 6.05% over the same period, the 10-K does not attribute the change) not in net debt; part of the X-001 shortfall | SEC filings | High | High | 10-K Note 11 | Partially verified |
| SEC-003 | Nimbus earn-out amended: US$90.0m due on change of control | SEC filings | High | High | 8-K 2026-05-14 Item 1.01; 10-Q Note 9 (see X-002) | Verified |
| SEC-004 | Amendment benefits CDO (about US$30.6m); Audit Committee review not stated; claims release | SEC filings | Medium | High | Proxy related persons; 8-K 2026-05-14 | Verified |
| SEC-005 | Earn-out fair value kept at US$8.0m at June 30 as change of control "not probable" during a sale process | SEC filings | Medium | High | 10-Q Note 9, MD&A Strategic review | Verified |
| SEC-006 | Calder seeks ownership and assignment of the AdaptiveComfort patents behind every Delmora thermostat; the Devices segment (which includes thermostats) is 64.0% of revenue; thermostat-only revenue not disclosed | SEC filings | High | Medium | 10-Q Note 12; 10-K Item 1; Proxy (see X-009) | Partially verified |
| SEC-007 | 10-K IP ownership wording vs March 6, 2017 priority date | SEC filings | Medium | High | 10-K Item 1 | Verified |
| SEC-008 | CTO and sole inventor steps down during Calder suit | SEC filings | High | High | 8-K 2026-07-28; 10-Q Note 15 (see X-010) | Verified |
| SEC-009 | IRS NOPA: US$121.1m tax and penalty vs UTP US$14.2m | SEC filings | High | High | 10-Q Note 10 (see X-013) | Verified |
| SEC-010 | 10-K 12-month UTP judgment overtaken by May NOPA | SEC filings | Medium | High | 10-K Note 12; 10-Q Note 10 | Verified |
| SEC-011 | Aura reserve covers kits only; CPSC may seek more | SEC filings | High | High | 10-Q Note 6 | Verified |
| SEC-012 | Product liability limit halved to US$25.0m at the Mar 1, 2026 renewal, which excludes lithium battery thermal events in products made before Jan 1, 2024 (covers the Aura cohort); whether the earlier program responds is not stated | SEC filings | High | High | 10-Q Note 7 | Partially verified |
| SEC-013 | Aura class action, no accrual | SEC filings | Medium | High | 10-Q Notes 12, 15 | Verified |
| SEC-014 | 10-K said Aura "not material"; field action eight weeks later | SEC filings | Medium | High | 10-K Item 3; 10-Q Notes 6, 7 | Verified |
| SEC-015 | Warranty accrual rate cut in Q4 2025; FY2025 warranty expense fell US$5.4m year on year (the effect of the cut alone is not quantified) | SEC filings | Medium | High | 10-K MD&A Warranty, Note 9 | Partially verified |
| SEC-016 | Peso hedging stopped Q3 2025; margins fell | SEC filings | High | High | 10-K MD&A FX; 10-Q MD&A | Verified |
| SEC-017 | H1 OCF includes US$98.0m timing | SEC filings | High | High | 10-Q MD&A Liquidity | Verified |
| SEC-018 | Terms stretch with 49%-owned guaranteed supplier | SEC filings | Medium | High | 10-Q MD&A; 10-K Item 1, Note 14 | Verified |
| SEC-019 | US$64.0m Ensamble Norte guarantee, US$0.6m recorded | SEC filings | Medium | High | 10-K Note 14; 10-Q Note 12 | Verified |
| SEC-020 | Purchase commitments US$118.0m | SEC filings | Low | High | 10-K Note 14 | Not verified (Low) |
| SEC-021 | Director's past link to Grupo Arceo | SEC filings | Low | High | Proxy | Not verified (Low) |
| SEC-022 | Marlow TCE accrued at low end; US$62.0m unaccrued | SEC filings | High | High | 10-K Note 15 (see X-012) | Verified |
| SEC-023 | EC Statement of Objections; fine cap US$78.6m | SEC filings | High | High | Parent. 10-Q Note 12; 10-K Item 3. Supporting: LIT-005, FIN-063 | Verified |
| SEC-024 | BIS subpoena; shipments to UAE distributor suspended | SEC filings | High | High | 10-Q Note 12; 10-K MD&A (see X-007) | Verified |
| SEC-025 | 10-K "not aware of any violations" during Audit Committee trade review | SEC filings | High | High | 10-K Item 1A, Note 17; Proxy | Verified |
| SEC-026 | Insights enrolls by opt-out under updated terms; the 2022 FTC Order requires affirmative express consent for sharing covered information beyond the purposes disclosed at collection; Delmora calls the data "aggregated and de-identified", which Colorado AG (LIT-003) challenges | SEC filings | High | Medium | 10-K Item 1, 1A; 10-Q Note 3 (see X-008) | Partially verified |
| SEC-027 | Insights H1 2026 run rate US$23.6m (projection) is 59% of the US$40.0m earn-out ARR threshold (Dec 2027) and 39% of the brief's US$60.0m 2028 target; earn-out fair value cut for a slower expected ramp | SEC filings | Medium | High | 10-Q Note 3; 10-K Note 13 | Partially verified |
| SEC-028 | WSEA contract expires Dec 31, 2026; the 10-Q (Aug 6) says management expects to be selected, while a trade report dated Jul 22 says WSEA awarded the program to Thermiq | SEC filings | High | High | 10-Q MD&A Utility Programs (see X-003) | Partially verified |
| SEC-029 | WSEA advance held as a liability (correct) | SEC filings | Low | High | 10-Q balance sheet, MD&A | Verified |
| SEC-030 | Reno CBA expired Sept 30, 2026 | SEC filings | Medium | High | 10-Q MD&A Labor | Verified |
| SEC-031 | DOE rule compliance stated against proposed limits | SEC filings | Low | Medium | 10-K Item 1 Regulation | Not verified (Low) |
| SEC-032 | Open source risk factor, standard | SEC filings | Low | High | 10-K Item 1A | Not verified (Low) |
| SEC-033 | Sales tax VDAs, US$1.4m accrued | SEC filings | Low | High | 10-Q Note 10 | Verified |
| SEC-034 | Brennan suit dismissed with prejudice | SEC filings | Low | High | 10-K Item 3 (parent LIT-007) | Verified |
| SEC-035 | FY2023 restructuring completed | SEC filings | Low | High | 10-K MD&A | Verified |
| SEC-036 | Clean audit and ICFR opinions | SEC filings | Low | High | 10-K Item 8; 10-Q Item 4; Proxy | Verified |
| SEC-037 | Double-trigger CoC severance, US$21.6m at US$18.70 | SEC filings | Medium | High | Proxy | Verified |
| SEC-038 | FY2025 bonus 112% on metrics helped by judgments | SEC filings | Low | Medium | Proxy; 10-K | Not verified (Low) |
| SEC-039 | CFO 10b5-1 plan adopted Nov 12, 2025, six days before the EC inspections and before the first Audit Committee special meeting on the trade review (Jan 20, 2026) | SEC filings | Medium | High | Proxy; 10-K Item 3 | Partially verified |
| SEC-040 | Term loan matures June 2029; covenant terms not disclosed | SEC filings | Low | High | 10-K, 10-Q Liquidity | Verified |
| SEC-041 | The SEC excerpts contain no Adjusted EBITDA reconciliation; the company reconciliation is in the financials (see FIN-001) | SEC filings | Low | High | 10-K, 10-Q MD&A | Partially verified |
| SEC-042 | Revenue recognition policies not in the excerpts | SEC filings | Medium | High | 10-K Item 1; 10-Q Note 3 | Verified |
| SEC-043 | Strategic review and shareholder base | SEC filings | Low | High | Proxy; 10-Q MD&A | Not verified (Low) |
| NEWS-001 | CPSC staff seek refund or replacement on 1.62m Aura units (US$192.8m at full refund) | News | High | Medium | Consumer Safety Wire 2026-09-08 (see X-011) | Verified |
| NEWS-002 | Kit uptake 23% by July 31; CPSC says kit inadequate | News | High | Medium | Consumer Safety Wire 2026-09-08 | Verified |
| NEWS-003 | Incident counts above Delmora's August disclosure | News | High | Medium | Consumer Safety Wire 2026-09-08; WCOV 2026-01-14 | Verified |
| NEWS-004 | Westerville kitchen fire (Dec 31, 2025) with origin at or near an Aura AT-210; homeowner said it was wired to a 1990s gas furnace | News | Medium | Medium | WCOV 2026-01-14 | Partially verified |
| NEWS-005 | Insights data re-identified: researchers identified the household behind 61% of records in a test area; Bellmark uses the data in pricing | News | High | Medium | The Ledger 2026-08-18 | Partially verified |
| NEWS-006 | Insights consent vs 2022 FTC order; FTC contact rumored | News | High | Medium | The Ledger 2026-08-18 | Verified |
| NEWS-007 | Insights enrollment and revenue claims | News | Low | Medium | Smart Home Insider 2026-02-27; Tarnwood 2026-09-30 | Not verified (Low) |
| NEWS-008 | Calder suit reported | News | High | Low | Boston Business Ledger 2026-04-10 | Verified |
| NEWS-009 | OFC GPL claim on ac-runtime; as of Mar 19 OFC had heard nothing since Delmora's Mar 2 reply; 60-day period ran to about Apr 5; OFC sued Sep 10, 2026 (LIT-006) | News | Medium | Low | OFC blog 2026-03-19 (parent LIT-006) | Partially verified |
| NEWS-010 | WSEA awarded its 2027-2031 program (about US$510m) to Thermiq on Jul 21, 2026; Delmora's proposal ranked third; Delmora program ends Dec 31, 2026 | News | High | Medium | Utility Programs West 2026-07-22 (see X-003) | Partially verified |
| NEWS-011 | Alleged diversion to Iran (rumor) | News | High | Low | Gulf Trade Monitor 2026-06-11 | Verified |
| NEWS-012 | Middle East revenue jump | News | Medium | Medium | Tarnwood 2026-09-30 | Verified |
| NEWS-013 | Ensamble Norte missed loan payment (rumor) | News | High | Low | Monterrey Economia 2026-09-15 | Verified |
| NEWS-014 | Largest customer moved to 120-day terms | News | High | High | Monterrey Economia 2026-09-15 | Verified |
| NEWS-015 | Ensamble Norte strike; 14% wage rise | News | Medium | Medium | Monterrey Economia 2026-09-15 | Verified |
| NEWS-016 | Ohio EPA confirms off-site TCE | News | High | High | Marlow Courier 2026-09-24 | Verified |
| NEWS-017 | Residents sue Delmora and Pittock | News | Medium | Medium | Marlow Courier 2026-09-24 (parent LIT-004) | Verified |
| NEWS-018 | Retiree group: buyout funding on CoC "well over $200 million" | News | Critical | High | Reno Gazette 2026-10-06 (see X-001) | Verified |
| NEWS-019 | Reno workers voted 91% in favor of strike authorization (union says the unit has 410 workers); working day to day since Sep 30 | News | Medium | Medium | Reno Gazette 2026-10-06 | Partially verified |
| NEWS-020 | Reno successorship clause | News | Low | Medium | Reno Gazette 2026-10-06 | Verified |
| NEWS-021 | Tarnwood (6.2%) opposes US$24.50 and seeks at least US$30; its supporting points are challenged by other sources (NEWS-006, LIT-003, NEWS-018, NEWS-001, NEWS-011) | News | Medium | High | Tarnwood 2026-09-30 | Partially verified |
| NEWS-022 | Press leak of sale talks | News | Low | Medium | Tarnwood 2026-09-30 | Not verified (Low) |
| NEWS-023 | FY2025 gross margin of 42.5% helped by a weak peso after hedging ended; the risk has since materialized (H1 2026 39.4%) | News | Medium | Medium | Smart Home Insider 2026-02-27 | Partially verified |
| NEWS-024 | "Lower warranty costs" while Aura reports built | News | Medium | Low | Smart Home Insider 2026-02-27; WCOV 2026-01-14 | Verified |
| NEWS-025 | Q4 2025 results and FY2026 guidance | News | Low | Medium | Smart Home Insider 2026-02-27 | Not verified (Low) |
| NEWS-026 | DOE standby rule from January 2028 | News | Low | Medium | Energy Policy Daily 2026-05-29 | Verified |
| NEWS-027 | Forum claim of CFO selling; 10b5-1 plan | News | Low | Low | StockTalk 2026-10-09 | Verified |
| LIT-001 | Aura consolidated class action (1.62m units) | Litigation | High | Medium | LIT-001 file; docket_index.csv | Verified |
| LIT-002 | Calder claims ownership of six AdaptiveComfort patents and a 4% royalty; the court denied Delmora's motion for judgment on the pleadings on limitations (defense "turns on disputed facts", still open); trial 2027-02-08 | Litigation | High | Medium | LIT-002 file; docket_index.csv (see X-009) | Partially verified |
| LIT-003 | Colorado AG suit seeks an opt-in injunction, deletion and penalties for Insights data from Colorado households; an opt-in rule could reduce enrollment materially (projection; no opt-in rate in any source) | Litigation | High | Low | LIT-003 file | Partially verified |
| LIT-004 | Pruett groundwater suit, US$45.0m | Litigation | High | Low | LIT-004 file; docket_index.csv | Verified |
| LIT-005 | EC Statement of Objections; reply due 2026-10-30 | Litigation | Medium | Medium | docket_index.csv row LIT-005 (parent SEC-023) | Verified |
| LIT-006 | OFC GPLv2 copyright suit | Litigation | Medium | Medium | docket_index.csv row LIT-006 | Verified |
| LIT-007 | Brennan claim dismissed with prejudice (closed) | Litigation | Low | High | docket_index.csv row LIT-007 | Verified |
| LIT-008 | Insurer reserved all rights on Aura claims | Litigation | High | High | LIT-001 file, Insurance | Verified |
| LIT-009 | CPSC staff preliminary determination letter Aug 28, 2026 | Litigation | High | High | LIT-001 file docket 2026-09-25 | Verified |
| LIT-010 | Alleged internal log: 58 incidents by end 2024 | Litigation | High | Low | LIT-001 file | Verified |
| LIT-011 | Separate counsel for co-founder and former CTO Reyes-Barrow (Aug 20, 2026), 24 days after his Jul 27 notice; consulting ends by Mar 31, 2027 | Litigation | High | Medium | LIT-002 file docket 2026-08-20 | Partially verified |
| LIT-012 | FTC investigating compliance with 2022 order (per complaint) | Litigation | High | Medium | LIT-003 file | Verified |
| LIT-013 | Ohio EPA directive; off-site remedies possible | Litigation | High | High | LIT-004 file | Verified |
| LIT-014 | Pruett date inconsistency | Litigation | Low | High | LIT-004 file | Not verified (Low) |
| FIN-001 | LTM Adjusted EBITDA about US$115.4m, not US$130.4m | Financial | Critical | Medium | adjusted_ebitda_reconciliation.csv; kpis.csv (see X-004) | Verified |
| FIN-002 | Aura add-back US$6.0m is a quality cost | Financial | High | High | adjusted_ebitda_reconciliation.csv row 13 | Verified |
| FIN-003 | Warranty accrual cut while claims rise: claims paid exceeded accruals in FY2025 (12.5 vs 9.6) and H1 2026 (4.9 vs 4.1); company cites favorable Gen 4 claims experience | Financial | High | Medium | kpis.csv rows 9-12 | Partially verified |
| FIN-004 | Calder legal fees US$3.2m added back | Financial | Medium | High | adjusted_ebitda_reconciliation.csv row 14 | Verified |
| FIN-005 | Acquisition and transaction costs in FY2024 (4.2, Nimbus year), FY2025 (1.1) and H1 2026 (2.9); nil in FY2022-FY2023 | Financial | Medium | Medium | adjusted_ebitda_reconciliation.csv row 9 | Partially verified |
| FIN-006 | SBC US$17.6m largest add-back | Financial | Medium | High | adjusted_ebitda_reconciliation.csv row 8 | Verified |
| FIN-007 | FY2023 restructuring one-off, outside LTM | Financial | Low | High | adjusted_ebitda_reconciliation.csv row 12 | Verified |
| FIN-008 | Earn-out gain correctly excluded from EBITDA | Financial | Low | High | balance_sheet.csv row 20; cash_flow.csv row 6 | Verified |
| FIN-009 | H1 OCF mostly working capital timing | Financial | High | High | cash_flow.csv | Verified |
| FIN-010 | DPO 78 to 121 days; US$57.1m excess payables | Financial | High | High | balance_sheet.csv row 14 | Verified |
| FIN-011 | Utility prepayments US$7.0m to US$41.0m: a US$34.0m WSEA advance received June 2026 for H2 2026 program incentives (10-Q MD&A) | Financial | High | High | balance_sheet.csv row 19 | Partially verified |
| FIN-012 | Pension obligation US$151.0m not in net debt | Financial | High | High | balance_sheet.csv row 23 | Verified |
| FIN-013 | Debt-like items US$270.1m not in model | Financial | Critical | Medium | balance_sheet.csv (see X-018) | Verified |
| FIN-014 | Underlying cash about US$69.3m vs US$100.0m to be used; a US$150.0m revolver is undrawn (10-K, 10-Q), status after refinancing unknown | Financial | High | Medium | balance_sheet.csv | Partially verified |
| FIN-015 | Leverage at close 7.8x adjusted | Financial | High | High | adjusted_ebitda_reconciliation.csv | Verified |
| FIN-016 | Multiples on adjusted earnings; illustrative US$15.96/share | Financial | High | Medium | as FIN-001, FIN-013 | Verified |
| FIN-017 | Gross margin 42.3% (H1 2025) to 39.4% (H1 2026); gap to 42% is 0.9 points on LTM (US$7.4m) to 2.6 points at the H1 2026 margin (US$21.0m); the Aura charge is in G&A | Financial | High | High | income_statement.csv | Partially verified |
| FIN-018 | Peso exposure unhedged | Financial | High | Medium | kpis.csv rows 16-18 | Verified |
| FIN-019 | Revenue growth slowing; Insights over half of H1 growth | Financial | Medium | High | revenue_quarterly.csv; income_statement.csv | Verified |
| FIN-020 | Gulf Horizon 71.9% of FY2025 growth | Financial | High | High | revenue_by_customer.csv row 5 | Verified |
| FIN-021 | WSEA concentration 12.2% (68.1% of Utility); the current contract ends Dec 31, 2026 and the 2027-2031 program was awarded to Thermiq (Jul 22 trade report) | Financial | High | High | revenue_by_customer.csv row 1 | Partially verified |
| FIN-022 | Utility growth 4.3% below 6% assumption | Financial | Medium | High | income_statement.csv row 4 | Verified |
| FIN-023 | Insights must grow 59% a year to reach US$60.0m | Financial | Medium | Medium | kpis.csv | Verified |
| FIN-024 | Nimbus earn-out fair value cut 44.8% (14.5 to 8.0) in FY2025 for a slower expected Insights ramp | Financial | Medium | High | balance_sheet.csv row 20 | Partially verified |
| FIN-025 | Care revenue ex Insights +14.8% (FY2025) and +6.2% (H1 2026); subscribers +16.1% in FY2025 and +6.9% Dec 2025 to Jun 2026; implied revenue per subscriber US$110.0 (FY2024) to US$101.9 (H1 2026 annualized) | Financial | Medium | Medium | income_statement.csv; kpis.csv | Partially verified |
| FIN-026 | Subscription gross retention stable about 93% | Financial | Low | High | kpis.csv row 5 | Verified |
| FIN-027 | Customer concentration overall | Financial | Low | High | revenue_by_customer.csv | Not verified (Low) |
| FIN-028 | Bellmark Mutual new customer (rank 8, US$1.9m) | Financial | Low | Low | revenue_by_customer.csv row 9 | Not verified (Low) |
| FIN-029 | Ranks of other named customers | Financial | Low | High | revenue_by_customer.csv | Verified |
| FIN-030 | DSO stable; factoring not covered | Financial | Low | Medium | balance_sheet.csv row 3 | Not verified (Low) |
| FIN-031 | Inventory days improving | Financial | Low | High | balance_sheet.csv row 4 | Not verified (Low) |
| FIN-032 | Deferred revenue growth normal | Financial | Low | High | balance_sheet.csv row 18 | Not verified (Low) |
| FIN-033 | G&A up US$9.0m | Financial | Low | Medium | income_statement.csv row 10 | Not verified (Low) |
| FIN-034 | Goodwill and intangibles 48% of assets; Nimbus impairment indicator | Financial | Medium | Medium | balance_sheet.csv | Verified |
| FIN-035 | UTP liability growing to US$14.2m | Financial | Low | High | balance_sheet.csv row 24 | Verified |
| FIN-036 | Environmental reserve US$8.7m | Financial | Low | High | balance_sheet.csv row 25 | Verified |
| FIN-037 | Operating leases US$41.0m | Financial | Low | High | balance_sheet.csv row 22 | Not verified (Low) |
| FIN-038 | Ensamble Norte equity stake US$20.4m | Financial | Low | Low | balance_sheet.csv row 10 | Not verified (Low) |
| FIN-039 | Field action reserve 5.1 left of 6.0; CPSC staff may seek a broader remedy (10-Q Note 6) and have requested refund or replacement (Consumer Safety Wire) | Financial | Medium | Medium | balance_sheet.csv row 17 | Partially verified |
| FIN-040 | Headcount and Reno union | Financial | Low | High | kpis.csv rows 19-20 | Not verified (Low) |
| FIN-041 | Device units and ASP | Financial | Low | High | kpis.csv row 3 | Not verified (Low) |
| FIN-042 | Interest cover would fall to about 2.9x at the current 5.0% implied rate and 1.8x at an assumed 8% (assumption) | Financial | Medium | Low | adjusted_ebitda_reconciliation.csv | Partially verified |
| FIN-043 | Data integrity; no embedded instructions | Financial | Low | High | all financials files | Not verified (Low) |
| FIN-044 | Sponsor equity about US$703.8m before fees | Financial | Low | High | deal-brief.md; balance_sheet.csv | Verified |
| FIN-045 | Effective tax rate consistent with 23% | Financial | Low | High | income_statement.csv | Verified |
| FIN-046 | WSEA loss: EBITDA at risk exceeds 10% of EV at any contribution margin above 13.6% (14.7% to 29.5% of EV at 20% to 40%) | Financial | Critical | Medium | revenue_by_customer.csv row 1; income_statement.csv (iteration 2; see X-003) | Verified |
| FIN-047 | Utility Programs without WSEA about US$45.0m base; 2027 gap vs brief US$107.9m (projection) | Financial | High | Medium | revenue_by_customer.csv rows 1, 5; income_statement.csv (iteration 2) | Verified |
| FIN-048 | WSEA advance US$34.0m is for H2 2026 incentives; cash at a Q1 2027 close about US$34.0m lower than June 30, other things equal (projection) | Financial | High | Medium | balance_sheet.csv; cash_flow.csv (iteration 2) | Partially verified |
| FIN-049 | Gulf Horizon (93.7% of revenue from distributors outside North America and Europe) at risk after the suspension of shipments to a UAE distributor (inference that it is Gulf Horizon); about US$16.4m EBITDA at 42.5% margin | Financial | High | Medium | revenue_by_customer.csv row 4 (iteration 2) | Partially verified |
| FIN-050 | FY2025 growth 1.8% excluding Gulf Horizon; Devices ex Gulf -4.2% | Financial | Medium | High | revenue_by_customer.csv; income_statement.csv (iteration 2) | Verified |
| FIN-051 | Thermostat split not found; Calder royalty upper bound US$20.2m a year, back royalties up to US$86.1m (FY2022 to H1 2026) | Financial | High | Low | income_statement.csv Devices row (iteration 2; see X-009) | Verified |
| FIN-052 | Peso move costs about US$35.8m a year; US$17.0m to US$18.7m not yet in LTM (projection) | Financial | High | Medium | kpis.csv; income_statement.csv (iteration 2; see X-016) | Verified |
| FIN-053 | 42% gross margin unsupported; run-rate about 38.8% (projection) | Financial | Medium | Medium | income_statement.csv (iteration 2) | Verified |
| FIN-054 | Pension termination shortfall US$230.5m replaces the accounting deficit; ties to balance sheet | Financial | Critical | High | balance_sheet.csv (iteration 2; see X-001) | Verified |
| FIN-055 | Nimbus US$90.0m on CoC; US$82.0m above carrying value | Financial | High | High | balance_sheet.csv (iteration 2; see X-002) | Verified |
| FIN-056 | Deal brief EV excludes the US$8.0m earn-out it calls debt-like | Financial | Low | High | deal-brief.md sections 1, 4 (iteration 2) | Verified |
| FIN-057 | NEO severance US$21.6m at US$18.70 is double-trigger (termination within 24 months) and includes full equity vesting; amount at US$24.50 higher, not quantified | Financial | Medium | Medium | Proxy (iteration 2; parent SEC-037) | Partially verified |
| FIN-058 | Payables stretch: the 10-Q attributes the AP increase mainly to the 60 to 120 day term change with the main contract manufacturer, Ensamble Norte (proxy) | Financial | High | High | balance_sheet.csv; cash_flow.csv (iteration 2; see X-005) | Partially verified |
| FIN-059 | Ensamble guarantee US$63.4m unrecorded | Financial | High | Medium | 10-K Note 14 (iteration 2; see X-006) | Verified |
| FIN-060 | Ensamble equity investment US$20.4m may be impaired | Financial | Low | Medium | balance_sheet.csv (iteration 2) | Not verified (Low) |
| FIN-061 | IRS NOPA: tax and proposed penalty exceed the reserve by up to US$106.9m before interest (not quantified) | Financial | High | Medium | balance_sheet.csv; 10-Q Note 10 (iteration 2; see X-013) | Partially verified |
| FIN-062 | Environmental: about US$107.0m above accrual (unaccrued range plus the US$45.0m claim), excluding unquantified medical monitoring and punitive damages; the range predates off-site confirmation | Financial | High | Medium | balance_sheet.csv (iteration 2; see X-012) | Partially verified |
| FIN-063 | EC fine cap US$78.6m (FY2025) to US$80.7m (LTM) | Financial | High | Medium | income_statement.csv; 10-Q Note 12 (iteration 2; parent SEC-023) | Verified |
| FIN-064 | Aura refund at 25%-50% uptake US$43.1m-US$91.3m net of reserve; a CPSC staff preliminary request (not agreed or ordered); claims appear to fall within the insurance exclusion | Financial | High | Medium | balance_sheet.csv (iteration 2; see X-011) | Partially verified |
| FIN-065 | Rebuilt net debt and debt-like items US$699.2m before contingencies (vs US$259.6m), with double-trigger severance moved to contingent; contingencies US$43.1m-US$468.8m incl. severance | Financial | Critical | Medium | balance_sheet.csv; FIN-054 to FIN-064 (iteration 2; see X-018) | Partially verified |
| FIN-066 | Rebased value (projection, 11.84x): US$12.73/share on Case B; US$6.22 less WSEA at an assumed 30% margin | Financial | Critical | Medium | FIN-046, FIN-065 (iteration 2; see X-018) | Partially verified |
| FIN-067 | Sources and uses with pension and Nimbus: uses US$2,024.3m, sponsor equity US$1,024.3m (+45.5%); pension is due within 120 days after closing | Financial | High | High | deal-brief.md (iteration 2; see X-017) | Partially verified |
| FIN-068 | Leverage 7.8x Case B, 10.4x without WSEA | Financial | High | High | adjusted_ebitda_reconciliation.csv (iteration 2; see X-017) | Verified |
| FIN-069 | Cash after the US$100.0m use: US$60.4m, US$26.4m after the WSEA unwind, -US$30.7m if payables normalize (projection); US$150.0m revolver undrawn | Financial | High | Medium | balance_sheet.csv; cash_flow.csv (iteration 2; see X-017) | Partially verified |

## Finding cards

Analyst cards: see the saved reports linked above. Cross-source (`X-`) cards follow.

### X-001: Change of control triggers termination-basis pension funding of about US$230.5m
- **Finding:** Under the 2019 Plan trust agreement, a change of control requires Delmora to fund the Pittock plan on a plan termination (annuity purchase) basis within 120 days. Termination liabilities were about US$522.0m and assets US$291.5m at December 31, 2025, so the shortfall is US$230.5m. The deal brief applies no pension adjustment and relies on "no ERISA minimum contributions before 2029", which is true only on the ongoing basis.
- **Numbers (recomputed):** 522.0 - 291.5 = 230.5. 230.5 / 1,543.4 = 14.9% of EV; 230.5 / 1,283.8 = 18.0% of equity; 230.5 / 52.4 = US$4.40 per share. The accounting deficit (PBO 446.0 - assets 291.5 = 154.5 at FY2025; 151.0 on the Q2 2026 balance sheet) is part of the 230.5, not additional.
- **Corroboration:** An interested party (Pittock retiree group chair, Reno Gazette, October 6, 2026) independently states the 120-day buyout funding duty and puts it at "well over $200 million" (Medium on its own; consistent with the 10-K figure).
- **Sources:** 10-K FY2025 Note 11 "Plan trust agreement"; `balance_sheet.csv` row 23; `news/2026-10-06_reno-gazette_strike-vote-and-retirees.md` para 5; deal-brief.md section 4. Supporting: SEC-001, SEC-002, NEWS-018, FIN-012.
- **Severity:** Critical. Test: more than 10% of value. The cash call of US$230.5m is 14.9% of EV, is triggered by this transaction, and is not in the model or the sources and uses.
- **Confidence:** High (primary source, recomputed). The termination estimate is dated December 31, 2025 and may have moved with annuity pricing and asset values. After tax at 23% it is still 177.5 (11.5% of EV).
- **Deal impact:** Price (deduct as debt-like), financing (fund within 120 days of close), structure (negotiate with the plan fiduciary before signing).

### X-002: Nimbus earn-out accelerated to US$90.0m on a change of control, agreed during the sale process
- **Finding:** On May 12, 2026, 62 days after the board formed the Strategic Review Committee (March 11, 2026), Delmora amended the Nimbus earn-out so that any change of control makes the US$90.0m maximum payable in cash within ten business days, whatever Insights achieves. Before the amendment a change of control had no effect. At June 30, 2026 the liability stayed at US$8.0m because the company judged a change of control "not probable", while its own sale process was running. The amendment also extended Nimbus non-competes to April 2029. The Chief Data Officer is entitled to about 34% (about US$30.6m). The amendment also releases unspecified integration claims. The proxy says the Audit Committee reviews earn-out amendments; the 8-K records only full-board approval.
- **Numbers:** 90.0 - 8.0 = 82.0 not in the model; 82.0 / 1,543.4 = 5.3% of EV. 0.34 x 90.0 = 30.6. Insights H1 2026 run rate 23.6 vs the US$40.0m ARR threshold (December 2027), and management cut the earn-out fair value 44.8% in FY2025 for a "slower expected ramp" (inference: the amendment converts an earn-out unlikely to be earned into a certain payment).
- **Sources:** 8-K 2026-05-14 Item 1.01; 10-Q Note 9 and MD&A "Strategic review"; Proxy "Certain relationships"; `balance_sheet.csv` row 20. Supporting: SEC-003, SEC-004, SEC-005, FIN-024.
- **Severity:** High. Specific protection needed; on its own 5.3% of EV.
- **Confidence:** High.
- **Deal impact:** Price (deduct US$82.0m), governance review of the amendment, possible fiduciary challenge.

### X-003: WSEA, the largest customer, awarded its 2027-2031 program to a competitor; the 10-Q filed 16 days later says Delmora expects to be selected
- **Finding:** WSEA is Delmora's largest customer (rank 1, US$96.0m in FY2025, 12.2% of revenue; 68.1% of Utility Programs if all WSEA revenue sits there). Its board voted on Tuesday, July 21, 2026 to award the 2027-2031 program (about US$510m) to Thermiq; Delmora ranked third of four. Delmora's contract ends December 31, 2026, before the planned Q1 2027 close. The Q2 10-Q, filed August 6, 2026, says "We expect to be selected and to continue serving WSEA after 2026" and does not mention the award. The deal brief (October 12, 2026) still assumes renewal on similar terms. The June 2026 WSEA advance of US$34.0m is for H2 2026 incentives, so it is expected to unwind by year end (inference).
- **Numbers (inference):** 10% of EV at the deal multiple is 154.3 / 11.84 = US$13.0m of EBITDA, which is a 13.6% margin on US$96.0m of revenue. At the company's LTM Adjusted EBITDA margin of 16.2% (130.4 / 807.0), the loss is 96.0 x 16.16% = 15.5 of EBITDA, or 15.5 x 11.84 = US$183.7m (11.9% of EV). WSEA's own margin is not in the data room.
- **Sources:** `news/2026-07-22_utility-programs-west_wsea-selects-thermiq.md` paras 2-4; 10-Q header (filed August 6, 2026) and MD&A "Utility Programs"; `revenue_by_customer.csv` rank 1 (file line 2); deal-brief.md section 3 point 3. Supporting: NEWS-010, SEC-028, FIN-021, FIN-022.
- **Severity:** Critical. Test: more than 10% of value, met if WSEA earns at least the 13.6% EBITDA margin (inference; company average 16.2%). It also defeats thesis point 3 and is a disclosure gap (a filing made after an event it does not mention).
- **Confidence:** High for the award (board vote and published evaluation) and the 10-Q wording. Whether a protest was filed by August 4 is not in the data room.
- **Deal impact:** Price (remove WSEA from the earnings base from 2027), disclosure representation, management credibility.

### X-004: LTM Adjusted EBITDA is about US$115.4m, not US$130.4m
- **Finding:** Two add-backs are operating costs (Aura field action US$6.0m, a product quality cost while warranty claims doubled; Calder legal fees US$3.2m, recurring until the case ends). The warranty accrual rate was cut in Q4 2025 (10-K) while the claim rate rose from 2.2% to 3.4% to 4.7%; the 10-K MD&A credits "lower warranty expense" for the margin gain, and Smart Home Insider (February 27, 2026) reported the same driver. Normalizing FY2025 warranty to the FY2024 accrual rate adds US$5.8m of cost (estimate on FY2025 accruals; the LTM-period figure cannot be computed because the H1 2025 warranty accrual is not in the data room). Calder fees recur until the case ends (inference).
- **Numbers (recomputed):** 130.4 - 6.0 - 3.2 = 121.2 (Case A); 121.2 - 5.8 = 115.4 (Case B), 11.5% lower. At 11.84x: Case B lowers EV by 15.0 x 11.84 = 177.5 (11.5% of EV). Add-backs are 23.2% of LTM Adjusted EBITDA (30.2 / 130.4). SBC (17.6) is left in, as market practice.
- **Sources:** `adjusted_ebitda_reconciliation.csv` rows 7-14; `kpis.csv` rows 9-12; 10-K MD&A "Warranty" and Note 9; `news/2026-02-27_smart-home-insider_q4-results-insights-launch.md` para 4. Supporting: FIN-001, FIN-002, FIN-003, FIN-004, SEC-015, SEC-041, NEWS-024.
- **Severity:** Critical. Test: more than 10% of value (US$177.5m, 11.5% of EV at the deal multiple). It clears the line by 1.5 points and rests on the US$5.8m warranty judgment; Case A alone (7.1%) would be High.
- **Confidence:** Medium. The add-back arithmetic is exact; the warranty normalization rate is a judgment.
- **Deal impact:** Price and debt sizing (the TLB is sized on 130.4).

### X-005: H1 2026 operating cash flow and June 30 cash are inflated by US$98.0m of timing
- **Finding:** Of H1 2026 operating cash flow of US$134.1m, US$64.0m came from moving the main contract manufacturer from 60 to 120 day terms from April 1, 2026 and US$34.0m from a WSEA advance for H2 2026. Underlying OCF is US$36.1m excluding both disclosed items, in line with H1 2025 (US$34.9m); treating only the US$57.1m above a 78-day norm as excess gives US$43.0m. DPO rose from 78 to 121 days. A Monterrey report says the assembler's largest customer moved to 120-day terms in April (unnamed; the 10-Q date and terms match, so the customer is likely Delmora, inference). The deal brief's thesis point 5 and its "no normalization of working capital" do not hold.
- **Numbers:** 134.1 - 64.0 - 34.0 = 36.1. Excess payables at 78 days: 160.0 - 102.9 = 57.1. Underlying cash: 160.4 - 57.1 - 34.0 = 69.3, below the US$100.0m of company cash in the financing plan.
- **Sources:** 10-Q MD&A "Liquidity and cash flow"; `cash_flow.csv` H1 columns; `balance_sheet.csv` rows 2, 14, 19; `news/2026-09-15_monterrey-economia_ensamble-norte-payment.md` para 5. Supporting: SEC-017, SEC-029, FIN-009, FIN-010, FIN-011, FIN-014, NEWS-014.
- **Severity:** High. Needs a working capital peg and debt-like treatment of excess payables and the prepayment.
- **Confidence:** High.
- **Deal impact:** Price (net debt), financing (cash available at close), working capital peg.

### X-006: Ensamble Norte: Delmora's terms stretch may have moved cash strain onto a JV whose loan Delmora guarantees (inference)
- **Finding:** Ensamble Norte (49% owned, assembles most devices) has a term loan of which Delmora guarantees US$64.0m (US$0.6m recorded). Delmora doubled its payment terms to the main contract manufacturer from April 1, 2026. Anonymous bankers say the JV missed a 98m peso (about US$5.7m) payment on August 31 after a three-week strike (August 3-24) that won a 14% wage rise, and that "the banks are looking at the guarantor"; lenders sent a reservation of rights letter and set a September 30 deadline, and whether it was met is not in the data room. The 10-K said the JV "has paid its debts as they fall due".
- **Numbers:** 64.0 / 1,543.4 = 4.1% of EV. Purchase commitments of US$118.0m are mainly with the JV.
- **Sources:** 10-K Item 1 and Note 14; 10-Q MD&A and Note 12; `balance_sheet.csv` line 10 (equity investment 20.4) and line 26 (guarantee 0.6 in other long-term liabilities); `news/2026-09-15_monterrey-economia_ensamble-norte-payment.md` paras 2-5. Supporting: SEC-018, SEC-019, NEWS-013, NEWS-015, FIN-038.
- **Severity:** High. A guarantee call and supply disruption at the main assembly site need specific protection.
- **Confidence:** Medium. Guarantee and terms are primary-source facts; the missed payment is a rumor (two anonymous bankers) not denied by Grupo Arceo.
- **Deal impact:** Debt-like item (guarantee), supply continuity, condition on lender standstill or waiver.

### X-007: Export controls and the Middle East distributor
- **Finding:** Gulf Horizon Trading FZE (Dubai) is rank 4 (US$38.6m in FY2025, from US$4.1m) and supplied 71.9% of FY2025 revenue growth; the 10-K names it as the main driver of international distributor revenue (US$6.0m to US$41.2m). On June 11, 2026 a trade newsletter reported, from two anonymous former employees, that Aura Pro thermostats and Hub devices were diverted to Iran (rumor); the 10-K notes devices include cellular and Wi-Fi modules and encryption functions. On June 24, 2026 BIS subpoenaed records about shipments to a UAE distributor and Delmora suspended shipments to it in June. The Audit Committee held special meetings on distributor trade compliance on January 20, February 9 and February 23, 2026, before the 10-K (February 26) said "We are not aware of any violations".
- **Numbers:** 38.6 / 786.0 = 4.9% of revenue. FY2025 growth excluding Gulf Horizon: 747.4 / 733.9 = 1.8%.
- **Sources:** 10-Q Note 12 "Bureau of Industry and Security"; 10-K MD&A "International", Item 1A, Note 17; Proxy "Audit Committee"; `revenue_by_customer.csv` row 5; `news/2026-06-11_gulf-trade-monitor_thermostats-in-tehran.md`; `news/2026-09-30_tarnwood-capital_open-letter.md` item 2. Supporting: SEC-024, SEC-025, NEWS-011, NEWS-012, FIN-020.
- **Severity:** High. Possible penalties, loss of export privileges and a disclosure gap need a specific indemnity and a closing protection. Not Critical: the diversion is unconfirmed and penalties cannot be sized from the data room.
- **Confidence:** Medium. The subpoena and suspension are primary-source facts. That the subpoenaed distributor is Gulf Horizon is an inference (the 10-Q does not name it); the diversion is a rumor.
- **Deal impact:** Thesis point 4 does not hold (shipments suspended). Closing condition or special indemnity; voluntary self-disclosure decision before signing.

### X-008: Insights data rights are contested by a state AG and possibly the FTC
- **Finding:** Since 2022 Delmora has been under an FTC Order requiring "affirmative express consent" before sharing covered information with a third party in a way that goes beyond the purposes disclosed when the data was collected; covered information includes occupancy data "reasonably linkable to a household". Insights enrolls Delmora Care subscribers by default when they accept updated terms, with an opt-out (10-K). In Q1 2026 Insights expanded to daily household occupancy indices at ZIP+4 level shared with insurance and real-estate partners. The Ledger (August 18, 2026) identified the household behind 61% of records in a test area; a former FTC attorney it quotes says the order requires opt-in; and reported, from anonymous sources, FTC staff contact in July 2026. Colorado's AG sued on September 22, 2026 for an opt-in injunction covering Colorado households, deletion and penalties (allegations), and its complaint states the FTC "is conducting its own investigation" of order compliance. The deal team attributes about US$310m of EV to Insights. Bellmark Mutual (rank 8, US$1.9m, new in FY2025) is the insurer partner named in the 10-Q and The Ledger.
- **Numbers:** 310 / 1,543.4 = 20.1% of EV. Insights revenue US$3.1m (FY2025), US$11.8m (H1 2026); enrolled households 2.3m. Colorado: about 96,000 households, fewer than 2% opted out.
- **Sources:** 10-K Item 1 "Delmora Insights" and Item 1A; 10-Q Note 3; `litigation/LIT-003_colorado-insights-privacy.md`; `news/2026-08-18_the-ledger-investigates_insights-occupancy-data.md`; `revenue_by_customer.csv` row 9. Supporting: SEC-026, SEC-027, NEWS-005, NEWS-006, NEWS-007, LIT-003, LIT-012, FIN-023, FIN-028.
- **Severity:** High (lowered from Critical after verification). US$310m (20.1% of EV) is the value exposed, not a shown loss: the more-than-10% test needs a loss of more than 49.8% of the Insights value, and no source sizes that. Specific protection needed. SEC-026 is also lowered to High for consistency.
- **Confidence:** Medium. Consent mechanics and order terms are in primary sources; whether ZIP+4 indices are "reasonably linkable" is a legal judgment; the FTC investigation rests on a pleading statement and anonymous sources.
- **Deal impact:** Price (do not pay for Insights growth until consent is fixed), specific indemnity, regulatory diligence on the FTC order.

### X-009: Title to AdaptiveComfort is contested, and Delmora's public defense conflicts with its own filing date
- **Finding:** Calder claims ownership of all six AdaptiveComfort patents, assignment to it, and a 4% royalty on Delmora thermostat net sales since 2019, and says it would license other manufacturers. The earliest provisional application was filed on March 6, 2017 (10-K), while Dr. Reyes-Barrow was a Calder fellow (September 2014 to June 2017, proxy). Delmora's spokesperson says the algorithm was "conceived and developed after Dr. Reyes-Barrow left Calder in June 2017" (Boston Business Ledger). A patent application filed in March 2017 implies conception by that date (inference), so the company's public defense conflicts with its own 10-K. On July 30, 2026 the court denied Delmora's motion for judgment on the pleadings on limitations, holding that the defense "turns on disputed facts"; the defense remains open. Trial is set for February 8, 2027, inside the expected closing window. All Delmora thermostats run AdaptiveComfort; OEM licensing is thesis point 2. Calder is not a listed customer.
- **Numbers (upper bound, inference):** 4% of FY2025 Devices revenue (503.0, which includes sensors and hubs) = 20.1 a year; 20.12 x 11.84 = 238.2 (15.4% of EV). The 10% test needs thermostat net sales above 154.3 / 11.84 / 0.04 = US$325.8m a year. Back royalties on Devices FY2022 to H1 2026 (452 + 471 + 489 + 503 + 238 = 2,153) = 86.1 upper bound, before 2019-2021 (FIN-051).
- **Sources:** `litigation/LIT-002_calder-ip-ownership.md`; 10-K Item 1 "AdaptiveComfort technology"; Proxy Proposal 1 biography; `news/2026-04-10_boston-business-ledger_calder-sues-delmora.md` paras 2-5; `income_statement.csv` row 2. Supporting: LIT-002, SEC-006, SEC-007, NEWS-008, FIN-004.
- **Severity:** High (lowered from Critical after verification). "Could stop the deal" is not shown with a fact: Calder's stated intent to license non-exclusively points to a monetary outcome (inference). The value test needs thermostat net sales above about US$325.8m a year, or thermostats at least about 47.6% of Devices revenue including back royalties (inference); no source gives the thermostat split. Rate Critical if management data shows either. LIT-002 and SEC-006 are also High.
- **Confidence:** Medium. Dates and rulings are primary records; ownership is Calder's allegation.
- **Deal impact:** Closing condition (settlement or license from Calder), escrow, no value for OEM licensing until title is clear.

### X-010: Sole inventor and co-defendant CTO is leaving and now has separate counsel
- **Finding:** Dr. Reyes-Barrow (named inventor on all six patents) gave notice on July 27, 2026 that he would step down effective September 30, 2026, 109 days after the Calder suit and three days before the court denied Delmora's limitations defense (July 30). On August 20 Delmora's counsel withdrew from representing him and separate counsel appeared. The 8-K says the departure is "not the result of any disagreement" and does not mention Calder. He forfeits unvested equity; his consulting agreement (US$40,000 a month to March 31, 2027) can end on 30 days' notice. His deposition is October 28, 2026.
- **Sources:** 8-K 2026-07-28 Item 5.02; 10-Q Note 15; `litigation/LIT-002_calder-ip-ownership.md` docket 2026-07-30, 2026-08-20, 2026-09-14. Supporting: SEC-008, LIT-011.
- **Severity:** High. A cooperation agreement is needed; divergent interests (inference) weaken the defense in X-009.
- **Confidence:** Medium. Facts are records; the reason for separate counsel is not stated.
- **Deal impact:** Condition: binding litigation cooperation and IP confirmation agreement from Dr. Reyes-Barrow before signing.

### X-011: Aura battery hazard is larger than the "contained, fully reserved" US$6.0m program
- **Finding:** The US$6.0m reserve covers mailing battery isolation kits for 1.62m Aura AT-200/AT-210 units (1.62m x US$3.70). 23% of kits sent had been installed by July 31 (CPSC staff, citing Delmora data). CPSC staff (letter dated August 28, 2026) made a preliminary substantial-hazard finding and seek a refund or free replacement at the owner's choice. Incident counts rose from 214 reports / 37 fires / 9 burn injuries in the 10-Q (filed August 6) to 296 / 52 / 11 in the CPSC letter. The March 1, 2026 insurance renewal halved the per-occurrence limit to US$25.0m and excludes battery thermal events in products made before January 1, 2024, which appears to cover the Aura units made 2021-2023; the insurer has acknowledged notice with a full reservation of rights. A consolidated class seeks refunds for all 1.62m units plus punitive damages; the motion to dismiss hearing is November 18, 2026. Plaintiffs allege an internal tracker logged 58 incidents by end 2024 (allegation, one former engineer). Disclosure timeline: January 14, 2026 "a small number of reports"; February 26 10-K "limited number ... not material"; March 1 exclusion; April 21 field action.
- **Numbers (recomputed):** 1.62m x 119 = up to US$192.8m at full refund uptake, gross of the 5.1 reserve (12.5% of EV; replacement cost not in the data room); 25% uptake 48.2; 50% uptake 96.4. Reaching 10% of EV (154.3) needs about 80% refund uptake (1.30m units); kit uptake so far is 23%.
- **Sources:** 10-Q Notes 6, 7, 12, 15; 10-K Item 3; `litigation/LIT-001_aura-battery-class-action.md`; `news/2026-09-08_consumer-safety-wire_cpsc-refund-push.md`; `news/2026-01-14_wcov-columbus-news_thermostat-kitchen-fire.md`; `balance_sheet.csv` row 17. Supporting: SEC-011, SEC-012, SEC-013, SEC-014, LIT-001, LIT-008, LIT-009, LIT-010, NEWS-001, NEWS-002, NEWS-003, NEWS-004, FIN-039.
- **Severity:** High. Specific indemnity or escrow needed; claims appear excluded from cover. Not rated Critical: the 10% test needs about 80% refund uptake, and no uptake estimate is in the data room. NEWS-001 keeps its own Critical rating.
- **Confidence:** Medium. Reserve, insurance and counts are primary or regulator figures; remedy and uptake are open.
- **Deal impact:** Specific indemnity or escrow sized to a recall scenario; MAE definition; pre-signing CPSC strategy.

### X-012: Pittock groundwater contamination has moved off site, overtaking the low-end accrual
- **Finding:** At FY2025 Delmora accrued US$9.0m, the low end of a US$9.0m to US$71.0m range, and named groundwater moving "beyond the site boundary" as the swing factor. On about September 22, 2026 Ohio EPA confirmed TCE above the federal limit in two off-site wells in Linden Park, ordered vapor intrusion sampling at about 60 homes by November 30 and a plume plan by December 15, and will evaluate off-site remedies. 42 residents (putative class of about 600 households) sued Delmora and Pittock on September 17, claiming US$45.0m plus medical monitoring and punitive damages. The reserve on the balance sheet is US$8.7m.
- **Numbers:** Unaccrued range 71.0 - 9.0 = 62.0; plus the claim 45.0 = 107.0 (6.9% of EV) before monitoring, punitive damages and any remedy beyond the range.
- **Sources:** 10-K Note 15 and Item 3; `litigation/LIT-004_marlow-groundwater.md`; `news/2026-09-24_marlow-courier_plume-off-site.md`; `balance_sheet.csv` row 25. Supporting: SEC-022, LIT-004, LIT-013, NEWS-016, NEWS-017, FIN-036.
- **Severity:** High. Dated judgment (accrual as of December 31, 2025) now in doubt; needs an environmental indemnity or escrow.
- **Confidence:** High for the facts; liability amounts are open.
- **Deal impact:** Environmental indemnity or escrow; sampling results as a pre-signing deliverable.

### X-013: IRS challenge to the 2019 Irish IP transfer exceeds the tax reserve by about US$106.9m
- **Finding:** A May 2026 NOPA values the AdaptiveComfort rights moved to Ireland at US$476.0m, not US$64.0m: tax about US$86.5m plus a 40% penalty of about US$34.6m, plus interest. The UTP liability is US$14.2m. The 10-K (February 26) said no significant UTP change was expected within 12 months. The deal brief assumes no tax exposure beyond recorded reserves. Delmora has filed a protest with IRS Appeals and believes its position is more likely than not to be sustained (10-Q Note 10). The same rights are claimed by Calder (X-009).
- **Numbers:** 86.5 + 34.6 = 121.1 (7.8% of EV, 9.4% of equity); 121.1 - 14.2 = 106.9 unreserved if all of the UTP relates to it (not stated). Interest not given.
- **Sources:** 10-Q Note 10; 10-K Item 1 and Note 12; `balance_sheet.csv` row 24. Supporting: SEC-009, SEC-010, FIN-035.
- **Severity:** High. Tax indemnity or escrow needed. Interest could take it above 10% of equity but cannot be shown from the data room.
- **Confidence:** High.
- **Deal impact:** Specific tax indemnity or escrow.

### X-014: Public statements and dated judgments overtaken within weeks to months
- **Finding:** Several statements in filings and investor communications were overtaken soon after, or were made while contrary facts were known internally:

  | Statement (date) | What followed or was known |
  |---|---|
  | 10-K: Aura "limited number of consumer reports", "not material" (Feb 26, 2026) | Insurance exclusion Mar 1 (3 days later); field action on 1.62m units Apr 21 (54 days); alleged 58 internal incidents by end 2024 (allegation) |
  | 10-K: "not aware of any violations of export control or sanctions laws" (Feb 26) | Audit Committee trade compliance meetings Jan 20, Feb 9, Feb 23; BIS subpoena Jun 24 |
  | 10-K: "We believe we own all intellectual property that is material" (Feb 26) | Calder suit Apr 9 (42 days); March 6, 2017 priority date during Calder fellowship |
  | 10-K: no significant UTP change expected in 12 months (Feb 26) | IRS NOPA in May for US$121.1m |
  | 10-K: environmental accrual at the low end, US$9.0m (as of Dec 31, 2025) | Off-site TCE confirmed about Sep 22, 2026 |
  | Q4 2025: warranty accrual rate cut; 10-K credits "lower warranty expense" (Feb 26) | Claim rate 3.4% FY2025 to 4.7% H1 2026 |
  | 10-Q: earn-out change of control "not probable" (as of Jun 30, 2026) | Strategic review including a possible sale running since Mar 11, 2026 |
  | 10-Q: "We expect to be selected" by WSEA (filed Aug 6) | WSEA awarded to Thermiq Jul 21 (16 days before filing) |
  | 8-K: CTO departure "not the result of any disagreement" (Jul 28) | Co-defendant in Calder; separate counsel Aug 20 |

- **Sources:** As listed; see X-003, X-007, X-009, X-010, X-011, X-012, X-013. Supporting: SEC-005, SEC-007, SEC-010, SEC-014, SEC-015, SEC-025, SEC-028, NEWS-003.
- **Severity:** High. Management representations need strong warranties, a specific indemnity regime and confirmatory diligence; management answers should not be relied on without documents.
- **Confidence:** High for the dated statements. What management knew at each date is inference.
- **Deal impact:** Representations, warranty insurance exclusions likely; 10b-5 exposure for the public company before closing, and warranty insurance exclusions likely (inference, for counsel). The goodwill impairment test date is not in the data room, so that judgment cannot be tested.

### X-015: Revenue durability is weakening across streams
- **Finding:** Two at-risk customers account for US$134.6m (17.1%) of FY2025 revenue: WSEA (US$96.0m, contract ends December 31, 2026, re-award lost) and Gulf Horizon (US$38.6m; inference that it is the UAE distributor whose shipments were suspended in June 2026). Underneath: Devices growth slowed to 0.8% in H1 2026 (4.2%, 3.8%, 2.9% before); Utility Programs growth slowed from 16.7% to 4.3%; Care revenue excluding Insights grew 6.2% in H1 2026 while subscribers grew 16.1% in FY2025 and 6.9% from December 2025 to June 2026 (implied revenue per subscriber US$110.0 in FY2024 to US$101.9 in H1 2026 annualized); revenue outside the top 8 customers fell 1.3% in FY2025. Mitigant: subscription gross retention stable at about 93% (FIN-026).
- **Numbers:** 96.0 + 38.6 = 134.6; 134.6 / 786.0 = 17.1%. H1 2026 growth excluding Insights 2.5%.
- **Sources:** `revenue_by_customer.csv`; `income_statement.csv`; `revenue_quarterly.csv`; `kpis.csv`; components X-003, X-007. Supporting: FIN-019, FIN-022, FIN-025, FIN-027, FIN-041.
- **Severity:** High. The trend undermines thesis points 1, 3 and 4. (The Critical element, WSEA, is rated in X-003.)
- **Confidence:** High.
- **Deal impact:** Rebase revenue plan; price.

### X-016: Gross margin is falling and the 42% assumption is unsupported
- **Finding:** Gross margin fell from 42.5% (FY2025) and 42.3% (H1 2025) to 39.4% in H1 2026. FY2025's peak was helped by a weak peso and the warranty accrual cut (41.8% normalized). Peso hedging stopped in Q3 2025 (hedge coverage 72% to 0%); 63% of cost of revenue is in pesos; the peso strengthened from 19.4 to 17.2. The company's sensitivity is about US$28m of cost per 10% strengthening. The JV assembler gave a 14% wage rise after the August strike. Warranty claims rose to 4.7%.
- **Numbers:** 155.2 / 394.0 = 39.4%. Peso move 19.4 / 17.2 - 1 = 12.8%; 28 x 1.28 = about US$35.8m a year (projection, linear). Gap to 42%: 0.9 points on LTM (41.1%, US$7.4m) to 2.6 points at the H1 2026 margin (US$21.0m). The 41.8% normalized figure assumes warranty sits in cost of revenue, which the data room does not state.
- **Sources:** 10-K MD&A "Foreign currency"; 10-Q MD&A "Results"; `income_statement.csv`; `kpis.csv` rows 8-9, 16-18; `news/2026-02-27_smart-home-insider_q4-results-insights-launch.md` para 4; `news/2026-09-15_monterrey-economia_ensamble-norte-payment.md` para 4. Supporting: SEC-016, FIN-017, FIN-018, NEWS-023, NEWS-015.
- **Severity:** High.
- **Confidence:** High on history; Medium on the forward view.
- **Deal impact:** Price (margin assumption), hedging policy at close.

### X-017: Financing does not cover the change-of-control cash calls
- **Finding:** The sources and uses in the deal brief (TLB US$900.0m, company cash US$100.0m, sponsor equity about US$703.8m before fees) leave out two payments this transaction triggers: pension funding (US$230.5m within 120 days after closing) and the Nimbus earn-out (US$90.0m within ten business days). NEO severance (up to US$21.6m at US$18.70, including accelerated equity) is double-trigger, so it is contingent on termination. With the two cash calls, uses rise from US$1,703.8m to US$2,024.3m and sponsor equity to US$1,024.3m (+45.5%). The TLB is 6.9x company Adjusted EBITDA, 7.8x Case B, and 9.0x Case B less WSEA at the company average margin (10.4x at an assumed 30% margin; assumption). June 30 cash of US$160.4m includes the WSEA advance and the payables stretch: after the US$100.0m use, cash is US$60.4m, US$26.4m once the advance unwinds by December 31, 2026, and -US$30.7m if payables return to 78 days (projection, before H2 operating cash flow; H2 2025 free cash flow was US$36.0m). An undrawn US$150.0m revolver exists today (10-K, 10-Q); its status after refinancing is unknown.
- **Numbers (recomputed):** 1,283.8 + 420.0 + 230.5 + 90.0 = 2,024.3; 2,024.3 - 1,000.0 = 1,024.3; 1,024.3 / 703.8 - 1 = 45.5%. 900.0 / 115.4 = 7.80x; 900.0 / 99.9 = 9.01x; 160.4 - 100.0 - 34.0 = 26.4.
- **Sources:** deal-brief.md section 1; 10-K Note 11 and MD&A Liquidity; 8-K 2026-05-14; Proxy "Change-of-control severance"; 10-Q Liquidity; `balance_sheet.csv`; `cash_flow.csv`; `adjusted_ebitda_reconciliation.csv`. Supporting: FIN-014, FIN-015, FIN-042, FIN-044, FIN-048, FIN-067, FIN-068, FIN-069, SEC-040.
- **Severity:** High. Calibration: a gap to be solved in the financing at closing, not a default or liquidity problem before signing or closing.
- **Confidence:** Medium (arithmetic High; the cash path is a projection).
- **Deal impact:** Re-size equity or price; check the TLB EBITDA definition and minimum liquidity; keep a revolver.

### X-018: Rebased valuation is far below US$24.50 (projection)
- **Finding:** Rebuilding net debt with debt-like items gives US$699.2m before contingencies, against US$259.6m in the deal brief: change-of-control cash calls US$320.5m (pension termination shortfall 230.5, which replaces the 151.0 accounting deficit; Nimbus 90.0, against the 8.0 carrying value the brief's net debt leaves out), normalization US$91.1m (excess payables 57.1, WSEA advance 34.0) and recorded reserves US$28.0m (UTP 14.2, environmental 8.7, field action 5.1). Contingent exposures add US$43.1m to US$468.8m (IRS up to 106.9 above reserve before interest; environmental about 107.0 plus unquantified items; EC cap 78.6; Ensamble guarantee 63.4; Aura net 43.1 to 91.3 at 25% to 50% refund uptake; severance up to 21.6). At the deal multiple of 11.84x:

  | Case | EBITDA | EV | Equity | Per share |
  |---|---|---|---|---|
  | Company base, only the pension and Nimbus cash calls deducted (320.5) | 130.4 | 1,543.4 | 963.3 | 18.38 |
  | Case B, full bridge (699.2) | 115.4 | 1,366.3 | 667.1 | 12.73 |
  | Case B less WSEA at the company average margin (15.5), full bridge | 99.9 | 1,182.7 | 483.5 | 9.23 |
  | Case B less WSEA at an assumed 30% margin (28.8), full bridge | 86.6 | 1,025.3 | 326.1 | 6.22 |

  Even the simplest case (management's EBITDA, only the two contractual cash calls) is below the US$18.70 unaffected price. Not included: Calder royalty (upper bound US$20.2m a year on LTM Devices revenue), peso cost not yet in LTM (US$17.0m to US$18.7m a year: run rate 2 x 17.1 = 34.1 or the 10-K sensitivity 35.8, less the 17.1 already in H1 2026; projection), Gulf Horizon loss. Case B (130.4 - 6.0 - 3.2 - 5.8) does not deduct the peso or Gulf Horizon effects, so these would be additional. The 5.1 field action reserve in the bridge partly overlaps the 6.0 Aura add-back removed from EBITDA (small).
- **Numbers (recomputed by lead):** 1,543.4 - 259.6 - 320.5 = 963.3; / 52.4 = 18.38. 11.84 x 115.4 = 1,366.3; - 699.2 = 667.1; / 52.4 = 12.73. 96.0 x 16.16% = 15.5; 115.4 - 15.5 = 99.9; x 11.84 = 1,182.7; - 699.2 = 483.5; / 52.4 = 9.23. 11.84 x 86.6 = 1,025.3; - 699.2 = 326.1; / 52.4 = 6.22. 320.5 / 1,543.4 = 20.8% of EV.
- **Sources:** FIN-065, FIN-066 (iteration 2 report, as corrected by the verifier); deal-brief.md section 1; X-001 to X-005, X-013. Supporting: FIN-013, FIN-016, FIN-056, FIN-065, FIN-066.
- **Severity:** Critical. Test: more than 10% of value. The two contractual cash calls alone are US$320.5m (20.8% of EV); the Case B rebased value is 48.0% below the offer.
- **Confidence:** Medium. Cash calls are High; margin and uptake inputs are assumptions; applying 11.84x to a smaller, more concentrated base is generous (inference).
- **Deal impact:** The current price is not supported on the data room; re-price or pause.

### X-019: Named parties and their revenue rank
| Party | Role | Revenue rank and amount (FY2025) |
|---|---|---|
| Western States Energy Alliance | Customer (utility program) | Rank 1, US$96.0m (12.2%) |
| HomeCrest Stores | Customer (retail) | Rank 2, US$84.0m (10.7%) |
| Parcelline Marketplace | Customer (online) | Rank 3, US$66.5m (8.5%) |
| Gulf Horizon Trading FZE | Customer (UAE distributor) | Rank 4, US$38.6m (4.9%) |
| Cascadia Power & Light | Customer (utility) | Rank 5, US$23.5m (3.0%) |
| Vierhaus Elektro GmbH | Customer (German-named; EU distributor role is an inference) | Rank 6, US$19.0m (2.4%); possibly relevant to the EC case (inference) |
| Northway Electronics | Customer | Rank 7, US$16.8m (2.1%) |
| Bellmark Mutual Insurance | Customer (Insights partner) | Rank 8, US$1.9m (0.2%) |
| Thermiq Energy | Competitor (won WSEA) | Not a listed customer |
| Ensamble Norte / Grupo Industrial Arceo | JV assembler / JV partner | Not listed customers; Ensamble is a supplier with US$212.0m of FY2025 purchases (10-K) |
| Calder Institute of Technology | Plaintiff | Not a listed customer |
| Harborline Specialty | Insurer | Not a listed customer |
| Open Firmware Conservancy | Plaintiff | Not a listed customer |
| Brennan Sales Group | Former claimant (dismissed) | Not a listed customer |
| Tarnwood Capital (6.2%), Broadleaf Index Funds (9.1%) | Shareholders | Not customers |
| Pruett plaintiffs, Colorado AG, Ohio EPA, CPSC, BIS, IRS, FTC, European Commission | Litigants and regulators | Not customers |
| Distribution Workers United Local 88 | Reno CBA counterparty | Not a listed customer |
| Pellbrook & Stroud LLP | Auditor | Not a listed customer |
| Nimbus former securityholders and representative | Earn-out counterparty | Not listed customers |
| Pittock retiree group | Pension claimant (news) | Not a listed customer |
- **Source:** `revenue_by_customer.csv` rows 1-8 (only 8 customers listed); FIN-029.
- **Severity:** Low. **Confidence:** High.

### X-020: The deal model's management assumptions do not survive the data room
| Brief assumption (section 4 unless noted) | Finding |
|---|---|
| Earnings base US$130.4m as reported | About US$115.4m (X-004) |
| Net debt US$259.6m, no working capital normalization | US$98.0m timing in cash (X-005) |
| Pension: no ERISA contributions before 2029, no adjustment | US$230.5m due within 120 days of closing (X-001) |
| Nimbus earn-out US$8.0m | US$90.0m due on closing (X-002) |
| Aura: US$6.0m, fully reserved, contained | CPSC staff seek refund or replacement on 1.62m units; claims appear excluded from cover (X-011) |
| Litigation without merit or immaterial | Calder, Colorado AG, Pruett, EC, OFC pending (X-008, X-009, X-012) |
| Tax: no exposure beyond reserves | US$121.1m NOPA vs US$14.2m (X-013) |
| Gross margin 42% from 2027 | 39.4% in H1 2026, unhedged peso (X-016) |
| Section 3: WSEA renews on similar terms | Awarded to Thermiq (X-003) |
| Section 3: Middle East growth | Shipments suspended, BIS subpoena (X-007) |
- All 8 section 4 assumptions are contradicted at least in part; only the 23% effective tax rate within the tax row holds (FIN-045). **Severity:** High. **Confidence:** High. **Sources:** deal-brief.md sections 3-4 and the X- findings cited.
