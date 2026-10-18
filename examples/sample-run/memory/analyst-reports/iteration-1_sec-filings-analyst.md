## SEC filings analyst: findings

### Files reviewed
All read in full:
- `data/sec-filings/TLFS_10-K_FY2025_excerpts.md` (10-K FY2025, filed Mar 9, 2026, excerpts)
- `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` (10-Q Q2 2026, filed Aug 6, 2026, excerpts)
- `data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md` (8-K Item 4.01)
- `data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md` (8-K Item 5.02)
- `data/sec-filings/TLFS_DEF14A_2026_excerpts.md` (proxy, filed Apr 24, 2026, excerpts)
- `data/deal-brief.md` (context only)

Not in the file set, so "not found in SEC filings": Q3 2025 and Q1 2026 10-Qs, anything covering Q3 2026, earnings 8-Ks, the credit agreement, the Norvale MSA, the Adjusted EBITDA reconciliation, and Linden Barr's opinion on the financial statements. Files are excerpts, so a missing item may be in the full filing.

**Key dates in the filings:** Mar 2024 Vantor suit filed. Aug 2024 Lumora bought ($85.0M; term loan +$70.0M). Q3 2025 Hartwell & Pryce (H&P) flags material weakness and wider Q4 testing. Nov 10, 2025 H&P dismissed; Nov 12 Linden Barr engaged. Q4 2025 $31.8M bill-and-hold revenue booked. Jan 20, 2026 CFO resigns ($900,000 payment). Mar 9, 2026 10-K: adverse ICFR opinion, outlook $555M to $565M / $114M to $122M. Apr 11 FieldOS intrusion. Apr 24 proxy: bonuses at 142%. May 2026 largest customer returns $9.4M of products. Jun 3 securities class action. Jun 17 Pinecrest sues ($12.0M). Aug 6 10-Q: outlook cut to $470M to $490M / $70M to $78M. Sep 30, 2026 covenant steps to 3.00x. Mar 2027 Vantor trial. Sep 30, 2027 Norvale MSA expires. Aug 2029 debt matures. Dec 2033 HQ lease ends.

### Findings

| ID | Finding | Severity | Confidence |
|---|---|---|---|
| SEC-01 | FY2026 guidance cut; deal model uses superseded March case | Critical | High |
| SEC-02 | Norvale (31.1% of revenue) can terminate on change of control | Critical | High |
| SEC-03 | $31.8M Q4 2025 bill-and-hold drove reported growth | High | High |
| SEC-04 | $9.4M of bill-and-hold reversed in 2026, not as a 2025 correction | High | High facts / Medium interpretation |
| SEC-05 | Auditor dismissed after flagging weakness; weakness still open | High | High facts |
| SEC-06 | CFO resigned with $900,000 payment; interim CFO since Feb | High | High facts |
| SEC-07 | Securities class action on revenue and controls | High | High |
| SEC-08 | Vantor seeks injunction on Gen-3 (about 42% of revenue) | High | High (description) |
| SEC-09 | Covenant steps to 3.00x as EBITDA falls; change of control is a default | High | High terms / Medium forecast |
| SEC-10 | Receivables +59%, cash flow -76%, allowance cut | Medium | High / Medium |
| SEC-11 | 2025 bonuses at 142% depended on bill-and-hold | Medium | High / Medium |
| SEC-12 | Single-trigger equity; $28.6M CIC payments | Medium | High |
| SEC-13 | CEO-family landlord can reset HQ rent on change in control | Medium | High |
| SEC-14 | Cyber incident called "not material"; $12.0M customer suit | Medium | High / Medium |
| SEC-15 | Single-source LiDAR supplier in China | Medium | High |
| SEC-16 | What the 10-Q recharacterized or stopped saying | Medium | Medium |
| SEC-17 | Goodwill last tested before guidance cut | Low | Medium |
| SEC-18 | Ruiz settlement accrued | Low | High |

#### SEC-01: FY2026 guidance cut 37% on EBITDA; deal model still uses the withdrawn March case
- **Finding:** On Aug 6, 2026 Talonfield replaced its March outlook with FY2026 revenue of $470M to $490M and Adjusted EBITDA of $70M to $78M. Deal model v3 (Sept 2026) still uses $560M / $118M.
- **Evidence:** 10-Q: "We now expect full-year 2026 revenue of $470 million to $490 million and Adjusted EBITDA of $70 million to $78 million." "This replaces the outlook we provided on March 9, 2026." Math: revenue midpoint 480 / 560 = -14.3%; EBITDA 74 / 118 = -37.3%; top of new range is below bottom of old range. vs FY2025: revenue -4.4%, EBITDA -25.1%, margin 15.4% vs 19.7%. EV = $1,159M + about $194M to $196M net debt at Jun 30, 2026 (cash $33.9M, revolver $45.0M, term loan $182.5M to $185.0M, not stated in 10-Q excerpt) = about $1,353M to $1,355M: 11.5x $118M but 18.3x $74M (17.3x to 19.4x across the range). Holding 11.5x on $74M gives EV about $851M, 37% lower (mechanically about $13.6/share; illustration only). Implied H2 2026: revenue $257.4M (-6.7% vs H2 2025 $275.8M); EBITDA $44.1M, 17.1% margin vs 13.4% in H1 2026.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2" (Updated 2026 outlook; Results summary); `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Item 7" (2026 outlook); `data/deal-brief.md`, "Valuation basis used in the current deal model".
- **Severity:** Critical
- **Confidence:** High: both outlooks in primary filings, recomputed. Per-share figure depends on assumed term loan balance.
- **Deal impact:** Valuation. Interpretation: the model took Jun 30 net debt from the same 10-Q that withdrew the March case. The March outlook implied +11.5% on reported 2025 revenue (+19.0% on the base excluding bill-and-hold) while Q1 2026, about three-quarters done when issued, grew 0.7% ($109.7M vs $108.9M). New guidance still needs an H2 margin step-up. The 34% premium is on a post-cut price; the multiple uses pre-cut numbers.
- **Cross-check:** Financial data: Q3 2026 results, current forecast, backlog. News: reaction to the Aug 6 cut, analyst estimates, later guidance changes.

#### SEC-02: Norvale, 31.1% of revenue, can terminate on 90 days' notice after the deal
- **Finding:** The merger lets the largest customer, Norvale, terminate its MSA on 90 days' notice; Norvale has no minimum volume and the MSA expires Sep 30, 2027 anyway.
- **Evidence:** 10-K: "The Norvale MSA allows Norvale to terminate the agreement on 90 days' notice if Talonfield undergoes a change of control." "Norvale is not required to purchase any minimum volume." Math: 0.311 x 502.3 = about $156.2M revenue; 0.38 x 121.5 = about $46.2M of gross AR. Excluding its $24.6M bill-and-hold, Norvale's share is 131.6 / 470.5 = 28.0%, same as 2024: the rise in concentration came from bill-and-hold.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 1. Business" (Customers), "Item 1A. Risk Factors", "Note 13. Concentrations", "Note 2. Revenue Recognition".
- **Severity:** Critical
- **Confidence:** High: stated in 10-K. MSA change-of-control definition and Norvale's 2026 share not found in SEC filings.
- **Deal impact:** Valuation, closing risk, post-closing. Interpretation: gives Norvale repricing leverage at the deal; the May 2026 return (SEC-04) shows it already has leverage. Options: waiver or new long-term agreement as signing/closing condition, price adjustment, or contingent consideration.
- **Cross-check:** News: Norvale automation plans, vendor changes, any Arbelion link. Financial data: Norvale 2026 revenue, orders, AR aging. Court records: any Norvale dispute.

#### SEC-03: $31.8M Q4 2025 bill-and-hold revenue (20.6% of Q4) drove reported 2025 growth
- **Finding:** Talonfield booked $31.8M of Q4 2025 hardware revenue under bill-and-hold for products still in its warehouses at year-end ($24.6M from the largest customer). Excluding it, 2025 growth falls from 19.1% to 11.6% and Q4 growth from 32.4% to about 5.1%.
- **Evidence:** Note 2: "In the fourth quarter of 2025 we recognized $31.8 million of hardware revenue under bill-and-hold arrangements (2024: none material)." "At December 31, 2025, these products remained in our warehouses." MD&A called Q4 "driven by strong hardware deliveries to enterprise customers"; 10-Q later cites "orders that customers pulled forward into the fourth quarter of 2025". Math: 31.8 / 154.4 = 20.6% of Q4; 6.3% of FY revenue; 10.6% of hardware; 77.4% from largest customer. Q4 2024 = 154.4 / 1.324 = $116.6M; Q4 2025 ex bill-and-hold $122.6M = +5.1%. FY: 470.5 / 421.7 = +11.6%. Hardware: 269.6 / 261.9 = +2.9% vs 15.1% reported.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Note 2. Revenue Recognition", "Item 7" (2025 highlights; Revenue by type); `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part I, Item 2" (Revenue).
- **Severity:** High
- **Confidence:** High: disclosed and recomputed. Organic growth not disclosed; Lumora (Aug 2024) was in all of 2025 but only part of 2024, so organic growth is likely lower still.
- **Deal impact:** Valuation and disclosure. Interpretation: the cluster came in the quarter after the auditor flagged these exact contracts and was replaced (SEC-05). Needs quality-of-earnings review against the four Note 2 criteria.
- **Cross-check:** Financial data: Q4 invoices, customer hold requests, delivery and cash records. Court records: securities complaint allegations on Q4 2025. News: analyst or short-seller commentary.

#### SEC-04: $9.4M of the bill-and-hold reversed in Q2 2026 as a "contract amendment", not a 2025 correction
- **Finding:** In May 2026 the largest customer returned $9.4M of Q4 2025 bill-and-hold products for a credit, booked as a Q2 2026 revenue reduction rather than revising 2025. Interpretation: this leaves FY2025 restatement risk.
- **Evidence:** 10-Q: products "were returned to our inventory, and we issued a credit for the same amount." "We recorded the credit as a reduction of revenue in the second quarter of 2026." Remaining $22.4M delivered by Jun 30, 2026. Note 2 criterion (d): "we cannot use the products or direct them to another customer." Math: 9.4 / 31.8 = 29.6% of bill-and-hold; 9.4 / 24.6 = 38.2% of largest customer's portion; 9.4 / 112.9 = 8.3% of Q2 revenue.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part I, Item 2" (Bill-and-hold amendment); `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 2. Revenue Recognition".
- **Severity:** High
- **Confidence:** High on facts; Medium on Norvale link (10-Q says only "our largest customer"; 10-K names Norvale as largest).
- **Deal impact:** Valuation, disclosure, post-closing. Interpretation: goods returnable to inventory question whether criterion (d) was met at year-end; booking in 2026 leaves 2025 results and bonuses (SEC-11) intact. Needs accounting review, no-restatement rep, price protection.
- **Cross-check:** Financial data: amended PO, credit memo, other concessions, Linden Barr's analysis. Court records: whether the complaint cites the return.

#### SEC-05: Auditor dismissed after flagging a weakness and wider Q4 testing; weakness still unremediated
- **Finding:** The Audit Committee dismissed H&P (auditor since 2016) on Nov 10, 2025 after it reported a material weakness on non-standard hardware contracts and said Q4 arrangements needed expanded procedures. Linden Barr, engaged two days later, gave an adverse ICFR opinion; the weakness was still open at Jun 30, 2026.
- **Evidence:** 8-K: "additional audit procedures would be required for revenue arrangements with these terms expected in the fourth quarter of 2025, which would expand the scope of its audit." 10-K: "Linden Barr LLP issued an adverse opinion on the effectiveness of our internal control over financial reporting." 10-Q: "The material weakness described in our 2025 Form 10-K has not yet been remediated."
- **Source:** `data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md`, "Item 4.01" (Reportable event); `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 9A. Controls and Procedures"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part I, Item 4".
- **Severity:** High
- **Confidence:** High on facts. Dismissal reason not found in SEC filings; any opinion-shopping inference is Low to Medium.
- **Deal impact:** Disclosure, valuation, post-closing. Interpretation: replacing the auditor about seven weeks before year-end, in the quarter that then produced $31.8M of exactly this revenue, is a serious red flag. Mitigant: no disagreements; H&P agreed with the 8-K (Exhibit 16.1). Needs forensic review of Q4 2025 before signing.
- **Cross-check:** News: Linden Barr's profile and PCAOB history. Court records: complaint references. Financial data: audit committee minutes, auditor letters, Linden Barr's financial statement opinion and critical audit matters.

#### SEC-06: CFO resigned with a $900,000 payment; interim CFO since February
- **Finding:** CFO Daniel Okafor resigned Jan 20, 2026, before the 10-K, and received $900,000 with a general release; Controller Rachel Simmons is still interim CFO at Aug 6, 2026, and Okafor is a securities-suit defendant.
- **Evidence:** 8-K: "not the result of any disagreement with the Company on any matter relating to the Company's operations, policies or practices." Agreement "provides for a cash payment of $900,000 and a general release of claims". 10-Q certified by Simmons as "Interim Chief Financial Officer".
- **Source:** `data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md`, "Item 5.02"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 18. Subsequent Events"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, header; `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, "Potential payments upon a change in control".
- **Severity:** High (as part of the SEC-03 to SEC-05 pattern; alone Medium)
- **Confidence:** High on facts; payment rationale not found in SEC filings.
- **Deal impact:** Post-closing and disclosure. Interpretation: a paid release on a voluntary resignation is unusual; timing fits the pattern. Needs CFO plan, separation agreement review.
- **Cross-check:** News: reasons for exit. Court records: complaint and witness accounts. Financial data: separation agreement, board minutes.

#### SEC-07: Securities class action on revenue and internal control statements
- **Finding:** A putative class action filed Jun 3, 2026 (S.D. Ohio) against Talonfield, its CEO and former CFO alleges misleading statements on revenue and controls; no accrual, class period or insurance is disclosed.
- **Evidence:** 10-Q: "alleging that we made false or misleading statements about our revenue and our internal controls." Accrual: not found in SEC filings.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1. Legal Proceedings"; "Part II, Item 1A. Risk Factors".
- **Severity:** High
- **Confidence:** High that the suit exists; claims are allegations.
- **Deal impact:** Post-closing and valuation (defense costs, amounts above D&O cover, indemnification of Hale and Okafor). Interpretation: maps onto SEC-03 to SEC-05; filed before the Aug 6 cut, so an earlier disclosure triggered it (not in file set). Public deals rarely have indemnities, so protection is price plus D&O tail.
- **Cross-check:** Court records: docket, class period, corrective disclosures, SEC inquiry, derivative suits. Financial data: D&O tower.

#### SEC-08: Vantor patent suit seeks an injunction on Gen-3; no accrual; trial March 2027
- **Finding:** Vantor alleges Gen-3 navigation infringes three patents and seeks damages and an injunction; no accrual or range is given.
- **Evidence:** 10-K: "we do not believe a loss is probable, and we cannot reasonably estimate a possible loss or range of loss." 10-Q: "Trial is currently scheduled for March 2027." Gen-3 is about 70% of hardware: 0.70 x 301.4 = $211.0M = 42.0% of 2025 revenue.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 1. Business", "Item 1A", "Item 3. Legal Proceedings"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1".
- **Severity:** High (could become Critical if the court record is unfavorable)
- **Confidence:** High for description and math; merits not assessable from filings.
- **Deal impact:** Valuation, post-closing; trial may fall before closing. Needs patent counsel review and design-around cost.
- **Cross-check:** Court records: claim construction, injunction motions, IPRs, damages reports. News: Vantor statements.

#### SEC-09: Covenant steps down to 3.00x as EBITDA falls; change of control is an event of default
- **Finding:** Max Total Net Leverage falls to 3.00x from Sep 30, 2026 while guidance cuts TTM EBITDA from $89.7M to $70M to $78M; at the low end, year-end headroom is only about $1.7M to $2.5M of EBITDA. Change of control lets lenders demand repayment of about $227.5M to $230.0M.
- **Evidence:** Note 9: "no more than 3.00 to 1.00 for each fiscal quarter ending on or after September 30, 2026"; cash netting "capped at $25.0 million"; "Permitted Add-backs may not exceed 15% of Consolidated EBITDA". "A change of control of Talonfield is an event of default". 10-Q: 2.26x at Jun 30, 2026. Math: term loan $182.5M (assumed; $5.0M/yr amortization) + $45.0M revolver - $25.0M cap = $202.5M; TTM Adjusted EBITDA 98.8 - 39.0 + 29.9 = $89.7M; 202.5 / 89.7 = 2.26x (ties). Dec 31, 2025 estimate: 195.0 / 98.8 = 1.97x. Dec 31, 2026: 202.5 / 74 = 2.74x; / 70 = 2.89x (2.93x if term loan $185.0M). EBITDA needed for 3.00x: $67.5M to $68.3M. Liquidity: $33.9M cash + $25.8M availability = $59.7M; H1 2026 operating cash flow -$4.2M.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 9. Debt"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part I, Item 2" (Covenant compliance; Liquidity).
- **Severity:** High
- **Confidence:** High for terms; Medium for forecast (assumes covenant EBITDA tracks Adjusted EBITDA; definitions are summaries; add-backs undisclosed).
- **Deal impact:** Closing risk, valuation. Interpretation: Q4 2025 drops out at the Dec 31, 2026 test, likely between signing and closing; breach allows acceleration. Sources and uses must include payoff plus $4.2M letters of credit.
- **Cross-check:** Financial data: credit agreement, Q2/Q3 compliance certificates, add-back totals. News: waiver talks.

#### SEC-10: Receivables up 59%, cash flow down 76%, allowance cut
- **Finding:** Gross AR rose 59.2% on 19.1% revenue growth and operating cash flow fell to $9.7M, yet the allowance was reduced; H1 2026 cash flow was negative.
- **Evidence:** Note 5: "The decrease in the allowance reflects improved collection experience". 10-K: "We expect collections to normalize in 2026." Math: allowance 3.8% to 2.1% of gross AR (about $2.0M lower than at 2024 ratio); DSO 63.5 to 86.4 days; Norvale AR $22.1M to $46.2M (+$24.0M, near its $24.6M bill-and-hold); cash flow / Adjusted EBITDA 9.8% vs about 55% in 2024.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 5", "Note 13", "Item 7" (Liquidity); `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part I, Item 2" (Liquidity).
- **Severity:** Medium
- **Confidence:** High for numbers; Medium for the Norvale AR inference.
- **Deal impact:** Valuation. Interpretation: "strong fourth-quarter shipments" conflicts with Note 2.
- **Cross-check:** Financial data: AR aging, collection of bill-and-hold invoices, contract assets.

#### SEC-11: 2025 bonuses at 142% of target depended on bill-and-hold revenue
- **Finding:** Without the $31.8M, 2025 revenue would be $470.5M, $0.5M above the $470.0M threshold, and EBITDA likely below threshold; no adjustment or clawback is disclosed.
- **Evidence:** Proxy: "the Compensation Committee approved bonus payouts at 142% of target for all executive officers." Math: EBITDA cushion 98.8 - 88.0 = $10.8M; 10.8 / 31.8 = 34.0%; if bill-and-hold contribution exceeded 34.0% (H1 2025 gross margin 40.8%), EBITDA misses threshold. Payout curve undisclosed.
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, "2025 annual incentive plan"; 10-K "Note 2".
- **Severity:** Medium
- **Confidence:** High for plan; Medium for counterfactual.
- **Deal impact:** Governance, disclosure. Interpretation: direct pay incentive to pull revenue forward.
- **Cross-check:** Financial data: comp committee minutes, clawback policy.

#### SEC-12: Single-trigger equity vesting; $28.6M CIC payments
- **Finding:** All unvested executive equity vests at a change in control even if executives stay ($17.6M); total estimated CIC payments are $28.6M, $11.8M for CEO Hale.
- **Evidence:** "vest in full immediately upon a change in control ('single-trigger'), whether or not the executive's employment ends." Totals recomputed and tie; 28.6 / 1,159 = 2.5% of equity value.
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, "Potential payments upon a change in control".
- **Severity:** Medium
- **Confidence:** High; values at $24.00 and 280G terms not found in SEC filings.
- **Deal impact:** Post-closing retention; new awards needed.
- **Cross-check:** Financial data: award ledger, 280G calculations.

#### SEC-13: CEO-family landlord can reset HQ rent on a change in control
- **Finding:** HQ and main assembly site are leased from Hale Family Properties LLC to Dec 2033, with a rent reset on change in control; Hale is Chair, CEO, 14.2% holder; no lead independent director.
- **Evidence:** "reset the rent to 'fair market value', as determined by an appraiser selected by the landlord." 2025 rent $2.1M, +3%/yr; remaining rent 2026 to 2033 about $19.2M. Hale stake at $24.00 about $160.6M plus $11.8M CIC.
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, "Certain relationships and related party transactions", "Board of Directors", "Security ownership".
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation, governance. Interpretation: Hale gains from shares, CIC and rent reset, so independent directors should run the process; seek reset waiver and voting agreement.
- **Cross-check:** Property records; lease; market rent study.

#### SEC-14: Cyber incident called "not material" despite outages, credits and a $12.0M suit
- **Finding:** April 2026 intrusion stopped some fleets up to three days; $1.8M costs added back to Adjusted EBITDA, $2.3M credits, $12.0M Pinecrest suit; risk factors called unchanged.
- **Evidence:** "we concluded that the incident was not material". 10-Q: "no material changes to the risk factors" except securities litigation. Math: 2.3 + 1.8 + 12.0 = $16.1M; 12.0 / 74 = 16.2% of EBITDA guidance midpoint. Pinecrest accrual not found.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part I, Item 2" (April 2026 service disruption), "Part II, Item 1", "Part II, Item 1A".
- **Severity:** Medium
- **Confidence:** High facts; Medium on disclosure view.
- **Deal impact:** Post-closing (claims, FieldOS churn), disclosure.
- **Cross-check:** Court records: Pinecrest docket. Financial data: forensic report, churn, insurance.

#### SEC-15: Single-source LiDAR supplier in China
- **Finding:** All Talon AMR models use LiDAR from one China-based supplier with no qualified second source; hardware is 60.0% of revenue.
- **Evidence:** "We do not currently have a qualified second source." H1 2026 gross margin 38.0% vs 40.8% (drivers unexplained).
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 1. Business" (Suppliers), "Item 1A".
- **Severity:** Medium
- **Confidence:** High; supplier terms not found in SEC filings.
- **Deal impact:** Post-closing (tariffs, second source).
- **Cross-check:** News: tariffs on Chinese LiDAR. Financial data: supply contract.

#### SEC-16: What the 10-Q recharacterized or stopped saying
- **Finding:** Q4 "deliveries" became "pull-forward"; the collections outlook, ARR, net revenue retention and revenue by type are absent from the 10-Q excerpt; Norvale is unnamed; risk factors called unchanged; no remediation timetable.
- **Evidence:** 10-K: "FieldOS ARR grew 27% to $139.2 million. Software net revenue retention was 118%." vs none in 10-Q excerpt.
- **Source:** 10-K "Item 7", "Item 9A"; 10-Q "Part I, Item 2", "Part I, Item 4", "Part II, Item 1A".
- **Severity:** Medium
- **Confidence:** Medium (excerpts).
- **Deal impact:** Disclosure.
- **Cross-check:** Earnings calls; Q1 to Q3 2026 KPIs.

#### SEC-17: Goodwill last tested before the guidance cut
- **Finding:** $98.4M goodwill ($57.4M Lumora) last tested Oct 1, 2025; no interim test in the 10-Q excerpt.
- **Source:** 10-K "Note 15. Goodwill". **Severity:** Low. **Confidence:** Medium. **Deal impact:** Disclosure. **Cross-check:** impairment analysis.

#### SEC-18: Ruiz settlement accrued
- **Finding:** $3.2M wage-and-hour settlement accrued Dec 31, 2025; preliminary approval May 20, 2026.
- **Source:** 10-K "Item 3"; 10-Q "Part II, Item 1". **Severity:** Low. **Confidence:** High. **Deal impact:** Post-closing. **Cross-check:** final approval docket.

### Positive or mitigating points
- No auditor disagreements; H&P agreed with the 8-K.
- $22.4M of $31.8M bill-and-hold (70.4%) delivered by Jun 30, 2026.
- Covenant compliance at 2.26x; $59.7M liquidity; no maturities before Aug 2029.
- Software +27.1%, ARR $139.2M, retention 118% at year-end 2025; software and services 40.0% of revenue.
- Q2 2026 revenue ex $9.4M and $2.3M credits: $124.6M, +6.0% (H1 +3.4%).
- Cash severance is double-trigger; Ruiz resolved within accrual; remediation started; 5 of 7 directors independent.

### Gaps and questions for management
1. Q3 2026 results and Sep 30 covenant certificate before the Nov 6 IC.
2. Full credit agreement definitions, add-backs, term loan balance, prepayment terms.
3. Adjusted EBITDA reconciliations FY2024 to H1 2026.
4. Bill-and-hold schedule by customer, recognition dates vs Nov 10 dismissal, cash receipts; why no 2025 correction.
5. May 2026 amendment terms; confirm customer is Norvale; other concessions.
6. Norvale 2026 revenue, renewal plans, waiver willingness.
7. Reason for auditor dismissal; Linden Barr's financial statement opinion; remediation timetable.
8. Why Okafor resigned and was paid $900,000; CFO search status.
9. Securities suit class period, triggers, D&O coverage, SEC inquiry.
10. Vantor merits, design-around, settlement talks.
11. Cyber materiality basis, other claims, churn.
12. ARR, retention, revenue by type for 2026; gross margin drivers.
13. Bonus payout curve; clawback.
14. CIC values at $24.00; 280G.
15. Lease reset waiver; special committee.
16. LiDAR supplier terms.
17. Other change-of-control contracts.
18. Lumora contribution; interim impairment test.
19. Whether the Q3 2025 10-Q disclosed the weakness.
