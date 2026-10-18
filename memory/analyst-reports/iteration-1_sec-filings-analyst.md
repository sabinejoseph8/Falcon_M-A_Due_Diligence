# Iteration 1: sec-filings-analyst report (unedited)

- Saved by the lead agent: 2026-10-18 02:31 EST
- Task: SEC filings analysis, iteration 1
- Subagent ID: ac1ee44f427043d52
- The report below is the subagent's final message exactly as returned. Only the harness's hand-back line and its two-space line indent were removed.

---

## SEC filings analyst: findings

### Files reviewed

I read all five SEC files in full and used the deal brief for context only. Source paths in the cards are relative to `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/`.

| File | Form | Date | Covers |
|---|---|---|---|
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md` | 8-K, Item 4.01 | Dated November 14, 2025 | Auditor dismissed November 10, 2025; new auditor engaged November 12, 2025 |
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md` | 8-K, Item 5.02 | Dated January 21, 2026 | CFO gave notice January 20, 2026 |
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-K_FY2025_excerpts.md` | 10-K (excerpts) | Filed March 9, 2026 | Fiscal year ended December 31, 2025 |
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_DEF14A_2026_excerpts.md` | DEF 14A (excerpts) | Filed April 24, 2026 | Annual meeting June 11, 2026 |
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` | 10-Q (excerpts) | Filed August 6, 2026 | Quarter ended June 30, 2026 |
| `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md` | Context only | October 17, 2026 | Deal terms and model basis |

Notes:
- The 10-K, 10-Q and proxy are labeled "EXCERPTS". When I say an item is missing, I mean it is missing from the excerpt. It may exist in the full filing.
- These are not in the file set: the Q3 2025 10-Q, the Q1 2026 10-Q, any earnings-release 8-K, any 8-K on the guidance cut or the April 2026 cyber incident, and the Q3 2026 10-Q.
- **Embedded instructions: none found.** I checked all five files and looked for hidden files in the folder. No text tried to direct the agents.

**Dated events stated in the filings** (for timing tests against court records and news):

| Date | Event | File |
|---|---|---|
| March 2024 | Vantor patent suit filed (D. Del.) | 10-K |
| August 2024 | Lumora acquired for US$85.0 million; term loan increased by US$70.0 million | 10-K |
| February 2025 | Ruiz wage-and-hour suit filed | 10-K |
| Q3 2025 | Hartwell & Pryce tells the Audit Committee about the material weakness and the need for extra Q4 procedures | 8-K Nov 2025, 10-K |
| October 1, 2025 | Annual goodwill test: no impairment | 10-K |
| November 10 / 12, 2025 | Hartwell & Pryce dismissed; Linden Barr engaged | 8-K Nov 2025 |
| Q4 2025 | US$31.8 million of bill-and-hold revenue recognized | 10-K |
| December 2025 | Ruiz settlement in principle (US$3.2 million) | 10-K |
| January 20, 2026 | CFO Okafor gives resignation notice | 8-K Jan 2026 |
| February 15, 2026 | Resignation takes effect; Simmons becomes interim CFO | 8-K Jan 2026 |
| March 9, 2026 | 10-K filed with 2026 outlook | 10-K |
| March 31, 2026 | Okafor's transition services end | 8-K Jan 2026 |
| April 11, 2026 | Unauthorized activity detected in FieldOS | 10-Q |
| May 2026 | Bill-and-hold amendment: US$9.4 million returned and credited | 10-Q |
| May 20, 2026 | Ruiz settlement gets preliminary approval | 10-Q |
| June 3, 2026 | Securities class action filed (S.D. Ohio) | 10-Q |
| June 17, 2026 | Pinecrest sues (Franklin County, Ohio) | 10-Q |
| June 30, 2026 | Leverage ratio 2.26x | 10-Q |
| August 6, 2026 | 10-Q filed; guidance cut | 10-Q |
| September 30, 2026 | Covenant maximum steps down to 3.00x | 10-K, 10-Q |
| March 2027 | Vantor trial | 10-Q |
| September 30, 2027 | Norvale MSA expires | 10-K |
| August 2029 | Term loan and revolver mature | 10-K |
| December 2033 | Headquarters lease ends | DEF 14A |

### Findings

#### SEC-01: 2026 guidance cut by 14.3% (revenue) and 37.3% (Adjusted EBITDA); the deal model still uses the withdrawn case
- **Finding:** On August 6, 2026 Talonfield replaced its March 9, 2026 outlook (revenue US$555.0 to 565.0 million, Adjusted EBITDA US$114.0 to 122.0 million). The new outlook is revenue of US$470.0 to 490.0 million and Adjusted EBITDA of US$70.0 to 78.0 million. Interpretation: the deal model's FY2026E (US$560.0 million and US$118.0 million) equals the midpoints of the withdrawn outlook. Model v3 is dated September 2026, after the company withdrew that outlook.
- **Evidence:**
  - 10-Q: "We now expect full-year 2026 revenue of $470 million to $490 million and Adjusted EBITDA of $70 million to $78 million." and "This replaces the outlook we provided on March 9, 2026."
  - Math, cut: revenue midpoint 480.0 vs 560.0 = -14.3%. Adjusted EBITDA midpoint 74.0 vs 118.0 = -37.3%.
  - Math, vs FY2025: revenue 480.0 / 502.3 = -4.4%. Adjusted EBITDA 74.0 / 98.8 = -25.1%.
  - Math, implied H2 2026: revenue 480.0 - 222.6 = 257.4, which is 15.6% above H1. Adjusted EBITDA 74.0 - 29.9 = 44.1, which is 47.5% above H1 (17.1% margin vs 13.4% in H1).
  - Context: Q2 2026 Adjusted EBITDA was 13.8 vs 20.6 (-33.0%). Gross margin was 37.6% vs 40.9%.
  - Multiple: EV of about 1,357.0 (11.5 x 118.0, per the deal brief) / 74.0 = 18.3x (17.4x to 19.4x across the range).
  - Illustrative arithmetic only: 11.5x on 74.0 gives an EV of about 851.0. Less about 197.8 of net debt implied by the brief, that is about US$13.50 per share.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2. Management's Discussion and Analysis (selected)" ("Updated 2026 outlook.", "Results summary ($ millions)"); `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Item 7. Management's Discussion and Analysis (selected)" ("2026 outlook (as of March 9, 2026)."); `data/deal-brief.md`, section "Valuation basis used in the current deal model"
- **Severity:** Critical. The EBITDA basis falls 37.3%, far above the 10% threshold.
- **Confidence:** High. Both outlooks are stated in primary filings and I recomputed the math. The per-share figure relies on the brief's approximate multiple.
- **Deal impact:** Valuation
- **Cross-check:** Financial data: rebuild the model on the revised guidance and on the H1 2026 run-rate, and get Q3 2026 actuals. News: the stock reaction around August 6, 2026, and whether management reaffirmed the March case after the May 2026 amendment (for example on a Q1 2026 call).

#### SEC-02: Q4 2025 bill-and-hold revenue (US$31.8 million) drove much of reported growth; 29.6% has since been reversed
- **Finding:** The 10-K says Talonfield recognized US$31.8 million of hardware revenue under bill-and-hold arrangements in Q4 2025 (none material in 2024). US$24.6 million of it came from its largest customer, which Item 1 names as Norvale, and the products were still in Talonfield's warehouses at year-end. The 10-Q says US$9.4 million was returned and credited in May 2026, and the other US$22.4 million was delivered by June 30, 2026. Interpretation: without bill-and-hold, FY2025 growth was about 11.6% (reported 19.1%), Q4 growth about 5.1% (reported 32.4%) and hardware growth about 2.9% (reported 15.1%).
- **Evidence:**
  - "In the fourth quarter of 2025 we recognized $31.8 million of hardware revenue under bill-and-hold arrangements (2024: none material)."
  - "At December 31, 2025, these products remained in our warehouses."
  - Share of revenue: 31.8 / 154.4 = 20.6% of Q4; 31.8 / 502.3 = 6.3% of FY2025; 31.8 / 301.4 = 10.6% of hardware.
  - By customer: largest customer 24.6 / 31.8 = 77.4%. Other customers 7.2, not named.
  - Growth: FY2025 without bill-and-hold is 470.5 / 421.7 = +11.6%, so bill-and-hold adds 7.5 points. Q4 2024 = 154.4 / 1.324 = 116.6, and Q4 2025 without bill-and-hold is 122.6, up 5.1%. Hardware without bill-and-hold is 269.6 / 261.9 = +2.9%.
  - Reversal: 9.4 / 31.8 = 29.6% (38.2% of the largest customer's 24.6). 31.8 - 9.4 = 22.4, which matches the 10-Q.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Note 2. Revenue Recognition (excerpt)" and "Item 1. Business" ("Customers."); `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2. Management's Discussion and Analysis (selected)" ("Bill-and-hold amendment.")
- **Severity:** Critical. It goes to IC question 1, part of it has already unwound, it sits under an unremediated material weakness over the same contracts (SEC-05), and it carries restatement risk (SEC-06).
- **Confidence:** High. The amounts are stated in the filings and I recomputed the math. Linking the US$24.6 million to Norvale relies on the 10-K naming Norvale as the largest customer. The 10-Q does not name the customer.
- **Deal impact:** Valuation (quality of the FY2025 base); disclosure
- **Cross-check:** Financial data: a bill-and-hold schedule by customer, the customers' written requests, delivery and cash collection dates for the 22.4, and Norvale's quarterly revenue in 2025 and 2026. Court records: whether the securities complaint cites bill-and-hold. News: Norvale site delays that would support a "substantive" reason.

#### SEC-03: Largest customer (31.1% of revenue) can terminate on 90 days' notice if Talonfield is acquired
- **Finding:** Per the 10-K, Norvale was 31.1% of 2025 revenue (28.0% in 2024) and 38% of gross receivables. It has no minimum purchase commitment, its MSA runs only to September 30, 2027, and it may terminate on 90 days' notice after a change of control. Interpretation: this deal itself triggers the termination right over about US$156.2 million of revenue. Norvale was also the counterparty to 77.4% of the Q4 bill-and-hold revenue and to the US$9.4 million return.
- **Evidence:**
  - "The Norvale MSA allows Norvale to terminate the agreement on 90 days' notice if Talonfield undergoes a change of control."
  - "Norvale is not required to purchase any minimum volume."
  - Revenue: 31.1% x 502.3 = 156.2, vs 28.0% x 421.7 = 118.1 in 2024 (+32.3%).
  - Without its 24.6 of bill-and-hold: about 131.6 (+11.4%), or 28.0% of non-bill-and-hold revenue (131.6 / 470.5), flat on 2024.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 1. Business" ("Customers."), "Item 1A. Risk Factors (selected)" and "Note 13. Concentrations"
- **Severity:** Critical. Losing Norvale would move value by well over 10%, and the transaction is the trigger.
- **Confidence:** High. The terms are stated in the 10-K. The dollar figures are approximate because the percentages are rounded.
- **Deal impact:** Closing risk and valuation (consent or waiver needed); post-closing (MSA renewal)
- **Cross-check:** News: Norvale's strategy, vendor diversification, capex cuts, or a competing robot supplier. Financial data: Norvale's 2026 revenue and orders. Court records: any Norvale dispute.

#### SEC-04: Auditor dismissed weeks after it flagged a material weakness and asked for extra procedures on expected Q4 2025 contracts
- **Finding:** The Audit Committee dismissed Hartwell & Pryce, auditor since 2016, on November 10, 2025 and engaged Linden Barr on November 12, 2025. As a "reportable event", Hartwell & Pryce had told the committee in Q3 2025 of a material weakness. It also said that arrangements with these terms "expected in the fourth quarter of 2025" would need extra procedures. Interpretation: the auditor that wanted to widen its audit of exactly these contracts was replaced 49 days before year-end. The 8-K does not say whether those procedures were ever performed, and it gives no reason for the dismissal.
- **Evidence:** "additional audit procedures would be required for revenue arrangements with these terms expected in the fourth quarter of 2025, which would expand the scope of its audit." The 8-K reports no disagreements. Hartwell & Pryce "agrees with the statements in this Item 4.01 (Exhibit 16.1)". Its FY2023 and FY2024 opinions were clean. Math: November 12 to December 31, 2025 = 49 days.
- **Source:** `data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md`, section "Item 4.01 Changes in Registrant's Certifying Accountant" ("(a) Dismissal...", "Reportable event.", "(b) Engagement...")
- **Severity:** High. It undermines confidence in FY2025 revenue and calls for a forensic accounting review and accounting-specific protections.
- **Confidence:** High for the facts. Reading this as possible "opinion shopping" is my inference only. The filing states there were no disagreements.
- **Deal impact:** Valuation and disclosure; closing risk if a restatement follows
- **Cross-check:** News: coverage of the auditor change. Court records: whether the securities complaint cites the dismissal. Financial data: audit fees, and Linden Barr's opinion on the FY2025 financial statements (not in the excerpt).

#### SEC-05: The material weakness over the same contracts was still unremediated at June 30, 2026
- **Finding:** The 10-K reports a material weakness over the review of hardware contracts with non-standard delivery and acceptance terms, including bill-and-hold. It was first identified in Q3 2025, and Linden Barr gave an adverse opinion on internal control. The 10-Q says the weakness has not been remediated and disclosure controls were not effective at June 30, 2026. The 10-Q excerpt gives no update on the remediation steps.
- **Evidence:**
  - 10-K: "We did not design and maintain effective controls over the review of hardware contracts with non-standard delivery and acceptance terms, including bill-and-hold arrangements."
  - 10-Q: "The material weakness described in our 2025 Form 10-K has not yet been remediated."
  - Remediation steps named in the 10-K: "hiring a director of technical accounting and creating a contract review committee."
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Item 9A. Controls and Procedures"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 4. Controls and Procedures"
- **Severity:** High. The US$9.4 million reversal happened while the weakness was open. The buyer would inherit remediation and a likely second adverse internal-control opinion for FY2026.
- **Confidence:** High. Stated directly in both filings.
- **Deal impact:** Post-closing; disclosure
- **Cross-check:** Financial data: whether the technical accounting hire happened, and contract review committee records. Court records: what the securities complaint alleges about controls.

#### SEC-06: The US$9.4 million return was booked as a Q2 2026 revenue reduction, not as a correction of FY2025
- **Finding:** The 10-Q recorded the May 2026 credit as a reduction of Q2 2026 revenue. Nothing in the files restates FY2025. Interpretation: one of the 10-K's four bill-and-hold criteria is that Talonfield cannot redirect the products, yet they went back into its inventory. If the customer had an explicit or implied right of return at December 31, 2025, this was a 2025 error rather than a 2026 contract change.
- **Evidence:**
  - 10-Q: "We recorded the credit as a reduction of revenue in the second quarter of 2026."
  - 10-K criterion: "(d) we cannot use the products or direct them to another customer."
  - Math: 9.4 / 112.9 = 8.3% of Q2 2026 revenue. Treated as a 2025 error, FY2025 revenue would be 492.9 (growth 16.9%, not 19.1%).
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2. Management's Discussion and Analysis (selected)" ("Bill-and-hold amendment.", "Revenue."); `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Note 2. Revenue Recognition (excerpt)"
- **Severity:** High. A restatement would feed the securities case, reopen 2025 bonuses (SEC-15) and affect covenant history.
- **Confidence:** High on how it was recorded. Medium on the restatement risk, which is an inference.
- **Deal impact:** Disclosure, valuation; closing risk if a restatement comes between signing and closing
- **Cross-check:** Financial data: the original purchase orders, any side letters, the May amendment, and the Audit Committee and Linden Barr conclusion on error vs modification. Court records: whether the June 3 complaint references the return.

#### SEC-07: The company described Q4 2025 three different ways
- **Finding:** The 10-K MD&A credits Q4 2025 to "strong hardware deliveries" and "strong fourth-quarter shipments". The same 10-K's Note 2 says US$31.8 million of Q4 hardware stayed in Talonfield's warehouses. The 10-Q later blames weak Q2 hardware partly on orders "pulled forward" into Q4 2025. Interpretation: the 10-K never mentioned pull-forward, and "deliveries" is hard to reconcile with Note 2. This bears directly on the class action's claim of misleading revenue statements.
- **Evidence:**
  - 10-K MD&A: "Record fourth-quarter revenue of $154.4 million, up 32.4% year over year, driven by strong hardware deliveries to enterprise customers."
  - 10-K Note 2: "At December 31, 2025, these products remained in our warehouses."
  - 10-Q: "orders that customers pulled forward into the fourth quarter of 2025"
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 7. Management's Discussion and Analysis (selected)" ("2025 highlights", "Liquidity.") and "Note 2. Revenue Recognition (excerpt)"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2. Management's Discussion and Analysis (selected)" ("Revenue.")
- **Severity:** High. This is disclosure liability the buyer would inherit. Pull-forward also means some 2026 demand was borrowed.
- **Confidence:** High. These are exact quotes. Calling them inconsistent is my interpretation.
- **Deal impact:** Disclosure; valuation
- **Cross-check:** Court records: which statements the complaint cites. News: wording on the Q4 2025 call and at the March 2026 investor day.

#### SEC-08: CFO left three weeks after year-end with a US$0.9 million payment; the role was still interim on August 6, 2026
- **Finding:** Daniel Okafor gave notice on January 20, 2026, effective February 15, 2026, which was before the March 9 10-K. He received US$900,000 in exchange for a general release of claims. Controller Rachel Simmons became interim CFO and still signed the August 6 10-Q as interim. Okafor is now a class action defendant. Interpretation: paying severance on a voluntary resignation is unusual. The timing, after the auditor dismissal and the bill-and-hold quarter, needs an explanation.
- **Evidence:**
  - 8-K: "Mr. Okafor's resignation was not the result of any disagreement with the Company on any matter relating to the Company's operations, policies or practices." It does not specifically mention accounting.
  - Payment: "a cash payment of $900,000 and a general release of claims". The proxy confirms US$0.9 million.
  - The 10-K's Note 18 omits the payment.
  - Math: February 15 to August 6, 2026 = 172 days with an interim CFO.
- **Source:** `data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md`, section "Item 5.02 Departure of Directors or Certain Officers; Appointment of Certain Officers"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Note 18. Subsequent Events"; `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, section "Potential payments upon a change in control"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, header ("Certifications signed by") and section "Part II, Item 1. Legal Proceedings"
- **Severity:** High. On its own this would be Medium. It is High because of the timing alongside SEC-02, SEC-04 and SEC-11, and because the interim CFO was Corporate Controller when appointed.
- **Confidence:** High for the facts. Medium for any link to the accounting issues, which is inference.
- **Deal impact:** Post-closing (finance leadership); disclosure
- **Cross-check:** News: any reported reason for Okafor's exit. Court records: the allegations against Okafor, and any whistleblower or employment claim.

#### SEC-09: Covenant maximum steps down to 3.00x from Q3 2026; revised guidance leaves thin headroom by year-end
- **Finding:** The Total Net Leverage maximum is 3.50x through June 30, 2026 and 3.00x from September 30, 2026, tested quarterly on a trailing twelve-month basis. Cash netting is capped at US$25.0 million, and Permitted Add-backs are capped at 15% of EBITDA before add-backs. Leverage was 2.26x at June 30, 2026. Interpretation: if covenant EBITDA tracks Adjusted EBITDA, the revised guidance implies about 2.63x to 2.93x at December 31, 2026 on flat net debt.
- **Evidence:**
  - Terms: "no more than 3.00 to 1.00 for each fiscal quarter ending on or after September 30, 2026" and "Permitted Add-backs may not exceed 15% of Consolidated EBITDA calculated before including those Permitted Add-backs."
  - Net debt at June 30, 2026: term loan (185.0 at December 31, 2025; the 10-Q excerpt does not give the June 30 balance) + revolver 45.0 - 25.0 cash cap = up to 205.0.
  - Implied covenant EBITDA: 205.0 / 2.26 = 90.7. That is close to trailing Adjusted EBITDA of 89.7 (98.8 - 39.0 + 29.9).
  - Headroom: the minimum EBITDA at 3.00x is 68.3, a 24.7% cushion at June 30 levels.
  - At FY2026 guidance: 205.0 / 70.0 = 2.93x; / 74.0 = 2.77x; / 78.0 = 2.63x. At the low end, the cushion is only about 1.7 of EBITDA.
  - Downside: if H2 only repeats H1 (29.9), FY2026 EBITDA is 59.8 and leverage is 3.43x, a breach.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Note 9. Debt" ("Financial covenant.", "Definitions (summarized from the credit agreement):"); `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2. Management's Discussion and Analysis (selected)" ("Covenant compliance.", "Liquidity and capital resources.")
- **Severity:** High. A breach between signing and closing would need a lender waiver and protection in the interim-period terms.
- **Confidence:** High on the terms and the 2.26x. Medium on the forward ratios, which assume covenant EBITDA equals Adjusted EBITDA and net debt stays flat. It is also unclear whether stock-based compensation counts toward the 15% cap.
- **Deal impact:** Closing risk (interim period); valuation
- **Cross-check:** Financial data: the Q3 2026 compliance certificate (the first 3.00x test; that quarter has ended), the Adjusted EBITDA reconciliation against the 15% cap, and the term loan balance. Timing: if the Q3 10-Q follows the Q2 lag of 37 days, it lands around November 6, 2026, the IC date.

#### SEC-10: Cash conversion collapsed in 2025 while receivables jumped 59.2% and the allowance fell
- **Finding:** 2025 operating cash flow was US$9.7 million, down from US$40.8 million in 2024. Gross receivables rose from US$76.3 million to US$121.5 million, yet the credit loss allowance fell from US$2.9 million to US$2.6 million, citing "improved collection experience". Interpretation: receivables far outgrew revenue, and Norvale's receivables rose by about the amount of its bill-and-hold revenue. Reserving less against a larger, more concentrated balance is aggressive.
- **Evidence:**
  - "mainly reflecting higher accounts receivable and contract assets following strong fourth-quarter shipments. We expect collections to normalize in 2026."
  - "The decrease in the allowance reflects improved collection experience with our enterprise customers."
  - Receivables: +59.2% vs revenue +19.1%. Days sales outstanding 86.4 vs 63.5 days. Allowance 2.1% of gross receivables vs 3.8%.
  - Cash conversion: operating cash flow / Adjusted EBITDA was 9.8% vs 54.5% (2024 Adjusted EBITDA = 98.8 / 1.321 = 74.8).
  - Bill-and-hold link: 31.8 = 70.4% of the 45.2 receivables increase. Norvale receivables rose about 24.0 (from about 22.1 to about 46.2), vs its 24.6 of bill-and-hold.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 7. Management's Discussion and Analysis (selected)" ("Liquidity."), "Note 5. Accounts Receivable" and "Note 13. Concentrations"
- **Severity:** High. It supports the revenue quality concern and affects the working capital peg.
- **Confidence:** High on the ratios. Medium on the Norvale link, because the percentages are rounded and the filing does not say whether the bill-and-hold invoices were unpaid.
- **Deal impact:** Valuation (quality of earnings, working capital)
- **Cross-check:** Financial data: receivables aging by customer, contract assets, cash collected on the Q4 bill-and-hold invoices, and receivables at June 30, 2026 (not in the 10-Q excerpt).

#### SEC-11: Securities class action alleges misleading statements on revenue and internal controls
- **Finding:** A putative securities class action was filed on June 3, 2026 in the Southern District of Ohio against Talonfield, its CEO and its former CFO. It alleges false or misleading statements about revenue and internal controls. The 10-Q adds a risk factor but gives no accrual, loss estimate, class period or insurance detail.
- **Evidence:** "alleging that we made false or misleading statements about our revenue and our internal controls. We intend to defend ourselves vigorously." It was filed after the May 2026 return and before the August 6 guidance cut. Interpretation: a later stock drop could extend the class period.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "Part II, Item 1. Legal Proceedings" ("Securities class action.") and "Part II, Item 1A. Risk Factors"
- **Severity:** High. It is an unquantified liability the buyer inherits, so it must be priced or insured.
- **Confidence:** High that the case exists (primary filing). The claims are unproven allegations.
- **Deal impact:** Valuation; post-closing (defense costs, indemnification of Hale and Okafor)
- **Cross-check:** Court records: the docket, class period, alleged corrective disclosures, and any motion to dismiss. News: stock drops before June 3, 2026. Financial data: D&O insurance limits and retention.

#### SEC-12: Vantor patent case threatens Talon Gen-3 (about 42% of 2025 revenue); no accrual
- **Finding:** Vantor (D. Del., filed March 2024) alleges that Gen-3 navigation infringes three patents and seeks damages and an injunction. Talonfield calls the claims meritless and has recorded no accrual. The 10-Q says the case is in discovery, with trial set for March 2027. The 10-Q excerpt does not repeat the 10-K's statement that a loss cannot be estimated.
- **Evidence:**
  - 10-K: "We have not recorded an accrual because we do not believe a loss is probable, and we cannot reasonably estimate a possible loss or range of loss."
  - 10-K risk factor: an adverse outcome could force it to "stop selling Talon Gen-3 robots".
  - Math: Gen-3 is about 70% x 301.4 = 211.0, or 42.0% of FY2025 revenue.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 1. Business", "Item 1A. Risk Factors (selected)" and "Item 3. Legal Proceedings"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1. Legal Proceedings"
- **Severity:** High. It could become Critical if the docket shows adverse rulings. Trial falls after a likely closing.
- **Confidence:** High. Stated in both filings, and I recomputed the Gen-3 share.
- **Deal impact:** Valuation; post-closing (special indemnity, escrow or price adjustment)
- **Cross-check:** Court records: any claim construction ruling, damages reports, or patent office challenges, and any docket events before August 6, 2026 that "in discovery" leaves out. The damages amount sought is not found in the SEC filings.

#### SEC-13: April 2026 FieldOS cyber incident judged "not material" despite credits, costs and a US$12.0 million suit
- **Finding:** On April 11, 2026 Talonfield detected unauthorized activity in FieldOS and took systems offline, stopping some customers' fleets for up to three days. It concluded the incident was not material and found no evidence that customer data was taken. It issued US$2.3 million of service credits and spent US$1.8 million on response costs, which it added back in Adjusted EBITDA. Interpretation: there is no cyber 8-K in the file set, and the 10-Q says risk factors are unchanged even though the 10-K's cyber risk factor was written as a hypothetical.
- **Evidence:** "Based on our investigation, we concluded that the incident was not material, and we have not identified evidence that customer data was taken." Math: credits 2.3 / 112.9 = 2.0% of Q2 revenue. Credits and costs (4.1) plus the Pinecrest claim (12.0) = 16.1. The Pinecrest claim alone is 87.0% of Q2 Adjusted EBITDA (12.0 / 13.8).
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "Part I, Item 2. Management's Discussion and Analysis (selected)" ("April 2026 service disruption.", "Revenue."), "Part II, Item 1. Legal Proceedings" and "Part II, Item 1A. Risk Factors"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Item 1A. Risk Factors (selected)"
- **Severity:** High. It calls for a forensic review and a cyber-specific representation. FieldOS is the recurring revenue line that supports the valuation.
- **Confidence:** High for the facts. Medium for the view that the materiality call is open to challenge.
- **Deal impact:** Valuation (FieldOS retention); post-closing; disclosure
- **Cross-check:** News: reports of data theft, ransomware claims, or customer churn. Court records: other customer or privacy suits. Financial data: FieldOS annual recurring revenue (ARR), retention and churn after April.

#### SEC-14: Pinecrest suit seeks US$12.0 million over the outage; no accrual stated
- **Finding:** On June 17, 2026 customer Pinecrest Distribution LLC sued in the Franklin County, Ohio Court of Common Pleas for breach of contract tied to the April disruption. Talonfield cites meritorious defenses. The excerpt says nothing about an accrual.
- **Evidence:** "seeking $12.0 million. We believe we have meritorious defenses." Math: 12.0 / 112.9 = 10.6% of Q2 2026 revenue.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1. Legal Proceedings" ("Pinecrest Distribution LLC.")
- **Severity:** Medium. Modest relative to deal value, but it tests the "not material" conclusion and may invite other claims.
- **Confidence:** High. Stated in the 10-Q.
- **Deal impact:** Post-closing
- **Cross-check:** Court records: the docket, contract liability caps, and any similar suits.

#### SEC-15: 2025 bonuses paid at 142% of target only cleared target because of bill-and-hold revenue
- **Finding:** 2025 bonuses were weighted 50/50 on revenue (target US$490.0 million) and Adjusted EBITDA (target US$95.0 million). Actuals were US$502.3 million and US$98.8 million, and all executive officers were paid at 142% of target. Interpretation: without bill-and-hold, revenue would have been just above threshold. Adjusted EBITDA would have fallen below threshold if the bill-and-hold sales carried a gross margin above 34.0%.
- **Evidence:**
  - "the Compensation Committee approved bonus payouts at 142% of target for all executive officers."
  - Revenue: 502.3 - 31.8 = 470.5 vs the 470.0 threshold. Removing only the reversed 9.4 gives 492.9, still just above target.
  - EBITDA: the cushion over threshold is 98.8 - 88.0 = 10.8, and 10.8 / 31.8 = 34.0%. For reference, blended gross margin was 40.8% in H1 2025. Hardware margin is not disclosed.
  - The excerpt shows no payout curve and no clawback policy.
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, section "2025 annual incentive plan"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Note 2. Revenue Recognition (excerpt)"
- **Severity:** Medium. Small in dollars, but it shows a pay incentive to pull revenue into 2025.
- **Confidence:** High on the plan figures. Medium on the EBITDA sensitivity.
- **Deal impact:** Disclosure; post-closing (clawback, pay design)
- **Cross-check:** Court records: whether the complaint pleads bonus motive. Financial data: the margin on the bill-and-hold units.

#### SEC-16: All executive equity vests on a change in control, whether or not the executive stays (US$17.6 million)
- **Finding:** Cash severance is double-trigger, but all unvested executive equity vests in full on a change in control. Estimated payments total US$28.6 million (cash 9.6, equity 17.6, other 1.4), including US$11.8 million for CEO Hale. Interpretation: the buyer loses its main retention tool at closing.
- **Evidence:** "all unvested equity awards held by executive officers vest in full immediately upon a change in control ("single-trigger"), whether or not the executive's employment ends." Math: the table totals reconcile. 28.6 / 1,159.2 = 2.5% of equity value. The values use an unstated December 31, 2025 share price.
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, section "Potential payments upon a change in control"
- **Severity:** Medium
- **Confidence:** High. Stated directly, and I recomputed the totals.
- **Deal impact:** Post-closing (retention)
- **Cross-check:** Financial data: confirm the 48.3 million diluted shares include all accelerated awards, and check for any excise tax gross-ups (not found in the SEC filings).

#### SEC-17: Related-party headquarters lease lets the Hale family landlord reset rent on a change in control
- **Finding:** The headquarters and main assembly facility are leased through December 2033 from Hale Family Properties LLC, which is controlled by Hale and his family. 2025 rent was US$2.1 million, rising 3% a year. A change in control lets the landlord reset rent to fair market value, using an appraiser the landlord chooses. Interpretation: the deal triggers an uncapped, landlord-controlled reset that benefits the CEO.
- **Evidence:** "a change in control of Talonfield allows the landlord to reset the rent to "fair market value", as determined by an appraiser selected by the landlord." Math: contractual rent for 2026 to 2033 totals about 19.2. The Audit Committee approved the lease when it was renewed in 2023.
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, section "Certain relationships and related party transactions"
- **Severity:** Medium. The dollars are probably modest, but it is a governance conflict and a waiver should be obtained at signing.
- **Confidence:** High. Stated directly.
- **Deal impact:** Post-closing; deal terms
- **Cross-check:** Financial data: the lease and market rent comparables.

#### SEC-18: Change of control is an event of default; about US$230.0 million must be repaid at closing
- **Finding:** Under the credit agreement, a change of control lets lenders demand immediate repayment. Debt at December 31, 2025 was US$220.0 million: a term loan of US$185.0 million and a revolver of US$35.0 million, both maturing in August 2029 at SOFR plus 3.25% to 3.75%. The revolver was US$45.0 million at June 30, 2026, with US$4.2 million of letters of credit.
- **Evidence:** "A change of control of Talonfield is an event of default, which allows the lenders to demand immediate repayment of all outstanding loans." Math: about 185.0 + 45.0 = 230.0, plus 4.2 of letters of credit. The June 30 term loan balance is not in the excerpt.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Note 9. Debt"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2. Management's Discussion and Analysis (selected)" ("Liquidity and capital resources.")
- **Severity:** Medium. This is standard, but Arbelion's financing must cover the payoff.
- **Confidence:** High
- **Deal impact:** Closing (payoff letter, financing size)
- **Cross-check:** Financial data: the payoff amount and any hedge breakage costs.

#### SEC-19: Liquidity tightened in H1 2026
- **Finding:** Cash fell from US$41.6 million to US$33.9 million. H1 operating cash flow was negative US$4.2 million, the company drew another US$10.0 million on the revolver, and availability was US$25.8 million. Interpretation: the 10-K's expectation that collections would normalize in 2026 was not met in H1.
- **Evidence:**
  - "Operating cash flow for the first half of 2026 was negative $4.2 million."
  - Math: availability 75.0 - 45.0 - 4.2 = 25.8, which matches. Liquidity is 33.9 + 25.8 = 59.7.
  - The revolver rose from 10.0 at December 31, 2024 to 45.0 at June 30, 2026.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2. Management's Discussion and Analysis (selected)" ("Liquidity and capital resources."); `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 7. Management's Discussion and Analysis (selected)" ("Liquidity.") and "Note 9. Debt"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Closing risk (interim period); net debt at closing
- **Cross-check:** Financial data: a 13-week cash forecast and the Q3 2026 cash and revolver balances.

#### SEC-20: All Talon robots depend on one LiDAR supplier in China with no second source
- **Finding:** Every Talon model uses LiDAR sensors from one supplier that manufactures in China, and there is no qualified second source. The 10-K flags tariff risk. Interpretation: the 10-Q excerpt does not explain the Q2 gross margin drop, and tariffs are one possible cause to test.
- **Evidence:** "We do not currently have a qualified second source." Q2 gross margin was 37.6% vs 40.9% (down 3.3 points). H1 was 38.0% vs 40.8%.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 1. Business" ("Suppliers.") and "Item 1A. Risk Factors (selected)"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2. Management's Discussion and Analysis (selected)" ("Results summary ($ millions)")
- **Severity:** Medium. It could rise if news shows new tariffs.
- **Confidence:** High for the dependency. The margin link is a hypothesis only.
- **Deal impact:** Post-closing (supply, margins)
- **Cross-check:** News: 2026 tariffs or export controls on LiDAR. Financial data: a gross margin bridge.

#### SEC-21: What changed from the 10-K to the 10-Q, and what management stopped saying
- **Finding:** The 10-Q says risk factors are unchanged apart from a new securities-litigation risk. By then a cyber incident, a guidance cut, a customer product return and an upcoming covenant step-down had all happened. Several 10-K metrics and statements do not reappear in the 10-Q excerpt.
- **Evidence:**
  - "There have been no material changes to the risk factors in our 2025 Form 10-K, except for the following addition".
  - Added in the 10-Q: the bill-and-hold return, "pulled forward" orders, the cyber incident, the class action, Pinecrest, the Vantor trial date, the Ruiz approval, the 2.26x ratio, and the new outlook.
  - Not repeated: FieldOS ARR (US$139.2 million) and net revenue retention (118%); "collections to normalize"; the remediation steps; the Vantor loss-estimate sentence; Norvale's name ("our largest customer" instead).
  - Reworded: Q4 2025 "deliveries" became "pulled forward".
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "Part II, Item 1A. Risk Factors", "Part I, Item 2. Management's Discussion and Analysis (selected)", "Part I, Item 4. Controls and Procedures" and "Part II, Item 1. Legal Proceedings"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 1A. Risk Factors (selected)", "Item 7. Management's Discussion and Analysis (selected)" and "Item 3. Legal Proceedings"
- **Severity:** Medium
- **Confidence:** Medium. This compares excerpts, so the full 10-Q may contain more.
- **Deal impact:** Disclosure; valuation (FieldOS metrics needed)
- **Cross-check:** Financial data: ARR, retention and churn at June 30, 2026. News: commentary on the Q2 2026 call.

#### SEC-22: Goodwill last tested before the guidance cut; Lumora's effect on growth not disclosed
- **Finding:** Goodwill is US$98.4 million, of which US$57.4 million comes from Lumora (bought in August 2024 for US$85.0 million). It was last tested on October 1, 2025, and the 10-Q excerpt mentions no 2026 test. Interpretation: 2025 includes a full year of Lumora but 2024 includes only part of a year, so the 27.1% software growth may be partly acquired. The 10-K excerpt does not separate organic from acquired growth.
- **Evidence:** "We performed our annual impairment test as of October 1, 2025 and found no impairment." H1 2026 net loss was 8.9.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Note 15. Goodwill", "Item 1. Business" and "Item 7. Management's Discussion and Analysis (selected)"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part I, Item 2. Management's Discussion and Analysis (selected)"
- **Severity:** Medium
- **Confidence:** High on the facts. Medium on the acquired-growth point.
- **Deal impact:** Valuation (organic growth)
- **Cross-check:** Financial data: Lumora's revenue in 2024 and 2025, and any 2026 impairment test triggered by events.

#### SEC-23: Founder is both Chairman and CEO, with no lead independent director
- **Finding:** Hale holds 6,690,000 shares (14.2%), and directors and officers together hold 17.6%. Five of the seven directors are independent. Interpretation: Hale's interests go beyond his shares (US$11.8 million of change-in-control payments and the lease reset), so a strong independent process matters.
- **Evidence:** "Mr. Hale serves as both Chairman and Chief Executive Officer. The Board has not appointed a lead independent director."
- **Source:** `data/sec-filings/TLFS_DEF14A_2026_excerpts.md`, sections "Security ownership" and "Board of Directors"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Closing (vote, voting agreement)
- **Cross-check:** News: activist positions.

#### SEC-24: Ruiz wage-and-hour class action settled for US$3.2 million and accrued
- **Finding:** The Ruiz case was settled in principle in December 2025 for US$3.2 million, which was accrued at year-end. The court granted preliminary approval on May 20, 2026.
- **Evidence:** "On May 20, 2026, the court granted preliminary approval of the $3.2 million settlement."
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Item 3. Legal Proceedings"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1. Legal Proceedings"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Post-closing (cash payment)
- **Cross-check:** Court records: final approval and any objections.

### Positive or mitigating points

- Hartwell & Pryce's FY2023 and FY2024 opinions were clean. It reported no disagreements and agreed with the 8-K.
- The company disclosed the bill-and-hold amount, the largest customer's share and the reversal. US$22.4 million (70.4%) of those products was delivered by June 30, 2026.
- Leverage was 2.26x against a 3.50x maximum at June 30, 2026. The debt does not mature until August 2029.
- Cash severance is double-trigger. Okafor is not eligible for change-in-control payments, and the 8-K and proxy agree on the US$0.9 million.
- FieldOS was strong in 2025, before the outage: software revenue up 27.1%, ARR up 27% to US$139.2 million, and net revenue retention of 118%.
- Without the US$9.4 million credit and the US$2.3 million of service credits, Q2 2026 revenue would have been US$124.6 million, up 6.0% (illustrative).
- Norvale's share of non-bill-and-hold revenue looks stable at about 28.0%, and its MSA runs to September 30, 2027.
- Ruiz is settled, accrued and preliminarily approved. The company engaged outside cyber experts and notified law enforcement.

### Gaps and questions for management

**Not found in the SEC filings:** the Q3 2025 and Q1 2026 10-Qs; any 8-K for earnings, the guidance cut or the cyber incident; the Q3 2026 10-Q; Linden Barr's opinion on the FY2025 financial statements; the Adjusted EBITDA reconciliation; the term loan balance at June 30, 2026; the full credit agreement; Lumora's revenue; damages sought in Vantor and the class action; the clawback policy.

1. **Bill-and-hold:** For each Q4 2025 arrangement, provide the customer, amount, written request date, the substantive reason, and delivery and collection dates. Who were the customers behind the US$7.2 million?
2. **The May 2026 return:** Why did the largest customer return US$9.4 million of product? Did it have any right of return or side letter? Why was the credit booked in Q2 2026 rather than as a correction of FY2025, and who signed off?
3. **Auditor change:** Why was Hartwell & Pryce dismissed? Were its extra Q4 procedures ever performed? Provide the Exhibit 16.1 letter and the Audit Committee minutes.
4. **Remediation:** Was the director of technical accounting hired? When is remediation expected?
5. **CFO departure:** Why did Okafor resign, and was the US$900,000 contractually required? Did he raise any accounting concerns? Where does the permanent CFO search stand?
6. **Covenant:** What was the Q3 2026 ratio? Provide the reconciliation of Permitted Add-backs against the 15% cap, the Q4 2026 forecast, and any lender talks.
7. **Norvale:** What is the 2026 revenue trend? Will Norvale waive its change-of-control right before signing? What are the renewal plans for 2027?
8. **Litigation:** For the class action, what are the class period and D&O insurance? For Vantor, what is the claim construction status? For Pinecrest, are there contract liability caps?
9. **Cyber:** Provide the forensic report and materiality analysis, details of cyber insurance, and churn since April.
10. **Outlook:** What drove the August 6 guidance cut? Why does management expect H2 Adjusted EBITDA of US$44.1 million vs US$29.9 million in H1? Provide ARR and net revenue retention at June 30 and September 30, 2026.
11. **Compensation:** Will 2025 bonuses be reviewed? Did Okafor receive a 2025 bonus? What are the single-trigger award values at US$24.00?
12. **Hale's conflicts:** Will the landlord waive the rent reset? Will Hale sign a voting agreement?

**For the lead:** the deal brief's FY2026E basis is stale (SEC-01) and should be updated before the IC on November 6, 2026.
