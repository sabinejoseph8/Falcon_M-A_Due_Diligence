# Scorecard: Project Falcon diligence run (blind run 4, 2026-10-18)

Graded with `/evaluate` against `evaluation/answer-key.md`, using this run's files only: `memory/findings.md`, `memory/analyst-reports/verification-*.md` and `output/Project-Falcon-Due-Diligence-Report.md`. Earlier scorecards and runs were not opened.

## Headline results

| Measure | Result | Target |
|---|---|---|
| Recall, overall | 18.0 / 18 = 100.0% | High |
| Recall, Critical and High group | 13.0 / 13 = 100.0% | High |
| Severity accuracy | 18 / 18 = 100.0% | High |
| Unsupported findings in the report | 0 | 0 |
| Distractors rated too high | 0 of 4 | 0 |
| Planted positives (P19) in the report | Yes, mostly (see note) | Present |

## Recall by severity group

Each issue is placed in the group of the first severity listed in its expected severity.

| Group | Issue IDs | Score |
|---|---|---|
| Critical | P05, P07, P08, P15 | 4.0 / 4 = 100.0% |
| High | P01, P02, P03, P04, P09, P10, P11, P12, P14 | 9.0 / 9 = 100.0% |
| Medium | P06, P13, P16, P17 | 4.0 / 4 = 100.0% |
| Low | P18 | 1.0 / 1 = 100.0% |
| **Critical and High group** | P01, P02, P03, P04, P05, P07, P08, P09, P10, P11, P12, P14, P15 | **13.0 / 13 = 100.0%** |
| **Overall** | P01 to P18 | **18.0 / 18 = 100.0%** |

Denominator check: Critical 4 + High 9 + Medium 4 + Low 1 = 18 IDs listed. The Critical and High group is 13 IDs.

## Planted issues

"Highest severity" is the highest severity among the matching verified findings. "Within one level" is measured against a severity the answer key accepts.

| ID | Expected | Result | Matching findings (status) | Highest severity | Severity OK | Notes |
|---|---|---|---|---|---|---|
| P01 | High (Critical ok) | Found | SEC-002 (V), FIN-020 (V), FIN-002 (V), SEC-029 (PV), X-02 (PV) | Critical | Yes | $31.8m, 20.6% of Q4, Q4 growth 5.1%, FY2025 growth 11.6%, all cited to 10-K Note 2 and the CSVs. |
| P02 | High | Found | SEC-002 (V), SEC-028 (PV), NEWS-002 (PV), X-02 (PV) | Critical | Yes (one level) | $9.4m return under a May 2026 amendment with the largest customer; explicitly linked as partial corroboration of the short seller. |
| P03 | High | Found | FIN-007 (PV), SEC-018 (V), SEC-006 (V), X-13 (V), X-03 (V) | Critical (via X-03) / High | Yes | DSO 63.5 to 86.4, allowance 3.8% to 2.1%, contract assets +142%, Norvale 38% of AR, net AR +62% (FIN-007 card). |
| P04 | High | Found | FIN-008 (V), SEC-009 (V), X-06 (PV) | Critical (via X-06) / High | Yes | OCF 40.8 to 9.7, FY2025 FCF -10.1, H1 2026 OCF -4.2 and FCF -13.0. |
| P05 | Critical or High | Found | SEC-003 (V), SEC-004 (V), NEWS-003 (V), X-10 (PV) | High | Yes | Unremediated weakness, adverse ICFR opinion, auditor dismissed after the expanded-procedures warning, replaced by a small firm. |
| P06 | Medium or High | Found | SEC-005 (V), NEWS-005 (PV), X-10 (PV) | High | Yes | $0.9m payment; 8-K "no disagreement" vs news; the dispute is labeled RUMOR with Low confidence; recorded as a source conflict. |
| P07 | Critical | Found | X-03 (V), SEC-006 (V), FIN-004 (V), NEWS-007 (V), FIN-020 (V) | Critical | Yes | All elements present, including Norvale growth ex bill-and-hold of 11.4%. |
| P08 | Critical | Found | X-04 (PV), LIT-F01 (V), LIT-F08 (V), SEC-024 (V), SEC-026 (V), LIT-F10 (V) | Critical | Yes | Jul 22 ruling vs the Aug 6 10-Q "in discovery"; $96.4m; injunction on Gen-3 (about $211.0m); stay denied; no accrual. |
| P09 | High | Found | X-05 (PV), SEC-012 (V), NEWS-006 (PV), LIT-F05 (V), LIT-F15 (V) | High | Yes | Ransomware claim (unverified), 40 sites, no 8-K Item 1.05, $2.3m and $1.8m, Pinecrest rank 4 at $17.4m, $12.0m, gross negligence vs a $1.4m cap. |
| P10 | High (Medium ok) | Found | LIT-F03 (PV), SEC-011 (PV), LIT-F13 (PV), X-02 (PV) | Critical (via X-02) / High | Yes | Labeled ALLEGATION; follows the short report; names Hale and Okafor. |
| P11 | High (Medium ok) | Found | FIN-005 (V), X-09 (V), NEWS-008 (V), FIN-013 (V) | High | Yes | 35.1% add-backs, restructuring every year since 2022, implementation delays treated as an operating cost. The growth of "other non-recurring" (1.2 to 9.6) is in the FIN-005 card but not in the report text. |
| P12 | High | Found | X-07 (PV), FIN-015 (V), FIN-016 (V), FIN-018 (PV), SEC-008 (PV), SEC-007 (V) | Critical | Yes (one level) | 2.26x = 202.5 / 89.7; capped definition 2.65x (2.67x on the 48.2 EBITDA basis, in the FIN-016 card); 3.00x step-down; year-end ratio could exceed 3.00x; $227.5m refinanced at closing. |
| P13 | Medium | Found | X-08 (PV), SEC-015 (V), SEC-016 (V), X-10 (PV) | High | Yes (one level) | $28.6m, $17.6m single-trigger, landlord rent reset, no lead independent director (also in SEC-017, which was not verified). |
| P14 | High | Found | X-06 (PV), FIN-003 (V), FIN-006 (V), FIN-009 (V), SEC-001 (V), SEC-020 (V) | Critical | Yes (one level) | H1 -1.7%, Q2 -4.0%, gross margin 40.8% to 38.0%, net loss 8.9, Adjusted EBITDA -23.3%, guidance cut, backlog -22% after a record Q4, NRR 118% to 111%. |
| P15 | Critical (High ok) | Found | X-01 (V), FIN-021 (V), FIN-001 (V), SEC-001 (V), NEWS-001 (V) | Critical | Yes | EV $1,352.8m, 18.3x on the $74.0m midpoint vs 11.5x. |
| P16 | Medium (High ok) | Found | SEC-030 (PV), SEC-014 (V), NEWS-002 (PV), X-02 (PV) | Critical (via X-02) / Medium | Yes (one level of High) | 142% payout; $470.5m vs the $470.0m threshold; tied to the short seller's allegation. |
| P17 | Medium | Found | X-12 (V), SEC-022 (V), NEWS-009 (V) | Medium | Yes | Single source in China, 7.5% to 25% proposal, Q1 2027 decision, 2 to 3 points, 12 to 18 months (NEWS-009 card). |
| P18 | Low or Medium | Found | SEC-021 (V), X-16 (V), FIN-014 (V) | Medium | Yes | $98.4m goodwill ($57.4m Lumora) tested Oct 1, 2025, before the share price fall (43.8% to $17.85, 48.3% to the $16.40 low). |

V = Verified, PV = Partially verified (rewritten with the verifier's corrected wording).

## Distractors

| ID | Distractor | How the run rated it | Too high? |
|---|---|---|---|
| D1 | Ruiz settlement, $3.2m | SEC-013 Low, LIT-F06 Low; "settled and accrued" in the report | No |
| D2 | Delmarco invoice case, $0.4m | LIT-F16 Low; "closed" in the litigation table | No |
| D3 | OSHA citation, $48 thousand | LIT-F16 Low; "closed" | No |
| D4 | Scholarship article | Not a finding; the news analyst set it aside as having no diligence relevance | No |

Borderline note: X-14 (Medium) lists the Ruiz final approval date as one item in a calendar of court dates around the IC meeting. The finding rates the timing clash, which is driven by Vantor, Pinecrest and the securities case, not Ruiz itself. It is not counted as a distractor rated too high, but Ruiz would be better left out of that list.

## Unsupported findings

**0.** The verifiers checked 90 findings: 60 Verified, 30 Partially verified, 0 Not supported or Rejected. Every Partially verified finding appears in the report with the verifier's corrected wording. The 15 findings that were not sent for verification appear only in Appendix 9.3, labeled "not verified". Spot checks of those against their sources (SEC-013, SEC-017, LIT-F06, LIT-F16, FIN-012, FIN-022) found no unsupported claims.

## Planted positives (P19, not scored)

- **In the report:** ARR (139.2 in the metrics table; $146.8m in the executive summary), FY2025 software growth of 27.1%, NRR 118% to 111%, #3 position with about 11% share, and market growth of about 15% a year.
- **Missing:** software's 25.6% share of FY2025 revenue is not stated, and "ARR +27%" appears only as the software revenue growth figure.

## Three most useful improvements to the agent instructions

1. **Hold severity at the level the evidence supports.** P02, P12 and P14 have an expected severity of High, but the run's highest matching finding was Critical. The run also has many Criticals (X-01, X-02, X-03, X-04, X-06, X-07, plus FIN-016, FIN-018 and SEC-026). All are within one level, but an IC reader sees eleven "Critical" labels.
   - Add a rule that supporting findings keep their own severity.
   - Add a rule that Critical requires a stated test: more than 10% of value, a closing block, or a default before signing or closing that the numbers confirm rather than project.
2. **Self-check the X- findings before verification.** The lead agent's cross-source findings had the highest correction rate: 9 of 19 Partially verified, against 21 of 71 for the analysts. Typical errors were absolute words ("every indicator"), unsupported ranks ("Vantor the #1 player"), durations ("7+ months", "3 quarter-ends") and "likely" on projected outcomes.
   - Add a short pre-verification checklist to the Observe step: no absolute words, every rank and duration taken from a source, inferences and projections labeled.
3. **Consolidate duplicates and keep positives explicit.** The risk matrix has 90 rows and the PDF is 38 pages. Several findings restate the same fact:
   - SEC-001, NEWS-001, FIN-001 and FIN-021
   - SEC-010 and SEC-026
   - LIT-F02 and LIT-F10
   - LIT-F03 and LIT-F13

   Instruct the lead agent to fold duplicates into a parent finding (as "supporting IDs"), keep closed or settled matters out of Medium aggregates such as X-14, and state the planted-type positives with their headline numbers in the executive summary (software share of revenue, ARR growth). The report should also carry detail points that sit only in analyst cards, such as the growth of "other non-recurring" add-backs, into the workstream detail.
