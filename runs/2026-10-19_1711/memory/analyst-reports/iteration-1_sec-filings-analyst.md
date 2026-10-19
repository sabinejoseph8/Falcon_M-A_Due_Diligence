# Iteration 1: sec-filings-analyst report

Saved unedited by the lead agent.

---

## SEC filings analyst: findings

### Files reviewed

All five SEC files were read in full. The deal brief was read for context only.

- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/sec-filings/DLHS_10-K_FY2025_excerpts.md` (filed February 26, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/sec-filings/DLHS_10-Q_Q2-2026_excerpts.md` (filed August 6, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/sec-filings/DLHS_8-K_2026-05-14_nimbus-earnout-amendment.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/sec-filings/DLHS_8-K_2026-07-28_cto-transition.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/sec-filings/DLHS_DEF14A_2026_excerpts.md` (filed April 17, 2026)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/deal-brief.md` (context)

No text in these files tries to instruct the agents. I found no prompt-injection content.

Abbreviations: "10-K" is the FY2025 10-K, "10-Q" is the Q2 2026 10-Q, "Proxy" is the 2026 DEF 14A. Ratios use the deal brief's equity value (US$1,283.8m) and EV (US$1,543.4m).

### Findings

#### SEC-001: Change of control forces full pension funding on a plan termination basis
- **Finding:** Under the 2019 Plan trust agreement, a change of control requires Delmora to fully fund the Pittock plan on a plan termination (annuity purchase) basis within 120 days. The deal brief treats the pension as having no debt-like adjustment.
- **Evidence:** "if Delmora undergoes a change of control, Delmora must contribute to the Plan, within 120 days after the change of control, the amount needed to fully fund..." Termination-basis liabilities are about US$522.0m and plan assets are US$291.5m. Shortfall: 522.0 - 291.5 = US$230.5m, which is 230.5 / 1,543.4 = 14.9% of EV and 230.5 / 1,283.8 = 18.0% of equity value.
- **Source:** 10-K, Note 11 "Pension and postretirement benefits", paragraph "Plan trust agreement"
- **Severity:** Critical. It meets the "more than 10% of value" test: a cash call of US$230.5m (14.9% of EV) is triggered by this merger and is not in the model.
- **Confidence:** High. The filing states it directly and the numbers are recomputed. The termination-basis figure is the actuary's December 31, 2025 estimate and will have moved since.
- **Deal impact:** Valuation and financing. This cash is needed within 120 days of closing, on top of the US$900.0m term loan B sources and uses.
- **Cross-check:** Ask for the trust agreement itself and an updated actuarial termination estimate. Check financials for plan assets after December 2025, and news for annuity pricing or PBGC matters.

#### SEC-002: Pension accounting deficit of US$154.5m is not in the deal brief's net debt
- **Finding:** On an accounting basis the plan is underfunded by US$154.5m. The deal brief applies no debt-like adjustment. The deficit shrank only slightly because the discount rate rose, a judgment made as of December 31, 2025.
- **Evidence:** PBO US$446.0m, assets US$291.5m, deficit (154.5) at FY2025, against (162.0) at FY2024. Discount rate rose from 5.85% to 6.05%. Expected return held at 6.75%. A US$9.5m FY2025 contribution was "voluntary". "We do not expect required minimum contributions before 2029", which rests on the "funding credit balance."
- **Source:** 10-K, Note 11 "Pension and postretirement benefits"
- **Severity:** High. Even without SEC-001 this is debt-like. If SEC-001 applies, this deficit is part of the US$230.5m and should not be counted twice.
- **Confidence:** High. Primary source, numbers recomputed.
- **Deal impact:** Valuation (net debt).
- **Cross-check:** Look for an interim remeasurement in the financials, and check the funding credit balance with the actuary.

#### SEC-003: Nimbus earn-out amended to pay the US$90.0m maximum on a change of control
- **Finding:** On May 12, 2026, two months after the board formed the Strategic Review Committee (March 11, 2026), Delmora amended the Nimbus earn-out. Any change of control now makes the full US$90.0m payable in cash within ten business days, whatever Insights revenue is. The deal brief carries the earn-out at US$8.0m.
- **Evidence:** "due in full at the maximum amount of US$90.0 million, regardless of Insights annual recurring revenue". "Before the Amendment, a Change of Control had no effect." Amount not in the model: 90.0 - 8.0 = US$82.0m, or 82.0 / 1,543.4 = 5.3% of EV.
- **Source:** 8-K May 14, 2026, Item 1.01. 10-Q, Note 9 "Contingent consideration". Proxy, "Certain relationships and related person transactions".
- **Severity:** High. It needs a price adjustment or a specific protection. On its own it is below 10% of value.
- **Confidence:** High. Primary source.
- **Deal impact:** Valuation and closing cash.
- **Cross-check:** Get the full Amendment No. 2. The exhibit was "to be filed", so check whether it was filed with the 10-Q. Check news on the amendment's timing.

#### SEC-004: Nimbus amendment benefits the Chief Data Officer, and the Audit Committee's review is not stated
- **Finding:** Leona Farkas, the Chief Data Officer, is entitled to about 34% of any earn-out, which is about 0.34 x 90.0 = US$30.6m if the acceleration applies. The Proxy says the Audit Committee reviews any amendment to the earn-out terms. The 8-K says only that the full board approved and that Farkas recused herself. The amendment also includes a release of "certain claims relating to the Company's integration of the Nimbus business", and the filings do not describe those claims.
- **Evidence:** "The Audit Committee reviews any amendment to the earn-out terms" (Proxy). "approved by the Company's board of directors on May 12, 2026" (8-K).
- **Source:** Proxy, "Certain relationships and related person transactions". 8-K May 14, 2026, Item 1.01, points 2 and 3 and the approval paragraph.
- **Severity:** Medium
- **Confidence:** High on the facts. It is my interpretation that the Audit Committee review may not have happened.
- **Deal impact:** Disclosure and governance. A fiduciary challenge to the amendment is possible.
- **Cross-check:** Get the Audit Committee minutes for May 2026. Check litigation records for claims by the Nimbus holders that were released.

#### SEC-005: Earn-out fair value kept at US$8.0m because a change of control was "not probable" (dated judgment)
- **Finding:** At June 30, 2026 the company kept the earn-out at US$8.0m and did not reflect the acceleration. It took this view while its own Strategic Review Committee was running a sale process.
- **Evidence:** "we do not consider the events covered by the amendment to be probable." The 10-Q itself describes the strategic review, "including a sale of the company." The fair value was cut from US$14.5m to US$8.0m in FY2025, and the US$6.5m reduction was booked as a gain.
- **Source:** 10-Q, Note 9 "Contingent consideration" and MD&A "Strategic review". 10-K, Note 13.
- **Severity:** Medium
- **Confidence:** High on the facts. It is my interpretation that the judgment is in doubt.
- **Deal impact:** Disclosure and valuation (the carrying value is stale).
- **Cross-check:** Compare news on sale-process timing (Meridale's indication, exclusivity) with the June 30 test date.

#### SEC-006: Calder Institute claims ownership of the AdaptiveComfort patents
- **Finding:** On April 9, 2026, Calder sued Delmora and Dr. Reyes-Barrow, seeking a declaration of ownership and assignment of the AdaptiveComfort patents. The earliest patent application was filed during his Calder fellowship.
- **Evidence:** Earliest provisional application filed "March 6, 2017" (10-K). He was a postdoctoral fellow at Calder "from September 2014 to June 2017", researching "machine learning models of residential heating and cooling" (Proxy). He is the named inventor on all six US patents. "All Delmora thermostats run AdaptiveComfort." Devices revenue was 503.0 / 786.0 = 64.0% of FY2025 revenue. H1 2026 Calder legal fees were US$3.2m. No accrual is disclosed.
- **Source:** 10-Q, Note 12 "Legal proceedings: Calder Institute of Technology". 10-K, Item 1 "AdaptiveComfort technology". Proxy, Proposal 1, director biography.
- **Severity:** Critical. It meets the "stop the deal" test: the claim seeks assignment of the patents behind every thermostat (64.0% of revenue) and the OEM licensing thesis. The filing dates put conception inside the Calder tenure.
- **Confidence:** Medium. The suit and the dates are in primary sources. The merits are an allegation, and Calder's IP policy terms are not in the SEC files.
- **Deal impact:** Closing risk and valuation. It probably needs a special indemnity, an escrow, or a condition tied to resolution.
- **Cross-check:** Litigation records: the complaint, Calder's IP policy, any assignment or invention disclosure Reyes-Barrow signed, and the case schedule.

#### SEC-007: The 10-K's IP ownership statements do not match the 2017 filing date
- **Finding:** The 10-K says AdaptiveComfort has been "refined by our engineering team since our founding in 2018" and that "We believe we own all intellectual property that is material." The same section gives a March 6, 2017 priority date, before Delmora existed. The 10-K does not mention Calder or say how the 2017 rights were assigned to Delmora.
- **Evidence:** The 10-K was filed February 26, 2026 and the Calder suit followed on April 9, 2026. Whether Delmora knew of the claim before filing is not found in SEC filings.
- **Source:** 10-K, Item 1 "AdaptiveComfort technology"
- **Severity:** Medium
- **Confidence:** High on the wording. It is my interpretation that the chain of title is unclear.
- **Deal impact:** Disclosure (accuracy of representations).
- **Cross-check:** USPTO assignment records. Any demand letter from Calder dated before February 2026 (litigation or news).

#### SEC-008: Co-founder CTO and sole inventor leaves while he is a co-defendant in the Calder suit
- **Finding:** Dr. Reyes-Barrow notified the company on July 27, 2026, 109 days after the Calder suit, that he would step down as CTO and director effective September 30, 2026. The 8-K does not mention Calder. His unvested equity is forfeited, so he gives up change-of-control vesting. His consulting agreement can be ended on 30 days' notice.
- **Evidence:** "not the result of any disagreement with the Company." Consulting fee is US$40,000 per month from October 1, 2026 to March 31, 2027 (6 x 0.04 = US$0.24m). He holds 1.6m shares (3.1%). The interim CTO is Tobias Lindqvist.
- **Source:** 8-K July 28, 2026, Item 5.02. 10-Q, Note 15 "Subsequent events". Proxy, "Security ownership".
- **Severity:** High. The Calder defense and the technology depend on him. A cooperation agreement is needed.
- **Confidence:** High on the facts. The link to Calder is my inference.
- **Deal impact:** Post-closing (technology leadership) and closing risk (litigation cooperation).
- **Cross-check:** News on the reasons for his departure and his next role. Check whether he joined Calder or a competitor. Check whether the consulting agreement includes litigation cooperation (Exhibit 10.1).

#### SEC-009: IRS proposes US$121.1m of tax and penalty on the 2019 Irish IP transfer
- **Finding:** A May 2026 NOPA values the AdaptiveComfort rights transferred to Ireland at US$476.0m instead of US$64.0m. The recorded uncertain tax position liability is only US$14.2m.
- **Evidence:** Adjustment US$412.0m. Tax about US$86.5m, plus a 40% penalty of about US$34.6m, plus interest: 86.5 + 34.6 = US$121.1m before interest. That is 121.1 / 1,543.4 = 7.8% of EV and 121.1 / 1,283.8 = 9.4% of equity. Unreserved: 121.1 - 14.2 = US$106.9m (if the full UTP balance relates to this, which is not stated). "more likely than not that our position will be sustained."
- **Source:** 10-Q, Note 10 "Income taxes". 10-K, Item 1 (2019 transfer) and Note 12.
- **Severity:** High. Interest for 2019 to 2021 could take the total above 10% of equity value, but the filings give no interest figure, so I cannot show the Critical test.
- **Confidence:** High. Primary source, numbers recomputed.
- **Deal impact:** Valuation. Needs a tax indemnity or escrow. It also conflicts with the deal brief's "no exposure assumed beyond recorded reserves."
- **Cross-check:** Appeals status and the interest estimate. Calder (SEC-006) also disputes ownership of the same rights.

#### SEC-010: The 10-K's 12-month tax judgment was overtaken within three months (dated judgment)
- **Finding:** On February 26, 2026 the company said it did not expect a significant change in uncertain tax positions within 12 months. In May 2026 the NOPA proposed US$121.1m. The UTP balance moved only from US$13.8m to US$14.2m.
- **Evidence:** "do not expect a significant change in our uncertain tax positions in the next 12 months."
- **Source:** 10-K, Note 12. 10-Q, Note 10.
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Disclosure
- **Cross-check:** When did the IRS first signal the valuation challenge, for example through IDRs or a draft NOPA before February 2026?

#### SEC-011: Aura field action reserve of US$6.0m covers only kits, and the CPSC may seek more
- **Finding:** The reserve covers mailing battery isolation kits for 1.62 million units. It does not cover replacement, a recall, injuries or the class action. The company "cannot currently estimate any additional costs."
- **Evidence:** 1.62m x US$3.70 = US$5.99m, or about 6.0. Reserve left at June 30 is US$5.1m. There have been 214 overheating reports, 37 fires and 9 burn injuries. "The CPSC staff may seek a different or broader remedy."
- **Source:** 10-Q, Note 6 "Product field action"
- **Severity:** High. The deal brief calls the matter "contained" and "fully reserved".
- **Confidence:** High. Primary source, recomputed.
- **Deal impact:** Valuation and post-closing. Needs an indemnity or escrow, and possibly an MAE definition point.
- **Cross-check:** CPSC records and news (recall announcements, incident counts after June 30). Litigation records for injury suits.

#### SEC-012: Product liability insurance halved and now excludes the Aura battery units
- **Finding:** At the March 1, 2026 renewal, the per-occurrence limit fell from US$50.0m to US$25.0m. Lithium battery thermal events in products made before January 1, 2024 are now excluded. That exclusion covers the Aura AT-200/AT-210 units made from 2021 to 2023.
- **Evidence:** "excludes claims arising from lithium battery thermal events in products manufactured before January 1, 2024."
- **Source:** 10-Q, Note 7 "Insurance". Note 6 gives the manufacturing years.
- **Severity:** High
- **Confidence:** High. Primary source. That the exclusion matches the Aura cohort is a direct comparison of two notes.
- **Deal impact:** Valuation and post-closing. Aura claims are uninsured, so a specific indemnity is needed.
- **Cross-check:** The insurance policy and broker correspondence. Did insurers know of the battery reports before March 1?

#### SEC-013: Aura putative class action, with no accrual disclosed
- **Finding:** A putative class action about the field-action Aura units was filed on July 15, 2026 in the Northern District of Illinois. The filings give no accrual or estimate.
- **Evidence:** "a putative class action was filed against us..." Note 15 records only the filing.
- **Source:** 10-Q, Note 12 "Legal proceedings: Aura class action" and Note 15
- **Severity:** Medium. Read with SEC-011 and SEC-012, the uninsured exposure is larger.
- **Confidence:** High on the existence of the case. The claim is an allegation.
- **Deal impact:** Post-closing liability
- **Cross-check:** Litigation records: class definition, damages sought, consolidation with other cases.

#### SEC-014: Aura described as "not material" in the 10-K, then a 1.62m-unit field action eight weeks later
- **Finding:** The 10-K, filed February 26, 2026, described "a limited number of consumer reports" and said the matter was not material. The insurance exclusion came on March 1, 2026 and the field action on April 21, 2026.
- **Evidence:** "We do not believe this matter is material" (10-K). Field action on April 21, 2026 (10-Q).
- **Source:** 10-K, Item 3 "Aura thermostat battery reports". 10-Q, Notes 6 and 7.
- **Severity:** Medium
- **Confidence:** High on the wording. Any inference about what management knew is mine.
- **Deal impact:** Disclosure and representations
- **Cross-check:** How many reports existed at February 26, 2026 (CPSC or news). When the engineering firm was engaged.

#### SEC-015: Warranty accrual rate cut in Q4 2025 while the Aura battery investigation was open
- **Finding:** Warranty expense fell from US$15.0m to US$9.6m after the company cut the accrual rate on new sales in Q4 2025. Claims paid exceeded the amount accrued.
- **Evidence:** "we reduced the accrual rate applied to new device sales". Expense change: 15.0 - 9.6 = US$5.4m, or 5.4 / 133.7 = 4.0% of FY2025 Adjusted EBITDA. Claims paid were 12.5 against 9.6 accrued, and the balance fell from 15.1 to 12.2. The cut was a stated driver of gross margin rising to 42.5%.
- **Source:** 10-K, MD&A "Warranty" and "FY2025 overview", and Note 9
- **Severity:** Medium
- **Confidence:** High. Primary source, recomputed.
- **Deal impact:** Valuation (quality of earnings). It also helped the FY2025 bonus metrics (see SEC-038).
- **Cross-check:** Quarterly warranty claims in the financials. Whether the Aura costs ran through warranty or G&A (the 10-Q books the US$6.0m in G&A).

#### SEC-016: Peso hedging stopped in Q3 2025, then the peso strengthened and margins fell
- **Finding:** The company dropped its peso hedges in Q3 2025. In H1 2026 the peso strengthened from 19.4 to 17.2 per US dollar and gross margin fell from 42.3% to 39.4%. The deal brief assumes 42% from 2027.
- **Evidence:** "we discontinued our program of hedging". The company's sensitivity is US$28m of cost per 10% peso strengthening. Move: 19.4 / 17.2 - 1 = 12.8%, so about US$35.8m a year (inference, linear). H1 operating income fell from 35.3 to 18.2 and net income from 19.3 to 4.8.
- **Source:** 10-K, MD&A "Foreign currency". 10-Q, MD&A "Results" and Item 1.
- **Severity:** High
- **Confidence:** High on the facts. The annualized figure is a projection.
- **Deal impact:** Valuation (margin assumption and earnings base)
- **Cross-check:** Current peso rate in news or market data. Hedging status after June 30. Monthly gross margin in the financials.

#### SEC-017: H1 2026 operating cash flow is inflated by US$98.0m of working capital timing
- **Finding:** Of the US$134.1m H1 operating cash flow, US$64.0m came from stretching supplier terms from 60 to 120 days and US$34.0m from a WSEA advance. Without them, cash flow is in line with H1 2025. Cash of US$160.4m, and so the brief's net debt of US$259.6m, includes this timing.
- **Evidence:** "US$64.0 million increase in accounts payable" and "US$34.0 million advance payment received from WSEA". 134.1 - 64.0 - 34.0 = US$36.1m, against US$34.9m in H1 2025. Net debt adjusted for this (inference): 420.0 - (160.4 - 98.0) = US$357.6m, which is US$98.0m higher (6.3% of EV).
- **Source:** 10-Q, MD&A "Liquidity and cash flow" and Item 1 balance sheet
- **Severity:** High
- **Confidence:** High. Primary source, recomputed.
- **Deal impact:** Valuation. Needs a working capital peg and a normalized net debt figure.
- **Cross-check:** Monthly AP and deferred revenue in the financials. Whether the 120-day terms continue.

#### SEC-018: Longer payment terms were agreed with a 49%-owned related supplier whose loan Delmora guarantees
- **Finding:** The "main contract manufacturer" is Ensamble Norte (the 10-K says most devices are assembled there and commitments are mainly with it). Delmora owns 49% of Ensamble Norte and guarantees US$64.0m of its debt. Doubling Delmora's payment terms moves liquidity pressure onto the guaranteed entity.
- **Evidence:** "longer payment terms (120 days, previously 60 days) agreed with our main contract manufacturer from April 1, 2026."
- **Source:** 10-Q, MD&A "Liquidity and cash flow". 10-K, Item 1 "Manufacturing and suppliers" and Note 14.
- **Severity:** Medium
- **Confidence:** Medium. That the counterparty is Ensamble Norte is inferred from the 10-K. The 10-Q does not name it.
- **Deal impact:** Valuation and post-closing
- **Cross-check:** Ensamble Norte financials and its compliance with its bank covenants.

#### SEC-019: Off-balance-sheet guarantee of US$64.0m of Ensamble Norte debt
- **Finding:** Delmora guarantees US$64.0m of Ensamble Norte's term loan, which matures in 2028. Only US$0.6m is recorded.
- **Evidence:** "Our maximum potential payment is US$64.0 million plus accrued interest and costs." That is 64.0 / 1,543.4 = 4.1% of EV.
- **Source:** 10-K, Note 14. 10-Q, Note 12.
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation (contingent debt-like item). Check whether the guarantee has change-of-control terms (not found in SEC filings).
- **Cross-check:** The guarantee agreement and Ensamble Norte's lender terms.

#### SEC-020: Non-cancellable purchase commitments of US$118.0m
- **Finding:** Ordinary-course commitments, mainly with Ensamble Norte.
- **Evidence:** "non-cancellable purchase commitments of US$118.0 million."
- **Source:** 10-K, Note 14
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Post-closing
- **Cross-check:** Inventory levels compared with demand in the financials.

#### SEC-021: Director's past link to Ensamble Norte's majority owner
- **Finding:** Howard Lindgren sat on the board of Grupo Industrial Arceo (51% owner of Ensamble Norte) until 2022. The board found him independent. He sits on the Strategic Review and Compensation committees.
- **Evidence:** "this past relationship does not affect Howard Lindgren's independence."
- **Source:** Proxy, "Certain relationships and related person transactions" and Proposal 1
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Disclosure
- **Cross-check:** None needed beyond confirming any current ties.

#### SEC-022: Marlow TCE cleanup accrued at the low end, with US$62.0m unaccrued
- **Finding:** The Ohio EPA consent order cost range is US$9.0m to US$71.0m and only US$9.0m is accrued. The 10-Q excerpt gives no update.
- **Evidence:** "we have accrued the low end of the range, US$9.0 million." Unaccrued: 71.0 - 9.0 = US$62.0m, or 4.0% of EV. The swing factor is groundwater moving "beyond the site boundary."
- **Source:** 10-K, Note 15 "Environmental matters" and Item 3
- **Severity:** High. Needs an environmental indemnity or escrow.
- **Confidence:** High
- **Deal impact:** Valuation and post-closing
- **Cross-check:** Ohio EPA records and news on off-site monitoring results.

#### SEC-023: European Commission Statement of Objections on cross-border sales restrictions
- **Finding:** The EC inspected in November 2025 and sent a Statement of Objections on June 30, 2026, alleging restrictions on EEA distributor sales from 2019 to 2025. No accrual is recorded.
- **Evidence:** "fines of up to 10% of worldwide annual turnover." On FY2025 revenue the cap is 0.10 x 786.0 = US$78.6m (5.1% of EV). The 10-K had said "It is too early to assess the outcome."
- **Source:** 10-Q, Note 12 "European Commission". 10-K, Item 3.
- **Severity:** High. It contradicts the deal brief's view that litigation is immaterial, and needs an indemnity.
- **Confidence:** High on the facts. The fine is an upper bound, not an estimate.
- **Deal impact:** Valuation, post-closing, and EU distributor model changes
- **Cross-check:** EC case records, the response deadline, oral hearing date and news.

#### SEC-024: BIS export subpoena and shipments halted to the UAE distributor behind the international growth thesis
- **Finding:** BIS subpoenaed documents on June 24, 2026 about shipments to a UAE distributor, and Delmora suspended shipments to that distributor in June. The 10-K names Gulf Horizon Trading FZE (Dubai) as the main driver of international distributor revenue.
- **Evidence:** International distributor revenue rose from US$6.0m to US$41.2m, which is 41.2 / 786.0 = 5.2% of FY2025 revenue. Devices include "cellular and Wi-Fi modules and encryption functions." The 10-Q does not name the distributor.
- **Source:** 10-Q, Note 12 "Bureau of Industry and Security". 10-K, MD&A "International" and Item 1A.
- **Severity:** High. Thesis 4 is at risk, and possible penalties or loss of export privileges need a closing protection.
- **Confidence:** High on the subpoena. That the distributor is Gulf Horizon is a Medium inference.
- **Deal impact:** Valuation, closing risk (CFIUS and regulatory), post-closing
- **Cross-check:** News and BIS records. Gulf Horizon's revenue rank in revenue_by_customer.csv. Possible diversion to sanctioned destinations.

#### SEC-025: The 10-K said "not aware of any violations" while the Audit Committee was running a trade compliance review
- **Finding:** The Audit Committee held special meetings on January 20, February 9 and February 23, 2026 on distributor trade compliance, all before the 10-K was filed on February 26. The 10-K said the company was not aware of violations, did not mention the review, and reported no subsequent events. The review first appears in the Proxy (April 17, 2026).
- **Evidence:** "We are not aware of any violations of export control or sanctions laws" (10-K). There were five special meetings from January to April 2026, and "The review is ongoing" (Proxy).
- **Source:** 10-K, Item 1A and Note 17. Proxy, "Board meetings and committees: Audit Committee".
- **Severity:** High. Disclosure timing matters for the accuracy of representations and for a possible voluntary self-disclosure.
- **Confidence:** High on the dates. Any inference about what management knew is mine.
- **Deal impact:** Disclosure and closing risk
- **Cross-check:** Audit Committee minutes, outside counsel's findings, and any voluntary self-disclosure filed with BIS or OFAC.

#### SEC-026: Insights consent mechanism may breach the 2022 FTC Order
- **Finding:** The FTC Order requires "affirmative express consent" before sharing covered household data beyond the purposes disclosed when it was collected. Insights enrolls Delmora Care subscribers by default when they accept updated terms, with opt-out only. In Q1 2026 the product expanded to "household-level occupancy and comfort indices, aggregated at the ZIP+4 level", updated daily, and is shared with insurance and real-estate partners.
- **Evidence:** "enrolled in Insights when they accept the updated Delmora Care terms of service. Customers may opt out" (10-K). Covered information includes "occupancy-sensor data linked or reasonably linkable to a household" (10-K). Partners include Bellmark Mutual Insurance (10-Q). Enrolled households rose from 2.1m to 2.3m. The deal brief puts about US$310m of EV on Insights: 310 / 1,543.4 = 20.1% of EV.
- **Source:** 10-K, Item 1 "Delmora Insights" and Item 1A (FTC risk factor). 10-Q, Note 3 "Revenue".
- **Severity:** Critical. It meets the "more than 10% of value" test: the data use supporting about US$310m (20.1% of EV) depends on consent that, on the company's own description, is opt-out. The Order also allows per-violation civil penalties.
- **Confidence:** Medium. The facts are in primary sources. Whether ZIP+4 indices are "reasonably linkable" and whether the updated terms count as express consent is a legal judgment.
- **Deal impact:** Valuation (Insights value) and post-closing (FTC penalties)
- **Cross-check:** The consent screens and terms of service, the biennial privacy assessments, any FTC inquiry (news or regulatory records), and Bellmark's use of the data.

#### SEC-027: Insights revenue is well behind the earn-out and plan ramp
- **Finding:** Insights revenue was US$3.1m in FY2025 and US$11.8m in H1 2026. Management cut the earn-out fair value because of a "slower expected ramp".
- **Evidence:** H1 run rate 11.8 x 2 = US$23.6m (projection), against the earn-out ARR threshold of US$40.0m at December 2027 and the deal brief's US$60.0m by 2028. "reflecting a slower expected ramp of Insights."
- **Source:** 10-Q, Note 3. 10-K, Item 1 and Note 13.
- **Severity:** Medium
- **Confidence:** High on the figures. The run rate is a projection.
- **Deal impact:** Valuation (Insights thesis)
- **Cross-check:** Monthly Insights revenue and contract pipeline in the financials.

#### SEC-028: Largest customer WSEA contract expires December 31, 2026, before closing, and the rebid is undecided
- **Finding:** The WSEA contract ends December 31, 2026. WSEA issued an RFP in February 2026 and Delmora bid in April. Management "expect[s] to be selected." The award is not disclosed. The 10-K risk factor warns of reliance on a few competitively procured contracts.
- **Evidence:** "We expect to be selected and to continue serving WSEA after 2026." WSEA revenue amount: not found in SEC filings. Utility Programs H1 2026 revenue was US$72.0m.
- **Source:** 10-Q, MD&A "Utility Programs". 10-K, Item 1A.
- **Severity:** High. The planned Q1 2027 closing is after expiry, and the deal brief assumes renewal on similar terms.
- **Confidence:** High on the facts. The outcome is unknown.
- **Deal impact:** Valuation and closing condition (consider a renewal condition)
- **Cross-check:** WSEA procurement records and news on the award. WSEA's rank and revenue in revenue_by_customer.csv.

#### SEC-029: WSEA advance correctly held as a liability, not revenue
- **Finding:** The US$34.0m WSEA advance sits in "Utility program customer prepayments", which rose from US$7.0m to US$41.0m. It is not booked as revenue. The accounting looks appropriate. The cash effect is covered in SEC-017.
- **Evidence:** "advance payment received from WSEA in June 2026 for second-half 2026 program incentives."
- **Source:** 10-Q, Item 1 balance sheet and MD&A "Liquidity and cash flow"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Disclosure
- **Cross-check:** Revenue recognition timing in the H2 2026 financials.

#### SEC-030: Reno collective bargaining agreement expired September 30, 2026
- **Finding:** The CBA covering about 405 Reno employees expired on September 30, 2026. Negotiations began in July 2026. The outcome is not found in SEC filings.
- **Evidence:** "expires on September 30, 2026. Negotiations with Local 88 began in July 2026."
- **Source:** 10-Q, MD&A "Labor". 10-K, Item 1 "Human capital" and Item 1A.
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing (distribution disruption)
- **Cross-check:** News on any strike or new agreement.

#### SEC-031: DOE connected standby rule; compliance stated only against the proposed limits
- **Finding:** The 10-K said all models, including legacy Gen 3 units, meet the "proposed limits" for a rule expected in May 2026. The 10-Q excerpt does not say whether the rule was finalized or whether the models comply with it.
- **Evidence:** "meet the proposed limits."
- **Source:** 10-K, Item 1 "Regulation"
- **Severity:** Low
- **Confidence:** Medium. The status after May 2026 is not in the SEC files.
- **Deal impact:** Post-closing
- **Cross-check:** News and DOE records for the final rule and any differences from the proposal.

#### SEC-032: Open source copyleft risk factor
- **Finding:** This is standard risk factor language. No specific non-compliance is disclosed.
- **Evidence:** "We believe we comply with the licenses that apply to us."
- **Source:** 10-K, Item 1A
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Post-closing (OEM licensing diligence)
- **Cross-check:** A code scan in technical diligence. Any GPL enforcement claims in litigation or news.

#### SEC-033: Sales tax voluntary disclosure agreements, US$1.4m accrued
- **Finding:** Delmora entered VDAs with six states for sales tax not collected on Delmora Care subscriptions from 2021 to 2025, and accrued US$1.4m.
- **Evidence:** "We accrued US$1.4 million for this matter in the second quarter."
- **Source:** 10-Q, Note 10 "Sales taxes"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (minor)
- **Cross-check:** Whether other states are exposed.

#### SEC-034: Brennan Sales Group suit dismissed with prejudice
- **Finding:** The US$3.2m commission claim was dismissed with prejudice on January 22, 2026. The matter is closed.
- **Evidence:** "The court dismissed the case with prejudice on January 22, 2026."
- **Source:** 10-K, Item 3
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** Confirm in court records that no appeal was filed.

#### SEC-035: FY2023 warehouse restructuring completed
- **Finding:** The US$6.8m program was completed in December 2023 and no further costs are expected.
- **Evidence:** "completed in December 2023 and no further costs are expected."
- **Source:** 10-K, MD&A "FY2023 restructuring"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None. The financial analyst should check that no restructuring add-back appears in FY2025 or 2026 Adjusted EBITDA.
- **Cross-check:** The Adjusted EBITDA bridge in the financials.

#### SEC-036: Clean auditor opinion and no ICFR changes
- **Finding:** Pellbrook & Stroud LLP, auditor since 2018, gave unqualified opinions on the FY2025 financial statements and on ICFR. The 10-Q reports no material ICFR changes. There is no auditor change or material weakness, and none of the 8-Ks is an Item 4.01 or 4.02 filing. Fees: audit US$2.9m, tax US$0.3m.
- **Evidence:** "issued an unqualified opinion on our FY2025 financial statements and on the effectiveness of our internal control."
- **Source:** 10-K, Item 8. 10-Q, Item 4. Proxy, Proposal 2.
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Positive
- **Cross-check:** Whether the auditor raised critical audit matters on the pension, the earn-out or the warranty (not in the excerpts).

#### SEC-037: Change-of-control severance is double-trigger, estimated at US$21.6m at US$18.70
- **Finding:** NEO severance requires a termination within 24 months after a change of control (double-trigger). The multiples are 2.5x for the CEO and 1.5x for other NEOs, with full equity vesting. The total will be higher at US$24.50 than at the US$18.70 basis. No single-trigger vesting is disclosed.
- **Evidence:** "estimated total for all named executive officers, at a share price of US$18.70, is US$21.6 million." 21.6 / 1,543.4 = 1.4% of EV.
- **Source:** Proxy, "Change-of-control severance"
- **Severity:** Medium
- **Confidence:** High on the terms. The figure at US$24.50 is not computed in the Proxy.
- **Deal impact:** Valuation (transaction costs) and retention planning
- **Cross-check:** Recompute at US$24.50 with the equity schedules from the financials.

#### SEC-038: FY2025 bonus paid at 112% of target on metrics helped by accounting judgments
- **Finding:** The FY2025 bonus weighted revenue at 40% and Adjusted EBITDA at 40%. FY2025 results were helped by the Q4 warranty accrual cut (US$5.4m lower expense, SEC-015). FY2025 other income included a US$6.5m earn-out gain, but whether that gain counts in Adjusted EBITDA is not found in SEC filings.
- **Evidence:** "The plan paid out at 112% of target."
- **Source:** Proxy, "Executive compensation". 10-K, MD&A "Warranty" and Note 13.
- **Severity:** Low
- **Confidence:** Medium. The link to the payout is my inference.
- **Deal impact:** Disclosure and governance
- **Cross-check:** The bonus scorecard and Adjusted EBITDA definition.

#### SEC-039: CFO 10b5-1 plan adopted days before the EC inspections
- **Finding:** CFO Martin Okafor adopted a plan on November 12, 2025 to sell up to 120,000 shares from February 15, 2026 to December 31, 2026. That was six days before the EC dawn raids (November 18 and 19, 2025) and before the Audit Committee trade review began. The 10-Q reports no plan adoptions or terminations in Q2.
- **Evidence:** Adoption on November 12, 2025. First possible sale on February 15, 2026, 95 days later.
- **Source:** Proxy, "Rule 10b5-1 trading plans". 10-K, Item 3. 10-Q, Part II Item 5.
- **Severity:** Medium
- **Confidence:** High on the dates. Any suggestion of improper timing is speculation.
- **Deal impact:** Disclosure and reputational
- **Cross-check:** Form 4 filings and news on executive sales.

#### SEC-040: Existing term loan matures June 2029; covenant definitions not disclosed
- **Finding:** The term loan was US$440.0m at December 31, 2025 and US$420.0m at June 30, 2026 after a US$20.0m repayment. It matures June 2029, and the US$150.0m revolver is undrawn. The company reports covenant compliance "with substantial headroom." Covenant definitions, test dates and change-of-control provisions are not found in SEC filings. The deal plans to refinance with a US$900.0m term loan B.
- **Evidence:** "term loan maturing in June 2029." "We were in compliance with all debt covenants with substantial headroom."
- **Source:** 10-K, MD&A "Liquidity". 10-Q, Item 1 and MD&A "Liquidity and cash flow".
- **Severity:** Low. It is expected to be refinanced at closing and no default is disclosed.
- **Confidence:** High on the amounts. The terms are not available.
- **Deal impact:** Closing mechanics (payoff). New leverage is 900.0 / 130.4 = 6.9x per the brief, before any of the adjustments above.
- **Cross-check:** The credit agreement (change-of-control default, prepayment premium) and the financial analyst's covenant model.

#### SEC-041: No Adjusted EBITDA reconciliation or definition in the SEC excerpts
- **Finding:** FY2025 Adjusted EBITDA was US$133.7m against LTM Q2 2026 of US$130.4m in the brief. The definition and add-backs are not found in SEC filings. Items whose treatment needs confirming: the US$6.0m Aura reserve and US$3.2m Calder legal fees (both in H1 2026 G&A), the US$6.5m FY2025 earn-out gain, the warranty accrual change and the US$1.4m sales tax accrual.
- **Evidence:** "Adjusted EBITDA (a non-GAAP measure) was US$133.7 million."
- **Source:** 10-K, MD&A "FY2025 overview". 10-Q, MD&A "Results".
- **Severity:** Medium
- **Confidence:** High that the reconciliation is missing from these files.
- **Deal impact:** Valuation (quality of earnings)
- **Cross-check:** The financial analyst's Adjusted EBITDA bridge and any change in definition between periods.

#### SEC-042: Revenue recognition policies not in the excerpts
- **Finding:** The excerpts disclose no segment revenue recognition policy, no bill-and-hold, no distributor sell-in or sell-through terms, and no multiple-element allocation (device plus Care subscription). There is also no separate Insights policy. A fourth "Insights" segment is not reported. Insights sits inside Subscriptions & Services.
- **Evidence:** Not found in SEC filings. The segment table lists three segments.
- **Source:** 10-K, Item 1 segment table. 10-Q, Note 3.
- **Severity:** Medium (gap)
- **Confidence:** High that it is absent
- **Deal impact:** Valuation (quality of revenue, especially the jump in Gulf Horizon distributor revenue)
- **Cross-check:** Distributor contracts, returns and rights of return, and quarter-end shipment patterns to Gulf Horizon in the financials.

#### SEC-043: Strategic review and shareholder base
- **Finding:** The Strategic Review Committee was formed March 11, 2026 (chaired by Gregory Tamsin) with a financial adviser. Major holders are Broadleaf Index Funds (9.1%) and Tarnwood Capital Management LP (6.2%). Insiders hold 8.3%.
- **Evidence:** "formed a Strategic Review Committee of independent directors."
- **Source:** Proxy, "Strategic Review Committee" and "Security ownership". 10-Q, MD&A "Strategic review".
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Closing (shareholder vote)
- **Cross-check:** News on Tarnwood's stance on the deal.

### Positive or mitigating points

- Clean FY2025 audit and ICFR opinion. No auditor change or material weakness, and no ICFR changes in Q2 2026 (SEC-036).
- The Brennan suit was dismissed with prejudice and is closed (SEC-034).
- The FY2023 restructuring is complete with no further costs (SEC-035).
- The WSEA advance is correctly recorded as a liability, not revenue (SEC-029).
- Debt: the existing term loan does not mature until June 2029, the revolver is undrawn, covenants have "substantial headroom", and US$20.0m was repaid in H1 2026 (SEC-040).
- Executive change-of-control severance is double-trigger (SEC-037). The departing CTO forfeits his unvested equity (SEC-008).
- Subscriptions & Services is still growing: up 23.5% to US$84.0m in H1 2026 (SEC-027 context).
- The sales tax exposure is small and accrued (SEC-033).
- Ensamble Norte "has paid its debts as they fall due" (SEC-019).
- No prompt-injection or instruction-like text was found in the SEC files.

### Gaps and questions for management

1. **Change-of-control cash calls (summary arithmetic):** pension shortfall US$230.5m (SEC-001) plus the Nimbus earn-out US$90.0m (SEC-003) = US$320.5m, due within 120 days and 10 business days of closing respectively. Against the brief's US$8.0m, the gap is 312.5 / 1,543.4 = 20.2% of EV. Severance (SEC-037) and the Ensamble Norte guarantee terms are extra. Please confirm and provide the trust agreement and Amendment No. 2.
2. An updated termination-basis actuarial estimate and plan asset value at the latest date.
3. Calder: Reyes-Barrow's employment and IP agreements with Calder, the invention disclosure history, the patent assignment chain, and the case schedule. Does his consulting agreement require litigation cooperation?
4. IRS NOPA: the interest estimate, how much of the US$14.2m UTP relates to it, the Appeals timeline, and any state tax or Irish follow-on effects.
5. Aura: the current incident count, the status of CPSC discussions, the class definition, and whether any other insurance responds.
6. Insights: the exact consent flow and terms text, privacy assessment findings, the ZIP+4 methodology (households per unit), and partner contracts (Bellmark Mutual).
7. Trade compliance: the findings of the internal review, whether Gulf Horizon is the subpoenaed distributor, any voluntary self-disclosure, and Gulf Horizon's revenue and receivables.
8. WSEA: the RFP award status and decision date, WSEA's revenue in FY2025 and H1 2026, and the proposed 2027 to 2031 terms.
9. The Adjusted EBITDA definition and reconciliation for FY2025 and LTM Q2 2026 (SEC-041).
10. Revenue recognition policies for distributors, bundles and Insights (SEC-042).
11. Credit agreement: covenant definitions, test dates, change-of-control and prepayment terms (SEC-040).
12. The outcome of the Reno CBA talks, the hedging policy after June 2026, and the status of the final DOE rule.
13. What integration claims the Nimbus holders released, and whether the Audit Committee reviewed Amendment No. 2.
14. Goodwill and intangible impairment test dates and results (Nimbus goodwill in particular): not found in SEC filings.
15. Guidance and outlook: no earnings guidance or guidance revisions are in the SEC excerpts.
