## SEC filings analyst: findings

### Files reviewed

All five files were read in full. I also read `data/deal-brief.md` for context.

1. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-K_FY2025_excerpts.md` (filed March 9, 2026)
2. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md` (dated November 14, 2025)
3. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md` (dated January 21, 2026)
4. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_DEF14A_2026_excerpts.md` (filed April 24, 2026)
5. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` (filed August 6, 2026)

**Embedded instructions:** none of the five files contains text that tries to instruct the agents. All files are labeled "EXCERPTS" or are short 8-Ks. When I write "not found in SEC filings", it may mean the item sits in a part of the filing we were not given.

### Findings

#### SEC-01: The 2025 deal-model case is stale. Guidance was cut 37% on EBITDA on August 6, 2026
- **Finding:** The Q2 10-Q replaced the March 9, 2026 outlook. The new outlook is far below the management case the deal model v3 (September 2026) still uses.
- **Evidence:** 10-Q: "We now expect full-year 2026 revenue of $470 million to $490 million and Adjusted EBITDA of $70 million to $78 million. This replaces the outlook we provided on March 9, 2026." Math:
  - Revenue midpoint is $480.0m against the model's $560.0m: 80.0 / 560.0 = 14.3% lower. It is also 4.4% below FY2025's $502.3m.
  - EBITDA midpoint is $74.0m against $118.0m: 44.0 / 118.0 = 37.3% lower.
  - The implied EV is about 11.5 x 118.0 = $1,357m. On $74.0m EBITDA that is 18.3x (inference).
  - Implied H2 2026 revenue is $247.4m to $267.4m, against H2 2025 of 502.3 - 226.5 = $275.8m. Implied H2 EBITDA is $40.1m to $48.1m, against H2 2025 of 98.8 - 39.0 = $59.8m.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Updated 2026 outlook"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "2026 outlook (as of March 9, 2026)"; `data/deal-brief.md`, "Valuation basis".
- **Severity:** Critical. It meets the test of changing value by more than 10%: company guidance puts EBITDA 37.3% below the model's basis.
- **Confidence:** High. Primary source, numbers recomputed.
- **Deal impact:** Valuation.
- **Cross-check:** Financials should give the Q3 2026 trend and a TTM bridge. News should show market reaction and any later guidance. Ask why model v3, built after August 6, kept the March case.

#### SEC-02: $31.8m of bill-and-hold revenue in Q4 2025 was 20.6% of the quarter, and 77% of it came from Norvale
- **Finding:** The "record" Q4 2025 was flattered by bill-and-hold sales. These goods were still in Talonfield's warehouses at year-end. Without them, growth is much lower.
- **Evidence:** Note 2: "In the fourth quarter of 2025 we recognized $31.8 million of hardware revenue under bill-and-hold arrangements (2024: none material). Of this amount, $24.6 million related to our largest customer." Math:
  - 31.8 / 154.4 = 20.6% of Q4 revenue.
  - 24.6 / 31.8 = 77.4% came from Norvale.
  - FY2025 without bill-and-hold: 502.3 - 31.8 = $470.5m, growth of 470.5 / 421.7 = 11.6% (reported 19.1%).
  - Q4 2024 was about 154.4 / 1.324 = $116.6m. Q4 2025 without bill-and-hold was $122.6m, about 5.1% growth (reported 32.4%).
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 2. Revenue Recognition" and "Item 7, 2025 highlights".
- **Severity:** High.
- **Confidence:** High. Primary source, recomputed. The Q4 2024 figure is derived from the stated growth rate.
- **Deal impact:** Valuation (quality of earnings) and disclosure.
- **Cross-check:** Use financials for quarterly revenue by customer and the inventory/warehouse records. News may report channel stuffing. Court records: the securities class action complaint.

#### SEC-03: $9.4m of Q4 2025 bill-and-hold revenue was reversed in May 2026, and some Q2 2026 weakness is pull-forward
- **Finding:** Goods the company had booked as sold to its largest customer were returned to inventory and credited. The reversal hit Q2 2026, not 2025. The 10-Q also admits that customers "pulled forward" orders into Q4 2025.
- **Evidence:** 10-Q: "products with a sales value of $9.4 million that we had recognized as revenue under a bill-and-hold arrangement in the fourth quarter of 2025 were returned to our inventory, and we issued a credit." Math:
  - 9.4 / 24.6 = 38.2% of Norvale's bill-and-hold amount, if "largest customer" is still Norvale. The 10-Q does not name the customer. The 10-K names Norvale as largest customer for 2025.
  - The remaining 31.8 - 9.4 = $22.4m was delivered by June 30, 2026.
  - Q2 2026 before the $9.4m credit and $2.3m SLA credits: 112.9 + 9.4 + 2.3 = $124.6m, or +6.0% on $117.6m. The 10-Q says pull-forward also hurt Q2, so underlying demand cannot be isolated (inference).
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Revenue" and "Bill-and-hold amendment".
- **Severity:** High.
- **Confidence:** High on the facts. Medium that the customer is Norvale (inferred from the "largest customer" wording).
- **Deal impact:** Valuation and disclosure. Booking this as a Q2 2026 adjustment rather than restating 2025 raises the question of whether the bill-and-hold criteria were met at December 31, 2025. That question should go to accounting diligence (interpretation).
- **Cross-check:** Financials for customer-level revenue in Q4 2025 and Q2 2026. Litigation: whether the securities complaint cites this amendment. Ask Linden Barr why this was not treated as an error correction.

#### SEC-04: The auditor was dismissed after flagging a material weakness and widening its Q4 audit scope
- **Finding:** Hartwell & Pryce, auditor since 2016, was dismissed on November 10, 2025. In Q3 2025 it had warned of a material weakness and said Q4 non-standard revenue would need more audit work. The $31.8m bill-and-hold revenue then landed in Q4 under the new auditor, Linden Barr, engaged November 12, 2025.
- **Evidence:** 8-K "Reportable event": additional procedures "would be required for revenue arrangements with these terms expected in the fourth quarter of 2025, which would expand the scope of its audit." The 8-K also says there were "no disagreements". Hartwell & Pryce's Exhibit 16.1 letter agrees with the disclosure.
- **Source:** `data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md`, Item 4.01 (a), "Reportable event", (b); `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 2".
- **Severity:** High.
- **Confidence:** High on the facts. Reading the timing as possible opinion shopping is my interpretation, not a statement in the filing.
- **Deal impact:** Disclosure, post-closing (restatement risk), and indemnity.
- **Cross-check:** News on the auditor change. Audit Committee minutes. Hartwell & Pryce's communications. Linden Barr's opinion on the financial statements, which was not found in SEC filings (only the adverse ICFR opinion is quoted).

#### SEC-05: The revenue-control material weakness was still not fixed at June 30, 2026
- **Finding:** Internal control over financial reporting (ICFR) was ineffective at December 31, 2025, and Linden Barr gave an adverse ICFR opinion. Disclosure controls were still ineffective at June 30, 2026. The weakness covers the same bill-and-hold contracts behind SEC-02 and SEC-03.
- **Evidence:** 10-K 9A: "We did not design and maintain effective controls over the review of hardware contracts with non-standard delivery and acceptance terms, including bill-and-hold arrangements." 10-Q Item 4: "has not yet been remediated". The weakness was "first identified in the third quarter of 2025".
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 9A"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part I, Item 4".
- **Severity:** High.
- **Confidence:** High. Primary source.
- **Deal impact:** Post-closing (integration into Arbelion's SOX environment) and disclosure.
- **Cross-check:** Whether the Q3 2025 10-Q disclosed the weakness (not in our files). A remediation timeline from management.

#### SEC-06: Covenant step-down to 3.00x from September 30, 2026 leaves thin headroom on the new guidance
- **Finding:** The maximum Total Net Leverage Ratio drops from 3.50x to 3.00x for quarters ending on or after September 30, 2026. At the low end of the cut guidance, the ratio would be close to 3.00x by December 31, 2026 (projection).
- **Evidence:** Note 9 thresholds are as above. Definitions:
  - "cash netting capped at $25.0 million"
  - Permitted Add-backs "may not exceed 15% of Consolidated EBITDA calculated before including those Permitted Add-backs"
  - The 10-Q states the ratio was 2.26 to 1.00 at June 30, 2026.

  Math (projection; assumes the term loan is still $185.0m, because the June balance was not found in SEC filings):
  - Net debt = 185.0 + 45.0 - 25.0 = $205.0m.
  - 205.0 / 2.26 implies covenant EBITDA of about $90.7m. TTM Adjusted EBITDA is 98.8 - 39.0 + 29.9 = $89.7m, which is consistent.
  - At FY2026 guidance EBITDA of $70m to $78m, the ratio is 205.0 / 70 = 2.93x down to 205.0 / 78 = 2.63x.
  - The break-even EBITDA at 3.00x is $68.3m, only 2.4% below the low end of guidance.
  - Each extra $10m of net debt adds about 0.14x at $70m EBITDA.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 9. Debt"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Covenant compliance" and "Results summary".
- **Severity:** High. Under the calibration rule, this becomes Critical if a breach occurs before signing or closing. The September 30, 2026 test result was not found in SEC filings.
- **Confidence:** Medium. The thresholds are primary-source facts, but the forward ratio is a projection with an assumed term loan balance. It is also unclear whether stock-based compensation counts as a capped "Permitted Add-back".
- **Deal impact:** Closing risk and liquidity.
- **Cross-check:** Financials for the Q3 2026 covenant certificate, the TTM EBITDA bridge and the term loan balance. News on any lender waiver or amendment.

#### SEC-07: A change of control is an event of default, so about $230m of debt must be refinanced at closing
- **Finding:** Closing the deal would let the lenders demand immediate repayment of all outstanding loans.
- **Evidence:** "A change of control of Talonfield is an event of default, which allows the lenders to demand immediate repayment of all outstanding loans."
  - Debt was $220.0m at December 31, 2025: term loan $185.0m maturing August 2029, plus $35.0m on the revolver.
  - The revolver was $45.0m at June 30, 2026. Total is about $230.0m, assuming the term loan is unchanged (inference).
  - Pricing is SOFR + 3.25% to 3.75%.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 9. Debt"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources".
- **Severity:** High. It is cured by refinancing at closing.
- **Confidence:** High.
- **Deal impact:** Closing (funds flow) and valuation (net debt in the equity bridge).
- **Cross-check:** Financials for the June 30 debt schedule and any prepayment fees.

#### SEC-08: Cash flow and liquidity are getting worse, and the "collections to normalize" claim did not hold
- **Finding:** Operating cash flow fell sharply in 2025 and turned negative in H1 2026. Cash is falling even with more revolver borrowing.
- **Evidence:**
  - The 10-K said OCF was $9.7m in 2025, against $40.8m in 2024 and net income of $18.6m. It added: "We expect collections to normalize in 2026."
  - The 10-Q reports H1 2026 OCF of negative $4.2m. Cash fell from $41.6m to $33.9m despite a $10.0m extra revolver draw.
  - Revolver availability is $25.8m after $4.2m of letters of credit. Liquidity is 33.9 + 25.8 = $59.7m.
  - Going-concern language: not found in SEC filings.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Liquidity"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources".
- **Severity:** Medium (High if Q3 cash burn continued).
- **Confidence:** High.
- **Deal impact:** Liquidity before closing and working-capital peg.
- **Cross-check:** Financials for monthly cash, AR aging and contract assets.

#### SEC-09: Receivables jumped 59% while the bad-debt allowance was cut (a judgment dated December 31, 2025)
- **Finding:** Gross AR rose much faster than revenue, and Norvale's share of AR rose. Yet management reduced the allowance, citing better collections. Later cash flow does not support that view.
- **Evidence:**
  - Gross AR went from $76.3m to $121.5m, up 59.2%, against revenue growth of 19.1%.
  - Days sales outstanding (DSO) went from 76.3 / 421.7 x 365 = 66.0 to 121.5 / 502.3 x 365 = 88.3 days.
  - The allowance went from $2.9m to $2.6m, or from 3.8% to 2.1% of gross AR.
  - The stated reason: "The decrease in the allowance reflects improved collection experience with our enterprise customers."
  - Norvale held 38% of gross AR, which is 0.38 x 121.5 = about $46.2m.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 5" and "Note 13".
- **Severity:** Medium.
- **Confidence:** High on the numbers. Doubt about the judgment is my interpretation, based on the H1 2026 negative OCF in SEC-08.
- **Deal impact:** Valuation (working capital) and quality of earnings.
- **Cross-check:** Financials for the AR aging by customer and whether the bill-and-hold receivables were collected.

#### SEC-10: Norvale (31.1% of revenue) can terminate on 90 days' notice after a change of control
- **Finding:** This deal itself would trigger a termination right for the largest customer. Norvale has no minimum volume, and the MSA ends September 30, 2027.
- **Evidence:** "The Norvale MSA allows Norvale to terminate the agreement on 90 days' notice if Talonfield undergoes a change of control. Norvale is not required to purchase any minimum volume." Math:
  - Norvale revenue was 0.311 x 502.3 = about $156.2m in 2025.
  - Without its $24.6m of bill-and-hold, Norvale is (156.2 - 24.6) / 470.5 = 28.0% of revenue, the same share as in 2024. So the rise in concentration came from bill-and-hold (inference).
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 1. Business, Customers", "Item 1A" and "Note 13".
- **Severity:** Critical. It meets the test of changing value by more than 10%: the deal would trigger a termination right over about $156.2m, or 31.1% of revenue.
- **Confidence:** High.
- **Deal impact:** Closing (consent or waiver as a condition) and valuation.
- **Cross-check:** News on Norvale's relationship, sourcing reviews or competitor wins. Financials for Norvale revenue by quarter in 2026. Talk to Norvale directly with management's permission.

#### SEC-11: The Vantor patent case could stop sales of Gen-3 (about 42% of revenue). No accrual, trial March 2027
- **Finding:** Vantor seeks damages and an injunction on Gen-3 navigation. The company has recorded no accrual and gives no range of loss, both as of March 9, 2026 and as of August 6, 2026.
- **Evidence:**
  - Filed March 2024 in the District of Delaware, covering three patents.
  - "We have not recorded an accrual because we do not believe a loss is probable, and we cannot reasonably estimate a possible loss or range of loss."
  - The 10-Q says the case is in discovery and trial is "currently scheduled for March 2027".
  - Gen-3 was about 70% of hardware revenue: 0.70 x 301.4 = $211.0m, or 42.0% of total revenue.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 3" and "Item 1"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1".
- **Severity:** High.
- **Confidence:** High on the disclosure. The outcome is unknown.
- **Deal impact:** Valuation, indemnity or escrow, and post-closing.
- **Cross-check:** Court docket for claim construction rulings, damages expert reports and settlement talks. News on Vantor.

#### SEC-12: A securities class action names the CEO and the former CFO over revenue and controls
- **Finding:** The suit was filed June 3, 2026 in the Southern District of Ohio. No accrual or loss estimate is disclosed. It was added as a new risk factor.
- **Evidence:** The complaint alleges "false or misleading statements about our revenue and our internal controls". The defendants are Talonfield, the CEO and the former CFO. The disclosed response is only "We intend to defend ourselves vigorously."
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1" and "Item 1A".
- **Severity:** High.
- **Confidence:** High on the existence of the suit. Low on the merits.
- **Deal impact:** Post-closing liability, D&O tail insurance, and indemnity.
- **Cross-check:** Court records for the class period, the alleged stock drop, lead plaintiff and whether bill-and-hold is cited. News for the date of the price drop.

#### SEC-13: The April 2026 cyber incident was judged "not material" (as of August 6, 2026), but a $12.0m customer suit followed
- **Finding:** FieldOS was taken offline for up to three days. The company concluded the incident was not material. Direct costs so far are $4.1m, and Pinecrest Distribution sued for $12.0m. No accrual is stated for Pinecrest.
- **Evidence:**
  - Incident detected April 11, 2026.
  - "we concluded that the incident was not material".
  - Costs: $1.8m response costs, which are added back to Adjusted EBITDA, plus $2.3m of SLA credits = $4.1m.
  - Pinecrest sued on June 17, 2026 for $12.0m: "We believe we have meritorious defenses."
  - An 8-K Item 1.05 cyber filing was not found in SEC filings.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "April 2026 service disruption" and "Part II, Item 1".
- **Severity:** Medium.
- **Confidence:** High on the facts. Doubt about the materiality judgment is my interpretation.
- **Deal impact:** Disclosure and post-closing (cyber remediation, further claims).
- **Cross-check:** Litigation for the Pinecrest docket. News on how many customers were affected and any data-theft claims. Financials for Pinecrest's revenue rank (not stated in SEC filings).

#### SEC-14: The CFO resigned 7 weeks before the 10-K and was paid $900,000
- **Finding:** Daniel Okafor gave notice on January 20, 2026, effective February 15. That was after the auditor dismissal and the material weakness, and before the 10-K was filed on March 9. A cash payment for a voluntary resignation is unusual. He is now a defendant in the securities suit. As of August 6, 2026 the CFO is still interim.
- **Evidence:** 8-K: the resignation "was not the result of any disagreement". The separation agreement gives "a cash payment of $900,000 and a general release of claims". Rachel Simmons, VP and Controller, signs as Interim CFO in the 10-Q.
- **Source:** `data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md`, Item 5.02; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 18"; `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, "Potential payments"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, header.
- **Severity:** High.
- **Confidence:** High on the facts. The reason for the payment is not disclosed.
- **Deal impact:** Governance, disclosure, and post-closing (finance leadership).
- **Cross-check:** News on why Okafor left. Court records for whether he is cooperating or has separate counsel. Ask for the separation agreement and the scope of the release.

#### SEC-15: The 2025 bonus paid at 142% of target relied on bill-and-hold revenue
- **Finding:** Revenue of $502.3m came close to the $510.0m maximum. Without bill-and-hold it would have been $470.5m, just above the $470.0m threshold. $9.4m of the bill-and-hold was later reversed.
- **Evidence:** Revenue threshold/target/maximum is 470.0 / 490.0 / 510.0 against actual 502.3. EBITDA is 88.0 / 95.0 / 102.0 against actual 98.8. Bonus payouts were "142% of target for all executive officers". Bill-and-hold EBITDA contribution is not disclosed, so its effect on the EBITDA measure cannot be computed. A clawback policy was not found in SEC filings.
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, "2025 annual incentive plan"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 2".
- **Severity:** Medium.
- **Confidence:** High on the numbers. The incentive link is my interpretation.
- **Deal impact:** Governance and post-closing (clawback, retention design).
- **Cross-check:** The clawback policy and Compensation Committee minutes.

#### SEC-16: Change-in-control payouts total $28.6m, including $17.6m of single-trigger equity vesting
- **Finding:** All unvested executive equity vests on the change of control even if the executive stays. That weakens the retention value of those awards after closing.
- **Evidence:**
  - "all unvested equity awards held by executive officers vest in full immediately upon a change in control ('single-trigger')".
  - Totals: cash severance $9.6m (double-trigger), equity $17.6m, other $1.4m, for $28.6m in all.
  - 28.6 / 1,159 = 2.5% of equity value.
  - These estimates are as of December 31, 2025, so the equity value at $24.00 may differ.
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, "Potential payments upon a change in control".
- **Severity:** Medium.
- **Confidence:** High.
- **Deal impact:** Valuation (transaction costs) and post-closing retention.
- **Cross-check:** Financials for the full award schedule at the $24.00 price.

#### SEC-17: The CEO's family owns the HQ lease, and the landlord can reset rent after a change of control
- **Finding:** Hale Family Properties can reset rent to "fair market value", set by an appraiser the landlord chooses, if Talonfield is acquired. The CEO is on both sides of the deal.
- **Evidence:**
  - The lease covers HQ and the main assembly facility and runs to December 2033.
  - 2025 rent was $2.1m, with 3% annual increases.
  - Remaining contract rent for 2026 to 2033 is about $19.2m, assuming the increases start in 2026 (inference).
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, "Certain relationships and related party transactions".
- **Severity:** Medium.
- **Confidence:** High.
- **Deal impact:** Post-closing cost and structure (seek a waiver at signing).
- **Cross-check:** Financials for the lease liability. A local real estate market rent benchmark.

#### SEC-18: Board structure: combined Chair and CEO, no lead independent director
- **Finding:** Marcus Hale is founder, Chairman and CEO, with no lead independent director. He owns 14.2%, and directors and officers together own 17.6%. Five of the seven directors are independent.
- **Evidence:** "The Board has not appointed a lead independent director."
  - Hale's stake at $24.00 is worth 6.69m x 24.00 = $160.6m (inference).
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, "Security ownership" and "Board of Directors".
- **Severity:** Low.
- **Confidence:** High.
- **Deal impact:** Governance. Consider a support agreement from Hale.
- **Cross-check:** News on board dynamics or activist involvement.

#### SEC-19: The goodwill test (as of October 1, 2025) came before the guidance cut, and no interim test is disclosed
- **Finding:** Goodwill of $98.4m, including $57.4m from Lumora, was found not impaired as of October 1, 2025. The inputs, such as share price, market cap and discount rate, were not found in SEC filings. Since then, 2026 EBITDA guidance has fallen 37%, and the stock closed at $17.85 on October 16, 2026. An interim impairment test is not mentioned in the Q2 10-Q.
- **Evidence:** "We performed our annual impairment test as of October 1, 2025 and found no impairment."
  - Lumora goodwill is 57.4 / 85.0 = 67.5% of its purchase price.
  - Market cap at $17.85 x 48.3m diluted shares = $862.2m (inference). The share price on October 1, 2025 was not found in SEC filings.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Note 15" and "Item 1"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Updated 2026 outlook"; `data/deal-brief.md`.
- **Severity:** Medium.
- **Confidence:** Medium. The test date is a fact, but whether the judgment is now in doubt depends on market data outside these files.
- **Deal impact:** Disclosure (possible impairment around the time of signing). The cash value effect is limited.
- **Cross-check:** Financials and market data for the share price on October 1, 2025 against now, book equity, and Lumora's revenue against its acquisition case.

#### SEC-20: All LiDAR sensors come from one unnamed supplier in China
- **Finding:** Every Talon AMR depends on a single-source LiDAR supplier in China, with no qualified second source. The supplier is not named.
- **Evidence:** "We do not currently have a qualified second source." Tariffs are cited as a risk.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 1. Suppliers" and "Item 1A".
- **Severity:** Medium.
- **Confidence:** High.
- **Deal impact:** Post-closing (supply chain, tariffs).
- **Cross-check:** News on tariffs on Chinese LiDAR. Financials for COGS exposure. Ask management for the supplier's name.

#### SEC-21: The wording changed between filings, and management stopped repeating some metrics and claims
- **Finding:** The way Q4 2025 was described changed over time, and some 10-K metrics are absent from the 10-Q excerpts:
  - The 10-K MD&A credits Q4 to "strong hardware deliveries to enterprise customers", while Note 2 says the bill-and-hold goods "remained in our warehouses".
  - The 10-Q later says customers "pulled forward" orders into Q4 2025.
  - FieldOS ARR ($139.2m) and the 118% net revenue retention figure are not updated in the 10-Q excerpts.
  - The "collections to normalize" expectation is not repeated.
  - The 10-Q says there were no material changes to risk factors apart from securities litigation. The cyber risk factor stays hypothetical after an actual incident. No new risk factor covers the guidance cut, the covenant step-down or the Pinecrest suit.
- **Evidence:** Quotes above. 10-Q 1A: "There have been no material changes to the risk factors in our 2025 Form 10-K, except for the following addition".
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 7" and "Note 2"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Revenue" and "Part II, Item 1A".
- **Severity:** Medium.
- **Confidence:** Medium. The files are excerpts, so the missing metrics may appear in sections we were not given.
- **Deal impact:** Disclosure (relevant to the class action).
- **Cross-check:** Investor day materials and earnings call transcripts in the news for ARR and NRR trends after Q4 2025. Financials for ARR.

#### SEC-22: The Ruiz wage-and-hour settlement is accrued and has preliminary approval
- **Finding:** The $3.2m settlement was accrued at December 31, 2025. The court granted preliminary approval on May 20, 2026.
- **Evidence:** "agreed in principle to settle for $3.2 million, which we accrued at December 31, 2025".
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, "Item 3"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1".
- **Severity:** Low.
- **Confidence:** High.
- **Deal impact:** Disclosure. Confirm final approval.
- **Cross-check:** Court docket for the final approval hearing date.

### Positive or mitigating points

- **Auditor change disclosure is clean on paper.** The 8-K reports "no disagreements", and Hartwell & Pryce's Exhibit 16.1 letter agrees with it. Prior audit opinions for 2023 and 2024 were not adverse or modified (`TLFS_8-K_2025-11-14_auditor-change.md`).
- **Most of the bill-and-hold goods shipped.** $22.4m of the $31.8m was delivered by June 30, 2026 (10-Q).
- **The covenant was met at June 30, 2026.** The ratio was 2.26x against a 3.50x maximum, and covenants were met at December 31, 2025.
- **Debt maturities are not near.** Both the term loan and the revolver mature in August 2029.
- **Cash severance is double-trigger.** Okafor is not eligible for change-in-control payments (DEF 14A).
- **The software business looked healthy at year-end 2025.** Software revenue grew 27.1% and FieldOS ARR was $139.2m, up 27%, at December 31, 2025. This is not updated after that date in our files.
- **Remediation has started.** The company hired a director of technical accounting and created a contract review committee (10-K 9A).
- **No going-concern language** was found in SEC filings.
- **No prompt-injection or instruction text** was found in any SEC file.

### Gaps and questions for management

1. **Q3 2026 data.** What was the covenant ratio at September 30, 2026, the first 3.00x test? Were waivers or amendments sought? What were Q3 cash, revolver draws and the June 30 term loan balance? (Not found in SEC filings.)
2. **Consolidated EBITDA.** Ask for the covenant EBITDA calculation. Are stock-based compensation and the $1.8m incident costs inside the 15% Permitted Add-back cap?
3. **The $9.4m credit.** Why was it booked in Q2 2026 rather than restating 2025? Was the customer Norvale? What did Linden Barr conclude about the December 31, 2025 bill-and-hold criteria?
4. **Auditor dismissal.** What did the Audit Committee record as the reason? Was Linden Barr's opinion on the 2025 financial statements unqualified? (Not found in SEC filings.)
5. **Okafor's payment.** Why was $900,000 paid on a voluntary resignation? What claims did the release cover? When will a permanent CFO be appointed?
6. **Norvale.** Has Norvale been approached about consent or a waiver of its change-of-control termination right? What were its 2026 volumes and its share of AR at June 30, 2026?
7. **Litigation reserves.** What are the accrual status and estimated ranges for Vantor, the securities class action and Pinecrest? Is there a D&O insurance tower and retention?
8. **Cyber incident.** Was an 8-K Item 1.05 filed? What supported the "not material" conclusion? How many customers were affected, and are other claims threatened?
9. **Goodwill.** Ask for the October 1, 2025 test inputs (share price, market cap, discount rate, Lumora forecast). Was an interim test done after the August guidance cut, and what are the results of the October 1, 2026 annual test?
10. **Bonus clawback.** Is there a clawback policy, and does it apply to 2025 bonuses given the $9.4m reversal?
11. **HQ lease.** Will Hale Family Properties waive the change-of-control rent reset?
12. **LiDAR supplier.** Ask for the supplier's name, the contract term, any tariff exposure already in 2026 COGS, and plans for a second source.
13. **Missing metrics.** Ask for FieldOS ARR and net revenue retention at June 30, 2026 (not found in the 10-Q excerpts).
14. **Deal model.** Why does model v3 (September 2026) still use the March 2026 case when the August 6, 2026 guidance replaced it?
