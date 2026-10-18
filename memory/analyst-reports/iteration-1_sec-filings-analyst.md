## SEC filings analyst: findings

### Files reviewed
All five files were read in full, plus the deal brief for context.
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-K_FY2025_excerpts.md` (filed March 9, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` (filed August 6, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_DEF14A_2026_excerpts.md` (filed April 24, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md` (dated November 14, 2025)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md` (dated January 21, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md` (context only)

Prompt-injection check: none of the SEC files contain text that tries to instruct the agents. Nothing to report.

Timing note: the newest SEC filing is the 10-Q filed August 6, 2026. Nothing after that date appears in these files, so the Q3 2026 covenant test (September 30, 2026) and anything that happened after August 6 are not found in SEC filings.

### Findings

#### SEC-01: The deal model uses a management case that has been withdrawn
- **Finding:** On August 6, 2026 the company replaced its March 2026 outlook with much lower guidance. The deal model still uses the March case ($560.0m revenue, $118.0m Adjusted EBITDA).
- **Evidence:** "We now expect full-year 2026 revenue of $470 million to $490 million and Adjusted EBITDA of $70 million to $78 million. This replaces the outlook we provided on March 9, 2026." The March outlook was $555m to $565m revenue and $114m to $122m Adjusted EBITDA.
- **Math:** Revenue midpoint goes from 560.0 to 480.0 (down 14.3%). Adjusted EBITDA midpoint goes from 118.0 to 74.0 (down 37.3%). The implied EV is 11.5 x 118.0 = about 1,357m. 1,357 / 74.0 = 18.3x new-guidance EBITDA. Implied H2 2026 Adjusted EBITDA is 70.0 to 78.0 minus H1 29.9 = 40.1 to 48.1, against H2 2025 of 98.8 - 39.0 = 59.8.
- **Source:** 10-Q, section "Updated 2026 outlook"; 10-K, section "2026 outlook (as of March 9, 2026)"; deal brief, "Valuation basis".
- **Severity:** Critical
- **Confidence:** High. Stated directly in the primary filings, and the numbers are recomputed.
- **Deal impact:** Valuation. At the same EV, the multiple rises from 11.5x to about 18.3x.
- **Cross-check:** Financial data: the Q3 2026 actuals and whether the deal model v3 (September 2026) reflects the cut. News: analyst reaction and any further guidance changes.

#### SEC-02: Q4 2025 bill-and-hold revenue inflated reported growth, and part of it has already been reversed
- **Finding:** $31.8m of Q4 2025 hardware revenue was booked under bill-and-hold, and $24.6m of that was with the largest customer (Norvale). In May 2026, $9.4m of it was returned to inventory and credited back. The 10-Q now also says customers "pulled forward" orders into Q4 2025.
- **Evidence:** 10-K Note 2: "$31.8 million of hardware revenue under bill-and-hold arrangements (2024: none material). Of this amount, $24.6 million related to our largest customer." 10-Q: products worth $9.4m "were returned to our inventory, and we issued a credit for the same amount."
- **Math:** 31.8 / 154.4 = 20.6% of Q4 2025 revenue. Q4 2024 revenue = 154.4 / 1.324 = 116.6. Excluding bill-and-hold, Q4 2025 was 122.6, which is +5.1% year over year against the reported +32.4%. FY2025 excluding bill-and-hold was 470.5, which is +11.6% against the reported +19.1%. Norvale's share was 24.6 / 31.8 = 77.4% of the bill-and-hold revenue, and 9.4 / 24.6 = 38.2% of Norvale's bill-and-hold was reversed. The remaining $22.4m was delivered by June 30, 2026.
- **Source:** 10-K, "Note 2. Revenue Recognition" and "Item 7 ... 2025 highlights"; 10-Q, "Revenue" and "Bill-and-hold amendment".
- **Interpretation:** The return of goods is hard to square with criterion (d), "we cannot use the products or direct them to another customer", and with the "substantive" reason test. The company booked the credit in Q2 2026 and did not restate 2025. A restatement risk may remain. This is my inference, not a statement in the filings.
- **Severity:** Critical
- **Confidence:** High. The amounts come from the filings and are recomputed. The restatement risk is an interpretation (Medium).
- **Deal impact:** Valuation (the growth quality behind IC question 1), disclosure, and post-closing (restatement or SEC inquiry).
- **Cross-check:** Financial data: the quarterly revenue split, inventory movements and the margin on the bill-and-hold units. Litigation: whether the securities class action cites bill-and-hold. News: any SEC inquiry or reporting on Norvale's orders.

#### SEC-03: The prior auditor flagged a material weakness and planned a wider audit, then was dismissed before Q4 closed
- **Finding:** In Q3 2025, Hartwell & Pryce (auditor since 2016) told the Audit Committee about a material weakness and said Q4 non-standard deals would need expanded audit procedures. It was dismissed on November 10, 2025. Linden Barr was engaged two days later. Q4 then included $31.8m of bill-and-hold revenue.
- **Evidence:** "additional audit procedures would be required for revenue arrangements with these terms expected in the fourth quarter of 2025, which would expand the scope of its audit." The 8-K reports "no disagreements", and Hartwell & Pryce's Exhibit 16.1 letter agrees with the disclosure.
- **Source:** 8-K dated 2025-11-14, Item 4.01, "Reportable event"; 10-K header and Item 9A.
- **Interpretation:** The timing looks like possible opinion shopping. The filings give no reason for the dismissal. That is my inference. The "no disagreements" statement is formally correct, but the reportable event is the substance.
- **Severity:** High
- **Confidence:** High on the facts (primary 8-K). Medium on the motive (inferred).
- **Deal impact:** Disclosure and post-closing (control environment, restatement risk).
- **Cross-check:** News: reporting on the dismissal. Litigation: whether the securities complaint relies on the auditor change. Ask for the Audit Committee minutes and the Hartwell & Pryce communications.

#### SEC-04: The material weakness is still not remediated, and disclosure controls were not effective at June 30, 2026
- **Finding:** The material weakness covers review of hardware contracts with non-standard delivery and acceptance terms, including bill-and-hold. It was first identified in Q3 2025. Linden Barr gave an adverse ICFR opinion for FY2025. At Q2 2026 it was still unremediated, with an interim CFO signing the certifications.
- **Evidence:** 10-K: "Linden Barr LLP issued an adverse opinion on the effectiveness of our internal control over financial reporting." 10-Q: "has not yet been remediated ... disclosure controls and procedures were not effective as of June 30, 2026."
- **Source:** 10-K, "Item 9A"; 10-Q, "Part I, Item 4" and header (certifications).
- **Severity:** High
- **Confidence:** High. Stated directly in the primary filings.
- **Deal impact:** Post-closing (integration under Arbelion's SOX), disclosure, and it supports a specific indemnity or escrow.
- **Cross-check:** Financial data: whether the Q2 2026 numbers needed adjustments. News or litigation: whether the class action cites the controls.

#### SEC-05: The leverage covenant steps down to 3.00x from Q3 2026, and headroom is thin on the new guidance
- **Finding:** The maximum Total Net Leverage Ratio falls from 3.50x to 3.00x for quarters ending on or after September 30, 2026. The ratio was 2.26x at June 30, 2026, but trailing EBITDA is falling and debt is rising.
- **Evidence:** The covenant is "no more than 3.00 to 1.00 for each fiscal quarter ending on or after September 30, 2026." Cash netting is "capped at $25.0 million". Permitted Add-backs "may not exceed 15% of Consolidated EBITDA" before the add-backs.
- **Math (my estimate; the June 30 term loan balance is not disclosed):** Debt is about 185.0 term loan plus 45.0 revolver = 230.0. Less capped cash of 25.0 (actual cash was 33.9), net debt is about 205.0. 205.0 / 2.26 = about 90.7 implied Consolidated EBITDA. That matches TTM Adjusted EBITDA: 98.8 - 39.0 + 29.9 = 89.7. At 3.00x, EBITDA can fall only to about 68.3 (205.0 / 3.00) before a breach, assuming flat net debt. On the new FY2026 guidance, December 2026 TTM EBITDA is 70.0 to 78.0, so 205.0 / 70.0 = 2.93x and 205.0 / 74.0 = 2.77x. More revolver draws or a binding 15% add-back cap would push the ratio higher.
- **Source:** 10-K, "Note 9. Debt" (covenant and definitions); 10-Q, "Liquidity and capital resources" and "Covenant compliance".
- **Severity:** High
- **Confidence:** Medium. The covenant terms are primary. The headroom figures are estimates because the June 30 term loan balance and the add-back amounts are not disclosed.
- **Deal impact:** Closing risk (a default or waiver before closing) and valuation (cost of a waiver).
- **Cross-check:** Financial data: the Q3 2026 covenant certificate, the add-back schedule, and the term loan balance. News: any waiver or amendment. Not found in SEC filings: Q3 2026 test results, waivers or amendments after August 2024.

#### SEC-06: A change of control triggers default on all debt and a Norvale termination right
- **Finding:** Under the credit agreement, a change of control is an event of default, so about $230m of debt would need repayment or refinancing at closing. Norvale (31.1% of revenue) may terminate on 90 days' notice after a change of control, and it has no minimum purchase commitment.
- **Evidence:** "A change of control of Talonfield is an event of default." "The Norvale MSA allows Norvale to terminate the agreement on 90 days' notice if Talonfield undergoes a change of control. Norvale is not required to purchase any minimum volume." The MSA runs through September 30, 2027.
- **Math:** Norvale revenue was 31.1% x 502.3 = 156.2 in 2025 (2024: 28.0% x 421.7 = 118.1, so +32.3%). Excluding its 24.6 of bill-and-hold, Norvale was 131.6, or +11.4%. Revenue excluding Norvale grew from 303.6 to 346.1 (+14.0%). Norvale also accounted for 38% of gross AR: 0.38 x 121.5 = about 46.2, against 0.29 x 76.3 = about 22.1 in 2024.
- **Source:** 10-K, "Item 1. Business (Customers)", "Item 1A" (Norvale risk factor), "Note 9" and "Note 13".
- **Severity:** Critical (Norvale), High (debt refinancing, which is manageable because the buyer is funding cash)
- **Confidence:** High. Stated in the primary filing, with numbers recomputed.
- **Deal impact:** Closing risk and valuation. Possible protections are a closing condition on Norvale consent or a waiver, and refinancing in sources and uses.
- **Cross-check:** News: Norvale's own strategy, other suppliers or dual-sourcing, any dispute over the returned $9.4m. Financial data: monthly Norvale revenue and AR collections. The 10-Q excerpts do not update Norvale's status.

#### SEC-07: Legal exposure has grown: securities class action, Pinecrest $12.0m, and Vantor injunction risk on Gen-3
- **Finding:** As of August 6, 2026, the disclosed cases are:
  - Vantor patent suit: trial in March 2027, no accrual. It seeks an injunction against Gen-3.
  - Securities class action filed June 3, 2026, naming the CEO and former CFO. The filings state no accrual or amount for it.
  - Pinecrest suit filed June 17, 2026, seeking $12.0m. The filings state no accrual for it.
  - Ruiz: $3.2m accrued, with preliminary approval on May 20, 2026.
- **Evidence:** Vantor: "seeks damages and an injunction"; "we have not recorded an accrual." The class action alleges "false or misleading statements about our revenue and our internal controls."
- **Math:** Gen-3 is about 70% of hardware revenue: 0.70 x 301.4 = about 211.0, or 42.0% of 2025 total revenue, exposed to an injunction.
- **Source:** 10-K, "Item 3. Legal Proceedings" and "Item 1A"; 10-Q, "Part II, Item 1. Legal Proceedings" and "Part II, Item 1A".
- **Severity:** High (Vantor injunction and the class action). Pinecrest is Medium on its own.
- **Confidence:** High on what is disclosed. The size of any exposure is not in the filings.
- **Deal impact:** Valuation, closing risk (an injunction before closing) and indemnity or escrow.
- **Cross-check:** Litigation: the docket status after August 6, claim construction or summary judgment rulings in Vantor, the class period and the bill-and-hold allegations in the securities complaint, and Pinecrest pleadings. News: settlement reports.

#### SEC-08: The cyber incident was called "not material", but costs and claims add up
- **Finding:** FieldOS was taken offline for up to three days in April 2026 after unauthorized activity. The company concluded the incident was "not material". Direct costs are $1.8m plus $2.3m of credits, and a customer is suing for $12.0m. The $1.8m is added back to Adjusted EBITDA.
- **Evidence:** "we concluded that the incident was not material, and we have not identified evidence that customer data was taken." The $1.8m is "included in 'other non-recurring items' in our Adjusted EBITDA reconciliation."
- **Math:** 1.8 + 2.3 + 12.0 = 16.1 of combined cost and claim exposure. 2.3 / 112.9 = 2.0% of Q2 revenue.
- **Source:** 10-Q, "April 2026 service disruption", "Revenue" and "Legal Proceedings (Pinecrest)".
- **Interpretation:** The 10-Q says the only risk factor change is the securities litigation addition. The cyber risk factor in the 10-K is written as hypothetical, but the risk has now happened. That framing may be stale.
- **Severity:** Medium
- **Confidence:** High on the facts. The materiality judgment is the company's own.
- **Deal impact:** Disclosure and post-closing (FieldOS security, customer retention).
- **Cross-check:** News: customer reports, data exfiltration claims, any 8-K Item 1.05 (not found in SEC filings). Litigation: other customer suits. Financial data: FieldOS churn after April.

#### SEC-09: Underlying Q2 2026 trend and cash conversion are weak, and the 10-K's statement on collections did not hold
- **Finding:** Q2 2026 revenue fell 4.0%, gross margin dropped 3.3 points, and the company had a net loss. The 10-K said, "We expect collections to normalize in 2026", but H1 2026 operating cash flow was negative and the revolver was drawn further.
- **Evidence:** H1 2026 operating cash flow was "negative $4.2 million". Revolver: $45.0m outstanding, with $25.8m available after $4.2m of letters of credit. Cash was $33.9m.
- **Math:**
  - Q2 2026 adjusted for the two one-offs: 112.9 + 9.4 + 2.3 = 124.6, which is +6.0% against 117.6.
  - Gross AR grew 59.2% in 2025 (76.3 to 121.5) while revenue grew 19.1%.
  - The credit loss allowance fell from 3.8% of gross AR (2.9 / 76.3) to 2.1% (2.6 / 121.5), explained as "improved collection experience".
  - FY2025 operating cash flow was 9.7, or 9.8% of Adjusted EBITDA (9.7 / 98.8).
- **Source:** 10-Q, "Results summary", "Revenue" and "Liquidity"; 10-K, "Liquidity" and "Note 5".
- **Severity:** High
- **Confidence:** High. Primary filings, with numbers recomputed.
- **Deal impact:** Valuation (quality of earnings) and liquidity at closing.
- **Cross-check:** Financial data: AR aging by customer (especially Norvale), DSO and Q3 cash flow.

#### SEC-10: Single-trigger equity vesting and a CFO payout described as a resignation
- **Finding:** All unvested executive equity vests at a change of control whether or not the executive leaves. That totals $17.6m, within $28.6m of estimated change-in-control payments. Former CFO Okafor "resigned" with "no disagreement" but received $900,000 and signed a general release. He is now a defendant in the securities class action.
- **Evidence:** "all unvested equity awards held by executive officers vest in full immediately upon a change in control ('single-trigger'), whether or not the executive's employment ends." 8-K: "a cash payment of $900,000 and a general release of claims."
- **Interpretation:** A cash payment for a voluntary resignation is unusual. Okafor resigned about two months after the auditor change and seven weeks before the 10-K with the adverse ICFR opinion was filed. The timing link is my inference. The interim CFO was still interim at August 6, 2026.
- **Source:** DEF 14A, "Potential payments upon a change in control"; 8-K dated 2026-01-21, Item 5.02; 10-K, "Note 18"; 10-Q, header.
- **Severity:** Medium (cost). High for the governance signal when combined with SEC-03 and SEC-04.
- **Confidence:** High on the facts. Medium on the interpretation.
- **Deal impact:** Valuation (about 28.6m of transaction cost), post-closing retention (vested executives have less reason to stay), disclosure.
- **Cross-check:** News: reports on why Okafor left and the CFO search. Litigation: Okafor's role in the securities complaint.

#### SEC-11: The 2025 bonus paid at 142% of target relied on bill-and-hold revenue
- **Finding:** Executives earned 142% of target on 2025 revenue of $502.3m and Adjusted EBITDA of $98.8m. Without the $31.8m of bill-and-hold revenue, revenue would have been $470.5m, just $0.5m above the $470.0m threshold.
- **Evidence:** Revenue threshold/target/max: 470.0 / 490.0 / 510.0, actual 502.3. Adjusted EBITDA: 88.0 / 95.0 / 102.0, actual 98.8. "bonus payouts at 142% of target for all executive officers."
- **Math (illustrative, my assumption):** If the bill-and-hold units carried about the FY2025 H1 gross margin of 40.8%, then 31.8 x 0.408 = about 13.0 of profit. 98.8 - 13.0 = about 85.8, which is below the 88.0 EBITDA threshold. Removing only the reversed 9.4: revenue 492.9, still above target. The payout curve is not disclosed. A clawback policy is not found in SEC filings.
- **Source:** DEF 14A, "2025 annual incentive plan"; 10-K, "Note 2".
- **Severity:** Medium
- **Confidence:** High on the reported figures. Low to Medium on the EBITDA sensitivity, which depends on an assumed margin.
- **Deal impact:** Governance and disclosure. It points to an incentive to pull revenue forward.
- **Cross-check:** Financial data: the margin on the bill-and-hold units. Ask about the clawback policy and whether it applies after the $9.4m reversal.

#### SEC-12: Related-party HQ lease lets the CEO's family landlord reset rent at a change of control
- **Finding:** The HQ and main assembly facility are leased from an entity controlled by CEO Hale's family through December 2033. After a change of control, the landlord can reset rent to fair market value using an appraiser the landlord picks. Hale is also Chairman, owns 14.2%, and there is no lead independent director.
- **Evidence:** "a change in control of Talonfield allows the landlord to reset the rent to 'fair market value', as determined by an appraiser selected by the landlord." 2025 rent was $2.1m with 3% annual increases.
- **Math:** Hale's stake: 6.69m shares x $24.00 = about 160.6m in deal proceeds. Remaining base rent over 2026 to 2033 at 3% escalation is about 2.1 x (1.03 + ... + 1.03^8) = about 19.2m, before any reset.
- **Source:** DEF 14A, "Certain relationships and related party transactions", "Security ownership" and "Board of Directors".
- **Severity:** Medium
- **Confidence:** High. Primary filing. The rent total is computed.
- **Deal impact:** Post-closing cost and negotiation dynamics with the CEO. A possible protection is a lease amendment as a closing deliverable.
- **Cross-check:** News: Hale's other dealings. Ask for the lease and an independent rent appraisal.

#### SEC-13: Other inherited risks: single-source LiDAR in China, and goodwill at risk after the guidance cut
- **Finding:** All Talon AMR LiDAR sensors come from one China-based supplier with no qualified second source. Goodwill of $98.4m includes $57.4m from Lumora, last tested October 1, 2025. The 10-Q excerpts do not mention an interim impairment test after the guidance cut.
- **Evidence:** "We do not currently have a qualified second source." The October 1, 2025 test "found no impairment."
- **Source:** 10-K, "Item 1 (Suppliers)", "Item 1A" and "Note 15"; the 10-Q excerpts do not address goodwill.
- **Severity:** Medium
- **Confidence:** High on the disclosures. Medium on the impairment risk (inferred).
- **Deal impact:** Post-closing (supply chain, tariffs) and purchase accounting.
- **Cross-check:** News: tariff actions on Chinese LiDAR. Financial data: Lumora revenue performance.

#### SEC-14: Things management stopped saying between the 10-K and the 10-Q
- **Finding:** The 10-Q excerpts drop several items the 10-K featured:
  - FieldOS ARR ($139.2m) and net revenue retention (118%) are no longer reported.
  - The Norvale and concentration update is missing.
  - The 10-Q does not name the "largest customer" behind the $9.4m reversal (the 10-K identifies the largest customer as Norvale).
  - Q4 2025 is re-described: from "strong hardware deliveries to enterprise customers" to "orders that customers pulled forward into the fourth quarter of 2025."
  - The 10-Q says risk factors are unchanged except for securities litigation, despite the cyber incident, the guidance cut, the bill-and-hold reversal and the covenant step-down.
  - Remaining performance obligations or backlog: not found in either filing.
- **Source:** 10-K, "Item 1", "Item 7"; 10-Q, "Revenue" and "Part II, Item 1A".
- **Severity:** Medium
- **Confidence:** Medium. The documents are excerpts, so the omissions may reflect excerpting rather than the full filings.
- **Deal impact:** Disclosure. It also feeds the securities litigation risk.
- **Cross-check:** Financial data: ARR and NRR trend for 2026. News: what management said at the investor day and on the Q2 call.

### Positive or mitigating points
- Hartwell & Pryce's Exhibit 16.1 letter agrees with the 8-K, and there were "no disagreements". Its prior opinions were clean (8-K Item 4.01).
- $22.4m of the remaining bill-and-hold products had been delivered by June 30, 2026 (10-Q).
- The covenant was met at June 30, 2026 (2.26x against 3.50x), and remediation steps have started: a director of technical accounting and a contract review committee (10-Q; 10-K Item 9A).
- Cash severance is double-trigger (DEF 14A). Okafor is "not eligible for change-in-control payments."
- Ruiz is capped at the $3.2m accrued, with preliminary approval granted (10-Q).
- The buyer is paying cash, so the change-of-control debt default can be handled by refinancing at closing.
- Q2 2026 revenue excluding the $9.4m reversal and $2.3m of credits was +6.0% year over year.
- Most of the Board is independent: five of seven directors (DEF 14A).

### Gaps and questions for management
1. Why was Hartwell & Pryce dismissed, and what did the Audit Committee minutes say? Did Linden Barr review the Q4 2025 bill-and-hold contracts before they were booked?
2. Name the customers behind the $31.8m of bill-and-hold revenue and the $9.4m return. Was it Norvale? What was the "substantive" reason, and why were goods "returned to our inventory" if criterion (d) was met? Is a restatement being considered?
3. What was the Q3 2026 Total Net Leverage Ratio? Please provide the add-back schedule (including the 15% cap test), the June 30 term loan balance, and any waiver or amendment talks. Not found in SEC filings.
4. Has Norvale said anything about the change-of-control termination right, a renewal after September 2027, or the dispute over the returned units? What are Norvale's AR aging and collections?
5. Why did Okafor resign, and why was he paid $900,000? What is the status of the permanent CFO search?
6. Is there an accrual or estimated range for the securities class action and Pinecrest? What are insurance coverage and D&O retention?
7. What is the Vantor status after August 6 (claim construction, any design-around for Gen-3), and what is the contingency plan if an injunction is granted?
8. What are FieldOS ARR, NRR and churn after the April 2026 incident? Was any customer data taken? Was an 8-K Item 1.05 considered?
9. Has goodwill been tested for interim impairment after the August guidance cut?
10. Will management amend the Hale Family Properties change-of-control rent reset? Does a clawback apply to 2025 bonuses?
11. What are remaining performance obligations or backlog? Not found in SEC filings.
12. Is there any LiDAR second-source qualification plan, and what is the tariff exposure?
