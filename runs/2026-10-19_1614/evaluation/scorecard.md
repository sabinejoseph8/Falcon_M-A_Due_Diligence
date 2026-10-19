# Project Kestrel: Scorecard

> FICTIONAL. Grades the blind diligence run on Kestrel (Corvane Diagnostics) completed on 2026-10-19, against `answer-key.md`. Graded from this run's files only: `memory/findings.md`, `memory/analyst-reports/` (including the verifier reports) and `output/Project-Kestrel-Due-Diligence-Report.md`. No earlier scorecards or runs were opened.

Run summary: 2 of 3 iterations; 151 analyst findings plus 19 cross-source (X-) findings; 155 verified (118 Verified, 37 Partially verified, 0 Rejected); 15 Low findings not verified; all three checkpoints logged; recommendation "Do not proceed at the current price".

## Headline metrics

| Metric | Result |
|---|---|
| Recall, overall | 18 / 18 = 100.0% |
| Recall, Critical and High group | 13 / 13 = 100.0% |
| Severity accuracy | 18 / 18 = 100.0% |
| Unsupported findings in the report | 0 (target: zero) |
| Distractors rated too high | 0 of 4 |
| Planted positives in the report | 6 of 6 |

## Recall by severity group

Severity group = first-listed expected severity in the answer key. Found = 1, Partially found = 0.5, Missed = 0.

| Group | IDs | Score |
|---|---|---|
| Critical | P01, P02, P03, P04 | 4 / 4 = 100.0% |
| High | P05, P06, P08, P09, P10, P13, P14, P15, P16 | 9 / 9 = 100.0% |
| Medium | P07, P11, P12, P17 | 4 / 4 = 100.0% |
| Low | P18 | 1 / 1 = 100.0% |
| **Critical and High group** | P01, P02, P03, P04, P05, P06, P08, P09, P10, P13, P14, P15, P16 (13 IDs) | **13 / 13 = 100.0%** |
| **Overall** | P01 to P18 (18 IDs) | **18 / 18 = 100.0%** |

Denominator check: Critical 4 IDs, High 9, Medium 4, Low 1, Critical and High 13, overall 18. Each matches the number of IDs listed.

## Planted issues

| ID | Planted issue | Expected severity | Result | Matching finding IDs (status) | Highest severity in run | Severity within one level? | Notes |
|---|---|---|---|---|---|---|---|
| P01 | FCA qui tam with DOJ intervention | Critical | Found | X-005 (V), LIT-001 (V), LIT-002 (V), SEC-012 (V), NEWS-007 (V) | Critical | Yes | 41,200 claims, 96.4 single, 289.2 trebled = 17.5% of EV, 3.2 to 61 physicians, Oct 30 complaint, exclusion and CIA risk all cited. The 2x figure (192.8) is not stated. |
| P02 | Medicare 0419U cut not in the model | Critical | Found | X-004 (V), FIN-058 (V), NEWS-004 (V), SEC-017 (V), NEWS-005 (PV), FIN-042 (V) | Critical | Yes | Sized at 30.3 on the FY2025 mix (22.9 + 7.5) and 29.0 on the H1 2026 mix; flat-rate assumption and guidance exclusion both flagged. |
| P03 | Covenant breach at the Sep 30, 2026 test | Critical (High ok) | Found | X-017 (PV), FIN-055 (V), FIN-057 (PV), FIN-056 (PV), SEC-007 (PV), SEC-008 (V), NEWS-003 (V) | Critical | Yes | 78.4 + 11.8 = 90.2, net debt 395.9, 4.39x vs 4.00x step-down, certificate about Nov 14 before signing, revolver 65.0 at risk. Calibration rule applied. |
| P04 | Recurring add-backs; debt sized on them | Critical (High ok) | Found | X-015 (PV), FIN-006 (V), FIN-007 (PV), FIN-008 (V), FIN-009 (PV), X-003 (PV), FIN-054 (V), FIN-017 (V), FIN-023 (V) | Critical | Yes | 44.8% LTM and 30.2% FY2025; 22.3 LTM recurring items; underlying 101.1; 7.4x; 110.0 condition at risk; OCF 22.7%. |
| P05 | DOJ disclosure-timing gap | High | Found | X-006 (PV), SEC-013 (V), LIT-003 (V), NEWS-007 (V) | High | Yes | 22 days, 10-K Item 3 and Note 15 quoted, first disclosure in the 10-Q. |
| P06 | One-off estimate change inflates growth | High | Found | X-001 (V), SEC-001 (V), FIN-049 (V), FIN-050 (PV), NEWS-014 (V), FIN-052 (PV), X-014 (V) | Critical | Yes (one level above) | 120.5 vs 106.3, 11.7% vs 8.0%; conflict with denials and DSO in FIN-052 and X-014. Rated Critical on 11.4% of EV. |
| P07 | Collections deteriorating | Medium (High ok) | Found | FIN-024 (V), FIN-037 (V), FIN-025 (V), SEC-025 (V), X-014 (V), FIN-023 (V) | High | Yes | DSO 58.5 / 62.7 / 79.0 / 80.9; denials 8.9% to 16.2%; reserve 21.3 / 31.3 / 32.9; prior authorization. |
| P08 | Material weakness, not remediated | High | Found | SEC-002 (V), X-014 (V), FIN-052 (PV) | High | Yes | Adverse ICFR opinion; linked to the 14.2; unremediated at the 10-Q. |
| P09 | Veltrane winding down its main trial | High | Found | X-011 (PV), SEC-023 (PV), NEWS-006 (V), FIN-031 (V), FIN-062 (PV) | Critical | Yes (one level above) | 50.5 rank 2, 61.0 of 231.4, halt Aug 27, 90-day termination, brief assumption stale. |
| P10 | Orvia change-of-control termination | High | Found | SEC-022 (V), FIN-069 (V), FIN-032 (V) | High | Yes | Rank 3, 48.7, 11.3%; closing-condition consent recommended. |
| P11 | Single trigger, 280G gross-up, bonus on the one-off | Medium (High ok) | Found | X-016 (V), SEC-031 (PV), FIN-053 (V), SEC-032 (V), SEC-033 (V) | High | Yes | 41.6 CEO (31.4 single trigger, 3.5 gross-up), 14.8 others; 150% vs about 57% without the 14.2. |
| P12 | Related-party lease above market to 2040 | Medium | Found | SEC-030 (V), FIN-067 (V), X-016 (V) | High (X-016); SEC-030 Medium | Yes | 4.8 vs 3.6, 3.5% escalator, extended Nov 2025; CEO is Chair (in X-016). |
| P13 | Patent case moving against Corvane | High (Critical ok) | Found | X-009 (PV), LIT-005 (V), LIT-006 (V), LIT-007 (PV), SEC-026 (V), FIN-059 (PV), FIN-060 (V) | High | Yes | IPR denial, Markman, 68.0 plus 9%, trial Feb 8, 2027, v3 mid-2027, OncoTrace 138.5, no accrual. The 10-K "without merit" wording is not quoted. |
| P14 | Breach described as "network disruption" | High | Found | X-007 (V), X-008 (PV), SEC-015 (V), SEC-016 (V), LIT-008 (PV), LIT-009 (V), LIT-010 (V), LIT-011 (V), NEWS-011 (V) | High | Yes | Item 8.01 not 1.05, Apr 21 claim, Apr 24 allegation, 412,300, OCR, 10.0 limit, 6.1 added back. |
| P15 | Short-seller allegations, partly corroborated | High | Found | NEWS-012 (V), NEWS-013 (V), NEWS-014 (V), NEWS-015 (V), NEWS-016 (V), NEWS-009 (V), X-005 (V) | High (Critical via X-005) | Yes | Labeled as allegations; corroboration by the unsealed qui tam, the CCO exit, the 14.2 and DSO stated in X-005, NEWS-014, NEWS-015 and report section 5. |
| P16 | Deal brief stale; price no longer anchored | High | Found | X-012 (PV), NEWS-019 (V), X-019 (V), FIN-043 (V), FIN-064 (V), LIT-014 (PV) | Critical (X-019); X-012 High | Yes | 137.0 vs 100 to 106; 32.6% vs 83.2%; 24.2x LTM EBITDA; 16.0x guidance midpoint. |
| P17 | Goodwill test stale | Medium (High ok) | Found | X-013 (V), SEC-019 (V), FIN-068 (PV), FIN-044 (V) | High | Yes | 14% headroom, 241.5, 27.80 to 13.10 (-52.9%), CMS cut and guidance cut. |
| P18 | NC DEQ notice of violation | Low | Found | LIT-012 (V) | Low | Yes | 0.18 agreed, payment Nov 15, 2026. |

V = Verified, PV = Partially verified.

## Severity accuracy

18 / 18 = 100.0%. Every Found issue has a highest matching severity within one level of an accepted severity. Two issues were rated one level above the key's only accepted severity: P06 (Critical vs High) and P09 (Critical vs High). Both carry a named test and a number (11.4% and 15.4% of EV); X-011's low end (10.8%) rests on a full-loss assumption, as the verifier noted.

## Distractors

| ID | Distractor | Run's rating | Too high? |
|---|---|---|---|
| D1 | Hollis wage and hour suit | LIT-013, SEC-027, FIN-071: Low; listed as a mitigant | No |
| D2 | FDA letter to Corvane Laboratories Pty | NEWS-021: Low; listed as "not Corvane" | No |
| D3 | 6.8 sale-leaseback gain | SEC-029, FIN-015: Low; listed as correctly excluded | No |
| D4 | 25% reagent tariff | SEC-028, NEWS-020, FIN-070: Low; listed as neutralized | No |

0 of 4 rated too high. Judgment note: FIN-021 (Medium) mentions the sale-leaseback lease liability as a possible debt-like item. It does not treat the gain as an earnings-quality issue, so it is not counted against D3.

## Unsupported findings in the report

0. The four verifier runs marked no finding Not supported (Rejected: 0 of 155). Every finding ID cited in the report is in the register, and spot checks of the key numbers (14.2, 289.2, 90.2 and 4.39x, 0419U rates, 50.5 and 61.0, 48.7) match the cited sources.

## Planted positives

| ID | Result | Matching finding IDs |
|---|---|---|
| P19 | Found in the report (not counted in recall) | LIT-013, SEC-028, SEC-010, FIN-040, SEC-037, FIN-003, SEC-029, FIN-015 |

All six appear in the report's positive and mitigating points: Hollis dismissed (LIT-013), Helixor tariff protection through 2028 (SEC-028), maturities in October 2028 and 2029 (SEC-010), informatics retention 95% to 96% (FIN-040), biopharma growth of 2.7% in H1 2026 (SEC-037, FIN-003), sale-leaseback gain excluded (SEC-029, FIN-015). Named-party lookups: Medicare (rank 1), Veltrane (rank 2) and Orvia (rank 3) are stated; Genaro, Bearhaven, Helixor, Tidewater and Corvane Laboratories Pty are stated as not customers (X-018).

## Three most useful improvements to the agent instructions

Recall and accuracy are at ceiling on this target. The improvements below target the process errors seen in this run.

1. **Give iteration 1 the cross-workstream definitions that numbers depend on.** In iteration 1 the financial analyst did not have the 10-K's 14.2 one-off or the covenant definition. It produced two findings later superseded (FIN-001, FIN-016). The SEC analyst sized covenant leverage on FY2026 guidance rather than on LTM covenant EBITDA under the 15% cap (SEC-007, corrected by the verifier). Suggested instruction: in Step 2, tell the financial analyst to read the covenant definition and any quantified one-offs in the 10-K itself. Tell the SEC analyst to compute any covenant ratio on the covenant definition and LTM data, or to hand it to the financial analyst.
2. **Tighten the Critical test when the number rests on a full-loss or outcome assumption.** X-009 (Genaro) was first rated Critical with no value figure above 10%. X-011 (Veltrane) and P06 were rated one level above the key. Suggested instruction: a Critical finding must show a central-case number above the test threshold, not an upside or full-loss case. If only an outcome (an injunction, a full termination) would meet the test, rate it High and state what would raise it.
3. **Record hygiene in the lead agent's own memory writes.** The lead wrote an invalid status ("Not verified (Low)") for unverified Lows and estimated run-log times instead of reading the clock. Both were corrected before the report. A rumor later confirmed by a primary source (NEWS-007) kept Low confidence until the verifier flagged it. Suggested instruction: unverified Low findings keep status Open with "not verified" in the source cell; take every run-log time from `date`; when a later source confirms a rumor, update the earlier finding's confidence in Observe.

Separate from the agent instructions: `tests/test_phase3_run.py` assumes Falcon's `case_id` column in `docket_index.csv`, but Kestrel's file uses `matter_id`, so Phase 3 failed to import on this run. Run in memory with the column mapped, all 10 Phase 3 checks passed. A separate session is fixing the test.
