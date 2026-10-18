# Iteration 1: news-media-analyst report (unedited)

- Saved by the lead agent: 2026-10-18 02:31 EST
- Task: News and media analysis, iteration 1
- Subagent ID: a13f8f52911841a3e
- The report below is the subagent's final message exactly as returned. Only the harness's hand-back line and its two-space line indent were removed.

---

## News and media analyst: findings

### Files reviewed

I read all 13 articles in `data/news/` in full, plus `data/deal-brief.md` for context. There are no hidden files in the folder. Each article has a "FICTIONAL ARTICLE" banner, which fits the case study. No article tries to give instructions to the agents, so there is no prompt-injection finding.

1. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2025-11-18_capital-markets-wire_auditor-switch.md` (Capital Markets Wire, November 18, 2025)
2. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-01-23_columbus-business-ledger_cfo-exit.md` (Columbus Business Ledger, January 23, 2026)
3. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-02-10_warehouse-tech-review_fieldos-5-launch.md` (Warehouse Tech Review, February 10, 2026)
4. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-03-10_capital-markets-wire_record-q4.md` (Capital Markets Wire, March 10, 2026)
5. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-03-28_columbus-business-ledger_scholarship.md` (Columbus Business Ledger, March 28, 2026)
6. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-04-14_supply-chain-dispatch_fieldos-outage.md` (Supply Chain Dispatch, April 14, 2026)
7. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-05-12_capital-markets-wire_short-seller-report.md` (Capital Markets Wire, May 12, 2026)
8. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-06-24_roboeconomy-weekly_norvale-buys-kinetic-aisle.md` (RoboEconomy Weekly, June 24, 2026)
9. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-07-30_columbus-business-ledger_layoffs.md` (Columbus Business Ledger, July 30, 2026)
10. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-08-07_capital-markets-wire_guidance-cut.md` (Capital Markets Wire, August 7, 2026)
11. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-08-20_warehouse-tech-review_market-report.md` (Warehouse Tech Review, August 20, 2026)
12. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-09-15_supply-chain-dispatch_lidar-tariffs.md` (Supply Chain Dispatch, September 15, 2026)
13. `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/2026-10-02_capital-markets-wire_sale-exploration.md` (Capital Markets Wire, October 2, 2026)

Context only: `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/deal-brief.md`

Method notes:
- Some articles give only a weekday (for example "on Friday"). I turned these into calendar dates and marked them "inferred".
- Figures marked "calculated" are my own. They use the rounded percentages in the articles, so they are approximate.

### Timeline

| Date | Event | Outlet | Fact / Allegation / Rumor |
|---|---|---|---|
| Q3 2025 (date not stated) | Outgoing auditor Hartwell & Pryce flags a "material weakness" in controls over certain hardware contracts | Capital Markets Wire (Nov 18, 2025), citing the company's filing | Fact |
| Nov 14, 2025 (Friday, inferred) | Company filing: Hartwell & Pryce (auditor since 2016) is replaced by Linden Barr LLP. The filing reports no disagreements. It says the outgoing auditor had planned expanded work on Q4 deals with "unusual delivery terms" | Capital Markets Wire (Nov 18, 2025) | Fact |
| Nov 17, 2025 (Monday, inferred) | Shares close down 2.1% | Capital Markets Wire (Nov 18, 2025) | Fact |
| Nov 18, 2025 | Company calls the change "a routine review". An accounting professor calls the timing "unusual" | Capital Markets Wire | Fact (company statement); commentary |
| Q4 2025 ("late 2025") | At least one bill-and-hold sale booked. The company later reported it was returned | Capital Markets Wire (Aug 7, 2026) | Fact |
| Jan 21, 2026 (Wednesday, inferred) | Company filing: CFO Daniel Okafor leaves, "not the result of any disagreement". He receives a US$0.9 million separation payment. Controller Rachel Simmons becomes interim CFO | Columbus Business Ledger (Jan 23, 2026) | Fact |
| Jan 22, 2026 (Thursday, inferred) | Spokesperson repeats the no-disagreement statement and declines further comment | Columbus Business Ledger (Jan 23, 2026) | Fact |
| Jan 23, 2026 | Two unnamed people say the exit followed weeks of tension with CEO Marcus Hale over how to book large Q4 hardware orders | Columbus Business Ledger | Rumor |
| February 2026 | "Hundreds" of robots booked as Q4 sales allegedly still sit in the Columbus warehouse | Capital Markets Wire (May 12, 2026), citing Greyfin | Allegation |
| Feb 10, 2026 | FieldOS 5 launch. Three enterprise agreements, including a Harbor & Vine Grocers expansion to 12 more distribution centers. CEO targets software at "more than a third of revenue" within three years | Warehouse Tech Review | Fact (announcement); company claims unverified |
| Mar 10, 2026 | Q4 2025 revenue US$154.4 million (+32%) against about US$128.0 million expected. FY2025 revenue US$502.3 million (+19%). 2026 guidance: US$555.0-565.0 million revenue, US$114.0-122.0 million Adjusted EBITDA. New auditor's adverse opinion on internal controls disclosed. Shares +9% to US$31.20 | Capital Markets Wire | Fact |
| Mar 10, 2026 | Unnamed analyst says receivables "jumped" and FY2025 operating cash flow fell under US$10.0 million | Capital Markets Wire | Fact (results); analyst commentary |
| March 2026 (date not stated) | Investor day repeats the 2026 targets. 52-week high of US$31.75 | Capital Markets Wire (Mar 10 and May 12, 2026) | Fact |
| Mar 27, 2026 (Friday, inferred) | US$1.5 million scholarship program announced (no diligence relevance) | Columbus Business Ledger (Mar 28, 2026) | Fact |
| About Apr 11 to 14, 2026 (start date inferred) | Parts of FieldOS taken offline after "unauthorized activity". Robots at 40-plus customer sites stop for up to three days. Systems restored by April 14 | Supply Chain Dispatch (Apr 14, 2026) | Fact |
| Apr 12, 2026 (Sunday, inferred) | Ransomware group claims it took "fleet configuration and customer site data" | Supply Chain Dispatch (Apr 14, 2026) | Rumor (unverified) |
| Apr 14, 2026 | No Form 8-K Item 1.05 filed. Company says the incident is "not material". Pinecrest Distribution COO: "We are reviewing our options" | Supply Chain Dispatch | Fact; customer claim |
| Apr 1 to Jun 30, 2026 (date not stated) | A customer returns robots from a late-2025 bill-and-hold sale. US$9.4 million credit booked in Q2 2026 | Capital Markets Wire (Aug 7, 2026) | Fact |
| May 12, 2026 (Tuesday) | Greyfin Research publishes short report "Holding the Bag" (on or just before this date). Shares fall 18% to US$19.85. Company calls it "misleading and inaccurate" | Capital Markets Wire | Allegation (report); Fact (price move and response) |
| Jun 24, 2026 (on or before) | Norvale Retail Group, Talonfield's largest customer, buys Kinetic Aisle to build its own robots. Pilot at five distribution centers in 2027. Shares fall 6% | RoboEconomy Weekly | Fact |
| Jul 30, 2026 (notice date not stated) | State notice: about 60 job cuts (4% of staff), mostly in hardware assembly and field services. Fourth restructuring since 2022 | Columbus Business Ledger | Fact |
| Aug 7, 2026 | Q2 2026 revenue down 4% to US$112.9 million. This includes a US$9.4 million bill-and-hold return credit and US$2.3 million of outage credits. 2026 guidance cut to US$470.0-490.0 million revenue and US$70.0-78.0 million Adjusted EBITDA. Interim CFO calls 2026 a "reset year". Two downgrades. Shares fall 14% to US$16.40 | Capital Markets Wire | Fact |
| Aug 20, 2026 | Calder Insights forecasts North American warehouse AMR spending to grow about 15% a year to 2030. Talonfield ranks third with about 11% share. Large retailers are building robots in-house | Warehouse Tech Review | Fact (third-party forecast) |
| Sep 15, 2026 | Proposal to raise tariffs on Chinese LiDAR modules from 7.5% to 25%. Talonfield buys all its LiDAR from one Chinese supplier. One analyst sees a 2 to 3 point hit to hardware gross margin | Supply Chain Dispatch | Fact (pending proposal); analyst estimate |
| Oct 2, 2026 | Talonfield said to have hired advisers to explore a sale. Arbelion and two private equity firms said to be interested. Shares up 12% to US$17.20. Company declines to comment | Capital Markets Wire | Rumor (process); Fact (price move) |
| Q1 2027 (expected) | Final decision on the LiDAR tariff proposal | Supply Chain Dispatch (Sep 15, 2026) | Fact (expected timing) |
| 2027 (planned) | Norvale pilots Kinetic Aisle robots at five distribution centers | RoboEconomy Weekly (Jun 24, 2026) | Fact (stated plan) |

**Share price reactions reported in coverage**

| Date | Trigger | Move | Close reported | Prior close (calculated) |
|---|---|---|---|---|
| Nov 17, 2025 (inferred) | Auditor change | -2.1% | Not reported | Not available |
| Mar 10, 2026 | Record Q4, 2026 guidance | +9% | US$31.20 | About US$28.62 |
| March 2026 | 52-week high | n/a | US$31.75 | n/a |
| April 2026 | FieldOS outage | Not reported | Not reported | Not available |
| May 12, 2026 | Greyfin short report | -18% | US$19.85 | About US$24.21 |
| Jun 24, 2026 | Norvale buys Kinetic Aisle | -6% | Not reported | Not available |
| Aug 7, 2026 | Guidance cut | -14% | US$16.40 | About US$19.07 |
| Oct 2, 2026 | Sale exploration report | +12% | US$17.20 | About US$15.36 |
| Oct 16, 2026 | Deal brief reference price | n/a | US$17.85 (deal brief) | n/a |

Between the March high of US$31.75 and the day before the Greyfin report (about US$24.21), the shares fell about 24%. No article explains this fall.

### Findings

Headline: three findings are Critical.
- The deal model still uses guidance the company withdrew on August 7, 2026 (NEWS-01).
- Seven data points across the coverage point to problems with Q4 2025 revenue (NEWS-02).
- A short seller alleged that bill-and-hold sales inflated 2025 revenue (NEWS-03). The company has since disclosed one such sale being returned (NEWS-04).

The most important High findings are that the largest customer is building its own robots (NEWS-09) and that a cyber incident hit FieldOS without a formal cyber filing (NEWS-10). No article reports any litigation.

#### NEWS-01: 2026 guidance cut leaves the deal model on an outdated management case
- **Finding:** On August 7, 2026, Talonfield cut its 2026 guidance to US$470.0-490.0 million revenue and US$70.0-78.0 million Adjusted EBITDA, down from US$555.0-565.0 million and US$114.0-122.0 million. The deal model (v3) is dated September 2026, after the cut, but still uses the March 2026 case of US$560.0 million and US$118.0 million.
- **Evidence:** The company "cut its 2026 revenue outlook to $470 million to $490 million, from $555 million to $565 million". Company explanation (interim CFO Rachel Simmons): "2026 is a reset year."
- **Source:** `data/news/2026-08-07_capital-markets-wire_guidance-cut.md` (Capital Markets Wire, August 7, 2026). Original guidance: `data/news/2026-03-10_capital-markets-wire_record-q4.md` (Capital Markets Wire, March 10, 2026). Deal model basis: `data/deal-brief.md`.
- **Claim type:** Fact
- **Severity:** Critical
- **Confidence:** High. This is on-record company guidance plus an earnings-call quote. Only one outlet reports it, so confirm it against the primary filing.
- **Deal impact:** Valuation (IC Q1, Q6). Calculated effects:
  - At the midpoints, revenue falls US$80.0 million (14.3%) and Adjusted EBITDA falls US$44.0 million (37.3%).
  - The new revenue midpoint is about 4.4% below FY2025 revenue. The old case assumed about 11.5% growth.
  - Adjusted EBITDA margin at the midpoint drops from 21.1% to 15.4%.
  - Keep the implied enterprise value of about US$1,357.0 million (about 11.5x times US$118.0 million). The multiple on the new range is then about 17.4x to 19.4x, or 18.3x at the midpoint.
  - Two brokers downgraded the stock and it fell 14% to US$16.40.
- **Cross-check:**
  - SEC filings: the Q2 2026 Form 8-K (Item 2.02 press release) and Q2 2026 Form 10-Q. The finding is confirmed if they show these ranges. Also check for any later guidance update.
  - Financial data: H1 2026 actuals, Q3 2026 trading and backlog.
  - Deal team: ask why model v3 kept the March case.

#### NEWS-02: News items converge on how Q4 2025 hardware revenue was recognized
- **Finding:** Five articles from two outlets, covering about nine months, contain seven data points that trace one issue: whether Q4 2025 hardware revenue, including bill-and-hold sales, was booked before delivery. In order, they are:
  1. A Q3 2025 material weakness over hardware contracts.
  2. An auditor change after the old auditor planned extra work on Q4 deals.
  3. A CFO exit reportedly linked to a dispute over revenue timing.
  4. A Q4 revenue beat with weak cash flow.
  5. An adverse opinion on internal controls.
  6. Short seller allegations of bill-and-hold abuse.
  7. The company's own disclosure that a bill-and-hold sale was returned.
- **Evidence:** In November 2025, the outgoing auditor "had warned that it would need to expand its audit work on fourth-quarter deals with unusual delivery terms". In August 2026, Q2 revenue included "a $9.4 million credit after a customer returned robots that had been sold under a bill-and-hold arrangement in late 2025".
- **Source:**
  - `data/news/2025-11-18_capital-markets-wire_auditor-switch.md` (Capital Markets Wire, November 18, 2025)
  - `data/news/2026-01-23_columbus-business-ledger_cfo-exit.md` (Columbus Business Ledger, January 23, 2026)
  - `data/news/2026-03-10_capital-markets-wire_record-q4.md` (Capital Markets Wire, March 10, 2026)
  - `data/news/2026-05-12_capital-markets-wire_short-seller-report.md` (Capital Markets Wire, May 12, 2026)
  - `data/news/2026-08-07_capital-markets-wire_guidance-cut.md` (Capital Markets Wire, August 7, 2026)
  - Component cards: NEWS-03 to NEWS-08.
- **Claim type:** Mixed. Facts: NEWS-04, NEWS-05, NEWS-07, NEWS-08. Rumor: the dispute in NEWS-06. Allegation: NEWS-03. The link between them is my inference.
- **Severity:** Critical
- **Confidence:** Medium. The data points come from separate sources. The company itself confirmed the core point: late-2025 bill-and-hold sales existed and at least one was returned. How large any misstatement is remains unknown.
- **Deal impact:**
  - Valuation: FY2025 revenue and its 19% growth may be overstated (IC Q1).
  - Closing risk: a restatement or a regulatory inquiry could delay signing or closing (IC Q2).
  - Governance (IC Q5).
  - Post-closing: securities claims and the need for indemnity (IC Q6).
  - Reputation.
- **Cross-check:** Four pieces of evidence would settle the issue:
  1. Total Q4 2025 revenue booked under bill-and-hold, by customer.
  2. Where those robots are now: delivered, still held, or returned.
  3. Written customer requests for each arrangement.
  4. The revenue threshold in the 2025 executive bonus plan.

  Where to look: the FY2025 Form 10-K revenue note and Item 9A, the Q1 and Q2 2026 Forms 10-Q, the proxy statement, data-room contracts, the Columbus warehouse inventory records, and court records for any securities class action.

#### NEWS-03: Greyfin short report alleges bill-and-hold sales were used to hit 2025 revenue and bonus targets
- **Finding:** On May 12, 2026, short seller Greyfin Research alleged that Talonfield used bill-and-hold arrangements to meet its 2025 revenue targets. Greyfin disclosed that it is betting against the stock. Shares fell 18% to US$19.85 that day.
- **Evidence:** Greyfin alleges: "\"Hundreds\" of robots booked as fourth-quarter sales were still sitting in Talonfield's Columbus warehouse in February 2026". Company response: the report is "misleading and inaccurate", and revenue recognition "complies with GAAP and was reviewed by our independent auditor". The company said it "would not comment on its customers."
- **Source:** `data/news/2026-05-12_capital-markets-wire_short-seller-report.md` (Capital Markets Wire, May 12, 2026)
- **Claim type:** Allegation. Greyfin is an interested party with a disclosed short position.
- **Severity:** Critical, if proven. It could mean a FY2025 restatement, regulatory exposure, securities claims, and an integrity issue tied to executive bonuses.
- **Confidence:**
  - Low for the three specific claims. They rest on anonymous former employees and photos that have not been checked independently, from an interested party.
  - Medium for the core claim that late-2025 bill-and-hold sales existed and at least one was returned. The company itself disclosed a US$9.4 million return on August 7, 2026 (NEWS-04).
- **Deal impact:** Valuation, closing risk, post-closing and reputation (IC Q1, Q2, Q5, Q6). The company's response, as reported, asserts GAAP compliance but does not deny using bill-and-hold arrangements. The "independent auditor" it cites is presumably Linden Barr. Linden Barr gave an adverse controls opinion for the same year (NEWS-07).
- **Cross-check:** See the table below. Also check court records for securities class actions filed after the 18% drop on May 12, 2026. Check SEC filings for any disclosed SEC inquiry or subpoena.

Greyfin's allegations one by one:

| # | Allegation | Evidence Greyfin offered (as reported) | Company response | What would confirm or refute it |
|---|---|---|---|---|
| 1 | "Hundreds" of robots booked as Q4 2025 sales were still in the Columbus warehouse in February 2026 | Photographs; interviews with two former warehouse employees | "misleading and inaccurate"; revenue recognition GAAP-compliant and reviewed by the auditor | The FY2025 10-K disclosure of bill-and-hold revenue and goods held for customers. Warehouse inventory and shipping logs for January and February 2026. Q1 2026 deliveries of units billed in Q4 2025. Whether the units were set aside and tagged by customer |
| 2 | Talonfield's "largest customer did not ask for the bill-and-hold arrangement" | One former Talonfield sales employee | Declined to comment on customers | Written customer requests and contract amendments in the data room. Under ASC 606, a bill-and-hold sale generally needs a substantive reason, such as a customer request. Later coverage names Norvale as the largest customer (NEWS-09) |
| 3 | Without the bill-and-hold sales, Talonfield "would have missed the revenue target in its executive bonus plan" | Not described in the article | No specific response reported | The proxy statement: the 2025 bonus plan revenue threshold and payouts. Compare the threshold with FY2025 revenue of US$502.3 million minus Q4 bill-and-hold revenue. Also the compensation committee minutes and the clawback policy |

#### NEWS-04: Company disclosed a US$9.4 million credit for robots returned from a late-2025 bill-and-hold sale
- **Finding:** Talonfield said Q2 2026 revenue included a US$9.4 million credit after a customer returned robots sold under a bill-and-hold arrangement in late 2025. This is the company's own confirmation that such sales existed and that at least one was returned. It came about three months after the company called Greyfin's report "misleading and inaccurate".
- **Evidence:** "a $9.4 million credit after a customer returned robots that had been sold under a bill-and-hold arrangement in late 2025". The customer is not named.
- **Source:** `data/news/2026-08-07_capital-markets-wire_guidance-cut.md` (Capital Markets Wire, August 7, 2026)
- **Claim type:** Fact
- **Severity:** High
- **Confidence:** High. This is a company statement reported in earnings coverage. Confirm it in the Q2 2026 Form 10-Q.
- **Deal impact:** Valuation, plus restatement and closing risk (IC Q1, Q2). Calculated:
  - The credit equals about 6.1% of Q4 2025 revenue (US$154.4 million).
  - It equals about 35.6% of the Q4 beat over consensus (about US$26.4 million).
  - Illustration: if this sale is treated as never earned in 2025, FY2025 growth falls from 19% to about 16.8%, and Q4 growth falls from 32% to about 24%.

  The company booked the return as a credit in the current period instead of correcting 2025. That is correct only if the original arrangement met the bill-and-hold criteria at the time. This needs accounting review.
- **Cross-check:**
  - SEC filings: the Q2 2026 Form 10-Q (revenue note, returns, contract balances, legal proceedings).
  - Data room: who the customer is, the return agreement, and its dates. If other late-2025 bill-and-hold units are still undelivered or disputed, this was not a one-off.
  - Timing test: if the return was requested before May 12, 2026, the company's response to Greyfin that day needs a fresh look.
  - Court records: any dispute with this customer.
  - Whether the customer is Norvale: not found in news coverage.

#### NEWS-05: Auditor replaced weeks before year-end after warning of a material weakness and extra work on Q4 deals
- **Finding:** In a filing on Friday, November 14, 2025 (inferred), Talonfield replaced Hartwell & Pryce, its auditor since 2016. The new auditor, Linden Barr LLP, is a Cleveland regional firm that audits fewer than ten listed companies. The filing reported no disagreements. It also disclosed that the outgoing auditor had flagged a Q3 2025 material weakness and planned expanded work on Q4 deals with unusual delivery terms.
- **Evidence:** The outgoing auditor "had warned that it would need to expand its audit work on fourth-quarter deals with unusual delivery terms." Company response: the change followed "a routine review to find the best fit for a growing company." An accounting professor commented: "Investors will want to know why the company did not want the expanded procedures."
- **Source:** `data/news/2025-11-18_capital-markets-wire_auditor-switch.md` (Capital Markets Wire, November 18, 2025)
- **Claim type:** Fact (filing contents and company statement, as reported). The professor's view is commentary.
- **Severity:** High
- **Confidence:** High. The article reports from the company's own filing. Check the exact filing wording.
- **Deal impact:** Governance, and how far the FY2025 audited numbers can be relied on (IC Q1, Q5). The "unusual delivery terms" are consistent with the bill-and-hold sales that were later alleged and partly confirmed (NEWS-03, NEWS-04). This supports an independent quality-of-earnings review of Q4 2025 before signing. Shares closed down 2.1% on Monday, November 17, 2025 (inferred).
- **Cross-check:**
  - SEC filings: Form 8-K Item 4.01 from around November 14, 2025, and the outgoing auditor's Exhibit 16 letter. Check whether they list the weakness and the planned Q4 procedures as reportable events. Any disagreement in the letter would contradict the company's account.
  - FY2025 Form 10-K: the auditor's reports and audit fees.
  - Whether Linden Barr carried out the expanded Q4 procedures.
  - Audit committee minutes on choosing the new auditor.

#### NEWS-06: CFO resigned with a US$0.9 million payment; anonymous sources tie the exit to a dispute with the CEO over booking Q4 orders
- **Finding:** A filing on Wednesday, January 21, 2026 (inferred) said CFO Daniel Okafor's departure "was not the result of any disagreement with the Company". It disclosed a US$0.9 million (US$900,000) separation payment. Two unnamed people said the exit followed weeks of tension with CEO Marcus Hale over how to book several large Q4 hardware orders.
- **Evidence:**
  - First source: Okafor "had argued that revenue on some orders should not be recognized until the robots were delivered to customer sites in 2026."
  - Second source: the dispute was "about timing, not about whether the orders were real."
  - The company repeated its no-disagreement statement and declined further comment. Okafor could not be reached.
- **Source:** `data/news/2026-01-23_columbus-business-ledger_cfo-exit.md` (Columbus Business Ledger, January 23, 2026)
- **Claim type:** Rumor (reason for the exit). Fact (resignation, filing statement, separation payment, interim CFO appointment).
- **Severity:** High
- **Confidence:**
  - Low for the dispute. It rests on two anonymous sources and is unconfirmed. It is consistent with NEWS-03, NEWS-04 and NEWS-05, which makes it more plausible but does not confirm it.
  - High for the filing facts.
- **Deal impact:** Governance and management integrity (IC Q5), the decision on retaining the CEO, and valuation if Q4 revenue was pulled forward (IC Q1). Compensation consultants said separation payments "are uncommon when an executive resigns voluntarily." Rachel Simmons, then corporate controller, was still interim CFO on August 7, 2026. So the CFO role has been filled on an interim basis for at least six and a half months.
- **Cross-check:**
  - SEC filings: Form 8-K Item 5.02 from around January 21, 2026, and the separation agreement (release of claims, cooperation, non-disparagement). The FY2025 Form 10-K certifications (who signed). The proxy statement for the payment.
  - Board or audit committee minutes on Q4 revenue would confirm or contradict the reported dispute.
  - Court and agency records: any claim by Okafor, including whistleblower complaints.

#### NEWS-07: New auditor gave an adverse opinion on internal controls
- **Finding:** When FY2025 results were reported on March 10, 2026, Talonfield disclosed that Linden Barr gave an adverse opinion on internal controls over financial reporting. The cause was the material weakness first reported in November 2025, which covered controls over certain hardware contracts.
- **Evidence:** "its new auditor had issued an adverse opinion on internal controls because of the material weakness first reported in November." Company response: not found in news coverage.
- **Source:** `data/news/2026-03-10_capital-markets-wire_record-q4.md` (Capital Markets Wire, March 10, 2026). The weakness is described in `data/news/2025-11-18_capital-markets-wire_auditor-switch.md` (Capital Markets Wire, November 18, 2025).
- **Claim type:** Fact
- **Severity:** High
- **Confidence:** High. This is a company disclosure as reported. Confirm it in the FY2025 Form 10-K.
- **Deal impact:**
  - Governance (IC Q5).
  - Remediation and Sarbanes-Oxley integration cost after closing.
  - Higher risk that FY2025 hardware revenue is misstated (IC Q1).
  - Supports specific representations on controls and a remediation covenant (IC Q6).
  - Remediation status: not found in news coverage.
- **Cross-check:** SEC filings: FY2025 Form 10-K Item 9A and the auditor's controls report. Check what type of opinion the auditor gave on the financial statements themselves (not found in news coverage). Check Item 4 of the Q1 and Q2 2026 Forms 10-Q for remediation progress.

#### NEWS-08: Record Q4 2025 beat came with a jump in receivables and weak operating cash flow
- **Finding:** Q4 2025 revenue was US$154.4 million, up 32% and about US$26.4 million above the roughly US$128.0 million analysts expected. FY2025 revenue rose 19% to US$502.3 million. An unnamed analyst said receivables "jumped" and FY2025 operating cash flow fell under US$10.0 million.
- **Evidence:** "Receivables jumped and operating cash flow fell to under $10 million for the year," and "We want to see the fourth-quarter shipments turn into cash before we get more constructive." Company response: not found in news coverage. Shares rose 9% to US$31.20.
- **Source:** `data/news/2026-03-10_capital-markets-wire_record-q4.md` (Capital Markets Wire, March 10, 2026)
- **Claim type:** Fact (reported results). The receivables and cash flow points are commentary from one unnamed analyst.
- **Severity:** High
- **Confidence:** Medium. The results are on record. The receivables and cash flow points rest on one unnamed analyst.
- **Deal impact:** Quality of revenue (IC Q1), and working capital and liquidity (IC Q4). Calculated:
  - Q4 made up 30.7% of FY2025 revenue.
  - Revenue for the first nine months grew only about 14%, so Q4 lifted full-year growth to 19%.

  Revenue running ahead of cash is consistent with the bill-and-hold concern (NEWS-02).
- **Cross-check:**
  - SEC filings: the FY2025 Form 10-K cash flow statement. Also receivables and days sales outstanding (DSO) at December 31, 2025 against 2024, contract assets, and quarterly revenue.
  - Financial data: receivables aging by customer, especially the largest customer, and how much of the Q4 2025 receivables was collected in H1 2026.

#### NEWS-09: Largest customer Norvale bought a robot startup to build its own robots
- **Finding:** Norvale Retail Group, described as Talonfield's largest customer, bought Kinetic Aisle for an undisclosed amount. Kinetic Aisle is a 60-person warehouse robot startup. Norvale plans to pilot its robots at five distribution centers in 2027. Talonfield shares fell 6% on the news.
- **Evidence:** Norvale's senior vice president of supply chain: "We want to own more of our automation stack and reduce our dependence on any single vendor." Asked about Talonfield, he said Norvale will "continue to work with existing partners while we evaluate the right long-term mix." Talonfield's response: not found in news coverage.
- **Source:** `data/news/2026-06-24_roboeconomy-weekly_norvale-buys-kinetic-aisle.md` (RoboEconomy Weekly, June 24, 2026). Industry trend support: `data/news/2026-08-20_warehouse-tech-review_market-report.md` (Warehouse Tech Review, August 20, 2026).
- **Claim type:** Fact (the acquisition and the customer's on-record statements). "Largest customer" is the outlet's own description.
- **Severity:** High. It could be Critical, depending on Norvale's share of revenue (not found in news coverage).
- **Confidence:** High for the acquisition and the quotes. Medium for "largest customer" until filings confirm it.
- **Deal impact:** Valuation and customer concentration (IC Q1, Q3). Volumes are at risk from 2027 if the pilot scales. Greyfin's bill-and-hold allegation concerned "Talonfield's largest customer" (NEWS-03), so by inference it concerns Norvale. Whether Norvale is also the customer behind the US$9.4 million return (NEWS-04) is not found in news coverage. This supports a customer-retention diligence workstream and possibly price protection tied to Norvale volumes (IC Q6).
- **Cross-check:**
  - SEC filings: customer concentration disclosures in the FY2025 Form 10-K and Q2 2026 Form 10-Q. These would confirm "largest customer" and give Norvale's share of revenue and receivables.
  - Data room: contract term, minimum volumes, exclusivity, change-of-control and termination rights, and FieldOS renewals.
  - Financial data: Norvale bookings and backlog trend.
  - Court records: any dispute with Norvale.

#### NEWS-10: FieldOS cyber incident stopped robots at 40-plus customer sites; no Item 1.05 Form 8-K; US$2.3 million of credits followed
- **Finding:** In April 2026, Talonfield took parts of FieldOS offline after "unauthorized activity". Robots at at least 40 customer sites stopped for up to three days (about April 11 to 14; start date inferred). As of April 14, no Form 8-K Item 1.05 had been filed, and management called the incident "not material". On August 7, the company disclosed US$2.3 million of credits to affected customers.
- **Evidence:**
  - Spokesperson: management had "determined that the incident is not material." The company called the incident "isolated" and said it found "no evidence that customer data was taken."
  - Pinecrest Distribution COO: "We had to go back to manual picking for three days in the middle of our biggest promotion of the quarter," and "We are reviewing our options."
  - On Sunday, April 12, 2026 (inferred), a ransomware group claimed it took "fleet configuration and customer site data". The outlet could not verify this.
- **Source:** `data/news/2026-04-14_supply-chain-dispatch_fieldos-outage.md` (Supply Chain Dispatch, April 14, 2026). Credits: `data/news/2026-08-07_capital-markets-wire_guidance-cut.md` (Capital Markets Wire, August 7, 2026).
- **Claim type:**
  - Fact: the outage, the platform being taken offline, no Item 1.05 filing as of April 14, the company's statements, and the US$2.3 million of credits.
  - Rumor: the ransomware group's data-theft claim.
  - Customer claim: Pinecrest's account of the impact and its possible action.
- **Severity:** High
- **Confidence:** High for the outage, the missing filing as of April 14, and the credits. Low for data theft.
- **Deal impact:** Closing and post-closing risk (IC Q2, Q3): a possible SEC disclosure question, customer claims, data-breach exposure, remediation and insurance. FieldOS is the strategic software asset. The US$2.3 million of credits is about 2.0% of Q2 2026 revenue. Item 1.05 materiality is not only a dollar test, so the 40-plus sites and the data-theft claim also count. No share price reaction was reported. This supports a specific cyber representation and indemnity (IC Q6).
- **Cross-check:**
  - SEC filings: any later Form 8-K (Item 1.05 or 8.01), FY2025 Form 10-K Item 1C, and the risk factors and legal proceedings in the Q1 and Q2 2026 Forms 10-Q. A later Item 1.05 filing, or any description of data loss, would contradict the April statements.
  - Court records: suits by Pinecrest or other customers, or data-breach claims.
  - Financial data: total incident cost beyond US$2.3 million, insurance recoveries, and customer losses at affected sites.

#### NEWS-11: Management's public statements were repeatedly weakened by later events
- **Finding:** In five episodes, Talonfield's on-record statements were later weakened by its own disclosures or by events. This affects how much weight to give management's representations and its projections.
- **Evidence:**
  - Auditor change (November 2025): the company called it "a routine review to find the best fit for a growing company". Yet the outgoing auditor had just flagged a material weakness and planned extra Q4 work (NEWS-05).
  - CFO exit (January 2026): "not the result of any disagreement with the Company". Yet there was a US$0.9 million payment and reports of a dispute (NEWS-06).
  - Guidance (March 2026): US$555.0-565.0 million revenue and US$114.0-122.0 million Adjusted EBITDA, repeated at the investor day. Five months later the midpoints were cut by 14.3% and 37.3% (NEWS-01).
  - Outage (April 2026): called "isolated" and "not material". US$2.3 million of credits followed (NEWS-10).
  - Short report (May 2026): called "misleading and inaccurate". In August the company disclosed the US$9.4 million bill-and-hold return (NEWS-04).
- **Source:**
  - `data/news/2025-11-18_capital-markets-wire_auditor-switch.md` (Capital Markets Wire, November 18, 2025)
  - `data/news/2026-01-23_columbus-business-ledger_cfo-exit.md` (Columbus Business Ledger, January 23, 2026)
  - `data/news/2026-03-10_capital-markets-wire_record-q4.md` (Capital Markets Wire, March 10, 2026)
  - `data/news/2026-04-14_supply-chain-dispatch_fieldos-outage.md` (Supply Chain Dispatch, April 14, 2026)
  - `data/news/2026-05-12_capital-markets-wire_short-seller-report.md` (Capital Markets Wire, May 12, 2026)
  - `data/news/2026-08-07_capital-markets-wire_guidance-cut.md` (Capital Markets Wire, August 7, 2026)
- **Claim type:** Fact (each statement and each later disclosure is on record). The pattern is my inference.
- **Severity:** High
- **Confidence:** Medium. Each element is on record, but none of the statements has been shown to be false. The CFO element rests on anonymous sources.
- **Deal impact:** Governance (IC Q5) and deal protections (IC Q6):
  - Rely less on management projections and build a fresh base case.
  - Seek stronger representations and specific indemnities.
  - Commission an independent quality-of-earnings review.
- **Cross-check:** Compare each statement with the matching filing text: Form 8-K Items 4.01, 5.02 and 2.02, and the Q1 and Q2 2026 Forms 10-Q. Also check board and audit committee minutes for each episode.

#### NEWS-12: Fourth restructuring since 2022, with the costs excluded from Adjusted EBITDA every year
- **Finding:** A state notice reported on July 30, 2026 shows Talonfield cutting about 60 jobs (4% of staff), mostly in hardware assembly and field services. It is the fourth restructuring program since 2022. Each year the company has left the costs out of Adjusted EBITDA.
- **Evidence:** "Each year the company has excluded restructuring costs from its Adjusted EBITDA as 'not part of ongoing operations.'" Company response: the cuts would "align our cost base with near-term demand."
- **Source:** `data/news/2026-07-30_columbus-business-ledger_layoffs.md` (Columbus Business Ledger, July 30, 2026). Headcount: `data/news/2026-03-28_columbus-business-ledger_scholarship.md` (Columbus Business Ledger, March 28, 2026).
- **Claim type:** Fact
- **Severity:** Medium
- **Confidence:** High for the cuts (state notice) and for the yearly exclusion, as reported. The amounts are not found in news coverage.
- **Deal impact:**
  - Valuation (IC Q1, Q6): restructuring costs that recur every year but are treated as one-off inflate Adjusted EBITDA, which is the basis for the 11.5x multiple.
  - The cuts came eight days before the August 7 guidance cut and point to weaker demand.
  - Cuts in field services could strain service levels after the April outage.
  - Calculated: 60 jobs is about 4.1% of the roughly 1,450 staff reported in March 2026, consistent with the 4% figure.
- **Cross-check:**
  - SEC filings: the Adjusted EBITDA reconciliations in the Forms 10-K and 10-Q for 2022 to 2026 (restructuring add-backs by year), any Form 8-K Item 2.05, and the state notice itself.
  - Financial data: recompute Adjusted EBITDA with restructuring treated as recurring, and check for overlap with the US$35.0 million synergy case.

#### NEWS-13: Talonfield's only LiDAR supplier is in China, and a tariff rise from 7.5% to 25% is proposed
- **Finding:** A proposal would raise tariffs on LiDAR modules imported from China from 7.5% to 25%. A final decision is expected in Q1 2027. Talonfield reportedly buys all its LiDAR sensors from one Chinese supplier. One analyst estimated a two to three point fall in hardware gross margin if the increase takes effect.
- **Evidence:** Talonfield "buys all of its LiDAR sensors from a single supplier in China." Head of an industry trade group: "Qualifying a new sensor supplier takes 12 to 18 months." Company response: not found in news coverage.
- **Source:** `data/news/2026-09-15_supply-chain-dispatch_lidar-tariffs.md` (Supply Chain Dispatch, September 15, 2026)
- **Claim type:** Fact (the pending proposal and the single-supplier status, as reported). The margin effect is an analyst estimate.
- **Severity:** Medium
- **Confidence:** Medium. One outlet reports it, the proposal is not final, and the estimate comes from one unnamed analyst.
- **Deal impact:** Valuation from 2027 (hardware margin) and the post-closing supply plan, since adding a second supplier takes 12 to 18 months. The decision is due after the IC meeting and possibly around closing, so the model should include it as a downside case.
- **Cross-check:**
  - SEC filings: risk factors and supplier concentration in the FY2025 Form 10-K.
  - Data room: the supply agreement (pricing, tariff pass-through, term) and whether customer contracts allow cost pass-through.
  - Financial data: hardware revenue, hardware gross margin, LiDAR cost per robot, and sensor inventory on hand.

#### NEWS-14: Market forecast to grow about 15% a year while Talonfield guides to a decline; large retailers are building robots in-house
- **Finding:** Calder Insights forecasts that North American warehouse AMR spending will grow about 15% a year through 2030. It ranks Talonfield third with about 11% share, behind two larger rivals including Vantor Robotics. Calder said FieldOS "remains a differentiator", but large retailers are increasingly building robots in-house.
- **Evidence:** Calder "warned that large retailers are increasingly developing robots in-house." Company response: not found in news coverage.
- **Source:** `data/news/2026-08-20_warehouse-tech-review_market-report.md` (Warehouse Tech Review, August 20, 2026)
- **Claim type:** Fact (a third-party research report; its figures are forecasts and estimates)
- **Severity:** Medium
- **Confidence:** Medium. One research firm, reported by one outlet.
- **Deal impact:** Growth and valuation (IC Q1).
  - The new 2026 revenue midpoint (US$480.0 million) is about 4.4% below FY2025, while the market is forecast to grow about 15% a year.
  - That gap points to problems specific to Talonfield, or lost market share, rather than a market downturn. This is my inference. Talonfield's revenue also includes software and services, and its regional mix is not found in news coverage.
  - The in-house trend matches Norvale's move (NEWS-09).
  - Market growth does support Arbelion's strategic case for entering the market.
- **Cross-check:** SEC filings: the competition section of the FY2025 Form 10-K. Financial data: revenue by product line and region, bookings, win and loss data, and customer churn.

#### NEWS-15: Sale-process leak named Arbelion; the 34% premium is measured against a price already lifted by the leak
- **Finding:** On October 2, 2026, unnamed people said Talonfield had hired advisers to explore a sale, and that Arbelion and two private equity firms had shown interest. Shares rose 12% to US$17.20 on the report. So the October 16 close of US$17.85, which the deal brief uses for the 34% premium, already reflects the leak.
- **Evidence:** "Arbelion Industries and two private equity firms are among the parties that have expressed interest, the people said." Company response: "declined to comment."
- **Source:** `data/news/2026-10-02_capital-markets-wire_sale-exploration.md` (Capital Markets Wire, October 2, 2026). Reference price: `data/deal-brief.md`.
- **Claim type:** Rumor (anonymous sources on the process and the bidders). Fact (the share price move).
- **Severity:** Medium
- **Confidence:** Medium. Arbelion's interest matches the deal brief. The private equity interest is unconfirmed.
- **Deal impact:** Price negotiation (IC Q6). Calculated:
  - The implied close before the report is about US$15.36 (US$17.20 / 1.12). Against that price, US$24.00 is a premium of about 56%, not 34%.
  - US$24.00 is also close to the implied price just before the Greyfin report (about US$24.21). Since then, EBITDA guidance has been cut by 37.3% at the midpoint, and the largest customer has started building its own robots.
  - By the day before the report, the shares were down about 51.6% from the March 2026 high of US$31.75.

  Private equity interest may add pressure on price. The public naming of Arbelion is a confidentiality and reputation issue.
- **Cross-check:**
  - Trading data: a price from before the leak, for example the 30-day volume-weighted average before October 2, 2026.
  - SEC filings: any later Schedule 13D or 13G filings, and the background-of-the-merger section of any proxy.
  - Talonfield's advisers: ask about other bidders and the source of the leak.

#### NEWS-16: FieldOS 5 and the software-mix target depend on Gen-3 robots and are unproven
- **Finding:** On February 10, 2026, Talonfield launched FieldOS 5 with AI route planning and announced three new enterprise agreements, including a Harbor & Vine Grocers expansion to 12 more distribution centers. CEO Marcus Hale said software would be "more than a third of revenue" within three years. Analysts noted the new features need Talon Gen-3 robots or newer.
- **Evidence:** Hale: "FieldOS is becoming the operating system of the warehouse." The company says the route planning "can raise picking productivity by up to 18%". Analysts noted that "the new features require Talon Gen-3 robots or newer."
- **Source:** `data/news/2026-02-10_warehouse-tech-review_fieldos-5-launch.md` (Warehouse Tech Review, February 10, 2026)
- **Claim type:** Fact (the launch, the agreements and the statements are on record). The productivity and software-mix claims are unverified company claims.
- **Severity:** Low
- **Confidence:** Medium. These are company claims made at its own customer conference, reported by one outlet. Two of the three new customers are not named.
- **Deal impact:** Valuation (IC Q1). A larger software share would support a higher multiple, but only if it is real. Customers with older fleets must buy Gen-3 robots to use the new features. That could help hardware sales or slow software adoption.
- **Cross-check:**
  - SEC filings: revenue split in the FY2025 Form 10-K (hardware, FieldOS subscription, services), to measure today's software share.
  - Financial data: FieldOS recurring revenue, net retention, and the installed base by robot generation.
  - Data room: the Harbor & Vine contract.

### Positive or mitigating points

- **Market tailwind.** Calder forecasts about 15% annual growth to 2030. Talonfield ranks third with about 11% share, and FieldOS "remains a differentiator" (`data/news/2026-08-20_warehouse-tech-review_market-report.md`, Warehouse Tech Review, August 20, 2026).
- **Customer wins.** Three new enterprise agreements, including the Harbor & Vine Grocers expansion to 12 more distribution centers. Analysts at the event reported positive customer feedback on FieldOS 5 (`data/news/2026-02-10_warehouse-tech-review_fieldos-5-launch.md`, Warehouse Tech Review, February 10, 2026).
- **Orders reportedly real.** One anonymous source said the CFO dispute was "about timing, not about whether the orders were real". That suggests a timing issue rather than fictitious sales. This is a rumor (`data/news/2026-01-23_columbus-business-ledger_cfo-exit.md`, Columbus Business Ledger, January 23, 2026).
- **Some transparency.** The company disclosed the outgoing auditor's material weakness and planned procedures, the adverse controls opinion, the US$9.4 million return and the US$2.3 million of outage credits, instead of leaving them out (Capital Markets Wire, November 18, 2025; March 10, 2026; August 7, 2026).
- **Underlying Q2 revenue.** Adding back the two credits gives Q2 2026 revenue of about US$124.6 million, about 5.9% above the implied Q2 2025 figure of about US$117.6 million. This is calculated and assumes both credits reduced reported revenue, as the article implies (`data/news/2026-08-07_capital-markets-wire_guidance-cut.md`).
- **Norvale shift will take time.** Norvale says it will "continue to work with existing partners". The Kinetic Aisle pilot covers only five distribution centers in 2027, and Kinetic Aisle has 60 staff. So any switch away from Talonfield would likely be gradual. This is my inference (`data/news/2026-06-24_roboeconomy-weekly_norvale-buys-kinetic-aisle.md`).
- **Tariff not final.** The tariff rise is only a proposal, with a decision expected in Q1 2027. The estimated effect is limited to 2 to 3 points of hardware gross margin (`data/news/2026-09-15_supply-chain-dispatch_lidar-tariffs.md`).
- **Small layoffs.** The July 2026 cut is modest: about 60 jobs, or 4% of staff (`data/news/2026-07-30_columbus-business-ledger_layoffs.md`).
- **Systems restored.** The company says all systems were back by April 14 and it found no evidence that customer data was taken. This is a company claim (`data/news/2026-04-14_supply-chain-dispatch_fieldos-outage.md`).

### Articles reviewed with no diligence relevance

- `data/news/2026-03-28_columbus-business-ledger_scholarship.md` (Columbus Business Ledger, March 28, 2026): a US$1.5 million, five-year scholarship program at three Ohio community colleges. It has no diligence relevance. Its only useful data point is a headcount of about 1,450, which matches the July 2026 layoff figure.

### Gaps and questions for management

**Gaps in news coverage (not found in news coverage)**

- **Litigation.** No article reports any lawsuit, class action, derivative suit, customer claim, arbitration, regulatory investigation or subpoena. This needs checking against court records, especially after the 18% drop on May 12, 2026 and the 14% drop on August 7, 2026.
- **Balance sheet.** Net debt, debt terms, covenants and liquidity are not covered (IC Q4). The only data point is the analyst's comment that FY2025 operating cash flow was under US$10.0 million.
- **Quarterly results.** Q1 2026 and Q3 2026 results are not covered.
- **Bill-and-hold details.** No article gives the total Q4 2025 bill-and-hold revenue, the number of units, or who the returning customer is.
- **Norvale.** Its share of revenue and its contract terms are not reported.
- **Restructuring.** The costs excluded from Adjusted EBITDA are not reported for any year.
- **CFO and controls.** No permanent CFO appointment is reported, and the remediation status of the material weakness is not reported.
- **Cyber incident.** No article says whether any Item 1.05 Form 8-K was filed after April 14, 2026, whether a ransom was paid, or what the forensic review found.
- **Company responses.** Talonfield's response to Norvale's acquisition, the market report and the tariff proposal is not reported.
- **Revenue mix.** The split between hardware, software and services is not reported.

**Dates to test against SEC filings and court records**

- **November 14, 2025 (inferred): auditor change.** Expect a Form 8-K Item 4.01 with an Exhibit 16 letter.
- **January 21, 2026 (inferred): CFO departure.** Expect a Form 8-K Item 5.02 and the separation agreement.
- **March 10, 2026: FY2025 results and adverse controls opinion.** Expect a Form 8-K Item 2.02 and the Form 10-K (Item 9A).
- **About April 11 to 14, 2026: cyber incident.** No Item 1.05 filing as of April 14. Check later Forms 8-K and the Q1 2026 Form 10-Q.
- **May 12, 2026: Greyfin report.** Check for class actions filed after this date, and for disclosure in the Q1 2026 Form 10-Q.
- **April 1 to June 30, 2026: bill-and-hold return.** Check the Q2 2026 Form 10-Q. If the Q1 2026 Form 10-Q was filed after the return was requested, check whether it mentions the return.
- **June 24, 2026: Norvale acquisition.** Check customer-risk disclosure in the Q2 2026 Form 10-Q.
- **July 30, 2026 or earlier: state layoff notice.** Check for a Form 8-K Item 2.05 and the restructuring note.
- **August 7, 2026: guidance cut.** Check the Form 8-K Item 2.02, and check for suits filed after the 14% drop.
- **October 2, 2026: sale leak.** Check for any company statement or filing.

**Questions for management**

1. How much Q4 2025 revenue was booked under bill-and-hold, for which customers, and how many robots? Where is each unit now: delivered, still held, or returned?
2. Did each customer request its arrangement in writing, and when? On December 31, 2025, were the robots set aside, tagged to the customer and ready to ship?
3. Which customer returned the robots behind the US$9.4 million credit? Is it Norvale? When was the return first requested and agreed, compared with the May 12, 2026 response to Greyfin?
4. Why was the return booked as a Q2 2026 credit instead of a correction of 2025? Did the audit committee and Linden Barr review that choice?
5. What was the revenue threshold in the 2025 executive bonus plan, and what was paid? Would a restatement trigger a clawback?
6. Why was Hartwell & Pryce replaced in mid-November 2025? Did Linden Barr carry out the expanded Q4 procedures its predecessor planned?
7. Was there a disagreement between Daniel Okafor and Marcus Hale? What does the US$0.9 million separation payment cover? Does the agreement include cooperation or non-disparagement terms? Has Okafor raised concerns with the board, the auditor or regulators?
8. As corporate controller, what role did Rachel Simmons play in the Q4 2025 revenue decisions? What is the status of the search for a permanent CFO?
9. What exactly is the material weakness? What is the remediation plan, and when will it be complete?
10. What did the cyber forensic review find? Was any data taken, and was a ransom paid? How did the board decide the incident was "not material", and has that decision been revisited? What are the total costs, insurance recoveries, customer claims (including Pinecrest) and customer losses?
11. What share of revenue, receivables and backlog does Norvale represent? What are the contract's expiry, minimum volumes and change-of-control terms? What has Norvale said about orders in 2027 and later?
12. What drove the August 7 guidance cut beyond the US$11.7 million of Q2 credits? How is Q3 2026 trading, and what is the current backlog? Will management provide an updated plan for the deal model?
13. What is the current revenue split between hardware, FieldOS software and services? How much of the installed base is Gen-3 or newer?
14. What restructuring costs were excluded from Adjusted EBITDA in each year from 2022 to 2026? Why should they count as non-recurring?
15. Who is the LiDAR supplier, and what do the contract terms say about tariffs? How much sensor inventory is on hand, and how far along is qualifying a second supplier?
16. Are there any lawsuits, class actions, customer claims or regulatory inquiries linked to the short report, the guidance cut or the outage?
17. What drove the roughly 24% share price fall between the March 2026 high and the Greyfin report?
18. Which other parties are in the sale process, and has the October 2 leak been investigated?
