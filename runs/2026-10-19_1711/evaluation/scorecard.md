# Project Heron: scorecard

Run graded: the diligence run of October 19, 2026 (`memory/target.txt` = heron; report `output/Project-Heron-Due-Diligence-Report.md`). Graded from this run's files only, against `targets/heron/evaluation/answer-key.md`, using the fixed grading rules.

**Interpretation used for "wrong severity" (Found vs Partially found):** an issue is Partially found when its main point is in the verified findings but the severity of its parent row in the report is not one the answer key accepts. Severity accuracy below applies the one-level tolerance separately.

## Recall

Severity groups use the first-listed expected severity. P19 (positives) is excluded.

| Group | IDs | Score |
|---|---|---|
| Critical | P01, P02, P03, P04 | 3.5 / 4 = 87.5% |
| High | P05, P06, P07, P08, P09, P10, P11, P12, P13 | 8.0 / 9 = 88.9% |
| Critical and High | P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13 | 11.5 / 13 = 88.5% |
| Medium | P14, P15, P16, P17 | 3.5 / 4 = 87.5% |
| Low | P18 | 1.0 / 1 = 100.0% |
| **Overall** | P01 to P18 | **16.0 / 18 = 88.9%** |

Denominator check: Critical 4 IDs, High 9, Critical and High 13, Medium 4, Low 1, overall 18. All match.

## Severity accuracy

Found or Partially found issues whose highest matching verified severity is within one level of an accepted severity: **18 / 18 = 100.0%**.

For information, exact match of the report's parent-row severity to an accepted severity: 14 / 18 = 77.8% (misses: P01 High vs Critical; P10 Critical vs High; P11 Critical parent vs High; P16 High vs Medium).

## Unsupported findings that reached the report

**0** (target: zero). The verifiers checked 151 findings: 98 Verified, 53 Partially verified (rewritten with corrected wording before the report), 0 Not supported. Every finding in the report matches its cited source.

## Distractors rated too high

**1 of 4.**

| ID | Distractor | Run's treatment | Result |
|---|---|---|---|
| D1 | Brennan Sales Group suit | LIT-007, SEC-034 Low; listed as a mitigant | OK |
| D2 | CFO "dumping shares" forum post | NEWS-027 Low, but **SEC-039 (Medium)** "CFO 10b5-1 plan adopted six days before EC inspections" has its own risk matrix row, with NEWS-027 as supporting | **Too high** |
| D3 | FY2023 restructuring add-back | FIN-007, SEC-035 Low; listed as a mitigant | OK |
| D4 | DOE standby rule | NEWS-026, SEC-031 Low; listed as a mitigant | OK |

## Planted issues

| ID | Planted issue | Expected | Result | Run severity (parent) | Matching finding IDs | Notes |
|---|---|---|---|---|---|---|
| P01 | Aura hazard far above the US$6.0m reserve | Critical | Partially found | High | X-011, NEWS-001, NEWS-002, NEWS-003, NEWS-004, SEC-011, SEC-013, SEC-014, LIT-001, LIT-009, LIT-010, FIN-002, FIN-039, FIN-064 | All facts found (1.62m x US$119 = US$192.8m, 12.5% of EV; 23% uptake; "limited number"; 58 alleged incidents). Lead and verifier lowered it to High because the 10% test needs about 80% refund uptake. The key rates the refund remedy itself as Critical |
| P02 | Change-of-control pension funding US$230.5m | Critical | Found | Critical | X-001, SEC-001, SEC-002, NEWS-018, FIN-012, FIN-054 | Tarnwood's "non-issue" view noted in conflicts |
| P03 | Insights vs 2022 FTC Order | Critical (High ok) | Found | High | X-008, SEC-026, SEC-027, NEWS-005, NEWS-006, LIT-003, LIT-012, FIN-023, X-019 (Bellmark rank 8) | US$310m (20.1% of EV), re-identification, Colorado AG, FTC inquiry all cited |
| P04 | AdaptiveComfort patent ownership | Critical (High ok) | Found | High | X-009, X-010, LIT-002, LIT-011, SEC-006, SEC-007, SEC-008, NEWS-008, FIN-051 | Includes the conflict between Delmora's "after June 2017" claim and the March 6, 2017 priority date, separate counsel, trial date, licensing thesis |
| P05 | Insurance gap for the Aura cohort | High | Found | High | SEC-012, LIT-008, X-011 | P01 + P05 cross-source link made in X-011 |
| P06 | IRS transfer pricing NOPA | High | Found | High | X-013, SEC-009, SEC-010, FIN-035, FIN-061 | |
| P07 | Nimbus earn-out accelerated to US$90.0m | High | Found | High | X-002, SEC-003, SEC-004, SEC-005, FIN-024, FIN-055 | 34% CDO interest and timing after the Strategic Review Committee included |
| P08 | Ensamble Norte guarantee at risk | High | Found | High | X-006, SEC-018, SEC-019, NEWS-013, NEWS-015, FIN-059, FIN-058 | P08 + P17 link made (terms stretch may have squeezed the JV, labeled inference) |
| P09 | Environmental accrual at the low end, contamination off site | High | Found | High | X-012, SEC-022, LIT-004, LIT-013, NEWS-016, NEWS-017, FIN-036, FIN-062 | 2023 report allegation in LIT-004 |
| P10 | WSEA contract lost | High | Partially found | Critical | X-003, NEWS-010, SEC-028, FIN-021, FIN-046, FIN-047, FIN-048 | Fully found, including the 10-Q filed after the award. Rated Critical (with a stated, labeled inference of more than 10% of value), which the key does not accept |
| P11 | Warranty reserve released while claims rise | High | Partially found | Critical (folded into X-004) | FIN-003, SEC-015, NEWS-024, X-004 | FIN-003 itself is High and covers the claim rate, accrual cut and expense fall. In the report it sits only under the Critical earnings-base parent (X-004), so it has no row of its own. The US$15.7m reserve comparison was not computed |
| P12 | Sanctions and export controls via the Dubai distributor | High (Critical ok) | Found | High | X-007, SEC-024, SEC-025, NEWS-011, NEWS-012, FIN-020, FIN-049, FIN-050 | Audit Committee meetings before the 10-K statement found |
| P13 | EU competition Statement of Objections | High | Found | High | SEC-023, LIT-005, FIN-063, X-019 (Vierhaus rank 6) | |
| P14 | Open source licence exposure | Medium | Found | Medium | LIT-006, NEWS-009, SEC-032 | P04 + P14 link made in the Q3 answer (both go to AdaptiveComfort) |
| P15 | Reno labour disruption | Medium | Found | Medium | SEC-030, NEWS-019, NEWS-020 | 10-K "relations good" contrast not noted |
| P16 | Unhedged peso exposure | Medium | Partially found | High (X-016 margin trend) | SEC-016, FIN-018, FIN-052, NEWS-023, X-016 | Fully found and sized, but rated High (alone, and inside the High margin-trend parent) |
| P17 | H1 2026 cash flow inflated by timing | Medium (High ok) | Found | High | X-005, SEC-017, FIN-009, FIN-010, FIN-011, FIN-014, FIN-048, NEWS-014 | P10 + P17 link made (advance comes from a lost contract) |
| P18 | Sales tax VDAs, US$1.4m | Low | Found | Low | SEC-033 | |

Cross-source checks in the key: P01 + P05 (made), P04 + P14 (made), P08 + P17 (made), P10 + P17 (made), P02 + P07 + P01 as closing cash obligations (made in X-017 and X-018; P01 shown as contingent).

## Planted positives (P19, not in recall)

| Positive | In the report? |
|---|---|
| Subscription gross retention about 93% | Yes (FIN-026) |
| Subscribers 1,370k to 1,465k | Not stated as a positive (subscriber growth appears only inside X-015) |
| Term loan to June 2029, undrawn US$150.0m revolver, covenant headroom | Yes (SEC-040) |
| DSO stable at 45 to 47 days | No (FIN-030 was Low and not verified) |
| Unqualified audit opinion and no internal control changes | Yes (SEC-036) |
| Current thermostats tested compliant with the DOE rule | No (the report mentions the rule's timing and industry scope, not the compliance test; SEC-031 not verified) |

## Three most useful improvements to the agent instructions

1. **Measure the Critical test at the remedy a regulator or claimant actually seeks.** P01 was lowered to High because no uptake estimate exists, even though CPSC staff formally seek a full refund or replacement worth 12.5% of EV and the claims appear uninsured. Suggested rule: when a regulator or claimant formally seeks a remedy whose cost exceeds 10% of value, rate it Critical on that remedy (labeled as an upper bound), unless a source shows the remedy is unlikely.
2. **Keep a component issue's own severity visible when a parent `X-` finding absorbs it.** P11 (warranty, High) appears in the report only under the Critical earnings-base parent, and P16 (peso, Medium) only under the High margin trend. Suggested rule: when a supporting finding's severity differs from its parent's, and it is a distinct accounting or risk issue, give it its own risk matrix row at its own severity, and do not let trend findings raise their components' visible severity.
3. **Treat date coincidence alone as Low, and check pre-set trading plans as mitigants.** SEC-039 rated the CFO's 10b5-1 plan Medium only because its adoption date fell six days before the EC inspections, which no source links to any wrongdoing (D2). Suggested rule: a finding that rests only on the timing of two dated events, with no source alleging misconduct, is Low; insider sales under a plan adopted before the relevant events are a mitigant.

Also noted (execution, not instructions): at Checkpoint 1 the plan summary was not printed in chat before the approval question; this was logged. The fixed mitigant list in CLAUDE.md has no "stable working capital metrics" or "regulatory compliance confirmed" item, which is why two planted positives (DSO, DOE compliance) were left out.
