<!-- Iteration 1, news-media-analyst. Full report as returned by the analyst, saved unedited by the lead agent. -->

## News and media analyst: findings

### Files reviewed

All 13 files in `data/news/` were read in full, plus `data/deal-brief.md` for context.

1. `data/news/2025-11-18_capital-markets-wire_auditor-switch.md`
2. `data/news/2026-01-23_columbus-business-ledger_cfo-exit.md`
3. `data/news/2026-02-10_warehouse-tech-review_fieldos-5-launch.md`
4. `data/news/2026-03-10_capital-markets-wire_record-q4.md`
5. `data/news/2026-03-28_columbus-business-ledger_scholarship.md`
6. `data/news/2026-04-14_supply-chain-dispatch_fieldos-outage.md`
7. `data/news/2026-05-12_capital-markets-wire_short-seller-report.md`
8. `data/news/2026-06-24_roboeconomy-weekly_norvale-buys-kinetic-aisle.md`
9. `data/news/2026-07-30_columbus-business-ledger_layoffs.md`
10. `data/news/2026-08-07_capital-markets-wire_guidance-cut.md`
11. `data/news/2026-08-20_warehouse-tech-review_market-report.md`
12. `data/news/2026-09-15_supply-chain-dispatch_lidar-tariffs.md`
13. `data/news/2026-10-02_capital-markets-wire_sale-exploration.md`

**Prompt-injection check:** no file contains text that tries to instruct the agents. Nothing to report.

**Source reliability ratings**

| Outlet / party | Type | Reliability | Notes |
|---|---|---|---|
| Capital Markets Wire | Financial wire | Medium-High | Mostly reports filings, guidance and price moves. The Oct 2 sale story uses anonymous sources (rumor). The Mar 10 analyst quote is unnamed. |
| Columbus Business Ledger | Local business press | Medium | The CFO story rests on two anonymous sources (rumor). The layoff story cites a state notice (fact). |
| Warehouse Tech Review | Trade press | Medium | Reports company claims and a third-party market study (Calder Insights). |
| Supply Chain Dispatch | Trade press | Medium | Says it "could not verify" the ransomware claim. The tariff impact is one unnamed analyst's estimate. |
| RoboEconomy Weekly | Trade press | Medium | Quotes a Norvale executive on record. |
| Greyfin Research (via Capital Markets Wire) | Short seller, holds a disclosed short position | Low | Interested party. Its evidence is photos and three former employees. The core bill-and-hold point was later partly confirmed by the company (see NEWS-02). |

### Timeline

Dates marked (inferred) are worked out from weekday references in the article. They are not stated directly.

| Date | Event | Outlet | Fact / Allegation / Rumor |
|---|---|---|---|
| ~Nov 14, 2025 (inferred, "Friday" filing) | Auditor switched from Hartwell & Pryce (auditor since 2016) to Linden Barr LLP. The outgoing auditor had flagged a material weakness and planned expanded Q4 work. | Capital Markets Wire | Fact (filing) |
| ~Nov 17, 2025 | Shares down 2.1% | Capital Markets Wire | Fact |
| ~Jan 21, 2026 (inferred, "Wednesday" filing) | CFO Daniel Okafor resigns with a $900,000 separation payment. Controller Rachel Simmons becomes interim CFO. | Columbus Business Ledger | Fact (filing) |
| Jan 23, 2026 | Report that the CFO exit followed a clash with the CEO over booking Q4 hardware orders | Columbus Business Ledger | Rumor (two anonymous sources) |
| Feb 10, 2026 | FieldOS 5 launched. Harbor & Vine expands to 12 more distribution centers. CEO targets software at "more than a third of revenue". | Warehouse Tech Review | Fact (announcement) / company claim |
| Mar 10, 2026 | Q4 2025 revenue $154.4m (+32%), FY2025 $502.3m (+19%). FY2026 guidance $555-565m revenue, $114-122m Adj. EBITDA. Adverse internal-control opinion. Shares +9% to $31.20. | Capital Markets Wire | Fact |
| Mar 10, 2026 | Analyst says receivables jumped and FY operating cash flow was under $10m | Capital Markets Wire | Fact-like, but from an unnamed analyst |
| Mar 28, 2026 | $1.5m scholarship program. About 1,450 employees. | Columbus Business Ledger | Fact (noise) |
| ~Apr 11-14, 2026 | FieldOS outage. Robots stopped at 40+ sites for up to 3 days. Ransomware group claims it took data. No Item 1.05 Form 8-K. | Supply Chain Dispatch | Fact (outage, no 8-K) / Rumor (data theft claim) |
| May 12, 2026 | Greyfin short report on bill-and-hold sales. Shares -18% to $19.85. Company calls it "misleading and inaccurate". | Capital Markets Wire | Allegation |
| Jun 24, 2026 | Norvale (Talonfield's largest customer) buys robot startup Kinetic Aisle. Shares -6%. | RoboEconomy Weekly | Fact |
| Jul 30, 2026 | About 60 jobs cut (4%). Fourth restructuring since 2022. | Columbus Business Ledger | Fact (state notice) |
| Aug 7, 2026 | Guidance cut to $470-490m revenue and $70-78m Adj. EBITDA. Q2 revenue $112.9m (-4%), including a $9.4m bill-and-hold return credit and $2.3m of outage credits. Shares -14% to $16.40. | Capital Markets Wire | Fact |
| Aug 20, 2026 | Calder Insights: North American warehouse AMR market growing ~15% a year to 2030. Talonfield is #3 with ~11% share. | Warehouse Tech Review | Fact (third-party report) |
| Sep 15, 2026 | Proposed LiDAR tariff rise from 7.5% to 25%. Talonfield buys from a single supplier in China. Decision expected Q1 2027. | Supply Chain Dispatch | Fact (proposal) / Analyst estimate (margin impact) |
| Oct 2, 2026 | Talonfield reported to be exploring a sale, with Arbelion named as a bidder. Shares +12% to $17.20. | Capital Markets Wire | Rumor (people familiar) |

### Findings

#### NEWS-01: FY2026 guidance cut far below the deal model's investor-day case
- **Finding:** On Aug 7, 2026 Talonfield cut FY2026 guidance to $470-490m revenue and $70-78m Adj. EBITDA. The deal model still uses $560.0m and $118.0m. At the midpoints, revenue is $80.0m (14.3%) below the model and Adj. EBITDA is $44.0m (37.3%) below it.
- **Evidence:** "cut its 2026 revenue outlook to $470 million to $490 million, from $555 million to $565 million, and its Adjusted EBITDA outlook to $70 million to $78 million"; "2026 is a reset year" (interim CFO Rachel Simmons).
- **Source:** `data/news/2026-08-07_capital-markets-wire_guidance-cut.md` (Capital Markets Wire, Aug 7, 2026), para 1 and 3. Original guidance: `data/news/2026-03-10_capital-markets-wire_record-q4.md`, para 2.
- **Claim type:** Fact (on-record company guidance)
- **Severity:** Critical. Test met: change in value by more than 10%. (inference) The deal brief implies EV of about $1,357.0m (11.5x × $118.0m). Applying the same 11.5x to the new $74.0m midpoint gives about $851.0m, a 37.3% drop. Put another way, the deal EV is about 18.3x guided EBITDA. Midpoint revenue of $480.0m would also be a 4.4% decline on FY2025's $502.3m, where the investor-day case had 11.5% growth.
- **Confidence:** High. This is the company's own on-record guidance as reported by a wire. Confirm against the 8-K or 10-Q.
- **Deal impact:** Valuation. The model base case is stale.
- **Cross-check:** Q2 2026 earnings 8-K and 10-Q for the guidance ranges and Q2 revenue. The financial data should show H1 2026 run-rate, the $9.4m and $2.3m credits, and whether $70-78m includes the restructuring add-backs (see NEWS-08).

#### NEWS-02: Bill-and-hold revenue in Q4 2025: short seller allegation now partly confirmed by the company
- **Finding:** Greyfin alleged that bill-and-hold sales were used to hit 2025 targets. The company denied it. In Q2 2026 the company itself recorded a $9.4m credit after a customer returned robots "sold under a bill-and-hold arrangement in late 2025". Two other parts of the allegation remain unconfirmed: that "hundreds" of robots were still in the warehouse, and that the bill-and-hold sales were needed to hit the bonus target.
- **Evidence:** Greyfin: "'Hundreds' of robots booked as fourth-quarter sales were still sitting in Talonfield's Columbus warehouse in February 2026". Company: "misleading and inaccurate" and "complies with GAAP and was reviewed by our independent auditor". Later: "$9.4 million credit after a customer returned robots that had been sold under a bill-and-hold arrangement in late 2025".
- **Source:** `data/news/2026-05-12_capital-markets-wire_short-seller-report.md` (Capital Markets Wire, May 12, 2026), bullets 1-3 and para 3. `data/news/2026-08-07_capital-markets-wire_guidance-cut.md`, para 2. Context: Q4 revenue of $154.4m was about $26.4m above the ~$128m consensus (`2026-03-10_...record-q4.md`, para 1).
- **Claim type:** Allegation (Greyfin's scale, customer and bonus claims). Fact (that a bill-and-hold arrangement existed and that $9.4m was reversed).
- **Severity:** High. This is a revenue quality and restatement risk that may need a special indemnity or escrow. The total amount of bill-and-hold revenue is not found in news coverage, so the more-than-10% test cannot be shown.
- **Confidence:** Medium. The existence of bill-and-hold sales is confirmed by the company. The scale comes from an interested short seller (Low on its own).
- **Deal impact:** Valuation (FY2025 base revenue may be overstated), post-closing (restatement, SEC inquiry, securities suits), reputation.
- **Cross-check:** 10-K FY2025 revenue recognition policy and any bill-and-hold disclosure, plus Q4 2025 revenue by customer. Financial data should show Q4 receivables, DSO, inventory or finished goods held, and the customer behind the $9.4m return. Litigation records should show any securities class action filed after May 12 or Aug 7. Check whether the "largest customer" in Greyfin's claim is Norvale.

#### NEWS-03: Auditor switch weeks before year-end, after a material weakness and planned expanded Q4 procedures
- **Finding:** In November 2025 Talonfield replaced its long-time auditor with a small regional firm. The outgoing auditor had flagged a material weakness in hardware contract controls and said it would expand work on Q4 deals with "unusual delivery terms". The new auditor later issued an adverse opinion on internal controls.
- **Evidence:** "outgoing auditor had flagged a 'material weakness' in controls over certain hardware contracts"; "its new auditor had issued an adverse opinion on internal controls". The company said the switch followed "a routine review to find the best fit for a growing company".
- **Source:** `data/news/2025-11-18_capital-markets-wire_auditor-switch.md` (Capital Markets Wire, Nov 18, 2025), para 1, 2 and 4. `data/news/2026-03-10_capital-markets-wire_record-q4.md`, para 5.
- **Claim type:** Fact (from the filing). The "why" behind the change is commentary by an academic quoted on record.
- **Severity:** High. A governance and internal-control concern that bears directly on the reliability of FY2025 revenue (NEWS-02). Needs specific reps and diligence protections.
- **Confidence:** High for the switch, the weakness and the adverse opinion (filing-based). Low for any inference about motive.
- **Deal impact:** Valuation (quality of earnings), post-closing (remediation cost), reputation.
- **Cross-check:** The 8-K Item 4.01 and the outgoing auditor's Exhibit 16 letter. The FY2025 10-K Item 9A for the material weakness description and remediation status. Q1 and Q2 2026 10-Qs for whether the weakness persists. Audit fee data.

#### NEWS-04: CFO resignation with $900,000 payout. Anonymous sources link it to a dispute over Q4 revenue timing
- **Finding:** CFO Daniel Okafor resigned in January 2026 with a $900,000 separation payment. The company filing says there was no disagreement. Two anonymous sources say he argued that some Q4 hardware revenue should be deferred to 2026. The CFO role was still interim as of Aug 7, 2026.
- **Evidence:** "Okafor had argued that revenue on some orders should not be recognized until the robots were delivered to customer sites in 2026". Company: departure "was not the result of any disagreement with the Company".
- **Source:** `data/news/2026-01-23_columbus-business-ledger_cfo-exit.md` (Columbus Business Ledger, Jan 23, 2026), para 1-4. Interim status: `data/news/2026-08-07_capital-markets-wire_guidance-cut.md`, para 3.
- **Claim type:** Fact (resignation, payout, interim CFO). Rumor (the reason for the exit).
- **Severity:** High. Taken with NEWS-02 and NEWS-03, this is a management and internal-control concern tied to the same Q4 2025 transactions.
- **Confidence:** Low for the dispute (anonymous, not confirmed). High for the payout and the interim appointment (filing-based).
- **Deal impact:** Post-closing (finance leadership gap), valuation (revenue quality), reputation.
- **Cross-check:** The 8-K Item 5.02 and the separation agreement exhibit (check for non-disparagement or cooperation clauses). The proxy statement for bonus plan revenue targets, which would test Greyfin's bonus claim. Court records for any whistleblower or employment claim by Okafor.

#### NEWS-05: FieldOS cyber incident: 3-day outage at 40+ sites, ransomware data-theft claim, no Item 1.05 8-K
- **Finding:** Parts of FieldOS were taken offline after "unauthorized activity", which stopped robots at 40 or more customer sites for up to three days. A ransomware group claimed it took customer data. The company denied any data was taken, called the incident not material, and filed no Item 1.05 8-K. It later gave customers $2.3m of credits. Customer Pinecrest said it is "reviewing our options".
- **Evidence:** "had not filed a Form 8-K under Item 1.05"; "determined that the incident is not material"; "We are reviewing our options" (Pinecrest COO).
- **Source:** `data/news/2026-04-14_supply-chain-dispatch_fieldos-outage.md` (Supply Chain Dispatch, Apr 14, 2026), para 1-5. Credits: `data/news/2026-08-07_capital-markets-wire_guidance-cut.md`, para 2.
- **Claim type:** Fact (outage, no 8-K, $2.3m credits). Rumor (the ransomware group's data-theft claim, which the outlet could not verify).
- **Severity:** High. Possible disclosure gap, customer claims and data exposure. Needs a specific indemnity and cyber reps.
- **Confidence:** Medium. The outage and customer quote are on record, and the credits were confirmed by the company in August. The data theft is unverified.
- **Deal impact:** Post-closing (customer claims, SEC disclosure scrutiny, remediation), reputation, customer retention.
- **Cross-check:** 8-K filings around April 2026 and the 10-Q risk factors and cybersecurity disclosure (Item 1C in the 10-K). Litigation records for any suit by Pinecrest or other customers, or a data-breach class action. Financial data for Pinecrest's revenue rank and amount, and where the $2.3m credits were booked.

#### NEWS-06: Largest customer Norvale is building its own robots
- **Finding:** Norvale Retail Group, named as Talonfield's largest customer, bought robot startup Kinetic Aisle to "reduce our dependence on any single vendor". It plans pilots at five distribution centers in 2027 and has made no firm commitment to keep buying Talonfield robots.
- **Evidence:** "We want to own more of our automation stack and reduce our dependence on any single vendor"; "continue to work with existing partners while we evaluate the right long-term mix".
- **Source:** `data/news/2026-06-24_roboeconomy-weekly_norvale-buys-kinetic-aisle.md` (RoboEconomy Weekly, Jun 24, 2026), para 1-4. Industry trend: `data/news/2026-08-20_warehouse-tech-review_market-report.md`, para 2.
- **Claim type:** Fact (acquisition, on-record executive statement)
- **Severity:** High. Norvale's revenue share is not found in news coverage, so the more-than-10% test cannot be shown from news alone. The financial analyst should check.
- **Confidence:** High for the event and the quote. Medium for the impact on Talonfield revenue.
- **Deal impact:** Valuation (revenue durability), post-closing.
- **Cross-check:** `revenue_by_customer` data for Norvale's rank, amount and share. The 10-K concentration disclosure and customer contract terms (term, minimums, change of control). Whether Norvale is the "largest customer" in Greyfin's bill-and-hold claim and the source of the $9.4m return (inference: possible link, not confirmed).

#### NEWS-07: Cash conversion weak in the record quarter
- **Finding:** An unnamed analyst noted that receivables jumped in Q4 2025 and that FY2025 operating cash flow was under $10m on $502.3m of revenue. This is consistent with the revenue-timing concerns in NEWS-02.
- **Evidence:** "Receivables jumped and operating cash flow fell to under $10 million for the year".
- **Source:** `data/news/2026-03-10_capital-markets-wire_record-q4.md` (Capital Markets Wire, Mar 10, 2026), para 4.
- **Claim type:** Fact-like claim from an unnamed analyst
- **Severity:** Medium
- **Confidence:** Medium. A single secondary source, and the analyst is not named.
- **Deal impact:** Valuation (quality of earnings), liquidity.
- **Cross-check:** FY2025 cash flow statement, receivables aging, and DSO trend by quarter in the financial data.

#### NEWS-08: Recurring restructuring excluded from Adjusted EBITDA
- **Finding:** The July 2026 cut of about 60 jobs (4%) is the fourth restructuring since 2022. Each year the costs were excluded from Adjusted EBITDA as "not part of ongoing operations". Recurring add-backs may overstate the EBITDA base for the multiple.
- **Evidence:** "It is the company's fourth restructuring program since 2022. Each year the company has excluded restructuring costs from its Adjusted EBITDA".
- **Source:** `data/news/2026-07-30_columbus-business-ledger_layoffs.md` (Columbus Business Ledger, Jul 30, 2026), para 1-3.
- **Claim type:** Fact (state notice and reporter's description)
- **Severity:** Medium
- **Confidence:** Medium. A single local outlet, though it is based on a state filing. The add-back amounts are not found in news coverage.
- **Deal impact:** Valuation (EBITDA quality), integration (headcount).
- **Cross-check:** The Adjusted EBITDA reconciliation in the 10-K and 10-Qs for FY2022 to FY2026. WARN notice details. Headcount of about 1,450 (`2026-03-28_...scholarship.md`), which is consistent with 60 being about 4%.

#### NEWS-09: LiDAR tariff and single-source China supplier
- **Finding:** A proposal would raise tariffs on Chinese LiDAR modules from 7.5% to 25%, with a decision expected in Q1 2027. Talonfield reportedly buys all its LiDAR from one Chinese supplier. One analyst estimates a 2 to 3 point hit to hardware gross margin, and qualifying a new supplier takes 12 to 18 months.
- **Evidence:** "buys all of its LiDAR sensors from a single supplier in China"; "Qualifying a new sensor supplier takes 12 to 18 months".
- **Source:** `data/news/2026-09-15_supply-chain-dispatch_lidar-tariffs.md` (Supply Chain Dispatch, Sep 15, 2026), para 1-3.
- **Claim type:** Fact (the proposal). Analyst estimate (the margin impact). The single-supplier claim is not attributed.
- **Severity:** Medium
- **Confidence:** Medium. Single trade-press source with one unnamed analyst estimate.
- **Deal impact:** Post-closing (margin, supply continuity), valuation (hardware margin).
- **Cross-check:** 10-K risk factors on supplier concentration and tariffs. Hardware gross margin by segment and the bill of materials in the financial data.

#### NEWS-10: Market growth versus Talonfield's performance
- **Finding:** Calder Insights forecasts about 15% annual growth in North American warehouse AMR spending through 2030. It ranks Talonfield third with about 11% share and warns of in-house development by large retailers. Talonfield's own 2026 guidance implies a revenue decline of 2.4% to 6.4% (inference, from $470-490m against $502.3m), so it is losing ground in a growing market.
- **Evidence:** "grow about 15% a year through 2030"; FieldOS "remains a differentiator"; "large retailers are increasingly developing robots in-house".
- **Source:** `data/news/2026-08-20_warehouse-tech-review_market-report.md` (Warehouse Tech Review, Aug 20, 2026), para 1-2.
- **Claim type:** Fact (third-party forecast as reported)
- **Severity:** Medium
- **Confidence:** Medium. One industry report, reported by trade press.
- **Deal impact:** Valuation (growth assumptions, share loss).
- **Cross-check:** Market data cited in the 10-K business section. Segment revenue trends in the financial data. Competitor Vantor Robotics is named; check whether it appears in any litigation.

#### NEWS-11: Sale leak inflated the reference price for the 34% premium
- **Finding:** Anonymous sources reported a sale process on Oct 2, 2026, naming Arbelion and two PE firms, and shares rose 12% to $17.20. The deal brief's 34% premium is measured against the Oct 16 price of $17.85, which already includes the leak bump. (inference) The pre-leak price was about $15.36 ($17.20 / 1.12), which makes the $24.00 offer about a 56% premium to the undisturbed price.
- **Evidence:** "has hired advisers to explore a sale ... according to people familiar with the matter"; "shares rose 12% to $17.20".
- **Source:** `data/news/2026-10-02_capital-markets-wire_sale-exploration.md` (Capital Markets Wire, Oct 2, 2026), para 1-2. `data/deal-brief.md`, "The deal".
- **Claim type:** Rumor (the sale process). Fact (the price move).
- **Severity:** Medium
- **Confidence:** Medium. The price data is factual. The sale process is anonymous, but consistent with the deal itself.
- **Deal impact:** Valuation (premium framing), process (other bidders, price tension), reputation (leak).
- **Cross-check:** Market price data. Any 13D, 13G or proxy disclosure of the process. Board minutes or a background-of-the-merger section once drafted.

#### NEWS-12: FieldOS 5 features require Gen-3 or newer robots; software mix target
- **Finding:** FieldOS 5's AI features need Talon Gen-3 or newer robots. That may limit upsell to the installed base or force hardware upgrades. The CEO's target of software at "more than a third of revenue" within three years is an unverified management aspiration.
- **Evidence:** "the new features require Talon Gen-3 robots or newer"; software would grow to "more than a third of revenue".
- **Source:** `data/news/2026-02-10_warehouse-tech-review_fieldos-5-launch.md` (Warehouse Tech Review, Feb 10, 2026), para 3-4.
- **Claim type:** Fact (launch). Company claim (productivity and mix targets).
- **Severity:** Low
- **Confidence:** Medium. Trade press relaying company statements and analyst comments.
- **Deal impact:** Valuation (software growth assumptions).
- **Cross-check:** Revenue by segment and installed base by robot generation in the financial data. Harbor & Vine's rank in the customer revenue data.

**Share price reaction summary:** 52-week high $31.75 (March 2026), then -18% on the short report (to $19.85), -6% on Norvale, -14% on the guidance cut (to $16.40), and +12% on the sale leak (to $17.20). The price fell about 46% from the March close of $31.20 to $16.40 by Aug 7 (computed).

### Positive or mitigating points

- Talonfield is #3 in North America with about 11% share in a market forecast to grow about 15% a year, and Calder calls FieldOS "a differentiator" (`2026-08-20_...market-report.md`).
- FieldOS 5 was launched with positive customer feedback, and Harbor & Vine expanded to 12 more distribution centers (`2026-02-10_...fieldos-5-launch.md`).
- The company says systems were restored and found no evidence of data theft (`2026-04-14_...fieldos-outage.md`). The outage credits were limited to $2.3m.
- Norvale said it would "continue to work with existing partners" (`2026-06-24_...norvale...md`). Its pilots do not start until 2027.
- The tariff is only a proposal. A decision is expected in Q1 2027 (`2026-09-15_...lidar-tariffs.md`).
- The lower share price and the reset guidance give Arbelion leverage on price before exclusivity expires on Nov 20, 2026.

### Articles reviewed with no diligence relevance

- `data/news/2026-03-28_columbus-business-ledger_scholarship.md`: a $1.5m five-year scholarship program. This is noise. The one useful data point is headcount of about 1,450, which supports the 4% layoff figure, and COO Priya Raman is named.

### Gaps and questions for management

1. How much FY2025 revenue (Q4 in particular) came from bill-and-hold arrangements, with which customers, and how much is still undelivered? Which customer returned robots for the $9.4m credit? Is it Norvale?
2. Why was Hartwell & Pryce replaced in November 2025? Provide the auditor's Exhibit 16 letter and the material weakness remediation status.
3. Provide Okafor's separation agreement and explain why a voluntary resignation came with $900,000. When will a permanent CFO be appointed?
4. Provide the materiality analysis behind not filing an Item 1.05 8-K for the April incident, plus forensic findings on the ransomware data claim and any customer claims (Pinecrest).
5. What is Norvale's share of revenue? Provide contract terms and any change in order flow since June 2026.
6. How do the $70-78m Adj. EBITDA guidance and the investor-day case treat restructuring add-backs? Provide the add-back history for 2022 to 2026.
7. What is the LiDAR supplier qualification plan, and what tariff cost has been modeled?
8. Is the bonus plan revenue target for FY2025 disclosed, and was it met only because of the bill-and-hold sales (Greyfin's claim)?
9. Not found in news coverage: covenant or debt terms, litigation filings, Norvale's revenue amount, and any SEC inquiry. These need the other workstreams.

Source folder: `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/data/news/`