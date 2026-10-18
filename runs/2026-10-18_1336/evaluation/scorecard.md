# Scorecard: Project Falcon diligence run (graded run 2)

- Run date: 2026-10-18 (memory/ and output/ as of the Step 5 report)
- Graded: 2026-10-18 by /evaluate against `evaluation/answer-key.md`
- Inputs: `memory/findings.md` (85 findings), `output/Project-Falcon-Due-Diligence-Report.md`, verifier reports in `memory/analyst-reports/verification_citation-verifier.md`

## Headline results

| Measure | Result | Target |
|---|---|---|
| Recall, all 18 planted issues | 16.5 / 18 = **91.7%** (15 Found, 3 Partially found, 0 Missed) | High |
| Recall, Critical and High issues (14: P01-P05, P07-P12, P14, P15) | 13.5 / 14 = **96.4%** | High |
| Recall, Critical issues only (P07, P08, P15) | 3 / 3 = **100%** | 100% |
| Recall, Medium and Low issues (5: P06, P13, P16, P17, P18) | 4.0 / 5 = **80.0%** | |
| Severity accuracy (within one level) | 18 / 18 = **100%** | High |
| Unsupported findings that reached the report | **0** (66 verified: 46 Verified, 20 Partially verified with corrected wording, 0 Rejected) | 0 |
| Distractors rated Medium or above | **0 of 4** | 0 |
| Planted positives (P19) shown as mitigating | Yes, mostly (software share of revenue not stated) | Yes |

Recall uses Found = 1, Partially found = 0.5, Missed = 0. Issues with a two-level expected severity are grouped by their first-listed level, except P06 ("Medium or High"), which is grouped with Medium.

**Builder note:** the Critical and High line above divides by 14, but its own list has 13 issues (P01 to P05, P07 to P12, P14, P15). The correct figure is 12.5 / 13 = 96.2%.

## Planted issues

| ID | Planted issue (short) | Expected severity | Result | Run severity | Matching finding IDs | Notes |
|---|---|---|---|---|---|---|
| P01 | $31.8 bill-and-hold; Q4 growth about 5.1%, FY2025 about 11.6% | High (Critical ok) | Found | Critical | X-03, SEC-02, FIN-15, FIN-01 | All figures match (122.6 vs 116.6; 470.5 vs 421.7; 20.6% of Q4). Cross-source done. |
| P02 | $9.4 reversed in Q2 2026; partly corroborates short seller | High | Found | High / Critical | SEC-19, NEWS-02, NEWS-03, X-01 | Link to Greyfin stated as "consistent with, but does not confirm" after verifier correction. |
| P03 | Receivables quality (AR +62%, DSO 63.5 to 86.4, allowance 3.8% to 2.1%, contract assets +142%, Norvale 38% of AR) | High | Found | High | FIN-04, SEC-09, SEC-07, X-01 | All elements present. |
| P04 | Cash conversion collapse (OCF 40.8 to 9.7; FCF -10.1; H1 2026 OCF -4.2, FCF -13.0) | High | Found | High | FIN-05, SEC-09 | All elements present. |
| P05 | Material weakness, adverse ICFR, unremediated; auditor dismissed after flagging; small regional replacement | Critical or High | Found | High | SEC-04, SEC-05, NEWS-04, X-01 | "Small firm" is in NEWS-04; the report body does not repeat the "fewer than ten listed clients" detail. |
| P06 | CFO exit, $0.9 payment, "no disagreement" vs rumored dispute (conflict; rumor at Low/Medium confidence) | Medium or High | Found | High | SEC-06, NEWS-05 | Conflict recorded in open-questions and report section 6; dispute labeled rumor, Low confidence. |
| P07 | Norvale concentration, no minimums, MSA to Sept 30, 2027, change-of-control termination, Kinetic Aisle, underlying growth about 11% | Critical | Found | Critical | X-05, SEC-07, SEC-20, FIN-07, FIN-22, NEWS-06 | Underlying Norvale growth 11.4% computed. |
| P08 | Vantor: adverse July 22 ruling, $96.4 expert damages, injunction on Gen-3 (about $211), stay denied, no accrual; 10-Q omits the ruling | Critical | Found | Critical | X-06, SEC-18, SEC-10, LIT-01, LIT-02, LIT-03, LIT-09 | Disclosure timing gap confirmed in iteration 2. |
| P09 | Cyber incident: ransomware claim, about 40 sites, no Item 1.05, $2.3 credits, $1.8 response, Pinecrest (#4 customer, $17.4 revenue) sues for $12.0 vs about $1.4 cap | High | Partially found | High | X-07, NEWS-07, SEC-11, SEC-21, LIT-07, LIT-08 | Everything found except the cross-source link that Pinecrest is the #4 customer with $17.4 of FY2025 revenue (`revenue_by_customer.csv`). The customer-retention angle is missing. |
| P10 | Securities class action, bill-and-hold allegations, after short seller, names CEO and former CFO | High (Medium ok) | Found | High | LIT-05, SEC-11, X-01 | Labeled as allegation. |
| P11 | Adj. EBITDA quality: add-backs 35% of FY2025; restructuring every year; implementation delays $4.1; other non-recurring 1.2 to 9.6 | High (Medium ok) | Found | High | FIN-03, X-11, NEWS-08 | Main points present. The "other non-recurring 1.2 to 9.6" trend is in FIN-03 but not repeated in the report body. |
| P12 | Covenant: 2.26x = 202.5 / 89.7; capped about 75.9 and 2.67x; 3.00x step-down; year-end risk; $227.5 refinanced at closing | High | Found | High | X-09, FIN-19, FIN-20, SEC-08, SEC-22, X-08 | Exact match, including both readings of the SBC cap. |
| P13 | Change-of-control costs ($28.6, $17.6 single-trigger), landlord rent reset, no lead independent director | Medium | Found | Medium / High | SEC-14, X-08 | Double-trigger split of the $28.6 correctly noted. |
| P14 | 2026 deterioration (H1 -1.7%, Q2 -4.0%, GM 40.8% to 38.0%, net loss -8.9, Adj. EBITDA -23%, guidance cut, backlog -22%, NRR 118% to 111%) | High | Found | Critical | X-04, FIN-01, FIN-08, FIN-09, SEC-01 | Combined into one trend finding as instructed. The H1 Adj. EBITDA -23% is not stated explicitly. Critical is within one level. |
| P15 | Stale model; 18.3x guidance midpoint, not 11.5x | Critical (High ok) | Found | Critical | X-02, SEC-01, NEWS-01, FIN-02, FIN-21 | Exact match. |
| P16 | Bonuses at 142%; $470.5 barely above $470.0 threshold; incentive; short seller similar | Medium (High ok) | Found | High / Medium | X-10, SEC-13, NEWS-03 | Verifier sharpened the logic (missed the $490.0 target). |
| P17 | Single-source China LiDAR; tariff 7.5% to 25%; 2-3 pt margin; 12-18 months to requalify | Medium | Partially found | Medium | SEC-16, NEWS-10 | Both halves found by separate analysts, but never combined into an X- finding and never verified; appears only in the "not verified" list. |
| P18 | Goodwill impairment risk: $98.4 ($57.4 Lumora) last tested Oct 1, 2025, before share price fell about 44% and results weakened | Low or Medium | Partially found | Medium | SEC-24, FIN-13 | Found from the filings (no interim test after guidance cut), but not linked to the share price fall; not verified. |

## Distractors

| ID | Distractor | Run rating | Result |
|---|---|---|---|
| D1 | Ruiz settlement $3.2 | Low (SEC-17; litigation matter table) | Correct |
| D2 | Delmarco $0.4 | Low (litigation matter table) | Correct |
| D3 | OSHA $48 thousand | Low (litigation matter table) | Correct |
| D4 | Scholarship article | Set aside as noise; no finding | Correct |

## Planted positive

P19 is shown as mitigating in the report (Q1 answer, X-04 offsets, workstream 5.2): FieldOS growth (+27.1% FY2025, +14.6% H1 2026), ARR to $146.8, NRR 118% to 111%, #3 with about 11% share in a market growing about 15% a year. Software's 25.6% share of FY2025 revenue is not stated.

## Unsupported findings check

- All 58 Critical and High findings and 8 Medium findings went through four verifier runs. None was rejected.
- The 20 Partially verified findings were rewritten with the verifier's corrected wording before the report was written; a re-read of the verifier reports found no missed correction.
- The 19 unverified Medium and Low findings appear only in the appendix list, labeled "not verified", and are not relied on in the conclusions.
- Result: 0 unsupported findings in the report.

## Process observations (not scored)

- Checkpoint 2: the lead agent ended its turn on the question prompt before printing the full red-flag table; the user saw only a short summary. It was corrected later and logged.
- Verification counts were miscounted twice (63, 59) before being corrected to 58 Critical/High + 8 Medium = 66. Totals of verdicts were unaffected.

## Three most useful improvements to the agent instructions

1. **Cross-reference every named counterparty against the customer data.** Add to the Observe step: for every customer, supplier or litigant named in news or court records, look up its rank and revenue in `revenue_by_customer.csv` and state it in the finding. This would have completed P09 (Pinecrest is the #4 customer, $17.4 of revenue), turning a litigation finding into a customer-retention finding.
2. **Create X- findings for corroborated Medium issues too, and verify them.** The trend rule only combines three or more findings. Add: when two workstreams report the same fact (for example SEC-16 and NEWS-10 on LiDAR), create an X- finding at any severity and include it in verification. Also add a market-signal check: compare the share price fall since the last goodwill test against goodwill balances. This would have completed P17 and P18.
3. **Make checkpoints and counts mechanical.** Require the lead agent to print the full checkpoint content (tables, conflicts, proposal) in its message before asking the checkpoint question, and to compute register and verification counts with a script over `memory/findings.md` rather than by hand. This addresses the Checkpoint 2 slip and the miscounts in this run without changing analysis quality.
