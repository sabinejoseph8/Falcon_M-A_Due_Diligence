## Litigation analyst: findings

### Files reviewed

- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/deal-brief.md` (for context)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/docket_index.csv` (6 matters, LIT-001 to LIT-006)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-002_genaro-v-corvane.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-003_data-security-incident-litigation.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-004_hollis-v-corvane.md`

The docket index lists two matters with no detail file: LIT-005 (HHS OCR) and LIT-006 (NC DEQ). I covered them from the index row only.

None of the files contain text that tries to instruct the agents.

**Note on IDs:** the docket index uses LIT-001 to LIT-006 as **matter** IDs. My **finding** IDs below run LIT-001 to LIT-014 and do not match the matter IDs. Each card names its matter.

### Matter summary table

| Case ID | Case | Posture | Claimed / exposure | Next date | Severity |
|---|---|---|---|---|---|
| Matter LIT-001 | US ex rel. Whitcomb v. Corvane (E.D.N.C., FCA qui tam) | Unsealed 2026-08-21. Government intervened on Counts I and II on 2026-08-18. | US$96.4m single damages alleged. US$289.2m if trebled, before per-claim penalties. | 2026-10-30: government complaint-in-intervention due | Critical |
| Matter LIT-002 | Genaro Biosciences v. Corvane (D. Del., patent) | Expert discovery. Markman order for Genaro on 2026-08-12. | US$68.0m past damages (plaintiff's expert), plus a 9% ongoing royalty or an injunction | 2026-11-20: summary judgment and Daubert motions. 2027-02-08: jury trial | High |
| Matter LIT-003 | In re Corvane Data Security Incident Litigation (E.D.N.C.) | Consolidated complaint filed 2026-09-28 | Not stated. About 412,300 individuals notified. | 2026-11-30: Corvane motion to dismiss due | High |
| Matter LIT-004 | Hollis v. Corvane (Wake County Superior Court) | Closed. Dismissed with prejudice 2026-06-09. No appeal. | US$2.4m claimed. No payment made. | None | Low |
| Matter LIT-005 | HHS OCR compliance review, April 2026 breach | Open. Data request outstanding. | Not stated | 2026-10-30: Corvane response due | Medium |
| Matter LIT-006 | NC DEQ notice of violation, Durham lab medical waste | Penalty agreed. Corrective action complete. | US$0.18m | 2026-11-15: civil penalty payment due | Low |

### Findings

#### LIT-001: Whitcomb FCA qui tam: the government has intervened, and trebled alleged damages exceed 10% of deal value
- **Finding:** On 2026-08-18 the United States intervened on the medical-necessity and kickback counts for Medicare OncoTrace claims. The relator's alleged single damages are US$96.4m, which is US$289.2m if trebled, before per-claim penalties on about 41,200 claims. The Critical test is "more than 10% of value". US$289.2m is 17.5% of the US$1,648.6m EV and 23.0% of the US$1,257.6m equity value. Even the untrebled US$96.4m is 5.8% of EV.
- **Evidence:** 2026-08-18: "United States' Notice of Election to Intervene in Part. The government intervenes on Counts I and II as to Medicare claims for OncoTrace." Relator's complaint (unsealed 2026-08-21): "about 41,200 claims from January 2019 to December 2025 with single damages of US$96.4 million." Count II alleges "US$3.2 million in 'speaker fees' ... to 61 physicians."
- **Source:** `targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`, docket entries 2026-08-18 and 2026-08-21; `docket_index.csv` row LIT-001
- **Severity:** Critical (more than 10% of value test, using trebled alleged damages against EV)
- **Confidence:** Intervention: High (court record). Damages amount: Low (the relator's allegation, not tested by the court, and the government's own damages figure is not filed yet).
- **Deal impact:** Valuation and structure. The complaint-in-intervention is due 2026-10-30, before signing. It will set out the government's own theory and possibly its own damages figure. Corvane must respond within 60 days of service, which is around signing. The case is likely to need a specific indemnity, a special escrow or a price adjustment. The per-claim penalty amount is not found in litigation records. The number of Count II claims is not stated. Settlement talks are not found in litigation records.
- **Trend:** Against Corvane. Six seal extensions (2024-05-16 to 2026-05-20), then the CID (2026-02-11), then intervention (2026-08-18).
- **Cross-check:** Compare with the 10-K and 10-Q descriptions of government investigations and any reserve. Check in the financials what share of revenue comes from Medicare OncoTrace. Check the news for settlement reports.

#### LIT-002: Whitcomb: risk of Medicare exclusion and a Corporate Integrity Agreement
- **Finding:** Apart from the money, an FCA or AKS liability can lead to exclusion from Medicare and Medicaid. Settlements often include an HHS OIG Corporate Integrity Agreement. Either outcome would affect how Corvane runs its main clinical testing business after closing.
- **Evidence:** Detail file summary: "Defendants found liable can also face exclusion from Medicare and Medicaid, and settlements often include a Corporate Integrity Agreement with the HHS Office of Inspector General."
- **Source:** `targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`, summary section (after the 2026-08-21 unsealing)
- **Severity:** High
- **Confidence:** Medium. This is the file's general statement of FCA remedies. No exclusion or CIA proceeding appears on the docket.
- **Deal impact:** Post-closing integration and compliance cost. Commercial practices (speaker programs, ordering-physician relationships) may need review before signing. A CIA would bring years of monitoring cost (inference).
- **Cross-check:** The 10-K risk factors on fraud and abuse. Any HHS OIG references in the filings or news.

#### LIT-003: Whitcomb: CID served February 11, 2026. Check whether the 10-K and 10-Q disclosed it
- **Finding:** The government served a civil investigative demand on 2026-02-11. That date may fall before the FY2025 10-K was filed, and it is before the Q2 2026 10-Q. The deal model assumes no litigation costs "beyond those described in the FY2025 10-K". If the 10-K did not describe the CID, that assumption is stale.
- **Evidence:** 2026-03-02 sealed status report (unsealed 2026-08-21): "The United States served a civil investigative demand on Corvane on February 11, 2026. The investigation is active."
- **Source:** `targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`, docket entries 2026-03-02 and 2026-08-21
- **Severity:** High
- **Confidence:** High. The CID date comes from a government filing in the court record. The 10-K filing date is not found in litigation records.
- **Deal impact:** Disclosure, and the reliability of the deal brief's assumption (IC question 5). The intervention (2026-08-18) and unsealing (2026-08-21) both came after the 2026-08-05 8-K.
- **Cross-check:** The SEC analyst should confirm the 10-K filing date and whether the 10-K, the 10-Q and the 8-Ks mention a CID, a DOJ investigation or a qui tam.

#### LIT-004: Whitcomb Count III (retaliation): the government declined, small claim
- **Finding:** The government declined to intervene on the relator's retaliation count, so the relator will pursue it herself. No amount is stated.
- **Evidence:** 2026-08-18: the government "declines to intervene on Count III."
- **Source:** `targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`, docket entry 2026-08-18
- **Severity:** Low
- **Confidence:** Low for the retaliation facts (allegation only). High for the declination (court record).
- **Deal impact:** Minor. It can be covered by the general Whitcomb indemnity.
- **Cross-check:** HR records on the relator's 2023 termination.

#### LIT-005: Genaro patent case: injunction risk to the current OncoTrace before closing, and recent rulings went against Corvane
- **Finding:** Genaro seeks a permanent injunction against the current OncoTrace. Two key rulings went against Corvane: the PTAB denied inter partes review (2025-12-15) and the court adopted Genaro's claim construction (2026-08-12). The jury trial is set for 2027-02-08, before the Q2 2027 closing. The redesigned v3 is not expected until mid-2027, so a gap with no non-infringing product is possible.
- **Evidence:** 2025-12-15: PTAB "denies institution of Corvane's petition for inter partes review." 2026-08-12: "The court adopts Genaro's proposed construction of the two disputed terms." Claims: Genaro seeks "a permanent injunction against further sales of the accused version of OncoTrace."
- **Source:** `targets/kestrel/data/litigation/LIT-002_genaro-v-corvane.md`, docket entries 2025-12-15 and 2026-08-12, and the upcoming dates table
- **Severity:** High. It could become Critical if OncoTrace revenue is more than 10% of value at risk. OncoTrace revenue share is not found in litigation records.
- **Confidence:** Medium. The rulings are in the court record. The injunction outcome is not decided.
- **Deal impact:** Closing risk and valuation. A verdict could arrive between signing and closing. Consider a closing condition or an MAE carve-in tied to the trial result, and a special indemnity. The flagship product line is also the subject of the Whitcomb case (finding LIT-001).
- **Trend:** Against Corvane since the 2026-08-12 claim construction order.
- **Cross-check:** The financials for OncoTrace revenue and margin. Whether the 10-Q (2026-08-05 period) described the case and whether later filings mention the Markman loss.

#### LIT-006: Genaro: US$68.0m past damages claimed, plus a 9% ongoing royalty
- **Finding:** Genaro's damages expert claims a 9% reasonable royalty on OncoTrace net revenue: US$68.0m of past damages through 2026-06-30, plus an ongoing royalty if there is no injunction. US$68.0m at 9% implies about US$755.6m of cumulative OncoTrace net revenue in the damages period (inference; the period start date is not stated).
- **Evidence:** 2026-09-25: "reasonable royalty of 9% of OncoTrace net revenue, past damages of US$68.0 million through June 30, 2026, plus an ongoing royalty or a permanent injunction."
- **Source:** `targets/kestrel/data/litigation/LIT-002_genaro-v-corvane.md`, docket entry 2026-09-25
- **Severity:** High
- **Confidence:** Low for the amount (plaintiff's expert, not tested, and no Corvane rebuttal report on file). High that the claim was served.
- **Deal impact:** Valuation. US$68.0m is 4.1% of EV. A 9% ongoing royalty would directly reduce Adjusted EBITDA, which matters for the US$110.0m LTM EBITDA financing condition (inference). Damages keep growing after 2026-06-30. Whether willfulness is pleaded is not found in litigation records.
- **Cross-check:** The financial analyst should apply 9% to OncoTrace revenue to size the run-rate royalty. Check any reserve in the filings.

#### LIT-007: Genaro: the OncoTrace v3 redesign depends on timing and New York State approval
- **Finding:** Corvane says a design-around, OncoTrace v3, is in validation. Corvane expects to launch it in mid-2027, subject to New York State approval. That is after the 2027-02-08 trial. The redesign would reduce exposure only once it launches, and it has not launched.
- **Evidence:** 2026-10-02: Corvane "expects to launch it in mid-2027, subject to New York State approval."
- **Source:** `targets/kestrel/data/litigation/LIT-002_genaro-v-corvane.md`, docket entry 2026-10-02
- **Severity:** Medium
- **Confidence:** Medium. This is Corvane's own statement in a filed interrogatory response, not a court finding.
- **Deal impact:** Post-closing integration. The v3 timeline needs diligence: validation status, the NY approval path, and whether payers and customers will switch.
- **Cross-check:** Whether the 10-Q or investor materials mention v3. News on regulatory status.

#### LIT-008: Data breach class action: about 412,300 individuals, genetic data, statutory damages sought
- **Finding:** Seven cases were consolidated (2026-08-14). The consolidated complaint (2026-09-28) alleges theft of about 1.1 TB of data, including genetic test results. It seeks damages, statutory damages under state genetic privacy laws, monitoring and injunctive security relief. No amount is stated.
- **Evidence:** Consolidated complaint (2026-09-28): notification letters went "to approximately 412,300 individuals". Plaintiffs seek "statutory damages under state genetic privacy laws."
- **Source:** `targets/kestrel/data/litigation/LIT-003_data-security-incident-litigation.md`, docket entries 2026-08-14 and 2026-09-28; `docket_index.csv` row LIT-003
- **Severity:** High
- **Confidence:** Low for the allegations (not tested). High for the procedural posture.
- **Deal impact:** Valuation and reputation. Statutory damages per person could scale with the class size, though no figure is in the records. The case could damage trust with patients and ordering physicians. The motion to dismiss is due 2026-11-30, the opposition 2027-01-15, and any ruling is likely after signing (inference). The plaintiffs' multi-factor authentication allegation points to a security remediation cost after closing.
- **Cross-check:** The 10-Q breach disclosure and any accrual. News on the ransomware group and on patient impact.

#### LIT-009: Data breach: allegation that the April 27, 2026 8-K was inaccurate when filed
- **Finding:** Plaintiffs allege that Corvane's forensic firm gave preliminary exfiltration findings on 2026-04-24. On 2026-04-27, Corvane's 8-K said there was "no evidence at this time" of exfiltration. If true, this is a disclosure-accuracy issue and could invite securities claims. No securities case is on the docket index.
- **Evidence:** Consolidated complaint (2026-09-28): "preliminary findings of data exfiltration on April 24, 2026" (citing "an internal timeline produced in early discovery"). The 8-K quoted: "no evidence at this time that patient information was exfiltrated."
- **Source:** `targets/kestrel/data/litigation/LIT-003_data-security-incident-litigation.md`, docket entry 2026-09-28 (allegations section)
- **Severity:** High
- **Confidence:** Low. Plaintiffs' allegation, though they cite a document Corvane itself produced.
- **Deal impact:** Disclosure and governance (IC question 5). Possible SEC or securities-class exposure (inference). Ask for the forensic firm's preliminary report and the 8-K drafting record.
- **Cross-check:** The SEC analyst should check the exact 8-K wording of 2026-04-27 and any later correction. Notification on 2026-06-12 was 55 days after the 2026-04-18 attack (recomputed). Outside counsel should check that timing against breach notification rules.

#### LIT-010: Data breach: cyber insurance limit of US$10.0m
- **Finding:** The litigation file notes that Corvane's 10-Q states a cyber insurance limit of US$10.0m. That limit has to cover the class action, the OCR review and remediation, so it may be small compared with a class of about 412,300 (inference).
- **Evidence:** Notes: "Corvane's 10-Q says its cyber insurance limit is US$10.0 million."
- **Source:** `targets/kestrel/data/litigation/LIT-003_data-security-incident-litigation.md`, notes for diligence
- **Severity:** Medium
- **Confidence:** Medium. This is a note in the litigation file quoting the 10-Q, not a court record.
- **Deal impact:** Valuation. Exposure above US$10.0m falls on Corvane. A specific indemnity or escrow for breach costs may be warranted.
- **Cross-check:** The SEC analyst should confirm the US$10.0m limit, the retention and any amount already used in the 10-Q.

#### LIT-011: HHS OCR HIPAA compliance review of the April 2026 breach
- **Finding:** OCR opened a compliance review on 2026-07-08. Corvane's response to OCR's data request is due 2026-10-30, before signing. No amount is stated and there is no detail file.
- **Evidence:** Docket index: "Open: data request outstanding", next event "Corvane response to OCR data request due" on 2026-10-30.
- **Source:** `targets/kestrel/data/litigation/docket_index.csv`, row LIT-005 (filed 2026-07-08)
- **Severity:** Medium
- **Confidence:** Medium. Index entry only, with no underlying record.
- **Deal impact:** Regulatory. A possible resolution payment and corrective action plan (inference). Ask for the OCR letter and Corvane's response.
- **Cross-check:** Whether the 10-Q or 8-Ks mention OCR.

#### LIT-012: NC DEQ notice of violation, Durham lab medical waste (small, nearly resolved)
- **Finding:** The penalty of US$0.18m is agreed and corrective action is complete. Payment is due 2026-11-15.
- **Evidence:** Docket index: "Open: penalty agreed; corrective action complete", amount 0.18.
- **Source:** `targets/kestrel/data/litigation/docket_index.csv`, row LIT-006 (last activity 2026-08-11)
- **Severity:** Low
- **Confidence:** Medium. Index entry only.
- **Deal impact:** None material. Confirm payment at closing.
- **Cross-check:** Environmental compliance records for the other six labs.

#### LIT-013: Hollis wage and hour class action: dismissed with prejudice, closed (mitigant)
- **Finding:** The court dismissed the US$2.4m overtime claim with prejudice because time records show travel time was paid. The appeal deadline passed with no appeal. No settlement was paid. This is a resolved matter and a positive point.
- **Evidence:** 2026-06-09: "Order dismissing the case with prejudice." 2026-07-09: "No appeal filed. Case closed." Notes: "No settlement payment was made."
- **Source:** `targets/kestrel/data/litigation/LIT-004_hollis-v-corvane.md`, docket entries 2026-06-09 and 2026-07-09
- **Severity:** Low (mitigant)
- **Confidence:** High (court record)
- **Deal impact:** None. It supports the quality of Corvane's timekeeping controls.
- **Cross-check:** None needed. Optionally confirm the filings show it as resolved.

#### LIT-014: Most adverse docket events came after Corvane's latest periodic filings
- **Finding:** Six adverse events came after the 2026-08-05 8-K: the Markman loss (2026-08-12), the government's intervention (2026-08-18), the unsealing (2026-08-21), the US$68.0m damages report (2026-09-25), the consolidated breach complaint (2026-09-28) and the v3 interrogatory response (2026-10-02). The deal model was built as of 2026-06-30, before all of them. Two earlier events may be missing from the filings: the CID (2026-02-11) and the OCR review (2026-07-08).
- **Evidence:** Docket entries as dated in findings LIT-001, LIT-005, LIT-006 and LIT-008. Deal brief section 6: "model built as of June 30, 2026."
- **Source:** `LIT-001_us-ex-rel-whitcomb-v-corvane.md`, `LIT-002_genaro-v-corvane.md`, `LIT-003_data-security-incident-litigation.md`, `docket_index.csv`
- **Severity:** High
- **Confidence:** Medium. Inferred from several docket dates. Filing dates other than the 8-Ks are not found in litigation records.
- **Deal impact:** Disclosure and stale model assumptions. Ask whether Corvane has filed, or plans, an 8-K on the intervention or the Markman ruling.
- **Cross-check:** The SEC analyst should list every filing after 2026-08-05 and the litigation disclosure in each.

### Matters reviewed with low relevance

- Matter LIT-004, Hollis (finding LIT-013): closed, no payment.
- Matter LIT-006, NC DEQ (finding LIT-012): US$0.18m, resolved apart from payment.
- Whitcomb Count III retaliation (finding LIT-004).
- No embedded instructions or prompt-injection text found in any litigation file.

### Gaps and questions for management or outside counsel

1. Whitcomb: will the government's 2026-10-30 complaint-in-intervention state its own damages figure? What penalty per claim applies to about 41,200 claims, and how many Count II claims are there? Have any settlement talks or tolling agreements taken place? (Not found in litigation records.)
2. Whitcomb: when was the 10-K filed relative to the 2026-02-11 CID, and was the CID disclosed? Has Corvane set any reserve?
3. Genaro: how much OncoTrace revenue and EBITDA is at risk from an injunction? Is willfulness pleaded? When is Corvane's rebuttal damages report due? Has Corvane approached Genaro about a license? What is the v3 validation status and NY State approval timeline?
4. Data breach: we need the forensic firm's 2026-04-24 preliminary findings and the 8-K drafting record. We also need the claims per state genetic privacy law, the remaining cyber insurance and its retention, and remediation costs (for example the MFA gap).
5. OCR (matter LIT-005) and DEQ (matter LIT-006): no detail files. Request the OCR data request, Corvane's response, and the DEQ consent order.
6. Do any securities class actions or derivative suits exist, for example tied to the April 27, 2026 8-K? None appear in the docket index.
7. Combined effect (for the lead agent): the Whitcomb and Genaro cases both target OncoTrace. Ask outside counsel how the two cases interact, and for a combined view on escrow or indemnity size.

This is not legal advice. All items should go to outside counsel.
