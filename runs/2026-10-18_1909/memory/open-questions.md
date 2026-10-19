# Open questions, conflicts and gaps

Status: Updated after iteration 1 (2026-10-18).

## Conflicts between sources

1. **Vantor case status:** 10-Q (Aug 6, 2026) says "in discovery" and "without merit"; the court docket shows a Markman order largely for Vantor on Jul 22, 2026 (before the 10-Q). See X-04.
2. **Cyber incident materiality:** company says "not material" and no customer data taken; news reports at least 40 sites down and an unverified ransomware data-theft claim; Pinecrest sues for $12.0m alleging gross negligence. See X-05.
3. **Bill-and-hold:** company says GAAP-compliant and auditor-reviewed; short seller (ALLEGATION) and class action (ALLEGATION) say the customer did not request it and revenue was inflated; the old auditor had warned about these deals before it was dismissed. See X-02.
4. **CFO departure:** 8-K says "not the result of any disagreement"; news (RUMOR, 2 anonymous sources) says a dispute over revenue timing; $900,000 payment with release is unusual for a voluntary exit.
5. **Covenant ratio:** company reports 2.26x, which matches full Adjusted EBITDA; the credit agreement caps add-backs at 15%. See X-07.
6. **Term loan balance:** SEC analyst could not find the Jun 30, 2026 term loan balance in filings and assumed 185.0; `balance_sheet.csv` shows 182.5. Use 182.5 (net debt 193.6).
8. **Covenant net debt (iteration 2):** the SEC analyst's SEC-032 estimate assumes net debt of 205.0 (term loan assumed 185.0); the financial analyst uses 202.5 from `balance_sheet.csv`. Use 202.5 (FIN-015).
9. **Class period anchor:** the complaint's start date (Mar 10, 2025) matches no filing in the data; Q4 2025 results were released Mar 10, 2026 (X-19).
7. **Premium basis:** brief's 34% premium uses $17.85, after the Oct 2 leak run-up (RUMOR). See X-11.

## Gaps and follow-ups for the next iteration

- Iteration 2 (financial): recompute the Total Net Leverage Ratio on the contractual definition (15% add-back cap; both readings of whether SBC is inside the cap) at Jun 30, 2026 and projected at Sep 30 and Dec 31, 2026 on guidance. Check Consolidated EBITDA vs reported EBITDA (net income + interest + tax + D&A).
- Iteration 2 (financial): CoC payments and Norvale exposure in valuation terms; FY2025 hardware growth ex bill-and-hold.
- Iteration 2 (SEC): confirm the 10-Q's exact Vantor wording and whether any filing mentions the Markman order; whether any filing gives a reason the bill-and-hold was requested; anything on Q3 2025 results needed for the Sep 30 test.
- Iteration 2 (litigation): exact Markman entry wording, willfulness and enhanced damages basis, Pinecrest's patch allegation, securities class period and whether the complaint cites the auditor dismissal, CFO exit or bonus.
- Not in the data: Q3 2026 results (10-Q due early Nov), backlog/RPO in filings, the full credit agreement, D&O insurance, Norvale contract text.

## Questions for management

1. Bill-and-hold: customers, substantive reason, who requested it, collection of the $22.4m delivered, any 2026 bill-and-hold, restatement assessment.
2. Why was Hartwell & Pryce dismissed? Audit Committee minutes; auditor communications.
3. CFO: reason for exit, separation agreement, permanent CFO search.
4. Norvale: 2026 volumes, willingness to waive the CoC termination right, MSA renewal, Kinetic Aisle pilot scope.
5. Credit agreement: full text, compliance certificates, covenant calculation detail, add-back mix vs 15% cap, Q3 2026 test result, prepayment terms.
6. Vantor: ASC 450 assessment after Jul 22 Markman order; design-around; settlement posture for December mediation; customer indemnity exposure.
7. Securities suit: D&O tower and retention; indemnification of Okafor.
8. Cyber: forensic report; data exfiltration; 8-K Item 1.05 materiality analysis; other customer claims; insurance.
9. Bridge from March to August guidance; Q3 2026 actuals; latest outlook.
10. Restructuring programs and why they recur; nature of "customer implementation delays" add-back.
11. Receivables aging, allowance method, inventory composition and reserves, FieldOS billing terms.
12. Goodwill interim impairment test.
13. Clawback policy; CoC payment values at $24.00; HQ lease rent reset waiver.
14. LiDAR second source and tariff plan.
