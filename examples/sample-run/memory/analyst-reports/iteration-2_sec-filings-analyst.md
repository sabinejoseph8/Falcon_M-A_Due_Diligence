## SEC filings analyst: findings

Iteration 2 follow-up on F4 and F5. New findings are SEC-19 to SEC-26. The court and news facts below come from the lead agent and are labeled "per lead". They are not from SEC filings.

**Caveat on the files.** The 10-K, 10-Q and DEF 14A are labeled "EXCERPTS". The 10-Q excerpt has only MD&A, Item 4 and Part II Items 1 and 1A. It has no financial statements or notes. "Not found" below means not found after a full read and a full-text search of these excerpts. The full filings could say more, for example in a contingencies note or a subsequent events note.

### Files reviewed (all read in full)
- `data/deal-brief.md`
- `data/sec-filings/TLFS_10-K_FY2025_excerpts.md` (filed March 9, 2026)
- `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md` (filed August 6, 2026)
- `data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md` (Item 4.01)
- `data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md` (Item 5.02)
- `data/sec-filings/TLFS_DEF14A_2026_excerpts.md` (filed April 24, 2026)

### Findings

**Direct answers**
- **F4:** Neither filing mentions the claim construction order, the PTAB proceedings, or any damages amount (SEC-19 to SEC-21). No statement in the 10-Q is directly contradicted by the court record. But on its filing date the 10-Q's description was incomplete: it leaves out the July 22 order, issued 15 days earlier, and repeats "without merit" (SEC-20). The $96.4M figure and the other August and September events came after every filing in the set (SEC-22).
- **F5(a):** No. There is no Item 1.05 8-K in the set, and no 8-K of any kind about the April incident (SEC-23).
- **F5(b):** No. The 10-Q never mentions ransomware or the group's claim that it took data (SEC-24).
- **F5(c):** No on both counts. The 10-Q never names Norvale and says nothing about Kinetic Aisle or the pilots. Its concentration risk factor is unchanged (SEC-25).

#### SEC-19: Vantor case: exact 10-K and 10-Q wording, and what the 10-Q dropped
- **Finding:** Vantor appears only in the 10-K (Item 3 and one risk factor) and in the 10-Q (Part II, Item 1). Neither gives a damages amount. The 10-Q keeps "without merit" and "no accrual", and adds the discovery status and a trial date. It drops the 10-K's description of the claims and the 10-K's statement on whether a loss is probable or can be estimated.
- **Evidence, 10-K Item 3 (complete text after the caption "U.S. District Court for the District of Delaware, filed March 2024"):** (1) "Vantor alleges that the navigation system in our Talon Gen-3 robots infringes three of its patents and seeks damages and an injunction." (2) "We believe the claims are without merit and intend to defend ourselves vigorously." (3) "We have not recorded an accrual because we do not believe a loss is probable, and we cannot reasonably estimate a possible loss or range of loss."
- **Evidence, 10-K Item 1A:** "An adverse outcome could require us to pay substantial damages or royalties, redesign our products, or stop selling Talon Gen-3 robots."
- **Evidence, 10-Q Part II Item 1 (complete text):** "The case is in discovery. Trial is currently scheduled for March 2027. We continue to believe the claims are without merit, and we have not recorded an accrual."
- **Interpretation:** A shorter update in a 10-Q is normal. But the 10-Q excerpt no longer says whether a loss is reasonably possible or can be estimated. When a loss is reasonably possible and not accrued, ASC 450 requires an estimate of the possible loss, or a statement that it cannot be estimated. The full 10-Q notes may cover this.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 3. Legal Proceedings" and "Item 1A. Risk Factors (selected)"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1. Legal Proceedings"
- **Severity:** Medium
- **Confidence:** High for the wording, which is quoted exactly. Medium for the full 10-Q, because we only have an excerpt.
- **Deal impact:** Disclosure. The filings give no number we can use to size the Vantor exposure.
- **Cross-check:** The full 10-Q contingencies note. The litigation analyst should confirm the March 2027 trial date, which is not in the court facts I was given.

#### SEC-20: The 10-Q leaves out the July 22, 2026 claim construction order, issued 15 days before filing
- **Finding:** The 10-Q (filed August 6, 2026) does not mention the July 22 claim construction order. It also says no risk factors changed except the new securities litigation one, so the 10-K patent risk factor was not updated.
- **Evidence:** No filing contains "claim construction", "Markman" or "localization". July 22 to August 6 is 15 days. 10-Q: "There have been no material changes to the risk factors in our 2025 Form 10-K, except for the following addition:" (the addition is securities litigation).
- **Court record (per lead):** The order adopted Vantor's construction for 3 of the 4 disputed terms, including "localization map". The view that this term is central to Gen-3 navigation comes from commentators, a secondary source.
- **Interpretation:** No 10-Q statement is directly contradicted. "In discovery" may have been literally true, since expert damages work was still going on September 4. But the description is stale and incomplete. The order went against Talonfield on the very feature the 10-K says is accused ("the navigation system in our Talon Gen-3 robots"). Even so, the 10-Q repeats "without merit" without any qualification. The order came after the June 30 quarter end, so one could argue it belonged in Q3 reporting. Against that, it came before filing, Talonfield had it as a party to the case, and it was relevant to the ASC 450 judgment. Whether leaving it out broke disclosure rules is a question for counsel.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "Part II, Item 1. Legal Proceedings" and "Part II, Item 1A. Risk Factors"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Item 3. Legal Proceedings"
- **Severity:** High
- **Confidence:** High for the excerpt (read in full and searched). Medium for the full 10-Q, whose notes are not in the excerpt. The court facts come through the lead.
- **Deal impact:** Disclosure and valuation. Management's public position lagged behind the court record. A securities class action about revenue and internal controls is already pending, and this omission could give plaintiffs another disclosure claim. Do not size the Vantor exposure from the filings.
- **Cross-check:** Litigation analyst: the docket date of the order and any motion for reconsideration. Talonfield's August 2026 earnings release or call (not in the set).

#### SEC-21: Neither filing discloses the PTAB outcome of May 15, 2025
- **Finding:** Neither filing mentions the inter partes review petitions or the PTAB decisions. The 10-K was filed 298 days after those decisions. It refers only to "three of its patents" and does not name them.
- **Evidence:** No filing contains "PTAB", "inter partes", "IPR", "Patent Trial", "institut", "'557" or "'812". The 10-Q was filed 448 days after the PTAB decisions.
- **Court record (per lead):** The PTAB denied institution on the '557 patent and instituted review only on the '812 patent.
- **Interpretation:** This was a partial setback for Talonfield's invalidity defense. The '557 patent goes forward with no PTAB review, and in district court Talonfield must prove invalidity by clear and convincing evidence. The 10-K said "without merit" after this setback and did not mention it. A final written decision on the '812 patent would normally come about 12 months after institution, around May 2026. Its outcome is not in the filings or in the facts I was given. The facts I was given do not cover the third asserted patent.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Item 3. Legal Proceedings"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Part II, Item 1. Legal Proceedings"
- **Severity:** Medium
- **Confidence:** High that the excerpts leave it out. The PTAB facts come through the lead.
- **Deal impact:** Disclosure. Also bears on how strong Talonfield's defense is.
- **Cross-check:** Litigation analyst: the '812 final written decision and its date; any IPR on the third patent; which claims are still asserted.

#### SEC-22: No filing covers the events after the 10-Q, and the filings describe the exposure as Gen-3 only
- **Finding:** No filing in the set is dated after August 6, 2026. So none of these appear in any filing, as expected from the timing: the August 14 Gen-3 Plus amendment, the September 4 $96.4M expert figure and injunction statement, and the September 25 denial of a stay. "Gen-3 Plus" appears in no filing.
- **Evidence:** 10-K: Talon Gen-3 "represented approximately 70% of hardware revenue in 2025." No filing contains "Gen-3 Plus", "successor" or "design-around".
- **Math:** Gen-3 revenue is about 0.70 x $301.4M = $211.0M, or 42.0% of 2025 total revenue of $502.3M, before counting Gen-3 Plus. $96.4M / 48.3M diluted shares = $2.00 per share. That is 8.3% of the $1,159.2M implied equity value (24.00 x 48.3), and 2.8x the $33.9M of cash at June 30, 2026.
- **Interpretation:** Two positions now predate a quantified claim and an injunction request: the 10-K's "cannot reasonably estimate" and the 10-Q's "no accrual". The Q3 10-Q must reassess both. The Q2 10-Q was filed 37 days after quarter end. At the same lag, the Q3 10-Q would be filed around November 6, 2026, the IC date. The $96.4M is the opposing side's expert number, not an estimate of probable loss. An injunction against Gen-3 and Gen-3 Plus is likely the bigger value risk. The March 2027 trial is likely to fall near or after closing.
- **Source:** `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 1. Business" and "Item 7. Management's Discussion and Analysis (selected)"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, section "Liquidity and capital resources"; `data/deal-brief.md`, section "The deal"
- **Severity:** High. The lead may rate the combined damages and injunction exposure Critical.
- **Confidence:** High for the filing figures and the math, though the filing says "approximately 70%". The post-10-Q events come through the lead.
- **Deal impact:** Valuation and closing risk. Talonfield is a listed company, so an indemnity from its public shareholders after closing is rarely available. Protection would have to come from price, a specific closing condition, or a contingent value right (CVR) tied to the litigation.
- **Cross-check:** Financial analyst: 2026 revenue and backlog by product (Gen-3, Gen-3 Plus); not found in SEC filings. Litigation analyst: when Vantor will file its injunction motion.

#### SEC-23: No Item 1.05 8-K, and no 8-K of any kind, about the April 2026 incident in the filing set
- **Finding:** The set has only two 8-Ks: November 14, 2025 (Item 4.01, auditor change) and January 21, 2026 (Item 5.02, CFO departure). The first filing in the set that mentions the April 11 incident is the 10-Q, filed 117 days after the incident was detected.
- **Evidence:** No filing contains "1.05" or "material cybersecurity". 10-Q: "Based on our investigation, we concluded that the incident was not material".
- **Interpretation:** An Item 1.05 8-K is due within four business days after a company determines that an incident is material. If the "not material" conclusion is sound, no Item 1.05 8-K was required. That fits the news report (per lead) that none had been filed by April 14. The 10-Q does not say when the determination was made or who made it. The 10-Q's own facts make "not material" a harder call:
  - fleet operations were interrupted for some customers for up to three days;
  - $2.3M of service level credits were issued, 2.0% of Q2 revenue (2.3 / 112.9);
  - $1.8M of response costs were incurred;
  - a customer sued for $12.0M.

  Separately, the set has no 8-K after January 21, 2026, including no Item 2.02 earnings releases. So it is probably a subset of what Talonfield filed with the SEC (EDGAR).
- **Source:** `data/sec-filings/TLFS_8-K_2025-11-14_auditor-change.md`, section "Item 4.01"; `data/sec-filings/TLFS_8-K_2026-01-21_cfo-departure.md`, section "Item 5.02"; `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "April 2026 service disruption" and "Part II, Item 1. Legal Proceedings"
- **Severity:** Medium
- **Confidence:** High for this filing set. Medium for EDGAR as a whole.
- **Deal impact:** Disclosure and regulatory risk if the materiality call is challenged.
- **Cross-check:** The full EDGAR 8-K list since April 11, 2026 (Items 1.05, 7.01 and 8.01). The board or disclosure committee record of the materiality decision.

#### SEC-24: The 10-Q says nothing about the ransomware group's claim and still presents the cyber risk as hypothetical
- **Finding:** The 10-Q does not mention ransomware, a ransom demand, or the group's claim that it took data. It calls the event a "service disruption" caused by "unauthorized activity", and its only statement on data is about "customer data". It keeps the 10-K risk factor unchanged, which still says an attack "could" stop fleets and bring credits and claims. Yet the 10-Q itself reports a fleet stoppage, credits and a customer claim in Q2.
- **Evidence:** 10-Q: "As a precaution we took the affected systems offline, which interrupted fleet operations for some customers for up to three days." 10-Q: "...we have not identified evidence that customer data was taken." 10-K: "An outage or attack could stop customers' robot fleets, expose us to service level credits and claims, and damage our reputation." No filing contains "ransomware", "extort", "exfiltrat", "threat actor", "fleet configuration" or "site data".
- **News (per lead; an allegation):** On April 14 a ransomware group claimed it took "fleet configuration and customer site data". The claim has not been verified.
- **Interpretation:** "Have not identified evidence" hedges; it is not a denial. It covers only "customer data", so it does not address fleet configuration data, which may be Talonfield's own. Notifying law enforcement suggests a criminal intrusion, but the filing's wording ("service disruption", "as a precaution") is softer than the public claim. The risk factor still describes as possible a risk that had already happened.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "April 2026 service disruption", "Part II, Item 1. Legal Proceedings" and "Part II, Item 1A. Risk Factors"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, section "Item 1A. Risk Factors (selected)"
- **Severity:** High
- **Confidence:** High for what the 10-Q says and leaves out. Low for the group's claim itself.
- **Deal impact:** Post-closing and disclosure. The exposure from lost data could go beyond the $12.0M Pinecrest claim: more customer claims, breach notification duties, and FieldOS customers leaving. Review the forensic report before signing and get a specific cybersecurity representation.
- **Cross-check:** News analyst: whether the data was posted on a leak site, or customers confirmed exposure. Litigation analyst: other lawsuits about the incident. Management: the forensic report, any ransom demand or payment, notifications sent, insurance.

#### SEC-25: The 10-Q does not mention Norvale's move to its own robots and does not update the concentration risk factor
- **Finding:** The 10-Q never names Norvale. It mentions "our largest customer" only in the revenue paragraph and in the $9.4M bill-and-hold reversal. It says nothing about Kinetic Aisle or Norvale's 2027 pilots. Because the only risk factor change is the securities litigation addition, the 10-K's Norvale risk factor stands unchanged.
- **Evidence:** "Norvale" appears 3 times in the set, all in the 10-K, and 0 times in the 10-Q. The 10-Q does not contain "Kinetic", "in-house", "pilot", "single vendor", "concentration", "depend" or "terminat". The 10-K risk factor still in force says "the loss of Norvale would materially harm our business". Norvale can terminate "on 90 days' notice if Talonfield undergoes a change of control", and "Norvale is not required to purchase any minimum volume." The master supply agreement (MSA) "runs through September 30, 2027."
- **News (per lead):** On June 24, 2026, Norvale bought Kinetic Aisle to "reduce our dependence on any single vendor". It plans pilots at 5 distribution centers in 2027.
- **Interpretation:** The Kinetic Aisle purchase came inside the quarter, 6 days before June 30 and 43 days before the 10-Q was filed. The 10-Q already shows strain with the largest customer. Under the May 2026 amendment, $9.4M of products came back. That is 38.2% of the $24.6M of Q4 2025 bill-and-hold revenue that the 10-K ties to that customer (9.4 / 24.6). The 10-K names the largest customer as Norvale; the 10-Q does not name it. Norvale's 2027 pilots overlap the last nine months of the MSA, and this deal itself triggers Norvale's right to terminate. Norvale was about $156.2M of 2025 revenue (0.311 x 502.3). Whether leaving this out broke disclosure rules is a question for counsel. For the deal, the risk factor as filed understates the risk.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, sections "Revenue", "Bill-and-hold amendment" and "Part II, Item 1A. Risk Factors"; `data/sec-filings/TLFS_10-K_FY2025_excerpts.md`, sections "Item 1. Business", "Item 1A. Risk Factors (selected)" and "Note 2. Revenue Recognition (excerpt)"
- **Severity:** High. The lead may rate the underlying Norvale risk Critical.
- **Confidence:** High that the excerpt leaves it out. Medium that the 10-Q's "largest customer" is Norvale, because that link relies on the 10-K.
- **Deal impact:** Valuation and closing risk. The March 2026 management case in the deal model was prepared before the Kinetic Aisle purchase. Options: diligence on Norvale before signing, a Norvale waiver or MSA extension as a condition, or a price adjustment.
- **Cross-check:** News analyst: whether Norvale named Talonfield as the vendor. Financial analyst: Norvale's share of Q2 and H1 2026 revenue and its order trend (not found in SEC filings).

#### SEC-26: Pattern: the 10-Q says "no material changes" to risk factors, and disclosure controls were not effective
- **Finding:** The 10-Q added only a securities litigation risk factor. Four developments bore on existing risk factors:
  - the cyber incident (reported in the 10-Q itself);
  - the reversal with the largest customer (reported in the 10-Q itself);
  - Norvale's move to its own robots (news);
  - the claim construction order (court record).

  The same 10-Q concludes that disclosure controls were not effective.
- **Evidence:** 10-Q Item 4: the CEO and Interim CFO "concluded that our disclosure controls and procedures were not effective as of June 30, 2026." The certifications are signed by Marcus Hale and Rachel Simmons.
- **Interpretation:** The ineffective controls stem from the material weakness over hardware contracts. Even so, the officers who certified this 10-Q admit their disclosure process is not reliable. They will also be the source of the deal representations. Taken with SEC-20, SEC-24 and SEC-25, this means Talonfield's filed risk disclosures should not be treated as complete.
- **Source:** `data/sec-filings/TLFS_10-Q_Q2-2026_excerpts.md`, header and sections "Part I, Item 4. Controls and Procedures" and "Part II, Item 1A. Risk Factors"
- **Severity:** Medium
- **Confidence:** Medium. It is inferred from several data points.
- **Deal impact:** Governance and disclosure (IC question 5). Ask for broad disclosure representations with a bring-down condition, and verify each key item independently.
- **Cross-check:** Disclosure committee minutes for the Q2 10-Q, and whether the committee considered the order, the Norvale news and the ransomware claim before filing.

### Positive or mitigating points
- The 10-Q does describe the incident with specifics: the date, outages of up to three days, notice to law enforcement, $1.8M of costs and $2.3M of credits. It also discloses the Pinecrest suit.
- The 10-K risk factors already warned that Talonfield might have to stop selling Gen-3, and that losing Norvale would hurt the business, including the change-of-control termination right. The types of risk were disclosed. The updates were not.
- The 10-Q added a trial date that the 10-K did not have.
- The lack of an Item 1.05 8-K fits management's stated conclusion that the incident was not material.
- The August and September litigation events came after every filing, so their absence from the filings is not an omission.
- The excerpt leaves out the 10-Q notes, which may close some of these gaps.

### Gaps and questions for management
1. Provide the full Q2 10-Q with its contingencies and subsequent events notes. Do they mention the July 22 order, the PTAB outcome, or a range of reasonably possible loss?
2. When did management and the disclosure committee consider the July 22 order? Why is it not in Part II, Item 1?
3. What is the current ASC 450 assessment of Vantor after September 4? Share the draft Q3 10-Q legal proceedings and contingencies text before the IC meeting.
4. What was the outcome of the '812 IPR, and what is the status of the third patent?
5. Gen-3 Plus: launch date, share of 2026 revenue and backlog, and whether it was designed to get around the patents.
6. Cyber: when the materiality decision was made and who made it; the forensic report; any ransom demand or payment; whether any customer or fleet configuration data left the network; notifications; insurance. Also provide 10-K Item 1C (Cybersecurity), which is not in the excerpt.
7. Norvale: when Talonfield learned of the Kinetic Aisle purchase; Norvale's share of H1 2026 revenue; talks on renewing the MSA; Norvale's stance on its change-of-control termination right; who asked for the May 2026 amendment.
8. A full list of SEC filings since January 21, 2026. The set has no 8-K after that date.
9. Deal brief: it is dated October 12, 2026 but cites the October 16, 2026 closing price. Confirm which version is current.
