## SEC filings analyst: findings (iteration 2 follow-up, SEC-15 onward)

### Files reviewed
I read all five files in full, plus the deal brief for context:
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-K_FY2025_excerpts.md (filed March 9, 2026)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md (filed August 6, 2026)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_DEF14A_2026_excerpts.md (filed April 24, 2026)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md

One caveat applies to every "not found" below. Each file is labeled "EXCERPTS", so a missing item could have been left out of the excerpt rather than out of the actual filing. None of the files contains text that tries to instruct the agents.

### Findings

#### SEC-15: Covenant definitions. Stock-based compensation is most likely in the uncapped base, but the 10-K wording leaves room for doubt
- **Finding:** The only covenant definitions are in 10-K Note 9, and they are labeled "summarized from the credit agreement". The 10-Q repeats none of them. On the most natural reading, net income, interest, taxes, D&A and non-cash stock-based compensation form the uncapped base. Only "restructuring, integration and other non-recurring charges" are Permitted Add-backs, capped at 15% of EBITDA before those add-backs. The label "("Permitted Add-backs")" comes right after the restructuring list, but the sentence is one run-on, so a lender could argue that stock-based compensation also falls under the cap.
- **Evidence (verbatim, 10-K Note 9):**
  - Total Net Leverage Ratio: "(Total Debt minus unrestricted cash, with cash netting capped at $25.0 million) divided by Consolidated EBITDA."
  - Consolidated EBITDA: "net income plus interest, taxes, depreciation and amortization, plus non-cash stock-based compensation, plus restructuring, integration and other non-recurring charges ("Permitted Add-backs")."
  - The cap: "Permitted Add-backs may not exceed 15% of Consolidated EBITDA calculated before including those Permitted Add-backs."
  - The test: "no more than 3.50 to 1.00 for each fiscal quarter ending on or before June 30, 2026, and no more than 3.00 to 1.00 for each fiscal quarter ending on or after September 30, 2026." It is "tested quarterly on a trailing twelve-month basis."
  - Not found in SEC filings: a definition of Total Debt (including whether the $4.2m of letters of credit count), equity cure rights, waiver or amendment history, any further step-downs after 3.00x, and the full credit agreement text.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Note 9. Debt"
- **Severity:** High
- **Confidence:** Medium. The text is primary, but it is a summary and the label could attach either way.
- **Deal impact:** Valuation and closing risk, because the covenant result depends on how the definition is read.
- **Cross-check:** Get the credit agreement itself (it is usually a 10-K exhibit) and any amendments. Ask the financial analyst which of the $23.7m of non-stock add-backs are restructuring, integration or non-recurring items, and which (if any) fit none of the permitted categories.

#### SEC-16: The reported 2.26x only reconciles if the 15% add-back cap is ignored
- **Finding:** The 10-Q gives the ratio but not the Consolidated EBITDA behind it. Backing it out shows the company used capped cash netting but full, uncapped Adjusted EBITDA. Applying the cap as the 10-K describes it gives about 2.67x. If stock-based compensation is also inside the cap, the ratio is about 3.65x, which would breach the 3.50x maximum at June 30, 2026.
- **Evidence (verbatim, 10-Q MD&A "Covenant compliance"):** "Our Total Net Leverage Ratio was 2.26 to 1.00 at June 30, 2026, compared with a maximum of 3.50 to 1.00, and we were in compliance." The 10-Q does not show its calculation.
- **My math** (balances and EBITDA figures come from the financial data the lead supplied):
  - Total debt: 182.5 term loan + 45.0 revolver = 227.5.
  - Net debt: cash of 33.9 is above the 25.0 netting cap, so 227.5 - 25.0 = 202.5.
  - Back-solve: 202.5 / 89.7 (company Adjusted EBITDA) = 2.2575, which rounds to 2.26x and matches exactly.
  - Other combinations do not match. Uncapped cash gives 193.6 / 89.7 = 2.16x. Adding the letters of credit gives 206.7 / 89.7 = 2.30x. So the company appears to have used capped cash and full add-backs, with letters of credit excluded.
  - Reading A (stock-based compensation in the base):
    - Base: 48.2 + 17.8 = 66.0.
    - Other add-backs: 41.5 - 17.8 = 23.7.
    - Cap: 15% x 66.0 = 9.9.
    - Consolidated EBITDA: 66.0 + 9.9 = 75.9.
    - Ratio: 202.5 / 75.9 = 2.67x. This passes 3.50x.
    - Add-backs disallowed: 13.8. The company's other add-backs equal 23.7 / 66.0 = 35.9% of the base, against a 15% cap.
  - Reading B (stock-based compensation also capped):
    - Cap: 15% x 48.2 = 7.2.
    - Consolidated EBITDA: 55.4.
    - Ratio: 202.5 / 55.4 = 3.65x. This breaches 3.50x.
  - The LTM Adjusted EBITDA of 89.7 ties to the SEC data: FY2025 98.8 - H1 2025 39.0 + H1 2026 29.9 = 89.7.
- **Interpretation, not stated in the filing:** The 2.26x looks like it was computed on Adjusted EBITDA, not on covenant Consolidated EBITDA. Another possibility is that the actual credit agreement differs from the 10-K summary.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2. MD&A, Covenant compliance"; `TLFS_10-K_FY2025_excerpts.md`, section "Note 9. Debt"
- **Severity:** High. It becomes Critical if Reading B is confirmed, because that would mean a June 30 breach that was not disclosed.
- **Confidence:** Medium. The back-solve is exact, but the covenant definition is only a summary and the inputs come from the financial data.
- **Deal impact:** Closing risk (a default before closing, lender leverage, liquidity) and disclosure risk (the compliance statement adds exposure in the securities suit).
- **Cross-check:** Lender compliance certificates for Q4 2025 through Q2 2026. The credit agreement's add-back categories. Any waiver or amendment, which might show up in news or 8-Ks not in this set.

#### SEC-17: The September 30, 2026 step-down to 3.00x leaves thin or no headroom
- **Finding:** The 10-Q notes the step-down but says nothing about expected headroom. Under Reading A, June 30 Consolidated EBITDA is only 11% above the 3.00x threshold. If the cut guidance is accurate, the December 31, 2026 test looks likely to fail under Reading A, even with net debt flat.
- **Evidence (verbatim, 10-Q MD&A):**
  - "Beginning with the quarter ending September 30, 2026, the maximum ratio decreases to 3.00 to 1.00."
  - Guidance: "Adjusted EBITDA of $70 million to $78 million." The March outlook was "$114 million to $122 million".
- **My math:**
  - Minimum Consolidated EBITDA at 3.00x: 202.5 / 3.00 = 67.5. The Reading A cushion is 75.9 - 67.5 = 8.4, or 11.1%.
  - Guidance implies H2 2026 Adjusted EBITDA of 70.0 to 78.0 minus H1 29.9, which is 40.1 to 48.1. H2 2025 was 98.8 - 39.0 = 59.8.
  - Illustration only. It assumes add-backs stay at 41.5 and net debt stays at 202.5. LTM Adjusted EBITDA falls by 11.7 to 19.7. The Reading A base becomes 46.3 to 54.3, and adding the 15% cap gives 53.2 to 62.4. The ratio is 3.24x to 3.80x at December 31, 2026, which is a breach. Even the company's own uncapped method gives 202.5 / 70.0 = 2.89x at the low end of guidance.
  - The Q3 2025 quarterly EBITDA needed for an exact September 30 test was not found in SEC filings.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, sections "Covenant compliance" and "Updated 2026 outlook"
- **Severity:** High
- **Confidence:** Medium. The inputs come from primary sources, but the forward test rests on my assumptions.
- **Deal impact:** Closing risk and interim operating covenants. The company may need a waiver before closing, which gives lenders leverage.
- **Cross-check:** The Q3 2026 10-Q or earnings release (not in these files). Quarterly EBITDA from the financial data. News about lender talks or waivers.

#### SEC-18: No cure rights, waivers or updated covenant risk factor were disclosed
- **Finding:** No filing mentions an equity cure, a waiver, an amendment or a lender discussion. The 10-Q says the risk factors are unchanged apart from the securities litigation one. It does this despite the step-down, the guidance cut and negative operating cash flow.
- **Evidence (verbatim):**
  - 10-Q Item 1A: "There have been no material changes to the risk factors in our 2025 Form 10-K, except for the following addition" (securities litigation).
  - 10-K risk factor: "A breach could allow our lenders to accelerate repayment of our debt."
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1A"; `TLFS_10-K_FY2025_excerpts.md`, section "Item 1A"
- **Severity:** Medium
- **Confidence:** Medium. The finding rests on what is absent, and the files are excerpts.
- **Deal impact:** Disclosure.
- **Cross-check:** Ask management directly whether any waiver, amendment or lender discussion has taken place. Check news for any lender talks.

#### SEC-19: Debt terms. A change of control is an event of default, so all debt must be refinanced at closing
- **Finding:**
  - Both the term loan and the revolver mature in August 2029.
  - Pricing is SOFR plus 3.25% to 3.75%.
  - The revolver commitment is $75.0m, with $45.0m drawn, $4.2m used by letters of credit and $25.8m available.
  - The term loan amortizes about $5.0m a year: 190.0 to 185.0 to 182.5.
  - Closing the deal would itself trigger a default.
- **Evidence (verbatim):**
  - 10-K Note 9: "Term loan (matures August 2029)". "Revolving credit facility ($75.0 million commitment, matures August 2029)". "A change of control of Talonfield is an event of default, which allows the lenders to demand immediate repayment".
  - 10-Q: "After $4.2 million of outstanding letters of credit, $25.8 million was available under the facility." Check: 75.0 - 45.0 - 4.2 = 25.8.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, section "Note 9. Debt"; `TLFS_10-Q_Q2-2026_excerpts.md`, section "Liquidity and capital resources"
- **Severity:** Medium
- **Confidence:** High. It is stated directly and I recomputed the numbers.
- **Deal impact:** Price and structure. Arbelion's financing must cover at least $227.5m of payoff, plus replacement of the $4.2m of letters of credit, plus breakage fees.
- **Cross-check:** Payoff letters. The prepayment terms in the credit agreement (not found in SEC filings).

#### SEC-20: The 10-Q filed August 6, 2026 does not mention the July 22, 2026 Markman order
- **Finding:** The 10-Q was filed 15 days after the court adopted Vantor's construction on three of four disputed terms. It does not mention the claim construction order or its outcome. It calls the case "in discovery" and repeats "without merit". It has no subsequent events disclosure. No 8-K after January 21, 2026 is in the files, so the September 4, 2026 expert report and the August 14, 2026 Gen-3 Plus amendment are not disclosed in any SEC filing I have.
- **Evidence (the full 10-Q text):** "*Vantor Robotics, Inc. v. Talonfield Systems, Inc.* The case is in discovery. Trial is currently scheduled for March 2027. We continue to believe the claims are without merit, and we have not recorded an accrual."
- **Context math:**
  - Gen-3 was "approximately 70% of hardware revenue in 2025". That is 0.70 x 301.4 = about 211.0, or 42.0% of total 2025 revenue of 502.3.
  - The $96.4m damages claim (from court records) is 96.4 / 1,159 = 8.3% of the implied equity value.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1. Legal Proceedings"; `TLFS_10-K_FY2025_excerpts.md`, section "Item 1. Business"
- **Severity:** Critical. A possible injunction covers products behind about 42% of revenue, and the disclosure gap adds securities-suit exposure.
- **Confidence:** High that the excerpt does not mention the order. Medium that the full filing also omits it.
- **Deal impact:** Valuation, closing risk and disclosure.
- **Cross-check:** The full 10-Q on EDGAR. The litigation docket for the order date. News coverage of the Markman ruling and how the stock reacted.

#### SEC-21: Between the 10-K and the 10-Q, the "not probable" and "cannot estimate" wording disappeared
- **Finding:** The 10-K gave the standard reasons for not accruing. The 10-Q keeps "without merit" and "no accrual" but drops both reasons and any statement about a range of loss. Management stopped saying that a loss is not probable and cannot be estimated.
- **Evidence (verbatim):**
  - 10-K Item 3: "We have not recorded an accrual because we do not believe a loss is probable, and we cannot reasonably estimate a possible loss or range of loss." The 10-K also says Vantor seeks "damages and an injunction" on "three of its patents".
  - 10-Q: "we have not recorded an accrual." No reason is given.
  - The 10-Q is silent on accruals for the securities class action and for Pinecrest ($12.0m sought). It says only "defend ourselves vigorously" and "meritorious defenses".
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, section "Item 3. Legal Proceedings"; `TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1"
- **Severity:** Medium
- **Confidence:** Medium. The quotes are exact, but the shorter wording could simply be how the text was excerpted.
- **Deal impact:** Disclosure, and possibly an accrual that should exist but does not.
- **Cross-check:** The full 10-Q legal contingencies note. Ask management for their current view of the reasonably possible range of loss after the Markman order.

#### SEC-22: The bill-and-hold return customer is "our largest customer", never named, but by inference Norvale
- **Finding:** No filing names the customer in the bill-and-hold disclosures. The 10-K names Norvale as the largest customer elsewhere. Both the bill-and-hold note and the 10-Q say "our largest customer". The products came "returned to our inventory" from goods that, per the 10-K, never left Talonfield's warehouses. The reversal was booked as a Q2 2026 revenue reduction, not as a correction of Q4 2025.
- **Evidence (verbatim):**
  - 10-K Note 2: "Of this amount, $24.6 million related to our largest customer. At December 31, 2025, these products remained in our warehouses."
  - 10-Q: "products with a sales value of $9.4 million ... were returned to our inventory, and we issued a credit for the same amount."
  - 10-K Item 1: "Our largest customer, Norvale Retail Group, Inc."
- **My math:**
  - Q4 2025 bill-and-hold: 31.8 / 154.4 = 20.6% of Q4 revenue.
  - Largest customer's share of bill-and-hold: 24.6 / 31.8 = 77.4%.
  - Returned: 9.4 / 24.6 = 38.2% of that customer's bill-and-hold, and 9.4 / 31.8 = 29.6% of all bill-and-hold.
  - Delivered: 31.8 - 9.4 = 22.4, which matches the 10-Q.
  - The reversal is 9.4 / 112.9 = 8.3% of Q2 2026 revenue.
- **Interpretation:** Goods sitting in Talonfield's own warehouse that were later "returned" raise the question of whether criterion (a), a "substantive" reason, was met in Q4 2025. If it was not, this is an error correction rather than a current-period amendment.
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, sections "Note 2" and "Item 1"; `TLFS_10-Q_Q2-2026_excerpts.md`, section "Bill-and-hold amendment"
- **Severity:** High
- **Confidence:** High on the numbers. Medium that the customer is Norvale (an inference, which assumes Norvale was still the largest customer in May 2026).
- **Deal impact:** Valuation (quality of earnings), disclosure, and the Norvale relationship.
- **Cross-check:** Norvale purchase orders and amendments. News on Norvale's ordering. The securities complaint's allegations about Q4 2025.

#### SEC-23: Critical audit matter not found. The auditor change was tied to Q4 bill-and-hold procedures
- **Finding:** The auditor's report is not in the files, so no critical audit matter on bill-and-hold or revenue was found in SEC filings. The filings do show three things:
  - Linden Barr issued an adverse opinion on internal control over financial reporting (ICFR).
  - Hartwell & Pryce had warned that it would need to expand procedures for exactly these Q4 2025 arrangements, and was dismissed shortly afterwards.
  - The material weakness was still not remediated at June 30, 2026.
- **Evidence (verbatim):**
  - 8-K: "additional audit procedures would be required for revenue arrangements with these terms expected in the fourth quarter of 2025, which would expand the scope of its audit."
  - Hartwell & Pryce was dismissed November 10, 2025, and Linden Barr was engaged November 12, 2025.
  - 10-K 9A: "Linden Barr LLP issued an adverse opinion on the effectiveness of our internal control over financial reporting."
  - 10-Q Item 4: "The material weakness described in our 2025 Form 10-K has not yet been remediated."
- **Source:** `TLFS_8-K_2025-11-14_auditor-change.md`, section "Reportable event"; `TLFS_10-K_FY2025_excerpts.md`, section "Item 9A"; `TLFS_10-Q_Q2-2026_excerpts.md`, section "Item 4"
- **Severity:** High
- **Confidence:** High on the quoted facts. The critical audit matter itself was not found.
- **Deal impact:** Disclosure and valuation. The same weakness affects how reliable the covenant calculations are.
- **Cross-check:** The full 10-K auditor's report (critical audit matters). Exhibit 16.1. Audit committee minutes.

#### SEC-24: Option, RSU and PSU counts and exercise prices not found
- **Finding:** No filing gives counts of options, RSUs or PSUs, or exercise prices, so a fully diluted share count cannot be built from the SEC set.
- **Available data points:**
  - Basic shares: 46,912,408 at February 27, 2026.
  - Hale owns 6,690,000 shares (14.2%), which implies about 6.69 / 0.142 = 47.1m shares at the proxy date.
  - 2025 diluted EPS gives 18.6 / 0.39 = about 47.7m weighted diluted shares.
  - The deal brief uses 48.3m. That is 1.39m (3.0%) above basic, and each 1.0m shares equals $24.0m at $24.00.
  - Single-trigger equity acceleration for the five executives was $17.6m at December 31, 2025 values.
- **Evidence (verbatim, proxy):** "all unvested equity awards held by executive officers vest in full immediately upon a change in control ("single-trigger")".
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, cover; `TLFS_DEF14A_2026_excerpts.md`, sections "Security ownership" and "Potential payments upon a change in control"
- **Severity:** Medium
- **Confidence:** High on the data points. The award detail was not found in SEC filings.
- **Deal impact:** Valuation (equity value bridge).
- **Cross-check:** The 10-K stock compensation note (not excerpted). A cap table from management. The financial data.

#### SEC-25: D&O insurance, officer indemnification and clawback policy not found, while the CEO and former CFO are defendants
- **Finding:** None of these appears in the SEC files. The securities class action names the CEO and the former CFO. The 142% bonus for 2025 rested on revenue that included the bill-and-hold amounts.
- **Evidence (verbatim):**
  - 10-Q: the suit is "against Talonfield, our Chief Executive Officer and our former Chief Financial Officer".
  - Proxy: "bonus payouts at 142% of target".
  - 8-K: Okafor's separation includes "a cash payment of $900,000 and a general release of claims".
- **My math:** Bonus revenue was 502.3 against a target of 490.0 and a threshold of 470.0. Removing the 9.4 return gives 492.9, still above target. Removing all 31.8 of bill-and-hold gives 470.5, just 0.5 above threshold.
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1"; `TLFS_DEF14A_2026_excerpts.md`, section "2025 annual incentive plan"; `TLFS_8-K_2026-01-21_cfo-departure.md`
- **Severity:** Medium
- **Confidence:** High on the math. The policies were not found in SEC filings.
- **Deal impact:** Post-closing (indemnification obligations and D&O tail cost) and governance.
- **Cross-check:** The D&O policy, its limits and retention. The charter and bylaws on indemnification. The Rule 10D-1 clawback policy (usually a 10-K exhibit). Whether Okafor's release covers the securities claims.

#### SEC-26: Ruiz accrual location not found
- **Finding:** The 10-K says the $3.2m was accrued at December 31, 2025, but does not name the balance sheet line. The 10-Q reports preliminary approval but says nothing about the accrual balance or payment.
- **Evidence (verbatim):**
  - 10-K: "agreed in principle to settle for $3.2 million, which we accrued at December 31, 2025."
  - 10-Q: "On May 20, 2026, the court granted preliminary approval of the $3.2 million settlement."
- **Source:** `TLFS_10-K_FY2025_excerpts.md`, section "Item 3"; `TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (treat it as a debt-like item if unpaid).
- **Cross-check:** The accrued liabilities breakdown in the financial data. The court docket for final approval.

#### SEC-27: Other covenant and liquidity pressure points
- **Finding:** Several disclosed items make a near-term covenant problem more likely:
  - Operating cash flow was negative in H1 2026.
  - The revolver was drawn further.
  - Cash above $25.0m gets no covenant credit. At June 30, that is 33.9 - 25.0 = 8.9.
  - The material weakness continues, and disclosure controls were not effective.
  - The $1.8m of incident costs are "other non-recurring items", which fall in the capped add-back bucket.
  - Norvale holds 38% of gross receivables, which, applied to the 10-K figure, is 0.38 x 121.5 = about 46.2, and the MSA allows termination on 90 days' notice after a change of control.
- **Evidence (verbatim):**
  - 10-Q: "Operating cash flow for the first half of 2026 was negative $4.2 million. We borrowed an additional $10.0 million under our revolving credit facility".
  - 10-Q: "$1.8 million of incident response costs, which are included in "other non-recurring items"".
  - 10-K: "terminate the agreement on 90 days' notice if Talonfield undergoes a change of control."
- **Source:** `TLFS_10-Q_Q2-2026_excerpts.md`, sections "Liquidity and capital resources" and "April 2026 service disruption"; `TLFS_10-K_FY2025_excerpts.md`, sections "Item 1A" and "Note 13"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Closing risk and liquidity in the period before closing.
- **Cross-check:** Weekly cash and revolver usage in the financial data. Collections from Norvale.

### Positive or mitigating points
- Under Reading A, which I think is the most natural reading, the June 30, 2026 test passes at about 2.67x against 3.50x.
- Both facilities mature in August 2029, so there is no near-term maturity wall, and $25.8m of revolver capacity remained.
- $22.4m of the Q4 2025 bill-and-hold goods had been delivered by June 30, 2026.
- The Ruiz settlement is accrued and has preliminary court approval.
- The CFO 8-K states there was no disagreement. The auditor 8-K reports no disagreements, and Hartwell & Pryce agreed with the disclosure.
- Cash severance in the change-in-control agreements is double-trigger.
- No text in the source files tries to instruct the agents.

### Gaps and questions for management
1. Please provide the full credit agreement and all amendments. Does the "Permitted Add-backs" cap cover non-cash stock-based compensation? Which line items made up Consolidated EBITDA for the 2.26x, and what was the dollar amount? Please also provide the compliance certificates.
2. How does the credit agreement define Total Debt? Are letters of credit included?
3. Are there equity cure rights? Have there been any waivers, amendments or lender talks? What is your forecast for the September 30 and December 31, 2026 tests at 3.00x?
4. Why did the August 6, 2026 10-Q leave out the July 22 Markman order? What is your current probable or estimable assessment, and has anything been accrued after the $96.4m expert report? Is an 8-K planned?
5. Was the $9.4m return from Norvale? What was the "substantive" reason for the bill-and-hold at Q4 2025? Did the audit committee or the auditor consider restating?
6. Please provide the auditor's report, including any critical audit matters, and the remediation timeline for the material weakness.
7. Please provide the full equity award table: options with strike prices, RSUs, and PSUs with performance conditions.
8. Please provide the D&O insurance terms, the indemnification agreements, the clawback policy, and whether Okafor's release covers the securities claims.
9. Where does the Ruiz $3.2m sit on the balance sheet, and is it still unpaid?
10. Note that the Q3 2026 10-Q and any 8-K filed after January 21, 2026 are not in the SEC file set.
