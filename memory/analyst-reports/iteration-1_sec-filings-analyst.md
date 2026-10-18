<!-- Iteration 1, saved unedited by the lead agent on 2026-10-18. -->

## SEC filings analyst: findings

### Files reviewed

All five files in `data/sec-filings/` were read in full, plus `data/deal-brief.md` for context.

| File | Filing date |
|---|---|
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md` | Nov 14, 2025 (dismissal Nov 10, 2025) |
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md` | Jan 21, 2026 |
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-K_FY2025_excerpts.md` | Mar 9, 2026 |
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_DEF14A_2026_excerpts.md` | Apr 24, 2026 |
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` | Aug 6, 2026 |

No embedded instructions aimed at a reader or AI were found in any of these files (see SEC-023).

### Findings

#### SEC-001: Company's own guidance cut makes the deal model's valuation case out of date
- **Finding:** On August 6, 2026 Talonfield replaced its March 2026 outlook. The new outlook is FY2026 revenue of $470.0 to $490.0 million and Adjusted EBITDA of $70.0 to $78.0 million. The deal model (v3, September 2026) still uses the March case of $560.0 million and $118.0 million.
- **Evidence:** "We now expect full-year 2026 revenue of $470 million to $490 million and Adjusted EBITDA of $70 million to $78 million. This replaces the outlook we provided on March 9, 2026." The March outlook was $555.0 to $565.0 million revenue and $114.0 to $122.0 million Adjusted EBITDA (midpoints $560.0 and $118.0, which match the deal model).
  - Revenue midpoint: 480.0 / 560.0 = -14.3%. Adjusted EBITDA midpoint: 74.0 / 118.0 = -37.3%.
  - Implied EV: 1,159.2 equity + about 196.1 net debt = about 1,355.3. The net debt assumes $185.0 million term loan + $45.0 million revolver - $33.9 million cash. The term loan balance at June 30, 2026 is not found in SEC filings. A check: 1,355.3 / 118.0 = 11.5x, which matches the deal brief.
  - On the new midpoint: 1,355.3 / 74.0 = 18.3x (17.4x at $78.0 million, 19.4x at $70.0 million).
  - Holding 11.5x on $74.0 million gives an EV of about 851.0, equity of about 654.9, or about $13.56 per share on 48.3 million diluted shares. That is a reference point only, not a valuation.
  - Implied H2 2026 revenue is 247.4 to 267.4 (470.0 or 490.0 - 222.6). H2 2025 was 275.8 (502.3 - 226.5), so H2 2026 is down 3.0% to 10.3%. Implied FY2026 revenue growth at the midpoint is -4.4% (480.0 / 502.3).
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "Updated 2026 outlook"; `TLFS_10-K_FY2025_excerpts.md`, Item 7 "2026 outlook (as of March 9, 2026)"
- **Severity:** Critical
- **Confidence:** High. The company states this in its own filing, and the numbers are recomputed.
- **Deal impact:** Valuation. The price rests on a forecast the company itself withdrew more than two months before the IC meeting.
- **Cross-check:** Financial analyst: Q3 2026 actuals and the H2 run-rate against the new guidance. News: analyst and market reaction to the August 6 cut, and whether guidance was updated again.

#### SEC-002: Q4 2025 bill-and-hold revenue of $31.8 million, of which $9.4 million has already been reversed
- **Finding:** Talonfield booked $31.8 million of Q4 2025 hardware revenue under bill-and-hold arrangements, with none material in 2024. Of this, $24.6 million came from its largest customer (Norvale is named as the largest customer in Item 1). In May 2026, $9.4 million of it was returned to inventory and credited back against Q2 2026 revenue.
- **Evidence:** "In the fourth quarter of 2025 we recognized $31.8 million of hardware revenue under bill-and-hold arrangements (2024: none material). Of this amount, $24.6 million related to our largest customer." The 10-Q says: "products with a sales value of $9.4 million ... were returned to our inventory, and we issued a credit."
  - 31.8 / 154.4 = 20.6% of Q4 2025 revenue.
  - Q4 2024 revenue is 154.4 / 1.324 = 116.6. Q4 2025 without bill-and-hold is 154.4 - 31.8 = 122.6, which is +5.1% year over year, against the +32.4% reported.
  - FY2025 without bill-and-hold is 502.3 - 31.8 = 470.5, which is +11.6% against the 19.1% reported.
  - 24.6 / 31.8 = 77.4% came from the largest customer. 9.4 / 31.8 = 29.6% has been reversed.
  - The 10-Q says the reversal was with "our largest customer". If that is Norvale, 9.4 / 24.6 = 38.2% of Norvale's bill-and-hold was reversed. This is an inference: the 10-Q does not name the customer.
  - The remaining $22.4 million was "delivered to customers as of June 30, 2026". The 10-Q does not say whether it was collected.
  - The 10-Q also concedes that Q2 hardware was hit by "orders that customers pulled forward into the fourth quarter of 2025". The 10-K had said Q4 growth was "driven by strong hardware deliveries to enterprise customers".
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Note 2 and Item 7; `TLFS_10-Q_Q2-2026_excerpts.md`, "Revenue" and "Bill-and-hold amendment"
- **Severity:** Critical
- **Confidence:** High for the amounts. Medium that the $9.4 million reversal is Norvale (inference).
- **Deal impact:** Valuation and disclosure. Reported FY2025 growth overstates underlying growth by about 7.5 points. There is also restatement risk: control had arguably not transferred on $9.4 million of goods that came back.
- **Cross-check:** Financial analyst: quarterly revenue by customer for Norvale in Q4 2025 and Q2 2026, and AR collection on the $22.4 million. Litigation: whether the securities class action cites bill-and-hold. News: reports on Q4 stuffing or pull-forward.

#### SEC-003: Auditor dismissed weeks after it warned it would expand audit scope on Q4 non-standard hardware deals
- **Finding:** The Audit Committee dismissed Hartwell & Pryce, auditor since 2016, on November 10, 2025. In Q3 2025 that auditor had reported a material weakness and said "additional audit procedures would be required" for non-standard Q4 revenue arrangements. The 8-K reports "no disagreements". The material weakness and the scope warning are disclosed as a reportable event. Linden Barr was engaged two days later, and Q4 then included $31.8 million of bill-and-hold revenue.
- **Evidence:** "additional audit procedures would be required for revenue arrangements with these terms expected in the fourth quarter of 2025, which would expand the scope of its audit." Hartwell & Pryce's Exhibit 16.1 letter agrees with the disclosure.
- **Source:** `TLFS_8-K_2025-11-14_auditor-change.md`, Item 4.01 "(a)", "Reportable event" and "(b)"
- **Severity:** High
- **Confidence:** High for the facts. The view that this suggests a search for a friendlier auditor is our interpretation, not stated in the filing.
- **Deal impact:** Disclosure and valuation (quality of earnings). It supports the case for a buyer-commissioned forensic revenue review.
- **Cross-check:** News: commentary on the auditor change. Litigation: whether the securities complaint cites the dismissal. Ask management for Audit Committee minutes and Hartwell & Pryce's workpapers or communications (this needs consent).

#### SEC-004: Material weakness over revenue contracts is still unremediated, and disclosure controls are not effective
- **Finding:** ICFR was not effective at December 31, 2025 because of a material weakness over non-standard hardware contracts, including bill-and-hold. Linden Barr gave an adverse ICFR opinion. At June 30, 2026 the weakness was "not yet been remediated" and disclosure controls were "not effective".
- **Evidence:** 10-K: "This material weakness was first identified in the third quarter of 2025." 10-Q: "The material weakness described in our 2025 Form 10-K has not yet been remediated."
  - The weakness has been open for at least three quarter-ends: Q3 2025, Q4 2025 and Q2 2026.
  - Remediation steps cited are a new director of technical accounting and a contract review committee.
  - The auditor's opinion on the financial statements themselves is not found in SEC filings (excerpt).
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 9A; `TLFS_10-Q_Q2-2026_excerpts.md`, Part I Item 4
- **Severity:** High
- **Confidence:** High. Both points are stated directly in the filings.
- **Deal impact:** Post-closing (SOX remediation cost, integration) and disclosure (reliability of the numbers the price is based on).
- **Cross-check:** Ask management for the remediation plan, timeline and any further control deficiencies. Financial analyst: whether other non-standard contracts exist in 2026.

#### SEC-005: CFO resigned two months after the auditor change and is now a defendant in the securities suit
- **Finding:** CFO Daniel Okafor gave notice on January 20, 2026, effective February 15, 2026, before the 10-K was filed on March 9, 2026. He received a $900,000 separation payment with a general release. The 8-K uses the standard wording that the resignation "was not the result of any disagreement". The Corporate Controller became interim CFO and still held the role when she certified the August 10-Q.
- **Evidence:**
  - 8-K: "a cash payment of $900,000 and a general release of claims". Transition services ran through March 31, 2026.
  - Proxy: Okafor "received $0.9 million under his separation agreement".
  - 10-Q: the class action names "our former Chief Financial Officer".
  - A permanent CFO is not named in any filing reviewed. The 10-Q certifications are by Rachel Simmons, "Interim Chief Financial Officer".
- **Source:** `TLFS_8-K_2026-01-21_cfo-departure.md`, Item 5.02; `TLFS_10-K_FY2025_excerpts.md`, Note 18; `TLFS_DEF14A_2026_excerpts.md`, "Potential payments upon a change in control"; `TLFS_10-Q_Q2-2026_excerpts.md`, header and Part II Item 1
- **Severity:** High
- **Confidence:** High for the facts. Medium for the inference that the departure is linked to the revenue and controls issues, which the filings do not state.
- **Deal impact:** Post-closing (finance leadership gap) and disclosure. A payment with a general release to a departing CFO resigning voluntarily is unusual and worth explaining.
- **Cross-check:** News: reporting on the reasons for Okafor's exit and the status of the CFO search. Litigation: Okafor's role in the securities complaint. Ask management for the separation agreement.

#### SEC-006: Norvale is 31.1% of revenue and can terminate on 90 days' notice after a change of control
- **Finding:** Norvale Retail Group made up 31.1% of 2025 revenue (28.0% in 2024) and 38% of gross AR. The Norvale MSA runs to September 30, 2027. It has no minimum purchase commitment, and Norvale may terminate on 90 days' notice if Talonfield undergoes a change of control. The acquisition itself would trigger that right.
- **Evidence:** "The Norvale MSA allows Norvale to terminate the agreement on 90 days' notice if Talonfield undergoes a change of control. Norvale is not required to purchase any minimum volume."
  - Norvale revenue: 31.1% x 502.3 = about 156.2 (2024: 28.0% x 421.7 = about 118.1, so +32.3%).
  - Norvale share of Q4 bill-and-hold: 24.6 (SEC-002). Without its bill-and-hold, Norvale 2025 revenue would be about 131.6, or 28.0% of 470.5.
  - Norvale AR: 38% x 121.5 = about 46.2.
  - No other customer was above 10%. The 10-Q does not update the concentration figures (see SEC-019).
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 1 "Customers", Item 1A, Note 13
- **Severity:** Critical
- **Confidence:** High. The terms are stated directly in the 10-K.
- **Deal impact:** Closing risk and valuation. Possible conditions include a Norvale consent or waiver of the termination right before signing or closing, or price protection.
- **Cross-check:** News: Norvale's own plans (dual sourcing, insourcing, competitor pilots). Financial analyst: Norvale's revenue by quarter in 2026 and its rank in `revenue_by_customer.csv`. Litigation: any dispute between Norvale and Talonfield.

#### SEC-007: The change of control is an event of default under the credit agreement
- **Finding:** Under the credit agreement, a change of control of Talonfield is an event of default, and lenders can demand immediate repayment. Debt was $220.0 million at December 31, 2025 ($185.0 million term loan and $35.0 million revolver, both maturing August 2029). The revolver was $45.0 million at June 30, 2026.
- **Evidence:** "A change of control of Talonfield is an event of default, which allows the lenders to demand immediate repayment of all outstanding loans."
  - Pricing: SOFR + 3.25% to 3.75%.
  - The June 30, 2026 term loan balance is not found in SEC filings. If it was unchanged at $185.0 million, total debt was about $230.0 million.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Note 9 "Definitions"; `TLFS_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources"
- **Severity:** High. It is cured by refinancing at closing, per the calibration rule.
- **Confidence:** High. Stated directly in the 10-K.
- **Deal impact:** Closing. About $230.0 million must be repaid or refinanced at closing and should be treated as part of the purchase price funding.
- **Cross-check:** Financial analyst: the June 30, 2026 debt schedule and any prepayment premiums or breakage costs. Ask management for the full credit agreement and amendments.

#### SEC-008: Covenant step-down to 3.00x from Q3 2026 while EBITDA is falling, with possible risk before closing
- **Finding:** The maximum Total Net Leverage Ratio steps down from 3.50x (through June 30, 2026) to 3.00x (from September 30, 2026). The ratio was 2.26x at June 30, 2026. Trailing EBITDA is shrinking, and the Q4 2025 bill-and-hold quarter drops out of the trailing twelve months at the December 31, 2026 test. Headroom against the 3.00x limit could be thin at the low end of guidance.
- **Evidence:** 10-K Note 9 covenant text and definitions (there are no credit agreement section numbers in the 10-K; it calls them "summarized from the credit agreement"). Verbatim pieces for the financial analyst:
  - Covenant: "no more than 3.50 to 1.00 for each fiscal quarter ending on or before June 30, 2026, and no more than 3.00 to 1.00 for each fiscal quarter ending on or after September 30, 2026." Tested quarterly on a trailing twelve-month basis.
  - "Total Net Leverage Ratio = (Total Debt minus unrestricted cash, with cash netting capped at $25.0 million) divided by Consolidated EBITDA."
  - Consolidated EBITDA = "net income plus interest, taxes, depreciation and amortization, plus non-cash stock-based compensation, plus restructuring, integration and other non-recurring charges ("Permitted Add-backs")."
  - "Permitted Add-backs may not exceed 15% of Consolidated EBITDA calculated before including those Permitted Add-backs."
  - Ambiguity: the summary does not make clear whether stock-based compensation falls inside the 15% cap. The full agreement is needed.

  Math (assumes total debt of about $230.0 million, since the term loan balance at June 30 is not found in SEC filings):
  - Net debt for the covenant: 230.0 - 25.0 (cap binds; cash $33.9 million) = 205.0.
  - Implied Consolidated EBITDA at June 30: 205.0 / 2.26 = about 90.7. TTM Adjusted EBITDA at June 30 is 98.8 - 39.0 + 29.9 = 89.7, which is consistent.
  - EBITDA needed to stay under 3.00x: 205.0 / 3.00 = about 68.3. The cushion at June 30 is (89.7 - 68.3) / 89.7 = about 24%.
  - FY2026 guidance of 70.0 to 78.0 approximates TTM EBITDA at December 31, 2026. That gives 205.0 / 70.0 = 2.93x and 205.0 / 78.0 = 2.63x. Headroom at the low end is about 2.4%, before any add-back cap haircut.
  - Q2 2026 already includes a $1.8 million cyber add-back.
  - Q3 2025 EBITDA is not found in SEC filings, so the September 30, 2026 test cannot be computed.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Note 9 "Financial covenant" and "Definitions"; `TLFS_10-Q_Q2-2026_excerpts.md`, "Covenant compliance"
- **Severity:** High. It would become Critical if the December 31, 2026 test fails before closing, which is plausible on timing: IC November 6, closing likely after year end.
- **Confidence:** Medium. The definitions are stated, but the headroom depends on the assumed debt balance, the add-back mix and guidance as a proxy.
- **Deal impact:** Closing risk and liquidity before closing.
- **Cross-check:** Financial analyst: a full covenant model using the definitions above, Q3 2026 actuals and the add-back mix. Ask management for the compliance certificates and the full credit agreement with section numbers.

#### SEC-009: Cash generation weakening and revolver use rising
- **Finding:** Operating cash flow fell to $9.7 million in 2025 from $40.8 million in 2024, and was negative $4.2 million in H1 2026. The 10-K had said "We expect collections to normalize in 2026." Cash fell from $41.6 million to $33.9 million, and the revolver rose from $35.0 million to $45.0 million.
- **Evidence:** "$25.8 million was available under the facility." The check is 75.0 - 45.0 - 4.2 letters of credit = 25.8. Total liquidity is about 33.9 + 25.8 = 59.7.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 7 "Liquidity"; `TLFS_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources"
- **Severity:** Medium
- **Confidence:** High. Stated directly in the filings, with the arithmetic recomputed.
- **Deal impact:** Valuation (working capital peg) and post-closing.
- **Cross-check:** Financial analyst: monthly cash, a working capital trend and collection of the bill-and-hold receivables.

#### SEC-010: Vantor patent case threatens Talon Gen-3 (about 42% of revenue), and no accrual has been made
- **Finding:** Vantor Robotics sued in March 2024 (D. Del.). It alleges that Talon Gen-3 navigation infringes three patents and seeks damages and an injunction. The company calls the claims "without merit" and has made no accrual or estimate. Trial is set for March 2027, after the expected signing.
- **Evidence:** 10-K risk factor: an adverse outcome could require us to "stop selling Talon Gen-3 robots."
  - Gen-3 is about 70% of hardware revenue: 0.70 x 301.4 = about 211.0, or 42.0% of FY2025 revenue (before any software or services tied to it).
  - 10-Q (Aug 6, 2026): "The case is in discovery. Trial is currently scheduled for March 2027." No rulings are mentioned.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 1, Item 1A and Item 3; `TLFS_10-Q_Q2-2026_excerpts.md`, Part II Item 1
- **Severity:** High
- **Confidence:** High for what is disclosed. The size of the exposure is not disclosed.
- **Deal impact:** Valuation and post-closing. A specific indemnity or escrow, and possibly a design-around assessment.
- **Cross-check:** Litigation: docket events up to and after August 6, 2026 (claim construction or Markman ruling, summary judgment, damages expert reports, settlement talks). Compare the timing with the 10-Q's unchanged "without merit" language.

#### SEC-011: Securities class action filed June 3, 2026, with no accrual or range disclosed
- **Finding:** A putative securities class action in the Southern District of Ohio names Talonfield, the CEO and the former CFO. It alleges false or misleading statements about revenue and internal controls. The 10-Q discloses no accrual or loss estimate and adds one generic risk factor.
- **Evidence:** "alleging that we made false or misleading statements about our revenue and our internal controls. We intend to defend ourselves vigorously."
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, Part II Item 1 and Item 1A
- **Severity:** High
- **Confidence:** High that the suit exists. Exposure is unknown.
- **Deal impact:** Valuation and post-closing. D&O insurance tower, indemnity, and the effect on Hale and Okafor.
- **Cross-check:** Litigation: the class period, the alleged misstatements (bill-and-hold, the auditor change), the lead plaintiff and any related derivative suits. News: stock drop dates.

#### SEC-012: April 2026 FieldOS cyber incident called "not material", but it led to credits and a $12.0 million customer suit
- **Finding:** On April 11, 2026 Talonfield detected "unauthorized activity" in FieldOS and took systems offline, halting some customers' fleets for up to three days. It concluded that the incident "was not material". It still issued $2.3 million of service level credits and spent $1.8 million on response, which was added back to Adjusted EBITDA. On June 17, 2026 the customer Pinecrest Distribution LLC sued for $12.0 million (Franklin County, Ohio). The 10-Q does not mention an accrual for Pinecrest.
- **Evidence:**
  - 10-Q: "we concluded that the incident was not material, and we have not identified evidence that customer data was taken."
  - The 10-Q risk factors say there are "no material changes" apart from the securities litigation addition. The cyber risk factor was not updated, although the risk actually occurred.
  - Total quantified impact: 2.3 + 1.8 + 12.0 claimed = 16.1.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "April 2026 service disruption", Part II Item 1 "Pinecrest" and Item 1A; `TLFS_10-K_FY2025_excerpts.md`, Item 1A (cyber risk factor)
- **Severity:** High
- **Confidence:** High for the disclosed facts. Medium on whether "not material" holds up.
- **Deal impact:** Valuation (FieldOS retention and ARR) and disclosure. A specific indemnity may be needed.
- **Cross-check:** News: the scope of the breach, other affected customers and any data exfiltration reports. Litigation: the Pinecrest docket and any other customer claims. Financial analyst: Pinecrest's revenue rank, plus FieldOS churn, ARR and NRR after April.

#### SEC-013: Ruiz wage-and-hour settlement accrued and given preliminary approval
- **Finding:** $3.2 million was agreed in principle in December 2025, accrued at December 31, 2025, and given preliminary court approval on May 20, 2026.
- **Evidence:** "In December 2025 the parties agreed in principle to settle for $3.2 million, which we accrued at December 31, 2025."
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 3; `TLFS_10-Q_Q2-2026_excerpts.md`, Part II Item 1
- **Severity:** Low
- **Confidence:** High. Stated directly in both filings.
- **Deal impact:** Disclosure only.
- **Cross-check:** Litigation: final approval status and the opt-out count.

#### SEC-014: 142% executive bonus earned on revenue that was boosted by bill-and-hold
- **Finding:** 2025 bonuses paid 142% of target. Revenue of $502.3 million beat the $490.0 million target, and Adjusted EBITDA of $98.8 million beat the $95.0 million target. Without the $31.8 million of bill-and-hold, revenue would have been $470.5 million, just $0.5 million above the $470.0 million threshold. Without only the $9.4 million later reversed, revenue would have been $492.9 million.
- **Evidence:** "the Compensation Committee approved bonus payouts at 142% of target for all executive officers."
  - The EBITDA effect of bill-and-hold is not disclosed. As an illustration only, at roughly 40% gross margin (H1 2025 was 40.8%), $31.8 million of revenue is about $12.7 million of EBITDA. That would put Adjusted EBITDA near $86.1 million, below the $88.0 million threshold.
  - The proxy does not mention clawback.
- **Source:** `TLFS_DEF14A_2026_excerpts.md`, "2025 annual incentive plan"; `TLFS_10-K_FY2025_excerpts.md`, Note 2
- **Severity:** Medium
- **Confidence:** High for the revenue math. Low for the EBITDA illustration, which rests on an assumed margin.
- **Deal impact:** Disclosure and governance. Possible clawback, and a sign of incentives to pull revenue forward.
- **Cross-check:** Ask management for the clawback policy and whether the Compensation Committee reviewed the bill-and-hold impact. Litigation: whether the securities complaint cites the incentive.

#### SEC-015: Single-trigger equity vesting and change-in-control payments of $28.6 million
- **Finding:** All unvested executive equity vests on a change in control, whether or not the executive leaves ($17.6 million). Cash severance is double-trigger ($9.6 million), and other benefits total $1.4 million. The total is $28.6 million as of December 31, 2025. Hale's total is $11.8 million.
- **Evidence:** "all unvested equity awards held by executive officers vest in full immediately upon a change in control ("single-trigger"), whether or not the executive's employment ends." The values are as of December 31, 2025. The value at $24.00 per share is not found in SEC filings.
- **Source:** `TLFS_DEF14A_2026_excerpts.md`, "Potential payments upon a change in control"
- **Severity:** Medium
- **Confidence:** High. Stated directly in the proxy.
- **Deal impact:** Valuation (transaction costs) and post-closing (retention: executives are paid out on day one).
- **Cross-check:** Financial analyst: recompute at the $24.00 deal price. HR diligence: a retention plan.

#### SEC-016: Related-party HQ lease lets the CEO's family landlord reset rent on a change in control
- **Finding:** The Columbus HQ and main assembly facility are leased from Hale Family Properties LLC through December 2033. Rent was $2.1 million in 2025, with 3% annual escalators. A change in control lets the landlord reset rent to "fair market value", as set by "an appraiser selected by the landlord".
- **Evidence:** "a change in control of Talonfield allows the landlord to reset the rent to "fair market value", as determined by an appraiser selected by the landlord."
- **Source:** `TLFS_DEF14A_2026_excerpts.md`, "Certain relationships and related party transactions"
- **Severity:** Medium
- **Confidence:** High. Stated directly in the proxy.
- **Deal impact:** Post-closing cost. This could be negotiated with Hale, who holds 14.2% and is a likely voting agreement counterparty.
- **Cross-check:** Real estate: the market rent for the facility. Ask management for the lease.

#### SEC-017: Concentrated governance: combined Chair and CEO, no lead independent director, founder owns 14.2%
- **Finding:** Hale is Founder, Chairman and CEO and owns 6,690,000 shares (14.2%). Directors and officers as a group own 17.6%. Five of seven directors are independent, and there is no lead independent director.
- **Evidence:** "The Board has not appointed a lead independent director."
- **Source:** `TLFS_DEF14A_2026_excerpts.md`, "Security ownership" and "Board of Directors"
- **Severity:** Low
- **Confidence:** High. Stated directly in the proxy.
- **Deal impact:** Disclosure. It affects the deal process (voting agreement, special committee) and how much weight to give board oversight of the controls issues.
- **Cross-check:** News: any activist or shareholder commentary.

#### SEC-018: AR rose 59% while the credit loss allowance was cut
- **Finding:** Gross AR rose from $76.3 million to $121.5 million (+59.2%) while revenue rose 19.1%. Norvale's share of AR rose from 29% to 38%. The credit loss allowance still fell from $2.9 million to $2.6 million, attributed to "improved collection experience".
- **Evidence:**
  - Allowance as a share of gross AR: 2.9 / 76.3 = 3.8% to 2.6 / 121.5 = 2.1%.
  - Simple DSO: 76.3 / 421.7 x 365 = 66 days, rising to 121.5 / 502.3 x 365 = 88 days.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Note 5 and Note 13
- **Severity:** Medium
- **Confidence:** High for the numbers. Interpreting the lower allowance as aggressive is our judgment.
- **Deal impact:** Valuation (working capital and quality of earnings).
- **Cross-check:** Financial analyst: AR aging by customer, and whether Norvale paid for bill-and-hold units before delivery.

#### SEC-019: What the Q2 2026 10-Q added, dropped or reworded compared with the FY2025 10-K
- **Finding:** Compared with the 10-K, the 10-Q makes these changes:
  - It drops FieldOS ARR ($139.2 million) and software NRR (118%), which the 10-K gave as highlights.
  - It gives no update on customer concentration or Norvale. Norvale is not named; the filing refers to "our largest customer".
  - It recasts Q4 2025 as including customer pull-forward.
  - It states "no material changes" to risk factors, adding only securities litigation. The real cyber incident, the guidance cut and the tighter covenant are not reflected in risk factors.
  - It drops the expectation that "collections ... normalize in 2026".
  - It does not discuss going concern in either filing (not found in SEC filings).
  - It updates the covenant level to 2.26x and mentions the step-down.
- **Evidence:**
  - 10-K Item 7: "FieldOS ARR grew 27% to $139.2 million. Software net revenue retention was 118%." There is no equivalent in the 10-Q excerpt.
  - 10-Q Item 1A: "There have been no material changes to the risk factors in our 2025 Form 10-K, except for the following addition."
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Items 1, 1A and 7; `TLFS_10-Q_Q2-2026_excerpts.md`, Items 2 and 1A
- **Severity:** Medium
- **Confidence:** Medium. These are excerpts, so the omitted items may appear in sections that were not provided.
- **Deal impact:** Disclosure. It points to weakening software metrics and customer relationships that management chose not to report.
- **Cross-check:** Financial analyst: ARR, NRR and churn for Q1 and Q2 2026. News: customer losses after the outage.

#### SEC-020: Q2 2026 results weaken beyond the one-off items
- **Finding:** Q2 2026 revenue was $112.9 million, down 4.0%, and gross margin fell from 40.9% to 37.6%. Adjusted EBITDA fell from $20.6 million to $13.8 million (-33.0%), and the quarter had a net loss of $6.0 million.
- **Evidence:**
  - Adding back the $9.4 million reversal and $2.3 million of credits gives 124.6, which is +6.0% against Q2 2025's 117.6. This understates the weakness because of the pull-forward from Q2.
  - Q1 2026 was 222.6 - 112.9 = 109.7, against Q1 2025 of 226.5 - 117.6 = 108.9 (+0.7%).
  - Q1 2026 Adjusted EBITDA was 29.9 - 13.8 = 16.1, against 18.4 in Q1 2025.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, "Results summary" and "Revenue"
- **Severity:** Medium (it supports the Critical SEC-001)
- **Confidence:** High. The figures are stated in the 10-Q and recomputed.
- **Deal impact:** Valuation.
- **Cross-check:** Financial analyst: the margin bridge and the revenue split by type for 2026.

#### SEC-021: Lumora goodwill at risk after the guidance cut
- **Finding:** Goodwill is $98.4 million, of which $57.4 million comes from the August 2024 Lumora acquisition (purchase price $85.0 million). The last impairment test was October 1, 2025, before the guidance cut. The 10-Q excerpt does not mention an interim triggering-event test.
- **Evidence:** "We performed our annual impairment test as of October 1, 2025 and found no impairment."
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 1 and Note 15
- **Severity:** Medium
- **Confidence:** Medium. The risk is inferred from the guidance cut and the lower share price.
- **Deal impact:** Disclosure and post-closing (purchase accounting).
- **Cross-check:** Financial analyst: Lumora's revenue contribution. Ask management whether an interim test was done.

#### SEC-022: Single-source LiDAR supply from China, with no second source
- **Finding:** All Talon AMR models use LiDAR from a single supplier that manufactures in China. There is "no qualified second source". The 10-K flags tariff risk.
- **Evidence:** "We do not currently have a qualified second source."
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, Item 1 "Suppliers" and Item 1A
- **Severity:** Medium
- **Confidence:** High. Stated directly in the 10-K.
- **Deal impact:** Post-closing (supply chain plan) and margin.
- **Cross-check:** News: tariff actions on Chinese LiDAR in 2026. Financial analyst: whether the gross margin decline is linked to component costs.

#### SEC-023: No embedded instructions found; backlog and RPO not disclosed
- **Finding:** None of the five SEC files contains text trying to instruct the reader or an AI. Backlog and remaining performance obligations (RPO) are not found in SEC filings.
- **Evidence:** Not applicable. This finding records the absence of embedded instructions and of backlog or RPO disclosure.
- **Source:** All five files in `data/sec-filings/`
- **Severity:** Low
- **Confidence:** High. All files were read in full.
- **Deal impact:** Disclosure. The backlog and RPO gap limits the ability to test the H2 2026 guidance.
- **Cross-check:** Financial analyst: backlog or RPO data in `data/financials/`.

### Legal matters and filing dates (for comparison with court record timing)

| Matter | Court / filed | 10-K (Mar 9, 2026) | Proxy (Apr 24, 2026) | 10-Q (Aug 6, 2026) | Accrual |
|---|---|---|---|---|---|
| Vantor v. Talonfield (patent) | D. Del., Mar 2024 | Disclosed, "without merit" | Not mentioned | "In discovery", trial Mar 2027, "without merit" | None |
| Ruiz et al. (wage and hour) | Cal. Superior Ct., Feb 2025 | Settled in principle, $3.2M | Not mentioned | Preliminary approval May 20, 2026 | $3.2M accrued |
| Securities class action | S.D. Ohio, Jun 3, 2026 | Not applicable (filed later) | Not applicable | Disclosed, no amount | Not disclosed |
| Pinecrest Distribution LLC | Franklin County, OH, Jun 17, 2026 | Not applicable | Not applicable | Disclosed, $12.0M claimed | Not disclosed |
| April 11, 2026 cyber incident | Not applicable | Not applicable | Not applicable | "Not material" | $1.8M costs, $2.3M credits |
| Other matters | Not applicable | "not material" | Not applicable | Not mentioned | Not applicable |

Timing points for the lead agent:
- The proxy was filed April 24, 2026, 13 days after the cyber incident. Its excerpt does not mention the incident.
- The 10-Q was filed August 6, 2026. Check court records for any Vantor rulings before that date that the 10-Q's unchanged wording leaves out.

### Key numbers ($ millions unless stated)

| Metric | Value | Source |
|---|---|---|
| FY2025 revenue / FY2024 | 502.3 / 421.7 (+19.1%) | 10-K Item 7 |
| FY2025 revenue without bill-and-hold | 470.5 (+11.6%) | computed |
| Q4 2025 revenue / Q4 2024 (implied) | 154.4 / 116.6 | 10-K, computed |
| Q4 2025 bill-and-hold / from largest customer | 31.8 (20.6% of Q4) / 24.6 | 10-K Note 2 |
| Bill-and-hold reversed in Q2 2026 / delivered | 9.4 / 22.4 | 10-Q |
| FY2025 Adjusted EBITDA / net income | 98.8 / 18.6 | 10-K |
| Hardware / Software / Services 2025 | 301.4 / 128.6 / 72.3 | 10-K |
| FieldOS ARR Dec 2025 / NRR | 139.2 / 118% | 10-K |
| Q2 2026 revenue / Adjusted EBITDA / GM | 112.9 / 13.8 / 37.6% | 10-Q |
| H1 2026 revenue / Adjusted EBITDA | 222.6 / 29.9 | 10-Q |
| TTM Adjusted EBITDA Jun 30, 2026 | 89.7 | computed |
| March guidance (revenue / Adjusted EBITDA) | 555 to 565 / 114 to 122 | 10-K |
| August guidance (revenue / Adjusted EBITDA) | 470 to 490 / 70 to 78 | 10-Q |
| Norvale share of revenue 2025 / 2024 | 31.1% (~156.2) / 28.0% (~118.1) | 10-K Note 13 |
| Norvale share of gross AR | 38% (~46.2) | 10-K |
| Gross AR Dec 2025 / Dec 2024 | 121.5 / 76.3 | 10-K Note 5 |
| Cash Dec 2025 / Jun 2026 | 41.6 / 33.9 | 10-K, 10-Q |
| Term loan Dec 2025 | 185.0 (June 2026 not found) | 10-K Note 9 |
| Revolver Dec 2025 / Jun 2026 (commitment 75.0) | 35.0 / 45.0, available 25.8 | 10-K, 10-Q |
| Net leverage Jun 30, 2026 / max | 2.26x / 3.50x, stepping down to 3.00x from Sep 30, 2026 | 10-Q |
| EBITDA needed at 3.00x (net debt 205.0) | ~68.3 | computed |
| Operating cash flow 2024 / 2025 / H1 2026 | 40.8 / 9.7 / (4.2) | 10-K, 10-Q |
| Change-in-control payments (total / single-trigger equity) | 28.6 / 17.6 | proxy |
| Okafor separation | 0.9 | 8-K, proxy |
| HQ rent 2025 (related party) | 2.1, +3% a year, to Dec 2033 | proxy |
| Goodwill / Lumora | 98.4 / 57.4 | 10-K Note 15 |
| Gen-3 revenue (70% of hardware) | ~211.0 (42.0% of total) | computed |

### Positive or mitigating points

- The 8-K auditor change reports no disagreements, and Hartwell & Pryce's Exhibit 16.1 letter agrees with the disclosure. Its 2023 and 2024 opinions were unmodified.
- Covenant compliance was reported at both December 31, 2025 and June 30, 2026 (2.26x against 3.50x).
- The company disclosed the bill-and-hold amounts, the customer concentration and the reversal openly, and $22.4 million of the bill-and-hold units has been delivered.
- Debt does not mature until August 2029. Cash severance is double-trigger. Okafor is excluded from change-in-control payments.
- The Ruiz case is settled and accrued.
- Remediation steps have started (director of technical accounting, contract review committee).
- The software business grew strongly in 2025: FieldOS revenue +27.1% and ARR +27%.
- No embedded instructions were found in the SEC documents.

### Gaps and questions for management

1. Bill-and-hold:
   - Which customers make up the $31.8 million?
   - Is the $9.4 million reversal with Norvale?
   - What were the substantive reasons for each arrangement, and has the $22.4 million been collected?
   - Is there any bill-and-hold activity in 2026?
   - Has Linden Barr or the Audit Committee considered restatement?
2. Auditor change: Why was Hartwell & Pryce dismissed on November 10, 2025? Provide the Audit Committee minutes and Hartwell & Pryce's Q3 2025 communications.
3. CFO: Why did Okafor leave, and why was a separation payment with a release paid? What is the status of the permanent CFO search?
4. Norvale: What is the current relationship, and what were 2026 volumes? Would Norvale waive the change-of-control termination right? Is the MSA renewal (September 2027) under discussion?
5. Credit agreement: Provide the full agreement with section numbers, the term loan balance at June 30, 2026, the Q3 2026 compliance certificate, the add-back mix against the 15% cap, prepayment terms, and whether stock-based compensation counts toward the cap.
6. Litigation:
   - Vantor: rulings to date, damages exposure, and design-around options.
   - Securities suit: class period, D&O coverage and retention.
   - Pinecrest: any accrual.
   - Other customer claims from the April outage.
7. Cyber: forensic report, scope of the unauthorized access, and the basis for the "not material" conclusion.
8. Software KPIs: FieldOS ARR, NRR and churn for Q1 to Q3 2026. Backlog and RPO were not found in SEC filings.
9. Guidance: What drove the cut from $560.0 million to $480.0 million at the midpoint? What is the Q3 2026 performance against the new range?
10. Goodwill: Was an interim impairment test performed after the guidance cut?
11. Compensation: Is there a clawback policy? Did the Compensation Committee review the bill-and-hold effect on the 142% bonus? What is the value of change-in-control payments at $24.00 per share?
12. Lease: Would Hale agree to waive the change-of-control rent reset?
13. LiDAR: Is a second source being qualified, and what is the tariff exposure?
