## News and media analyst: findings

### Files reviewed

I read all 13 articles in full in `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/news/`, plus `targets/kestrel/data/deal-brief.md` for context. Paragraph numbers below count the body paragraphs after the byline.

| # | File | Outlet (type) | Source reliability |
|---|---|---|---|
| 1 | `2025-11-06_triangle-commerce-ledger_durham-lab-opening.md` | Triangle Commerce Ledger (regional business paper) | Medium-High. On-record CEO quote and a company statement. |
| 2 | `2026-01-15_lab-industry-insider_compliance-chief-exit.md` | Lab Industry Insider (trade) | Medium. Departure based on an internal memo. The concerns come from two anonymous former employees and were not confirmed. |
| 3 | `2026-02-20_healthcare-compliance-monitor_doj-genetic-testing-probe.md` | Healthcare Compliance Monitor (newsletter, staff report) | Low. Two anonymous sources. The article itself says the report is unconfirmed. |
| 4 | `2026-03-06_capital-street-wire_record-2025-results.md` | Capital Street Wire (financial newswire) | High. Reported results and on-record earnings call quotes. |
| 5 | `2026-04-22_lab-industry-insider_ransomware-attack.md` | Lab Industry Insider (trade) | Medium for the outage (several practices, plus a company statement). Low for the data theft claim (criminal leak site, not verified). |
| 6 | `2026-05-19_capital-street-wire_bearhaven-short-report.md` | Capital Street Wire (financial newswire) | High that the report exists and that the company denied it. Low for the claims themselves (an interested short seller citing unnamed former employees). |
| 7 | `2026-06-14_triangle-commerce-ledger_charity-5k.md` | Triangle Commerce Ledger | High, but not relevant. |
| 8 | `2026-07-30_healthcare-policy-daily_cms-lab-fee-schedule.md` | Healthcare Policy Daily (trade) | High. Reports a published CMS final rate. |
| 9 | `2026-08-06_capital-street-wire_guidance-cut.md` | Capital Street Wire (financial newswire) | High. Company guidance and on-record CFO remarks. |
| 10 | `2026-08-27_pharma-pipeline-news_veltrane-halts-atlas-3.md` | Pharma Pipeline News (trade) | High for Veltrane's own announcement. It does not name Corvane. |
| 11 | `2026-09-03_fda-enforcement-roundup_corvane-laboratories-pty.md` | FDA Enforcement Roundup (newsletter) | High. FDA action, and the company confirmed it is a different entity. |
| 12 | `2026-09-17_supply-chain-health_sequencing-reagent-tariffs.md` | Supply Chain Health (trade) | Medium. The tariff is a fact. The contract protection is a company statement only. |
| 13 | `2026-10-05_capital-street-wire_halvard-take-private-talks.md` | Capital Street Wire (financial newswire) | Medium for the talks (anonymous sources). High for share prices. |

**Embedded instructions:** none found. No article contains text that tries to instruct the agents.

### Timeline

| Date | Event | Outlet | Fact / Allegation / Rumor |
|---|---|---|---|
| Nov 6, 2025 | Durham lab (the 7th) opens with 120 jobs. Start-up costs are to be reported outside Adjusted EBITDA. | Triangle Commerce Ledger | Fact |
| 2025 (undated) | CCO Pruitt reportedly raised internal concerns about the physician speaker program | Lab Industry Insider | Rumor |
| Jan 15, 2026 | CCO Daniel Pruitt leaves. The Deputy GC becomes interim compliance chief. | Lab Industry Insider | Fact (memo; company did not deny) |
| 2nd week of Feb 2026 | Corvane reportedly receives a DOJ civil investigative demand (CID) covering billing since 2019 and speaker events | Healthcare Compliance Monitor (Feb 20) | Rumor |
| Mar 6, 2026 | Record FY2025: revenue US$431.0m (+11.7%), Adj. EBITDA US$125.3m (+25.4%), Q4 revenue US$120.5m. CFO cites a "refinement of our collection estimates". Shares +6.4% to US$22.30. | Capital Street Wire | Fact |
| Apr 18, 2026 | Labs unable to process most samples (reported as ransomware) | Lab Industry Insider (Apr 22) | Fact (outage); cause per physicians |
| Apr 21, 2026 | Ransomware group claims it took 1.1 TB of files, including patient results | Lab Industry Insider | Rumor / criminal claim |
| May 19, 2026 | Bearhaven short report: kickbacks, test stacking, Q4 estimate change, receivables growth. Corvane: "false and misleading". Shares -11.2% to US$17.85. | Capital Street Wire | Allegation |
| Jun 14, 2026 | Corvane Hope 5K raises US$410,000 | Triangle Commerce Ledger | Fact (noise) |
| Jun 30, 2026 | Deal team model built (per the deal brief) | Deal brief | Fact |
| Jul 30, 2026 | CMS final 2027 lab fee schedule cuts OncoTrace code 0419U from US$2,150 to US$1,505 (-30%), effective Jan 1, 2027 | Healthcare Policy Daily | Fact |
| Jul 31, 2026 | Close of US$18.10, the deal brief's premium reference | Deal brief / Capital Street Wire | Fact |
| Aug 5-6, 2026 | FY2026 guidance cut: Adj. EBITDA to US$100-106m (from 134-140), revenue to US$405-415m (from 455-465). Q2 revenue -3.0% to US$100.8m. Shares -31.2% to US$12.45. | Capital Street Wire | Fact |
| Aug 27, 2026 | Veltrane halts ATLAS-3, cuts 40% of staff, will close sites by Q1 2027 and "wind down vendor contracts" | Pharma Pipeline News | Fact (about Veltrane) |
| Sep 3, 2026 | FDA warning letter to Corvane Laboratories Pty Ltd (Australia), which is not affiliated | FDA Enforcement Roundup | Fact (different entity) |
| Sep 17, 2026 | 25% tariff on sequencing reagents from Oct 1, 2026. Corvane says its Helixor contract fixes prices including duties through 2028. | Supply Chain Health | Fact (tariff); company statement (contract) |
| Sep 30, 2026 | Tighter leverage test under the existing credit agreement (per analyst question) | Capital Street Wire (Aug 6) | Fact that a test exists; result not found |
| Oct 2, 2026 | Shares close at US$13.10 | Capital Street Wire | Fact |
| Oct 5, 2026 | Leak: Halvard in exclusive talks at about US$24 a share; special committee formed. Shares +9.2% to US$14.30. | Capital Street Wire | Rumor (anonymous); prices are fact |

### Findings

#### NEWS-001: FY2026 Adjusted EBITDA guidance cut far below the deal model
- **Finding:** Corvane cut FY2026 Adj. EBITDA guidance to US$100-106m. The new midpoint of US$103.0m is US$34.0m (24.8%) below the US$137.0m used in the deal model, and 17.8% below FY2025's US$125.3m. Revenue guidance fell to US$405-415m. The midpoint of US$410.0m is 10.9% below the old midpoint and 4.9% below FY2025 revenue of US$431.0m.
- **Evidence:** "cut its FY2026 Adjusted EBITDA outlook to US$100 to 106 million from US$134 to 140 million"
- **Source:** `targets/kestrel/data/news/2026-08-06_capital-street-wire_guidance-cut.md` para 1 (Capital Street Wire, Aug 6, 2026)
- **Claim type:** Fact
- **Severity:** Critical. Test: changes value by more than 10%. The model's FY2026 EBITDA falls 24.8%. At the proposed EV of US$1,648.6m, the implied multiple rises from 12.0x on the US$137.0m model figure to 16.0x on US$103.0m (recomputed).
- **Confidence:** High. Company guidance reported by a financial newswire.
- **Deal impact:** Valuation. The deal brief (dated Oct 12) still uses the stale US$137.0m.
- **Cross-check:** Q2 2026 10-Q and the Aug 2026 8-K earnings release (Item 2.02) for the exact guidance. Quarterly financials for H1 2026 actuals.

#### NEWS-002: The guidance range sits entirely below the term loan's US$110.0m LTM EBITDA condition
- **Finding:** Even the top of the new guidance range (US$106m) is below the commitment letter's US$110.0m LTM Adjusted EBITDA closing condition. LTM at a Q2 2027 closing will include Q1 2027, the first quarter under the cut Medicare rate (inference). Leverage is also affected: the US$750.0m term loan equals 7.3x the US$103.0m guidance midpoint, against the planned 6.0x (recomputed).
- **Evidence:** "Adjusted EBITDA outlook to US$100 to 106 million" (guidance article, para 1). The condition comes from deal brief section 3.
- **Source:** `targets/kestrel/data/news/2026-08-06_capital-street-wire_guidance-cut.md` para 1; `targets/kestrel/data/deal-brief.md` section 3
- **Claim type:** Fact (guidance). The effect on LTM at closing is an inference.
- **Severity:** Critical. Test: could block closing. US$106m at the top of guidance is less than the US$110.0m condition.
- **Confidence:** Medium. The numbers are on record, but LTM at closing is a projection.
- **Deal impact:** Closing risk and financing.
- **Cross-check:** Financials (quarterly Adj. EBITDA, LTM build). The credit agreement and commitment letter definition of Adjusted EBITDA (which add-backs are allowed).

#### NEWS-003: Existing credit agreement leverage test at September 30, 2026 is unresolved
- **Finding:** Analysts asked whether Corvane would pass a tighter leverage test at the end of September. The CFO declined to give a leverage figure. The result is not found in news coverage.
- **Evidence:** "Corvane 'has a constructive relationship with its lenders' and declined to give a leverage figure."
- **Source:** `targets/kestrel/data/news/2026-08-06_capital-street-wire_guidance-cut.md` para 3 (Capital Street Wire, Aug 6, 2026)
- **Claim type:** Fact (the question and the answer). A breach is not reported.
- **Severity:** High. Escalate to Critical if the filings show a breach, waiver or default before signing, which would be a pre-signing liquidity or default issue.
- **Confidence:** Medium. The CFO's evasive on-record answer is a warning sign but not proof of a breach.
- **Deal impact:** Closing risk and balance sheet stability (IC question 4).
- **Cross-check:** Credit agreement covenant step-downs in the 10-K. Q3 2026 10-Q covenant disclosure. Any 8-K for an amendment or waiver (Item 1.01 or 2.04).

#### NEWS-004: CMS cuts the OncoTrace Medicare rate by 30% from January 1, 2027
- **Finding:** CMS's final 2027 fee schedule cuts code 0419U (the 84-gene OncoTrace panel) from US$2,150 to US$1,505, which is -US$645 or -30.0% per test (recomputed). Commercial contracts priced off Medicare will also reprice. The deal model assumes flat Medicare rates through 2030.
- **Evidence:** "falls from US$2,150 to US$1,505, a cut of 30%. The new rate takes effect on January 1, 2027."
- **Source:** `targets/kestrel/data/news/2026-07-30_healthcare-policy-daily_cms-lab-fee-schedule.md` paras 1 and 3 (Healthcare Policy Daily, Jul 30, 2026)
- **Claim type:** Fact (CMS final schedule). The commercial repricing point comes from an unnamed consultant.
- **Severity:** High. Rate it Critical if the financials show that OncoTrace Medicare revenue plus Medicare-linked commercial revenue is large enough for a 30% cut to move value by more than 10%. OncoTrace revenue share is not found in news coverage.
- **Confidence:** High. Published final rate, and rates "can be reconsidered only in limited circumstances" (para 2).
- **Deal impact:** Valuation. The flat-rate assumption in deal brief section 6 is stale.
- **Cross-check:** Financials for revenue by product and payer and OncoTrace volume. 10-K risk factors on PLA code and gapfill pricing. Payer contracts tied to the Medicare rate.

#### NEWS-005: Management did not quantify the Medicare cut when it cut guidance
- **Finding:** On the Aug 6 call, one week after the CMS final rate, management declined to size the 2027 effect.
- **Evidence:** "Management did not quantify the effect of the new Medicare rate for OncoTrace, saying it would apply only from 2027."
- **Source:** `targets/kestrel/data/news/2026-08-06_capital-street-wire_guidance-cut.md` para 3
- **Claim type:** Fact
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Disclosure quality (IC question 5) and valuation.
- **Cross-check:** Q2 2026 10-Q MD&A, known trends and uncertainties: does it discuss the 0419U rate?

#### NEWS-006: Veltrane halts its lead Phase 3 trial and will wind down vendor contracts
- **Finding:** Veltrane stopped ATLAS-3 for futility, will close sites by Q1 2027, cut about 40% of staff, and will "wind down vendor contracts". The article does not name Corvane. The deal model assumes full conversion of the Veltrane backlog, so that assumption is likely impaired (inference).
- **Evidence:** "It did not name its trial vendors, but said it would 'wind down vendor contracts in an orderly way.'"
- **Source:** `targets/kestrel/data/news/2026-08-27_pharma-pipeline-news_veltrane-halts-atlas-3.md` paras 1-2 (Pharma Pipeline News, Aug 27, 2026)
- **Claim type:** Fact about Veltrane. The link to Corvane's backlog is an inference from the deal brief.
- **Severity:** High
- **Confidence:** Medium. The Veltrane announcement is on record, but the Corvane exposure is not found in news coverage.
- **Deal impact:** Valuation. Backlog quality behind the US$246.0m year-end 2025 backlog.
- **Cross-check:** Financials for backlog and revenue by customer (Veltrane rank and amount). 10-K backlog and customer concentration. Q3 10-Q or 8-K disclosure of the cancellation. Contract termination fee terms.

#### NEWS-007: DOJ civil investigative demand reportedly received in February 2026
- **Finding:** Anonymous sources say Corvane received a DOJ CID in the second week of February 2026. It reportedly covers Medicare billing for hereditary cancer panels since 2019 and physician speaker events. A CID may signal a sealed qui tam False Claims Act case. Timing flag: the FY2025 results came on Mar 6, 2026, so the FY2025 10-K was likely filed after the reported CID date (inference). Check whether it discloses the CID.
- **Evidence:** "Corvane Diagnostics received a demand 'in the second week of February' covering billing since 2019 and the company's physician speaker events."
- **Source:** `targets/kestrel/data/news/2026-02-20_healthcare-compliance-monitor_doj-genetic-testing-probe.md` paras 1-3 (Healthcare Compliance Monitor, Feb 20, 2026)
- **Claim type:** Rumor. Corvane did not respond and DOJ declined to comment.
- **Severity:** High. False Claims Act exposure covering seven-plus years of billing on the flagship product would need a specific indemnity or escrow if confirmed.
- **Confidence:** Low. Anonymous sources, not confirmed.
- **Deal impact:** Valuation, post-closing liability, reputation.
- **Cross-check:** FY2025 10-K legal proceedings and contingencies notes, and the 10-K filing date against mid-February. Q1 and Q2 10-Q. Litigation dockets for unsealed qui tam complaints.

#### NEWS-008: Chief Compliance Officer departure in January 2026
- **Finding:** CCO Daniel Pruitt left after about three years, and the Deputy General Counsel became interim compliance chief. No 8-K was required, because he is not an executive officer.
- **Evidence:** "leaving 'to pursue other opportunities' and that the Deputy General Counsel would serve as interim compliance chief."
- **Source:** `targets/kestrel/data/news/2026-01-15_lab-industry-insider_compliance-chief-exit.md` paras 1 and 3 (Lab Industry Insider, Jan 15, 2026)
- **Claim type:** Fact (internal memo seen by the outlet; Corvane did not deny it)
- **Severity:** Medium. The timing is about one month before the reported CID.
- **Confidence:** Medium. Single trade source citing a memo.
- **Deal impact:** Governance and controls (IC question 5).
- **Cross-check:** 10-K or proxy description of the compliance function. Whether a permanent CCO was hired. Board minutes in confirmatory diligence.

#### NEWS-009: Former CCO reportedly raised internal concerns about the speaker program
- **Finding:** Two unnamed former employees say Pruitt raised concerns in 2025 about how the physician speaker program was managed. Corvane said it "does not comment on personnel matters".
- **Evidence:** "Mr. Pruitt had raised concerns internally in 2025 about how the company's physician speaker program was managed. Lab Industry Insider could not confirm those accounts."
- **Source:** `targets/kestrel/data/news/2026-01-15_lab-industry-insider_compliance-chief-exit.md` para 2
- **Claim type:** Rumor
- **Severity:** High. A possible whistleblower or qui tam relator.
- **Confidence:** Low. Anonymous and unconfirmed.
- **Deal impact:** Post-closing liability, reputation.
- **Cross-check:** Litigation dockets (qui tam relator, employment or retaliation claims). 10-K contingencies. Hotline and audit committee records.

#### NEWS-010: Ransomware outage stopped most sample processing from April 18, 2026
- **Finding:** Labs could not process most samples from Apr 18. Oncology practices were told to send samples elsewhere. The duration is not found in news coverage. Q2 2026 revenue later fell 3.0% (NEWS-001 source). A causal link is an inference.
- **Evidence:** "unable to process most samples since April 18... Several oncology practices told Lab Industry Insider they had been asked to send samples to other labs."
- **Source:** `targets/kestrel/data/news/2026-04-22_lab-industry-insider_ransomware-attack.md` paras 1 and 3 (Lab Industry Insider, Apr 22, 2026)
- **Claim type:** Fact (outage, plus the company's "working around the clock to restore systems"). The ransomware cause comes from physicians' offices.
- **Severity:** High. Customer leakage, lost volume, and a possible add-back of incident costs to Adj. EBITDA.
- **Confidence:** Medium. Several practices plus a company statement, single outlet.
- **Deal impact:** Valuation (lost revenue, physician defection), post-closing (remediation).
- **Cross-check:** 8-K Item 1.05 (material cybersecurity incident). It should have been filed within four business days of a materiality determination. Check whether one was filed and when. Q2 10-Q. Financials for April-May volumes and any cyber-cost add-back. Cyber insurance recoveries.

#### NEWS-011: Ransomware group claims theft of 1.1 TB, including patient results
- **Finding:** A ransomware group claimed on its leak site on Apr 21 that it took 1.1 TB of Corvane files, including patient test results, and set a payment deadline. Corvane declined to comment on the claim.
- **Evidence:** "claiming to have taken '1.1 terabytes' of Corvane files, including patient test results"
- **Source:** `targets/kestrel/data/news/2026-04-22_lab-industry-insider_ransomware-attack.md` paras 2-3
- **Claim type:** Rumor (claim by a criminal party; screenshots seen but not verified)
- **Severity:** High. HIPAA breach notification, OCR enforcement and class action exposure if confirmed.
- **Confidence:** Low. Unverified.
- **Deal impact:** Post-closing liability, reputation; possible indemnity.
- **Cross-check:** 8-K Item 1.05 and the 10-Q on data exfiltration. HHS breach portal filings. Litigation dockets for data breach class actions.

#### NEWS-012: Bearhaven claim 1: speaker fees to high-ordering oncologists (Anti-Kickback Statute)
- **Finding:** Bearhaven alleges that "speaker fees" averaging US$40,000 a year went to dozens of high-ordering oncologists. Corvane says the program "complies with all applicable laws". Shares fell 11.2% to US$17.85.
- **Evidence:** "paid 'speaker fees' averaging US$40,000 a year to dozens of high-ordering oncologists"
- **Source:** `targets/kestrel/data/news/2026-05-19_capital-street-wire_bearhaven-short-report.md` paras 1-2 (item 1), 3, 4 (Capital Street Wire, May 19, 2026)
- **Claim type:** Allegation (disclosed short seller; eight unnamed former employees; public Medicare data)
- **Severity:** High
- **Confidence:** Low. Interested party, not confirmed. It is consistent with NEWS-007 and NEWS-009 (see NEWS-016).
- **Deal impact:** Post-closing liability, reputation; indemnity or escrow.
- **Verifiable?** Yes, largely. CMS Open Payments data, Corvane speaker program spend, and ordering volumes by physician.
- **Cross-check:** 10-K contingencies and risk factors. Financials (speaker or marketing expense). Litigation dockets for securities suits after the 11.2% drop.

#### NEWS-013: Bearhaven claim 2: "test stacking" of the full OncoTrace panel
- **Finding:** Bearhaven alleges that sales staff pushed the full panel when a smaller test was appropriate.
- **Evidence:** "sales staff encouraged physicians to order the full OncoTrace panel when a smaller test was appropriate ('test stacking')"
- **Source:** `targets/kestrel/data/news/2026-05-19_capital-street-wire_bearhaven-short-report.md` para 2 (item 2)
- **Claim type:** Allegation
- **Severity:** High. Medical necessity and False Claims Act exposure on the flagship code, which falls within the reported CID scope (NEWS-007).
- **Confidence:** Low
- **Deal impact:** Post-closing liability; revenue quality.
- **Verifiable?** Partly. Test mix (full panel against smaller panels), payer denial reasons, and sales compensation plans. Hard to prove from public data alone.
- **Cross-check:** Financials (volume by test type, denials). Litigation dockets.

#### NEWS-014: Bearhaven claim 3: Q4 2025 revenue boosted by a change in collection estimates
- **Finding:** Bearhaven alleges that Q4 2025 revenue was "manufactured" by an estimate change while denials rose. This is partly supported on record: the CFO attributed the Q4 jump partly to "a refinement of our collection estimates" without giving an amount. Q4 revenue of US$120.5m was 16.4% above the Q1-Q3 2025 quarterly average of US$103.5m (recomputed from US$431.0m FY). The CEO said "collections have never been stronger."
- **Evidence:** "it reflected 'strong volumes and a refinement of our collection estimates.' She did not give an amount on the call." (Mar 6). Also: "fourth-quarter 2025 revenue was 'manufactured' by a change in collection estimates" (May 19).
- **Source:** `targets/kestrel/data/news/2026-03-06_capital-street-wire_record-2025-results.md` paras 1-2; `targets/kestrel/data/news/2026-05-19_capital-street-wire_bearhaven-short-report.md` para 2 (item 3)
- **Claim type:** Allegation. The fact that an estimate was changed is confirmed on record by the CFO.
- **Severity:** High. It goes to whether the US$125.3m FY2025 base (+25.4%) is recurring, and that base drives the 13.2x price and the 6.0x loan sizing.
- **Confidence:** Medium. Partly confirmed by the CFO statement; the size is unknown.
- **Deal impact:** Valuation (quality of earnings), IC question 1.
- **Verifiable?** Yes. The 10-K revenue note and critical accounting estimates (change in variable consideration or implicit price concession), quarterly revenue, and the denial rate trend.
- **Cross-check:** FY2025 10-K revenue recognition note. Financials (quarterly revenue, the size of the estimate change, denial rates). Does the 10-K quantify the change?

#### NEWS-015: Bearhaven claim 4: receivables growing much faster than revenue
- **Finding:** Bearhaven alleges that accounts receivable are outpacing revenue. No figures are given in the article.
- **Evidence:** "receivables are growing much faster than revenue."
- **Source:** `targets/kestrel/data/news/2026-05-19_capital-street-wire_bearhaven-short-report.md` para 2 (item 4)
- **Claim type:** Allegation
- **Severity:** Medium. Rate it High if DSO growth is confirmed, because it would support NEWS-014.
- **Confidence:** Low
- **Deal impact:** Valuation; working capital peg.
- **Verifiable?** Yes, directly. Balance sheet AR and DSO trend.
- **Cross-check:** Financials (AR, DSO, aging, cash conversion). 10-K balance sheet.

#### NEWS-016: Speaker program concern appears in three separate outlets
- **Finding:** The physician speaker program shows up in three separate reports: the former CCO's reported 2025 concerns (Jan), the reported CID scope (Feb), and Bearhaven's kickback claim (May). All three rest on anonymous or interested sources. They point the same way but none confirms the others.
- **Evidence:** "physician speaker program" (Jan 15 para 2); "the company's physician speaker events" (Feb 20 para 2); "'speaker fees' averaging US$40,000 a year" (May 19 para 2)
- **Source:** the three files cited in NEWS-009, NEWS-007 and NEWS-012
- **Claim type:** Rumor and Allegation (the pattern is my inference)
- **Severity:** High
- **Confidence:** Low-Medium. Three independent outlets, but none is on record.
- **Deal impact:** Post-closing liability; needs a specific indemnity or escrow if the filings or court records confirm any part.
- **Cross-check:** Litigation dockets (sealed or unsealed qui tam), 10-K contingencies, and the speaker program spend in the financials.

#### NEWS-017: Reported FY2025 results match the deal brief baseline
- **Finding:** FY2025 revenue of US$431.0m (+11.7%) and Adj. EBITDA of US$125.3m (+25.4%) match the deal brief. Original FY2026 revenue guidance was US$455-465m. Shares rose 6.4% to US$22.30.
- **Evidence:** "full-year revenue of US$431.0 million, up 11.7%. Adjusted EBITDA rose 25.4% to US$125.3 million."
- **Source:** `targets/kestrel/data/news/2026-03-06_capital-street-wire_record-2025-results.md` paras 1 and 3
- **Claim type:** Fact
- **Severity:** Low (the quality issues are in NEWS-014)
- **Confidence:** High
- **Deal impact:** Baseline only.
- **Cross-check:** FY2025 10-K and the Adj. EBITDA reconciliation in the financials.

#### NEWS-018: Take-private talks leaked; special committee formed
- **Finding:** Anonymous sources report exclusive talks at about US$24 a share and a special committee of independent directors. Both companies declined to comment.
- **Evidence:** "Corvane's board has formed a special committee of independent directors to consider the approach, one of the people said."
- **Source:** `targets/kestrel/data/news/2026-10-05_capital-street-wire_halvard-take-private-talks.md` paras 1 and 3 (Capital Street Wire, Oct 5, 2026)
- **Claim type:** Rumor
- **Severity:** Medium. The leak creates disclosure pressure and a public anchor at US$24.
- **Confidence:** Medium. Credible newswire, anonymous sources, and consistent with the deal brief.
- **Deal impact:** Process and closing risk (a public anchor makes a price cut harder).
- **Cross-check:** 8-K or Schedule 13D filings, and the proxy background of the merger.

#### NEWS-019: Deal brief premium is stale; US$24.00 is an 83.2% premium to the latest pre-leak price
- **Finding:** The brief computes a 32.6% premium on the Jul 31 close of US$18.10, which came before the Aug 6 guidance cut. The pre-leak close on Oct 2 was US$13.10. US$24.00 is 83.2% above that and 67.8% above the post-leak US$14.30 (recomputed). Shares are down from US$27.80 a year ago.
- **Evidence:** "Corvane shares closed at US$13.10 on Friday, October 2, before the report"
- **Source:** `targets/kestrel/data/news/2026-10-05_capital-street-wire_halvard-take-private-talks.md` para 2; `targets/kestrel/data/news/2026-08-06_capital-street-wire_guidance-cut.md` para 2; deal brief section 2
- **Claim type:** Fact
- **Severity:** High. The market has re-rated the stock after the guidance cut, Medicare cut and short report. The price needs revisiting (IC question 6).
- **Confidence:** High
- **Deal impact:** Valuation.
- **Cross-check:** Trading data in the financials, if available.

**Share price reaction summary (all from the cited articles):** +6.4% to US$22.30 (Mar 6, results); -11.2% to US$17.85 (May 19, Bearhaven); -31.2% to US$12.45 from US$18.10 (Aug 6, guidance cut); US$13.10 (Oct 2); +9.2% to US$14.30 (Oct 5, leak). No price reaction is reported for the ransomware attack or the CMS rule.

#### NEWS-020: Sequencing reagent tariff neutralized by the Helixor fixed-price contract through 2028
- **Finding:** A 25% tariff on imported sequencing reagents starts Oct 1, 2026. Corvane says its Helixor Instruments agreement fixes prices, including duties, through 2028. The model runs to 2030, so 2029-2030 exposure remains after the contract ends (inference).
- **Evidence:** "its reagent supply agreement with Helixor Instruments fixes prices, including duties, through 2028... 'no meaningful impact'"
- **Source:** `targets/kestrel/data/news/2026-09-17_supply-chain-health_sequencing-reagent-tariffs.md` paras 1-2 (Supply Chain Health, Sep 17, 2026)
- **Claim type:** Fact (tariff); company statement (contract)
- **Severity:** Low (neutralized through 2028)
- **Confidence:** Medium. Company statement only; the contract has not been reviewed.
- **Deal impact:** Low for the forecast through 2028; renewal risk after that.
- **Cross-check:** 10-K material contracts and supply concentration. The Helixor agreement itself (duty pass-through, change-of-control clause).

#### NEWS-021: FDA warning letter concerns an unrelated Australian company with a similar name
- **Finding:** The FDA warning letter and import alert target Corvane Laboratories Pty Ltd, a Brisbane compounding pharmacy. The article says it is "not affiliated" with Corvane Diagnostics, and Corvane Diagnostics confirmed it has no relationship with the firm. Closed.
- **Evidence:** "It is not affiliated with Corvane Diagnostics, Inc., the Raleigh, North Carolina, testing laboratory"
- **Source:** `targets/kestrel/data/news/2026-09-03_fda-enforcement-roundup_corvane-laboratories-pty.md` paras 1-2 (FDA Enforcement Roundup, Sep 3, 2026)
- **Claim type:** Fact
- **Severity:** Low (closed; possible name confusion only)
- **Confidence:** High
- **Deal impact:** Minor reputation risk from name confusion.
- **Cross-check:** 10-K subsidiary list (Exhibit 21) to confirm no Australian entity with this name.

#### NEWS-022: Durham lab start-up costs excluded from Adjusted EBITDA, as for earlier lab openings
- **Finding:** Corvane said Durham start-up costs would be reported outside Adjusted EBITDA, "as it has done for earlier lab openings". A repeat add-back for a growth company that keeps opening labs may not be truly one-off. The deal brief accepts all company add-backs.
- **Evidence:** "start-up costs for the new site will be reported outside its Adjusted EBITDA, as it has done for earlier lab openings."
- **Source:** `targets/kestrel/data/news/2025-11-06_triangle-commerce-ledger_durham-lab-opening.md` para 3 (Triangle Commerce Ledger, Nov 6, 2025)
- **Claim type:** Fact (company statement)
- **Severity:** Medium. The amount is not found in news coverage.
- **Confidence:** High that the policy exists; its size is unknown.
- **Deal impact:** Valuation (quality of earnings) and the US$110.0m covenant definition.
- **Cross-check:** Financials (Adj. EBITDA bridge: start-up cost add-backs by year). Credit agreement EBITDA definition.

#### NEWS-023: Durham lab opening adds capacity and 120 jobs
- **Finding:** The 48,000 sq ft seventh lab adds capacity for OncoTrace volumes and 120 jobs by end of 2026, with a US$0.6m five-year property tax grant. Capacity was planned before the Medicare cut and the volume weakness, so utilization risk is an inference.
- **Evidence:** "Durham gives us room to grow OncoTrace volumes for the next five years"
- **Source:** `targets/kestrel/data/news/2025-11-06_triangle-commerce-ledger_durham-lab-opening.md` paras 1-2
- **Claim type:** Fact
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Minor; check whether grant clawback terms apply on a change of control.
- **Cross-check:** 10-K properties section; grant agreement terms.

#### NEWS-024: Corvane Hope 5K charity event
- **Finding:** A community charity race raised US$410,000. The company matched employee fundraising up to US$100,000. No diligence relevance.
- **Evidence:** "raising US$410,000 for a regional cancer center"
- **Source:** `targets/kestrel/data/news/2026-06-14_triangle-commerce-ledger_charity-5k.md` paras 1-2
- **Claim type:** Fact
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None.
- **Cross-check:** None needed.

#### Timing flags summary
1. **DOJ CID (mid-Feb 2026) against the FY2025 10-K (results Mar 6, 2026):** check whether the 10-K, likely filed after the reported CID, discloses it (NEWS-007).
2. **CCO exit (Jan 15, 2026) before the 10-K:** check the governance and compliance disclosure (NEWS-008).
3. **Ransomware (Apr 18, 2026):** check for an 8-K Item 1.05 and its date, and Q2 10-Q disclosure (NEWS-010, NEWS-011).
4. **CMS final rate (Jul 30, 2026) before the Q2 earnings call and 10-Q (about Aug 5-6):** management did not quantify it. Check the 10-Q known trends section (NEWS-005).
5. **Veltrane halt (Aug 27, 2026):** check whether the Q3 10-Q or an 8-K discloses a backlog reduction (NEWS-006).
6. **Sep 30, 2026 leverage test:** check the Q3 10-Q or 8-K for a waiver or amendment (NEWS-003).
7. **Deal brief (dated Oct 12, 2026) still uses the June 30 model and the Jul 31 price.** That model came before the CMS cut, the guidance cut, the Veltrane halt and the tariff (NEWS-001, -004, -006, -019).

### Positive or mitigating points
- **NEWS-020:** Tariff exposure is neutralized through 2028 by the fixed-price Helixor contract, which includes duties (company statement).
- **NEWS-021:** The FDA warning letter concerns an unaffiliated entity. Closed.
- **NEWS-017:** FY2025 reported figures match the deal brief baseline (quality still to be tested under NEWS-014).
- **NEWS-018:** A special committee of independent directors has reportedly been formed, which supports a clean process (rumor).
- The CMS cut applies only from Jan 1, 2027 (NEWS-004), so FY2026 is not directly affected by it.
- Corvane formally denied the Bearhaven claims ("false and misleading", NEWS-012). This is a denial, not evidence.

### Articles reviewed with no diligence relevance
- `2026-06-14_triangle-commerce-ledger_charity-5k.md`: community charity event (NEWS-024).
- `2026-09-03_fda-enforcement-roundup_corvane-laboratories-pty.md`: a different, unaffiliated company with a similar name (NEWS-021).

### Gaps and questions for management
1. Did Corvane receive a DOJ CID or any subpoena? When, covering what, and is the company aware of a qui tam complaint? Why does (or doesn't) the 10-K disclose it?
2. What was the dollar amount of the Q4 2025 "refinement of our collection estimates", and what were the denial rate and DSO trends in 2025-2026?
3. What was the Sep 30, 2026 leverage ratio against the covenant? Were any waivers or amendments sought?
4. What is the FY2027 EBITDA impact of the 0419U rate cut, including commercial contracts tied to Medicare? What share of revenue is OncoTrace Medicare? (Not found in news coverage.)
5. Is Corvane a Veltrane vendor? How much of the US$246.0m backlog is Veltrane, and what are the termination terms? (Corvane is not named in the coverage.)
6. Ransomware: how long was the outage, how much revenue was lost, how much volume shifted to other labs, and how much do the costs come to? Was patient data taken? Was a ransom paid? Were HIPAA notifications and an 8-K Item 1.05 filed?
7. Why did the CCO leave? Did he raise concerns about the speaker program, and how were they handled? Has a permanent CCO been hired?
8. What are speaker program payments by physician (2019-2026) against ordering volumes?
9. What are the Durham and earlier lab start-up add-backs by year, and does the credit agreement EBITDA definition allow them?
10. What are the Helixor contract terms after 2028, and is there a change-of-control clause?
11. Do the Durham tax grant terms include a clawback or change-of-control provisions?
