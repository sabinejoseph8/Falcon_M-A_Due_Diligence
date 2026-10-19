# Scorecard: Project Falcon diligence run (graded run 5)

- Graded: October 18, 2026
- Run graded: the run in `memory/` and `output/` (started and finished October 18, 2026; 2 of 3 iterations; 3 checkpoints logged)
- Files used: `evaluation/answer-key.md`, `memory/findings.md`, `memory/analyst-reports/verification-A..D_*.md`, `output/Project-Falcon-Due-Diligence-Report.md`
- No earlier scorecards or runs were opened.

## Headline

| Measure | Result | Target |
|---|---|---|
| Recall, overall | 17.5 / 18 = 97.2% | high |
| Recall, Critical and High group | 13.0 / 13 = 100.0% | high |
| Severity accuracy | 18 / 18 = 100.0% | high |
| Unsupported findings that reached the report | 0 | 0 |
| Distractors rated too high | 0 / 4 | 0 |
| Planted positives in the report | Yes (P19) | present |

## Recall by severity group

Severity group = the first severity listed in the answer key's expected severity.

| Group | IDs | Score |
|---|---|---|
| Critical | P05, P07, P08, P15 | 4.0 / 4 = 100.0% |
| High | P01, P02, P03, P04, P09, P10, P11, P12, P14 | 9.0 / 9 = 100.0% |
| Medium | P06, P13, P16, P17 | 4.0 / 4 = 100.0% |
| Low | P18 | 0.5 / 1 = 50.0% |
| **Critical and High** | P01, P02, P03, P04, P05, P07, P08, P09, P10, P11, P12, P14, P15 | 13.0 / 13 = 100.0% |
| **Overall** | P01 to P18 | 17.5 / 18 = 97.2% |

Denominator check: 4 + 9 + 4 + 1 = 18 IDs listed; the Critical and High group lists 13 IDs.

## Planted issues

| ID | Planted issue (short) | Expected severity | Result | Matching finding IDs (parent first) | Run severity (highest verified) | Severity OK | Notes |
|---|---|---|---|---|---|---|---|
| P01 | $31.8M Q4 2025 bill-and-hold; growth ex bill-and-hold 5.1% (Q4) and 11.6% (FY) | High (Critical ok) | Found | X-03, SEC-02, FIN-16, FIN-02 | High | Yes | Cross-source link made; all four numbers recomputed. |
| P02 | $9.4M reversed in Q2 2026 under an amendment with the largest customer; partly corroborates the short seller | High | Found | X-03, SEC-30, NEWS-02, FIN-17 | High | Yes | Verifier softened "partly confirmed" to "consistent with, but does not confirm"; still links the return to the short report and to Norvale. |
| P03 | Receivables quality: AR +62%, DSO 63.5 to 86.4, allowance 3.8% to 2.1%, contract assets +142%, Norvale 38% of AR | High | Found | FIN-04, SEC-07, X-03 | High | Yes | All elements present across FIN-04 and SEC-07. |
| P04 | Cash conversion collapse: OCF 40.8 to 9.7, FY2025 FCF -10.1, H1 2026 OCF -4.2, FCF -13.0 | High | Found | FIN-05, SEC-32, X-07 | High | Yes | |
| P05 | Material weakness, adverse ICFR, not remediated; auditor dismissed after flagging expanded Q4 procedures; small regional replacement | Critical or High | Found | X-04, SEC-03, NEWS-03 | High | Yes | "Small regional firm" is in NEWS-03's analyst card, not in the report text. |
| P06 | CFO exit with $0.9M payment; 8-K says no disagreement vs anonymous sources (rumor) | Medium or High; rumor at Low/Medium confidence | Found | X-04, SEC-04, NEWS-04 | High | Yes | Conflict recorded in open-questions.md; dispute claim labeled rumor, confidence Low. |
| P07 | Norvale 31.1%, 38% of AR, no minimums, MSA to Sep 30, 2027, 90-day CoC termination, Kinetic Aisle, $24.6M bill-and-hold, underlying growth about 11% | Critical | Found | X-06, SEC-08, NEWS-06, FIN-07, FIN-17 | Critical | Yes | Every element present, with the named Critical test. |
| P08 | Vantor: adverse Jul 22 ruling, $96.4M expert damages, injunction on Gen-3 (about $211M), stay denied, trial Mar 2027, no accrual; 10-Q says "in discovery" | Critical | Found | X-05, X-08, LIT-01, LIT-02, FIN-19, SEC-09, SEC-20 | Critical | Yes | Disclosure-timing gap found as its own cross-source finding (X-08). |
| P09 | Cyber incident: ransomware claim, about 40 sites, no 8-K Item 1.05, $2.3M credits, $1.8M costs, Pinecrest (#4, $17.4M) sues for $12.0M vs about $1.4M cap | High | Found | X-09, NEWS-05, SEC-11, LIT-06, SEC-26 | High | Yes | Pinecrest's revenue rank stated. |
| P10 | Securities class action alleging bill-and-hold inflation; follows the short report; names CEO and former CFO | High (Medium ok) | Found | LIT-04, SEC-10, X-04 | High | Yes | |
| P11 | Adj. EBITDA quality: add-backs 35% of FY2025; restructuring every year since 2022; implementation delays an operating cost; other non-recurring 1.2 to 9.6 | High (Medium ok) | Found | X-10, FIN-03, NEWS-08, FIN-08 | High | Yes | |
| P12 | Covenant: 2.26x = 202.5 / 89.7; capped 75.9 and 2.67x; step-down to 3.00x; could approach or exceed 3.00x by year-end; CoC default, $227.5M refinanced | High | Found | X-07, FIN-14, FIN-15, SEC-05, SEC-24, SEC-06 | High | Yes | Every element present. |
| P13 | CoC costs: $28.6M payments incl. $17.6M single-trigger; landlord rent reset; no lead independent director | Medium | Found | X-14, SEC-14, SEC-15 | Medium | Yes | Lead independent director point is in SEC-16 (not verified) and the report's Q5 answer. |
| P14 | 2026 deterioration: H1 -1.7%, Q2 -4.0%, GM 40.8% to 38.0%, H1 net loss, H1 Adj. EBITDA -23%, guidance cut, backlog -22%, retention 118% to 111% | High | Found | X-02, X-01, FIN-09, FIN-10, FIN-18, NEWS-01 | Critical | Yes | Main point found; the report omits the H1 net loss of $8.9M and the reported Q2 -4.0%. |
| P15 | Deal model uses stale March case; 18.3x on guidance midpoint, not 11.5x | Critical (High ok) | Found | X-01, SEC-01, NEWS-01, FIN-01, FIN-20 | Critical | Yes | |
| P16 | Bonus at 142%; ex bill-and-hold $470.5M barely above $470.0M threshold; incentive to pull revenue forward | Medium (High ok) | Found | SEC-13, X-03 | High | Yes | Short seller's bonus claim is in the NEWS-02 analyst card. |
| P17 | Single-source LiDAR in China; tariff 7.5% to 25%; 2 to 3 point margin hit; 12 to 18 months to qualify | Medium | Found | X-13, SEC-19, NEWS-09 | Medium | Yes | |
| P18 | Goodwill $98.4M ($57.4M Lumora) last tested Oct 1, 2025, before the share price fall | Low or Medium | Partially found | SEC-18, FIN-12 | Medium (not verified) | Yes | Found in the register but never sent to the verifier, so it appears only as "not verified". The share price fall since the test date was not quantified. |

## Severity accuracy

18 / 18 = 100.0%. Every Found or Partially found issue has a highest matching severity within one level of an accepted severity. P18 is counted on its unverified register severity (Medium), because it has no verified finding.

## Unsupported findings in the report

0. The four verifier runs checked 79 register rows: 59 Verified, 20 Partially verified, 0 Not supported. The report uses the corrected wording for each partially verified finding.

## Distractors

| ID | Distractor | Run rating | Too high? |
|---|---|---|---|
| D1 | Ruiz settlement, $3.2M | Low (LIT-07, SEC-12) | No |
| D2 | Delmarco unpaid invoice, $0.4M | Low relevance, not a finding | No |
| D3 | OSHA citation, $48 thousand | Low relevance, not a finding | No |
| D4 | Scholarship article | Set aside as noise | No |

Distractors rated too high: 0 / 4.

## Planted positives

P19 appears in the report's mitigating points: FieldOS software growth, ARR ($139.2M in the metrics table, $146.8M at June 30, 2026), retention 118% slowing to 111%, and Talonfield #3 with about 11% share of a market growing about 15% a year. Not counted in recall.

## Process notes (not scored)

- Checkpoint 1: the plan summary was not printed in chat before the approval question (logged in the run log). Checkpoints 2 and 3 showed their full content.
- One verifier run's headline count (10 partially verified) did not match its own table (6).

## Three most useful improvements to the agent instructions

1. **Verify every finding the report shows, not only the ones IC answers cite.** P18 lost half a point because SEC-18 (goodwill) was Medium, not cited by an IC answer, and never sent to the verifier. Change Step 4 to send every Medium finding that will appear anywhere in the report, or require a short "not verified" spot check by the lead for each remaining Medium.
2. **Test accounting estimates against later market events.** Add a cross-source rule to Step 3: for each dated accounting judgment in the filings (impairment test date, reserve level, materiality conclusion), compare it with what happened afterwards in news or market data, and quantify the change (for example the share price fall since the October 1, 2025 goodwill test). This would have turned P18 into a full find and is general, not specific to this case.
3. **Make checkpoint content and verifier counts mechanical.** Require that each checkpoint's content is printed in chat before the question and logged as shown, and require the verifier to count its summary line from its table. Both slipped in this run without affecting recall, but both affect the audit trail the IC relies on.
