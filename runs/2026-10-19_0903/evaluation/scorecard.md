# Scorecard: graded run 6 (Project Falcon)

Graded: 2026-10-19. Sources: `evaluation/answer-key.md`, `memory/findings.md`, `memory/analyst-reports/verification_summary.md`, `output/Project-Falcon-Due-Diligence-Report.md`. Graded from this run's files only.

## Headline

| Measure | Result |
|---|---|
| Recall, overall | 18 / 18 = 100.0% |
| Recall, Critical and High group | 13 / 13 = 100.0% |
| Severity accuracy | 18 / 18 = 100.0% |
| Unsupported findings in the report | 0 (target 0) |
| Distractors rated too high | 0 of 4 (target 0) |
| Planted positives (P19) | Mostly present |

## Recall by severity group

Groups use the first-listed expected severity in the answer key.

| Group | IDs | Score |
|---|---|---|
| Critical | P05, P07, P08, P15 | 4 / 4 = 100.0% |
| High | P01, P02, P03, P04, P09, P10, P11, P12, P14 | 9 / 9 = 100.0% |
| Critical and High | P01, P02, P03, P04, P05, P07, P08, P09, P10, P11, P12, P14, P15 | 13 / 13 = 100.0% |
| Medium | P06, P13, P16, P17 | 4 / 4 = 100.0% |
| Low | P18 | 1 / 1 = 100.0% |
| Overall | P01 to P18 | 18 / 18 = 100.0% |

Denominator check: 4 + 9 + 4 + 1 = 18; Critical and High = 4 + 9 = 13.

## Planted issues

| ID | Planted issue | Result | Matching finding IDs | Highest severity in run | Accepted severity | Severity OK |
|---|---|---|---|---|---|---|
| P01 | $31.8M Q4 2025 bill-and-hold; ex B&H Q4 +5.1%, FY2025 +11.6% | Found | X-02, SEC-02, FIN-16 | High | High (Critical ok) | Yes |
| P02 | $9.4M reversed in Q2 2026 with the largest customer; corroborates short seller | Found | SEC-03, FIN-17, NEWS-02, X-02 | High | High | Yes |
| P03 | AR +62%, DSO 63.5 to 86.4, allowance 3.8% to 2.1%, contract assets +142%, Norvale 38% of AR | Found | FIN-05, SEC-09, SEC-26, X-08, FIN-18 | High | High | Yes |
| P04 | OCF $40.8M to $9.7M; FCF -$10.1M; H1 2026 OCF -$4.2M, FCF -$13.0M | Found | FIN-06, SEC-08 | High | High | Yes |
| P05 | Material weakness, adverse ICFR, unremediated; auditor dismissed after flagging Q4; small regional replacement | Found | X-06, SEC-04, SEC-05, NEWS-04 | High | Critical or High | Yes |
| P06 | CFO exit, $0.9M payment, 8-K "no disagreement" vs rumored dispute (labeled rumor, Low confidence) | Found | NEWS-05 (confidence Low), SEC-14, X-06 | High | Medium or High | Yes |
| P07 | Norvale 31.1%, 38% of AR, no minimums, MSA to Sep 30, 2027, CoC termination, Kinetic Aisle, underlying growth about 11% | Found | X-04, SEC-10, FIN-03, NEWS-07, FIN-16, FIN-18 | Critical | Critical | Yes |
| P08 | Vantor: adverse Jul 22 ruling, $96.4M expert, Gen-3 injunction (about $211M), stay denied, no accrual; 10-Q silent on ruling | Found | X-05, LIT-01, LIT-02, SEC-23, SEC-28 | Critical | Critical | Yes |
| P09 | Cyber: ransomware claim, about 40 sites, no Item 1.05, $2.3M credits, $1.8M costs; Pinecrest #4 ($17.4M) sues $12.0M, gross negligence vs $1.4M cap | Found | X-07, NEWS-06, SEC-24, SEC-13, LIT-06 | High | High | Yes |
| P10 | Securities class action on bill-and-hold; follows short seller; names CEO and former CFO | Found | SEC-12, LIT-04, LIT-05 | High | High (Medium ok) | Yes |
| P11 | Add-backs 35% of FY2025 Adj. EBITDA; restructuring every year; implementation delays; other items $1.2M to $9.6M | Found | X-10, FIN-04, NEWS-08, FIN-13 | High | High (Medium ok) | Yes |
| P12 | 2.26x uses full Adj. EBITDA; capped about 2.67x; step-down to 3.00x; may exceed by YE2026; CoC default, $227.5M | Found | X-03, FIN-14, FIN-15, SEC-06, SEC-07 | High | High | Yes |
| P13 | $28.6M CoC payments ($17.6M single-trigger); CEO-family landlord rent reset; no lead independent director | Found | SEC-16, SEC-17 (SEC-18 Low, not verified) | Medium | Medium | Yes |
| P14 | 2026 deterioration: H1 -1.7%, Q2 -4.0%, GM 40.8% to 38.0%, H1 net loss, guidance cut, backlog fall, NRR 118% to 111% | Found | X-11, FIN-02, FIN-08, FIN-09, SEC-01 | High | High | Yes |
| P15 | Stale March case; EV $1,352.8M is about 18.3x guidance midpoint, not 11.5x | Found | X-01, SEC-01, NEWS-01, FIN-01 | Critical | Critical (High ok) | Yes |
| P16 | Bonus at 142%; revenue ex B&H $470.5M vs $470.0M threshold; short seller similar claim | Found | SEC-15, X-06, NEWS-02 | High (via X-06); SEC-15 Medium | Medium (High ok) | Yes |
| P17 | Single LiDAR supplier in China; tariff 7.5% to 25%; 2 to 3 point margin hit; 12 to 18 months to requalify | Found | X-13, SEC-20, NEWS-10 | Medium | Medium | Yes |
| P18 | Goodwill $98.4M ($57.4M Lumora) tested Oct 1, 2025, before share price fall and weaker results | Found | X-09, SEC-19, SEC-25, FIN-11 | Medium | Low or Medium | Yes |

Notes on grading judgment:
- P13: the main points (payouts, single-trigger equity, rent reset) are in verified Medium findings. The "no lead independent director" detail sits in SEC-18 (Low, not verified) and appears in the report only in the appendix list of unverified findings. Graded Found on the main point.
- P14: "H1 Adjusted EBITDA down 23%" is not stated as a percentage (the report gives the margin, 13.4% vs 17.2%), and the "backlog fell 22% at FY2025 despite record Q4" pull-forward signal is in the FIN-08 card but the report quotes the 29.8% fall from Dec 31, 2024 instead. Core points present; graded Found.

## Distractors

| ID | Distractor | Rating in run | Too high? |
|---|---|---|---|
| D1 | Ruiz settlement $3.2M | SEC-22 Low, LIT-07 Low | No |
| D2 | Delmarco $0.4M | Low (litigation report "low relevance"; no register finding above Low) | No |
| D3 | OSHA $48 thousand | Low (litigation report "low relevance") | No |
| D4 | Scholarship article | Set aside as "no diligence relevance" | No |

## Unsupported findings

Zero. The verifier marked no finding Not supported (78 checked: 50 Verified, 28 Partially verified, 0 Rejected). All 28 Partially verified findings were rewritten with corrected wording before the report.

## Planted positives

P19 is mostly present: ARR rising to $146.8M, software revenue +14.6% in H1 2026, NRR at 111%, #3 position with about 11% share of a market growing about 15% a year. Not in the report text: FY2025 ARR growth of +27% and software at 25.6% of FY2025 revenue.

## Three most useful improvements to the agent instructions

1. **Share cross-workstream facts in iteration 1.** The covenant definition (10-K Note 9) was needed by the financial analyst but only reached it in iteration 2, which cost an iteration and a usage-limit interruption. Ask the SEC analyst's standard output for a short "facts other analysts need" section (covenant formulas, one-off revenue amounts, named customers), and have the lead forward it in the same Observe step.
2. **Stop analysts rating projections Critical.** The financial analyst rated a projected covenant breach Critical (FIN-15), and the verifier had to downgrade it. Add to the shared rubric that a projection or a party's claimed amount cannot by itself meet the Critical test; the analyst should state "Critical if confirmed by X" and rate High.
3. **Self-check the report against the register before converting.** A few verified details stayed in finding cards and did not reach the report text (FY2025 ARR growth and software share for the positives; H1 Adjusted EBITDA decline; the year-end backlog fall as a pull-forward signal). Add a Step 5 check: for every parent finding and the positives, confirm the headline numbers from the register appear in the report.
