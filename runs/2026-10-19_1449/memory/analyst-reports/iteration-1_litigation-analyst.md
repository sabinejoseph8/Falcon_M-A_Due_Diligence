## Litigation analyst: findings

### Files reviewed

- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/deal-brief.md` (context only)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/docket_index.csv`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-002_genaro-v-corvane.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-003_data-security-incident-litigation.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-004_hollis-v-corvane.md`

The docket index lists six matters. LIT-005 (HHS OCR) and LIT-006 (NC DEQ) have no detail file, so I reviewed them from the index row only. I found no text in any file that tries to instruct the agents.

### Matter summary table

| Case ID | Case | Posture | Claimed / exposure | Next date | Severity |
|---|---|---|---|---|---|
| LIT-001 | US ex rel. Whitcomb v. Corvane (E.D.N.C., 5:24-cv-00187), FCA qui tam | Unsealed 2026-08-21. Government intervened in part on 2026-08-18 | Relator's single damages US$96.4m. Trebled US$289.2m, before per-claim penalties. Exclusion risk | 2026-10-30: government complaint-in-intervention due | Critical |
| LIT-002 | Genaro Biosciences v. Corvane (D. Del., 1:25-cv-00412), patent | Expert discovery. Markman ruling went against Corvane on 2026-08-12 | Past damages US$68.0m (plaintiff's expert), 9% ongoing royalty, or a permanent injunction against OncoTrace | 2026-11-20: summary judgment and Daubert motions. 2027-02-08: jury trial | High |
| LIT-003 | In re Corvane Data Security Incident Litigation (E.D.N.C., 5:26-cv-00341) | Consolidated complaint filed 2026-09-28 | Not stated. About 412,300 people notified. Cyber insurance limit US$10.0m (file note citing the 10-Q) | 2026-11-30: motion to dismiss due | High |
| LIT-005 | HHS OCR compliance review (OCR 26-418820), HIPAA | Data request outstanding | Not stated | 2026-10-30: Corvane response due | Medium |
| LIT-006 | NC DEQ notice of violation (NOV-2026-MW-0093), medical waste | Penalty agreed. Corrective action complete | US$0.18m | 2026-11-15: penalty payment due | Low |
| LIT-004 | Hollis v. Corvane (Wake County, 24-CVS-011873), wage and hour | Closed. Dismissed with prejudice. No appeal filed | US$2.4m claimed. No payment made | None | Low |

### Findings

#### LIT-01: Government has intervened in the Whitcomb False Claims Act case on the OncoTrace Medicare claims
- **Finding:** The United States elected to intervene on Count I (medical necessity) and Count II (kickbacks) for Medicare claims on OncoTrace. It declined Count III (retaliation). It must file its own complaint by October 30, 2026, which is before the mid-December 2026 signing.
- **Evidence:** 2026-08-18: "United States' Notice of Election to Intervene in Part. The government intervenes on Counts I and II as to Medicare claims for OncoTrace, and declines to intervene on Count III." 2026-08-21: "the government's complaint-in-intervention is due October 30, 2026. Corvane to respond within 60 days of service."
- **Source:** `targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`, docket entries 2026-08-18 and 2026-08-21. Also `docket_index.csv`, row LIT-001.
- **Severity:** Critical. Test met: more than 10% of value. The relator's single damages of US$96.4m, trebled as the FCA allows, come to US$289.2m before penalties. That is 17.5% of the US$1,648.6m EV and 23.0% of the US$1,257.6m equity value. Exclusion from Medicare and Medicaid, which the file names as a possible outcome, could also stop the deal. The damages figure is still the relator's allegation (see LIT-02).
- **Confidence:** High for the intervention and the dates (court record). Low for the damages amount (relator's pleading, not tested).
- **Deal impact:** Valuation, closing risk and post-closing. The case may need a specific indemnity or escrow, a price adjustment, or a closing condition tied to the case status. A settlement could include a Corporate Integrity Agreement, which would affect integration and billing operations. It also contradicts the deal model assumption of "no material litigation or regulatory costs beyond those described in the FY2025 10-K", because intervention came after that filing.
- **Cross-check:** Check whether the FY2025 10-K and the 10-Qs for Q1 and Q2 2026 disclose the case, the CID served February 11, 2026, and any reserve. Check whether an 8-K or Q3 10-Q discloses the August 18 intervention. Check news coverage of the unsealing.

#### LIT-02: How large the FCA exposure could be (arithmetic shown)
- **Finding:** The record supports a trebled figure of US$289.2m before penalties. The per-claim penalty amount is not given in the litigation records, so I cannot state total exposure. Penalties on about 41,200 claims could add a large amount on top.
- **Evidence:** "about 41,200 claims from January 2019 to December 2025 with single damages of US$96.4 million". "three times its damages plus a civil penalty for each false claim". Count II: "US$3.2 million in 'speaker fees' from 2019 to 2025 to 61 physicians".
- **Arithmetic:**
  - Single damages: US$96.4m (relator's figure).
  - Treble: 96.4 x 3 = US$289.2m. The file states the same number.
  - Average single damages per claim: 96.4 / 41,200 = about US$2,340 per claim.
  - Penalties: 41,200 claims x the per-claim penalty. The penalty amount is not found in litigation records. As a sensitivity only, each US$1,000 of penalty per claim adds US$41.2m.
  - Count II: the number and value of claims tainted by kickbacks are not stated. It is unclear whether they overlap with the 41,200 Count I claims (not found in litigation records).
  - Scope: the government intervened only "as to Medicare claims for OncoTrace". Count I is already framed as Medicare billing, so the US$96.4m probably falls mostly within the intervened scope (inference).
- **Source:** `targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`, complaint summary (unsealed 2026-08-21) and notes for diligence.
- **Severity:** Critical. This is the same exposure as LIT-01 and the same test applies (US$289.2m is more than 10% of EV). The lead may want to make LIT-01 the parent finding.
- **Confidence:** Low for the amounts (relator allegation). High that trebling and per-claim penalties apply under the statute as the file describes them.
- **Deal impact:** Valuation. This sets the size of any escrow or indemnity. FCA cases often settle below the trebled amount, but the records give no settlement figure, so I make no prediction.
- **Cross-check:** Ask the financial analyst how much Medicare OncoTrace revenue Corvane booked from 2019 to 2025 and test it against US$96.4m. Check the SEC filings for any loss contingency or reserve.

#### LIT-03: A civil investigative demand was served February 11, 2026, and the case was under seal for about 29 months
- **Finding:** The government served a CID on Corvane on February 11, 2026, so Corvane knew of an active federal investigation during its FY2025 10-K cycle. The complaint was under seal from March 18, 2024 to August 21, 2026, with six seal extensions in total.
- **Evidence:** 2026-03-02 status report: "The United States served a civil investigative demand on Corvane on February 11, 2026. The investigation is active." 2024-05-16: first extension granted. "2024-11-12 to 2026-05-20: Five further seal extensions requested by the government. Each granted."
- **Source:** `targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`, docket entries 2024-03-18, 2024-05-16, 2024-11-12 to 2026-05-20, and 2026-03-02.
- **Severity:** High (disclosure)
- **Confidence:** High (court record)
- **Deal impact:** Disclosure and governance. This bears on whether the 10-K and later 10-Qs were reliable (IC question 5).
- **Cross-check:** Compare the 10-K filing date with February 11, 2026. Did the 10-K, or the Q1 or Q2 2026 10-Q, mention the CID or a government investigation? Did the 10-Q filed after August 18 mention the intervention?

#### LIT-04: Genaro patent case has moved against Corvane, and trial is set before closing
- **Finding:** Corvane lost its inter partes review petition and the claim construction ruling. Genaro's damages expert puts past damages at US$68.0m and seeks either an ongoing 9% royalty or a permanent injunction against the current OncoTrace. The jury trial starts February 8, 2027, before the Q2 2027 closing.
- **Evidence:** 2025-12-15: PTAB "denies institution of Corvane's petition for inter partes review". 2026-08-12: "The court adopts Genaro's proposed construction of the two disputed terms". 2026-09-25: "reasonable royalty of 9% of OncoTrace net revenue, past damages of US$68.0 million through June 30, 2026, plus an ongoing royalty or a permanent injunction."
- **Source:** `targets/kestrel/data/litigation/LIT-002_genaro-v-corvane.md`, docket entries 2025-12-15, 2026-08-12 and 2026-09-25, and upcoming dates.
- **Severity:** High. I cannot show the Critical test from my files: US$68.0m is 4.1% of EV, and OncoTrace's share of revenue is not in the litigation records. If OncoTrace is a large share of revenue, an injunction could meet the "block closing" or "more than 10% of value" test. The lead should test this with financial data.
- **Confidence:** High for the rulings and dates (court record). Low for the US$68.0m (plaintiff's expert, not tested).
- **Deal impact:** Valuation, closing risk and post-closing. A trial verdict between signing and closing could trigger MAE arguments. The deal may need a specific IP indemnity or escrow, an ongoing royalty in the model, and a closing condition or MAE carve-out drafted around this case.
- **Trend:** Against Corvane since the 2025-12-15 IPR denial and the 2026-08-12 Markman order.
- **Cross-check:** Get OncoTrace revenue from the financials. Check whether the 10-K and 10-Qs disclose the IPR denial and the Markman loss, and whether they describe the case as without merit. Check whether Genaro appears in `revenue_by_customer.csv`.

#### LIT-05: Corvane's own filing says the patent redesign will not launch until mid-2027, which leaves an injunction gap
- **Finding:** The redesigned "OncoTrace v3", meant to avoid the asserted claims, is still in validation. Corvane expects to launch it in mid-2027, subject to New York State approval. That is after the February 2027 trial, so an injunction could take effect before a non-infringing product is available.
- **Evidence:** 2026-10-02: Corvane "expects to launch it in mid-2027, subject to New York State approval."
- **Source:** `targets/kestrel/data/litigation/LIT-002_genaro-v-corvane.md`, docket entry 2026-10-02 (interrogatory response excerpt).
- **Severity:** High
- **Confidence:** High for the stated timeline (Corvane's own sworn discovery response, filed in court). Medium that a gap would exist, because that depends on whether an injunction is granted and when.
- **Deal impact:** Post-closing integration and value. The redesign timeline and NY approval are execution risks. Past damages through June 30, 2026 do not cover use after that date. Imputed revenue base: 68.0 / 0.09 = about US$755.6m of cumulative OncoTrace net revenue over the damages period (inference). The start date of that period is not found in litigation records.
- **Cross-check:** Does management's description of OncoTrace v3 in its filings or news match the mid-2027 timeline? Check the status of the NY State approval.

#### LIT-06: Data breach class action alleges the April 27, 2026 Form 8-K was wrong when filed
- **Finding:** Plaintiffs allege that Corvane's forensic firm reported preliminary findings of data exfiltration on April 24, 2026. Three days later, on April 27, Corvane's Form 8-K said there was "no evidence at this time that patient information was exfiltrated." Notice letters went to about 412,300 people on June 12, 2026, and the stolen data included genetic test results.
- **Evidence:** Consolidated complaint (2026-09-28): "preliminary findings of data exfiltration on April 24, 2026". 8-K quoted as "no evidence at this time that patient information was exfiltrated." Notice "June 12, 2026, to approximately 412,300 individuals".
- **Source:** `targets/kestrel/data/litigation/LIT-003_data-security-incident-litigation.md`, allegations in the consolidated complaint and docket entry 2026-09-28.
- **Severity:** High
- **Confidence:** Low. These are plaintiffs' allegations, and the file says they "have not been proven". Plaintiffs say they rely on an internal timeline produced in discovery, which makes the claim worth testing.
- **Deal impact:** Disclosure, controls and valuation. If true, the claim raises questions about disclosure controls and could support securities claims. No securities case appears in the docket index. Statutory damages under state genetic privacy laws, across about 412,300 people, could be large. The amount is not stated. The file notes a cyber insurance limit of US$10.0m (citing the 10-Q). Any exposure above that limit is uninsured, so a specific indemnity or escrow may be needed.
- **Cross-check:** Compare the text of the April 27, 2026 8-K in the SEC filings. Check later 10-Q language on the breach and on cyber insurance. Ask for the forensic firm's April 24 findings.

#### LIT-07: Seven data breach cases have been consolidated, and the case is still early
- **Finding:** Seven cases were consolidated on August 14, 2026. Corvane's motion to dismiss is due November 30, 2026 and plaintiffs' opposition January 15, 2027, so no ruling is likely before signing (inference from the schedule). Plaintiffs also seek court-ordered security improvements.
- **Evidence:** 2026-08-14: "Order consolidating seven cases and appointing interim class counsel." Upcoming dates: 2026-11-30 and 2027-01-15.
- **Source:** `targets/kestrel/data/litigation/LIT-003_data-security-incident-litigation.md`, docket entries 2026-05-04 to 2026-09-28.
- **Severity:** Medium (sizing is covered under LIT-06)
- **Confidence:** High (court record)
- **Deal impact:** Post-closing. Plan for remediation costs, including the alleged missing multi-factor authentication on a remote-access account. There is also reputational risk with patients and ordering physicians.
- **Cross-check:** Check news on patient and physician reaction, and remediation costs in the 10-Q.

#### LIT-08: HHS OCR HIPAA review of the April 2026 breach is open, with a response due October 30, 2026
- **Finding:** OCR opened a compliance review on July 8, 2026. Corvane's response to OCR's data request is due October 30, 2026, the same day as the government's FCA complaint-in-intervention.
- **Evidence:** Index row: "Open: data request outstanding", next date "2026-10-30", amount "Not stated".
- **Source:** `targets/kestrel/data/litigation/docket_index.csv`, row LIT-005 (no detail file)
- **Severity:** Medium
- **Confidence:** High for the status and dates (index). There are no further details.
- **Deal impact:** Possible HIPAA penalty or corrective action plan. Disclosure.
- **Cross-check:** Check whether the SEC filings disclose the OCR review.

#### LIT-09: Deal brief assumption on litigation is out of date
- **Finding:** These events all came after or around the FY2025 10-K: the CID (February 11, 2026), the breach (April 18, 2026), the OCR review (July 8, 2026), the Markman loss (August 12, 2026), the FCA intervention (August 18, 2026) and the US$68.0m damages report (September 25, 2026). The model assumption of "no material litigation or regulatory costs beyond those described in the FY2025 10-K" is therefore out of date.
- **Evidence:** Docket dates as cited in LIT-01 to LIT-08.
- **Source:** `docket_index.csv` and detail files LIT-001 to LIT-003
- **Severity:** High
- **Confidence:** Medium (inferred from several docket entries compared with the brief)
- **Deal impact:** Valuation. The model needs litigation scenarios.
- **Cross-check:** Find the 10-K filing date and its legal proceedings section.

### Docket event timeline (for comparison with SEC filing dates)

| Date | Matter | Event | Source |
|---|---|---|---|
| 2024-03-18 | LIT-001 | Qui tam complaint filed under seal | LIT-001 file |
| 2024-05-16 | LIT-001 | First seal extension granted | LIT-001 file |
| 2024-09-12 | LIT-004 | Hollis complaint filed | LIT-004 file |
| 2024-11-12 to 2026-05-20 | LIT-001 | Five more seal extensions granted | LIT-001 file |
| 2024-11-18 | LIT-004 | Corvane motion to dismiss | LIT-004 file |
| 2025-04-02 | LIT-002 | Genaro complaint filed | LIT-002 file |
| 2025-04-03 | LIT-004 | Hearing; limited discovery allowed | LIT-004 file |
| 2025-06-20 | LIT-002 | Corvane answer and counterclaims | LIT-002 file |
| 2025-12-15 | LIT-002 | PTAB denies IPR institution | LIT-002 file |
| 2026-02-11 | LIT-001 | CID served on Corvane (per status report) | LIT-001 file |
| 2026-03-02 | LIT-001 | Government sealed status report | LIT-001 file |
| 2026-03-10 | LIT-004 | Renewed motion to dismiss | LIT-004 file |
| 2026-04-18 | LIT-003 | Ransomware intrusion (alleged) | LIT-003 file |
| 2026-04-24 | LIT-003 | Forensic preliminary findings of exfiltration (alleged) | LIT-003 file |
| 2026-04-27 | LIT-003 | Corvane Form 8-K, "no evidence" of exfiltration (as quoted by plaintiffs) | LIT-003 file |
| 2026-05-04 | LIT-003 | First complaint (Ortega) filed | LIT-003 file |
| 2026-05-20 | LIT-006 | DEQ notice of violation filed | docket index |
| 2026-06-09 | LIT-004 | Dismissed with prejudice | LIT-004 file |
| 2026-06-12 | LIT-003 | Breach notices mailed to about 412,300 people | LIT-003 file |
| 2026-06-24 | LIT-002 | Markman hearing | LIT-002 file |
| 2026-07-08 | LIT-005 | OCR review opened | docket index |
| 2026-07-09 | LIT-004 | Appeal deadline passes; case closed | LIT-004 file |
| 2026-07-22 | LIT-003 | Last of six related complaints filed | LIT-003 file |
| 2026-08-11 | LIT-006 | Last activity (penalty agreed, corrective action complete) | docket index |
| 2026-08-12 | LIT-002 | Claim construction order for Genaro | LIT-002 file |
| 2026-08-14 | LIT-003 | Seven cases consolidated | LIT-003 file |
| 2026-08-18 | LIT-001 | Government Notice of Election to Intervene in Part | LIT-001 file |
| 2026-08-21 | LIT-001 | Unsealing order; complaint-in-intervention deadline set | LIT-001 file |
| 2026-09-25 | LIT-002 | Genaro damages expert report (US$68.0m) | LIT-002 file |
| 2026-09-28 | LIT-003 | Consolidated class complaint filed | LIT-003 file |
| 2026-10-02 | LIT-002 | Corvane interrogatory response on OncoTrace v3 | LIT-002 file |
| **2026-10-30** | LIT-001 | Government complaint-in-intervention due | LIT-001 file |
| **2026-10-30** | LIT-005 | Corvane response to OCR due | docket index |
| 2026-11-15 | LIT-006 | DEQ civil penalty (US$0.18m) due | docket index |
| 2026-11-20 | LIT-002 | Summary judgment and Daubert motions due | LIT-002 file |
| 2026-11-30 | LIT-003 | Corvane motion to dismiss due | LIT-003 file |
| About 2026-12-29 | LIT-001 | Corvane answer due if served on 2026-10-30 (inference: 60 days after service) | LIT-001 file |
| 2027-01-15 | LIT-002 / LIT-003 | Genaro pretrial conference; class plaintiffs' opposition due | LIT-002, LIT-003 files |
| **2027-02-08** | LIT-002 | Five-day jury trial begins | LIT-002 file |
| Mid-2027 | LIT-002 | Expected OncoTrace v3 launch, subject to NY approval | LIT-002 file |

### Key numbers

| Item | Value | Source |
|---|---|---|
| FCA single damages (relator) | US$96.4m on about 41,200 claims, 2019 to 2025 | LIT-001 file |
| FCA trebled | US$289.2m (17.5% of EV, 23.0% of equity value) | LIT-001 file; my percentages |
| Alleged speaker fees | US$3.2m to 61 physicians | LIT-001 file |
| Genaro past damages | US$68.0m through 2026-06-30 at a 9% royalty (4.1% of EV) | LIT-002 file |
| Implied OncoTrace revenue in the damages period | About US$755.6m (inference) | 68.0 / 0.09 |
| People notified of the breach | About 412,300 | LIT-003 file |
| Cyber insurance limit | US$10.0m (file note citing the 10-Q) | LIT-003 file |
| Hollis claim | US$2.4m, dismissed, no payment | LIT-004 file |
| DEQ penalty | US$0.18m | docket index |

### Matters reviewed with low relevance

- **LIT-004 Hollis v. Corvane:** a wage and hour class claim (about 340 phlebotomists, US$2.4m) that was dismissed with prejudice on 2026-06-09. No appeal was filed by 2026-07-09 and no settlement was paid. I found no link in the litigation records to compliance or whistleblower issues. It is a travel-time overtime claim only. The whistleblower retaliation claim in this portfolio is Whitcomb Count III (LIT-001), on which the government declined to intervene. Severity Low.
- **LIT-006 NC DEQ notice of violation:** a medical waste storage violation at the Durham laboratory. The penalty of US$0.18m is agreed and due 2026-11-15, and corrective action is complete (docket index). Severity Low.

### Gaps and questions for management or outside counsel

1. The per-claim FCA penalty amount and the number of claims tainted by kickbacks under Count II are not found in the litigation records. Outside counsel should give a range of exposure, including how likely exclusion or a Corporate Integrity Agreement is.
2. Did Corvane disclose the February 11, 2026 CID, and has it booked an FCA reserve? When and how did it disclose the August 18, 2026 intervention?
3. What is OncoTrace's revenue and share of the total? The litigation records do not say. Is OncoTrace revenue from Medicare the same revenue base at risk in both the FCA case and the Genaro case?
4. What are counsel's views on summary judgment and trial for Genaro? Is there a design-around timeline, a status for the NY State approval, and any settlement or license talks?
5. Was the April 24, 2026 forensic finding made, and who knew of it before the April 27 8-K was filed? Have any securities class actions or derivative demands been filed? None appears in the docket index.
6. What is the full insurance tower: cyber above US$10.0m, D&O, and any coverage for the FCA and IP cases? Not found in the litigation records.
7. What is the scope of the OCR data request (LIT-005) and the possible penalties? There is no detail file.
8. Whitcomb Count III (retaliation) goes on without the government. What does the relator say about other employees who raised concerns?

This is not legal advice. All items should go to outside counsel.
