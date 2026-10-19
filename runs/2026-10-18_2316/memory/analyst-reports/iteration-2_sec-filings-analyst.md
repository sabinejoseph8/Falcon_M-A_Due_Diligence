<!-- Iteration 2, sec-filings-analyst. Full report as returned by the analyst, saved unedited by the lead agent. -->

## SEC filings analyst: findings (iteration 2)

### Files reviewed

I read all five files in full. I also read the deal brief for context.

- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-K_FY2025_excerpts.md` (filed March 9, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` (filed August 6, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_DEF14A_2026_excerpts.md` (filed April 24, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md` (context only)

None of the files contain text that tries to instruct the agents. All five SEC files are excerpts, so "not found" below means "not found in these excerpts".

### Findings

#### SEC-20: The 10-Q does not mention the July 22, 2026 claim-construction ruling in Vantor
- **Finding:** The 10-Q was filed August 6, 2026, which is 15 days after the court adopted Vantor's construction for three of four disputed terms (per LIT-001). It describes the case only as being in discovery and does not mention the ruling.
- **Evidence:** The whole 10-Q entry reads: "The case is in discovery. Trial is currently scheduled for March 2027. We continue to believe the claims are without merit, and we have not recorded an accrual." It does not mention claim construction, a Markman ruling or "localization map".
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1. Legal Proceedings". Compare with LIT-001 (docket entry of 2026-07-22, as provided by the lead).
- **Severity:** High. This is a disclosure gap about an adverse development in the case that threatens Gen-3, the main product (see SEC-23 for the revenue math). It supports a specific indemnity or escrow, and it adds to the securities-litigation pattern. I did not rate it Critical because the gap itself does not meet a named test. The underlying exposure is assessed in SEC-22 and SEC-23.
- **Confidence:** High. The 10-Q wording is direct. The July 22 date comes from the court docket as provided to me. I did not read the docket myself.
- **Deal impact:** Disclosure, and valuation through the litigation exposure.
- **Cross-check:** Litigation: confirm the July 22 order date, which terms went against Talonfield, and whether the ruling was public before August 6. News: check whether the press reported the ruling before or after the 10-Q. Ask counsel whether omitting it was reasonable.

#### SEC-21: The 10-Q drops language the 10-K used about Vantor: the injunction request, the loss-range statement and "defend vigorously"
- **Finding:** The 10-K said Vantor seeks damages and an injunction, and that a loss range could not be estimated. The 10-Q says neither. Its accrual statement no longer gives a reason.
- **Evidence:**
  - 10-K: "seeks damages and an injunction."
  - 10-K: "We have not recorded an accrual because we do not believe a loss is probable, and we cannot reasonably estimate a possible loss or range of loss."
  - 10-K: "intend to defend ourselves vigorously."
  - 10-Q: "we have not recorded an accrual."
  - "Vigorously" still appears in the 10-Q, but only for the securities class action, not for Vantor.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, "Item 3. Legal Proceedings". `TLFS_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1. Legal Proceedings".
- **Severity:** High. Management stopped mentioning the injunction risk and the loss-range statement right after a ruling that went against the company.
- **Confidence:** High for the wording comparison, since both are primary sources. What this means is my interpretation. The 10-Q is an excerpt, and the full notes might hold a fuller contingency disclosure.
- **Deal impact:** Disclosure and valuation.
- **Cross-check:** Get the full 10-Q, including the contingencies note, to see whether the loss-range language appears there. Litigation: confirm the injunction request (the 10-K says one was sought from the start, and LIT-001 says a permanent injunction will be sought).

#### SEC-22: Neither filing states how much Vantor claims or gives any range of loss
- **Finding:** Neither filing quantifies the Vantor claim. The 10-K says no range can be estimated. The 10-Q says nothing on range. The complaint's "not less than $140 million" (LIT-001) does not appear in any SEC file.
- **Evidence:** The 10-K says "cannot reasonably estimate a possible loss or range of loss". The 10-Q gives no amount. I searched all five files and found no dollar figure for Vantor.
- **Math (against the deal's implied equity value of $1,159.0M):**
  - $140.0M / 1,159.0 = 12.1%
  - $96.4M expert damages figure / 1,159.0 = 8.3%
- **Source:** Same sections as SEC-21.
- **Severity:** High as a disclosure finding. The exposure itself may meet the Critical test (more than 10% of value), because $140.0M is 12.1% of equity value. That depends on probability, which is outside my files. I leave the Critical call to the lead's cross-source analysis.
- **Confidence:** High that the amount is missing from the filings. The $140M and $96.4M figures come from the litigation source as provided.
- **Deal impact:** Valuation, plus a specific indemnity or escrow.
- **Cross-check:** Litigation: the complaint's prayer for relief and the damages report. Financial: whether any reserve sits in the trial balance.

#### SEC-23: No SEC filing in the folder covers the Vantor events after August 6, and the injunction threat covers about 42% of 2025 revenue
- **Finding:** Vantor added Gen-3 Plus on August 14 and served its $96.4M damages report and injunction intent on September 4 (LIT-001). Both came after the 10-Q. No later 8-K or other filing is in the folder. The 10-K itself says an adverse outcome could force Talonfield to "stop selling Talon Gen-3 robots".
- **Evidence:** The 10-K says Gen-3 "represented approximately 70% of hardware revenue in 2025". The 10-K risk factor warns the company could "stop selling Talon Gen-3 robots." The most recent filing in the folder is the 10-Q dated August 6, 2026.
- **Math:**
  - Gen-3 hardware revenue: 0.70 x $301.4M = $211.0M.
  - Share of total revenue: $211.0M / $502.3M = 42.0% of 2025 revenue (inference: it assumes the 70% applies to the 2025 hardware line as stated).
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, "Item 1. Business" and "Item 1A. Risk Factors". `TLFS_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1".
- **Severity:** High. An injunction against products that make up about 42% of revenue could exceed the 10% value test. That depends on the litigation outcome, so I flag it for the lead's X- analysis rather than rating it Critical myself.
- **Confidence:** High for the filing facts and the math. Low to Medium for the probability of an injunction, which is outside my files.
- **Deal impact:** Valuation, closing risk (a possible closing condition or MAE carve-out), and post-closing.
- **Cross-check:** EDGAR (outside my files): whether any 8-K was filed after August 6. Financial: the Gen-3 versus Gen-3 Plus revenue split. Litigation: the injunction timetable relative to closing.

#### SEC-24: The 10-Q states 2.26x with no Consolidated EBITDA reconciliation and no mention of the 15% add-back cap
- **Finding:** The 10-Q gives a single ratio and a compliance statement. It does not give the Consolidated EBITDA used, the debt or cash figures used, or whether the 15% Permitted Add-backs cap was applied or binding.
- **Evidence:**
  - 10-Q: "Our Total Net Leverage Ratio was 2.26 to 1.00 at June 30, 2026, compared with a maximum of 3.50 to 1.00, and we were in compliance."
  - 10-K definition: "Permitted Add-backs may not exceed 15% of Consolidated EBITDA calculated before including those Permitted Add-backs." Cash netting is "capped at $25.0 million."
- **Implied numbers (inference; the June 30 term loan balance is not in the 10-Q):**
  - Debt: revolver $45.0M plus term loan of about $182.5M to $185.0M (the 10-K shows it amortizing $5.0M a year) gives $227.5M to $230.0M.
  - Net debt: less capped cash of $25.0M (actual cash of $33.9M exceeds the cap) gives $202.5M to $205.0M.
  - Implied Consolidated EBITDA: $202.5M / 2.26 = $89.6M, up to $205.0M / 2.26 = $90.7M.
  - Trailing-twelve-month Adjusted EBITDA: 98.8 - 39.0 + 29.9 = $89.7M.
  - So the 2.26x is consistent with management's Adjusted EBITDA being used almost one-for-one as Consolidated EBITDA (inference). If Adjusted EBITDA's add-backs exceed 15% of pre-add-back EBITDA, the covenant figure would be lower and the ratio higher.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "Covenant compliance" and "Liquidity and capital resources". `TLFS_10-K_FY2025_excerpts.md`, "Note 9. Debt". `TLFS_10-K_FY2025_excerpts.md`, "Item 7", 2025 highlights.
- **Severity:** High. The covenant can only be checked if the add-back cap was applied correctly, and the step-down is already in effect (see SEC-25).
- **Confidence:** High for the quote. Medium for the implied EBITDA, which is inferred and depends on an assumed term loan balance.
- **Deal impact:** Closing risk and valuation. The change-of-control event of default means the debt must be refinanced at closing in any case.
- **Cross-check:** Financial: the add-back detail in the Adjusted EBITDA reconciliation (stock-based compensation, the $1.8M incident costs, restructuring), the June 30 term loan balance, and the compliance certificate delivered to lenders.

#### SEC-25: No forward-looking statement on headroom at the September 30, 2026 step-down to 3.00x, and the guidance points to thin headroom
- **Finding:** The 10-Q mentions the step-down only as a fact. It says nothing about expected headroom, lender talks, waivers or amendments. Its excerpts contain no subsequent-events disclosure and no statement that liquidity is sufficient.
- **Evidence:** 10-Q: "Beginning with the quarter ending September 30, 2026, the maximum ratio decreases to 3.00 to 1.00." Nothing more on the subject is found in the SEC filings.
- **Math (projection):**
  - With net debt held at about $202.5M, 3.00x requires Consolidated EBITDA of at least 202.5 / 3.00 = $67.5M.
  - Against the full-year 2026 Adjusted EBITDA guidance of $70M to $78M: 202.5 / 70 = 2.89x and 202.5 / 78 = 2.60x.
  - That is a cushion of only $2.5M of EBITDA at the low end, before any cap haircut. More revolver borrowing would raise net debt. Cash already exceeds the $25.0M netting cap, so a drop in cash down to that level would not change the ratio.
  - The September 30 trailing-twelve-month figure cannot be computed from the filings, because Q4 2025 and Q3 2026 standalone EBITDA are not given.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "Covenant compliance" and "Updated 2026 outlook". `TLFS_10-K_FY2025_excerpts.md`, "Note 9. Debt".
- **Severity:** High. A September 30 breach before signing or closing would make this Critical under the calibration rule. The filings do not show whether it happened. The Q3 test result becomes due with the Q3 10-Q (inference: around mid-November 2026, after the November 6 IC meeting).
- **Confidence:** Medium. It is a projection from guidance and an inferred debt balance.
- **Deal impact:** Closing risk and liquidity.
- **Cross-check:** Financial: monthly Q3 2026 EBITDA and the September 30 compliance certificate. News: any reports of a waiver or amendment. Ask management directly.

#### SEC-26: The 10-Q downplays the April incident: "some customers", no data-theft finding, and a bare "not material" conclusion that never mentions Item 1.05
- **Finding:** The 10-Q describes the scale only as "some customers" and says no evidence of data theft was found. It concludes the incident was "not material" but does not mention Form 8-K Item 1.05. No incident 8-K is among the files. The news source reports 40+ sites and a ransomware data-theft claim (unverified).
- **Evidence:**
  - "interrupted fleet operations for some customers for up to three days".
  - "we concluded that the incident was not material, and we have not identified evidence that customer data was taken."
  - The 10-Q excerpts do not mention ransomware, a ransom demand, a threat actor's claim, or the number of customers or sites affected.
  - The only 8-Ks in the folder are dated November 14, 2025 and January 21, 2026.
- **Math:** Direct costs are $1.8M of response costs plus $2.3M of service credits = $4.1M. Adding Pinecrest's $12.0M claim gives $16.1M. That is more than Q2 2026 Adjusted EBITDA of $13.8M.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "April 2026 service disruption". The file list of `data/sec-filings/`.
- **Severity:** High. A disclosure gap on cybersecurity materiality is an SEC enforcement and litigation risk. It also bears on the representations about data security in the merger agreement.
- **Confidence:** High for the filing wording and for the absence of an 8-K in the folder. The ransomware claim is an allegation from news and is unverified.
- **Deal impact:** Disclosure, post-closing (regulatory and customer claims), and the need for a specific cyber indemnity.
- **Cross-check:** News: the 40+ sites figure and the ransomware group's claim. EDGAR, outside my files: whether any Item 1.05 or 8.01 8-K exists. Litigation: other outage suits besides Pinecrest. Financial: customer churn after April.

#### SEC-27: Incident response costs are added back to Adjusted EBITDA and could also count as covenant add-backs
- **Finding:** The $1.8M incident cost is excluded from Adjusted EBITDA as "other non-recurring items". Under the credit agreement it would be a Permitted Add-back, which counts toward the 15% cap.
- **Evidence:** "$1.8 million of incident response costs, which are included in 'other non-recurring items' in our Adjusted EBITDA reconciliation". The 10-K lists "other non-recurring charges ('Permitted Add-backs')".
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "April 2026 service disruption". `TLFS_10-K_FY2025_excerpts.md`, "Note 9. Debt".
- **Severity:** Medium.
- **Confidence:** High for the quotes. Whether the cap binds is not known.
- **Deal impact:** Valuation (quality of earnings) and covenant.
- **Cross-check:** Financial: the full add-back schedule for the trailing twelve months to June 30, 2026, and whether the $2.3M of credits was also added back.

#### SEC-28: The 10-Q says the risk factors have not changed materially, despite the outage, the Markman ruling, the guidance cut and the revolver draw
- **Finding:** The 10-Q adds only a securities-litigation risk factor. It leaves the 10-K's cyber risk factor as a hypothetical ("could disrupt") even though the incident has happened. It adds nothing on the Vantor ruling or covenant headroom.
- **Evidence:** "There have been no material changes to the risk factors in our 2025 Form 10-K, except for the following addition". The 10-K risk factor reads: "An outage or attack could stop customers' robot fleets".
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1A". `TLFS_10-K_FY2025_excerpts.md`, "Item 1A".
- **Severity:** Medium.
- **Confidence:** High for the wording. That this is inadequate is my interpretation.
- **Deal impact:** Disclosure, and it could support the class action.
- **Cross-check:** Litigation: whether the class action complaint cites risk factors that were framed as hypothetical after the risk had already happened.

#### SEC-29: The 10-Q describes the class action generically and gives no accrual or loss-range position for it or for Pinecrest
- **Finding:** The 10-Q does not mention the bill-and-hold allegation (LIT-003). It does state Pinecrest's $12.0M claim. It gives no accrual or loss-range statement for either case.
- **Evidence:**
  - Class action: "alleging that we made false or misleading statements about our revenue and our internal controls."
  - Pinecrest: "seeking $12.0 million. We believe we have meritorious defenses."
  - The defendants include "our former Chief Financial Officer". This is Okafor, whose January 8-K said his departure "was not the result of any disagreement".
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1". `TLFS_8-K_2026-01-21_cfo-departure.md`, "Item 5.02".
- **Severity:** Medium for the wording gap. The class action itself is assessed by the litigation analyst.
- **Confidence:** High.
- **Deal impact:** Disclosure, and whether D&O insurance or an indemnity should cover these cases.
- **Cross-check:** Litigation: the class period, the alleged statements (likely the Q4 2025 "record" revenue language; this is my inference) and whether Okafor is cooperating. Financial: any reserve for Pinecrest.

#### SEC-30: The $9.4M bill-and-hold return was booked as a Q2 2026 revenue reduction, and neither filing discusses restating Q4 2025
- **Finding:** The return was treated as a current-period credit, not as a correction of Q4 2025. No SEC file discusses a restatement, an error analysis or a non-reliance conclusion. The underlying control weakness is still unremediated.
- **Evidence:**
  - "We recorded the credit as a reduction of revenue in the second quarter of 2026."
  - Item 4: "The material weakness described in our 2025 Form 10-K has not yet been remediated."
  - The words "restate", "restatement" and "Item 4.02" are not found in the SEC filings.
- **Math:**
  - 9.4 / 31.8 = 29.6% of the Q4 2025 bill-and-hold revenue.
  - 9.4 / 24.6 = 38.2% of the largest customer's Q4 bill-and-hold.
  - 9.4 / 154.4 = 6.1% of Q4 2025 revenue.
  - FY2025 revenue less 9.4 = $492.9M, which is 16.9% growth instead of 19.1%.
  - The remainder ties: 31.8 - 9.4 = 22.4, matching the "remaining $22.4 million" in the 10-Q.
  - Bonus effect: revenue of $492.9M would still clear the $490.0M target, but would fall below the actual $502.3M that drove the 142% payout. No clawback disclosure is found in the SEC filings.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "Bill-and-hold amendment" and "Part I, Item 4". `TLFS_10-K_FY2025_excerpts.md`, "Note 2" and "Item 7". `TLFS_DEF14A_2026_excerpts.md`, "2025 annual incentive plan".
- **Severity:** High. If the Q4 2025 recognition was an error rather than a later amendment, a restatement could follow, and that feeds the class action. This calls for a specific indemnity or condition.
- **Confidence:** High for the accounting treatment stated. Whether a restatement is needed is my interpretation and depends on the facts in the May amendment.
- **Deal impact:** Valuation, disclosure and post-closing.
- **Cross-check:** Financial: the May 2026 amendment terms and Norvale's Q4 2025 versus Q2 2026 revenue. Auditor: Linden Barr's view on the treatment. News: any reporting that the Norvale goods were never wanted.

#### SEC-31: The 10-Q now says customers pulled orders forward into Q4 2025, a description the 10-K did not give
- **Finding:** The 10-K said Q4 was a record driven by strong deliveries. The 10-Q now says some Q4 2025 orders were pulled forward, which weakened 2026.
- **Evidence:**
  - 10-K: "Record fourth-quarter revenue of $154.4 million, up 32.4% year over year, driven by strong hardware deliveries".
  - 10-Q: "orders that customers pulled forward into the fourth quarter of 2025."
  - The 10-K also said "We expect collections to normalize in 2026". Neither that expectation nor any update to it appears in the 10-Q.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, "Item 7" (highlights and Liquidity). `TLFS_10-Q_Q2-2026_excerpts.md`, "Revenue".
- **Severity:** Medium (it supports the revenue-quality findings).
- **Confidence:** High.
- **Deal impact:** Valuation.
- **Cross-check:** Financial: quarterly hardware revenue and the accounts receivable aging, and how much was pulled forward.

#### SEC-32: Liquidity got worse in H1 2026, and no statement on 12-month sufficiency or going concern was found
- **Finding:** Operating cash flow was negative and the revolver draw increased. The excerpts contain no statement that liquidity is sufficient for the next 12 months.
- **Evidence:**
  - "Operating cash flow for the first half of 2026 was negative $4.2 million."
  - "$45.0 million was outstanding ... $25.8 million was available".
- **Math:**
  - Revolver commitment check: 75.0 - 45.0 - 4.2 = 25.8, which ties.
  - Cash fell from $41.6M to $33.9M, a decline of $7.7M, despite the extra $10.0M draw.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources". `TLFS_10-K_FY2025_excerpts.md`, "Item 7" Liquidity and "Note 9".
- **Severity:** Medium on its own. It is High together with SEC-25.
- **Confidence:** High.
- **Deal impact:** Closing risk (whether Talonfield can operate on its own between signing and closing) and the interim operating covenants in the merger agreement.
- **Cross-check:** Financial: Q3 2026 cash and revolver usage, and the 13-week cash forecast.

### Positive or mitigating points

- The 10-Q discloses the Pinecrest claim amount ($12.0M) and the $9.4M bill-and-hold reversal openly, and says why Q2 revenue fell. (`TLFS_10-Q_Q2-2026_excerpts.md`, "Revenue" and "Part II, Item 1")
- The rest of the Q4 2025 bill-and-hold revenue, $22.4M, "had been delivered to customers as of June 30, 2026." The numbers tie: 31.8 - 9.4 = 22.4.
- Underlying Q2 revenue before the two one-off items: 112.9 + 9.4 + 2.3 = $124.6M, against $117.6M a year earlier, which is +6.0% (inference: it treats both items as one-off).
- The company was in covenant compliance at June 30, 2026, at 2.26x against a 3.50x limit.
- The Ruiz settlement ($3.2M) was already accrued and has received preliminary court approval.
- The 10-Q discloses the cyber incident costs ($1.8M plus $2.3M) separately.

### Gaps and questions for management

1. Why does the August 6 10-Q not mention the July 22 claim-construction ruling? Did management and counsel consider it material?
2. Why were the injunction reference and the "cannot reasonably estimate a possible loss or range of loss" statement removed in the 10-Q? What is the current ASC 450 assessment, given the $96.4M damages report?
3. Has any 8-K been filed since August 6, 2026 about Vantor, the Q3 covenant test or the cyber incident? None was found in the SEC filings.
4. Please provide the Consolidated EBITDA calculation and the compliance certificate for June 30, 2026. Was the 15% Permitted Add-backs cap binding? Which add-backs were used?
5. What is the projected Total Net Leverage Ratio at September 30, 2026? Have the lenders been approached about a waiver or amendment?
6. How many customers and sites were affected by the April outage? What was the analysis behind the decision not to file an Item 1.05 8-K? What is the company's response to the ransomware group's claim of data theft? The 10-Q says only "we have not identified evidence that customer data was taken."
7. Was the $9.4M return assessed as an error under ASC 250? What was Linden Barr's view? Will the 2025 bonuses be clawed back or recalculated?
8. What is the timetable for remediating the material weakness, and who is the permanent CFO candidate?
9. Does the company carry D&O and cyber insurance that covers the class action, Pinecrest and other outage claims? Not found in SEC filings.
10. Did former CFO Okafor raise any concerns about bill-and-hold before he resigned? He is now a defendant in the class action.