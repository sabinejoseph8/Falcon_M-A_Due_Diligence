## Litigation analyst: findings (iteration 2 follow-up, Project Kestrel)

### Files reviewed

- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/deal-brief.md` (context)
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/docket_index.csv`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-002_genaro-v-corvane.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-003_data-security-incident-litigation.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/litigation/LIT-004_hollis-v-corvane.md`

I also ran a keyword search across the litigation folder for: Veltrane, Orvia, recoup, audit, Pruitt, compliance, securities, derivative, SEC, forensic, settle, licens, preliminary injunction, genetic privacy. LIT-005 and LIT-006 exist only as rows in the docket index and have no detail files. None of the files contained text that tried to instruct the agents.

### Matter summary table

| Case ID | Case | Posture | Claimed / exposure | Next date | Severity |
|---|---|---|---|---|---|
| LIT-001 | US ex rel. Whitcomb v. Corvane (FCA qui tam) | Unsealed 2026-08-21. Government intervened in part on 2026-08-18 (Counts I and II, Medicare OncoTrace claims) | US$96.4m single damages alleged; US$289.2m trebled, before per-claim penalties | 2026-10-30, government complaint-in-intervention due | High (set in iteration 1) |
| LIT-002 | Genaro v. Corvane (patent) | Expert discovery. Markman order (2026-08-12) and IPR denial (2025-12-15) both went against Corvane | US$68.0m past damages (plaintiff's expert), plus 9% ongoing royalty or a permanent injunction | 2026-11-20 SJ/Daubert motions; 2027-02-08 jury trial | High |
| LIT-003 | In re Corvane Data Security Incident Litigation | Consolidated complaint filed 2026-09-28 | Not stated; about 412,300 people notified (allegation) | 2026-11-30, motion to dismiss due | High (disclosure) / Medium (money) |
| LIT-004 | Hollis v. Corvane (wage and hour) | Closed. Dismissed with prejudice 2026-06-09, no appeal | US$2.4m claimed; nothing paid | None | Low |
| LIT-005 | HHS OCR compliance review (HIPAA, April 2026 breach) | Open. Data request outstanding | Not stated | 2026-10-30, OCR response due | Medium |
| LIT-006 | NC DEQ notice of violation (Durham medical waste) | Penalty agreed; corrective action complete | US$0.18m | 2026-11-15, penalty payment due | Low |

### Findings

#### LIT-10: Relator Whitcomb was a senior sales executive; the record does not say whom she reported to or mention the compliance function
- **Finding:** Dana Whitcomb was Corvane's Regional Sales Director (Southeast) from 2017 to 2023. She alleges she was demoted and then fired in 2023 "after raising concerns". The record does not say what concerns she raised, to whom, or when. Daniel Pruitt and the compliance function are not mentioned anywhere in the litigation records. The government declined to intervene on Count III (retaliation), so that claim stays with the relator.
- **Evidence:** Caption: "Dana Whitcomb, former Regional Sales Director (Southeast), Corvane Diagnostics, employed 2017 to 2023". Count III: "demoted and then terminated in 2023 after raising concerns." 2026-08-18: the government "declines to intervene on Count III."
- **Source:** `targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`, complaint summary (unsealed 2026-08-21) and docket entry 2026-08-18
- **Severity:** Medium. Count III on its own is a small employment-type claim. Its value is in what it suggests: a sales leader inside the company may have raised concerns internally before the 2024 filing.
- **Confidence:** High for the role, the dates and the declination (court record). Low for the retaliation facts (an untested allegation).
- **Deal impact:** Disclosure and governance. If concerns went to compliance or management in 2023, the question is what Corvane knew before the CID.
- **Cross-check:** The litigation records are silent on whether Pruitt's January 2026 departure (DEF 14A) is linked to this case. It came about one month before the February 11, 2026 CID (inference on timing only, no causal link in the records). Ask management for Whitcomb's hotline or compliance reports, the investigation file, and Pruitt's departure terms.

#### LIT-11: The complaint's speaker fees average about US$7,500 per physician per year, not US$40,000
- **Finding:** Count II alleges US$3.2m in speaker fees paid to 61 physicians from 2019 to 2025. That is about US$52,500 per physician over seven years, or about US$7,500 per physician per year. Bearhaven's figure of US$40,000 a year is about 5.3 times higher. The "dozens of physicians" description does match the 61 named in the complaint.
- **Evidence:** Count II: "Corvane paid US$3.2 million in 'speaker fees' from 2019 to 2025 to 61 physicians who were among its highest-volume ordering physicians."
- **Calculation:** 3.2 / 61 = US$0.0525m (about US$52,459) per physician. Over 7 years (2019 to 2025 inclusive) that is about US$7,494 per year. At Bearhaven's rate, 61 physicians x US$40,000 x 7 years = US$17.1m, versus US$3.2m in the complaint.
- **Possible reconciliation (inference):** if each physician was paid in only about 1.3 of the 7 years (52,459 / 40,000), an average of US$40,000 "per paid year" could fit. The complaint does not give a year-by-year split.
- **Source:** `targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`, Count II (complaint unsealed 2026-08-21)
- **Severity:** Medium (a discrepancy between sources). The kickback theory itself stays serious because the government intervened on Count II (2026-08-18).
- **Confidence:** Medium. The inputs are in the court record, but the figures are allegations, and the annual average is my calculation.
- **Deal impact:** Valuation and disclosure. The short report may overstate fee levels, or it may use a different population or period.
- **Cross-check:** Open Payments data and Corvane's speaker program ledger. Also ask how Bearhaven defined "a year".

#### LIT-12: Genaro royalty exposure is about 14.1% of EV if the royalty runs indefinitely (projection), and much lower if OncoTrace v3 launches on time
- **Finding:** Genaro's expert claims US$68.0m in past damages through June 30, 2026, plus a 9% ongoing royalty on OncoTrace net revenue.
- **Calculation (projection):**
  - Applying 9% to FY2025 OncoTrace revenue of about US$138.5m gives about US$12.5m a year.
  - Capitalized at 13.2x, that is about US$164.5m, or 10.0% of the US$1,648.6m EV. The unrounded figure is 9.98%, so this falls just short of the 10% test.
  - Adding the US$68.0m in past damages gives about US$232.5m, or 14.1% of EV.
  - Past damages alone are 4.1% of EV.
- **Why the projection overstates exposure:**
  - Corvane says a design-around, OncoTrace v3, is expected "in mid-2027, subject to New York State approval" (2026-10-02). If it launches then, the royalty would run for about one year (roughly US$12.5m), not in perpetuity.
  - Capitalizing a pre-tax royalty at an EBITDA multiple is a rough proxy.
- **What could make exposure larger:**
  - The 9% royalty, applied to US$76.2m of Medicare-paid panel revenue, is a small part of Count I's scope. That is separate exposure, not double counting.
  - Enhanced damages for willfulness could add to it. Whether Genaro pleads willfulness is not found in litigation records.
- **Gaps:** the start date of the damages period is not found in litigation records. The complaint was filed 2025-04-02, but the expert report entry gives only the end date. No statement about OncoTrace's share of revenue is found in litigation records.
- **Evidence:** 2026-09-25: "reasonable royalty of 9% of OncoTrace net revenue, past damages of US$68.0 million through June 30, 2026, plus an ongoing royalty or a permanent injunction."
- **Source:** `targets/kestrel/data/litigation/LIT-002_genaro-v-corvane.md`, docket entries 2026-09-25 and 2026-10-02
- **Severity:** High. The more than 10% Critical test is met only under the indefinite-royalty projection, and the court record partly contradicts that projection (v3 timing). I recommend that the lead treat it as Critical if v3 slips or fails NY approval.
- **Confidence:** Medium. The figures are plaintiff's expert numbers, untested by the court. The revenue input comes from financial data, and the calculation is mine.
- **Deal impact:** Valuation. This needs a specific indemnity or escrow sized to past damages plus the royalty to the v3 launch, and a price adjustment if v3 is uncertain.
- **Cross-check:** Corvane's rebuttal expert report (not found in litigation records), 10-Q accrual or disclosure for Genaro, and the v3 validation timeline and NY submission status.

#### LIT-13: Genaro seeks a permanent injunction, not a preliminary one, and the jury trial is before closing
- **Finding:** The docket shows no motion for a preliminary injunction. Genaro seeks a permanent injunction "against further sales of the accused version of OncoTrace". Trial starts 2027-02-08, before the planned Q2 2027 closing. That is about four months before v3's "mid-2027" target launch. No settlement or license talks are found in litigation records.
- **Trend:** against Corvane. The IPR was denied (2025-12-15), the Markman order adopted Genaro's construction of both disputed terms (2026-08-12), and Genaro's damages report followed (2026-09-25).
- **Evidence:** Claims section: "Genaro seeks damages and a permanent injunction against further sales of the accused version of OncoTrace." 2026-08-12: "The court adopts Genaro's proposed construction of the two disputed terms."
- **Source:** `targets/kestrel/data/litigation/LIT-002_genaro-v-corvane.md`, Claims section and docket entries 2025-12-15, 2026-08-12, 2026-10-02
- **Severity:** High. OncoTrace is 32.1% of FY2025 revenue (financial data). An injunction granted after a February 2027 verdict and before v3 launches could hit that revenue between signing and closing, and could be argued as an MAE.
- **Confidence:** High for the docket posture. The outcome and timing of any injunction are unknown.
- **Deal impact:** Closing risk and valuation. Consider an explicit treatment of the Genaro outcome in the MAE definition, a closing condition or price mechanism tied to the verdict, and a covenant on settlement or licensing.
- **Cross-check:** Ask outside counsel about the likelihood of an injunction after trial, given that a royalty is offered as the alternative, and about the status of any license talks.

#### LIT-14: Breach plaintiffs allege the forensic firm found exfiltration three days before the 8-K said there was no evidence of it
- **Finding:** Plaintiffs allege the following timeline, citing an internal timeline produced in early discovery.

| Date | Alleged event |
|---|---|
| April 18, 2026 | Ransomware attack; about 1.1 TB of data taken |
| April 24, 2026 | Outside forensic firm gives preliminary findings of exfiltration |
| April 27, 2026 | 8-K states "no evidence at this time that patient information was exfiltrated" |
| June 12, 2026 | Notification letters mailed to about 412,300 individuals |

  The letters went out 55 days after the attack and 49 days after the alleged findings. Plaintiffs also allege that a remote-access account the attackers used had no MFA.
- **Not found in litigation records:** the forensic firm's name, and any state genetic privacy law by name or statutory damages per person.
- **Evidence:** "Corvane's outside forensic firm gave Corvane preliminary findings of data exfiltration on April 24, 2026." "Corvane failed to use multi-factor authentication on a remote-access account that the attackers used."
- **Source:** `targets/kestrel/data/litigation/LIT-003_data-security-incident-litigation.md`, consolidated complaint allegations (filed 2026-09-28)
- **Severity:** High. If proven, the 8-K statement was inaccurate when made. That creates securities disclosure risk, not just consumer exposure.
- **Confidence:** Low. These are pleading allegations, untested. They are somewhat stronger because plaintiffs cite a discovery document.
- **Deal impact:** Disclosure, valuation and indemnity. A specific indemnity is needed for breach liabilities, including OCR (LIT-005).
- **Cross-check:**
  - Ask management for the forensic firm's engagement letter and its April 24 deliverable.
  - Check whether any later 8-K or the 10-Q corrected the April 27 statement.
  - Check whether exposure exceeds the US$10.0m cyber insurance limit. That figure is cited in the detail file's notes as coming from the 10-Q, not from a court record.

#### LIT-15: No securities class action, derivative suit or SEC inquiry appears in the litigation records
- **Finding:** The docket index lists six matters, and none is a securities, derivative or SEC matter. Given the alleged 8-K inaccuracy (LIT-14), the CID disclosure timing (LIT-17) and the May 2026 short report, such claims may still be filed (inference).
- **Evidence:** In `docket_index.csv`, matter types are FCA, patent, data breach class action, employment, HIPAA inquiry and environmental.
- **Source:** `targets/kestrel/data/litigation/docket_index.csv`, all rows
- **Severity:** Low as a current matter. Treat it as a watch item.
- **Confidence:** High that none appears in these records. Records outside this folder may differ.
- **Deal impact:** Disclosure. Ask for a bring-down representation and a litigation search before signing.
- **Cross-check:** SEC filings and news for any shareholder suit or SEC comment letter.

#### LIT-16: No docket entry mentions Veltrane, Orvia, Medicare recoupment or payer audits
- **Finding:** A keyword search found no reference to Veltrane, Orvia, recoupment or audits. The only Medicare-related content is LIT-001: the FCA claims, and the note that liability can lead to exclusion and settlements often include a Corporate Integrity Agreement.
- **Evidence:** Not found in litigation records.
- **Source:** all files in `targets/kestrel/data/litigation/`
- **Severity:** Low
- **Confidence:** High for the absence in these files.
- **Deal impact:** None from litigation. Any Veltrane, Orvia or payer audit risk must come from other sources.
- **Cross-check:** SEC, news and financial analysts.

#### LIT-17: The CID was served 22 days before the 10-K, the government called the investigation "active" 3 days before the 10-K, and the first disclosure came 175 days after service
- **Finding:** The government's status report confirms the CID was served February 11, 2026. That report, dated 2026-03-02, says "The investigation is active." The FY2025 10-K, filed March 5, 2026, does not mention the CID and says Corvane is "not aware of any pending government investigation that we expect to be material" (SEC fact supplied by the lead). The Q2 10-Q first disclosed the CID on August 5, 2026, 175 days after service.
- **Evidence:** 2026-03-02: "The United States served a civil investigative demand on Corvane on February 11, 2026. The investigation is active."
- **Source:** `targets/kestrel/data/litigation/LIT-001_us-ex-rel-whitcomb-v-corvane.md`, docket entry 2026-03-02 (unsealed 2026-08-21)
- **Severity:** High. This is a disclosure-control and governance issue that bears on IC question 5. It also means the deal brief's assumption of "no material litigation or regulatory costs beyond those described in the FY2025 10-K" is stale.
- **Confidence:** High for the court dates. The filing dates and quotes come from the SEC analyst, as supplied by the lead.
- **Deal impact:** Disclosure, plus a FCA indemnity or escrow. Also check whether the 10-K's materiality judgment was reasonable given that the government said on March 2 that the investigation was active.
- **Cross-check:**
  - The 10-K's exact wording, and when the CID response was internally escalated.
  - Whether Corvane knew of the sealed qui tam before the CID. The record does not say.
  - Disclosure committee minutes.

#### LIT-18: Other event dates to compare with filings
- **Finding:** These court and agency events need a disclosure check against the SEC record.

| Event (court record) | Event date | Nearest filing | Gap to check |
|---|---|---|---|
| PTAB denies IPR of '318 patent | 2025-12-15 | 10-K, 2026-03-05 | Did the 10-K disclose the denial? |
| Breach class actions filed (7 cases) | 2026-05-04 to 2026-07-22 | 10-Q, 2026-08-05 | Disclosed in 10-Q? |
| NC DEQ notice of violation | 2026-05-20 | 10-Q, 2026-08-05 | Minor (US$0.18m) |
| HHS OCR compliance review opened | 2026-07-08 | 10-Q, 2026-08-05 | Disclosed in 10-Q? |
| Genaro Markman order (adverse) | 2026-08-12 | After 10-Q | Any 8-K? |
| Government intervenes in part in FCA case | 2026-08-18 | After 10-Q | Any 8-K? Material change from the 10-Q |
| Complaint unsealed | 2026-08-21 | After 10-Q | Any 8-K? |
| Genaro damages report, US$68.0m | 2026-09-25 | After 10-Q | Next 10-Q (Q3) |
| Corvane says v3 expected mid-2027 | 2026-10-02 | Court filing only | Was the design-around plan disclosed to investors? |

- **Evidence:** the docket entries cited in each row.
- **Source:** `targets/kestrel/data/litigation/docket_index.csv`; `LIT-001_...md` entries 2026-08-18 and 2026-08-21; `LIT-002_...md` entries 2025-12-15, 2026-08-12, 2026-09-25, 2026-10-02; `LIT-003_...md` entries 2026-05-04 to 2026-07-22
- **Severity:** Medium
- **Confidence:** High for the court dates. Whether each item was disclosed is unknown from these records.
- **Deal impact:** Disclosure. It also shows which events the deal brief model (as of June 30, 2026) did not reflect.
- **Cross-check:** the SEC filings analyst should confirm each row.

### Matters reviewed with low relevance

- **LIT-004 Hollis:** dismissed with prejudice 2026-06-09. No appeal was filed by 2026-07-09, and no settlement was paid. No exposure.
- **LIT-006 NC DEQ:** US$0.18m penalty due 2026-11-15. Corrective action is complete (2026-08-11).
- **LIT-005 HHS OCR:** an open HIPAA review tied to the April 2026 breach, with the response due 2026-10-30. No amount is stated and there is no detail file. Medium as part of the breach indemnity package.

### Gaps and questions for management or outside counsel

1. What did Whitcomb report internally, to whom and when? Did any of it reach CCO Daniel Pruitt? What were the reasons for and terms of Pruitt's January 2026 departure? (Not found in litigation records.)
2. What is the year-by-year speaker fee ledger for the 61 physicians, and how does it compare with Bearhaven's US$40,000 a year?
3. What is the per-claim penalty count, and has the government quantified damages ahead of its October 30, 2026 complaint-in-intervention? What is the status of any settlement or Corporate Integrity Agreement talks?
4. For Genaro: what is the start date of the damages period, whether willfulness is pleaded, whether any license or settlement talks are under way, what Corvane's rebuttal damages figure is, and how certain the v3 validation and NY approval timeline is.
5. Who is the forensic firm, what did it deliver on April 24, 2026, and who saw it before the April 27 8-K? Which state genetic privacy laws are pleaded, and what statutory damages per person do they allow?
6. Is the US$10.0m cyber insurance limit the full coverage? What is the retention, and has the carrier issued any reservation of rights?
7. Have any securities, derivative or books-and-records demands been received but not filed?
8. Why did Corvane conclude in the March 5, 2026 10-K that the CID was not material, when the government reported on March 2, 2026 that the investigation was active?

This is not legal advice. All items should go to outside counsel.
