<!-- Iteration 2, saved unedited by the lead agent on 2026-10-18. -->

## SEC filings analyst: findings (iteration 2, narrow follow-up)

### Files reviewed

I read all five files in full, plus the deal brief for context.
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-K_FY2025_excerpts.md` (filed March 9, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` (filed August 6, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_DEF14A_2026_excerpts.md` (filed April 24, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md` (context only)

None of these files contains text that tries to instruct the agents.

**Short answers to the six tasks**
1. The full Vantor text in the Q2 2026 10-Q is three sentences, quoted in SEC-024. No SEC filing mentions the July 22, 2026 claim construction order or a loss estimate or range. The only accrual statement is "we have not recorded an accrual." The 10-Q drops the 10-K's ASC 450 wording. None of the filings uses the phrase "reasonably possible."
2. Quoted in SEC-027 and SEC-028. The 10-K describes the criteria in general terms only. It never says who asked for the Q4 2025 arrangements, what the reason was, or that the criteria were met.
3. Not found in SEC filings: Q3 2025 results, their release dates, Q3 or Q4 2025 quarterly EBITDA, any waiver, and any forward-looking statement about the September 30, 2026 test beyond the step-down itself (SEC-031, SEC-032).
4. The 10-K excerpt has no Item 1C. The only cyber text is a risk factor written as a hypothetical. It describes no controls, so I cannot show a direct contradiction (SEC-033).
5. The only text on who requested bill-and-hold is a general phrase in Note 2. The bonus table is quoted in SEC-030.
6. No. March 10, 2025 does not match any filing date in the SEC files (SEC-034).

### Findings

#### SEC-024: The Q2 2026 10-Q does not mention the adverse claim construction order issued 15 days before filing
- **Finding:** The 10-Q's entire Vantor disclosure is three sentences. It does not mention the July 22, 2026 Markman order, which according to the docket the lead agent supplied adopted Vantor's construction for three of four terms. The 10-Q says only that the case "is in discovery."
- **Evidence:** The complete text reads: "*Vantor Robotics, Inc. v. Talonfield Systems, Inc.* The case is in discovery. Trial is currently scheduled for March 2027. We continue to believe the claims are without merit, and we have not recorded an accrual." The 10-Q was filed August 6, 2026, which is 15 days after July 22, 2026. The 10-Q also says "There have been no material changes to the risk factors in our 2025 Form 10-K, except for" the new securities litigation risk factor. So the patent risk factor was not updated.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "Part II, Item 1. Legal Proceedings" and "Part II, Item 1A. Risk Factors"
- **Severity:** High. This is a disclosure gap. The underlying exposure may be Critical (see SEC-026).
- **Confidence:** High for what the filing says and leaves out, which comes from the primary source. Confirming the order's date and content depends on the LIT-001 docket.
- **Deal impact:** Disclosure, valuation and closing risk. The gap may also support the securities class action theory or extend its class period.
- **Cross-check:** Check in the litigation docket that the Markman order was entered on the public docket before August 6, 2026. Check news for any Talonfield 8-K or press release about the order. Ask whether the Audit Committee or disclosure committee discussed it before the 10-Q was certified.

#### SEC-025: The 10-Q drops the 10-K's ASC 450 wording, and no filing gives a loss range
- **Finding:** The 10-K said a loss was not probable and could not be estimated. The 10-Q keeps only "we have not recorded an accrual." It drops both the probability statement and the "cannot reasonably estimate" statement. It gives no "reasonably possible" assessment and no range. No SEC filing mentions the $96.4 million damages figure (September 4, 2026), the addition of Gen-3 Plus (August 14, 2026) or the injunction request. All three came after the 10-Q, and the SEC folder holds no later filing.
- **Evidence:** 10-K: "We have not recorded an accrual because we do not believe a loss is probable, and we cannot reasonably estimate a possible loss or range of loss." 10-Q: "we have not recorded an accrual." The phrase "reasonably possible" does not appear in any SEC file.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 3. Legal Proceedings"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1. Legal Proceedings"
- **Severity:** High
- **Confidence:** High. This is a direct text comparison of two primary sources.
- **Deal impact:** Disclosure and valuation. After the Markman order, a "reasonably possible" assessment with a range would be expected. The Q3 2026 10-Q (due about early November, near the November 6 IC meeting) may show a large change in tone.
- **Cross-check:** Ask management and auditor Linden Barr for the current ASC 450 assessment and any range estimate. Compare it with the $96.4 million expert figure in LIT-001.

#### SEC-026: The product line at risk from the injunction is about 42% of 2025 revenue
- **Finding:** The 10-K says Gen-3 was about 70% of hardware revenue. That implies about $211.0 million, or about 42% of 2025 total revenue, is tied to the product Vantor wants to enjoin. The 10-K already warns the company could have to "stop selling Talon Gen-3 robots."
- **Evidence:** "Talon Gen-3 ... represented approximately 70% of hardware revenue in 2025." 0.70 x 301.4 = 211.0; 211.0 / 502.3 = 42.0% of revenue. The damages claim (from LIT-001, as given) of 96.4 / 1,159 = 8.3% of implied equity value, and 96.4 / 33.9 = 2.8x June 30, 2026 cash.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 1. Business" and "Item 1A. Risk Factors"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources"
- **Severity:** Critical. An injunction on a product line worth about 42% of revenue, together with damages of about 8.3% of equity value, could change value by more than 10%.
- **Confidence:** Medium. The revenue share is from a primary source, and "approximately 70%" is an approximation. The outcome of the injunction request is uncertain.
- **Deal impact:** Valuation, closing risk (possible condition or special indemnity or escrow) and post-closing (redesign cost).
- **Cross-check:** Ask the financial analyst for Gen-3 and Gen-3 Plus revenue by quarter. Ask the litigation analyst for the injunction briefing schedule and any design-around status.

#### SEC-027: The 10-K lists the bill-and-hold criteria but never says who asked, why, or that the criteria were met
- **Finding:** Note 2 describes the arrangements in general terms ("a customer asks us"). It lists criteria (a) to (d) as a policy. It does not say who requested the Q4 2025 arrangements, what the substantive reason was, or that each criterion was met. No filing in the folder answers these points.
- **Evidence:** "In some cases a customer asks us to hold finished products at our facilities until the customer's site is ready." Criteria: "(a) the reason for the arrangement is substantive, (b) the products are separately identified as belonging to the customer, (c) the products are ready for physical transfer, and (d) we cannot use the products or direct them to another customer." Amounts: "$31.8 million ... Of this amount, $24.6 million related to our largest customer ... these products remained in our warehouses." 31.8 / 154.4 = 20.6% of Q4 2025 revenue; 24.6 / 31.8 = 77.4% from the largest customer (Norvale, per Item 1).
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 2. Revenue Recognition (excerpt)" and "Item 1. Business"
- **Severity:** High
- **Confidence:** High. The text comes from the primary source. The absence of any statement about the requester or the reason is confirmed across all five files.
- **Deal impact:** Valuation (quality of FY2025 revenue) and disclosure (restatement risk).
- **Cross-check:** Request the signed customer bill-and-hold request letters, the warehouse segregation records, and the Linden Barr audit workpapers or a summary. Check news for former-employee accounts of who started the arrangements.

#### SEC-028: The $9.4 million return was booked as a Q2 2026 revenue reduction, not a correction of 2025
- **Finding:** Goods recognized as revenue in Q4 2025 were returned to Talonfield's inventory under a May 2026 amendment. The company booked the credit as Q2 2026 revenue reduction and did not revise 2025. Returning goods to inventory is hard to reconcile with criterion (d) ("we cannot use the products or direct them to another customer") and raises the question of whether the original reason was substantive. That is my interpretation, not the company's.
- **Evidence:** "products with a sales value of $9.4 million that we had recognized as revenue under a bill-and-hold arrangement in the fourth quarter of 2025 were returned to our inventory, and we issued a credit for the same amount. We recorded the credit as a reduction of revenue in the second quarter of 2026." Also: "The remaining $22.4 million ... had been delivered to customers as of June 30, 2026." Check: 31.8 - 9.4 = 22.4. Also 9.4 / 24.6 = 38.2% of the largest customer's bill-and-hold amount. The 10-Q does not say whether the $9.4 million was part of the $24.6 million, but it involved the same "largest customer."
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part I, Item 2", "Bill-and-hold amendment" and "Revenue"
- **Severity:** High
- **Confidence:** High for the facts. Medium for the interpretation about criterion (d).
- **Deal impact:** Valuation and disclosure. FY2025 revenue may be overstated, and Q2 2026 is understated by the same amount.
- **Cross-check:** Ask whether the auditor considered an error correction under ASC 250. Ask for the amendment's terms and why Norvale returned the goods. Check news and the class action complaint (LIT-003) for how they describe this event.

#### SEC-029: The 10-K described "deliveries" of products that were still in Talonfield's warehouses; the 10-Q later admits a pull-forward
- **Finding:** The 10-K MD&A credits record Q4 revenue to "strong hardware deliveries." Note 2 says the bill-and-hold products, 20.6% of Q4 revenue, had not left Talonfield's warehouses. The 10-Q adds new language that customers "pulled forward" orders into Q4 2025.
- **Evidence:** 10-K: "Record fourth-quarter revenue of $154.4 million, up 32.4% year over year, driven by strong hardware deliveries to enterprise customers." 10-K Note 2: "these products remained in our warehouses." 10-Q: "orders that customers pulled forward into the fourth quarter of 2025." My calculation: Q4 2024 = 154.4 / 1.324 = 116.6; Q4 2025 excluding bill-and-hold = 154.4 - 31.8 = 122.6, which is growth of 5.1% instead of 32.4%. FY2025 excluding bill-and-hold = 470.5, which is growth of 11.6% instead of 19.1%.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 7" and "Note 2"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Revenue"
- **Severity:** High
- **Confidence:** High. The quotes come from primary sources and the numbers are recomputed.
- **Deal impact:** Valuation (underlying growth) and disclosure (supports the class action theory).
- **Cross-check:** Compare with the financial analyst's quarterly revenue data and with the LIT-003 complaint's alleged misstatements.

#### SEC-030: Revenue excluding bill-and-hold is $0.5 million above the bonus threshold; executives were paid at 142%
- **Finding:** The proxy shows 2025 revenue of $502.3 million against a $490.0 million target. Without the $31.8 million of Q4 bill-and-hold revenue, revenue would have been $470.5 million, only $0.5 million above the $470.0 million threshold. Without only the $9.4 million later returned, revenue would have been $492.9 million, still above target. The proxy was filed April 24, 2026, before the May 2026 amendment. It mentions no clawback. Neither the 10-K nor the proxy says who requested the bill-and-hold arrangements, beyond Note 2's "a customer asks us."
- **Evidence:** Proxy table: "Revenue ($ millions) | 470.0 | 490.0 | 510.0 | 502.3" and "Adjusted EBITDA ($ millions) | 88.0 | 95.0 | 102.0 | 98.8". "each weighted 50%". "the Compensation Committee approved bonus payouts at 142% of target for all executive officers." 502.3 - 31.8 = 470.5. The proxy does not disclose payout percentages at threshold or maximum, so I cannot recompute the 142%. The EBITDA effect of bill-and-hold is not disclosed.
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, "2025 annual incentive plan"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 2"
- **Severity:** High. This is a governance and incentive issue, and the facts are relevant to the class action.
- **Confidence:** High for the numbers. The incentive link is my interpretation.
- **Deal impact:** Governance, disclosure and post-closing (clawback policy and management retention terms).
- **Cross-check:** Ask for the clawback policy (Rule 10D-1) and the payout curve. Check news for any shareholder or proxy-adviser criticism and the LIT-003 complaint for scienter allegations tied to bonuses.

#### SEC-031: Not found in SEC filings: Q3 2025 results, their dates and quarterly EBITDA for H2 2025
- **Finding:** No file gives Q3 2025 results, an earnings release date, or Q3 or Q4 2025 EBITDA. The only quarterly data is in the 10-Q. From it I derive Q1 figures and H2 2025 Adjusted EBITDA.
- **Evidence:** 10-Q table: Adjusted EBITDA Q2 2026 13.8; Q2 2025 20.6; H1 2026 29.9; H1 2025 39.0. Derived: Q1 2026 = 29.9 - 13.8 = 16.1; Q1 2025 = 39.0 - 20.6 = 18.4; H2 2025 = 98.8 - 39.0 = 59.8. Trailing twelve months (TTM) Adjusted EBITDA at June 30, 2026 = 98.8 - 39.0 + 29.9 = 89.7. The 8-K places the material weakness in Q3 2025 ("During the third quarter of 2025, Hartwell & Pryce advised the Audit Committee"), but gives no results.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Results summary"; `data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md`, "Reportable event"
- **Severity:** Medium
- **Confidence:** High for the derived figures. The absence of the other data is confirmed.
- **Deal impact:** Valuation and debt analysis.
- **Cross-check:** The financial analyst should supply quarterly EBITDA for Q3 and Q4 2025 so the September 30 and December 31, 2026 covenant tests can be modeled.

#### SEC-032: The September 30, 2026 step-down to 3.00x is disclosed, but no waiver or forward assessment is
- **Finding:** The 10-Q reports 2.26x at June 30 and notes the step-down. It says nothing about expected compliance, a waiver or an amendment. My rough estimate, below, suggests headroom is thin under the cut guidance.
- **Evidence:** "Our Total Net Leverage Ratio was 2.26 to 1.00 at June 30, 2026 ... Beginning with the quarter ending September 30, 2026, the maximum ratio decreases to 3.00 to 1.00." The 10-K says cash netting is "capped at $25.0 million." Add-backs "may not exceed 15%." The 10-K also says "A change of control ... is an event of default." Headroom at constant net debt: 1 - 2.26 / 3.00 = 24.7% fall in Consolidated EBITDA. Estimate (the June 30 term loan balance is not disclosed; I assume about $185.0 million): debt about 185.0 + 45.0 = 230.0, less 25.0 of capped cash = 205.0 net debt. That implies Consolidated EBITDA of about 205.0 / 2.26 = 90.7, which matches TTM Adjusted EBITDA of 89.7. At FY2026 guidance of $70 million to $78 million, the December 31, 2026 ratio would be about 205.0 / 78 = 2.63x to 205.0 / 70 = 2.93x. If Adjusted EBITDA is used as a stand-in for Consolidated EBITDA, H2 2026 implied by guidance is 40.1 to 48.1, against H2 2025 of 59.8. Revolver availability is $25.8 million. The word "waiver" does not appear in any SEC file.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Covenant compliance", "Liquidity and capital resources" and "Updated 2026 outlook"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 9. Debt"
- **Severity:** High. The debt is cured by refinancing at closing, since change of control is an event of default. It would become Critical if a breach occurs at September 30 or December 31, 2026, before closing.
- **Confidence:** Medium. The covenant terms come from the primary source, but the net debt and EBITDA path are my estimates.
- **Deal impact:** Closing risk and liquidity before closing. The deal needs a payoff letter and refinancing at closing.
- **Cross-check:** Ask for the Q3 2026 compliance certificate, the June 30 term loan balance and any lender communications. Check news for reports of an amendment or waiver.

#### SEC-033: The 10-K cyber disclosure is hypothetical, has no Item 1C in the excerpts, and was not updated after the April incident
- **Finding:** The 10-K excerpts contain no Item 1C. The only cyber text is a risk factor written as something that "could" happen. It describes no controls, so a direct contradiction of described controls cannot be shown from the SEC files. The 10-Q concluded the incident "was not material," filed no 8-K Item 1.05 (none is in the folder), and stated "no material changes" to risk factors other than securities litigation. The disclosed costs plus the Pinecrest claim total $16.1 million.
- **Evidence:** 10-K: "An outage or attack could stop customers' robot fleets, expose us to service level credits and claims, and damage our reputation." 10-Q: "interrupted fleet operations for some customers for up to three days" and "we concluded that the incident was not material." Costs: 1.8 response + 2.3 credits + 12.0 Pinecrest claim = 16.1. The 10-Q's "some customers" compares with the news report (as given) of "at least 40 customer sites."
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 1A. Risk Factors"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "April 2026 service disruption", "Part II, Item 1" and "Part II, Item 1A"
- **Severity:** Medium
- **Confidence:** High that Item 1C is missing from the excerpts, which do not include it. Medium on the materiality question.
- **Deal impact:** Disclosure (possible SEC cyber disclosure scrutiny) and post-closing (FieldOS security remediation).
- **Cross-check:** Request the full 10-K Item 1C and the incident forensic report. Compare the number of sites in the news with the 10-Q. Check for other customer claims beyond Pinecrest.

#### SEC-034: The class period start date (March 10, 2025) does not match any filing in the SEC folder
- **Finding:** No SEC file is dated March 10, 2025. The nearest is the FY2025 10-K, filed March 9, 2026, exactly one year and one day later. The FY2024 10-K, which might match, is not in the folder. The class period end, May 12, 2026, also matches no file here. The Q1 2026 10-Q and any May 2026 release are not in the folder.
- **Evidence:** 10-K: "Filed: March 9, 2026." Other filing dates: 8-K November 14, 2025; 8-K January 21, 2026; proxy April 24, 2026; 10-Q August 6, 2026.
- **Source:** All five files, header sections
- **Severity:** Medium
- **Confidence:** High that no file matches. Low for any explanation, for example that the date anchors to a FY2024 10-K or press release, or that one source has a year error.
- **Deal impact:** Disclosure and litigation exposure. The class period determines potential damages.
- **Cross-check:** The litigation analyst should check what statement the complaint ties to March 10, 2025 and to May 12, 2026. The news analyst should check what Talonfield announced on May 12, 2026, possibly Q1 results or the bill-and-hold amendment.

### Positive or mitigating points
- The 10-Q discloses the $9.4 million return, the pull-forward and the cut in guidance openly, and says the remaining $22.4 million was delivered by June 30, 2026 (10-Q, "Bill-and-hold amendment").
- The covenant ratio of 2.26x at June 30 is well under 3.50x, and the ratio estimated from TTM figures matches the reported one (SEC-032).
- Q2 2026 revenue excluding the two one-off items is 112.9 + 9.4 + 2.3 = 124.6, up 6.0% on 117.6. This is my calculation, and it assumes the items are truly one-off.
- The Ruiz settlement ($3.2 million) was accrued and received preliminary approval on May 20, 2026.

### Gaps and questions for management
1. Why did the Q2 10-Q not mention the July 22, 2026 Markman order? What is the current ASC 450 assessment, and is a loss reasonably possible? If so, what is the range?
2. For each Q4 2025 bill-and-hold arrangement, who requested it, what was the substantive reason, and what documents support criteria (a) to (d)?
3. Why was the $9.4 million returned to inventory, and why was it not treated as a correction of FY2025?
4. Please provide Q3 and Q4 2025 quarterly results, Consolidated EBITDA and the add-back calculation, the June 30, 2026 term loan balance, and the Q3 2026 compliance certificate. Have lenders been approached about a waiver or amendment?
5. Please provide the full 10-K Item 1C, the incident report, and the number of customers and sites affected. What was the basis for concluding the incident was not material?
6. Is there a clawback policy, and has the Compensation Committee reviewed the 2025 bonus in light of the $9.4 million return?
7. What did Talonfield file or announce on or around March 10, 2025 and May 12, 2026? Not found in SEC filings.
