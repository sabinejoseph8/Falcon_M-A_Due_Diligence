# Verification summary (Step 4, 2026-10-19)

Four citation-verifier runs in parallel. Full verifier outputs are in the session transcript; this file records each verdict and correction applied to `memory/findings.md`.

## Statistics

| Run | Findings | Verified | Partially verified | Rejected |
|---|---|---|---|---|
| SEC filings | 26 | 19 | 7 | 0 |
| News + Litigation | 19 | 11 | 8 | 0 |
| Financial | 20 | 14 | 6 | 0 |
| Cross-source (X-) | 13 | 6 | 7 | 0 |
| **Total** | **78** | **50** | **28** | **0** |

Not verified (Low, by design): SEC-18, SEC-22, NEWS-11, LIT-07, LIT-10, FIN-20.

No source file contained text trying to instruct the agents (all four verifiers).

## Partially verified: corrections applied

| ID | Correction |
|---|---|
| SEC-06 | Projection used a $185.0m term loan; balance sheet shows $182.5m. Ratio 2.60x to 2.89x; break-even $67.5m (3.6% below guidance low end). |
| SEC-07 | "Must be refinanced" changed to "allows lenders to demand repayment; repaid or refinanced unless lenders consent"; total $227.5m, not $230m. |
| SEC-08 | "Did not hold" softened; gross AR fell from $121.5m to $107.6m in H1 2026. |
| SEC-12 | "No accrual" restated as "no accrual or loss estimate disclosed"; complaint states no damages amount. |
| SEC-20 | Supplier manufactures in China; nationality not stated. |
| SEC-21 | The "strong deliveries" vs warehouse contrast is within the 10-K, not between filings; excerpt caveat added. |
| SEC-28 | Critical test rests on the injunction leg (42.0% of revenue); $140m is an alleged floor; treble damages share 25.0% (not 24.9%). |
| NEWS-01 | Use actual net debt $193.6m; illustrative value $13.61 (not $13.52); range 17.3x to 19.3x. |
| NEWS-03 | Label "revenue booked ahead of cash" as inference; OCF and AR confirmed by cash_flow.csv. |
| NEWS-05 | Interim CFO since Feb 15, 2026, about eight months (not nine). |
| LIT-01 | Remove "after the expected closing"; Critical test restated on Gen-3 injunction ($211.0m, 42.0%). |
| LIT-03 | Dec 18 is when summary judgment motions are due; PTAB decision may land before or after the IC. |
| LIT-04 | Complaint alleges failure to disclose the "full extent" of control weaknesses (a weakness was disclosed Nov 14, 2025). |
| LIT-05 | "Will expand" changed to "is due; may add (inference)". |
| LIT-09 | Dec 9, 2025 Ruiz entry is a notice of settlement in principle. |
| FIN-01 | Title: price implies a higher multiple; $17.85 is not unaffected; add guidance test ($12.66 to $14.56 at 11.5x). |
| FIN-14 | "First binds in FY2025" holds only among year-end dates; definition is the 10-K summary. |
| FIN-15 | Severity lowered Critical to High (projection; upside case compliant; Sep 30 result not in data). Removed "breach likely" and "test has already passed" wording. |
| FIN-16 | Bill-and-hold was 39.5% of FY2025 growth (80.5% of hardware growth), not "most"; slowdown from Q4 2025 labeled inference. |
| FIN-17 | 10-Q ties the return to the "largest customer" (Norvale per 10-K); remaining $22.4m was delivered by Jun 30; garbled 15.6% sentence replaced with 11.5% / 19.0%. |
| FIN-19 | Runway labeled projection; refinancing stated as consequence of event of default. |
| X-02 | Greyfin does not allege accounting-rule failure; only the class action does. |
| X-03 | State projection assumptions; "refinanced or waived"; Sep 30 result not in data. |
| X-05 | Drop "only"; September events postdate the 10-Q; lead with injunction test; "not among the top 10". |
| X-06 | Deleted unsourced "five statements" sentence; added 8-K "no disagreement" conflict; clawback caveat. |
| X-08 | Negative OCF and the $9.4m return are not credit-loss evidence; rest on allowance up 30.8% while gross AR fell 11.4%. |
| X-11 | Shipment annualization labeled projection; periods added; Q2 includes $11.7m credits. |
| X-12 | Use brief's "34%"; 56.3% presented as inference. |

## Severity changes and notes

- FIN-15: Critical to High (accepted verifier advice; calibration rule).
- LIT-08: Medium to Low (records an absence of risk; mitigating point).
- SEC-14: kept High because Okafor is a named defendant in the securities action (verifier said Medium on its own facts unless tied).
- Duplicates resolved by parent X- findings: SEC-13/SEC-24 under X-07; SEC-19/SEC-25 under X-09.
- DSO: report uses net-AR DSO (63.5 to 86.4 days) consistently.
- Verifier follow-up question: a $1.1m "Executive search and CFO transition" add-back was booked in FY2025, before the CFO resigned on Jan 20, 2026 (added to open questions).

## Re-read check

Verifier reports re-read once after updating the register; all 28 corrections above are reflected in `memory/findings.md`.
