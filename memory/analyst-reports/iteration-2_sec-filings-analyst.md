# Iteration 2: sec-filings-analyst report (unedited)

- Saved by the lead agent: 2026-10-18 03:54 EST
- Task: SEC filings follow-ups, iteration 2
- Subagent ID: aaaf79e7f0a8bd2c0
- The report below is the subagent's final message exactly as returned. Only the harness's hand-back line and its two-space line indent were removed.

---

## SEC filings analyst: findings (iteration 2)

### Files reviewed

I read all five files in full, plus nothing outside `data/sec-filings/`:
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-K_FY2025_excerpts.md` (filed March 9, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` (filed August 6, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_DEF14A_2026_excerpts.md` (filed April 24, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md`

None of the files contained text that tried to instruct the agents. There is no filing in the folder dated after August 6, 2026, so I found no 8-K covering the August 14, September 4 or September 25 court events.

### Answers to follow-up questions

**1. Credit agreement covenant**

Quotes (10-K, Note 9 "Debt"):
- Cap and step-down: "no more than 3.50 to 1.00 for each fiscal quarter ending on or before June 30, 2026, and no more than 3.00 to 1.00 for each fiscal quarter ending on or after September 30, 2026."
- Test dates: "The ratio is tested quarterly on a trailing twelve-month basis."
- Ratio: "(Total Debt minus unrestricted cash, with cash netting capped at $25.0 million) divided by Consolidated EBITDA."
- EBITDA base: "net income plus interest, taxes, depreciation and amortization, plus non-cash stock-based compensation, plus restructuring, integration and other non-recurring charges ("Permitted Add-backs")."
- 15% cap: "Permitted Add-backs may not exceed 15% of Consolidated EBITDA calculated before including those Permitted Add-backs."
- Change of control: "A change of control of Talonfield is an event of default, which allows the lenders to demand immediate repayment of all outstanding loans."
- Note 9 also says: "We were in compliance with all covenants at December 31, 2025."
- Breach (10-K, Item 1A "Our credit agreement contains financial covenants"): "A breach could allow our lenders to accelerate repayment of our debt."
- 10-Q covenant sentence (MD&A "Covenant compliance"): "Our Total Net Leverage Ratio was 2.26 to 1.00 at June 30, 2026, compared with a maximum of 3.50 to 1.00, and we were in compliance."
- Letters of credit (10-Q, MD&A "Liquidity and capital resources"): "After $4.2 million of outstanding letters of credit, $25.8 million was available under the facility."

What the filings do not say:
- How "Total Debt" is defined, and whether letters of credit count toward it: not found in SEC filings. Letters of credit appear only in the revolver availability sentence.
- Equity cure rights: not found in SEC filings.
- How the 2.26x was calculated: not found in SEC filings. The 10-Q gives no reconciliation or EBITDA figure for the covenant.

Interpretation:
- The definition is a summary, and its wording is ambiguous on stock-based compensation. Read literally, the label "Permitted Add-backs" is attached only to the last item ("restructuring, integration and other non-recurring charges"). On that reading, stock-based compensation is a base adjustment and is not subject to the 15% cap. This is my inference, not a stated fact.
- My recalculation of the 2.26x is in SEC-25 below. It suggests the company used its full Adjusted EBITDA with no 15% cap applied.

**2. Vantor in the 10-Q versus the 10-K**

Full 10-K passage (Item 3 "Legal Proceedings"), in three quotes:
- "Vantor alleges that the navigation system in our Talon Gen-3 robots infringes three of its patents and seeks damages and an injunction."
- "We believe the claims are without merit and intend to defend ourselves vigorously."
- "We have not recorded an accrual because we do not believe a loss is probable, and we cannot reasonably estimate a possible loss or range of loss."
- The 10-K also lists the case as "filed March 2024" in the District of Delaware.

10-K risk factor: "An adverse outcome could require us to pay substantial damages or royalties, redesign our products, or stop selling Talon Gen-3 robots."

Full 10-Q passage (Part II, Item 1 "Legal Proceedings"):
- "The case is in discovery. Trial is currently scheduled for March 2027. We continue to believe the claims are without merit, and we have not recorded an accrual."

10-Q risk factors (Part II, Item 1A): "There have been no material changes to the risk factors in our 2025 Form 10-K, except for the following addition". The only addition is a securities litigation risk factor.

What the 10-Q does not mention:
- The July 22, 2026 claim construction order, or any ruling: not found in SEC filings.
- Gen-3 Plus: not found in any SEC filing.
- Any change in the company's view: none. The 10-Q says "continue to believe".

Interpretation:
- The 10-Q was filed August 6, 2026, 15 days after the July 22 order, and does not mention it.
- The 10-Q also drops the 10-K's statement that a loss range "cannot reasonably estimate[d]", and its reference to damages and an injunction.
- The later court events (August 14, September 4 and September 25) came after the 10-Q was filed, so the 10-Q could not have disclosed them.

**3. Norvale, Kinetic Aisle and the largest customer in the 10-Q**

- Norvale by name, Kinetic Aisle, or a customer building its own robots: not found in the 10-Q or any other SEC filing.
- The only 10-Q text about the largest customer (MD&A "Revenue"): "Q2 2026 revenue includes a $9.4 million reduction related to a contract amendment with our largest customer". Also, from "Bill-and-hold amendment": "In May 2026 we amended a purchase order with our largest customer."
- 10-Q risk factors: "no material changes to the risk factors in our 2025 Form 10-K" (the only exception is securities litigation).

10-K risk factor (Item 1A), in four quotes:
- "We depend on a small number of customers, and the loss of Norvale would materially harm our business."
- "Norvale accounted for 31.1% of our 2025 revenue and 38% of our gross accounts receivable at December 31, 2025."
- "The Norvale MSA allows Norvale to terminate the agreement on 90 days' notice if Talonfield undergoes a change of control."
- "Norvale is not required to purchase any minimum volume."
- The 10-K (Item 1 "Customers") also says the Norvale MSA "runs through September 30, 2027."

Interpretation: news places the Norvale purchase of Kinetic Aisle on or before June 24, 2026. The 10-Q, filed about six weeks later, keeps the customer concentration risk factor unchanged and does not say whether Norvale's relationship with the company has changed.

**4. Who returned the US$9.4 million of bill-and-hold product, and when**

- 10-Q (MD&A "Bill-and-hold amendment"): "In May 2026 we amended a purchase order with our largest customer."
- "products with a sales value of $9.4 million that we had recognized as revenue under a bill-and-hold arrangement in the fourth quarter of 2025 were returned to our inventory, and we issued a credit for the same amount."
- "We recorded the credit as a reduction of revenue in the second quarter of 2026."
- "The remaining $22.4 million of products recognized under bill-and-hold arrangements in the fourth quarter of 2025 had been delivered to customers as of June 30, 2026."

Timing:
- Amendment: "May 2026". The exact day is not found in SEC filings.
- Return: no separate date is given. The return happened "under the amendment" and was booked in Q2 2026.

Interpretation:
- The 10-Q does not name the customer. The 10-K (Item 1 "Customers") names Norvale as "Our largest customer", and Note 2 says "$24.6 million related to our largest customer." It is therefore highly likely, though not stated in the 10-Q, that Norvale returned the goods.
- Math:
  - 9.4 / 24.6 = 38.2% of Norvale's Q4 2025 bill-and-hold revenue.
  - 9.4 / 31.8 = 29.6% of all Q4 2025 bill-and-hold revenue.
  - 31.8 - 9.4 = 22.4, which matches the 10-Q.
- Both the amendment and the return fall in May 2026, around the time of the May 12 short report and before the June 24 Kinetic Aisle news.

**5. Bill-and-hold criteria in the 10-K**

- 10-K Note 2 "Revenue Recognition": "In some cases a customer asks us to hold finished products at our facilities until the customer's site is ready (a "bill-and-hold" arrangement)."
- "We recognize revenue under a bill-and-hold arrangement when (a) the reason for the arrangement is substantive, (b) the products are separately identified as belonging to the customer,"
- "(c) the products are ready for physical transfer, and (d) we cannot use the products or direct them to another customer."
- "In the fourth quarter of 2025 we recognized $31.8 million of hardware revenue under bill-and-hold arrangements (2024: none material)."
- "At December 31, 2025, these products remained in our warehouses."

Interpretation:
- A customer request appears only in the descriptive sentence ("a customer asks us"). It is not one of the four listed criteria; criterion (a) asks only for a "substantive" reason.
- No filing says that customers actually requested the Q4 2025 arrangements: not found in SEC filings.
- The 10-Q gives a different reason for weak Q2 hardware: "orders that customers pulled forward into the fourth quarter of 2025." That fits poorly with the 10-K's description of goods held "until the customer's site is ready."

**6. Vantor as a competitor**

- No filing describes Vantor Robotics as a competitor, and the excerpts contain no Competition section: not found in SEC filings.
- Vantor appears only as the plaintiff (10-K Item 3; 10-Q Part II, Item 1).

Interpretation: the filings do not tell investors that the plaintiff is a direct rival. That matters because a direct competitor is more likely to win a permanent injunction. The 10-K already says Vantor "seeks damages and an injunction."

**7. Scale of the April 2026 incident**

- 10-Q (MD&A "April 2026 service disruption"): "we detected unauthorized activity in part of the FieldOS cloud environment."
- "As a precaution we took the affected systems offline, which interrupted fleet operations for some customers for up to three days."
- "we concluded that the incident was not material, and we have not identified evidence that customer data was taken."
- Costs: "$1.8 million of incident response costs" (included in "other non-recurring items" in Adjusted EBITDA) and "$2.3 million of service level credits."

What the 10-Q does not say:
- How many customers or sites were affected: not found. It says only "some customers".
- Any third-party claim that data was stolen: not found.
- Any known or unpatched vulnerability: not found.
- An 8-K for the incident: none in the folder.
- The 10-Q risk factors say "no material changes", so the cybersecurity risk factor was not updated.

Interpretation:
- The wording "have not identified evidence" is a hedge. It is not a statement that no data was taken.
- The one customer lawsuit disclosed, Pinecrest, seeks US$12.0 million. That is 2.9 times the US$4.1 million of disclosed costs (1.8 + 2.3), yet the company calls the incident "not material."

**Effect on earlier findings (iteration 1):** I did not have access to the iteration 1 register in this run, so I describe the affected findings by topic. Please map them to their SEC IDs.
- Covenant finding: SEC-25 adds a recalculation. The company's 2.26x appears to use EBITDA with no cap on add-backs. Raise severity if the finding was Medium or lower.
- Vantor litigation finding: SEC-26 adds the timing gap (the 10-Q was filed 15 days after the adverse order) and the dropped loss-estimate language.
- Norvale concentration and bill-and-hold findings: SEC-27 and SEC-28 add the unchanged risk factor and the 38.2% return ratio.
- Cyber incident finding: SEC-30 adds the vague scale language and the hedged data-theft wording.

### Findings

#### SEC-25: The 2.26x leverage ratio appears to ignore the 15% add-back cap; capped ratios are 2.67x or 3.65x
- **Finding:** The reported 2.26x matches net debt divided by uncapped company Adjusted EBITDA. Applying the 10-K's 15% cap gives about 2.67x. That is close to the 3.00x limit that applies from September 30, 2026. If stock-based compensation counts as a Permitted Add-back, the ratio is 3.65x, a breach at June 30, 2026.
- **Evidence:** "Permitted Add-backs may not exceed 15% of Consolidated EBITDA calculated before including those Permitted Add-backs" (10-K). "Our Total Net Leverage Ratio was 2.26 to 1.00" (10-Q). The math:
  - **Net debt:** term loan 182.5 + revolver 45.0 = 227.5 (the revolver balance is in the 10-Q; the term loan is from financial data). Net of cash capped at 25.0 (cash was 33.9): 227.5 - 25.0 = 202.5.
  - **TTM Adjusted EBITDA from SEC data:** 98.8 - 39.0 + 29.9 = 89.7. Then 202.5 / 89.7 = 2.26x, an exact match to the reported ratio.
  - **Letters of credit:** if the 4.2 of letters of credit were counted as debt, the ratio would be 206.7 / 89.7 = 2.30x. So the reported figure appears to exclude them.
  - **Cap applied, stock-based compensation in the base:** base 48.2 + 17.8 = 66.0. Cap 15% x 66.0 = 9.9 (other add-backs are 41.5 - 17.8 = 23.7). Consolidated EBITDA = 75.9. Ratio 202.5 / 75.9 = 2.67x.
  - **Cap applied, stock-based compensation treated as a Permitted Add-back:** base 48.2, cap 7.2, Consolidated EBITDA 55.4. Ratio 202.5 / 55.4 = 3.65x, above 3.50x.
  - **September 30 headroom:** at 3.00x with flat net debt, a breach occurs if Consolidated EBITDA falls below 202.5 / 3.00 = 67.5. That is 8.4 below 75.9, or 11.1%. TTM Adjusted EBITDA already fell 9.1 in six months (98.8 to 89.7), and guidance was cut to 70.0 to 78.0.
  - **Data sources:** the 48.2, 41.5, 17.8 and 182.5 come from the financial data relayed by the lead, not from the SEC filings.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Note 9. Debt"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "Covenant compliance", "Liquidity and capital resources" and "Results summary"; 10-K "2025 highlights".
- **Severity:** High. Critical if the full credit agreement treats stock-based compensation as a Permitted Add-back, because that would mean an undisclosed breach.
- **Confidence:** Medium. The ratio reconciles exactly, but the definitions are a "summarized" version, the 10-Q gives no covenant calculation, and some inputs come from financial data.
- **Deal impact:** Closing risk and disclosure. A possible default or waiver need before closing, and possible misstated compliance (it adds to the securities class action risk). The debt must be repaid at closing in any case because of the change-of-control default.
- **Cross-check:** Obtain the full credit agreement and the June 30, 2026 compliance certificate. Ask whether lenders have granted waivers or amendments, and how the September 30, 2026 test came out. Ask the financial analyst to confirm that the 48.2 EBITDA matches the credit agreement's base definition.

#### SEC-26: The Q2 10-Q's Vantor disclosure is stale and leaves out the July 22 claim construction loss
- **Finding:** The 10-Q was filed August 6, 2026, 15 days after the court adopted Vantor's construction on three of four terms. It describes the case only as "in discovery," keeps the "without merit" stance, and leaves the patent risk factor unchanged. It also drops the 10-K's statement that the company "cannot reasonably estimate a possible loss or range of loss."
- **Evidence:**
  - 10-Q: "The case is in discovery. Trial is currently scheduled for March 2027. We continue to believe the claims are without merit".
  - 10-Q risk factors: "no material changes to the risk factors".
  - No filing mentions Gen-3 Plus.
  - Gen-3 made up about 70% of 2025 hardware revenue: 0.70 x 301.4 = 211.0, or 42.0% of total revenue.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "Part II, Item 1. Legal Proceedings" and "Part II, Item 1A. Risk Factors"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 1. Business" and "Item 3. Legal Proceedings".
- **Severity:** High.
- **Confidence:** High for what the filings say and leave out. Medium for the conclusion that this is a disclosure failure, since that depends on the court docket dates the litigation analyst reported.
- **Deal impact:** Valuation (injunction risk to about 42% of revenue, and a US$96.4 million damages claim with no accrual), disclosure (adds to securities claim risk), and closing (needs a specific indemnity or escrow, or a price adjustment).
- **Cross-check:** Litigation docket for the July 22 order and its entry date. Ask whether the Audit Committee or outside counsel reviewed the ASC 450 assessment after July 22. Check what the Q3 2026 10-Q (if filed by early November) says about the US$96.4 million damages report.

#### SEC-27: The 10-Q is silent on Norvale's move to build its own robots; customer risk factor unchanged
- **Finding:** The 10-Q does not mention Norvale's purchase of Kinetic Aisle (reported on or before June 24, 2026) and says there were no material changes to risk factors. The 10-K risk factor already says Norvale has no minimum purchase commitment and can terminate on 90 days' notice after a change of control.
- **Evidence:** 10-K: "Norvale is not required to purchase any minimum volume." 10-K: "terminate the agreement on 90 days' notice if Talonfield undergoes a change of control." 10-Q: "no material changes to the risk factors in our 2025 Form 10-K".
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1A. Risk Factors"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 1A. Risk Factors" and "Item 1. Business".
- **Severity:** High. Norvale was 31.1% of 2025 revenue, about 156.2 (0.311 x 502.3).
- **Confidence:** High that the 10-Q is silent. The acquisition itself is a news fact and not in the SEC filings.
- **Deal impact:** Valuation (revenue at risk), closing (needs a Norvale consent or commitment as a condition), and disclosure.
- **Cross-check:** News and Norvale's own statements on how it will use Kinetic Aisle. Talonfield's 2026 order and backlog data for Norvale. A management interview on whether Norvale has signaled lower volumes or a decision not to renew after September 30, 2027.

#### SEC-28: Bill-and-hold criteria do not require a customer request; 38.2% of Norvale's Q4 2025 bill-and-hold was later returned
- **Finding:** The 10-K's four criteria do not include a customer-request requirement, and no filing says customers requested the Q4 2025 holds. The largest customer (Norvale per the 10-K) later returned 9.4 of its 24.6. The 10-Q links Q2 weakness to orders "pulled forward" into Q4 2025, which fits poorly with the "site not ready" explanation.
- **Evidence:**
  - "(a) the reason for the arrangement is substantive" (10-K Note 2).
  - "orders that customers pulled forward into the fourth quarter of 2025" (10-Q).
  - 9.4 / 24.6 = 38.2% of Norvale's bill-and-hold revenue.
  - Q4 2025 revenue net of the reversal: 154.4 - 9.4 = 145.0.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Note 2. Revenue Recognition (excerpt)"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "Revenue" and "Bill-and-hold amendment".
- **Severity:** Medium on its own. It strengthens the iteration 1 bill-and-hold and revenue quality findings.
- **Confidence:** High on the quotes and math. Medium on naming Norvale, which is inferred from "largest customer" in both filings.
- **Deal impact:** Valuation (quality of 2025 base revenue) and post-closing (the restatement risk is tied to the unremediated material weakness).
- **Cross-check:** Customer written requests for the holds, warehouse records, and Linden Barr audit workpapers. Ask the financial analyst for the delivery dates of the remaining 22.4. Check news or the short report for claims about whether Norvale asked for the holds.

#### SEC-29: The filings never identify Vantor as a competitor
- **Finding:** No SEC filing describes Vantor Robotics as a rival, although news calls it one of Talonfield's two larger competitors. That raises the risk of an injunction, which the 10-K says Vantor seeks.
- **Evidence:** 10-K: "seeks damages and an injunction." No Competition section and no mention of Vantor outside Legal Proceedings: not found in SEC filings.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 1. Business" and "Item 3. Legal Proceedings".
- **Severity:** Medium.
- **Confidence:** Medium. The files are excerpts, and the full 10-K may contain a Competition section.
- **Deal impact:** Valuation and disclosure (how much weight to put on the injunction scenario).
- **Cross-check:** The full 10-K Item 1 Competition section, market reports, and Vantor's injunction filings.

#### SEC-30: The 10-Q gives no scale for the April 2026 incident and uses hedged language on data theft
- **Finding:** The 10-Q says "some customers" were affected without giving a number. It says the company has "not identified evidence" that data was taken, and calls the incident not material. No 8-K for the incident is in the folder, and the risk factors were not updated. The one disclosed customer suit (12.0) is 2.9 times the disclosed costs.
- **Evidence:**
  - "interrupted fleet operations for some customers for up to three days"
  - "we have not identified evidence that customer data was taken"
  - Disclosed costs: 1.8 + 2.3 = 4.1. Then 12.0 / 4.1 = 2.9x.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "April 2026 service disruption", "Part II, Item 1. Legal Proceedings" and "Part II, Item 1A. Risk Factors".
- **Severity:** Medium.
- **Confidence:** High on the wording. The scale itself is not disclosed.
- **Deal impact:** Post-closing (cyber remediation and further customer claims) and disclosure.
- **Cross-check:** News for the number of affected customers, any data-theft claims, and any known vulnerability. Court records for other customer suits. The forensic report from the outside cybersecurity firm.

### Positive or mitigating points
- The 10-Q fully discloses the US$9.4 million reversal, the US$2.3 million of credits, the cut in guidance, and the material weakness that is still unremediated. The revenue reversal was not buried.
- The 10-Q says the remaining 22.4 of bill-and-hold products were delivered by June 30, 2026.
- The 10-K discloses the change-of-control default and the Norvale termination right. These are known costs that can be priced: the debt is repaid at closing, and the Norvale right is a matter for a closing condition.
- The change-of-control default means Arbelion would refinance the debt at closing anyway. A covenant breach therefore matters mainly for the period before closing and for disclosure, not for the debt structure after closing.

### Gaps and questions for management
1. Provide the full credit agreement, the June 30, 2026 compliance certificate and the September 30, 2026 calculation. Is stock-based compensation a Permitted Add-back? Was the 15% cap applied? Are letters of credit in Total Debt? Are there any equity cure rights? Have any waivers been requested?
2. When did the company learn of the July 22, 2026 claim construction order? Why does the August 6 10-Q not mention it or Gen-3 Plus? Has the ASC 450 accrual assessment been updated for the US$96.4 million damages report?
3. Has Norvale signaled lower purchases, non-renewal, or an intent to rely on Kinetic Aisle? Was Norvale the customer behind the May 2026 amendment, and on what date was it signed?
4. Did each Q4 2025 bill-and-hold customer request the arrangement in writing, and what substantive reason was recorded under criterion (a)?
5. How many customers and sites were affected by the April 2026 incident? Is the forensic work finished? Has anyone, including the attacker, claimed to have customer data? How was the vulnerability that was exploited fixed?
6. Has any 8-K been filed after August 6, 2026 on the Vantor rulings, Norvale or the covenant? Not found in SEC filings.
