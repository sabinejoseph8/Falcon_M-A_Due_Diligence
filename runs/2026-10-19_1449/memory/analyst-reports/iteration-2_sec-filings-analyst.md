## SEC filings analyst: findings (iteration 2, Project Kestrel)

### Files reviewed

I read all six files in full:
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/deal-brief.md` (for context)
- `.../targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md` (filed March 5, 2026)
- `.../targets/kestrel/data/sec-filings/CRVD_DEF14A_2026_excerpts.md` (filed April 10, 2026)
- `.../targets/kestrel/data/sec-filings/CRVD_8-K_2026-04-27_network-disruption.md` (filed April 27, 2026)
- `.../targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md` (filed August 5, 2026)
- `.../targets/kestrel/data/sec-filings/CRVD_8-K_2026-08-05_q2-results-guidance.md` (filed August 5, 2026)

The latest filing in the folder is dated August 5, 2026. There is no filing in the folder from after the August 12 Markman ruling, the August 18 intervention, the August 21 unsealing or the August 27 ATLAS-3 halt. None of the files contains text that tries to give instructions.

### Findings

#### SEC-21: The 10-K does not mention the IPR denial and calls the Genaro claims "without merit". The 10-Q repeats this, and no filing covers the Markman loss
- **Finding:** The 10-K was filed March 5, 2026, 80 days after the December 15, 2025 PTAB denial (from LIT-002). It does not mention the IPR petition or its denial. The 10-Q says only that claim construction briefing was done. No filing in the folder mentions the August 12, 2026 Markman ruling, the US$68.0m damages claim or the February 8, 2027 trial date. That is expected for the Markman ruling, because it came after the August 5 10-Q.
- **Evidence:**
  - 10-K Item 3: "We believe the claims are without merit and intend to defend vigorously. We have not recorded an accrual because we do not believe a loss is probable and cannot estimate a range of loss." The 10-K also says Genaro "seeks damages and an injunction."
  - 10-Q Part II Item 1: "Claim construction briefing was completed in the second quarter. We continue to believe Genaro's claims are without merit. No accrual has been recorded."
  - 10-K Note 15: "identified none requiring disclosure."
  - IPR, PTAB, inter partes review, Markman, US$68.0m and the trial date: not found in SEC filings.
- **Math:** OncoTrace is the accused product. It is 44% x 314.8 = US$138.5m, or 138.5 / 431.0 = 32.1% of FY2025 revenue. The US$68.0m damages claim / US$1,648.6m EV = 4.1% of EV, before any injunction effect.
- **Source:** 10-K, "Item 3. Legal Proceedings" and "Note 15. Subsequent events"; 10-Q, "Part II, Item 1. Legal Proceedings"
- **Severity:** High. Losing the IPR and the Markman ruling makes "without merit" and "loss not probable" hard to support. An injunction against a product that is 32.1% of revenue could exceed 10% of value, but the filings alone do not show how likely that is.
- **Confidence:** High that the filings are silent and for the quoted wording. Whether the omission was improper is my interpretation.
- **Deal impact:** Valuation, disclosure, post-closing (specific indemnity or escrow; possible need to design around the patent).
- **Cross-check:** Litigation: the PTAB decision date, the Markman order, the expert report date and whether any injunction motion is pending. Financial: is there any accrual or legal reserve in the trial balance?

#### SEC-22: The 10-K said no material government investigation was pending three weeks after the DOJ CID. The CID first appears in the 10-Q of August 5, 2026. No filing names Whitcomb
- **Finding:** The CID was received February 11, 2026, 22 days before the 10-K was filed on March 5. The 10-K only discloses ordinary-course inquiries and denies any material pending investigation. The CID is first disclosed in the Q2 10-Q, filed August 5, 2026, 175 days after receipt. The Q1 10-Q is not in the folder, so I cannot tell whether it disclosed the CID earlier.
- **Evidence:**
  - 10-K Item 3: "We are not aware of any pending government investigation that we expect to be material to our business."
  - 10-Q: "On February 11, 2026, we received a civil investigative demand (CID) from the U.S. Department of Justice requesting documents about our billing of genetic tests to Medicare, including OncoTrace, and our physician speaker program, for the period from January 2019." It adds: "We cannot predict its outcome or estimate a range of possible loss, and we have not recorded an accrual."
  - The 10-K mentions qui tam suits only as a general risk: "Private individuals may bring 'qui tam' suits under seal on behalf of the government."
  - Whitcomb, the relator, the seal, the August 18 intervention and the unsealing: not found in SEC filings. There is no 8-K after August 5 in the folder.
- **Source:** 10-K, "Item 3. Legal Proceedings" and "Item 1A. Risk Factors (selected)"; 10-Q, "Part II, Item 1. Legal Proceedings"
- **Severity:** High. FCA exposure brings treble damages, per-claim penalties and possible exclusion (10-K risk factor). The look-back runs from January 2019. The filings give no amount, so I cannot show the more-than-10% test, but the lead may be able to with litigation data.
- **Confidence:** High for the quotes and dates.
- **Deal impact:** Closing risk, valuation, disclosure (possible securities claim over the 10-K statement), special indemnity or escrow.
- **Cross-check:** Litigation: the scope of the intervention and the damages the government alleges. Does any 8-K or the Q3 10-Q (if filed) disclose the intervention? Was a Q1 2026 10-Q filed and what did it say?

#### SEC-23: The 10-K describes a compliance program run by a CCO who had already left, and calls the speaker program compliant after the CID targeted it
- **Finding:** The 10-K, filed March 5, 2026, describes the CCO as overseeing the program. The proxy and the 10-Q say the CCO left in January 2026. The 10-K also says the speaker program complies with the Anti-Kickback Statute, although the February 11 CID asks for speaker program documents.
- **Evidence:**
  - 10-K: "We maintain a compliance program overseen by our Chief Compliance Officer, who reports to the Audit Committee." Also: "a physician speaker program, which we believe complies with the federal Anti-Kickback Statute."
  - DEF 14A: "Our Chief Compliance Officer, Daniel Pruitt, left Corvane in January 2026."
  - 10-Q Item 1A: the CCO "left the company in January 2026"; the Deputy General Counsel is interim CCO.
  - The reason for the departure, any severance and any speaker program spend: not found in SEC filings.
- **Source:** 10-K, "Compliance program"; DEF 14A, "Executive officers"; 10-Q, "Part II, Item 1A"
- **Severity:** Medium. On its own it is a disclosure and governance follow-up; it adds weight to SEC-22.
- **Confidence:** High.
- **Deal impact:** Disclosure, post-closing (rebuild compliance).
- **Cross-check:** News and litigation: is Pruitt the relator, or a witness in Whitcomb? Is a separation agreement on file? Financial: speaker program spend by year since 2019.

#### SEC-24: The filings set out the Medicare-linked pricing but do not state the new 0419U rate. With the news rate, the exposure is US$16.6m to US$35.4m
- **Finding:** The 40% linkage figure is in the 10-K, not the 10-Q. The 10-Q discusses the final 2027 0419U rate but gives neither the amount nor the direction of the change, and it does not repeat the 40% figure. The updated guidance leaves the rate change out.
- **Evidence:**
  - 10-K Item 1: "Approximately 40% of our non-Medicare revenue for OncoTrace is earned under commercial contracts that set the price as a percentage of the Medicare clinical laboratory fee schedule rate for code 0419U."
  - 10-K risk factor: "A reduction in the Medicare rate for OncoTrace would also reduce the price under commercial contracts that reference the Medicare rate."
  - 10-Q: "CMS published final 2027 rates ... including a new rate for code 0419U (OncoTrace)... We do not expect it to affect our 2026 results. We are evaluating the effect on future periods and may seek reconsideration."
  - 8-K of August 5: the outlook "does not include any effect of the final 2027 Medicare rate for code 0419U."
  - US$2,150, US$1,505 and the -30% figure: not found in SEC filings.
- **Math (inference, using the -30% from news on the FY2025 base):**
  - OncoTrace revenue is US$138.5m. Total Medicare revenue is 24.2% x 431.0 = US$104.3m. The filings do not give OncoTrace's Medicare share.
  - Lower bound, assuming no OncoTrace revenue is Medicare: 0.30 x 0.40 x 138.5 = US$16.6m.
  - Upper bound, assuming all US$104.3m of Medicare revenue is OncoTrace: 0.30 x (104.3 + 0.40 x 34.2) = 0.30 x 118.0 = US$35.4m.
  - A price cut largely flows straight to EBITDA. US$16.6m to US$35.4m is 16.1% to 34.4% of the US$103.0m FY2026 Adjusted EBITDA guidance midpoint.
- **Source:** 10-K, "Payer contracts" and "Item 1A"; 10-Q, "Reimbursement"; 8-K 2026-08-05, "Item 7.01"
- **Severity:** Critical. Test: changes value by more than 10%. Even the lower bound, US$16.6m, is more than 10% of guided FY2026 Adjusted EBITDA, and the deal brief assumes "Medicare reimbursement rates flat through 2030."
- **Confidence:** Medium. The linkage is primary. The rate cut comes from news, and the Medicare share of OncoTrace is not disclosed.
- **Deal impact:** Valuation (the model assumption no longer holds), disclosure.
- **Cross-check:** Financial: OncoTrace revenue split by Medicare and commercial, and the contract list with Medicare-linked pricing. Also check whether the Orvia contract is Medicare-linked.

#### SEC-25: The cyber 8-K was filed under Item 8.01, said there was no evidence of exfiltration and no material impact, and was never amended
- **Finding:** Corvane reported the incident under Item 8.01 (Other Events), not Item 1.05 (Material Cybersecurity Incidents). It called it a "network disruption". The 10-Q later calls it "a ransomware attack". The 8-K was filed April 27, 6 days after the attacker's claim on April 21 (news) and 3 days after the alleged preliminary forensic finding on April 24 (LIT-003, an allegation).
- **Evidence:**
  - 8-K: "Item 8.01. Other Events"; "Corvane has no evidence at this time that patient information was exfiltrated."; "Corvane does not currently believe the disruption will have a material impact on its financial condition or results of operations."
  - 10-Q: "we detected a ransomware attack"; "approximately 412,300 individuals" were notified in June 2026; US$6.1m of response costs; about US$4.0m of lost revenue; insurance limit of US$10.0m; class actions filed and an HHS OCR inquiry opened; "We cannot estimate a range of possible loss."
  - An amended 8-K (8-K/A) or an Item 1.05 filing: not found in SEC filings.
- **Math:** 6.1 + 4.0 = US$10.1m of direct cost and lost revenue in H1, which already exceeds the US$10.0m policy limit before any litigation or OCR outcome.
- **Source:** 8-K 2026-04-27, "Item 8.01"; 10-Q, "Cybersecurity incident"
- **Severity:** High. Disclosure accuracy, uninsured exposure and an open regulatory inquiry.
- **Confidence:** High for the filing content. The April 24 forensic finding is an allegation (Low until confirmed).
- **Deal impact:** Disclosure (possible SEC or securities claims), post-closing, indemnity.
- **Cross-check:** Litigation: the forensic report date in the class complaints. News: the ransom note and leak-site timing. Financial: insurance recoveries received.

#### SEC-26: Revolver confirmed at US$100.0m with US$65.0m available at June 30, 2026, subject to the September 30 step-down
- **Finding:** The commitment and drawn figures reconcile, and total debt matches the US$424.7m repayment figure in the deal brief.
- **Evidence:**
  - 10-K: "US$30.0 million drawn on our US$100.0 million revolving credit facility" at December 31, 2025; the revolver matures October 2028.
  - 10-Q: "US$35.0 million drawn on our revolving credit facility, leaving US$65.0 million of revolving capacity" at June 30, 2026; "steps down from 4.50x to 4.00x at the September 30, 2026 test date."
  - 10-K: after an event of default the lenders "may stop further revolving loans." It also says "A change of control of Corvane is also an event of default."
- **Math:**
  - 100.0 - 35.0 = 65.0. Liquidity is 28.8 cash + 65.0 = US$93.8m.
  - Net debt is 389.7 + 35.0 - 28.8 = US$395.9m. Total debt is 389.7 + 35.0 = 424.7, matching the deal brief.
  - At 4.00x, Consolidated EBITDA must be at least 395.9 / 4.00 = US$99.0m, using June debt (inference).
  - The Q3 certificate is due 45 days after September 30, which is November 14, 2026.
  - Consolidated EBITDA itself: not found in SEC filings. Letters of credit: not found.
- **Source:** 10-K, "Liquidity and capital resources" and "Financial covenant"; 10-Q, "Liquidity and capital resources"
- **Severity:** High. Failing the September 30 test would be a default before signing, which would make this Critical. The filings do not let me test that. Change of control is cured by refinancing at closing.
- **Confidence:** High for the figures. Medium for the covenant inference.
- **Deal impact:** Closing risk, liquidity before closing.
- **Cross-check:** Financial: the Q3 2026 compliance certificate and a Consolidated EBITDA build with the 15% cap applied.

#### SEC-27: The goodwill test date was October 1, 2025, with 14% headroom. The US$27.80 share price is stated in the 10-K, and the 10-Q is silent on impairment triggers
- **Finding:** The 10-K itself states the test-date share price (not an outside source). Both key assumptions have since failed, and the 10-Q does not discuss an interim impairment test.
- **Evidence:**
  - 10-K: "We test goodwill for impairment annually on October 1." The Clinical testing unit's fair value "exceeded its carrying value by approximately 14%." "Our share price was US$27.80 at the test date." The test assumed "stable Medicare reimbursement for OncoTrace and revenue growth of 9% a year." "A 10% reduction in projected cash flows of the Clinical testing unit would eliminate most of the headroom." The Pell Ridge goodwill of US$22.3m "was not tested."
  - Goodwill, impairment and triggering events in the 10-Q: not found in SEC filings.
- **Math:**
  - The US$18.10 price on July 31, 2026 (from the deal brief, not a filing) is (18.10 - 27.80) / 27.80 = -34.9% from the test date. The US$24.00 offer is -13.7%.
  - Adjusted EBITDA guidance midpoint: 137.0 to 103.0, down 24.8%.
  - Revenue guidance midpoint: 460.0 to 410.0, down 10.9%.
  - H1 Clinical testing revenue fell 1.9%, against the 9% growth assumed.
  - Clinical testing goodwill at risk is US$241.5m, plus part of the untested US$22.3m.
- **Source:** 10-K, "Critical accounting estimates: goodwill"; 10-Q (silent); 8-K 2026-08-05, "Item 7.01"
- **Severity:** High. An impairment is non-cash, but it signals that the 10-K judgment is stale and could weigh on covenant optics and disclosure.
- **Confidence:** High for the filing facts. The impairment conclusion is my inference.
- **Deal impact:** Disclosure, valuation signal.
- **Cross-check:** Financial and market data: the share price path and whether any interim test was run in Q2 or Q3 2026.

#### SEC-28: The filings do not name the payers that added prior authorization (Orvia is not named) or disclose speaker program spend
- **Finding:** The 10-Q gives only the count of payers and the effect on denials.
- **Evidence:**
  - 10-Q: "two commercial payers introduced prior authorization for hereditary cancer panels." The initial denial rate was "16.2% in the first half of 2026 (FY2025: 13.4%)."
  - The payer names, and whether Orvia is one of them: not found in SEC filings.
  - Speaker program spend: not found in SEC filings.
  - Orvia context (10-K): 11.3% of FY2025 revenue (US$48.7m), contract to December 31, 2028, terminable "on 60 days' notice if Corvane undergoes a change of control."
- **Math:** The denial rate rose 2.8 points, or 20.9% relative.
- **Source:** 10-Q, "Results for the six months ended June 30, 2026"; 10-K, "Payer contracts" and "Compliance program"
- **Severity:** Medium
- **Confidence:** High that the filings are silent.
- **Deal impact:** Valuation (collections), closing (an Orvia consent).
- **Cross-check:** News and financial data: which payers added prior authorization, Orvia's denial trend, and speaker spend by year.

#### SEC-29: No filing discloses the ATLAS-3 halt or any Veltrane termination notice. The 10-Q still counts US$61.0m of VLT-220 backlog
- **Finding:** The halt on August 27 came after the August 5 filings, and the folder has no later 8-K.
- **Evidence:**
  - 10-Q: "Backlog includes US$61.0 million related to Veltrane Therapeutics' VLT-220 program. Book-to-bill was 0.7."
  - 10-K: Veltrane may "terminate any work order for convenience on 90 days' notice, paying only for work performed."
  - The trial halt, any termination notice and any backlog write-down: not found in SEC filings.
- **Math:**
  - VLT-220 backlog is 61.0 / 231.4 = 26.4% of June 30 backlog.
  - Veltrane revenue in FY2025 was 11.7% x 431.0 = US$50.4m.
  - Backlog without VLT-220 would be 231.4 - 61.0 = US$170.4m, down 30.7% from US$246.0m.
- **Source:** 10-Q, "Biopharma services"; 10-K, "Biopharma services"
- **Severity:** High. It undercuts thesis point 3 and the deal brief's backlog assumption.
- **Confidence:** High for the filings. The halt comes from news only.
- **Deal impact:** Valuation, disclosure (watch for an 8-K or the Q3 10-Q).
- **Cross-check:** News and financial data: termination notices received, and work orders cancelled in Q3.

#### SEC-30: The filings give no full Adjusted EBITDA definition. "Non-recurring" appears only in the credit agreement's Consolidated EBITDA. Without the one-off, LTM Adjusted EBITDA is below the US$110.0m financing condition
- **Finding:** The 10-K points to a reconciliation "in our financial data" that is not in the filings. The add-backs I could identify are stock-based compensation (credit definition only), the cyber response costs and, by exclusion, the sale-leaseback gain. The US$14.2m Q4 2025 change in estimate stays inside Adjusted EBITDA.
- **Evidence:**
  - 10-K: "Adjusted EBITDA (a non-GAAP measure) was US$125.3 million, up 25.4%. See the reconciliation in our financial data."
  - The credit agreement adds back "restructuring charges and other non-recurring or unusual cash costs," capped at 15%, and says "Consolidated EBITDA is therefore not the same as our Adjusted EBITDA."
  - 10-Q: US$6.1m of incident costs, "which we exclude from Adjusted EBITDA."
  - Note 7: the US$6.8m gain "is excluded from EBITDA and Adjusted EBITDA."
  - A company description of the Adjusted EBITDA add-backs as "non-recurring": not found in SEC filings.
- **Math:**
  - LTM June 2026 = 125.3 - 56.0 + 54.1 = US$123.4m. Without the US$14.2m Q4 2025 one-off: US$109.2m (inference).
  - The FY2026 guidance of US$100 to 106m is below the US$110.0m term loan B condition (deal brief) by US$4.0m to US$10.0m.
  - The implied H2 2026 is 45.9 to 51.9, against H2 2025 of 125.3 - 56.0 = 69.3.
- **Source:** 10-K, "Results" and "Financial covenant"; 10-Q, "Results" and "Cybersecurity incident"; 8-K 2026-08-05, "Item 7.01"
- **Severity:** Critical. Test: could block closing. Guided FY2026 Adjusted EBITDA (US$100 to 106m) is below the US$110.0m financing condition. Also, the 6.0x sizing on US$125.3m includes the US$14.2m one-off: 6.0 x 14.2 = US$85.2m of term loan B debt resting on it.
- **Confidence:** High for the figures. Medium for the closing-date LTM, which depends on 2027 results.
- **Deal impact:** Closing risk (financing), valuation.
- **Cross-check:** Financial: the full Adjusted EBITDA reconciliation, the quarterly bridge and the Q3 2026 actuals.

#### SEC-31: The DEF 14A bonus scale paid 150% on Adjusted EBITDA that included the one-off. No special committee is disclosed
- **Finding:** The bonus was paid on the reported figure. Without the US$14.2m change in estimate, Adjusted EBITDA was just above threshold.
- **Evidence:**
  - DEF 14A: threshold US$110.0m (50%), target US$118.0m (100%), maximum US$129.0m (175%), actual US$125.3m (150%).
  - "The Compensation Committee did not adjust FY2025 Adjusted EBITDA for the change in estimate of implicit price concessions recorded in the fourth quarter of 2025."
  - Ellery's bonus was US$1,710,000 on a US$1,140,000 target.
  - Special committee: not found in SEC filings. The proxy was filed April 10, 2026, before the deal.
- **Math (inference, assuming linear interpolation; this checks out because 100% + 7.3/11 x 75% = 149.8% at actual):**
  - 125.3 - 14.2 = 111.1. Payout = 50% + 1.1/8 x 50% = 56.9%.
  - Ellery's bonus would be about US$648,600, which is US$1,061,400 less than paid.
  - The other change-in-control items are unchanged: single-trigger equity of US$31.4m, a US$3.5m 280G gross-up, and an Ellery total of US$41.6m.
  - The related-party lease rent is 4.8 vs 3.6 market = US$1.2m (33.3%) above market, extended to 2040.
- **Source:** DEF 14A, "FY2025 annual bonus", "Change-in-control arrangements" and "Certain relationships and related transactions"
- **Severity:** Medium for the bonus (governance). The lease and the change-in-control terms remain points to negotiate.
- **Confidence:** High for the quotes. Medium for the recomputed payout.
- **Deal impact:** Governance, post-closing (clawback, lease renegotiation), negotiation with the CEO, who is also the founder and the landlord.
- **Cross-check:** News: any special committee formed for the Halvard deal. Financial: the bonus accrual and the clawback policy.

### Positive or mitigating points
- The 10-K disclosed the US$14.2m change in estimate, the material weakness, the adverse ICFR opinion, the 15% add-back cap and the change-of-control default. The proxy openly states that the bonus was not adjusted.
- The 10-Q discloses the CID with its scope and date, though late. It also discloses the cyber costs, the 412,300 notifications, the OCR inquiry and that the material weakness is not yet remediated.
- Hollis was dismissed with prejudice on June 9, 2026.
- The debt figures reconcile exactly to the deal brief's US$424.7m repayment.
- No prompt injection was found in any file.

### Gaps and questions for management
1. Why did the 10-K (March 5, 2026) deny any material pending investigation after the February 11 CID? Was a Q1 2026 10-Q filed, and did it disclose the CID?
2. When did Corvane learn of the Whitcomb complaint and the seal? Will it file an 8-K on the August 18 intervention? What loss estimate does it have now?
3. Why does the 10-K omit the December 2025 IPR denial? Does the "without merit" view still hold after the Markman ruling? What about the US$68.0m damages claim and injunction risk?
4. What is the final 0419U rate? What share of OncoTrace revenue is Medicare? Which contracts, and which payers including Orvia, are Medicare-linked?
5. When did the forensic firm first report exfiltration? Why Item 8.01 and not Item 1.05? Why no 8-K/A?
6. What are the Q3 2026 Consolidated EBITDA and the covenant ratio? Is a waiver or amendment needed?
7. Was an interim goodwill impairment test run after the guidance cut and the share price fall?
8. Which payers added prior authorization? What has speaker program spend been since 2019?
9. What is the Veltrane status: any termination notices, and how much of the US$61.0m backlog remains?
10. Provide the full Adjusted EBITDA reconciliation and add-back definitions, and the CCO separation terms.
11. Is there a special committee of independent directors for the Halvard transaction?
