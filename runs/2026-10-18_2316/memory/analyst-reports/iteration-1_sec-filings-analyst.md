<!-- Iteration 1, sec-filings-analyst. Full report as returned by the analyst, saved unedited by the lead agent. -->

## SEC filings analyst: findings

### Files reviewed

All five files were read in full, plus the deal brief for context.

- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-K_FY2025_excerpts.md` (filed March 9, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` (filed August 6, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_DEF14A_2026_excerpts.md` (filed April 24, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md` (context only)

**Prompt-injection check:** none of the SEC files contain text that tries to instruct the agents.

**Date sequence (to compare with court records and news):**

| Date | Event |
|---|---|
| March 2024 | Vantor patent suit filed |
| August 2024 | Lumora acquisition and term loan increase |
| February 2025 | Ruiz suit filed |
| Q3 2025 | Hartwell & Pryce flags the material weakness |
| Nov 10, 2025 | Hartwell & Pryce dismissed |
| Nov 12, 2025 | Linden Barr engaged |
| Nov 14, 2025 | 8-K on the auditor change |
| Q4 2025 | $31.8M of bill-and-hold revenue recognized |
| Dec 2025 | Ruiz settlement agreed in principle |
| Jan 20, 2026 | CFO resigns (8-K dated Jan 21) |
| Feb 15, 2026 | Resignation effective |
| Mar 9, 2026 | 10-K filed with the original guidance |
| Apr 11, 2026 | FieldOS cyber incident |
| Apr 24, 2026 | Proxy filed |
| May 2026 | Bill-and-hold amendment ($9.4M credit) |
| May 20, 2026 | Ruiz preliminary approval |
| Jun 3, 2026 | Securities class action filed |
| Jun 17, 2026 | Pinecrest suit filed |
| Aug 6, 2026 | 10-Q filed with the guidance cut |
| Sep 30, 2026 | Covenant step-down to 3.00x takes effect (test date) |
| Mar 2027 | Vantor trial |

### Findings

#### SEC-01: The guidance behind the deal model was withdrawn on August 6, 2026
- **Finding:** The 10-Q replaced the March 2026 outlook that the deal model (v3, September 2026) still uses. The new EBITDA midpoint is 37.3% below the model.
- **Evidence:** "We now expect full-year 2026 revenue of $470 million to $490 million and Adjusted EBITDA of $70 million to $78 million. This replaces the outlook we provided on March 9, 2026."
  - Revenue midpoint: 480.0 vs 560.0 = 14.3% lower.
  - EBITDA midpoint: 74.0 vs 118.0 = 37.3% lower.
  - Q2 2026 revenue: 112.9 vs 117.6 = down 4.0%.
  - Q2 Adjusted EBITDA margin: 13.8 / 112.9 = 12.2%, vs 20.6 / 117.6 = 17.5% a year earlier.
  - H1 Adjusted EBITDA: 29.9 vs 39.0, down 23.3%.
- **Valuation math (inference):**
  - Net debt at June 30, 2026 is about 196.1. This assumes the term loan stayed at $185.0M (its June 30 balance is not disclosed): 185.0 + 45.0 revolver - 33.9 cash.
  - EV is about 1,159.0 + 196.1 = 1,355.1, which is 11.5x on 118.0. This matches the deal brief.
  - On guidance, the multiple becomes 17.4x (at 78.0) to 19.4x (at 70.0).
  - At a constant 11.5x on the 74.0 midpoint: EV of about 851.0, equity of about 654.9, or about $13.56 per share vs the $24.00 offer (projection).
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Updated 2026 outlook" and "Results summary"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, Item 7 "2026 outlook".
- **Severity:** Critical. It meets the "more than 10% of value" test: the model's EBITDA base is 37.3% above current company guidance.
- **Confidence:** High. Stated in a primary filing; numbers recomputed. Net debt rests on the stated term loan assumption.
- **Deal impact:** Valuation.
- **Cross-check:**
  - Financials: Q3 2026 actuals and the latest management forecast.
  - News: market reaction to the August 6 cut and whether there was any later revision.

#### SEC-02: Q4 2025 bill-and-hold revenue inflated 2025 growth, and part of it was reversed
- **Finding:** $31.8M of Q4 2025 hardware revenue was recognized on goods that were still in Talonfield's warehouses, mostly for the largest customer. In May 2026, $9.4M of it was returned to inventory and credited back.
- **Evidence:**
  - 10-K: "$31.8 million of hardware revenue under bill-and-hold arrangements (2024: none material). Of this amount, $24.6 million related to our largest customer."
  - 10-Q: products of "$9.4 million... were returned to our inventory, and we issued a credit for the same amount."
  - Share of revenue: 31.8 / 154.4 = 20.6% of Q4 2025 revenue; 31.8 / 502.3 = 6.3% of FY2025 revenue.
  - Largest customer's share: 24.6 / 31.8 = 77.4% of the bill-and-hold amount.
  - FY2025 growth without bill-and-hold: (502.3 - 31.8) / 421.7 = 11.6%, vs 19.1% reported.
  - Q4 growth without bill-and-hold: 154.4 - 31.8 = 122.6, vs an implied Q4 2024 of 154.4 / 1.324 = 116.6, so about 5.1% vs 32.4% reported.
  - The remaining 31.8 - 9.4 = 22.4 had been delivered by June 30, 2026.
- **Interpretation:** The return of $9.4M to inventory raises a question. The fourth bill-and-hold criterion ("we cannot use the products or direct them to another customer") and the "substantive" reason for the arrangement may not have been met. That could lead to a restatement of Q4 2025 rather than a Q2 2026 credit. The 10-Q does not name the customer, but it uses the same "largest customer" wording as the 10-K. The 10-K names Norvale as the largest customer.
- **Source:** 10-K, Note 2 "Revenue Recognition" and Item 7 "Revenue by type"; 10-Q, Item 2 "Bill-and-hold amendment".
- **Severity:** High. The quality of growth is overstated, and an accounting-indemnity or restatement risk needs a protection. The valuation effect is captured in SEC-01.
- **Confidence:** High. Primary filings; recomputed.
- **Deal impact:** Valuation and disclosure.
- **Cross-check:**
  - Financials: quarterly revenue by customer, and whether Norvale's Q4 2025 and Q2 2026 revenue show the $24.6M and $9.4M.
  - News: reports of channel stuffing or quarter-end pull-forward.
  - Court records: whether the securities complaint cites bill-and-hold.

#### SEC-03: Material weakness tied to bill-and-hold, auditor dismissed after it expanded scope, still not remediated
- **Finding:** The material weakness covers exactly the contracts that produced the Q4 bill-and-hold revenue. The prior auditor flagged it in Q3 2025 and said Q4 deals of this type would need more audit work. The audit committee dismissed that auditor before Q4 closed, and the weakness was still unremediated at June 30, 2026.
- **Evidence:**
  - 8-K, reportable event: Hartwell & Pryce said "additional audit procedures would be required for revenue arrangements with these terms expected in the fourth quarter of 2025, which would expand the scope of its audit."
  - Timeline: dismissed November 10, 2025, after auditing the company since 2016. Linden Barr engaged November 12, 2025, two days later.
  - Linden Barr "issued an adverse opinion" on internal control over financial reporting (ICFR).
  - 10-Q: "has not yet been remediated"; disclosure controls "not effective as of June 30, 2026."
- **What the 8-K says:** there were "no disagreements," and Hartwell & Pryce agreed with the disclosure (Exhibit 16.1).
- **Interpretation:** The timing (scope expansion flagged, then dismissal, then $31.8M of bill-and-hold recognized in Q4) looks like possible opinion shopping. That is not alleged in the filings.
- **Source:** `data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md`, Item 4.01 "Reportable event"; 10-K Item 9A; 10-Q Part I Item 4.
- **Severity:** High. It needs accounting representations, a special indemnity or escrow, and possibly a closing condition tied to remediation or a forensic review.
- **Confidence:** High. Primary filings.
- **Deal impact:** Disclosure and post-closing (SOX integration).
- **Cross-check:**
  - News: coverage of the auditor change.
  - Court records: whether the securities complaint cites the auditor dismissal.
  - The Q3 2025 10-Q is not in my files. Check whether it disclosed the weakness that was "first identified in the third quarter of 2025."

#### SEC-04: The CFO left with a $0.9M payment two months after the auditor change and is now a defendant
- **Finding:** The CFO resigned on January 20, 2026, before the 10-K was filed. He received a cash payment and gave a general release, which is unusual for a voluntary resignation. He is named in the June 2026 securities class action. The interim CFO is still in place about eight months later.
- **Evidence:**
  - 8-K: the resignation "was not the result of any disagreement"; "a cash payment of $900,000 and a general release of claims."
  - DEF 14A: Okafor "received $0.9 million under his separation agreement."
  - 10-Q: the class action names "our former Chief Financial Officer"; certifications are signed by the "Interim Chief Financial Officer."
- **Source:** `data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md`, Item 5.02; 10-K Note 18; DEF 14A "Potential payments upon a change in control"; 10-Q cover and Part II Item 1.
- **Severity:** Medium. Finance leadership is a gap that needs an integration plan. It raises the concern in SEC-03 but does not need its own price protection.
- **Confidence:** High on the facts. The reason for the payment is not disclosed.
- **Deal impact:** Post-closing and disclosure.
- **Cross-check:**
  - News: the reason for the departure and whether Okafor took a new role.
  - Court records: the allegations against Okafor in the class action.

#### SEC-05: The covenant step-down to 3.00x took effect September 30, 2026, and headroom on new guidance is thin
- **Finding:** The maximum leverage ratio fell from 3.50x to 3.00x for the quarter ended September 30, 2026. That test date has passed and the result is not in my files. On FY2026 guidance, year-end leverage could approach 3.00x. Two definition features tighten it: cash netting is capped at $25.0M, and add-backs are capped at 15%.
- **Evidence:**
  - 10-K Note 9: "no more than 3.00 to 1.00 for each fiscal quarter ending on or after September 30, 2026"; "cash netting capped at $25.0 million"; "Permitted Add-backs may not exceed 15% of Consolidated EBITDA calculated before including those Permitted Add-backs."
  - 10-Q: 2.26x at June 30, 2026.
- **Math (inference):**
  - Assume a term loan of about 182.5 (the 2025 amortization rate of 5.0 per year). Debt is then 182.5 + 45.0 = 227.5. Less the 25.0 cash cap, net debt is 202.5. That implies Consolidated EBITDA of 202.5 / 2.26 = 89.6.
  - This is close to trailing twelve months (TTM) Adjusted EBITDA of 98.8 - 39.0 + 29.9 = 89.7.
  - At the December 31, 2026 test, TTM equals FY2026: 202.5 / 78.0 = 2.60x to 202.5 / 70.0 = 2.89x.
  - With $10.0M more revolver borrowing: 2.72x to 3.04x (projection).
  - The add-back cap and the $1.8M incident costs could push Consolidated EBITDA below Adjusted EBITDA.
- **Source:** 10-K Note 9 "Financial covenant" and "Definitions"; 10-Q Item 2 "Covenant compliance".
- **Severity:** High. Under the calibration, a covenant issue cured by refinancing at closing is High. It escalates to Critical if the September 30, 2026 test was failed or a waiver was needed before closing. My files cannot show that.
- **Confidence:** Medium. The thresholds are primary. The forward ratios are projections that use an assumed term loan balance.
- **Deal impact:** Closing risk and liquidity.
- **Cross-check:**
  - Financials: the Q3 2026 covenant certificate, the TTM Consolidated EBITDA bridge and the add-back amounts.
  - News: any waiver or amendment.

#### SEC-06: Change of control is an event of default, so all debt must be repaid at closing
- **Finding:** The merger would let lenders demand immediate repayment of about $227.5 to $230.0M (term loan plus $45.0M revolver at June 30, 2026), plus $4.2M of letters of credit to replace.
- **Evidence:** "A change of control of Talonfield is an event of default, which allows the lenders to demand immediate repayment of all outstanding loans."
  - Pricing: SOFR plus 3.25% to 3.75%.
  - Prepayment premiums or breakage terms: not found in SEC filings.
- **Source:** 10-K Note 9; 10-Q "Liquidity and capital resources".
- **Severity:** High. Arbelion's sources and uses need to cover the full repayment.
- **Confidence:** High. The June 30 term loan balance is not disclosed.
- **Deal impact:** Closing (financing).
- **Cross-check:** Financials: the payoff amount and any prepayment fees in the credit agreement.

#### SEC-07: Liquidity is weakening
- **Finding:** Cash is falling, operating cash flow has turned negative and the revolver is being drawn. Receivables grew much faster than revenue while the bad-debt allowance went down.
- **Evidence:**
  - Cash: 41.6 to 33.9.
  - Revolver: 10.0 (Dec 2024) to 35.0 (Dec 2025) to 45.0 (Jun 2026). Availability is 75.0 - 45.0 - 4.2 = 25.8.
  - Operating cash flow: 40.8 (2024), 9.7 (2025), -4.2 (H1 2026).
  - Gross accounts receivable rose 59.2% (76.3 to 121.5) vs revenue growth of 19.1%.
  - Allowance fell from 3.8% to 2.1% of gross receivables (2.9 to 2.6).
  - Norvale share of receivables: 38% x 121.5 = about 46.2, vs 29% x 76.3 = about 22.1 in 2024.
  - The 10-K said "We expect collections to normalize in 2026." The 10-Q does not repeat this.
- **Source:** 10-K Item 7 "Liquidity", Note 5 and Note 13; 10-Q "Liquidity and capital resources".
- **Severity:** Medium.
- **Confidence:** High.
- **Deal impact:** Valuation (working capital peg).
- **Cross-check:** Financials: receivables aging by customer and collection of the bill-and-hold receivables.

#### SEC-08: Norvale concentration, and the deal itself triggers Norvale's termination right
- **Finding:** Norvale is 31.1% of revenue and has no minimum purchase commitment. It can terminate on 90 days' notice after a change of control, which this merger would be.
- **Evidence:**
  - "allows Norvale to terminate the agreement on 90 days' notice if Talonfield undergoes a change of control. Norvale is not required to purchase any minimum volume."
  - The master supply agreement (MSA) runs through September 30, 2027.
  - Norvale 2025 revenue: 31.1% x 502.3 = 156.2. 2024: 28.0% x 421.7 = 118.1.
  - Without its $24.6M of bill-and-hold: 131.6, which is 28.0% of 470.5 and growth of 11.4%, not 32.3%.
  - No other customer is above 10%; there are 276 active customers.
- **Interpretation:** The $9.4M return in May 2026 most likely relates to Norvale (inference from the "largest customer" wording), which may signal weaker demand.
- **Source:** 10-K Item 1 "Customers", Item 1A, Note 13; 10-Q "Bill-and-hold amendment".
- **Severity:** High. It needs a closing condition or covenant, such as Norvale consent, a waiver or an MSA extension. It would be Critical if other sources show Norvale intends to leave or is cutting volume, because 31.1% of revenue is exposed.
- **Confidence:** High on the terms. The customer in the 10-Q is not named.
- **Deal impact:** Valuation and closing.
- **Cross-check:**
  - Financials: Norvale's rank and quarterly trend in `revenue_by_customer.csv`.
  - News: Norvale dual-sourcing, competitor wins or comments about the deal.

#### SEC-09: The Vantor patent case threatens the robot behind about 42% of revenue, and no accrual is recorded
- **Finding:** Vantor is seeking an injunction against Talon Gen-3. Gen-3 was about 70% of hardware revenue, which is about 0.70 x 301.4 = 211.0, or 42.0% of total 2025 revenue. Trial is set for March 2027, after the expected closing.
- **Evidence:**
  - "seeks damages and an injunction"; "We have not recorded an accrual... cannot reasonably estimate a possible loss."
  - 10-Q: "The case is in discovery. Trial is currently scheduled for March 2027."
  - The case was filed March 2024 in the District of Delaware and involves three patents.
- **Source:** 10-K Item 3 and Item 1 "Business"; 10-Q Part II Item 1.
- **Severity:** High. It needs a special indemnity or escrow. It would be Critical if court records show adverse claim-construction rulings or a high damages estimate.
- **Confidence:** High on what the company discloses. The merits are unknown to me.
- **Deal impact:** Valuation and post-closing.
- **Cross-check:**
  - Court records: docket status, claim-construction (Markman) rulings, damages expert figures and any motions for an injunction. Compare these with "in discovery."

#### SEC-10: A securities class action names the CEO and the former CFO, with no accrual statement
- **Finding:** The class action was filed June 3, 2026 and alleges false statements about revenue and internal controls. The 10-Q is silent on any accrual or estimate of loss.
- **Evidence:** It alleges "false or misleading statements about our revenue and our internal controls." Court: Southern District of Ohio. A risk factor was added in the 10-Q.
- **Source:** 10-Q Part II Item 1 and Item 1A.
- **Severity:** High. Liabilities pass to Arbelion in a one-step merger. It needs a review of D&O insurance and an indemnity.
- **Confidence:** High that the case exists. The allegations are unproven.
- **Deal impact:** Post-closing and valuation.
- **Cross-check:**
  - Court records: the class period, the alleged misstatements (bill-and-hold, the auditor change) and lead plaintiff status.
  - News: any SEC inquiry. None is mentioned in the SEC filings.

#### SEC-11: The FieldOS cyber incident was called "not material" despite more than $16M of direct and claimed exposure
- **Finding:** Some customer fleets were down for up to three days. The company calls the incident not material. A customer has sued for $12.0M, and the 10-Q added no cyber risk factor update. No 8-K about the incident is among my files.
- **Evidence:**
  - "we concluded that the incident was not material."
  - Costs: $1.8M of response costs, added back to Adjusted EBITDA, and $2.3M of credits deducted from revenue.
  - Pinecrest suit: $12.0M, filed June 17, 2026, Franklin County, Ohio.
  - Total: 1.8 + 2.3 + 12.0 = 16.1.
  - 10-Q risk factors: "no material changes... except" securities litigation.
- **Source:** 10-Q "April 2026 service disruption", Part II Item 1 and Item 1A; 10-K Item 1A "Cybersecurity".
- **Severity:** Medium.
- **Confidence:** High on the facts. The "materiality" judgment is the company's.
- **Deal impact:** Disclosure and post-closing.
- **Cross-check:**
  - News: the scale of the outage, data exposure and other customer claims.
  - Court records: the Pinecrest complaint.
  - Financials: Pinecrest's revenue rank. Also confirm whether an 8-K under Item 1.05 was filed.

#### SEC-12: The Ruiz wage-and-hour settlement is accrued
- **Finding:** $3.2M was accrued at December 31, 2025. The court granted preliminary approval on May 20, 2026.
- **Evidence:** "agreed in principle to settle for $3.2 million, which we accrued."
- **Source:** 10-K Item 3; 10-Q Part II Item 1.
- **Severity:** Low.
- **Confidence:** High.
- **Deal impact:** Post-closing.
- **Cross-check:** Court records: final approval and any objectors.

#### SEC-13: The 2025 bonus paid 142% of target on revenue that included bill-and-hold
- **Finding:** Revenue of 502.3 was near the 510.0 maximum.
  - Without the $9.4M later reversed: 492.9, just above the 490.0 target.
  - Without all $31.8M of bill-and-hold: 470.5, essentially at the 470.0 threshold.
  - The EBITDA effect of bill-and-hold is not disclosed.
  - The proxy (April 24, 2026) came out before the May reversal. A clawback policy or action is not found in SEC filings.
- **Evidence:** "approved bonus payouts at 142% of target for all executive officers." Revenue scale: threshold 470.0, target 490.0, maximum 510.0, actual 502.3.
- **Source:** DEF 14A "2025 annual incentive plan".
- **Severity:** Medium.
- **Confidence:** High on the numbers. The payout curve is not disclosed.
- **Deal impact:** Governance and disclosure.
- **Cross-check:**
  - Court records: whether the class action raises incentive-driven revenue.
  - Financials: the EBITDA contribution of bill-and-hold.

#### SEC-14: Single-trigger equity vesting and change-in-control payments
- **Finding:** All unvested executive equity vests at closing whether or not the executive stays, $17.6M as of December 31, 2025. Total potential payments are $28.6M. Cash severance is double-trigger.
- **Evidence:** "all unvested equity awards held by executive officers vest in full immediately upon a change in control ('single-trigger')."
  - The CEO's total is $11.8M.
  - Hale also holds 6,690,000 shares. At $24.00 that is about 160.6 (inference).
- **Source:** DEF 14A "Potential payments upon a change in control".
- **Severity:** Medium. It is a retention risk after closing, so a retention plan is needed.
- **Confidence:** High. The values are as of December 31, 2025 and will change at the deal price.
- **Deal impact:** Post-closing and valuation (transaction costs).
- **Cross-check:** Financials: recompute at $24.00 and add the broader employee equity pool.

#### SEC-15: The related-party HQ lease lets the CEO's family landlord reset rent at closing
- **Finding:** The headquarters and main assembly plant are leased from Hale Family Properties through December 2033. A change of control lets the landlord reset rent to "fair market value" using an appraiser the landlord chooses.
- **Evidence:** Rent was $2.1M in 2025, with 3% annual increases. The reset uses "an appraiser selected by the landlord."
  - Rough remaining rent for 2026 to 2033 at 3%: about 19.2 (inference) before any reset.
- **Source:** DEF 14A "Certain relationships and related party transactions".
- **Severity:** Medium. Negotiate a waiver or cap as part of the merger agreement.
- **Confidence:** High.
- **Deal impact:** Valuation and post-closing.
- **Cross-check:** News and financials: market rents in Columbus; whether this is the only assembly site.

#### SEC-16: Board structure
- **Finding:** Hale is both Chairman and CEO, and there is no lead independent director. Five of seven directors are independent. Hale owns 14.2%, and insiders as a group own 17.6%.
- **Evidence:** "The Board has not appointed a lead independent director."
- **Source:** DEF 14A "Board of Directors" and "Security ownership".
- **Severity:** Low.
- **Confidence:** High.
- **Deal impact:** Governance and closing (shareholder vote dynamics).
- **Cross-check:** News: shareholder activism.

#### SEC-17: Management's description of Q4 2025 changed between the 10-K and the 10-Q
- **Finding:** The 10-K credited Q4 to "strong hardware deliveries," even though $31.8M of that revenue had not been delivered. The 10-Q now says customers "pulled forward" orders into Q4 2025. The 10-K's line that "collections [will] normalize in 2026" is not repeated.
- **Evidence:**
  - 10-K: "driven by strong hardware deliveries to enterprise customers."
  - 10-K Note 2: "At December 31, 2025, these products remained in our warehouses."
  - 10-Q: "orders that customers pulled forward into the fourth quarter of 2025."
  - The 10-K figures for ARR ($139.2M) and net revenue retention (118%) were not found in the 10-Q excerpts.
- **Source:** 10-K Item 7 and Note 2; 10-Q Item 2 "Revenue".
- **Severity:** Medium.
- **Confidence:** High on the wording. The 10-Q is an excerpt, so omitted metrics may exist in the full filing.
- **Deal impact:** Disclosure.
- **Cross-check:**
  - News and court records: whether the class action quotes the "deliveries" language.
  - Financials: current ARR and net revenue retention.

#### SEC-18: Possible goodwill impairment trigger not addressed
- **Finding:** Goodwill is $98.4M, including $57.4M from the Lumora acquisition. It was last tested October 1, 2025, before the guidance cut and the share price fall. The 10-Q excerpts do not mention an interim test.
- **Evidence:** "We performed our annual impairment test as of October 1, 2025 and found no impairment."
- **Source:** 10-K Note 15.
- **Severity:** Medium.
- **Confidence:** Medium. Whether an impairment trigger exists is my inference.
- **Deal impact:** Post-closing (purchase accounting).
- **Cross-check:** Financials: Lumora revenue against its acquisition case.

#### SEC-19: Single-source LiDAR supplier in China
- **Finding:** All Talon AMR models use LiDAR sensors from one supplier that makes them in China. There is no qualified second source.
- **Evidence:** "We do not currently have a qualified second source."
- **Source:** 10-K Item 1 "Suppliers" and Item 1A.
- **Severity:** Medium.
- **Confidence:** High.
- **Deal impact:** Post-closing.
- **Cross-check:** News: tariff actions on LiDAR. Financials: hardware gross margin trend (gross margin fell to 37.6% in Q2 2026 from 40.9%).

### Positive or mitigating points
- **Covenant:** Talonfield was in compliance at 2.26x vs 3.50x at June 30, 2026 (10-Q).
- **Bill-and-hold:** $22.4M of the $31.8M was delivered by June 30, 2026 (10-Q).
- **Auditor change:** the 8-K reports "no disagreements," and the former auditor's Exhibit 16.1 letter agrees with the disclosure.
- **Software:** FieldOS ARR grew 27% to $139.2M, and software net revenue retention was 118% (10-K, FY2025).
- **Underlying Q2:** without the $9.4M credit and $2.3M of service credits, Q2 2026 revenue would be 124.6, up 6.0% vs 117.6 (inference).
- **Customers:** no customer other than Norvale is above 10% of revenue, across 276 customers.
- **Severance:** cash severance is double-trigger.
- **Ruiz:** fully accrued and preliminarily approved.

### Gaps and questions for management
1. **September 30, 2026 covenant test:** what was the ratio? Was a waiver or amendment needed? Provide the Consolidated EBITDA bridge, including the add-back cap calculation and the term loan balance. (Not found in SEC filings.)
2. **Q3 2026 10-Q:** not in my files. Any further guidance change, remediation update or new litigation?
3. **Bill-and-hold:** for each 2025 contract, did the customer request it in writing? What was the substantive reason? Why was $9.4M taken back into inventory, and was that inventory resold? Has the auditor or audit committee considered a restatement?
4. **Auditor change:** what was the reason for dismissing Hartwell & Pryce? Provide audit committee minutes and the Exhibit 16.1 letter. Was Linden Barr's opinion on the financial statements unqualified? (Not found in SEC filings.)
5. **Material weakness:** when did the company first disclose it publicly (the Q3 2025 10-Q)? What is the remediation timeline?
6. **CFO departure:** why was a $0.9M payment made on a voluntary resignation? What claims were released? What is the status of the permanent CFO search?
7. **Norvale:** current order trends. Has Norvale been approached about the deal, and would it waive the change-of-control termination right? Is the $9.4M credit Norvale-related?
8. **Vantor:** status of claim construction, the damages theory and any settlement talks.
9. **Securities class action and Pinecrest:** D&O coverage limits and retention, and any loss estimates. Was an 8-K filed for the April 2026 cyber incident?
10. **Debt payoff:** prepayment premiums and payoff mechanics. (Not found in SEC filings.)
11. **Compensation:** is there a clawback policy, and will it be applied to the 2025 bonuses?
12. **Lease:** will Hale Family Properties waive or cap the rent reset on a change of control?
13. **Goodwill:** has an interim impairment test been performed since the guidance cut?