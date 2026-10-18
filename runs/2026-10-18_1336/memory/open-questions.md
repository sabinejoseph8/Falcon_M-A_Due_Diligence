# Open questions, conflicts and gaps

Status: Updated after iteration 2 (2026-10-18).

## Conflicts between sources

1. **Term loan balance.** SEC analyst assumed $185.0 (10-K balance; the 10-Q does not state it). `balance_sheet.csv` shows $182.5 at June 30, 2026. Resolution: use $182.5 (company financials). Net debt $193.6; EV $1,352.8.
2. **Company says vs filings and records:**
   - Q4 2025 described as "strong hardware deliveries" (10-K) vs $31.8 undelivered bill-and-hold (10-K Note 2) and "pulled forward" (10-Q). (SEC-03)
   - Company: short seller report "misleading and inaccurate", revenue "complies with GAAP" (news) vs $9.4 of bill-and-hold later returned and credited (10-Q). (NEWS-03, SEC-02)
   - Company: auditor change was "a routine review" (news) vs 8-K reportable event on a material weakness and planned wider Q4 procedures. (NEWS-04, SEC-04)
   - CFO exit "not the result of any disagreement" (8-K) vs rumor of a clash over Q4 revenue timing (two anonymous sources). Rumor only. (SEC-06, NEWS-05)
   - April incident "not material" (10-Q) vs 40+ sites down up to 3 days, $2.3 credits, $12.0 lawsuit. (SEC-11, NEWS-07, LIT-07)
3. **Vantor case.** 10-Q (Aug 6, 2026): "in discovery", no accrual. Court record: Markman order adverse on 3 of 4 terms on July 22, 2026, before the 10-Q. Confirmed in iteration 2 (SEC-18): the 10-Q omits the ruling, any damages figure, the injunction and any loss range. (X-06)
5. **Covenant compliance.** 10-Q reports 2.26x. Recomputing with the 10-K's 15% cap on Permitted Add-backs gives about 2.6x to 2.7x. The reported figure matches uncapped Adj. EBITDA. Unresolved without the full credit agreement. (X-09, FIN-19, SEC-22)
6. **Cyber scope.** News: 40+ customer sites down. 10-Q: "some customers". (X-07, SEC-21, NEWS-07)
7. **Norvale.** News (June 24, 2026): Norvale building in-house capability via Kinetic Aisle. 10-Q (Aug 6, 2026): no mention. (X-05, SEC-20)
4. **Deal brief vs filings.** Deal brief (Oct 17, 2026) values on the March 2026 case; company cut guidance Aug 6, 2026. (X-02)

## Gaps and follow-ups for the next iteration

Iteration 2 was run (SEC and financial analysts). Answered: Vantor 10-Q wording, Norvale amendment text, cyber disclosure text, covenant definitions, underlying growth and EBITDA, covenant headroom. Not answerable from the data (need management or the data room): the reason for the Norvale amendment, the full credit agreement, Q3 2026 actuals and the Sept 30 covenant certificate, quarterly unit shipments, segment gross margins, Lumora contribution, the full audit report. No iteration 3 planned.

Original iteration 2 task list:
- SEC analyst: exact 10-Q wording on Vantor and whether it mentions the July 22 Markman order or any damages figure; 10-K wording on the Vantor claim amount; 10-K Item 1C and 10-Q on cyber disclosure; the "Bill-and-hold amendment" terms with Norvale; whether the 10-Q mentions Norvale's Kinetic Aisle acquisition (June 24); the exact covenant definitions (Consolidated EBITDA, 15% add-back cap, $25.0 cash netting); whether robots shipped and backlog definitions are given; Linden Barr's opinion on the financial statements; Lumora contribution if disclosed.
- Financial analyst: recompute quarterly and half-year growth with the $31.8 bill-and-hold and the $9.4 reversal; covenant headroom at Sept 30 and Dec 31, 2026 using the covenant definitions; whether 2025 robots shipped appear to include undelivered bill-and-hold units; normalized FY2026 run-rate EBITDA.

## Questions for management

Revenue and accounting
1. For each Q4 2025 bill-and-hold contract: customer, amount, the customer's written request and substantive reason, and how each ASC 606 criterion was met. Who holds the non-Norvale $7.2?
2. Why did Norvale return $9.4 in May 2026? What are the amendment terms? Are more returns expected?
3. Were bill-and-hold units counted in 2025 robots shipped and installed base?
4. Why was Hartwell & Pryce dismissed? Audit Committee minutes and the expanded Q4 scope it proposed.
5. Material weakness remediation plan, timeline and testing.
6. Any SEC inquiry, subpoena, internal investigation or whistleblower complaint?
7. Support for each Adj. EBITDA add-back; why restructuring recurs every year; what "customer implementation delays" are.
8. Lumora Vision revenue and EBITDA contribution; organic growth.

Forecast and valuation
9. Current FY2026 forecast and bridge from the March case to the August guidance; Q3 2026 actuals.
10. Basis for the $35.0 synergy target given the restructuring already underway.
11. Interim goodwill impairment assessment after the guidance cut.

Customers
12. Norvale's 2026 revenue, AR aging and stance on a change of control; its plans for Kinetic Aisle; renewal plans for the MSA ending Sept 30, 2027.
13. Other customers affected by the April 2026 outage; claims, credits, churn.

Debt and liquidity
14. Q3 2026 covenant certificate, Consolidated EBITDA build against the 15% add-back cap, payoff amounts and lender consent position.
15. Lease liabilities and other debt-like items; diluted share count at $24.00.

Legal
16. Vantor: Talonfield's damages estimate, design-around feasibility and cost, settlement authority, insurance, willfulness evidence; status of the '094 patent.
17. Pinecrest contract cap wording and any gross negligence carve-out; outcome of the Nov 5, 2026 hearing.
18. D&O insurance limits for the securities class action.
19. Full litigation and claims schedule, including threatened claims.

Cyber
20. Forensic report on the April incident; whether data was taken; whether a ransom was paid; the basis for the "not material" decision; cyber insurance.

Governance and people
21. Okafor separation agreement terms and whether he raised concerns with the Audit Committee; permanent CFO search.
22. Hale lease rent reset mechanics and market rent; whether independent directors oversee the sale process.
23. Clawback policy for 2025 bonuses paid at 142%.
24. Retention plan for key staff given single-trigger vesting.

Supply chain
25. LiDAR dual-sourcing plan, LiDAR share of hardware cost, tariff impact estimate.

Added after iteration 2
26. Q3 2026 actuals and the Sept 30, 2026 covenant compliance certificate (the quarter has ended).
27. Full credit agreement: is SBC inside the 15% Permitted Add-back cap? Basis of the cap? Show the 2.26x calculation.
28. Quarterly robot shipments with bill-and-hold units shown separately; KPI definitions (robots shipped, installed base, backlog, ARR, NRR); why ARR and NRR were dropped from the 10-Q.
29. Full FY2025 audit report (financial statement opinion, critical audit matters) and the Exhibit 16.1 letter.
30. ASC 450 assessment of Vantor after the July 22 Markman order; why the 10-Q did not mention it.
31. Valuation reserve on the $9.4 of returned robots now in inventory.
