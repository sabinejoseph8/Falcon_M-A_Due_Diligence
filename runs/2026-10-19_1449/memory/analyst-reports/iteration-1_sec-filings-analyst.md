## SEC filings analyst: findings

### Files reviewed

All five files were read in full, plus the deal brief for context.
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/deal-brief.md` (context only)
- `.../targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md` (filed March 5, 2026)
- `.../targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md` (filed August 5, 2026)
- `.../targets/kestrel/data/sec-filings/CRVD_8-K_2026-04-27_network-disruption.md` (event April 18, 2026; filed April 27, 2026)
- `.../targets/kestrel/data/sec-filings/CRVD_8-K_2026-08-05_q2-results-guidance.md` (filed August 5, 2026)
- `.../targets/kestrel/data/sec-filings/CRVD_DEF14A_2026_excerpts.md` (filed April 10, 2026)

No file tried to instruct the agents. I found no prompt-injection text.

### Key numbers (for the financial analyst)

| Item | Value | Source |
|---|---|---|
| FY2025 revenue / FY2024 | 431.0 / 386.0 (+11.7%) | 10-K Item 7 |
| Q4 2025 favorable change in estimate (implicit price concessions) | 14.2 (revenue and operating income) | 10-K Item 7 |
| FY2025 Adjusted EBITDA | 125.3 (+25.4%, so FY2024 about 99.9) | 10-K Item 7 |
| Implicit price concession reserve | 31.3 at Dec 31, 2025 (2024: 21.3) | 10-K Note 2 |
| H1 2026 / H1 2025 revenue | 203.4 / 205.2 | 10-Q MD&A |
| H1 2026 / H1 2025 operating income | 6.0 / 26.6 | 10-Q MD&A |
| H1 2026 / H1 2025 Adjusted EBITDA | 54.1 / 56.0 | 10-Q MD&A |
| Q2 2026 revenue / Adjusted EBITDA | 100.8 / 26.0 | 8-K Aug 5 |
| FY2026 guidance, March 5 to August 5 | Revenue 455-465 to 405-415; Adj. EBITDA 134-140 to 100-106 | 8-K Aug 5 |
| Debt at June 30, 2026 | Term loan 389.7 + revolver 35.0 = 424.7; cash 28.8; net 395.9 | 10-Q Liquidity |
| Debt at Dec 31, 2025 | Term loan 391.8 + revolver 30.0; cash 30.8; net 391.0 | 10-K Liquidity |
| Covenant maximum | 4.50x through June 30, 2026; 4.00x from September 30, 2026 | 10-K / 10-Q |
| Biopharma backlog | 246.0 (Dec 2025) to 231.4 (June 2026), of which Veltrane 61.0 | 10-K / 10-Q |
| Cyber incident | Costs 6.1 (excluded from Adj. EBITDA), lost revenue about 4.0, insurance limit 10.0 | 10-Q |

**Covenant definitions, quoted exactly from the 10-K, Item 7, "Financial covenant" (for the financial analyst):**
- "Consolidated Net Leverage Ratio (consolidated total debt less unrestricted cash, divided by Consolidated EBITDA for the last four fiscal quarters)"
- "'Consolidated EBITDA' means operating income plus depreciation and amortization and non-cash stock-based compensation, plus restructuring charges and other non-recurring or unusual cash costs."
- "The total of restructuring charges and other non-recurring or unusual costs added back may not exceed 15% of Consolidated EBITDA calculated before those add-backs."
- "Gains on asset sales and other non-operating income are excluded. Consolidated EBITDA is therefore not the same as our Adjusted EBITDA."
- "A compliance certificate is due to the lenders within 45 days after each quarter end. A breach of the covenant is an event of default."
- "A change of control of Corvane is also an event of default."

### Findings

#### SEC-01: FY2025 results include a one-off US$14.2 million Q4 change in estimate, on the same estimate that has a material weakness
- **Finding:** In Q4 2025 Corvane updated its collection-rate model for OncoTrace. This added US$14.2 million to FY2025 revenue and operating income, all of it in Q4. The deal brief accepts FY2025 Adjusted EBITDA of US$125.3 million "with all company add-backs accepted", which includes this amount.
- **Evidence:** "increased FY2025 revenue and operating income by **US$14.2 million**, all recorded in the fourth quarter of 2025." My math:
  - Adjusted EBITDA without it: 125.3 - 14.2 = 111.1.
  - Revenue growth without it: (431.0 - 14.2) / 386.0 - 1 = 8.0%, against the 11.7% reported.
  - Clinical testing growth without it: 300.6 / 279.3 (implied FY2024) - 1 = 7.6%, against 12.7%.
  - Value at the deal multiple: 14.2 x 13.2 = 187.4, which is 11.4% of the 1,648.6 EV.
  - Leverage: EV / 111.1 = 14.8x (not 13.2x). The term loan is 750.0 / 111.1 = 6.75x (not 6.0x).
  - Dated judgment: the Q4 2025 estimate was based on "improved collection experience". By H1 2026 the 10-Q reports "lower collections on OncoTrace claims" and a denial rate that rose from 13.4% to 16.2%. That puts the Q4 2025 assumption in doubt (interpretation).
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, section "Item 7, Change in estimate of implicit price concessions"; same file, "Item 9A"; `CRVD_10-Q_Q2-2026_excerpts.md`, "Results for the six months ended June 30, 2026"
- **Severity:** Critical. It meets the more-than-10%-of-value test: 14.2 x 13.2 = 187.4, or 11.4% of EV.
- **Confidence:** High. Stated directly in the 10-K, with numbers recomputed.
- **Deal impact:** Valuation, plus financing sizing.
- **Cross-check:** Find the Q4 2025 quarterly revenue in the financials to show the 14.2 as a share of the quarter. Check the Adjusted EBITDA bridge and whether the change is flagged there. Check cash collections for 2023-2024 dates of service against the model.

#### SEC-02: FY2026 guidance cut to US$100-106 million Adjusted EBITDA, below the US$110.0 million financing condition
- **Finding:** On August 5, 2026, Corvane cut FY2026 Adjusted EBITDA guidance to US$100-106 million. The whole new range is below the commitment letter's LTM Adjusted EBITDA condition of US$110.0 million. The deal brief model (built as of June 30, 2026) still uses the old US$137.0 million midpoint. The new guidance also excludes the 2027 Medicare rate for 0419U, which will sit inside the LTM period at a Q2 2027 closing.
- **Evidence:**
  - Midpoint cut: 137.0 to 103.0 = -34.0 (-24.8%). Revenue midpoint: 460 to 410 = -50 (-10.9%).
  - Implied H2 2026 Adjusted EBITDA: 100 to 106 minus 54.1 = 45.9 to 51.9, against H2 2025 of 125.3 - 56.0 = 69.3 (which includes the 14.2).
  - LTM at June 30, 2026: 125.3 - 56.0 + 54.1 = 123.4. This rolls off to 100-106 at December 31, 2026 if guidance is met (projection).
  - Value: 34.0 x 13.2 = 448.8, or 27.2% of EV.
  - The guidance "does not include any effect of the final 2027 Medicare rate for code 0419U."
- **Source:** `CRVD_8-K_2026-08-05_q2-results-guidance.md`, section "Item 7.01, Updated FY2026 outlook"; `CRVD_10-Q_Q2-2026_excerpts.md`, "Results for the six months"
- **Severity:** Critical. It meets two tests. Block closing: guidance of 100-106 is below the 110.0 financing condition. More than 10% of value: 448.8 is 27.2% of EV.
- **Confidence:** High for the filed numbers. The LTM figure at closing is a projection.
- **Deal impact:** Closing risk (financing condition) and valuation.
- **Cross-check:** Look for Q3 2026 actuals or any later guidance update in news or financials. Get the share price after August 5: the 32.6% premium is measured on July 31, before the cut. Check analyst consensus.

#### SEC-03: Covenant steps down to 4.00x at September 30, 2026; headroom never disclosed
- **Finding:** The maximum net leverage falls from 4.50x to 4.00x at the September 30, 2026 test. The 10-Q says only that Corvane was "in compliance" at June 30. It gives no ratio, no headroom and no forward-looking warning, even though guidance was cut the same day. Q4 2025's 14.2 rolls out of LTM Consolidated EBITDA at the December 31, 2026 test. The 15% cap may also limit add-backs such as the 6.1 of cyber costs.
- **Evidence:**
  - Minimum Consolidated EBITDA needed at June 30 net debt of 395.9: 395.9 / 4.00 = 99.0 at the 4.00x test (395.9 / 4.50 = 88.0 at the old level).
  - FY2026 Adjusted EBITDA guidance is 100-106, and Consolidated EBITDA "is therefore not the same as our Adjusted EBITDA."
  - The September 30 certificate is due by about November 14, 2026. The December 31 certificate is due by about February 14, 2027. Both fall before closing.
  - Breach is an event of default with acceleration.
- **Source:** `CRVD_10-K_FY2025_excerpts.md`, "Item 7, Liquidity and capital resources / Financial covenant"; `CRVD_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources"
- **Severity:** High. A breach before signing or closing would make this Critical under the calibration rule. I cannot compute Consolidated EBITDA from SEC data, because D&A, SBC and the add-back detail are not in these files.
- **Confidence:** Medium. The definitions and debt are primary. Whether headroom is tight is my inference.
- **Deal impact:** Closing risk and liquidity before closing. Revolver availability is US$65.0 million.
- **Cross-check:** The financial analyst should compute LTM Consolidated EBITDA under the exact definition and apply the 15% cap. Check whether goodwill impairment (non-cash, and not listed as an add-back) would cut covenant EBITDA. Look in news for any amendment or waiver talks.

#### SEC-04: DOJ civil investigative demand received before the 10-K was filed, but the 10-K says no material investigation
- **Finding:** Corvane received a DOJ CID on February 11, 2026. It covers Medicare billing of genetic tests, including OncoTrace, and the physician speaker program, going back to January 2019. The 10-K was filed 22 days later, on March 5, 2026. It does not mention the CID. It states "not aware of any pending government investigation that we expect to be material." It also lists no subsequent events.
- **Evidence:** 10-Q: "On February 11, 2026, we received a civil investigative demand (CID) from the U.S. Department of Justice." 10-K Note 15: "identified none requiring disclosure." No accrual, and no range of loss. The 10-K risk factors cite treble damages and exclusion.
- **Source:** `CRVD_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1. Legal Proceedings"; `CRVD_10-K_FY2025_excerpts.md`, "Item 3. Legal Proceedings" and "Note 15"
- **Severity:** High. False Claims Act exposure on the flagship test, plus a disclosure-quality issue. Not quantifiable from the filings.
- **Confidence:** High. Both dates are in primary filings.
- **Deal impact:** Valuation, closing risk (MAE definition), and post-closing liability. Needs a specific indemnity or escrow.
- **Cross-check:** Litigation: look for a related qui tam complaint (possibly under seal or unsealed) and its filing date. News: reports of the CID or the speaker program. Financials: Medicare OncoTrace revenue since 2019.

#### SEC-05: CMS final 2027 rate for OncoTrace (0419U) published, but Corvane did not disclose the amount
- **Finding:** CMS set a new 0419U rate on July 29, 2026, effective January 1, 2027. The 10-Q does not give the rate or its effect. It says the company is "evaluating" and "may seek reconsideration". The rate also passes through to about 40% of non-Medicare OncoTrace revenue, through commercial contracts priced off the Medicare rate. The deal brief assumes flat Medicare rates through 2030.
- **Evidence:**
  - OncoTrace = 44% x 314.8 = 138.5 in FY2025, or 32.1% of total revenue.
  - Medicare is 24.2% x 431.0 = 104.3 of total revenue.
  - "We do not expect it to affect our 2026 results. We are evaluating the effect on future periods."
- **Source:** `CRVD_10-Q_Q2-2026_excerpts.md`, "Reimbursement"; `CRVD_10-K_FY2025_excerpts.md`, "Clinical testing", "Payer contracts", "Item 1A"
- **Severity:** High. The size is unknown from the SEC filings, so I cannot show the Critical test.
- **Confidence:** High that the rate changed and was not quantified. The direction of the change is not found in SEC filings.
- **Deal impact:** Valuation and the closing LTM condition.
- **Cross-check:** News or the CMS final rule for the new 0419U rate. Financials: OncoTrace revenue by payer, to size the direct and pass-through effect.

#### SEC-06: Material weakness and adverse ICFR opinion, still not remediated at Q2 2026
- **Finding:** Internal control over financial reporting was not effective at December 31, 2025. The weakness was in the controls over the same implicit price concession estimate that produced the 14.2 one-off (SEC-01). Brannock & Lyle issued an adverse ICFR opinion. At June 30, 2026 the weakness "has not yet been remediated." The target date has moved from "during 2026" to "by the end of 2026". There was no auditor change (Brannock & Lyle has been auditor since 2019).
- **Evidence:** "review of the data and assumptions used in the collection-rate model was not precise enough to detect a material misstatement." The implicit price concession reserve rose from 21.3 to 31.3 (+47.0%) while revenue rose 11.7%.
- **Source:** `CRVD_10-K_FY2025_excerpts.md`, "Item 9A" and "Note 2"; `CRVD_10-Q_Q2-2026_excerpts.md`, "Part I, Item 4"
- **Severity:** High. Earnings quality behind the valuation and the financing condition both rest on this estimate.
- **Confidence:** High. Stated in primary filings.
- **Deal impact:** Valuation and disclosure. Supports a quality-of-earnings review and specific representations.
- **Cross-check:** Financials: reconcile the reserve roll-forward to cash collections. News: any restatement chatter or auditor comments. The opinion on the financial statements themselves is not found in the SEC excerpts.

#### SEC-07: Ransomware first described as a "network disruption" with no evidence of data theft; 412,300 people later notified
- **Finding:** The detection on April 18 was reported nine days later, on April 27, under Item 8.01 (not Item 1.05). The 8-K called it a "network disruption" and said there was "no evidence at this time that patient information was exfiltrated", and that no material impact was expected. The 10-Q later called it a ransomware attack and reported several further facts (listed below). The August guidance cut cites the disruption as a cause.
- **Evidence:**
  - Testing was disrupted for nine days. The 8-K says operations were restored April 26, which is eight days.
  - About 412,300 individuals were notified in June 2026.
  - Costs were 6.1 plus lost revenue of about 4.0, a total of 10.1, against an insurance limit of 10.0.
  - Putative class actions have been filed, and HHS OCR has opened an inquiry. "We cannot estimate a range of possible loss."
  - No amended 8-K was found in SEC filings.
- **Source:** `CRVD_8-K_2026-04-27_network-disruption.md`, "Item 8.01"; `CRVD_10-Q_Q2-2026_excerpts.md`, "Cybersecurity incident"
- **Severity:** High. Disclosure reliability, uninsured exposure, and a regulatory inquiry.
- **Confidence:** High. Both filings are primary sources. Whether Item 1.05 was required is my interpretation.
- **Deal impact:** Disclosure, post-closing liability, indemnity.
- **Cross-check:** News: when ransomware or data theft was first reported (for example a ransom group's leak-site claims before June). Litigation: class action filing dates and claims. Financials: the 6.1 add-back.

#### SEC-08: Dated judgment: goodwill test at October 1, 2025 had only 14% headroom, and its assumptions have since broken
- **Finding:** At the October 1, 2025 test, the Clinical testing unit (goodwill 241.5) had about 14% headroom. The test assumed stable OncoTrace Medicare rates and 9% growth. Since then:
  - the 0419U rate has changed (SEC-05);
  - H1 2026 clinical revenue fell 1.9%;
  - guidance was cut by 24.8% at the EBITDA midpoint;
  - the share price fell from US$27.80 at the test date to US$18.10 on July 31, 2026 (-34.9%). The offer of US$24.00 is itself 13.7% below the test-date price.

  The 10-K says "A 10% reduction in projected cash flows... would eliminate most of the headroom." The 10-Q excerpts do not mention an interim impairment assessment.
- **Evidence:** 18.10 / 27.80 - 1 = -34.9%. 24.00 / 27.80 - 1 = -13.7%.
- **Source:** `CRVD_10-K_FY2025_excerpts.md`, "Critical accounting estimates: goodwill"; `CRVD_10-Q_Q2-2026_excerpts.md`; deal brief (share price)
- **Severity:** High. The impairment is non-cash, but the covenant's Consolidated EBITDA adds back only D&A, SBC and "non-recurring or unusual cash costs". An impairment may therefore cut covenant EBITDA (interpretation, needs legal reading of the credit agreement).
- **Confidence:** Medium. The facts are primary. The impairment conclusion is inference.
- **Deal impact:** Valuation signal, covenant, disclosure.
- **Cross-check:** Market data for the current CRVD price. Financials: Clinical testing projections. Ask whether an interim test was done at June 30, 2026.

#### SEC-09: Largest commercial payer Orvia (11.3% of revenue) can terminate on change of control
- **Finding:** Orvia Health Plan may terminate its network agreement on 60 days' notice if Corvane undergoes a change of control. This deal would be one.
- **Evidence:** 11.3% x 431.0 = 48.7 of FY2025 revenue. "Orvia may terminate the agreement on 60 days' notice if Corvane undergoes a change of control."
- **Source:** `CRVD_10-K_FY2025_excerpts.md`, "Payer contracts"
- **Severity:** High. It needs a consent or waiver as a closing condition, or price protection.
- **Confidence:** High. Stated in the 10-K, with numbers recomputed.
- **Deal impact:** Closing risk and post-closing revenue.
- **Cross-check:** Financials: confirm Orvia's rank and revenue in `revenue_by_customer.csv`. News: Orvia's relationship with Corvane, and whether Orvia is one of the two payers that added prior authorization.

#### SEC-10: Veltrane (11.7% of revenue, 26.4% of backlog) can terminate work orders on 90 days' notice
- **Finding:** Veltrane is the largest biopharma client. Most of its work comes from the ATLAS-3 Phase 3 trial of VLT-220. Its work orders are terminable for convenience on 90 days' notice, "paying only for work performed." The deal brief assumes the backlog converts on its historical schedule, including Veltrane.
- **Evidence:** 11.7% x 431.0 = 50.4 of FY2025 revenue. Veltrane backlog 61.0 / 231.4 = 26.4% of June 30, 2026 backlog.
- **Source:** `CRVD_10-K_FY2025_excerpts.md`, "Biopharma services"; `CRVD_10-Q_Q2-2026_excerpts.md`, "Biopharma services"
- **Severity:** High. Single-trial dependency with short-notice termination.
- **Confidence:** High for the contract terms and numbers. The SEC filings say nothing about the trial's status.
- **Deal impact:** Valuation (backlog thesis), post-closing.
- **Cross-check:** News: ATLAS-3 / VLT-220 trial results, any halt, or Veltrane's financial condition. Financials: Veltrane revenue by quarter in 2026.

#### SEC-11: Biopharma backlog is shrinking (book-to-bill 0.7)
- **Finding:** Backlog fell from 246.0 to 231.4 in six months, and the "slower biopharma bookings" are cited in the guidance cut. This conflicts with the thesis of "a growing biopharma services backlog".
- **Evidence:** 231.4 - 246.0 = -14.6 (-5.9%). "Book-to-bill was 0.7 in the first half of 2026."
- **Source:** `CRVD_10-Q_Q2-2026_excerpts.md`, "Biopharma services"; `CRVD_8-K_2026-08-05_q2-results-guidance.md`
- **Severity:** Medium
- **Confidence:** High. Stated in primary filings.
- **Deal impact:** Valuation (thesis point 3 is stale).
- **Cross-check:** Financials: backlog roll-forward and cancellations.

#### SEC-12: Gap between operating income and Adjusted EBITDA widened by US$18.7 million in H1 2026
- **Finding:** Operating income fell 77.4%, but Adjusted EBITDA fell only 3.4%. The add-back gap grew from 29.4 (26.6 to 56.0) to 48.1 (6.0 to 54.1). Only 6.1 of the 18.7 increase is explained in the filings (cyber costs). The financing condition uses Corvane's own definition, so add-back quality decides whether the 110.0 test is met.
- **Evidence:**
  - Gap increase: 48.1 - 29.4 = 18.7; unexplained: 18.7 - 6.1 = 12.6.
  - Gross margin: 38.0% (77.3 / 203.4) in H1 2026 against 43.0% (88.2 / 205.2) in H1 2025.
- **Source:** `CRVD_10-Q_Q2-2026_excerpts.md`, "Results for the six months ended June 30, 2026" and "Cybersecurity incident"
- **Severity:** High. It bears on the size of EBITDA, the financing condition and the covenant cap.
- **Confidence:** Medium. The numbers are primary. The add-back breakdown is not found in SEC filings.
- **Deal impact:** Valuation and closing (definition of the financing condition).
- **Cross-check:** Financials: the H1 2026 Adjusted EBITDA bridge, line by line.

#### SEC-13: Chief Compliance Officer left in January 2026, just before the DOJ CID; 10-K still describes the CCO role
- **Finding:** CCO Daniel Pruitt "left" in January 2026, with no reason or payment disclosed. The CID covering the speaker program arrived on February 11. The 10-K (March 5) describes a program "overseen by our Chief Compliance Officer" and does not mention the departure. The Deputy General Counsel is interim CCO. The departure was first disclosed in the proxy on April 10.
- **Evidence:** DEF 14A: "Our Chief Compliance Officer, Daniel Pruitt, left Corvane in January 2026." The 10-K says the speaker program is one "we believe complies with the federal Anti-Kickback Statute."
- **Source:** `CRVD_DEF14A_2026_excerpts.md`, "Executive officers"; `CRVD_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1A"; `CRVD_10-K_FY2025_excerpts.md`, "Compliance program"
- **Severity:** Medium on its own. It supports SEC-04.
- **Confidence:** High for the facts. Any link between the departure and the CID is not stated in the filings.
- **Deal impact:** Disclosure and governance. Possible whistleblower angle (a question to check, not a finding).
- **Cross-check:** Litigation: whether Pruitt is a relator or plaintiff. News: reports on why he left. Separation terms are not found in SEC filings.

#### SEC-14: CEO gets US$41.6 million on change of control, with single-trigger equity and a 280G gross-up
- **Finding:** Mr. Ellery's equity acceleration (US$31.4 million) is single trigger, and he has a Section 280G excise tax gross-up (US$3.5 million). Other executives also have single-trigger equity, with combined benefits of US$14.8 million.
- **Evidence:** Executive total: 41.6 + 14.8 = 56.4, which is 4.5% of the 1,257.6 equity value. Cash severance check: 3.0 x (0.95 + 1.14) = 6.27, which rounds to 6.3.
- **Source:** `CRVD_DEF14A_2026_excerpts.md`, "Change-in-control arrangements"
- **Severity:** Medium
- **Confidence:** High. Stated in the proxy, with numbers recomputed.
- **Deal impact:** Valuation (transaction cost), retention after closing, and CEO incentives in negotiation.
- **Cross-check:** Check that the fees and expenses line (47.7) and the equity value include these costs.

#### SEC-15: FY2025 bonus paid at 150% because of the unadjusted one-off
- **Finding:** Bonuses are 100% based on Adjusted EBITDA. The Committee "did not adjust FY2025 Adjusted EBITDA for the change in estimate." Excluding the 14.2, Adjusted EBITDA was 111.1, which is below the 118.0 target and just above the 110.0 threshold.
- **Evidence:** Assuming linear interpolation (my assumption), the payout would be about 50% + (1.1 / 8.0) x 50% = 56.9% instead of 150%. Mr. Ellery's bonus would have been about US$0.65 million instead of US$1.71 million. The bonus threshold (110.0) equals the financing condition level.
- **Source:** `CRVD_DEF14A_2026_excerpts.md`, "FY2025 annual bonus"; `CRVD_10-K_FY2025_excerpts.md`, Item 7
- **Severity:** Medium
- **Confidence:** High for the facts. Medium for the recomputed payout (the interpolation is assumed).
- **Deal impact:** Governance and incentives, and the reliability of management's estimate.
- **Cross-check:** The timing of the Q4 model change compared with when bonus results were finalized.

#### SEC-16: CEO-owned headquarters lease extended to 2040 at 33% above appraised market rent
- **Finding:** In November 2025 the Audit Committee extended the lease with Ellery Property Holdings LLC (owned by the CEO and his spouse) from 2030 to 2040. It kept the existing rent of US$4.8 million, with 3.5% annual increases, despite an independent appraisal of US$3.6 million market rent. The CEO is also Board Chair.
- **Evidence:**
  - Premium: 4.8 - 3.6 = 1.2 a year (33.3%).
  - Over 15 years the excess is at least US$18.0 million undiscounted at a flat 1.2 gap. It is about US$24.0 million if both rents grow 3.5% a year (projection).
- **Source:** `CRVD_DEF14A_2026_excerpts.md`, "Certain relationships and related transactions"; `CRVD_10-K_FY2025_excerpts.md`, "Note 12"
- **Severity:** Medium
- **Confidence:** High. Stated in primary filings. The projection is labeled as such.
- **Deal impact:** Valuation (EBITDA normalization of about 1.2 a year) and governance. Renegotiate as part of the deal.
- **Cross-check:** Financials: rent expense. News or property records on Ellery Property Holdings.

#### SEC-17: Genaro patent suit seeks an injunction against the OncoTrace method; no accrual
- **Finding:** Genaro alleges that the OncoTrace target-capture method infringes U.S. Patent No. 11,604,318. It seeks damages and an injunction. Claim construction briefing was completed in Q2 2026. No accrual has been recorded and no range of loss is given. The wording is unchanged between the 10-K and the 10-Q.
- **Evidence:** "Genaro seeks damages and an injunction." OncoTrace is about 138.5 of revenue (32.1% of total).
- **Source:** `CRVD_10-K_FY2025_excerpts.md`, "Item 3"; `CRVD_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1"
- **Severity:** High. An injunction would hit the flagship test, so a specific indemnity is needed.
- **Confidence:** Medium. The suit is a fact. The merits are allegations.
- **Deal impact:** Valuation, post-closing.
- **Cross-check:** Litigation docket: the claim construction ruling or schedule, the trial date, any preliminary injunction motion, and the damages theory.

#### SEC-18: Inconsistent Pell Ridge goodwill timing; FY2025 growth includes an acquisition
- **Finding:** The 10-K says Pell Ridge was acquired in May 2025. It also says Pell Ridge goodwill of US$22.3 million "was added after the test date" of October 1, 2025 "and was not tested". These two statements do not fit together as written. FY2025 growth of 11.7% also includes Pell Ridge's revenue. The amount is not found in SEC filings.
- **Evidence:** Acquired May 2025 for US$31.0 million. Goodwill 22.3 / 31.0 = 71.9% of the price.
- **Source:** `CRVD_10-K_FY2025_excerpts.md`, "Item 1. Overview" and "Critical accounting estimates: goodwill"
- **Severity:** Medium
- **Confidence:** Medium. The inconsistency is in the text. The cause (for example, measurement-period adjustments) is unknown.
- **Deal impact:** Valuation (organic growth) and disclosure quality.
- **Cross-check:** Financials: Pell Ridge revenue in FY2025 and organic growth.

#### SEC-19: Denial rate rising on payer prior authorization
- **Finding:** The initial denial rate rose from 13.4% (FY2025) to 16.2% (H1 2026). Corvane attributes this mainly to two commercial payers adding prior authorization for hereditary cancer panels. The higher denials drove the clinical revenue decline and the guidance cut. The direction is opposite to the improved collections assumed in Q4 2025 (SEC-01).
- **Evidence:** +2.8 percentage points (+20.9% relative).
- **Source:** `CRVD_10-Q_Q2-2026_excerpts.md`, "Results for the six months ended June 30, 2026"
- **Severity:** Medium
- **Confidence:** High. Stated in the 10-Q.
- **Deal impact:** Valuation (recurring revenue level).
- **Cross-check:** News: which payers added prior authorization, and whether Orvia is one. Financials: denial and collection trends by payer.

#### SEC-20: Change of control is an event of default under the existing credit agreement
- **Finding:** The deal triggers a default under the existing credit agreement. The plan is to repay it at closing. The 424.7 in the uses table equals the June 30, 2026 balances (389.7 + 35.0). Prepayment premiums, interest rate and breakage costs are not found in SEC filings.
- **Evidence:** "A change of control of Corvane is also an event of default." The term loan matures October 2029 and the revolver October 2028.
- **Source:** `CRVD_10-K_FY2025_excerpts.md`, "Liquidity and capital resources"; `CRVD_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources"
- **Severity:** Low. It is cured by repayment at closing. Covenant risk before closing is covered in SEC-03.
- **Confidence:** High. Stated in the 10-K, and the balances reconcile to the deal brief.
- **Deal impact:** Closing mechanics. The payoff amount could change if the revolver is drawn further.
- **Cross-check:** Financials: the debt schedule and any prepayment fees.

### Positive or mitigating points
- The Hollis overtime class action was "dismissed... with prejudice" on June 9, 2026 (10-Q).
- The Helixor supply agreement fixes reagent prices through December 31, 2028, and Helixor bears "all import duties and tariffs" (10-K, Suppliers).
- The US$6.8 million sale-leaseback gain is "excluded from EBITDA and Adjusted EBITDA" (10-K Note 7). The covenant also excludes asset-sale gains.
- Corvane disclosed the material weakness, received an adverse ICFR opinion, and hired a revenue cycle controller in May 2026. There was no auditor change (Brannock & Lyle since 2019).
- The related-party lease was approved after an independent appraisal and is disclosed in full.
- Cash severance is double trigger. Revolver capacity of US$65.0 million was available at June 30, 2026.
- Net debt of 391.0 and the repayment amount of 424.7 in the deal brief reconcile exactly to the filings.

### Gaps and questions for management
1. What is the actual Consolidated Net Leverage Ratio at June 30 and September 30, 2026, with the add-backs and the 15% cap applied? Is a waiver or amendment being discussed? Was the September 30 certificate delivered?
2. What is the final 2027 rate for 0419U compared with 2026, and what is the effect on OncoTrace revenue, including the commercial contracts priced off Medicare?
3. Why did the 10-K (March 5, 2026) not disclose the February 11, 2026 DOJ CID? Is there a related qui tam? What is the status of document production?
4. Why did the CCO leave, and on what terms? Is he connected to the CID?
5. When did Corvane learn that patient data had been taken? Why was the incident filed under Item 8.01 and never updated? What is the ransom status, and what is the status of the OCR inquiry and the class actions?
6. Provide a line-by-line H1 2026 Adjusted EBITDA bridge explaining the 18.7 increase in add-backs.
7. Was an interim goodwill impairment test done at June 30, 2026? Explain the Pell Ridge goodwill timing.
8. What is the ATLAS-3 / VLT-220 trial status? Has Veltrane given notice on any work order?
9. Will Orvia waive its change-of-control termination right?
10. Revenue contributed by Pell Ridge in FY2025 (organic growth): not found in SEC filings.
11. Q4 2025 quarterly revenue, D&A, SBC and the add-back detail: not found in SEC filings (financial analyst).
12. Credit agreement interest rate and prepayment terms: not found in SEC filings.
13. The current share price after the August 5 guidance cut is not found in SEC filings, so the 32.6% premium may be stale.
