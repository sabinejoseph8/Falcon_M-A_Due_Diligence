## Litigation analyst: findings

### Files reviewed

- `data/deal-brief.md` (deal context only)
- `data/litigation/docket_index.csv` (six matters: LIT-001 to LIT-005 and REG-001)
- `data/litigation/LIT-001_vantor-v-talonfield.md`
- `data/litigation/LIT-002_ruiz-v-talonfield.md`
- `data/litigation/LIT-003_securities-class-action.md`
- `data/litigation/LIT-004_pinecrest-v-talonfield.md`

LIT-005 and REG-001 have no detail file because their `detail_file` field in the index is blank. I reviewed them from their index rows. There are no other files in `data/litigation/`, and I read no other folders.

### Matter summary table

| Case ID | Case | Posture | Claimed / exposure | Next date | Severity |
|---|---|---|---|---|---|
| LIT-001 | Vantor Robotics v. Talonfield (D. Del., patent) | Active. Markman order adopted Vantor's construction on 3 of 4 terms (2026-07-22); stay denied (2026-09-25); mediation ordered (2026-10-05); jury trial 2027-03-08 | Complaint: "not less than $140 million". Vantor expert: $96.4M reasonable royalty through the trial date (2026-09-04). Enhanced damages and a permanent injunction on Gen-3 sales sought. No contractual cap | PTAB '812 decision expected Nov 2026; expert discovery closes 2026-11-20 | Critical |
| LIT-002 | Ruiz et al. v. Talonfield Field Services LLC (Cal. Super. Ct., Alameda; wage and hour class action) | Settled; preliminary approval 2026-05-20 | $3.2M settlement including fees and costs (2025-12-09) | Final approval hearing 2026-11-13 | Low |
| LIT-003 | In re Talonfield Systems Securities Litigation (S.D. Ohio; Exchange Act 10(b) and 20(a)) | Active; pleadings stage; institutional lead plaintiff appointed 2026-09-10 | Not stated in the complaint; cannot be quantified from the records | Amended complaint due 2026-11-09; motion to dismiss expected 2027-01-08 | High |
| LIT-004 | Pinecrest Distribution v. Talonfield (Franklin County, Ohio; contract and negligence) | Active; pleadings stage; Talonfield motion to cap damages filed 2026-08-29 | $12.0M claimed, against a cap of 12 months' fees, about $1.4M by Talonfield's estimate (answer 2026-08-01) | Hearing on the motion 2026-11-05 | Medium |
| LIT-005 | Delmarco Electrical Contractors v. Talonfield (Franklin County, Ohio; unpaid invoice / mechanics lien) | Closed; dismissed after settlement 2025-08-11 | $0.4M claimed; settlement amount not found in litigation records | None | Low |
| REG-001 | OSHA inspection 1590442, Columbus assembly facility | Closed; penalty paid 2025-09-02 | $48 thousand paid (index shows $0.05M) | None | Low |

Notes:
- The amounts stated for open matters add up to $101.0M to $155.2M (see LIT-04). Implied equity value is about $1,159M. These totals leave out enhanced damages, any injunction effect, LIT-003 and defense costs.
- Each of Talonfield's three business lines has an open matter:
  - robots: LIT-001, plus LIT-003 on hardware revenue recognition;
  - FieldOS software: LIT-004;
  - field services: LIT-002.
- The index amount for LIT-001 ($140.0M) is the complaint figure. It does not reflect the 2026-09-04 expert figure or the injunction request.

### Findings

Finding IDs LIT-01 to LIT-11 are not the same as docket case IDs (LIT-001 to LIT-005, REG-001). LIT-01 to LIT-03 are parts of one Critical matter (Vantor). LIT-04 adds up all open matters, so do not add it to them.

#### LIT-01: Vantor patent case has turned against Talonfield since the July 2026 Markman order
- **Finding:** Risk in the Vantor case has increased since the July 22, 2026 claim construction order. The order adopted Vantor's construction on three of four disputed terms, including "localization map" in the '557 patent. Since then the case has been widened to the Gen-3 Plus variant, and the court refused to stay it for the PTAB review, which covers only the '812 patent.
- **Evidence:**
  - 2026-07-22: "The court adopts Vantor's proposed construction for three of the four disputed terms". Commentators, not the court, say the term is "central to how the Talon Gen-3 navigation system works".
  - 2026-08-14: "Vantor serves amended infringement contentions adding the Talon Gen-3 Plus variant."
  - 2026-09-25: "Court denies Talonfield's motion to stay the case pending the PTAB decision on the '812 patent." and "The '557 and '094 patents are not affected by the IPR."
  - 2025-05-15: "PTAB denies institution of IPR on the '557 patent."
- **Source:** `data/litigation/LIT-001_vantor-v-talonfield.md`, docket entries 2025-05-15, 2026-07-22, 2026-08-14, 2026-09-25
- **Severity:** Critical
- **Confidence:** High for the rulings, which are court orders. The link between "localization map" and Gen-3 navigation comes from commentators, not from a court finding (Medium).
- **Deal impact:** Valuation and closing risk (IC Q2).
  - The PTAB declined to review the '557 patent, which contains the key term. No IPR petition on the '094 patent appears in the records; the 2024-11-04 petitions covered only '557 and '812. A favorable '812 decision in November 2026 would narrow the case but would not remove the core risk.
  - No ruling on Talonfield's non-infringement and invalidity counterclaims (2024-05-20) appears in the records.
  - Before the March 8, 2027 trial, the remaining ways out are summary judgment (motions due 2026-12-18) and the December 2026 mediation the court ordered on 2026-10-05. The mediation is the main chance to settle.
- **Cross-check:** SEC filings: whether Talonfield disclosed the Markman outcome, whether it still calls its defenses strong, and how it describes the PTAB review. News: commentary on the ruling and statements by Vantor.

#### LIT-02: Vantor will seek a permanent injunction against sales of Talon Gen-3 robots
- **Finding:** Vantor has told the court it will seek a permanent injunction against sales of Talon Gen-3 robots, and the Gen-3 Plus variant is now accused too. If granted, the injunction could stop sales of the accused robots, which belong to the robot business behind Arbelion's plan to enter warehouse automation. Their share of revenue is not found in litigation records.
- **Evidence:** 2026-09-04: "Vantor will seek a permanent injunction against sales of Talon Gen-3 robots". Case header: relief sought includes "a permanent injunction"; accused products are "Talon Gen-3 robots; Talon Gen-3 Plus added August 2026". 2026-08-14: amended contentions "adding the Talon Gen-3 Plus variant".
- **Source:** `data/litigation/LIT-001_vantor-v-talonfield.md`, case header and docket entries 2026-08-14, 2026-09-04
- **Severity:** Critical
- **Confidence:** High that Vantor is seeking an injunction, because a public letter on the docket says so. Whether a court would grant it has not been tested. The records show no preliminary injunction motion. On the current schedule, an injunction would normally come only after a liability finding at or after the March 8, 2027 trial (counsel to confirm).
- **Deal impact:** Valuation, closing risk and post-closing (IC Q2, Q6).
  - Illustrative sensitivity, not a forecast: at the deal's multiple of about 11.5x, each $10.0M of lost annual Adjusted EBITDA removes about $115.0M of value, about 10% of equity value. $10.0M is about 8.5% of the $118.0M FY2026E figure.
  - Customers may hold back orders for accused robots while the request is pending.
  - The request targets "sales". The records do not say how it would affect servicing of installed robots or FieldOS subscriptions.
  - Protections to discuss with counsel: a closing condition or walk right tied to an injunction or an adverse verdict on Gen-3 or Gen-3 Plus; Arbelion's consent before any settlement or license is agreed before closing; and diligence on design-around options.
- **Cross-check:** SEC filings and financials: revenue, margin and installed base of Gen-3 and Gen-3 Plus, and risk factor language on injunction risk. News: customer reactions or delayed orders.

#### LIT-03: Vantor damages run from a $96.4M expert figure to "not less than $140 million", with no cap
- **Finding:** Vantor's damages expert calculates reasonable-royalty damages of $96.4M through the trial date. That is below the complaint's "not less than $140 million", and Vantor also seeks enhanced damages for willful infringement. No contractual cap applies, and Talonfield's own damages figure is not found in litigation records.
- **Evidence:** 2026-09-04: "Vantor's expert calculates reasonable-royalty damages of $96.4 million through the trial date". Case header (complaint, 2024-03-11): damages "not less than $140 million" and "enhanced damages for willful infringement". 2024-03-11: "Vantor alleges willful infringement".
- **Source:** `data/litigation/LIT-001_vantor-v-talonfield.md`, case header and docket entries 2024-03-11, 2026-09-04
- **Severity:** Critical
- **Confidence:** High that these are Vantor's stated figures, because they appear in the court record. Both are one party's positions that the court has not tested, and the expert report is under seal.
- **Deal impact:** Valuation (IC Q2, Q6).
  - Before tax, $96.4M is about $2.00 per share (8.3% of equity value) and $140.0M is about $2.90 per share (12.1%).
  - What could raise exposure:
    - a willfulness finding. US patent law lets a court increase damages up to three times. On the expert figure that gives a legal ceiling of $289.2M; this is a ceiling, not a forecast, and counsel should assess it.
    - sales after the trial date, which the $96.4M does not cover.
    - adding Gen-3 Plus, if the figure leaves it out (the records do not say).
    - defense costs through trial.
  - What could lower exposure: PTAB invalidation of '812 claims (November 2026), summary judgment (motions due 2026-12-18), Talonfield's rebuttal expert, or a settlement at the December 2026 mediation.
  - In a one-step merger with a public company, an indemnity or escrow from the target's shareholders is generally not available (counsel to confirm). The available tools are price, contingent payments, closing conditions and consent rights before closing.
- **Cross-check:** SEC filings: any accrual or disclosed range of reasonably possible loss. Financials: legal reserves and legal spending, and whether defense costs are added back to Adjusted EBITDA.

#### LIT-04: Stated amounts for open matters total $101.0M to $155.2M, before the largest unknowns
- **Finding:** Using the figures in the records, open matters total:
  - $101.0M at the low end (Vantor expert figure, Ruiz settlement, Pinecrest cap estimate);
  - $155.2M at the high end (Vantor complaint floor, Ruiz settlement, full Pinecrest claim).

  That is 8.7% to 13.4% of the implied equity value of about $1,159M. The totals leave out enhanced damages, any injunction effect, the unquantified securities class action and defense costs, and they are not a range of likely outcomes.
- **Evidence:** LIT-001 2026-09-04: "$96.4 million through the trial date"; complaint: "not less than $140 million". LIT-002 2025-12-09: "settlement in principle for $3.2 million". LIT-004: "Amount claimed: $12.0 million"; answer (2026-08-01): cap "at about $1.4 million". LIT-003: "No damages amount is stated in the complaint." Deal brief: "Implied equity value: about $1,159 million."
- **Source:** `data/litigation/LIT-001_vantor-v-talonfield.md`, case header and docket entry 2026-09-04; `data/litigation/LIT-002_ruiz-v-talonfield.md`, docket entry 2025-12-09; `data/litigation/LIT-004_pinecrest-v-talonfield.md`, case header and docket entry 2026-08-01; `data/litigation/LIT-003_securities-class-action.md`, docket summary; `data/deal-brief.md`, The deal
- **Severity:** Critical
- **Confidence:** Medium. Each input is in a court record, but they are party positions of different kinds. The totals are my own pre-tax arithmetic: 96.4 + 3.2 + 1.4 = 101.0, and 140.0 + 3.2 + 12.0 = 155.2.
- **Deal impact:** Valuation and balance sheet (IC Q2, Q4, Q6).
  - Per share, the totals are $2.09 to $3.21, against the $24.00 offer.
  - Vantor makes up 90% or more of each total.
  - Likely litigation payments should be treated as debt-like items when moving from enterprise value to equity value. The deal brief's valuation basis mentions no litigation reserve.
  - The Ruiz amount may already be accrued (confirm).
- **Cross-check:** SEC filings and financials: accruals, disclosed ranges of reasonably possible loss, and expected insurance recoveries for each matter.

#### LIT-05: Court dates crowd the IC and exclusivity window, and the Vantor trial likely lands before or around closing
- **Finding:** Four dated court events fall between November 5 and November 20, 2026, around the November 6 IC, and the PTAB '812 decision is also expected in November. Vantor's expert discovery closes on November 20, the same day exclusivity expires. The Vantor jury trial on March 8, 2027 is likely to fall before or around a closing several months after November 2026, so a verdict and an injunction request could arrive between signing and closing.
- **Evidence:**
  - 2026-11-05 (LIT-004): "Hearing on Talonfield's motion." This is the day before the IC.
  - 2026-11-09 (LIT-003): "Consolidated amended complaint due." This is the next business day after the IC.
  - 2026-11-13 (LIT-002): "Final approval hearing scheduled."
  - November 2026 (LIT-001, entry 2026-09-25): "A PTAB final written decision on the '812 patent is expected in November 2026."
  - 2026-11-20 (LIT-001): "Close of expert discovery: November 20, 2026". Deal brief: exclusivity "expires November 20, 2026".
  - December 2026 (LIT-001, entry 2026-10-05): "Mediation scheduled for December 2026."
  - 2026-12-18 (LIT-001): "Summary judgment motions due: December 18, 2026"
  - 2027-01-08 (LIT-003): "Defendants' motion to dismiss due (expected)."
  - 2027-03-08 (LIT-001, entry 2025-09-30): "Jury trial set for March 8, 2027."
- **Source:** `data/litigation/docket_index.csv`, next_event_date column; `data/litigation/LIT-001_vantor-v-talonfield.md`, docket entries 2025-09-30, 2026-09-25, 2026-10-05 and Upcoming dates; `data/litigation/LIT-002_ruiz-v-talonfield.md`, 2026-11-13; `data/litigation/LIT-003_securities-class-action.md`, 2026-11-09 and 2027-01-08; `data/litigation/LIT-004_pinecrest-v-talonfield.md`, 2026-11-05; `data/deal-brief.md`, The deal
- **Severity:** High
- **Confidence:** High for the dates, which come from court records and the deal brief. Whether they overlap with closing depends on the deal team's closing timeline, which is not in the litigation records.
- **Deal impact:** Closing risk and terms (IC Q2, Q6).
  - The IC will decide before anyone knows the amended securities complaint or the Ruiz final approval result, and possibly before the PTAB decision.
  - Exclusivity ends before the December mediation.
  - Options for the deal team and counsel:
    - update the review of all dockets just before signing;
    - extend exclusivity past the PTAB decision and the mediation;
    - write merger agreement terms that cover a Vantor verdict or injunction between signing and closing (a closing condition or treatment as a material adverse effect) and give Arbelion consent rights over settlements.
- **Cross-check:** The deal team's signing and regulatory timetable. SEC filings: any disclosed settlement talks.

#### LIT-06: Securities class action is live and unquantified, names the CEO, and will be amended right after the IC
- **Finding:** A federal securities fraud class action names Talonfield, CEO Marcus Hale and former CFO Daniel Okafor, for a proposed class period of March 10, 2025 to May 12, 2026. The court appointed an institutional investor as lead plaintiff on September 10, 2026. The consolidated amended complaint is due November 9, 2026, and the complaint states no damages amount.
- **Evidence:** Case header: "Marcus Hale (CEO); Daniel Okafor (former CFO)" and "Proposed class period: March 10, 2025 to May 12, 2026". 2026-08-03: "Three motions filed." 2026-09-10: "Court appoints an institutional investor as lead plaintiff". 2026-11-09: "Consolidated amended complaint due." Docket summary: "No damages amount is stated in the complaint."
- **Source:** `data/litigation/LIT-003_securities-class-action.md`, case header and docket entries 2026-06-03, 2026-08-03, 2026-09-10, 2026-11-09
- **Severity:** High
- **Confidence:** High, because this is in the court record. The exposure cannot be quantified from the records.
- **Deal impact:** Valuation, post-closing and governance (IC Q2, Q5).
  - Trend: the case is at an early stage and there is no ruling on the merits. But the plaintiffs are organized: three investors moved to lead, and an institutional investor was appointed.
  - The company stays a defendant after a merger, so Arbelion would inherit the defense costs and any settlement not covered by insurance. D&O insurance would offset part of the cost, but its limits are not found in litigation records.
  - The CEO is a named defendant, which matters for decisions on retention and governance.
  - The case alone is unlikely to block closing.
  - The amended complaint may add facts, defendants or a longer class period.
  - The motion to dismiss is expected to be filed by 2027-01-08. The records give no date for a ruling.
- **Cross-check:** SEC filings: the legal proceedings description, D&O insurance, and any filing on the CFO's departure. News: the May 12, 2026 short seller report and how the stock reacted.

#### LIT-07: Securities complaint alleges 2025 revenue was inflated through improper bill-and-hold sales (untested allegation)
- **Finding:** The complaint alleges that Talonfield inflated 2025 revenue with bill-and-hold sales that did not meet accounting requirements, including sales customers had not requested. It also alleges that weaknesses in controls over hardware revenue recognition were not fully disclosed. These allegations are untested, but if proven they would affect the revenue base behind the FY2026E management case.
- **Evidence:** Complaint (2026-06-03): "Defendants inflated reported 2025 revenue by recognizing bill-and-hold sales that did not meet accounting requirements, including sales the customer had not requested." and "Defendants failed to disclose the full extent of control weaknesses over hardware revenue recognition." The complaint says the truth came out through "the November 14, 2025 auditor change disclosure and the May 12, 2026 short seller report, after which the stock fell 18% in one day."
- **Source:** `data/litigation/LIT-003_securities-class-action.md`, Allegations section (complaint, docket entry 2026-06-03)
- **Severity:** High. It would rise to Critical if the allegations are proven at scale.
- **Confidence:** Low. These are allegations in a pleading that the court has not tested.
- **Deal impact:** Valuation and internal controls (IC Q1, Q5). This supports a forensic review of 2025 bill-and-hold transactions before signing.
- **Cross-check:** SEC filings: the revenue policy for bill-and-hold sales, any material weakness disclosures, and the November 14, 2025 auditor change filing and the reasons it gives. Financials: the 2025 quarterly revenue pattern (especially Q4), receivables, and goods held for customers. News: the May 12, 2026 short seller report.

#### LIT-08: The deal model's valuation basis predates every adverse 2026 legal development
- **Finding:** The deal model (v3, September 2026) uses the management case from Talonfield's March 2026 investor day. That case predates:
  - the April 2026 outage behind the Pinecrest suit;
  - the May 12, 2026 short seller report cited in the securities complaint;
  - both lawsuits filed in 2026;
  - every adverse 2026 development in the Vantor case.

  The investor day also falls inside the proposed securities class period. The deal brief mentions no litigation reserve and no downside case for an injunction.
- **Evidence:** Deal brief: "uses the management case presented at Talonfield's March 2026 investor day". LIT-004: "The April 11 to 14, 2026 outage"; complaint filed 2026-06-17. LIT-003: "Proposed class period: March 10, 2025 to May 12, 2026"; complaint filed 2026-06-03. LIT-001: Markman order 2026-07-22; damages report and injunction notice 2026-09-04; stay denied 2026-09-25.
- **Source:** `data/deal-brief.md`, Valuation basis; `data/litigation/LIT-001_vantor-v-talonfield.md`, docket entries 2026-07-22, 2026-09-04, 2026-09-25; `data/litigation/LIT-003_securities-class-action.md`, case header and 2026-06-03; `data/litigation/LIT-004_pinecrest-v-talonfield.md`, key facts and 2026-06-17
- **Severity:** High
- **Confidence:** High for the dates. The litigation records do not quantify the effect on the forecast.
- **Deal impact:** Valuation (IC Q1, Q2, Q6). The model needs a case adjusted for litigation, covering:
  - damages or a settlement;
  - defense costs;
  - a downside for an injunction on Gen-3 and Gen-3 Plus;
  - any adjustment for revenue quality.
- **Cross-check:** Financials: any updated guidance, and 2026 results compared with $560.0M revenue and $118.0M Adjusted EBITDA. SEC filings and news: guidance changes since March 2026.

#### LIT-09: Pinecrest seeks $12.0M against a cap of about $1.4M; the cap motion is heard on November 5
- **Finding:** Pinecrest seeks $12.0M for the April 11 to 14, 2026 FieldOS outage, which stopped robots at four of its distribution centers. Talonfield says a contract cap of 12 months of subscription fees, about $1.4M, applies. The hearing on Talonfield's motion to enforce the cap is on November 5, 2026, the day before the IC.
- **Evidence:** Case header: "Amount claimed: $12.0 million". Key facts: "The April 11 to 14, 2026 outage stopped robots at four Pinecrest distribution centers for about three days." Pinecrest "argues this was gross negligence, which would remove the contract's limitation of liability". Answer (2026-08-01): "capped by contract at 12 months of subscription fees, which it estimates at about $1.4 million". 2026-08-29: "Talonfield motion for partial judgment on the pleadings, seeking to cap damages at the contract limit." 2026-11-05: "Hearing on Talonfield's motion."
- **Source:** `data/litigation/LIT-004_pinecrest-v-talonfield.md`, case header, key facts and docket entries 2026-06-17, 2026-08-01, 2026-08-29, 2026-11-05
- **Severity:** Medium. Raise it to High if Pinecrest is a material customer, if other customers were affected, or if a ruling would weaken similar caps in other FieldOS contracts.
- **Confidence:** High for the parties' positions and the dates, which are in the court record. The claims of gross negligence and an unpatched vulnerability are untested allegations (Low).
- **Deal impact:**
  - The effect on value is small: $12.0M is about 1.0% of equity value.
  - Trend: neutral, since there is no ruling yet. A ruling for Talonfield would cap damages at the contract limit (about $1.4M by Talonfield's estimate). A denial would leave the full $12.0M claim open, which is about 8.6 times the cap estimate.
  - The bigger issues are:
    - the customer relationship (IC Q3);
    - FieldOS reliability and patch management, an integration item after closing;
    - whether FieldOS liability caps will hold.
  - The cap estimate implies Pinecrest pays about $1.4M a year in FieldOS fees. Its other spending with Talonfield is not found in litigation records.
- **Cross-check:** SEC filings: disclosure of the April 2026 outage and its cause, customer concentration, and any cyber incident disclosure. News: coverage of the outage and other affected customers. Financials: service level credits and FieldOS customer losses.

#### LIT-10: Court events since mid-2026 to test against Talonfield's SEC disclosures
- **Finding:** Several court events since June 2026 change the risk in the Vantor, securities and Pinecrest cases. The deal team should test whether Talonfield's filings and its loss contingency accruals or ranges reflect each event, and whether any filing made after an event leaves it out.
- **Evidence:**
  - LIT-001 2026-07-22: "The court adopts Vantor's proposed construction for three of the four disputed terms"
  - LIT-001 2026-08-14: "adding the Talon Gen-3 Plus variant"
  - LIT-001 2026-09-04: "$96.4 million through the trial date"; "Vantor will seek a permanent injunction against sales of Talon Gen-3 robots"
  - LIT-001 2026-09-25: "Court denies Talonfield's motion to stay"; "The '557 and '094 patents are not affected by the IPR."
  - LIT-001 2026-10-05: "Court orders the parties to mediation."
  - LIT-003 2026-06-03 and 2026-09-10: "Class action complaint filed."; "Court appoints an institutional investor as lead plaintiff"
  - LIT-004 2026-06-17 and 2026-08-29: "Complaint filed."; "Talonfield motion for partial judgment on the pleadings"
- **Source:** `data/litigation/LIT-001_vantor-v-talonfield.md`, `data/litigation/LIT-003_securities-class-action.md`, `data/litigation/LIT-004_pinecrest-v-talonfield.md`, docket entries as listed
- **Severity:** Medium. It becomes High if the filings leave out or understate these events.
- **Confidence:** High for the court events. What the filings say is outside my sources.
- **Deal impact:** Disclosure and governance (IC Q5). Tests to run:
  1. Are the Markman outcome, the $96.4M figure, the injunction request, the stay denial and the Gen-3 Plus addition disclosed?
  2. Is the PTAB review described accurately? The PTAB declined to review the '557 patent (2025-05-15), and only the '812 patent is under review.
  3. Does the description of the securities case include the bill-and-hold and control weakness allegations?
  4. Are the April 2026 outage and Pinecrest's gross negligence argument disclosed, and not only the cap?
  5. Is the $3.2M Ruiz settlement accrued?
- **Cross-check:** SEC filings: legal proceedings and risk factors in Forms 10-Q and 10-K, and Form 8-Ks, compared by filing date with each event. News: whether the market learned of these events from the company or from others.

#### LIT-11: Ruiz wage and hour class action settled for $3.2M; final approval hearing November 13
- **Finding:** The California wage and hour class action for about 140 field installation technicians settled for $3.2M, including fees and costs. The court gave preliminary approval on May 20, 2026, and the final approval hearing is on November 13, 2026.
- **Evidence:** 2025-12-09: "Notice of settlement in principle for $3.2 million (inclusive of attorneys' fees and administration costs)." 2026-05-20: "Court grants preliminary approval of the settlement." 2026-11-13: "Final approval hearing scheduled."
- **Source:** `data/litigation/LIT-002_ruiz-v-talonfield.md`, docket entries 2025-12-09, 2026-05-20, 2026-11-13
- **Severity:** Low
- **Confidence:** High, because this is in the court record.
- **Deal impact:**
  - The effect on value is minimal, about 0.3% of equity value. The trend is favorable: the case is moving to closure.
  - After closing, review overtime and meal break practices for field technicians in California and other states.
  - The defendant is the subsidiary Talonfield Field Services LLC.
- **Cross-check:** Financials: the $3.2M accrual and whether it is added back to Adjusted EBITDA. SEC filings: disclosure of the settlement.

### Matters reviewed with low relevance

- **LIT-005, Delmarco Electrical Contractors LLC v. Talonfield Systems, Inc.** (Franklin County, Ohio; unpaid invoice / mechanics lien; $0.4M claimed): "Closed (dismissed after settlement on 2025-08-11)". Index row only, and the settlement amount is not found in litigation records. Confirm the lien was released. Low. Source: `data/litigation/docket_index.csv`, row LIT-005.
- **REG-001, OSHA inspection 1590442, Columbus assembly facility** (opened 2025-06-09; workplace safety citation): "Closed (penalty of $48 thousand paid 2025-09-02)". Index row only, and the nature of the citation is not found in litigation records. Confirm the cited conditions were fixed during environmental, health and safety diligence. Low. Source: `data/litigation/docket_index.csv`, row REG-001.

### Gaps and questions for management or outside counsel

LIT-001 (Vantor)
1. What is Talonfield's rebuttal damages figure, and what is outside counsel's view of liability and damages? Not found in litigation records.
2. Does the $96.4M include Gen-3 Plus, and does the injunction request cover Gen-3 Plus? Not stated.
3. What are the revenue, margin and installed base of Gen-3 and Gen-3 Plus, including linked FieldOS and service revenue? Not found in litigation records.
4. Are there design-around options, and what would they cost and how long would they take? Not found in litigation records.
5. How did the court construe the fourth disputed term? What non-infringement and invalidity defenses remain for the '557 and '094 patents? No IPR on '094 appears in the records.
6. Willfulness: when did Talonfield learn of the patents, and did it get an opinion of counsel? Not found in litigation records.
7. Is Vantor a competitor of Talonfield? This matters for injunction risk. Not found in litigation records.
8. What is the settlement history, and what form might a settlement take (lump sum or running royalty) before the December 2026 mediation? Will Arbelion be consulted?
9. What IP indemnities does Talonfield owe its customers, and has it received any customer notices? Not found in litigation records.
10. Can Arbelion's counsel see the sealed expert reports under a common interest arrangement and the protective order?

LIT-003 (securities)

11. What are the D&O insurance limits, retention and carrier positions, and what indemnification does the company owe Hale and Okafor? Not found in litigation records.
12. Is there any SEC or other regulatory inquiry into revenue recognition? None appears in the docket index; confirm.
13. When and why did Daniel Okafor leave the CFO role? Not found in litigation records.
14. Has there been any internal or audit committee investigation of bill-and-hold sales, or any consideration of a restatement? Not found in litigation records.
15. Review the consolidated amended complaint when it is filed (due 2026-11-09).

LIT-004 (Pinecrest)

16. What does Pinecrest spend with Talonfield in total each year, and what is the status of its contract? Not found in litigation records.
17. Were other customers affected by the April 11 to 14, 2026 outage? Were service level credits issued, and are there other claims or demand letters? Not found in litigation records.
18. What was the root cause of the outage and the "known vulnerability", and how were remediation and patching handled? Not found in litigation records.
19. What exactly does the limitation of liability clause say, is it standard across FieldOS contracts, and is there cyber or technology errors and omissions insurance?

Other matters and general

20. Ruiz: accrual, payment timing, and any objections or opt-outs. Is there similar exposure in other states?
21. Delmarco: settlement amount and lien release. OSHA: details of the citation and whether the conditions were fixed.
22. Is the docket index complete? Ask about threatened claims, demand letters, arbitrations and non-public regulatory matters, and compare with the company's responses to its auditor's legal letters.
23. What are the legal reserves for each matter and the current rate of legal spending, and are litigation costs added back to Adjusted EBITDA?
24. Update all dockets before signing, covering the November 5 ruling, the November 9 amended complaint, the November 13 final approval and the PTAB '812 decision.

This is not legal advice. All items are flagged for outside counsel. This is a fictional case study.
