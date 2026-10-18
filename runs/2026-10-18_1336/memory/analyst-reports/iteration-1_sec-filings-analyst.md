# Iteration 1: sec-filings-analyst (full report, unedited)

## SEC filings analyst: findings

### Files reviewed
All five files read in full, plus `data/deal-brief.md` for context:
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-K_FY2025_excerpts.md` (filed March 9, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` (filed August 6, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_DEF14A_2026_excerpts.md` (filed April 24, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md` (dated November 14, 2025)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md` (dated January 21, 2026)

Prompt-injection check: I found no text in these files that tries to instruct the agents.

Timeline from the filings: Q3 2025 old auditor flags a material weakness. Nov 10, 2025 auditor dismissed. Nov 12 new auditor engaged. Q4 2025 $31.8m of bill-and-hold revenue booked. Jan 20, 2026 CFO resigns. Mar 9, 2026 10-K filed with FY2026 guidance of $555-565m. Mar 2026 investor day (per deal brief). Apr 11 cyber incident. Apr 24 proxy. May 2026 Norvale amendment reverses $9.4m. Jun 3 securities class action. Jun 17 Pinecrest suit. Aug 6 10-Q cuts guidance.

### Findings

#### SEC-01: Guidance cut makes the deal model's management case stale
- **Finding:** On August 6, 2026, the 10-Q replaced the March 9 outlook. The new outlook is FY2026 revenue of $470-490m and Adjusted EBITDA of $70-78m. The deal model still uses $560.0m and $118.0m.
- **Evidence:** "We now expect full-year 2026 revenue of $470 million to $490 million and Adjusted EBITDA of $70 million to $78 million. This replaces the outlook we provided on March 9, 2026." The prior outlook was "$555 million to $565 million and Adjusted EBITDA of $114 million to $122 million."
- **Math:** Revenue midpoint $560.0m to $480.0m = -14.3%. EBITDA midpoint $118.0m to $74.0m = -37.3%. Revenue midpoint $480.0m vs 2025 $502.3m = -4.4%, so revenue now falls year over year. My EV estimate is $1,159.2m equity plus about $196.1m net debt (assumes the term loan is still $185.0m, which the 10-Q does not state, plus $45.0m revolver, minus $33.9m cash), so about $1,355.3m. That gives 1,355.3 / 118.0 = 11.5x, which matches the deal brief. On the new guidance it is 1,355.3 / 74.0 = 18.3x (17.4x to 19.4x across the range). Keeping 11.5x on $74.0m implies EV of about $851m, equity of about $655m, or about $13.56 per share on 48.3m diluted shares. That is below the October 16 close of $17.85. This is my calculation, not the filing's.
- **Implied H2:** H2 2026 revenue = $470-490m minus H1 $222.6m = $247.4-267.4m, vs H2 2025 $275.8m ($502.3m - $226.5m), a drop of 3.0% to 10.3%. H2 Adjusted EBITDA = $40.1-48.1m.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Updated 2026 outlook"; `TLFS_10-K_FY2025_excerpts.md`, Item 7 "2026 outlook (as of March 9, 2026)"
- **Severity:** Critical
- **Confidence:** High. The filing states it directly. The EV math uses one assumption (term loan balance at June 30).
- **Deal impact:** Valuation
- **Cross-check:** Financial data: Q3 2026 results or trading updates, the June 30 term loan balance, and the deal model v3 inputs. News: analyst reaction to the August 6 cut and the share price move.

#### SEC-02: $31.8m bill-and-hold in Q4 2025 inflated reported growth; $9.4m later reversed
- **Finding:** 20.6% of record Q4 2025 revenue came from bill-and-hold arrangements, a practice that was new in 2025. 77.4% of it was with Norvale. In May 2026, $9.4m was returned to inventory and credited back.
- **Evidence:** 10-K Note 2: "$31.8 million of hardware revenue under bill-and-hold arrangements (2024: none material). Of this amount, $24.6 million related to our largest customer... these products remained in our warehouses." 10-Q: "$9.4 million... were returned to our inventory, and we issued a credit for the same amount."
- **Math:** 31.8 / 154.4 = 20.6% of Q4 revenue. 24.6 / 31.8 = 77.4% Norvale. Q4 2024 = 154.4 / 1.324 = $116.6m. Q4 2025 without bill-and-hold = $122.6m, growth +5.1% (vs reported +32.4%). FY2025 without bill-and-hold = 502.3 - 31.8 = $470.5m, growth 11.6% (vs reported 19.1%). Hardware without bill-and-hold = 301.4 - 31.8 = $269.6m, growth +2.9% (vs reported 15.1%). Reversed share = 9.4 / 31.8 = 29.6% of the total (38.2% of the Norvale portion, if the full $9.4m was Norvale, which the 10-Q says: "our largest customer"). The remaining $22.4m was delivered by June 30, 2026.
- **Interpretation:** Criterion (d) in Note 2 requires that the company "cannot use the products or direct them to another customer." Taking goods back into inventory five months later raises the question of whether the criteria, especially (a) "substantive" reason, were met. This is my inference, not a filing statement. No restatement is disclosed. The reversal was treated as a Q2 2026 revenue reduction.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Note 2 and Item 7 "2025 highlights"; `TLFS_10-Q_Q2-2026_excerpts.md`, "Bill-and-hold amendment" and "Revenue"
- **Severity:** Critical
- **Confidence:** High. The amounts are stated directly and I recomputed them. Whether the accounting was proper is an inference.
- **Deal impact:** Valuation, disclosure (restatement risk), post-closing (litigation)
- **Cross-check:** Litigation: whether the securities class action complaint cites bill-and-hold. News: reports on Norvale or Q4 shipments. Financial data: quarterly hardware revenue, inventory and contract asset movements, whether the other $7.2m (non-Norvale) went to one customer.

#### SEC-03: 10-K described Q4 as "deliveries"; 10-Q later says orders were "pulled forward"
- **Finding:** The 10-K credited record Q4 revenue to "strong hardware deliveries" even though $31.8m was undelivered. The 10-Q now says customers "pulled forward" orders into Q4 2025.
- **Evidence:** 10-K: "Record fourth-quarter revenue of $154.4 million, up 32.4%... driven by strong hardware deliveries to enterprise customers." 10-Q: "orders that customers pulled forward into the fourth quarter of 2025."
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 7 "2025 highlights"; `TLFS_10-Q_Q2-2026_excerpts.md`, "Revenue"
- **Severity:** High
- **Confidence:** High for the wording. Medium for the inference that the 10-K description was misleading.
- **Deal impact:** Disclosure, post-closing (securities litigation exposure)
- **Cross-check:** The class action complaint's alleged misstatements. Investor day transcript or news coverage of how management described Q4.

#### SEC-04: Auditor dismissed after it flagged a material weakness and planned a wider Q4 audit
- **Finding:** Hartwell & Pryce, auditor since 2016, flagged a material weakness in hardware contracts with non-standard terms in Q3 2025. It said Q4 arrangements with these terms would need extra procedures. The Audit Committee dismissed it on November 10, 2025, about seven weeks before year-end. The replacement firm signed the FY2025 audit, and $31.8m of bill-and-hold was booked in that quarter.
- **Evidence:** "additional audit procedures would be required for revenue arrangements with these terms expected in the fourth quarter of 2025, which would expand the scope of its audit." The 8-K states "no disagreements," and Hartwell & Pryce's Exhibit 16.1 letter "agrees with the statements."
- **Interpretation:** The sequence fits a pattern of opinion shopping. This is not stated in the filing. The 8-K gives no reason for the dismissal. The reportable event is disclosed properly. Note that the 8-K said Q4 arrangements with these terms were "expected." That means management planned non-standard Q4 deals before the quarter closed.
- **Source:** `TLFS_8-K_2025-11-14_auditor-change.md`, Item 4.01 "Reportable event" and (a), (b); `TLFS_10-K_FY2025_excerpts.md`, header and Item 9A
- **Severity:** High
- **Confidence:** High for the facts. Low to Medium for motive.
- **Deal impact:** Disclosure, closing risk (restatement), indemnity/R&W scope
- **Cross-check:** News on the auditor switch. Whether the class action cites it. Audit Committee minutes and Hartwell & Pryce workpapers in the data room. Linden Barr's opinion on the financial statements, which is not in the excerpts.

#### SEC-05: Material weakness not remediated; adverse ICFR opinion; disclosure controls not effective at June 30, 2026
- **Finding:** Linden Barr gave an adverse opinion on ICFR at December 31, 2025. At June 30, 2026, the weakness is "not yet been remediated." Remediation steps are early stage: a director of technical accounting and a contract review committee.
- **Evidence:** 10-Q Item 4: "The material weakness described in our 2025 Form 10-K has not yet been remediated... disclosure controls and procedures were not effective as of June 30, 2026."
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 9A; `TLFS_10-Q_Q2-2026_excerpts.md`, Part I Item 4
- **Severity:** High
- **Confidence:** High. Stated directly.
- **Deal impact:** Post-closing (SOX integration and cost), disclosure, valuation (reliability of reported numbers)
- **Cross-check:** Remediation timeline from management. Whether the 10-K financial statement audit opinion was clean (not found in SEC filings excerpts). Any SEC comment letters or inquiries (not found in SEC filings).

#### SEC-06: CFO resigned seven weeks before the 10-K, was paid $0.9m, and is now a class action defendant; interim CFO still in place
- **Finding:** CFO Daniel Okafor resigned on January 20, 2026, effective February 15, before the March 9 10-K. Despite resigning voluntarily, he received a $900,000 separation payment in exchange for a general release. Rachel Simmons, the Corporate Controller (the function covering the controls with the weakness), has been interim CFO since then and certified the August 10-Q. The June 3 class action names the "former Chief Financial Officer."
- **Evidence:** 8-K: "not the result of any disagreement with the Company on any matter relating to the Company's operations, policies or practices" and "a cash payment of $900,000 and a general release of claims." 10-Q header: "Rachel Simmons (Interim Chief Financial Officer)."
- **Interpretation:** A cash payment plus release on a voluntary resignation is unusual. The "no disagreement" wording is standard boilerplate. These are my observations.
- **Source:** `TLFS_8-K_2026-01-21_cfo-departure.md`, Item 5.02; `TLFS_10-K_FY2025_excerpts.md`, Note 18; `TLFS_DEF14A_2026_excerpts.md`, "Potential payments upon a change in control"; `TLFS_10-Q_Q2-2026_excerpts.md`, header and Part II Item 1
- **Severity:** High
- **Confidence:** High for the facts. Medium for the inference.
- **Deal impact:** Post-closing (finance leadership gap), disclosure
- **Cross-check:** News on why Okafor left and his current role. Class action allegations about his statements. Whether a permanent CFO search has produced a hire (not found in SEC filings).

#### SEC-07: Norvale concentration plus a change-of-control termination right
- **Finding:** Norvale was 31.1% of 2025 revenue (about $156.2m) and 38% of gross AR. It can terminate the MSA on 90 days' notice if Talonfield undergoes a change of control. It has no minimum volume, and the MSA expires September 30, 2027.
- **Evidence:** "The Norvale MSA allows Norvale to terminate the agreement on 90 days' notice if Talonfield undergoes a change of control. Norvale is not required to purchase any minimum volume."
- **Math:** 0.311 x 502.3 = $156.2m. Norvale AR = 0.38 x 121.5 = $46.2m (2024: 0.29 x 76.3 = $22.1m, about 2.1x). Norvale revenue excluding its $24.6m bill-and-hold = $131.6m, which is 131.6 / 470.5 = 28.0% of underlying revenue. So the rise in concentration from 28.0% came from bill-and-hold. The May 2026 $9.4m reversal is a concrete sign the relationship has changed.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 1 "Customers", Item 1A, Note 13; `TLFS_10-Q_Q2-2026_excerpts.md`, "Bill-and-hold amendment"
- **Severity:** Critical (this acquisition triggers the termination right directly)
- **Confidence:** High. Stated directly and recomputed.
- **Deal impact:** Closing risk (consent or waiver), valuation
- **Cross-check:** News on Norvale's automation strategy, competitor wins, and its own finances. Financial data: Norvale revenue by quarter in 2026 and AR aging. Note that the 10-Q excerpts give no updated Norvale share or AR (see SEC-15).

#### SEC-08: Change of control is an event of default; covenant steps down to 3.00x while EBITDA falls
- **Finding:** The credit agreement treats a change of control as an event of default, so all debt (about $230m) must be repaid or waived at closing. The leverage covenant tightens from 3.50x to 3.00x from September 30, 2026. Cash netting is capped at $25.0m and add-backs at 15%.
- **Evidence:** "A change of control of Talonfield is an event of default, which allows the lenders to demand immediate repayment of all outstanding loans." The cap reads "no more than 3.00 to 1.00 for each fiscal quarter ending on or after September 30, 2026." Reported ratio: "2.26 to 1.00 at June 30, 2026."
- **Math (my estimates):** Debt at June 30 is about $185.0m term loan (10-K balance; the 10-Q does not state it) plus $45.0m revolver = $230.0m. Netting is capped at $25.0m (cash $33.9m), so net debt is $205.0m. Implied Consolidated EBITDA = 205.0 / 2.26 = $90.7m. TTM Adjusted EBITDA at June 30 = 98.8 - 39.0 + 29.9 = $89.7m, which is consistent. At 3.00x, the minimum EBITDA with debt unchanged is 205.0 / 3.00 = $68.3m, a cushion of about 25% vs $90.7m. At December 31, 2026, TTM equals FY2026: on guidance of $70-78m the ratio is 205.0 / 78 = 2.63x to 205.0 / 70 = 2.93x. That leaves almost no room at the low end. With an extra $10m revolver draw (215.0 / 70 = 3.07x), the covenant would be breached. TTM through September 30 still includes Q4 2025 bill-and-hold EBITDA. Consolidated EBITDA could also fall below Adjusted EBITDA if non-recurring add-backs (for example the $1.8m incident cost) exceed the 15% cap.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Note 9 "Financial covenant" and "Definitions"; `TLFS_10-Q_Q2-2026_excerpts.md`, "Covenant compliance", "Liquidity and capital resources", "Updated 2026 outlook"
- **Severity:** High (repayment at closing is routine for a cash buyer, but it must be in sources and uses. A covenant breach before closing would add leverage risk.)
- **Confidence:** High for the terms. Medium for the headroom math (the term loan balance is assumed).
- **Deal impact:** Closing risk (payoff letters, refinancing), valuation (net debt in the price)
- **Cross-check:** Financial data: the actual term loan balance, Q3 2026 covenant certificate, the Consolidated EBITDA build including the add-back cap. News: any lender waiver or amendment talk.

#### SEC-09: Liquidity is weakening: falling cash, rising revolver, weak operating cash flow
- **Finding:** Operating cash flow fell from $40.8m (2024) to $9.7m (2025) and was negative $4.2m in H1 2026. Cash fell from $41.6m to $33.9m while the revolver rose from $35.0m to $45.0m. Available revolver capacity is $25.8m.
- **Evidence:** 10-K: "We expect collections to normalize in 2026." 10-Q: "Operating cash flow for the first half of 2026 was negative $4.2 million."
- **Math:** Gross AR rose 121.5 / 76.3 - 1 = 59.2%, vs revenue growth of 19.1%. The allowance fell from 3.8% of gross AR (2.9 / 76.3) to 2.1% (2.6 / 121.5) while AR and concentration rose. The 10-K says this "reflects improved collection experience." Total liquidity at June 30 is about 33.9 + 25.8 = $59.7m.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 7 "Liquidity", Note 5; `TLFS_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation (working capital peg), post-closing
- **Cross-check:** Financial data: AR aging (especially Norvale), contract assets, Q3 cash. The management prediction that collections would "normalize" did not come true in H1 2026.

#### SEC-10: Vantor patent case threatens Talon Gen-3 (about 42% of revenue); trial March 2027; no accrual
- **Finding:** Vantor seeks damages and an injunction against the Gen-3 navigation system. Trial is scheduled for March 2027, after the planned closing. There is no accrual. The 10-Q drops the 10-K's "cannot reasonably estimate" statement.
- **Evidence:** 10-K: "seeks damages and an injunction... We have not recorded an accrual because we do not believe a loss is probable, and we cannot reasonably estimate a possible loss or range of loss." 10-Q: "The case is in discovery. Trial is currently scheduled for March 2027... we have not recorded an accrual."
- **Math:** Gen-3 is about 70% of hardware revenue: 0.70 x 301.4 = $211.0m, or 42.0% of 2025 total revenue (software and services attached to Gen-3 would add more exposure).
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 1, Item 1A, Item 3; `TLFS_10-Q_Q2-2026_excerpts.md`, Part II Item 1
- **Severity:** High
- **Confidence:** High for the disclosures. Exposure size: not found in SEC filings.
- **Deal impact:** Valuation, post-closing (specific indemnity or escrow)
- **Cross-check:** Litigation: docket status, claim construction rulings, damages expert reports, any settlement talks. News on Vantor's licensing demands.

#### SEC-11: Two new 2026 lawsuits plus a cyber incident called "not material"; no accrual or range disclosed
- **Finding:** The 10-Q discloses a securities class action (June 3, 2026) against the company, the CEO and the former CFO over revenue and controls statements. It also discloses a $12.0m Pinecrest breach-of-contract suit (June 17, 2026) tied to the April 11 FieldOS incident. Neither has an accrual or loss range disclosed. The company calls the incident "not material."
- **Evidence:** "we concluded that the incident was not material, and we have not identified evidence that customer data was taken." Fleets were interrupted "for up to three days."
- **Math:** Known incident cost = $1.8m response + $2.3m SLA credits + $12.0m Pinecrest claim = $16.1m. That equals 21.8% of the $74.0m guidance midpoint EBITDA. The $1.8m is added back in Adjusted EBITDA as "other non-recurring items."
- **Interpretation:** The "not material" conclusion is hard to square with a three-day outage, a lawsuit and SLA credits. A current report for the cyber incident was not found in SEC filings (only these five files were provided).
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "April 2026 service disruption", Part II Item 1
- **Severity:** High
- **Confidence:** High for the facts. Medium for the materiality inference.
- **Deal impact:** Post-closing (indemnity, D&O tail), valuation, disclosure
- **Cross-check:** Litigation: class period, alleged misstatements, lead plaintiff, Pinecrest complaint. News: coverage of the outage, other affected customers, any data exposure claims.

#### SEC-12: 10-Q says "no material changes" to risk factors despite major developments
- **Finding:** The 10-Q adds only a securities litigation risk factor. It adds nothing on the guidance cut, the Norvale bill-and-hold reversal, the cyber incident and Pinecrest suit, the covenant step-down, or the unremediated weakness.
- **Evidence:** "There have been no material changes to the risk factors in our 2025 Form 10-K, except for the following addition."
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, Part II Item 1A
- **Severity:** Medium
- **Confidence:** Medium. The 10-Q is an excerpt, and existing 10-K risk factors cover some topics in general terms.
- **Deal impact:** Disclosure
- **Cross-check:** The full 10-Q if available. Class action claims about risk disclosure.

#### SEC-13: 2025 bonuses paid at 142% on revenue that included bill-and-hold
- **Finding:** Executive bonuses were 50% revenue and 50% Adjusted EBITDA and paid at 142% of target. Without the $31.8m bill-and-hold, revenue of $470.5m only just clears the $470.0m threshold, against a $490.0m target.
- **Evidence:** Revenue threshold 470.0, target 490.0, maximum 510.0, actual 502.3. "bonus payouts at 142% of target for all executive officers."
- **Math:** 502.3 - 31.8 = 470.5, which is $0.5m above threshold. The EBITDA effect of the bill-and-hold is not disclosed. If margin on it were near the 2025 gross margin level (assumption), Adjusted EBITDA of $98.8m could fall toward or below the $88.0m threshold. That is my illustration only. A clawback policy or action: not found in SEC filings.
- **Source:** `TLFS_DEF14A_2026_excerpts.md`, "2025 annual incentive plan"; `TLFS_10-K_FY2025_excerpts.md`, Note 2
- **Severity:** Medium
- **Confidence:** High for the numbers. Low for the EBITDA illustration.
- **Deal impact:** Governance, post-closing (clawback), disclosure
- **Cross-check:** The full proxy for the payout curve and clawback policy. Class action allegations about motive.

#### SEC-14: Single-trigger equity, related party HQ lease with CoC rent reset, weak board structure
- **Finding:** All executive equity vests on a change of control alone ($17.6m, total CoC package $28.6m). The CEO's family entity owns the HQ and main assembly facility. On a change of control it can reset rent to "fair market value" using an appraiser the landlord picks. Hale is Chairman and CEO, owns 14.2%, and there is no lead independent director.
- **Evidence:** "all unvested equity awards held by executive officers vest in full immediately upon a change in control ('single-trigger'), whether or not the executive's employment ends." Lease: "allows the landlord to reset the rent to 'fair market value', as determined by an appraiser selected by the landlord."
- **Math:** Hale's CoC package is $11.8m. His shares are worth 6.69m x $24.00 = $160.6m at the offer price. The lease is $2.1m in 2025 with 3% escalators through December 2033. The size of the reset is not disclosed. Single-trigger vesting removes a retention lever for the COO, CTO and other key staff after closing.
- **Interpretation:** Hale has a conflict: he benefits from the sale through his shares, his equity acceleration and the landlord's reset right.
- **Source:** `TLFS_DEF14A_2026_excerpts.md`, "Security ownership", "Board of Directors", "Potential payments upon a change in control", "Certain relationships and related party transactions"
- **Severity:** Medium (High if the rent reset is large)
- **Confidence:** High
- **Deal impact:** Valuation (lease cost, retention packages), post-closing, governance
- **Cross-check:** Market rent comps for Columbus industrial property. The lease document. Whether a special committee of independent directors is running the sale process (not found in SEC filings).

#### SEC-15: Items missing from the 10-Q
- **Finding:** The Q2 10-Q excerpts include no updated Norvale share or AR. They do not name Norvale (only "our largest customer"). They have no goodwill or interim impairment discussion despite the guidance cut ($98.4m goodwill, $57.4m from Lumora, tested only as of October 1, 2025). They have no allowance update, no going concern language, no subsequent events note, no update on ARR or net revenue retention, and no update on the CFO search.
- **Evidence:** 10-K: "FieldOS ARR grew 27% to $139.2 million. Software net revenue retention was 118%." No equivalent appears in the 10-Q excerpts.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md` (absence); `TLFS_10-K_FY2025_excerpts.md`, Item 7, Note 15
- **Severity:** Medium
- **Confidence:** Medium. The documents are excerpts, so the items may exist in the full filing.
- **Deal impact:** Disclosure, valuation (possible goodwill impairment)
- **Cross-check:** Financial data: ARR and NRR trend through 2026, Norvale revenue in 2026, impairment indicators.

#### SEC-16: Single-source LiDAR supplier in China with no second source
- **Finding:** All Talon AMR models use LiDAR from one supplier that makes them in China. There is no qualified second source, and tariffs are a stated risk.
- **Evidence:** "We do not currently have a qualified second source."
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 1 "Suppliers", Item 1A
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing (supply chain plan), valuation (margin)
- **Cross-check:** News on tariffs affecting LiDAR. Supplier contract terms. Whether the H1 2026 gross margin decline (40.8% to 38.0%) includes tariff effects.

#### SEC-17: Ruiz wage-and-hour settlement
- **Finding:** A $3.2m settlement was accrued at December 31, 2025 and received preliminary court approval on May 20, 2026.
- **Evidence:** "the court granted preliminary approval of the $3.2 million settlement."
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 3; `TLFS_10-Q_Q2-2026_excerpts.md`, Part II Item 1
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Post-closing (minor)
- **Cross-check:** Final approval date and opt-outs in the court records.

### Positive or mitigating points
- The auditor change 8-K disclosed the reportable event openly. The former auditor's letter agrees, and no disagreements are reported.
- $22.4m of the $31.8m bill-and-hold was delivered by June 30, 2026. The $9.4m reversal went through current-period revenue, and no restatement is disclosed.
- The covenant was met at June 30, 2026 (2.26x vs 3.50x).
- The Ruiz case is accrued and near final settlement.
- Cash severance is double-trigger.
- Q2 2026 revenue adjusted for the $9.4m reversal and $2.3m SLA credits would be 112.9 + 9.4 + 2.3 = $124.6m, up 6.0% vs $117.6m. This is my calculation and ignores the stated pull-forward effect.
- FieldOS software grew 27.1% in 2025, with 118% net revenue retention (2025 data only).

### Gaps and questions for management
1. Why was Hartwell & Pryce dismissed in November 2025? Provide Audit Committee minutes and the expanded audit scope they proposed.
2. For each Q4 2025 bill-and-hold contract: customer, amount, the substantive reason, the customer request letters, and how criterion (d) was met. Who are the customers behind the non-Norvale $7.2m?
3. Why did Norvale return $9.4m of product in May 2026? Has Norvale indicated how it would respond to a change of control? Provide Norvale's 2026 revenue and AR aging.
4. What are the current term loan balance, the Q3 2026 covenant calculation, and the add-back amounts against the 15% cap? Have lenders been approached about consent or payoff?
5. Has the board or Audit Committee started an investigation related to the securities class action? Is there an SEC inquiry? (Not found in SEC filings.)
6. What was the reason for Okafor's $900,000 separation payment? Did he raise any concerns before leaving? What is the status of the permanent CFO search?
7. What is the material weakness remediation timeline, and when will testing be done?
8. Provide FieldOS incident forensics, other customer claims, the SLA credit total and the cyber insurance coverage. Was a cyber incident current report filed? (Not found in SEC filings.)
9. Provide Vantor damages estimates, design-around options and settlement discussions.
10. Provide the Hale lease change-of-control rent reset mechanics and an estimated market rent. Is the sale process overseen by independent directors?
11. Is there an interim goodwill impairment assessment for Lumora after the guidance cut?
12. Provide the updated ARR and net revenue retention for 2026, and the bridge from the March to the August guidance.
13. Does a clawback policy apply to the 2025 bonuses?
