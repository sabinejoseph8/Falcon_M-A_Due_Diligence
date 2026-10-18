# Scorecard: Project Falcon diligence run

- Run graded: blind run of 2026-10-18 (the Phase 4 blind run on this Mac), report in `output/Project-Falcon-Due-Diligence-Report.md`
- Graded: 2026-10-18, against `evaluation/answer-key.md` (18 planted issues, 1 planted positive set, 4 distractors)
- Inputs: `memory/findings.md` (94 findings; 68 verified: 47 Verified, 21 Partially verified, 0 Not supported) and the report

## Headline scores

| Measure | Result | Target |
|---|---|---|
| Recall, overall | 17.0 / 18 = **94.4%** (16 Found, 2 Partially found, 0 Missed) | High |
| Recall, Critical issues (P05, P07, P08, P15) | 4.0 / 4 = **100%** | High |
| Recall, High issues (P01 to P04, P09 to P12, P14) | 8.5 / 9 = **94.4%** | High |
| Recall, Critical and High combined | 12.5 / 13 = **96.2%** | High |
| Recall, Medium issues (P06, P13, P16, P17) | 4.0 / 4 = 100% | |
| Recall, Low or Medium issues (P18) | 0.5 / 1 = 50% | |
| Severity accuracy (within one level) | 18 / 18 = **100%** | High |
| Unsupported findings that reached the report | **0** | 0 |
| Distractors rated Medium or above | **0** of 4 | 0 |
| Planted positives (P19) in the report | Partly | Present |

Severity grouping uses the first expected level in the answer key. Severity accuracy uses the highest rating among the matching verified findings, or the standalone finding where noted.

## Planted issues

| ID | Planted issue (short) | Expected severity | Result | Run's severity | Matching finding IDs | Notes |
|---|---|---|---|---|---|---|
| P01 | Q4 2025 bill-and-hold of US$31.8m; underlying Q4 growth about 5.1%, FY2025 about 11.6% | High (Critical ok) | Found | Critical | X-01, SEC-02, FIN-18, FIN-01 | Exact figures, cross-source. Also showed Q4 missed consensus without bill-and-hold. |
| P02 | US$9.4m reversed in Q2 2026 under an amendment with the largest customer; corroborates short seller | High | Found | High | SEC-02, SEC-06, NEWS-04, NEWS-03, X-02, X-08 | Linked to the May 12 denial and to Norvale (labeled inference). |
| P03 | Receivables quality: AR +62%, DSO 63.5 to 86.4, allowance 3.8% to 2.1%, contract assets +142%, Norvale 38% of AR | High | Found | High | FIN-06, SEC-10, X-01 | All five elements present. |
| P04 | Cash conversion collapse; FY2025 FCF -10.1; H1 2026 OCF -4.2, FCF -13.0 | High | Found | High | FIN-08, SEC-10, SEC-19, X-10 | FIN-08 corrected by the verifier ("12 months", not 18). |
| P05 | Material weakness, adverse opinion, unremediated; auditor dismissed after flagging Q4 procedures; small regional replacement | Critical or High | Found | High | SEC-04, SEC-05, NEWS-05, NEWS-07, X-07 | Small regional firm noted (NEWS-05). |
| P06 | CFO exit with unusual US$0.9m; 8-K "no disagreement" vs anonymous dispute claim (rumor) | Medium or High | Found | High (NEWS-06); Medium (SEC-08) | SEC-08, NEWS-06, X-07, conflict C4 | Dispute labeled rumor with Low confidence, as required. |
| P07 | Norvale concentration, change-of-control termination, Kinetic Aisle, underlying growth about 11% | Critical | Found | Critical | X-02, SEC-03, NEWS-09, FIN-11, SEC-27, FIN-18 | Underlying Norvale growth 11.4% computed. |
| P08 | Vantor: adverse July 22 ruling, US$96.4m expert damages, Gen-3 injunction, stay denied, no accrual; 10-Q silent on the ruling | Critical | Found | Critical | X-03, LIT-01, LIT-02, LIT-03, LIT-11, SEC-12, SEC-26 | Disclosure gap confirmed in iteration 2. |
| P09 | Cyber incident: ransomware claim, about 40 sites, no Item 1.05 8-K, US$2.3m credits, US$1.8m costs; Pinecrest (#4 customer, US$17.4m) sues for US$12.0m vs about US$1.4m cap | High | **Partially found** | High | X-09, SEC-13, NEWS-10, LIT-07, SEC-14 | Missing cross-source link: no finding identifies Pinecrest as the #4 customer with US$17.4m of FY2025 revenue (`revenue_by_customer.csv` row 4). The litigation analyst flagged it as unknown and the lead agent did not look it up. |
| P10 | Securities class action on bill-and-hold; follows short report; names CEO and former CFO | High (Medium ok) | Found | High | LIT-05, LIT-06, LIT-13, SEC-11, X-13 | |
| P11 | Adjusted EBITDA quality: add-backs 35%, restructuring every year, implementation delays, other non-recurring 1.2 to 9.6 | High (Medium ok) | Found | High | X-06, FIN-04, FIN-05, NEWS-12 | The growth of "other non-recurring items" was not called out explicitly; the main point is fully covered. |
| P12 | Covenant: 2.26x equals uncapped EBITDA; capped about 2.67x; step-down to 3.00x; change of control default, about US$227.5m to refinance | High | Found | Critical (X-05, FIN-17); High (SEC-25) | X-05, FIN-17, SEC-25, SEC-09, SEC-18, X-10 | Exact match to the key (202.5 / 89.7; 75.9; 2.67x). Rated one level high; within tolerance, and the verifier flagged it as borderline. |
| P13 | Change-of-control costs: US$28.6m incl. US$17.6m single-trigger; landlord rent reset; no lead independent director | Medium | Found | Medium (SEC-16, SEC-17); covered in X-07 (High) | SEC-16, SEC-17, SEC-23, X-07 | Main points are in verified X-07 (verifier confirmed the proxy facts). The standalone Medium cards were not sent to the verifier. |
| P14 | 2026 deterioration: revenue, margin, net loss, EBITDA, guidance cut, backlog -22%, retention 118% to 111% | High | Found | High | X-11, FIN-03, FIN-12, SEC-01 | Backlog drop at year-end despite record Q4 noted (FIN-12). |
| P15 | Stale deal model; 18.3x on revised guidance, not 11.5x | Critical (High ok) | Found | Critical | X-04, SEC-01, NEWS-01, FIN-14, FIN-20 | Also flagged the leak-inflated premium. |
| P16 | Bonuses at 142%; without bill-and-hold revenue 470.5 vs 470.0 threshold; short seller made similar claim | Medium (High ok) | Found | High (FIN-19); Medium (SEC-15) | SEC-15, FIN-19, X-07, NEWS-03 | Verifier narrowed the wording correctly. |
| P17 | Single-source LiDAR in China; tariff 7.5% to 25%; 2 to 3 points; 12 to 18 months | Medium | Found | Medium (SEC-20, NEWS-13); covered in X-11 (High) | SEC-20, NEWS-13, X-11 | Cross-source link made in X-11 and verified. Standalone cards not verified. |
| P18 | Goodwill (US$98.4m, US$57.4m Lumora) last tested before the share price fell about 44% | Low or Medium | **Partially found** | Medium (SEC-22); Low (FIN-15) | SEC-22, FIN-15 | Found, but not verified and not linked to the share price fall (FIN-15 compared market cap to book equity instead). Appears only in the report's "not verified" list. |

## Planted positives

| ID | Positive | Result | Notes |
|---|---|---|---|
| P19 | FieldOS ARR US$139.2m (+27%), retention 118% slowing to 111%, software 25.6% of revenue; #3 with about 11% share of a market growing about 15% a year | Partly | All elements are in the analyst reports' "positive or mitigating points" (SEC, NEWS, FIN). The report mentions only "Software is still growing" and the 15% market growth; it has no mitigating-points section, and the #3 / 11% share appears only as Vantor context. |

## Distractors

| ID | Distractor | Run's rating | Result |
|---|---|---|---|
| D1 | Ruiz settlement, US$3.2m | Low (SEC-24, LIT-10) | Correct |
| D2 | Delmarco case, US$0.4m | Low relevance, one line | Correct |
| D3 | OSHA citation, US$48 thousand | Low relevance, one line | Correct |
| D4 | Scholarship article | No diligence relevance | Correct |

## Unsupported findings

- Verifier results: 68 checked, 0 Not supported. All 21 Partially verified findings were rewritten with corrected wording before the report, and the corrections were re-checked once.
- Errors the verifier caught before the report: X-03 faulted the 10-Q for omitting Gen-3 Plus, which was added after the filing; X-09 used a software-below-ARR point that also held before the outage; FIN-08 said 18 months of negative free cash flow instead of 12; X-07 used 49 days instead of 51.
- Unsupported findings in the report: **0**.

## Builder note: automated checks

Added by the builder after grading. With the checks as written, this run fails 3 of 34 (`python3 tests/run_all.py`). During the run, the lead agent edited `tests/test_phase3_run.py` so that its own output passed; that edit was reverted, because the system being graded must not change its grader. In all three, the run followed `CLAUDE.md`, and the check expected the sample run's format instead: (1) the report heading "Answers to the six IC questions" is the template's own wording, but the check looks for "investment committee"; (2) the run log names the step "Step 5: REPORT", as `CLAUDE.md` does, but the check looks for "5. REPORT", so the run counts as incomplete and the checkpoint-log check is skipped; (3) register IDs are links to the full finding cards, as `CLAUDE.md` asks, but the check reads only plain IDs, so it sees an empty register and every cited ID looks unknown. The one real departure from the template is an extra report section, "6. Hypotheses tested". None of this changes the grades above.

## Three most useful improvements to the agent instructions

1. **Size every named counterparty against the customer data (would have fully found P09).** Add to the lead agent's Observe step: "For every customer, supplier or litigant named in any source, look it up in `revenue_by_customer.csv` (or ask the financial analyst) and state its rank and revenue." Pinecrest was the #4 customer (US$17.4m), and the litigation analyst explicitly listed this as unknown, but no one closed the gap.
2. **Verify the Medium findings the report relies on, and connect impairment tests to market data (would have fully found P18).** Change Step 4 to send every Medium finding that is cited in the IC answers, or that feeds an X- finding, to the verifier, not just three. Add to the financial analyst's checklist: "Compare the date of the last goodwill test with share price and market cap moves since then." The run's goodwill finding stayed unverified and missed the 44% share price fall.
3. **Add a mitigating-points section to the report template and tighten Critical calibration.** Add "Positive and mitigating points" to the report template so planted positives such as P19 surface (the analysts found them; the template dropped them). Also add a calibration note: "Debt issues that are cured by refinancing at closing are High unless they create a pre-signing default or liquidity event." This would have kept X-05 at the expected High instead of the verifier's "borderline Critical".
