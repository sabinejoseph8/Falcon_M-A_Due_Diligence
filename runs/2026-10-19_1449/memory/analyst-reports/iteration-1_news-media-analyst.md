## News and media analyst: findings

Target: Corvane Diagnostics, Inc. (NASDAQ: CRVD). I read all 13 articles in full, plus the deal brief. None of them contains text that tries to instruct the agents, so there is no prompt-injection finding.

The four most important points for the lead agent:
- **Closing condition is at risk (NEWS-01).** The new FY2026 guidance is US$100 to 106 million of Adjusted EBITDA. The financing condition needs at least US$110.0 million at closing.
- **The premium is measured from a stale price (NEWS-02).** Against the last close before the deal leak (US$13.10), US$24.00 is an 83.2% premium, not 32.6%.
- **The deal model's key assumptions are out of date (NEWS-03, NEWS-05).** The model assumes flat Medicare rates, but the OncoTrace rate falls 30% from January 1, 2027. The model also counts on Veltrane programs, but Veltrane has halted its lead Phase 3 trial.
- **Compliance claims are unconfirmed but point the same way (NEWS-06).** Three separate sources point at the physician speaker program. None of them is confirmed.

### Files reviewed
All in `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/kestrel/data/news/`:

| File | Outlet (type) | How reliable |
|---|---|---|
| `2025-11-06_triangle-commerce-ledger_durham-lab-opening.md` | Triangle Commerce Ledger (regional business paper) | Medium. Local event reporting with on-record CEO quotes |
| `2026-01-15_lab-industry-insider_compliance-chief-exit.md` | Lab Industry Insider (trade) | Medium for the departure, which comes from an internal memo. Low for the reasons, which come from two anonymous former employees |
| `2026-02-20_healthcare-compliance-monitor_doj-genetic-testing-probe.md` | Healthcare Compliance Monitor (newsletter, staff report) | Low. Anonymous sources, and the article itself says the report "has not been confirmed" |
| `2026-03-06_capital-street-wire_record-2025-results.md` | Capital Street Wire (financial newswire) | High. Reported results and on-record quotes from the earnings call |
| `2026-04-22_lab-industry-insider_ransomware-attack.md` | Lab Industry Insider (trade) | Medium for the operational disruption, based on physicians' offices. Low for the data theft, which is an unverified attacker claim |
| `2026-05-19_capital-street-wire_bearhaven-short-report.md` | Capital Street Wire | High that the report was published and for the price move. Low for the claims, which come from an interested short seller |
| `2026-06-14_triangle-commerce-ledger_charity-5k.md` | Triangle Commerce Ledger | Not relevant (noise) |
| `2026-07-30_healthcare-policy-daily_cms-lab-fee-schedule.md` | Healthcare Policy Daily (trade) | High. Reports a published CMS final rate that can be checked against the CMS schedule |
| `2026-08-06_capital-street-wire_guidance-cut.md` | Capital Street Wire | High. Company guidance and call quotes |
| `2026-08-27_pharma-pipeline-news_veltrane-halts-atlas-3.md` | Pharma Pipeline News (trade) | High for Veltrane's own announcement. The article does not name Corvane |
| `2026-09-03_fda-enforcement-roundup_corvane-laboratories-pty.md` | FDA Enforcement Roundup (newsletter) | High, but it covers a different, unaffiliated company |
| `2026-09-17_supply-chain-health_sequencing-reagent-tariffs.md` | Supply Chain Health (trade) | High for the tariff. Medium for Corvane's self-reported exposure, which is a company statement nobody has checked |
| `2026-10-05_capital-street-wire_halvard-take-private-talks.md` | Capital Street Wire | Rumor for the deal talks (people familiar with the matter). Fact for the share prices |

### Timeline

| Date | Event | Outlet | Fact / Allegation / Rumor |
|---|---|---|---|
| Around Oct 2025 ("a year ago" per Oct 5, 2026 article) | Shares at US$27.80 | Capital Street Wire | Fact |
| Nov 6, 2025 | Seventh lab opens in Durham. 120 jobs by end of 2026. US$0.6M county tax grant. Start-up costs to be reported outside Adjusted EBITDA | Triangle Commerce Ledger | Fact (company statement) |
| 2025 (date not given) | CCO Daniel Pruitt allegedly raised internal concerns about the physician speaker program | Lab Industry Insider | Rumor (two anonymous former employees) |
| By Jan 15, 2026 | CCO Pruitt leaves "to pursue other opportunities". Deputy GC becomes interim compliance chief. No 8-K was required | Lab Industry Insider | Fact (internal memo) |
| Second week of Feb 2026 | Corvane allegedly received a DOJ civil investigative demand covering billing since 2019 and speaker events | Healthcare Compliance Monitor | Rumor |
| Mar 6, 2026 | FY2025 results: revenue US$431.0M (+11.7%), Q4 revenue US$120.5M, Adj. EBITDA US$125.3M (+25.4%). FY2026 revenue guidance US$455-465M. CFO cites "refinement of our collection estimates". Shares +6.4% to US$22.30 | Capital Street Wire | Fact |
| Apr 18, 2026 | Labs unable to process most samples. Physicians' offices describe a ransomware attack and are told to send samples elsewhere | Lab Industry Insider | Fact (several practices). The cause is as described by physicians |
| Apr 21, 2026 | Ransomware group claims 1.1 TB of files, including patient test results, and sets a payment deadline | Lab Industry Insider | Allegation (attacker claim, not verified) |
| May 19, 2026 (Tue) | Bearhaven short report alleges kickbacks, test stacking, a "manufactured" Q4 and fast receivables growth. Corvane: "false and misleading". Shares -11.2% to US$17.85 | Capital Street Wire | Allegation |
| Jun 13, 2026 | Corvane Hope 5K | Triangle Commerce Ledger | Fact (noise) |
| Jun 30, 2026 | Deal model built (per the brief) | Deal brief | Context |
| Jul 29, 2026 (Wed) | CMS final 2027 lab fee schedule: code 0419U (OncoTrace) cut from US$2,150 to US$1,505 (-30%), effective Jan 1, 2027 | Healthcare Policy Daily (Jul 30) | Fact |
| Jul 31, 2026 | Close of US$18.10, the brief's premium reference | Deal brief / Capital Street Wire | Fact |
| Aug 4, 2026 (Tue) | Close of US$18.10 | Capital Street Wire | Fact |
| Aug 5, 2026 (Wed) | FY2026 Adj. EBITDA guidance cut to US$100-106M (from US$134-140M). Revenue guidance cut to US$405-415M (from US$455-465M). Q2 revenue -3.0% to US$100.8M. CFO declines to give a leverage figure for the end-September covenant test. Shares -31.2% to US$12.45 | Capital Street Wire (Aug 6) | Fact |
| Aug 27, 2026 | Veltrane halts its Phase 3 ATLAS-3 trial (VLT-220) for futility. Sites close by Q1 2027. 40% of staff cut. "Wind down vendor contracts" | Pharma Pipeline News | Fact (Veltrane statement). The link to Corvane is not stated |
| Sep 3, 2026 | FDA warning letter to Corvane Laboratories Pty Ltd (Australia), an unaffiliated company | FDA Enforcement Roundup | Fact (different entity) |
| Sep 30, 2026 | "Tighter leverage test" in the credit agreement (per analysts' question on the Aug call) | Capital Street Wire (Aug 6) | Fact that the test exists. Result not found in news coverage |
| Oct 1, 2026 | 25% tariff on imported sequencing reagents takes effect. Corvane says its Helixor contract fixes prices, including duties, through 2028 | Supply Chain Health (Sep 17) | Fact (tariff). Company statement (exposure) |
| Oct 2, 2026 (Fri) | Close of US$13.10, before the leak | Capital Street Wire | Fact |
| Oct 5, 2026 (Mon) | Report of exclusive Halvard talks at about US$24/share. Special committee formed. Shares +9.2% to US$14.30 in early trading | Capital Street Wire | Rumor (talks). Fact (prices) |

### Findings

#### NEWS-01: FY2026 EBITDA guidance cut to below the US$110.0M financing condition
- **Finding:** Corvane cut its FY2026 Adjusted EBITDA guidance by US$34.0M at the midpoint, from US$137.0M to US$103.0M (-24.8%). It cut revenue guidance from a US$460.0M midpoint to US$410.0M (-10.9%). Even the top of the new range (US$106.0M) is below the term loan B condition of at least US$110.0M of LTM Adjusted EBITDA at closing. That condition is in the deal brief.
- **Evidence:** "cut its FY2026 Adjusted EBITDA outlook to US$100 to 106 million from US$134 to 140 million"
- **Source:** `targets/kestrel/data/news/2026-08-06_capital-street-wire_guidance-cut.md` (Capital Street Wire, Aug 6, 2026), paragraph 1
- **Claim type:** Fact (company guidance)
- **Severity:** Critical. Tests met:
  - **Block closing:** the guided FY2026 range of US$100-106M is below the US$110.0M LTM condition in the commitment letter.
  - **More than 10% of value:** the model's FY2026 EBITDA of US$137.0M falls 24.8%. At the deal EV of US$1,648.6M, the multiple rises from 12.0x to 16.0x guided FY2026 EBITDA. The term loan of US$750.0M is 7.3x guided EBITDA, against 6.0x as sized.
  - (inference) LTM at a Q2 2027 closing would include Q1 2027, when the CMS rate cut is in effect (NEWS-03).
- **Confidence:** High. The guidance is an on-record company statement reported by a financial newswire. The calculations are mine.
- **Deal impact:** valuation, closing risk (financing condition), debt sizing.
- **Cross-check:** Q2 2026 10-Q or 8-K earnings release for the guidance; quarterly financials for actual LTM Adjusted EBITDA; the commitment letter's definition of Adjusted EBITDA (as Corvane defines it, including add-backs).

#### NEWS-02: The 32.6% premium is measured from a stale price
- **Finding:** The brief measures the premium against the July 31, 2026 close of US$18.10, which was before the August 5 guidance cut. The last close before the deal leak was US$13.10 (October 2). Against that price, US$24.00 is an 83.2% premium. It is 92.8% over the US$12.45 close after the guidance cut. Implied market cap at US$13.10 is US$686.4M, against the US$1,257.6M deal equity value.
- **Evidence:** "Corvane shares closed at US$13.10 on Friday, October 2, before the report, and rose 9.2% to US$14.30"
- **Source:** `targets/kestrel/data/news/2026-10-05_capital-street-wire_halvard-take-private-talks.md` (Capital Street Wire, Oct 5, 2026); `2026-08-06_capital-street-wire_guidance-cut.md`
- **Claim type:** Fact for the prices. Rumor for the talks ("according to people familiar with the matter").
- **Severity:** High
- **Confidence:** High for the prices. Low for the deal-talk details, including the special committee, which come from one anonymous person.
- **Deal impact:** valuation (the offer price may be anchored too high), reputation (the leak).
- **Cross-check:** market price data; Corvane 8-K or proxy on the special committee; whether Corvane made any formal disclosure after the leak.

#### NEWS-03: CMS cuts the OncoTrace Medicare rate by 30% from Jan 1, 2027
- **Finding:** The final 2027 CLFS rate for PLA code 0419U (OncoTrace) falls from US$2,150 to US$1,505, a cut of US$645 per test (-30.0%), effective January 1, 2027. Commercial contracts priced off Medicare will also reprice. The deal model assumes flat Medicare rates through 2030, and the model date (June 30) is before this rule. Management did not quantify the impact.
- **Evidence:** "the rate for PLA code 0419U ... falls from US$2,150 to US$1,505, a cut of 30%. The new rate takes effect on January 1, 2027." Also: "Management did not quantify the effect of the new Medicare rate for OncoTrace."
- **Source:** `targets/kestrel/data/news/2026-07-30_healthcare-policy-daily_cms-lab-fee-schedule.md` (Healthcare Policy Daily, Jul 30, 2026); `2026-08-06_capital-street-wire_guidance-cut.md`, paragraph 3
- **Claim type:** Fact
- **Severity:** High. Rate it Critical if the financial data shows OncoTrace Medicare plus Medicare-linked commercial revenue large enough that a 30% cut takes away more than 10% of value. OncoTrace volumes and payer mix were not found in news coverage.
- **Confidence:** High. This is a published federal rate. CMS says reconsideration is possible "only in limited circumstances".
- **Deal impact:** valuation (the 2027+ revenue base), and the LTM EBITDA condition for a Q2 2027 closing.
- **Cross-check:** revenue by test, payer and code in the financials; 10-K reimbursement and risk factor disclosures; any reconsideration request filed by Corvane.

#### NEWS-04: Possible covenant breach at the September 30, 2026 leverage test
- **Finding:** Analysts asked whether Corvane would pass the "tighter leverage test" at the end of September. The CFO declined to give a leverage figure. A breach would happen before signing (planned for mid-December 2026).
- **Evidence:** CFO said Corvane "has a constructive relationship with its lenders" and declined to give a leverage figure.
- **Source:** `targets/kestrel/data/news/2026-08-06_capital-street-wire_guidance-cut.md` (Capital Street Wire, Aug 6, 2026), paragraph 3
- **Claim type:** Fact (the question and the non-answer). The breach risk is my inference.
- **Severity:** High. Under the shared calibration rule, a default before signing would make this Critical. The result was not found in news coverage.
- **Confidence:** Medium. On-record evasion, but no covenant figures.
- **Deal impact:** closing risk, balance sheet stability between now and closing.
- **Cross-check:** covenant step-down schedule and definitions in the 10-K or credit agreement; Q3 2026 10-Q or 8-K for any waiver, amendment or default notice; financials for net debt and LTM Adjusted EBITDA at September 30.

#### NEWS-05: Veltrane halts ATLAS-3, a threat to the backlog assumption
- **Finding:** Veltrane stopped its Phase 3 ATLAS-3 trial of its lead program for futility. It will close sites by Q1 2027, cut 40% of staff, and wind down vendor contracts. The brief assumes the US$246.0M backlog converts on schedule, including the Veltrane programs. The article does not name Corvane as a vendor.
- **Evidence:** "It did not name its trial vendors, but said it would 'wind down vendor contracts in an orderly way.'"
- **Source:** `targets/kestrel/data/news/2026-08-27_pharma-pipeline-news_veltrane-halts-atlas-3.md` (Pharma Pipeline News, Aug 27, 2026)
- **Claim type:** Fact (Veltrane's announcement). The effect on Corvane is my inference.
- **Severity:** High
- **Confidence:** High for the halt. Medium for the Corvane exposure, which rests on the brief's statement that Veltrane programs are in the backlog. The amount was not found in news coverage.
- **Deal impact:** valuation (backlog and biopharma revenue), and a stale model assumption.
- **Cross-check:** Veltrane's share of backlog and revenue in the 10-K and `revenue_by_customer.csv`; contract termination or cancellation-fee terms; Q3 2026 backlog disclosure.

#### NEWS-06: Compliance cluster: CCO exit, DOJ civil investigative demand (rumor), Bearhaven kickback claims (allegation)
- **Finding:** Three separate unconfirmed sources point at the physician speaker program:
  - the CCO left in January 2026 after allegedly raising concerns about it in 2025;
  - Corvane allegedly received a DOJ civil investigative demand in February 2026 covering billing since 2019 and speaker events;
  - Bearhaven alleges speaker fees averaging US$40,000 a year to high-ordering oncologists, plus "test stacking".

  Corvane denies the Bearhaven claims, did not comment on the DOJ report, and declined to discuss the CCO exit.
- **Evidence:**
  - "Corvane Diagnostics received a demand 'in the second week of February' covering billing since 2019 and the company's physician speaker events."
  - Bearhaven: "speaker fees" averaging US$40,000 a year to dozens of high-ordering oncologists.
  - Corvane: "false and misleading"; "complies with all applicable laws"; "remains robust."
- **Source:** `2026-01-15_lab-industry-insider_compliance-chief-exit.md` (Jan 15, 2026); `2026-02-20_healthcare-compliance-monitor_doj-genetic-testing-probe.md` (Feb 20, 2026); `2026-05-19_capital-street-wire_bearhaven-short-report.md` (May 19, 2026), allegations 1 and 2
- **Claim type:**
  - CCO departure: Fact.
  - CCO's concerns: Rumor.
  - DOJ civil investigative demand: Rumor.
  - Bearhaven claims: Allegation by an interested party with a disclosed short position.
- **Severity:** High. If confirmed, False Claims Act and Anti-Kickback Statute exposure, with damages on Medicare billing since 2019, would need a special indemnity or escrow. I cannot show a >10% number from news alone, so this is not Critical.
- **Confidence:** Low. No source is confirmed. The three sources do point the same way.
- **Deal impact:** valuation, post-closing liability, reputation, and possible exclusion risk.
- **Cross-check:**
  - Whether the 10-K or 10-Q discloses a civil investigative demand or DOJ inquiry. If the demand was received in February 2026 and the March 2026 10-K is silent, that is a disclosure gap.
  - Any qui tam or unsealed complaint in the litigation dockets.
  - Speaker fee spend in the financials.
  - The 8-K record on officer changes.

#### NEWS-07: Q4 2025 revenue boosted by an unquantified change in collection estimates
- **Finding:** Q4 2025 revenue was a record US$120.5M, against an FY2025 quarterly average of US$107.8M. The CFO credited "a refinement of our collection estimates" but gave no amount. Bearhaven later alleged Q4 was "manufactured" by that change while payer denials rose and receivables grew faster than revenue.
- **Evidence:** "strong volumes and a refinement of our collection estimates." She did not give an amount on the call.
- **Source:** `2026-03-06_capital-street-wire_record-2025-results.md` (Mar 6, 2026); `2026-05-19_capital-street-wire_bearhaven-short-report.md`, allegations 3 and 4
- **Claim type:** Fact (CFO statement). Allegation (Bearhaven's "manufactured" claim).
- **Severity:** High. It feeds directly into the US$125.3M FY2025 EBITDA base used for the 6.0x term loan.
- **Confidence:** Medium. The CFO confirmed the change on record, but there is no amount.
- **Deal impact:** valuation, quality of earnings, debt sizing.
- **Cross-check:**
  - 10-K notes on revenue recognition and implicit price concession, and any change in estimate.
  - Quarterly revenue, DSO, AR aging and denial rates in the financials.
  - Whether FY2025 growth of 11.7% (prior-year revenue about US$385.9M) holds without the change.

#### NEWS-08: Ransomware attack: sample processing halted from April 18 and patient data claimed
- **Finding:** From April 18, 2026, labs could not process most samples, and oncology practices were told to send samples elsewhere. On April 21 a ransomware group claimed 1.1 TB of files, including patient test results. Corvane only said it was restoring systems and did not address the data claim.
- **Evidence:**
  - "unable to process most samples since April 18"
  - claiming to have taken "1.1 terabytes" of Corvane files, including patient test results
  - Corvane: "working around the clock to restore systems"
- **Source:** `targets/kestrel/data/news/2026-04-22_lab-industry-insider_ransomware-attack.md` (Lab Industry Insider, Apr 22, 2026)
- **Claim type:** Fact (the disruption, reported by several practices). Allegation (data theft, an attacker claim the outlet could not verify).
- **Severity:** High. Possible HIPAA breach liability, lost volume (samples redirected to competitors) and billing backlog. Q2 2026 revenue fell 3.0% to US$100.8M. Linking that fall to the attack is my inference.
- **Confidence:** Medium for the disruption. Low for the data theft.
- **Deal impact:** valuation (Q2 and LTM EBITDA), post-closing liability, reputation.
- **Not found in news coverage:** how long the outage lasted, whether a ransom was paid, billing or claims-submission effects, HHS breach notification, and insurance recovery.
- **Cross-check:**
  - Whether there is an 8-K Item 1.05 cybersecurity filing and when it was made.
  - How the 10-Q describes the incident's impact.
  - Q2 volumes and revenue in the financials.
  - Any class action over the data breach in the litigation dockets.

#### NEWS-09: Durham lab start-up costs are excluded from Adjusted EBITDA
- **Finding:** Corvane said start-up costs for the seventh lab would be reported outside Adjusted EBITDA, as it has done for earlier openings. This recurring add-back bears on whether the US$125.3M base is "recurring".
- **Evidence:** "start-up costs for the new site will be reported outside its Adjusted EBITDA, as it has done for earlier lab openings."
- **Source:** `targets/kestrel/data/news/2025-11-06_triangle-commerce-ledger_durham-lab-opening.md` (Triangle Commerce Ledger, Nov 6, 2025)
- **Claim type:** Fact (company statement)
- **Severity:** Medium
- **Confidence:** Medium. A single regional outlet reporting a company statement. The amount was not found in news coverage.
- **Deal impact:** valuation, and the Adjusted EBITDA definition behind the US$110.0M condition.
- **Cross-check:** the EBITDA bridge in the financials and the non-GAAP reconciliation in the 10-K, for the start-up cost add-back amount and how often it recurs.

#### NEWS-10: Share price falls about 53% in a year; the test dates behind earlier accounting judgments need review
- **Finding:** Shares fell from US$27.80 about a year ago to US$13.10 on October 2, 2026 (-52.9%). Step moves:
  - +6.4% to US$22.30 on FY2025 results (Mar 6);
  - -11.2% to US$17.85 on the Bearhaven report (May 19);
  - -31.2% to US$12.45 on the guidance cut (Aug 5).

  Implied market cap at US$13.10 is US$686.4M on 52.4M diluted shares.
- **Evidence:** "Shares fell 31.2% to US$12.45 on Wednesday, from US$18.10 at Tuesday's close"
- **Source:** `2026-03-06_capital-street-wire_record-2025-results.md`; `2026-05-19_capital-street-wire_bearhaven-short-report.md`; `2026-08-06_capital-street-wire_guidance-cut.md`; `2026-10-05_capital-street-wire_halvard-take-private-talks.md`
- **Claim type:** Fact
- **Severity:** Medium
- **Confidence:** High. Prices are reported by a financial newswire.
- **Deal impact:** valuation. (inference) The share price fall may put in doubt any goodwill impairment test or other judgment dated at or before year-end 2025.
- **Cross-check:** goodwill balance and impairment test date in the 10-K; market price data.

#### NEWS-11: Reagent tariff exposure is hedged through 2028, per the company only
- **Finding:** A 25% tariff on imported sequencing reagents took effect on October 1, 2026. Reagents are an estimated 15-25% of test cost. Corvane says its Helixor Instruments contract fixes prices, including duties, through 2028, and expects "no meaningful impact". Exposure after 2028, and Helixor's willingness to absorb the duties, are not addressed.
- **Evidence:** fixes prices, including duties, through 2028, and that it expects "no meaningful impact" from the tariff during the contract term.
- **Source:** `targets/kestrel/data/news/2026-09-17_supply-chain-health_sequencing-reagent-tariffs.md` (Supply Chain Health, Sep 17, 2026)
- **Claim type:** Fact (the tariff). Company statement (the hedge, not independently checked).
- **Severity:** Medium
- **Confidence:** Medium. A company statement in a single trade article.
- **Deal impact:** post-closing margin risk from 2029, and supplier concentration.
- **Cross-check:** Helixor contract terms (duty pass-through, term, termination) in the 10-K or material contracts; supplier concentration disclosure; reagent cost share in the financials.

### Positive or mitigating points
- **Reagent tariff:** fixed-price Helixor contract covering duties through 2028, per the company (NEWS-11).
- **Bearhaven:** Corvane publicly denied the report. Bearhaven discloses that it profits from a price fall, and its sources are eight unnamed former employees (NEWS-06).
- **CCO departure:** no 8-K was required for the CCO departure, so there is no disclosure breach from that alone (NEWS-06).
- **Durham lab:** capacity expansion with a US$0.6M tax grant over five years. The CEO says it supports five years of OncoTrace volume growth (NEWS-09).
- **Special committee:** a committee of independent directors was reportedly formed, which supports deal process governance. This is a rumor (NEWS-02).

### Articles reviewed with no diligence relevance
- `2026-06-14_triangle-commerce-ledger_charity-5k.md`: community charity race. The company matched up to US$100,000. No diligence relevance.
- `2026-09-03_fda-enforcement-roundup_corvane-laboratories-pty.md`: FDA warning letter and import alert for **Corvane Laboratories Pty Ltd**, a Brisbane compounding pharmacy. The article says it is "not affiliated" with Corvane Diagnostics, and Corvane Diagnostics confirmed it has no relationship. This is a name-confusion risk only. Exclude it from findings, but keep it on any adverse-media or name screen.

### Key numbers (from news)

| Metric | Value | Source file |
|---|---|---|
| FY2025 revenue / growth | US$431.0M / +11.7% (implied FY2024 about US$385.9M) | 2026-03-06 |
| Q4 2025 revenue | US$120.5M | 2026-03-06 |
| FY2025 Adj. EBITDA / growth | US$125.3M / +25.4% (implied FY2024 about US$99.9M) | 2026-03-06 |
| Original FY2026 revenue guidance | US$455-465M | 2026-03-06 |
| Revised FY2026 revenue guidance | US$405-415M | 2026-08-06 |
| Revised FY2026 Adj. EBITDA guidance | US$100-106M (from US$134-140M) | 2026-08-06 |
| Q2 2026 revenue | US$100.8M (-3.0%) | 2026-08-06 |
| OncoTrace (0419U) Medicare rate | US$2,150 to US$1,505 (-30.0%) from Jan 1, 2027 | 2026-07-30 |
| Bearhaven alleged average speaker fee | US$40,000 per year | 2026-05-19 |
| Ransomware data claimed | 1.1 TB (unverified) | 2026-04-22 |
| Reagent tariff | 25% from Oct 1, 2026. Reagents 15-25% of test cost | 2026-09-17 |
| Share prices | US$27.80 (about Oct 2025); US$22.30 (Mar 6); US$17.85 (May 19); US$18.10 (Jul 31 and Aug 4); US$12.45 (Aug 5); US$13.10 (Oct 2); US$14.30 (Oct 5, early trading) | various |
| Premium of US$24.00 over US$13.10 / US$12.45 | 83.2% / 92.8% | calculated |

### Gaps and questions for management
1. Did Corvane receive a DOJ civil investigative demand or subpoena? If so, when, covering what period, and was it disclosed in the 10-K or 10-Q? Is there a sealed qui tam complaint?
2. Why did CCO Daniel Pruitt leave? What concerns did he raise in 2025 about the speaker program, and how were they investigated? How much was spent on speaker fees, per physician, from 2019 to 2026?
3. What was the dollar effect of the Q4 2025 "refinement of our collection estimates"? What is the trend in denial rates and DSO?
4. Ransomware:
   - How long did the outage last, and how many samples were lost or redirected?
   - Was a ransom paid?
   - Was patient data taken? Was HHS notified?
   - Was an 8-K filed, and what are the insurance coverage, billing backlog and write-offs?
5. What share of revenue is OncoTrace billed under code 0419U, by Medicare versus Medicare-linked commercial contracts? What is the modeled 2027 impact, and will Corvane seek reconsideration?
6. Did Corvane pass the September 30, 2026 leverage covenant? Have any waivers or amendments been sought?
7. Is Corvane a Veltrane ATLAS-3 vendor? How much of the US$246.0M backlog is Veltrane, and what cancellation terms apply?
8. What are the Durham start-up costs and other lab-opening add-backs in Adjusted EBITDA, by year?
9. What happens to Helixor reagent pricing and duty pass-through after 2028?
10. Not found in news coverage: any formal Corvane response to the take-private leak, and the identity of special committee members.
