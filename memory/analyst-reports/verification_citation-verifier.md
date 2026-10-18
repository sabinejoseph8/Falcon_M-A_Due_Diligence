# Citation verifier results (Step 4, 2026-10-18)

Four parallel runs. Each run read the cited files in `data/`, recomputed every number, and found no text in any source trying to instruct the agents. Verdict tables below are recorded as returned (verdict, key check, correction). Run C's header said "15 checked"; its table has 16 rows, so the table count is used.

## Statistics

| Run | Scope | Checked | Verified | Partially verified | Rejected |
|---|---|---|---|---|---|
| A | Cross-source X- | 12 | 8 | 4 | 0 |
| B | SEC filings | 17 | 13 | 4 | 0 |
| C | News and litigation | 16 | 13 | 3 | 0 |
| D | Financial | 19 | 15 | 4 | 0 |
| Total | | 64 | 49 | 15 | 0 |

All 53 Critical and High findings were checked, plus 11 Medium findings (X-09, X-10, X-11, SEC-10, SEC-12, SEC-21, NEWS-08, LIT-F08, FIN-09, FIN-10, FIN-11).

## Run A: cross-source

| ID | Verdict | Correction / note |
|---|---|---|
| X-01 | Verified | Label $13.61 as illustrative at a constant 11.5x. |
| X-02 | Verified | Add: $22.4m of the $31.8m was delivered by June 30, 2026 and the 10-Q says orders were "pulled forward"; the adjustment is mainly timing, not proof of fictitious revenue. |
| X-03 | Partially verified | CFO gave notice January 20, 2026, effective February 15, 2026 (8-K dated January 21). Add the company's "no disagreement" statements for the auditor and CFO. Revenue ex bill-and-hold still meets the threshold by $0.5m. Intent not established. |
| X-04 | Verified | Add Norvale's hedge: it will "continue to work with existing partners while we evaluate the right long-term mix". |
| X-05 | Verified | Say "the 10-Q excerpt available". "In discovery" is literally accurate; the issue is the omission. $96.4m is Vantor's expert figure; "central to Gen-3" is commentators' view. |
| X-06 | Partially verified | Inventory +17.8% includes $9.4m of returned bill-and-hold units (+4.6% without them). Calder 15% is a forecast through 2030. Software (+14.6%) and services (+14.4%) still grew in H1 2026. |
| X-07 | Partially verified | December 31, 2026 range under the SBC-in-base reading is about 3.1x to 3.6x with flat net debt and add-backs at the H1 run rate (3.74x was the debt-trend case). EBITDA base per Note 9 may be 48.6 (excluding other income), giving 2.65x and 3.62x; conclusions unchanged. A breach is possible, not established; the full credit agreement must confirm. |
| X-08 | Verified | Label $72.6m as a diligence view, not a QoE result. |
| X-09 | Verified | Pinecrest sues for breach of contract and negligence; it argues gross negligence to avoid the cap. |
| X-10 | Verified | Sale-process report is a rumor; the 12% price move is fact. |
| X-11 | Verified | No customer-level revenue mix; the cap may apply only to the specific SLA contract. |
| X-12 | Partially verified | The $28.6m is not all cash due at closing: $17.6m single-trigger equity acceleration is settled through merger consideration and may be in the 48.3m diluted shares; $9.6m severance is double-trigger. Cash needs at or near closing about $234.9m gross (debt 227.5, LCs 4.2 to replace or collateralize, Ruiz 3.2), about $201.0m net of $33.9m cash, plus up to $11.0m contingent severance and benefits, plus Vantor $96.4m to $140.0m+ (plaintiff figures). |

## Run B: SEC filings

| ID | Verdict | Correction / note |
|---|---|---|
| SEC-01 | Verified | |
| SEC-02 | Verified | The $9.4m return was also with "our largest customer". |
| SEC-03 | Verified | "Advised the Audit Committee of"; Exhibit 16.1 letter agrees with the disclosure. |
| SEC-04 | Verified | |
| SEC-05 | Verified | |
| SEC-06 | Verified | |
| SEC-07 | Verified | $211.0m Gen-3 revenue is an estimate from "approximately 70%". |
| SEC-09 | Verified | Allowance back at 3.2% at June 30, 2026, which supports the view that the 2025 release was premature. |
| SEC-15 | Verified | Note 9 is "summarized from the credit agreement". |
| SEC-16 | Partially verified | Cite the $182.5m term loan to balance_sheet.csv. Corrected: "Using the $182.5m term loan from balance_sheet.csv, the reported 2.26x matches (182.5 + 45.0 - 25.0) / 89.7, which implies the company applied no add-back cap; under the definition as summarized in 10-K Note 9, the ratio would be 2.67x if SBC sits in the base and other add-backs are capped, and 3.65x if all add-backs are capped." Consider Critical if the strict reading holds. |
| SEC-17 | Partially verified | "Assuming net debt stays at $202.5m, the 3.00x test from September 30, 2026 requires covenant EBITDA of at least $67.5m, about 11% below the $75.9m implied under the SBC-in-base reading; under the all-capped reading the company would already fail the test." |
| SEC-20 | Verified | Confirmed for the 10-Q excerpt; check against the full filing. |
| SEC-22 | Verified | "Largest customer = Norvale" in May 2026 is an inference. |
| SEC-23 | Partially verified | "The 8-K discloses, as a reportable event, that the outgoing auditor had said Q4 2025 non-standard hardware arrangements would require additional procedures expanding its audit scope (the 8-K gives no reason for the dismissal and reports no disagreements); the auditor's report is not in the excerpts, so whether a critical audit matter was reported cannot be determined; the weakness was unremediated at June 30, 2026." |
| SEC-10 | Verified | $28.6m assumes a qualifying termination for the cash part; $17.6m equity is payable on the change in control alone. |
| SEC-12 | Partially verified | Landlord is Hale Family Properties LLC, "an entity controlled by Mr. Hale and members of his family": a personal conflict for the selling CEO. |
| SEC-21 | Verified | Excerpt caveat. |

## Run C: news and litigation

| ID | Verdict | Correction / note |
|---|---|---|
| NEWS-01 | Verified | |
| NEWS-02 | Partially verified | The $9.4m credit "is consistent with, but does not prove" the Greyfin allegations; the article does not name the customer. Specific allegations Low confidence; credit High. |
| NEWS-03 | Verified | About six to seven weeks before year-end; filing stated "no disagreements"; "after" is timing only. |
| NEWS-04 | Partially verified | Only one of two anonymous sources said Okafor wanted revenue deferred until delivery; the other called it "about timing, not about whether the orders were real". Rumor. Payment is the only confirmed fact. |
| NEWS-05 | Verified | "Announced by June 24, 2026"; add the hedged quote. |
| NEWS-06 | Partially verified | April 11 to 14 dates come from LIT-004; add LIT-004 and the company's statement that it found no evidence data was taken. |
| NEWS-07 | Verified | Add 10-K as primary source (operating cash flow $9.7m; net AR +62.0%); confidence High. |
| NEWS-08 | Verified | |
| LIT-F01 | Verified | "Central to Gen-3" is commentary. |
| LIT-F02 | Verified | Plaintiff figures, not a judgment. |
| LIT-F03 | Verified | |
| LIT-F04 | Verified | '812 IPR instituted; final decision expected November 2026. |
| LIT-F05 | Verified | |
| LIT-F06 | Verified | No damages amount stated. |
| LIT-F11 | Verified | These are events new since the 10-Q. |
| LIT-F08 | Verified | Outage hit four Pinecrest DCs; claim is 1.0% of equity value. |

## Run D: financial

| ID | Verdict | Correction / note |
|---|---|---|
| FIN-01 | Verified | |
| FIN-02 | Verified | |
| FIN-03 | Verified | Book-to-bill is implied, not reported; H1 2026 hardware is net of the $9.4m credit. |
| FIN-04 | Partially verified | Restructuring recurred FY2022 to FY2025 (3.1, 4.6, 5.2, 7.9) and was 4.4 in H1 2026 alone; $72.6m is analyst judgment pending a QoE. |
| FIN-05 | Verified | DSO on year-end net AR excluding contract assets; including them FY2025 is 104.4. |
| FIN-06 | Verified | |
| FIN-07 | Verified | |
| FIN-08 | Verified | |
| FIN-18 | Verified | Note 9 is a summary; EBITDA 48.6 strict basis gives 3.62x under (b). Confidence Medium. |
| FIN-19 | Verified | Conditional wording; confidence Low to Medium; first 3.00x test is September 30, 2026. |
| FIN-20 | Verified | Present as a sensitivity, not a restatement; $22.4m later delivered. |
| FIN-21 | Verified | Revenue ex bill-and-hold still clears the threshold by $0.5m; do not imply intent. |
| FIN-22 | Verified | |
| FIN-23 | Partially verified | H1 2026 adjusted revenue is 234.3 (+3.4%), not 233.9 (+3.3%). Q2 124.6 (+6.0%) correct. The $9.4m add-back must be paired with removing it from Q4 2025. Severity could be Medium. |
| FIN-25 | Verified | Illustrative; the 11.5x applied to trailing bases is the analyst's choice. |
| FIN-26 | Partially verified | Same as X-12: about $245.9m including up to $11.0m double-trigger severance and benefits, or $234.9m excluding it; $17.6m equity acceleration not a cash claim until confirmed. |
| FIN-09 | Partially verified | H1 2026 net new ARR 7.6 (about 15.2 annualized) vs 29.7 for full-year FY2025. |
| FIN-10 | Verified | Opex includes restructuring of 4.4 vs 2.6. |
| FIN-11 | Verified | DIO on annualized H1 cost of revenue; 102.2 days on LTM. Inventory includes returned bill-and-hold units. |
