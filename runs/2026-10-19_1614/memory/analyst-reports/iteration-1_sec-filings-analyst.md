## SEC filings analyst: findings

### Files reviewed

All read in full:
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/deal-brief.md` (context only)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md` (filed March 5, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/sec-filings/CRVD_DEF14A_2026_excerpts.md` (filed April 10, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/sec-filings/CRVD_8-K_2026-04-27_network-disruption.md` (filed April 27, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md` (filed August 5, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/sec-filings/CRVD_8-K_2026-08-05_q2-results-guidance.md` (filed August 5, 2026)

My folder has no Q1 2026 10-Q and no other 8-Ks. So when I say "not disclosed", I mean not disclosed in these five filings.

### Findings

#### SEC-001: The Q4 2025 change in estimate added US$14.2m to FY2025 revenue and EBITDA
- **Finding:** In Q4 2025 Corvane updated its collection-rate model. This one-off change in estimate added US$14.2m to FY2025 revenue and operating income, all in Q4. That is 11.3% of FY2025 Adjusted EBITDA (14.2 / 125.3). Without it, Adjusted EBITDA is US$111.1m, which is US$1.1m above the US$110.0m term loan floor.
- **Evidence:** "This change in estimate increased FY2025 revenue and operating income by US$14.2 million, all recorded in the fourth quarter of 2025." Calculations: revenue growth without the item is (431.0 - 14.2) / 386.0 = 8.0%, against 11.7% reported. Adjusted EBITDA growth without it is about 11.2%, against 25.4% reported (FY2024 base of 99.9 is implied by the 25.4%). At the deal multiple, 14.2 x 13.2 = US$187.4m, or 11.4% of the US$1,648.6m EV.
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 7 "Results", "Change in estimate of implicit price concessions"
- **Severity:** Critical. It meets the "more than 10% of value" test: the brief's base case accepts all add-backs at 13.2x, and the item is worth US$187.4m, or 11.4% of EV.
- **Confidence:** High. Stated in the 10-K and recomputed.
- **Deal impact:** Valuation. It also reduces cushion under the US$110.0m term loan condition.
- **Cross-check:** Financials: Q4 2025 revenue and EBITDA by quarter, and whether the company's Adjusted EBITDA reconciliation removes the item (the SEC text suggests it does not). News: analyst commentary on Q4 2025 quality.

#### SEC-002: Material weakness in controls over the same estimate, adverse audit opinion, still not fixed at Q2 2026
- **Finding:** Management found internal control over financial reporting "not effective" at December 31, 2025. The weakness sits in the controls over the implicit price concession estimate, the same estimate that produced SEC-001. The auditor gave an adverse opinion on internal controls. The weakness "has not yet been remediated" at June 30, 2026. The target date for fixing it moved from "during 2026" to "by the end of 2026".
- **Evidence:** "the review of the data and assumptions used in the collection-rate model was not precise enough to detect a material misstatement." The 10-Q adds: "has not yet been remediated. We hired a revenue cycle controller in May 2026."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 9A; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, Part I Item 4
- **Severity:** High
- **Confidence:** High. Primary source.
- **Deal impact:** Valuation (reliability of the US$14.2m and of the reserve) and disclosure.
- **Cross-check:** Financials: reserve roll-forward and cash collections by date of service. The auditor's opinion on the financial statements themselves is not found in SEC filings. Ask whether it was unqualified.

#### SEC-003: Dated judgment. The reserve release looks weak against H1 2026 collections
- **Finding:** The Q4 2025 favorable estimate was based on "improved collection experience" for claims with 2023 and 2024 dates of service. Since then, H1 2026 clinical revenue fell because of "lower collections on OncoTrace claims", and the initial denial rate rose to 16.2% from 13.4%. Separately, the reserve balance rose from US$21.3m to US$31.3m (+US$10.0m, +46.9%) in the same year as the favorable change.
- **Evidence:** 10-K Note 2: reserve "US$31.3 million at December 31, 2025 (2024: US$21.3 million)." 10-Q: "lower collections on OncoTrace claims."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 7 and Note 2; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, MD&A "Results"
- **Severity:** High
- **Confidence:** Medium. Inference: the filings do not say the Q4 2025 estimate was wrong, and none of these filings reports a reversal.
- **Deal impact:** Valuation. There is a risk of a later unfavorable change in estimate (inference).
- **Cross-check:** Financials: the reserve at June 30, 2026 and collection rates by cohort. News: any analyst or short-seller comment on the reserve release.

#### SEC-004: Adjusted EBITDA definition and reconciliation are not in the SEC filings, and a new add-back appeared in 2026
- **Finding:** The 10-K refers readers to "our financial data" for the reconciliation. The definition and the full list of add-backs are not found in SEC filings. The 10-Q excludes a new item from Adjusted EBITDA: US$6.1m of cyber incident costs. The gap between operating income and Adjusted EBITDA grew from 29.4 (56.0 - 26.6) in H1 2025 to 48.1 (54.1 - 6.0) in H1 2026, up US$18.7m. The cyber costs explain US$6.1m of the increase. The SEC filings do not explain the other US$12.6m.
- **Evidence:** "US$6.1 million of incident response costs ... which we exclude from Adjusted EBITDA." H1 table: operating income 6.0 vs 26.6, and Adjusted EBITDA 54.1 vs 56.0.
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 7 "Results"; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, MD&A "Results" and "Cybersecurity incident"
- **Severity:** Medium
- **Confidence:** High on the numbers, Medium on what they mean.
- **Deal impact:** Valuation, and the term loan condition, which is tested on "Adjusted EBITDA (as Corvane defines it)".
- **Cross-check:** Financials: the Adjusted EBITDA bridge for FY2025 and H1 2026, line by line, including any change in add-back categories.

#### SEC-005: FY2026 guidance cut by 24.8% on Adjusted EBITDA (base case is out of date)
- **Finding:** On August 5, 2026, Corvane cut FY2026 revenue guidance from US$455 to 465m to US$405 to 415m. It cut Adjusted EBITDA guidance from US$134 to 140m to US$100 to 106m. The midpoint fell from 137 to 103 (-24.8%). That is 17.8% below FY2025's US$125.3m. The brief's model, built as of June 30, 2026, still uses US$137.0m.
- **Evidence:** Updated outlook table. Calculations: 1,648.6 / 103 = 16.0x EV/EBITDA on the guidance midpoint. At 13.2x, 103 x 13.2 = US$1,359.6m, which is US$289.0m (17.5%) below the US$1,648.6m EV. Implied H2 2026 Adjusted EBITDA is 100 - 54.1 = 45.9 to 51.9, against 69.3 in H2 2025.
- **Source:** `targets/kestrel/data/sec-filings/CRVD_8-K_2026-08-05_q2-results-guidance.md`, Item 7.01; `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, "Outlook for FY2026"
- **Severity:** Critical. It meets the "more than 10% of value" test: holding 13.2x, the guidance midpoint implies 17.5% lower EV.
- **Confidence:** High. Company guidance, recomputed.
- **Deal impact:** Valuation.
- **Cross-check:** Financials: Q3 2026 trading. News: share price reaction after August 5. The brief's 32.6% premium is measured on the July 31 price, which is before the cut.

#### SEC-006: The term loan's LTM Adjusted EBITDA condition (at least US$110.0m) fails on the new guidance
- **Finding:** FY2026 Adjusted EBITDA guidance of US$100 to 106m is US$4.0 to 10.0m below the US$110.0m closing condition. By a Q2 2027 closing, the last twelve months will no longer include Q4 2025, so the US$14.2m one-off will drop out (inference). The guidance also excludes the 2027 Medicare rate for code 0419U (SEC-017). At the midpoint, term loan leverage is 750 / 103 = 7.3x, against the 6.0x sizing.
- **Evidence:** "Adjusted EBITDA | 134 to 140 | 100 to 106"; "It does not include any effect of the final 2027 Medicare rate for code 0419U."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_8-K_2026-08-05_q2-results-guidance.md`, Item 7.01; condition from `targets/kestrel/data/deal-brief.md`, section 3
- **Severity:** Critical. It meets the "block closing" test: the company's own guidance midpoint (103) is below the financing condition (110).
- **Confidence:** High on the numbers. The LTM period at closing is a projection.
- **Deal impact:** Closing risk (financing).
- **Cross-check:** Financials: Q3 2026 actuals and the LTM path. Commitment letter: how LTM is defined and dated, and whether lenders can waive the condition.

#### SEC-007: Covenant step-down to 4.00x at September 30, 2026 leaves thin headroom (projection)
- **Finding:** The maximum Consolidated Net Leverage Ratio stepped down from 4.50x to 4.00x at the September 30, 2026 test. The 10-Q says Corvane complied at June 30 but does not disclose the ratio. At June 30 net debt of US$395.9m (389.7 + 35.0 - 28.8), a 4.00x test needs at least US$99.0m of Consolidated EBITDA. On FY2026 Adjusted EBITDA guidance, implied leverage is 3.73x to 3.96x. That is before the covenant definition's differences and its 15% add-back cap (SEC-008). The September 30 compliance certificate is due within 45 days, around November 14, 2026, before signing. The December 31, 2026 certificate falls between signing and closing.
- **Evidence:** "steps down from 4.50x to 4.00x at the September 30, 2026 test date." "A breach of the covenant is an event of default ... accelerate all amounts outstanding."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 7 "Financial covenant"; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, MD&A "Liquidity and capital resources"
- **Severity:** High. This should become Critical if Q3 or Q4 2026 data show a breach, because that would be an event of default before signing or closing. The SEC filings do not show one.
- **Confidence:** Medium. Projection; covenant EBITDA is not disclosed.
- **Deal impact:** Closing risk and capital structure.
- **Cross-check:** Financials: covenant EBITDA build at June 30 and September 30, 2026, and the compliance certificates. News: any waiver or amendment.

#### SEC-008: Covenant EBITDA definition has a 15% add-back cap and unclear treatment of non-cash charges
- **Finding:** Consolidated EBITDA adds back restructuring and "other non-recurring or unusual cash costs", capped at 15% of pre-add-back EBITDA. Gains, including the US$6.8m sale-leaseback gain, are excluded. The quoted definition adds back depreciation, amortization and stock compensation. It does not clearly add back a non-cash goodwill impairment (interpretation). The cyber costs and any new add-backs (SEC-004) count against the cap.
- **Evidence:** "The total of restructuring charges and other non-recurring or unusual costs added back may not exceed 15% of Consolidated EBITDA calculated before those add-backs."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 7 "Financial covenant"
- **Severity:** Medium
- **Confidence:** Medium. Based on an excerpt of the definition; the full credit agreement was not reviewed.
- **Deal impact:** Capital structure.
- **Cross-check:** Credit agreement text (not in SEC excerpts). Financials: add-back totals compared with the cap.

#### SEC-009: Change of control is an event of default under the existing credit agreement
- **Finding:** The merger would itself trigger default under the existing facility. The brief plans to repay US$424.7m at closing. That equals June 30, 2026 gross debt (389.7 + 35.0). Prepayment premiums and call protection are not found in SEC filings.
- **Evidence:** "A change of control of Corvane is also an event of default."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 7 "Financial covenant"
- **Severity:** High. Per the calibration rule, a debt problem cured by refinancing at closing is High.
- **Confidence:** High
- **Deal impact:** Closing mechanics. Payoff letter needed.
- **Cross-check:** Financials: payoff amount, accrued interest, breakage or prepayment fees. Check that the US$47.7m fees line covers them.

#### SEC-010: No debt maturities before closing
- **Finding:** The revolver matures October 2028 and the term loan October 2029.
- **Evidence:** "The term loan matures in October 2029 and the revolving facility in October 2028."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 7 "Liquidity and capital resources"
- **Severity:** Low (mitigating)
- **Confidence:** High
- **Deal impact:** Capital structure
- **Cross-check:** Financials debt schedule.

#### SEC-011: Liquidity and net debt reconcile to the brief
- **Finding:** Net debt at December 31, 2025 was 391.8 + 30.0 - 30.8 = US$391.0m, which matches the brief. At June 30, 2026, liquidity was US$93.8m (28.8 cash + 65.0 undrawn revolver). The revolver draw rose by US$5.0m. A covenant breach would let lenders "stop further revolving loans".
- **Evidence:** 10-Q: "cash of US$28.8 million ... US$35.0 million drawn ... leaving US$65.0 million of revolving capacity."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 7; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Capital structure
- **Cross-check:** Financials: cash flow and revolver usage after June 30.

#### SEC-012: DOJ civil investigative demand on Medicare genetic test billing and the speaker program
- **Finding:** On February 11, 2026, DOJ issued a CID covering Medicare billing of genetic tests, including OncoTrace, and the physician speaker program, from January 2019. There is no accrual and no range of loss. The 10-K had said the speaker program "we believe complies with the federal Anti-Kickback Statute." Exposure includes treble damages and exclusion from Medicare, which was 24.2% of FY2025 revenue, or US$104.3m (from the 10-K risk factors).
- **Evidence:** "we received a civil investigative demand (CID) from the U.S. Department of Justice ... for the period from January 2019."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, Part II Item 1 "Government investigation"; `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 1 "Compliance program" and Item 1A
- **Severity:** High. It cannot be quantified from SEC filings, so it is not rated Critical.
- **Confidence:** High on the facts.
- **Deal impact:** Valuation, closing (MAE), post-closing. Needs a specific protection.
- **Cross-check:** Litigation: any unsealed qui tam, relator, or related docket. News: reports of a DOJ probe.

#### SEC-013: The 10-K, filed after the CID was received, did not mention it
- **Finding:** Corvane received the CID on February 11, 2026, 22 days before the 10-K was filed on March 5, 2026. The 10-K's legal proceedings and subsequent events note do not mention it. In my files, the first disclosure is the August 5 10-Q. The Q1 2026 10-Q is not in my folder.
- **Evidence:** 10-K Item 3: "We are not aware of any pending government investigation that we expect to be material." Note 15: "identified none requiring disclosure."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 3 and Note 15; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, Part II Item 1
- **Severity:** High
- **Confidence:** High. Dates in primary sources. The 10-K wording is qualified by "expect to be material".
- **Deal impact:** Disclosure, and reliability of management representations.
- **Cross-check:** The Q1 2026 10-Q. News: when the CID became public. Litigation: securities suits.

#### SEC-014: Chief Compliance Officer left in January 2026; the 10-K describes the role in the present tense
- **Finding:** CCO Daniel Pruitt left in January 2026, before the February 11 CID and the March 5 10-K. The 10-K describes the compliance program as "overseen by our Chief Compliance Officer" with no mention of the vacancy. The proxy (April 10) and the 10-Q disclose the departure. The Deputy General Counsel is interim CCO. No reason or separation payment is given. No 8-K on the departure appears in my files.
- **Evidence:** Proxy: "Our Chief Compliance Officer, Daniel Pruitt, left Corvane in January 2026."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_DEF14A_2026_excerpts.md`, "Executive officers"; `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 1 "Compliance program"; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, Part II Item 1A
- **Severity:** Medium
- **Confidence:** High on the facts. Any link to the CID is not stated (inference only).
- **Deal impact:** Disclosure and post-closing compliance.
- **Cross-check:** News: the reason Pruitt left. Litigation: whether Pruitt is a relator or witness.

#### SEC-015: The April cyber 8-K described a "network disruption" that the 10-Q later called ransomware
- **Finding:** The April 27 8-K, filed under Item 8.01 rather than Item 1.05, described a "network disruption". It said there was "no evidence at this time that patient information was exfiltrated" and expected no material impact. The 10-Q calls it a "ransomware attack". It reports notice letters to about 412,300 people in June, class actions and an HHS OCR inquiry, and the guidance cut cites the incident. No amended 8-K appears in my files. The August 5 CEO quote still says "network disruption", on the same day the 10-Q says ransomware.
- **Evidence:** 8-K: "does not currently believe the disruption will have a material impact." 10-Q: "we detected a ransomware attack on our network."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_8-K_2026-04-27_network-disruption.md`, Item 8.01; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, "Cybersecurity incident"; `targets/kestrel/data/sec-filings/CRVD_8-K_2026-08-05_q2-results-guidance.md`, Item 2.02
- **Severity:** High
- **Confidence:** High on the wording. Whether Item 1.05 applied is a legal judgment.
- **Deal impact:** Disclosure, plus regulatory and securities litigation risk.
- **Cross-check:** News: reports of the ransomware group or data leak, and timing. Litigation: class action filing dates and allegations about the 8-K.

#### SEC-016: Financial exposure from the cyber incident is open-ended
- **Finding:** Response costs were US$6.1m in H1 2026, plus about US$4.0m of lost revenue. The cyber insurance limit is US$10.0m. If insurance covers all response costs, US$3.9m of limit is left (inference). There are class actions and an OCR inquiry, with no estimate of loss.
- **Evidence:** "Our cyber insurance policy has a limit of US$10.0 million ... We cannot estimate a range of possible loss."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, "Cybersecurity incident"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing and valuation.
- **Cross-check:** Litigation: number of class actions and claimed damages. News: OCR or state attorney general actions.

#### SEC-017: Final 2027 Medicare rate for OncoTrace code 0419U published but not quantified
- **Finding:** CMS published the final 2027 rate for code 0419U on July 29, 2026, effective January 1, 2027. Corvane does not disclose the rate or its direction, and its guidance excludes it. About 40% of non-Medicare OncoTrace revenue is priced off the Medicare rate. OncoTrace was 44% of clinical testing revenue, or 0.44 x 314.8 = US$138.5m in FY2025.
- **Evidence:** "We are evaluating the effect on future periods and may seek reconsideration." The mention of reconsideration suggests the change is unfavorable (inference).
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, "Reimbursement"; `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 1 and Item 1A; `targets/kestrel/data/sec-filings/CRVD_8-K_2026-08-05_q2-results-guidance.md`, Item 7.01
- **Severity:** High
- **Confidence:** High that the rate exists and was left out. The size of the change is not found in SEC filings.
- **Deal impact:** Valuation. It contradicts the brief's "Medicare rates flat through 2030".
- **Cross-check:** News: the CMS final rate for 0419U and the percent change. Financials: OncoTrace Medicare volume and revenue split.

#### SEC-018: Medicare and rate-linked commercial concentration
- **Finding:** Traditional Medicare was 24.2% of FY2025 revenue (US$104.3m). Commercial contracts that reference the Medicare rate amplify any CMS change.
- **Evidence:** "Medicare (traditional fee-for-service) accounted for 24.2% of our total revenue in FY2025."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 1 "Clinical testing" and "Payer contracts"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation
- **Cross-check:** Financials: revenue by payer.

#### SEC-019: Dated judgment. October 1, 2025 goodwill test is in doubt
- **Finding:** At October 1, 2025, the Clinical testing unit (goodwill US$241.5m) had about 14% headroom. A 10% cut in projected cash flows would "eliminate most of the headroom". The test assumed stable Medicare rates for OncoTrace and 9% growth. Since then, FY2026 Adjusted EBITDA guidance has fallen 24.8%, H1 clinical revenue has fallen 1.9%, and a new 0419U rate has been published. The share price was US$27.80 at the test date and US$18.10 on July 31, 2026 (brief), down 34.9%. The offer of US$24.00 is 13.7% below the test-date price. The 10-Q excerpts contain no interim impairment assessment.
- **Evidence:** "exceeded its carrying value by approximately 14%. Our share price was US$27.80 at the test date."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, "Critical accounting estimates: goodwill"; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, MD&A
- **Severity:** High
- **Confidence:** Medium. The trigger analysis is inference; the inputs are primary.
- **Deal impact:** Disclosure and controls. An impairment is non-cash, but its covenant treatment is unclear (SEC-008).
- **Cross-check:** News and market data: share price after August 5. Financials: Clinical testing projections.

#### SEC-020: Pell Ridge goodwill was not tested
- **Finding:** US$22.3m of goodwill from the May 2025 Pell Ridge acquisition was added after the October 1 test and was not tested. Total goodwill is 241.5 + 57.1 + 22.3 = US$320.9m.
- **Evidence:** "Goodwill of US$22.3 million from the Pell Ridge acquisition was added after the test date and was not tested."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, "Critical accounting estimates: goodwill"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Disclosure
- **Cross-check:** Financials: Pell Ridge results.

#### SEC-021: FY2025 growth includes an acquisition; organic growth is not disclosed
- **Finding:** Pell Ridge, bought in May 2025 for US$31.0m, contributed to FY2025 revenue. Its revenue is not found in SEC filings. The 11.7% growth in the thesis is therefore partly bought, as well as boosted by SEC-001.
- **Evidence:** "the Pell Ridge Pathology laboratory we acquired in May 2025 for US$31.0 million in cash."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 1 "Overview"
- **Severity:** Medium
- **Confidence:** Medium. The contribution is not quantified.
- **Deal impact:** Valuation
- **Cross-check:** Financials: organic growth excluding Pell Ridge and the US$14.2m.

#### SEC-022: Orvia Health Plan (11.3% of revenue) can terminate on a change of control
- **Finding:** Orvia, the largest commercial payer at about US$48.7m (0.113 x 431.0), may terminate on 60 days' notice after a change of control. The agreement otherwise runs to December 31, 2028.
- **Evidence:** "Orvia may terminate the agreement on 60 days' notice if Corvane undergoes a change of control."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 1 "Payer contracts"
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Closing (a consent or waiver should be a condition) and valuation.
- **Cross-check:** Financials: Orvia revenue rank and trend. News: whether Orvia is one of the "two commercial payers" that added prior authorization (SEC-025).

#### SEC-023: Veltrane concentration and right to terminate for convenience
- **Finding:** Veltrane was 11.7% of FY2025 revenue (about US$50.4m), mostly from the ATLAS-3 trial of VLT-220. It can end any work order on 90 days' notice. Veltrane is US$61.0m of the US$231.4m backlog (26.4%). Orvia and Veltrane together are 23.0% of revenue.
- **Evidence:** "allows Veltrane to terminate any work order for convenience on 90 days' notice, paying only for work performed."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 1 "Biopharma services"; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, "Biopharma services"
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation. The brief assumes the Veltrane backlog converts on its historical schedule.
- **Cross-check:** News: ATLAS-3 or VLT-220 trial status, and Veltrane's finances. Financials: Veltrane revenue trend.

#### SEC-024: Backlog is falling, book-to-bill is 0.7, and backlog is not defined
- **Finding:** Backlog fell from US$246.0m to US$231.4m (-US$14.6m, -5.9%) in H1 2026, with book-to-bill of 0.7. This checks out: implied bookings of 0.7 x 48.9 = 34.2, less 48.9 of revenue, gives a change of -14.7. The filings do not define backlog or say whether cancellable work orders are included (not found in SEC filings). That matters because Veltrane can cancel for convenience.
- **Evidence:** "Book-to-bill was 0.7 in the first half of 2026."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, "Biopharma services"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation. This contradicts thesis point 3, "a growing backlog".
- **Cross-check:** Financials: backlog definition, cancellations and conversion history.

#### SEC-025: Claim denials are rising because of payer prior authorization
- **Finding:** The initial denial rate rose to 16.2% in H1 2026 from 13.4% in FY2025 (+2.8 points). The filing attributes this to two unnamed commercial payers adding prior authorization for hereditary cancer panels.
- **Evidence:** "two commercial payers introduced prior authorization for hereditary cancer panels."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, MD&A "Results"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation
- **Cross-check:** News: which payers. Financials: denials by payer.

#### SEC-026: Genaro patent suit seeks an injunction on OncoTrace, with no accrual
- **Finding:** Genaro sued in D. Del. on April 2, 2025, seeking damages and an injunction against OncoTrace's target-capture method. OncoTrace is about US$138.5m of revenue. Claim construction briefing was completed in Q2 2026. No accrual has been recorded and no range of loss is given.
- **Evidence:** "Genaro seeks damages and an injunction ... We have not recorded an accrual."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 3; `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, Part II Item 1
- **Severity:** High
- **Confidence:** High on the facts. The merits are unknown.
- **Deal impact:** Valuation and post-closing. A specific indemnity or escrow should be considered.
- **Cross-check:** Litigation: the docket, claim construction ruling date, trial date and any IPR petitions.

#### SEC-027: Hollis wage case dismissed with prejudice
- **Finding:** The phlebotomist overtime class action was dismissed with prejudice on June 9, 2026.
- **Evidence:** "the court dismissed the case with prejudice."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, Part II Item 1
- **Severity:** Low (closed, mitigating)
- **Confidence:** High
- **Deal impact:** None expected
- **Cross-check:** Litigation: whether an appeal was filed.

#### SEC-028: Helixor supply agreement fixes reagent prices and puts tariffs on the supplier
- **Finding:** Reagent prices are fixed through December 31, 2028, including duties and tariffs, which Helixor bears. This neutralizes tariff risk for most of the forecast period.
- **Evidence:** "The prices are inclusive of all import duties and tariffs, which Helixor bears."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Item 1 "Suppliers"
- **Severity:** Low (neutralized)
- **Confidence:** High
- **Deal impact:** None in the forecast period to 2028. Renewal risk after that.
- **Cross-check:** News: Helixor's financial health and tariff disputes.

#### SEC-029: Sale-leaseback gain correctly excluded from Adjusted EBITDA
- **Finding:** The US$6.8m gain on the September 2025 Charlotte sale-leaseback (US$18.5m to an unrelated REIT, 12-year leaseback at market rent) is excluded from EBITDA and Adjusted EBITDA.
- **Evidence:** "The gain is excluded from EBITDA and Adjusted EBITDA."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Note 7
- **Severity:** Low (neutralized by accounting treatment)
- **Confidence:** High
- **Deal impact:** None. The new rent is a recurring cost.
- **Cross-check:** Financials: confirm the gain is absent from the EBITDA bridge.

#### SEC-030: Related-party HQ lease extended to 2040 at rent 33% above market
- **Finding:** Corvane leases its Raleigh headquarters and main lab from the CEO's family entity. Rent is US$4.8m, with 3.5% annual increases. In November 2025 the Audit Committee extended the lease from 2030 to 2040 at existing rent, despite an appraisal of US$3.6m market rent. The excess is US$1.2m a year (33.3%), or roughly US$18.0m undiscounted over 15 years if the gap stayed flat (inference).
- **Evidence:** "estimated market rent for the property at US$3.6 million a year. The Audit Committee approved the extension at the existing rent."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_DEF14A_2026_excerpts.md`, "Certain relationships and related transactions"; `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, Note 12
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation and post-closing governance. Renegotiate at closing.
- **Cross-check:** News: coverage of the lease. Financials: rent expense.

#### SEC-031: FY2025 bonus paid at 150% only because of the US$14.2m change in estimate
- **Finding:** Executive bonuses are based 100% on Adjusted EBITDA. The Compensation Committee chose not to adjust for the Q4 2025 change in estimate. Without it, Adjusted EBITDA of US$111.1m would have paid about 56.9% rather than 150%, assuming straight-line interpolation (inference): 50% + (1.1 / 8.0) x 50%. The 150% reported is consistent with straight-line interpolation: 100% + (7.3 / 11.0) x 75% = 149.8%. For the CEO, that is about US$0.65m against the US$1.71m paid (about US$1.06m more). The estimate behind the bonus is the one with the material weakness (SEC-002).
- **Evidence:** "The Compensation Committee did not adjust FY2025 Adjusted EBITDA for the change in estimate of implicit price concessions."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_DEF14A_2026_excerpts.md`, "FY2025 annual bonus"
- **Severity:** High
- **Confidence:** High on the facts. The payout without the item is an inference.
- **Deal impact:** Disclosure and governance (incentive to inflate estimates). Post-closing pay design.
- **Cross-check:** News: shareholder or proxy-adviser criticism. Financials: whether the change in estimate was reviewed by the Audit Committee.

#### SEC-032: Single-trigger equity acceleration on change of control
- **Finding:** All of Mr. Ellery's unvested options and RSUs (US$31.4m at US$24.00) vest on the change of control alone. Other officers also have single-trigger acceleration. Total change-in-control benefits are US$56.4m (41.6 + 14.8), or 4.5% of equity value. Single-trigger vesting removes retention value after closing.
- **Evidence:** "Acceleration of all unvested stock options and restricted stock units | Single trigger (change in control alone) | 31.4"
- **Source:** `targets/kestrel/data/sec-filings/CRVD_DEF14A_2026_excerpts.md`, "Change-in-control arrangements"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing retention and the management rollover plan.
- **Cross-check:** Financials: whether the 52.4m diluted shares include these awards.

#### SEC-033: Section 280G excise tax gross-up for the CEO
- **Finding:** Mr. Ellery has a 280G excise tax gross-up estimated at US$3.5m. This is a cash cost to the buyer and is likely not deductible (inference).
- **Evidence:** "Excise tax gross-up (Section 280G) | Change in control | 3.5"
- **Source:** `targets/kestrel/data/sec-filings/CRVD_DEF14A_2026_excerpts.md`, "Change-in-control arrangements"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation (transaction costs). Check whether it is in the US$47.7m of fees.
- **Cross-check:** Financials: transaction cost budget.

#### SEC-034: CEO cash severance and health benefits are double trigger
- **Finding:** CEO severance is 3.0x (950,000 + 1,140,000) = US$6.3m, plus US$0.4m of health benefits. Both are paid only on a change of control followed by termination.
- **Evidence:** "Double trigger (change in control and termination) | 6.3"
- **Source:** `targets/kestrel/data/sec-filings/CRVD_DEF14A_2026_excerpts.md`, "Change-in-control arrangements"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Post-closing, if the CEO is replaced.
- **Cross-check:** None needed.

#### SEC-035: Board structure. Founder CEO is also Chair
- **Finding:** Five of seven directors are independent. The Audit Committee chair is independent. Founder and CEO Martin Ellery is also Chair and is landlord of the HQ (SEC-030).
- **Evidence:** "Seven directors, five of them independent."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_DEF14A_2026_excerpts.md`, "Board of directors"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Governance. A special committee will be needed for the take-private.
- **Cross-check:** News: board changes.

#### SEC-036: No auditor change
- **Finding:** Brannock & Lyle LLP has been the auditor since 2019. No auditor change or reportable event is found in SEC filings. The opinion on the financial statements is not in the excerpts.
- **Evidence:** "Auditor: Brannock & Lyle LLP (auditor since 2019)"
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-K_FY2025_excerpts.md`, header and Item 9A
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Disclosure
- **Cross-check:** News: any auditor resignation after August 2026.

#### SEC-037: H1 2026 results by segment
- **Finding:** H1 2026 revenue fell 0.9% to US$203.4m. Clinical testing fell 1.9%, Lab informatics fell 2.3% (a subscription business), and Biopharma services grew 2.7%. Q2 revenue fell 3.0% to US$100.8m. Implied Q1 was US$102.6m of revenue and US$28.1m of Adjusted EBITDA (54.1 - 26.0).
- **Evidence:** H1 segment table.
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, MD&A "Results"; `targets/kestrel/data/sec-filings/CRVD_8-K_2026-08-05_q2-results-guidance.md`, Item 2.02
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation. This contradicts the thesis of steady growth.
- **Cross-check:** Financials: quarterly segment data and informatics retention.

#### SEC-038: Margins compressed in H1 2026
- **Finding:** Gross margin fell to 38.0% (77.3 / 203.4) from 43.0% (88.2 / 205.2). Operating income fell 77.4% to US$6.0m. This runs against the thesis of margin expansion.
- **Evidence:** "Gross profit | 77.3 | 88.2 | -12.4%"; "Operating income | 6.0 | 26.6 | -77.4%"
- **Source:** `targets/kestrel/data/sec-filings/CRVD_10-Q_Q2-2026_excerpts.md`, MD&A "Results"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation
- **Cross-check:** Financials: cost of revenue detail and the status of the billing system and lab automation.

#### SEC-039: The August 5 earnings 8-K left out key items
- **Finding:** The earnings 8-K mentions none of the following: the DOJ CID, the covenant step-down, the material weakness, or the size of the 0419U rate. It still calls the attack a "network disruption". The 10-Q filed the same day covers all of these except the rate amount.
- **Evidence:** "The quarter was affected by the April network disruption and by slower payer collections."
- **Source:** `targets/kestrel/data/sec-filings/CRVD_8-K_2026-08-05_q2-results-guidance.md`, Items 2.02 and 7.01
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Disclosure
- **Cross-check:** News: how the press reported Q2.

#### SEC-040: No embedded instructions in the source files
- **Finding:** I found no text in the SEC filings that tries to instruct the agents.
- **Evidence:** Not applicable.
- **Source:** All five files in `targets/kestrel/data/sec-filings/`
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** None needed.

### Positive or mitigating points
- **No near-term maturities (SEC-010):** revolver due October 2028, term loan October 2029. The existing debt is repaid at closing (SEC-009).
- **Supplier protection (SEC-028):** Helixor fixes reagent prices and bears tariffs through December 31, 2028.
- **Gain correctly excluded (SEC-029):** the US$6.8m sale-leaseback gain is kept out of Adjusted EBITDA and covenant EBITDA.
- **Case closed (SEC-027):** Hollis was dismissed with prejudice on June 9, 2026.
- **Biopharma still growing (SEC-037):** biopharma revenue grew 2.7% in H1 2026, though book-to-bill is weak.
- **Some pay is double trigger (SEC-034):** the CEO's cash severance and health benefits require termination.
- **Controls remediation under way (SEC-002):** a revenue cycle controller was hired in May 2026.
- **Liquidity (SEC-011):** US$93.8m at June 30, 2026, and net debt ties to the brief.

### Gaps and questions for management
1. Provide the Adjusted EBITDA definition and full reconciliation for FY2025, H1 2026 and LTM. What makes up the US$12.6m increase in add-backs not explained by the cyber costs? (Not found in SEC filings.)
2. Provide the Consolidated Net Leverage Ratio and the covenant EBITDA build at June 30 and September 30, 2026. Has the September 30 certificate been delivered, or a waiver sought? How is a goodwill impairment treated under the definition?
3. What is the final 2027 Medicare rate for 0419U and its percent change? What is the revenue effect, including on commercial contracts that reference the Medicare rate?
4. Why did the 10-K (March 5) not disclose the February 11 CID? Was it in the Q1 2026 10-Q? Is there a related qui tam?
5. Why did the CCO leave? Were any separation or settlement payments made?
6. Provide a roll-forward of the implicit price concession reserve and cohort collection data since Q4 2025. Has any part of the US$14.2m reversed?
7. Has the auditor issued an unqualified opinion on the FY2025 financial statements?
8. Was Item 1.05 considered for the April 18 incident? When was exfiltration confirmed? What are the insurance claim status and remaining limit?
9. What is the backlog definition, and how much is cancellable? What is the current status of the ATLAS-3 trial?
10. Has Orvia indicated whether it will consent to the change of control? Is Orvia one of the two payers that added prior authorization?
11. What did Pell Ridge contribute to FY2025 revenue, and what was organic growth?
12. Will Mr. Ellery agree to bring the HQ lease rent down to market at closing? Was the 2040 extension made with a sale process in mind?
13. Are the single-trigger awards included in the 52.4m diluted shares? Are the 280G gross-up and severance included in the US$47.7m of fees?
14. Prepayment premiums under the existing credit agreement are not found in SEC filings.
