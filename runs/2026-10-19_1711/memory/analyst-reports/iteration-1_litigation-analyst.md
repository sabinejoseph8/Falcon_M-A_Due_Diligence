# Iteration 1: litigation-analyst report

Saved unedited by the lead agent.

---

## Litigation analyst: findings

### Files reviewed

- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/deal-brief.md` (context only)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/litigation/docket_index.csv` (7 matters)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/litigation/LIT-001_aura-battery-class-action.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/litigation/LIT-002_calder-ip-ownership.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/litigation/LIT-003_colorado-insights-privacy.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/heron/data/litigation/LIT-004_marlow-groundwater.md`

LIT-005, LIT-006 and LIT-007 have no detail file. For those three I used only their docket index row. No source file contained text that tries to instruct the agents.

**Finding IDs.** LIT-001 to LIT-007 use the same numbers as the docket case IDs. LIT-008 to LIT-014 are separate topics that come out of those matters.

### Matter summary table

| Case ID | Case | Posture | Claimed / exposure | Next date | Severity |
|---|---|---|---|---|---|
| LIT-001 | In re Delmora Aura Thermostat Battery Litigation (N.D. Ill.) | Pending. Consolidated 2026-09-02. Motion to dismiss fully briefed | No total stated. Seeks a full refund or replacement for about 1.62m units, plus property damage and punitive damages | MTD hearing 2026-11-18 | High |
| LIT-002 | Calder Institute of Technology v. Delmora and Reyes-Barrow (Mass. Super. Ct.) | Discovery. Limitations defense denied 2026-07-30 | Ownership of 6 AdaptiveComfort patents, plus a 4% royalty on thermostat net sales since 2019 | Reyes-Barrow deposition 2026-10-28. Discovery closes 2026-11-20. SJ motions 2026-12-11. Trial 2027-02-08 | Critical |
| LIT-003 | State of Colorado ex rel. AG v. Delmora (Denver Dist. Ct.) | Answer not yet filed | Injunction, data deletion, penalties up to US$20,000 per violation, disgorgement | Answer due 2026-10-27 | High |
| LIT-004 | Pruett et al. v. Delmora and Pittock Heating (Harlan County, Ohio) | Pending. Defendants appeared 2026-10-02 | US$45.0m, plus medical monitoring and punitive damages | CMC 2026-11-05 | High |
| LIT-005 | European Commission Case AT.40977 (online sales restrictions) | Statement of Objections issued 2026-06-30 | Not stated | Reply to SO due 2026-10-30 | Medium |
| LIT-006 | Open Firmware Conservancy v. Delmora (N.D. Cal.) | Pending | Not stated | Initial CMC 2026-12-03 | Medium |
| LIT-007 | Brennan Sales Group v. Delmora (D. Nev.) | Dismissed with prejudice 2026-01-22 | US$3.2m claimed | None | Low |

### Findings

#### LIT-001: Aura thermostat battery class action covers about 1.62 million units
- **Finding:** A consolidated nationwide putative class plus three property damage suits (one over a December 2025 house fire in Westerville, Ohio) seek a refund or replacement for every Aura AT-200 and AT-210 buyer. The court has not yet ruled on Delmora's motion to dismiss.
- **Evidence:** "putative nationwide class of all US purchasers of Delmora Aura models AT-200 and AT-210 (about 1.62 million units)". Relief sought: "Full refund of the purchase price for every class member, or free replacement; damages for property loss; punitive damages". Docket: 2026-07-15 "Complaint filed"; 2026-09-02 "Order consolidating related cases"; 2026-10-09 "Reply brief on motion to dismiss filed".
- **Source:** `targets/heron/data/litigation/LIT-001_aura-battery-class-action.md`, docket entries 2026-07-15, 2026-09-02, 2026-10-09; `docket_index.csv` row LIT-001
- **Severity:** High
- **Confidence:** Medium. The case facts are in court records, but the hazard and incident counts are allegations the court has not tested.
- **Deal impact:** Valuation and post-closing. The deal brief treats the matter as a US$6.0m repair kit program that is "fully reserved" and "contained". That reserve does not obviously cover refund claims across 1.62m units, property damage or punitive damages. The unit price is not found in litigation records, so the refund exposure cannot be sized here. Exposure would grow if the motion is denied, a class is certified, or a CPSC action (LIT-009) widens the remedy. It would shrink if the warranty-period defense succeeds. The case is moving against Delmora: consolidation on 2026-09-02, then plaintiffs filing the CPSC letter on 2026-09-25. Recommend a specific indemnity or escrow, or a price adjustment. The hearing on 2026-11-18 falls before the November 30 signing target.
- **Cross-check:** Financial analyst: the reserve level and its date. SEC analyst: how the 10-Q describes the reserve and the consolidated case. News: further fire incidents.

#### LIT-002: Calder claims ownership of the core AdaptiveComfort patents, with trial set inside the closing window
- **Finding:** Calder seeks a declaration that it owns all six AdaptiveComfort patents, an order assigning them to Calder, and a 4% royalty on Delmora thermostat net sales since 2019. Delmora lost its limitations defense at the pleadings stage. Trial is set for February 8, 2027, inside the expected Q1 2027 closing window.
- **Evidence:** Exhibit A assignment language: "hereby assigns to the Institute all right, title and interest". The provisional application was filed "On March 6, 2017, while still employed by Calder". Relief sought: "a royalty of 4% of net sales of Delmora thermostats from 2019". Calder intends to license "on a non-exclusive basis to qualified manufacturers". Docket 2026-07-30: "Order denying Delmora's motion for judgment on the pleadings (limitations defense 'turns on disputed facts')".
- **Source:** `targets/heron/data/litigation/LIT-002_calder-ip-ownership.md`, Claims, Key facts, Relief sought, docket entries 2026-04-09, 2026-07-30, 2026-09-14; `docket_index.csv` row LIT-002
- **Severity:** Critical. Tests met: it could stop the deal, and it could change value by more than 10%.
  - *Stop the deal:* AdaptiveComfort runs on Delmora's devices (deal brief section 2), and OEM licensing is thesis point 2. Calder says it would license the patents non-exclusively to other manufacturers. Title would still be undecided at signing, and trial (2027-02-08) could fall before or after closing.
  - *More than 10% of value (inference):* 10% of EV is US$154.3m. At the deal multiple of 11.8x, a royalty that reduces EBITDA would cross that line once thermostat net sales exceed about US$327.0m a year (154.3 / 11.8 / 0.04). FY2025 Devices revenue was US$503.0m. That includes sensors and hubs as well as thermostats, so 4% of it (US$20.1m a year) is an upper bound. Back royalties since 2019 come on top. If thermostat sales prove to be below about US$327.0m, the value test depends on the back royalties and the loss of OEM licensing alone, and the lead may prefer High.
- **Confidence:** Medium. The ruling and the trial date are court records (High). The ownership facts are Calder's allegations, though they are supported by exhibits. The valuation is an inference.
- **Deal impact:** Valuation, closing and post-closing. The case has moved against Delmora: the limitations defense was denied on 2026-07-30, and Delmora's counsel withdrew from representing the CTO on 2026-08-20 (LIT-011). Possible protections: a closing condition tied to resolution or a settlement or license from Calder, a price reduction, or a specific escrow. The OEM licensing thesis should not be valued until title is clear.
- **Cross-check:** SEC analyst: whether the 10-Q or 8-Ks disclose the 2026-07-30 ruling and the trial date, and how they describe patent ownership. Financial analyst: thermostat net sales by year since 2019. News: commentary from Calder.

#### LIT-003: Colorado AG suit seeks an injunction on selling Insights data
- **Finding:** Colorado alleges that Delmora Insights data described as "de-identified" can be linked to individual households, and that Delmora sold occupancy inferences without valid consent. The state seeks an injunction requiring opt-in consent, deletion of data already shared, and civil penalties.
- **Evidence:** About 96,000 Colorado households were enrolled through a terms of service update with an opt-out setting, and fewer than 2% opted out. Daily occupancy indices at the ZIP+4 level went to "an insurer and two real-estate analytics firms" from January 2026. Relief sought: "A permanent injunction stopping the sale of Insights data from Colorado households without opt-in consent; deletion of data already shared; civil penalties of up to US$20,000 per violation". Docket: 2026-09-22 "Complaint filed"; 2026-09-29 "Stipulated extension of time to answer to October 27, 2026".
- **Source:** `targets/heron/data/litigation/LIT-003_colorado-insights-privacy.md`, Claims, Allegations, Relief sought, docket entries 2026-09-22, 2026-09-29; `docket_index.csv` row LIT-003
- **Severity:** High. It needs specific protection and directly affects the Insights thesis. The deal team attributes about US$310m of EV to Insights, which is 20.1% of US$1,543.4m. I have not rated it Critical because the injunction is limited to Colorado and the claims are untested. LIT-012 is the path that could make it Critical.
- **Confidence:** Low to Medium. The filing is a court record, but every allegation is untested and no answer has been filed.
- **Deal impact:** Valuation and post-closing. An opt-in rule would remove most of the base enrolled through opt-out. If other states follow, the Insights growth case to US$60.0m by 2028 is at risk (inference). Multiplying 96,000 households by US$20,000 gives US$1,920.0m. That is arithmetic on the statutory ceiling only. The court has not decided how violations are counted, and this is not an estimate. The case is too early to show a trend. The answer is due 2026-10-27.
- **Cross-check:** SEC analyst: whether risk factors and the 10-Q describe Insights data as de-identified, and whether the suit has been disclosed. News: other state or FTC activity. Financial analyst: Insights revenue and its customers (the insurer and the two real-estate analytics firms).

#### LIT-004: Pruett groundwater toxic tort over the former Pittock plant
- **Finding:** 42 named residents, for a putative class of about 600 Linden Park households, sue Delmora and Pittock over TCE migrating in groundwater from the former Pittock plant. They claim US$45.0m plus medical monitoring and punitive damages. Delmora itself is named as a defendant alongside its subsidiary.
- **Evidence:** "US$45.0 million for loss of property value, plus medical monitoring and punitive damages". The complaint alleges that Pittock's own 2023 site investigation report recommended off-site monitoring wells, which were "not installed until the Ohio EPA required them in 2026". Docket: 2026-09-17 "Complaint filed"; 2026-10-02 "Notice of appearance for defendants".
- **Source:** `targets/heron/data/litigation/LIT-004_marlow-groundwater.md`, header table, Allegations, docket entries 2026-09-17, 2026-10-02; `docket_index.csv` row LIT-004 (amount_claimed_usd_m 45.0)
- **Severity:** High
- **Confidence:** Low for liability (pleading allegations only). High for the claimed amount (court record).
- **Deal impact:** Inherited liability and valuation. The US$45.0m claimed is 2.9% of EV before medical monitoring, punitive damages and remediation (LIT-013). The deal brief has no environmental item. The allegation of a delay after the 2023 report could support punitive damages. Recommend a specific environmental indemnity or escrow and a Phase II review. The case is too early to show a trend.
- **Cross-check:** SEC analyst: environmental reserves, the 2021 Ohio EPA consent order disclosure, and whether this suit is disclosed. Financial analyst: any environmental accrual. News: local Marlow coverage.

#### LIT-005: European Commission Statement of Objections on online sales restrictions
- **Finding:** The EC opened Case AT.40977 on 2025-11-18 and issued a Statement of Objections on 2026-06-30 over online sales restrictions in Delmora's distribution. The reply is due 2026-10-30. There is no detail file, and no amount is stated.
- **Evidence:** Docket index: "Competition law; vertical restrictions", "Statement of Objections issued 2026-06-30", "Reply to Statement of Objections due", 2026-10-30.
- **Source:** `targets/heron/data/litigation/docket_index.csv`, row LIT-005
- **Severity:** Medium. A Statement of Objections is a formal adverse step, but the size of any fine is not found in litigation records, and I cannot size EU revenue from my files. This should be raised to High if EU revenue or a fine estimate shows material exposure.
- **Confidence:** Medium. Docket index row only. No detail file or decision text is available.
- **Deal impact:** Valuation (a possible fine) and post-closing (changes to distributor agreements). This is a conduct case, not merger control, so it is not a closing condition item. The deal team should get outside counsel's estimate of the fine range and timing. The trend is adverse: the case moved from opening to a Statement of Objections in about 7 months.
- **Cross-check:** SEC analyst: whether the Statement of Objections (June 30, 2026) is disclosed in the Q2 10-Q. Financial analyst: European revenue. News: EC press releases.

#### LIT-006: Open Firmware Conservancy GPLv2 copyright suit
- **Finding:** A copyright and GPLv2 open source license suit was filed on 2026-09-10 in N.D. Cal. The initial case management conference is 2026-12-03. There is no detail file. The relief sought and the products involved are not found in litigation records.
- **Evidence:** Docket index: "Copyright; open source license (GPLv2)", "Pending", "Initial case management conference", 2026-12-03.
- **Source:** `targets/heron/data/litigation/docket_index.csv`, row LIT-006
- **Severity:** Medium
- **Confidence:** Medium. Docket index row only.
- **Deal impact:** Post-closing and technology rights. GPL claims can lead to demands to release source code or to stop distributing firmware (general risk, not stated in the record). If the firmware at issue contains AdaptiveComfort code, this would add to the technology rights concern in LIT-002 (inference). The deal team needs an open source code scan in technical diligence.
- **Cross-check:** SEC analyst: disclosure. News: statements from the Conservancy.

#### LIT-007: Brennan Sales Group commissions claim dismissed with prejudice (closed)
- **Finding:** A US$3.2m breach of contract claim for sales commissions was dismissed with prejudice on 2026-01-22. This is a mitigant.
- **Evidence:** Docket index: "Breach of contract (sales commissions)", "Dismissed with prejudice on 2026-01-22", 3.2, next event "None".
- **Source:** `targets/heron/data/litigation/docket_index.csv`, row LIT-007
- **Severity:** Low (closed matter, a mitigant)
- **Confidence:** High for the dismissal (court record). Whether an appeal was filed is not found in litigation records.
- **Deal impact:** None expected. The deal team should confirm that the appeal period has passed with no appeal.
- **Cross-check:** SEC analyst: the matter should be described as resolved.

#### LIT-008: Product liability insurer has reserved all rights on the Aura claims
- **Finding:** Harborline Specialty acknowledged the Aura claims with a full reservation of rights, citing the policy period that began March 1, 2026. So insurance cover for LIT-001 is not assured.
- **Evidence:** "acknowledged notice of the claims with a full reservation of rights, citing the terms of the policy period that began March 1, 2026". Docket 2026-08-12: "Harborline Specialty reservation of rights letter (filed as exhibit to case management statement)".
- **Source:** `targets/heron/data/litigation/LIT-001_aura-battery-class-action.md`, Insurance section, docket entry 2026-08-12
- **Severity:** High
- **Confidence:** High that the reservation exists (court exhibit). Medium on why. The reference to the policy period, read with the alleged 58 incidents by end of 2024 (LIT-010), suggests a prior-knowledge or prior-period dispute (inference).
- **Deal impact:** Valuation. Exposure under LIT-001 may be uninsured. Supports a specific indemnity or escrow.
- **Cross-check:** SEC analyst: whether filings describe the matter as insured. Financial analyst: whether any insurance receivable has been recorded.

#### LIT-009: CPSC staff preliminary determination letter on Aura
- **Finding:** Plaintiffs filed notice of a CPSC staff preliminary determination letter dated August 28, 2026. The letter's content is not found in litigation records.
- **Evidence:** Docket 2026-09-25: "Plaintiffs' notice of CPSC staff preliminary determination letter dated August 28, 2026".
- **Source:** `targets/heron/data/litigation/LIT-001_aura-battery-class-action.md`, docket entry 2026-09-25
- **Severity:** High
- **Confidence:** High that the letter exists (docket). Its content is unknown.
- **Deal impact:** Valuation, post-closing and reputation. A regulator's preliminary view could make the do-it-yourself kit fix inadequate and lead to a formal recall or replacement program, well beyond the US$6.0m reserve in the deal brief (inference). Plaintiffs are using it to support their case, which is an adverse trend. It also challenges management's statement that the matter is "contained".
- **Cross-check:** SEC analyst: whether the August 28, 2026 letter is disclosed, for example in an 8-K or a 10-Q subsequent events note. News: CPSC announcements. The deal team should request the letter from management.

#### LIT-010: Alleged internal incident log contradicts the February 2026 investor statement
- **Finding:** Plaintiffs allege that engineers had logged 58 overheating incidents by end of 2024, more than a year before Delmora told investors in February 2026 that it had received "a limited number of consumer reports". If proven, this could create securities disclosure and punitive damages exposure.
- **Evidence:** "Delmora engineers logged 58 overheating incidents in an internal 'Thermal Event Tracker' by the end of 2024". The allegation "relies on a declaration from a former Delmora quality engineer".
- **Source:** `targets/heron/data/litigation/LIT-001_aura-battery-class-action.md`, Main allegations (complaint filed 2026-07-15)
- **Severity:** High
- **Confidence:** Low. This is a pleading allegation backed by a single former employee's declaration, and the court has not tested it.
- **Deal impact:** Disclosure risk, reputation, and possible follow-on securities claims. No securities suit is found in litigation records. It also bears on CPSC timely-reporting duties (inference, for outside counsel).
- **Cross-check:** SEC analyst: the exact February 2026 wording, probably in the 10-K. News: any reporting on the former engineer. Management: request the Thermal Event Tracker.

#### LIT-011: Delmora and its CTO now have separate counsel in the Calder case
- **Finding:** Delmora's counsel withdrew from representing CTO and co-founder Dr. Reyes-Barrow, and separate counsel appeared for him. His deposition is set for October 28, 2026.
- **Evidence:** Docket 2026-08-20: "Separate counsel appears for Dr. Reyes-Barrow; Delmora's counsel withdraws from representing Dr. Reyes-Barrow". Docket 2026-09-14: "Deposition of Dr. Reyes-Barrow scheduled for October 28, 2026".
- **Source:** `targets/heron/data/litigation/LIT-002_calder-ip-ownership.md`, docket entries 2026-08-20, 2026-09-14
- **Severity:** High
- **Confidence:** Medium. The withdrawal is a court record. The reason is not stated, and any conflict of interest is an inference.
- **Deal impact:** Closing risk and post-closing. Separate representation can mean the defendants' interests now diverge (inference). His testimony on when the invention was conceived is central to the case. There is also a key-person and retention risk for the co-founder CTO.
- **Cross-check:** SEC analyst: any 8-K on officer matters, and any indemnification agreements. News: coverage of the deposition.

#### LIT-012: The Colorado AG says the FTC is investigating compliance with a 2022 consent order
- **Finding:** The Colorado complaint states that the FTC is "conducting its own investigation of Delmora's compliance with its 2022 consent order". Violating a federal consent order could bring nationwide relief that goes beyond Colorado.
- **Evidence:** "The Attorney General's office states that it has shared information with the Federal Trade Commission, 'which is conducting its own investigation of Delmora's compliance with its 2022 consent order'".
- **Source:** `targets/heron/data/litigation/LIT-003_colorado-insights-privacy.md`, Main allegations (complaint filed 2026-09-22)
- **Severity:** High. Escalate to Critical if another source confirms the FTC inquiry targets Insights nationally: the roughly US$310m of Insights EV is 20.1% of EV, which would meet the more-than-10% test.
- **Confidence:** Low. This is a statement in a pleading. No FTC record is in the litigation files.
- **Deal impact:** Valuation (the Insights thesis) and disclosure. The terms of the 2022 consent order are not found in litigation records.
- **Cross-check:** SEC analyst: disclosure of the 2022 consent order and any FTC inquiry. News: FTC reporting.

#### LIT-013: Ohio EPA directive could lead to off-site groundwater remedies
- **Finding:** Under the 2021 administrative consent order, Ohio EPA confirmed TCE above the federal maximum contaminant level in two off-site wells. It directed vapor intrusion sampling at about 60 homes by November 30, 2026 and an off-site plume work plan by December 15, 2026. It will evaluate whether off-site remedies are required.
- **Evidence:** "confirms TCE above the federal maximum contaminant level in two off-site monitoring wells in Linden Park". The letter also says the agency "will evaluate whether off-site groundwater remedies are required".
- **Source:** `targets/heron/data/litigation/LIT-004_marlow-groundwater.md`, Related regulatory action (Ohio EPA letter dated 2026-09-22)
- **Severity:** High
- **Confidence:** High. This is an agency letter attached to a court filing.
- **Deal impact:** Inherited liability. Remediation cost is unquantified and separate from the US$45.0m tort claim. The sampling deadline falls on the signing target date, so results may come out between signing and closing. Recommend an environmental indemnity or escrow and making the sampling results a pre-signing deliverable.
- **Cross-check:** SEC analyst: the 2021 consent order and any environmental reserve. Financial analyst: environmental accruals.

#### LIT-014: Date inconsistency in the Pruett record
- **Finding:** The complaint is shown as filed on 2026-09-17, but it is said to attach an Ohio EPA letter dated 2026-09-22, five days later. Either the complaint was amended, or one of the dates is wrong.
- **Evidence:** "Filed | September 17, 2026" and "The complaint attaches an Ohio EPA letter to Pittock dated September 22, 2026". The docket shows only 2026-09-17 "Complaint filed" and 2026-10-02 "Notice of appearance".
- **Source:** `targets/heron/data/litigation/LIT-004_marlow-groundwater.md`, header table and Related regulatory action
- **Severity:** Low
- **Confidence:** High that the inconsistency exists in the record.
- **Deal impact:** A data quality issue. Outside counsel should confirm the actual docket, including any amended complaint.
- **Cross-check:** News or SEC dates for the Ohio EPA letter.

### Matters reviewed with low relevance

- **LIT-007 (Brennan):** closed with prejudice. A mitigant.
- **LIT-014:** a record inconsistency only.
- **Topics checked and not found in litigation records:** trade, customs or export-control matters; utility contract or government agency disputes (including the Western States Energy Alliance); Pittock pension or ERISA disputes; Nimbus earn-out disputes; employment disputes; securities class actions; merger challenges or shareholder suits over the deal. The only CPSC item is the letter noted in LIT-009.
- **Prompt injection:** no instruction-like text was found in any litigation file.

### Gaps and questions for management or outside counsel

1. **CPSC letter (LIT-009):** request the August 28, 2026 letter, any reply, and the Thermal Event Tracker (LIT-010). Ask counsel to assess timely-reporting exposure.
2. **Aura sizing (LIT-001, LIT-008):** unit price, number of kits shipped, the basis of the US$6.0m reserve, Harborline's specific coverage defenses, and policy limits.
3. **Calder (LIT-002, LIT-011):**
   - thermostat net sales by year since 2019;
   - counsel's view after the denial on 2026-07-30;
   - why separate counsel was appointed for the CTO;
   - any indemnification or cooperation agreement with Dr. Reyes-Barrow;
   - settlement or license talks with Calder.
   - The research was partly funded by a US Department of Energy grant. Ask counsel whether federal funding rights could also attach to the patents (inference; not found in litigation records).
4. **Colorado and FTC (LIT-003, LIT-012):** the 2022 FTC consent order, any FTC civil investigative demand, the share of Insights revenue from opt-out enrollments nationwide, and any other state inquiries.
5. **Pruett and Ohio EPA (LIT-004, LIT-013):**
   - the 2021 consent order;
   - the 2023 site investigation report;
   - the vapor intrusion sampling results, due November 30, 2026;
   - any remediation cost estimate;
   - any indemnity from Pittock's sellers under the 2019 purchase agreement (not found in litigation records).
6. **EC (LIT-005):** the Statement of Objections, Delmora's reply due 2026-10-30, counsel's estimate of the fine range, and EU revenue in the affected products.
7. **GPL (LIT-006):** the complaint, the firmware at issue, whether AdaptiveComfort code is involved, and the relief sought.
8. **Brennan (LIT-007):** confirm that no appeal was filed.
9. **Disclosure timing for the SEC analyst to check against the Q2 2026 10-Q and later 8-Ks:**
   - EC Statement of Objections (2026-06-30);
   - Aura complaint (2026-07-15);
   - Calder ruling (2026-07-30);
   - Harborline reservation of rights (2026-08-12);
   - Reyes-Barrow counsel change (2026-08-20);
   - CPSC letter (2026-08-28);
   - GPL suit (2026-09-10);
   - Pruett suit (2026-09-17);
   - Colorado AG suit (2026-09-22);
   - Ohio EPA letter (2026-09-22).

   Also compare all of these with management's statement that every pending matter is "without merit or immaterial".
10. **Key dates near signing and closing:**
    - 2026-10-27: Colorado answer due
    - 2026-10-28: Reyes-Barrow deposition
    - 2026-10-30: reply to EC Statement of Objections due
    - 2026-11-05: Pruett case management conference
    - 2026-11-18: Aura motion to dismiss hearing
    - 2026-11-20: Calder discovery closes
    - 2026-11-30: Ohio EPA sampling deadline, and the signing target
    - 2026-12-03: GPL case management conference
    - 2026-12-11: Calder summary judgment motions due
    - 2026-12-15: Ohio EPA plume work plan due
    - 2027-02-08: Calder trial

This is not legal advice. Every item above should go to outside counsel.
