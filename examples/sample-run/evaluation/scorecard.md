# Scorecard: sample run of October 18, 2026

Graded with the `/evaluate` rules against `evaluation/answer-key.md`: 18 planted issues, 1 set of planted positives and 4 distractors. The answer key was opened only after the report was final.

## Read this first: how blind was this run?

- **The analysts and verifiers were blind. The lead agent was not.** The same Claude Code session that wrote the fictional data, the answer key and `CLAUDE.md` then acted as the lead agent. The 10 subagent runs (4 analysts, 2 follow-ups, 4 verifiers) started with fresh context and never saw the answer key or the build conversation. The lead agent's plan, follow-up questions and cross-source (`X-`) findings may have been helped by what the builder knew.
- **The checkpoints were approved by the builder**, not by an Investment Committee member.
- **The setup changed during the run** (all logged in `memory/run-log.md`): the iteration 1 financial analyst still had shell access, and the prompt-injection rule was added after iteration 1 had started.
- **The data is small and clean** compared with a real data room, so treat these numbers as an upper bound.
- **The real blind test** is to run `/diligence` in a fresh Claude Code session that has never seen the answer key, then `/evaluate`. That is the next step in `Project Memory/progress.md` (Phase 4).

## Summary

| Metric | Result | Target |
|---|---|---|
| Recall, all 18 planted issues | **97.2%** (17 found, 1 partially found) | |
| Recall, the 13 Critical and High issues | **100%** (13 of 13 found) | at least 80% |
| Recall, the 5 Medium and Low issues | 90% (4 found, 1 partially found) | |
| Severity accuracy | **100%** (18 of 18 within one level; 17 at an expected level) | |
| Unsupported findings in the report | **0** | 0 |
| Distractors rated too high | **0** of 4 | 0 |
| Planted positives in the report | Yes (P19, in the answer to Q1) | |

Recall counts Found as 1 and Partially found as 0.5. Critical and High issues are P01 to P05, P07 to P12, P14 and P15 (by the first severity the key lists).

## Planted issues

| ID | Planted issue | Expected severity | Result | Run's severity | Matching findings | Notes |
|---|---|---|---|---|---|---|
| P01 | Q4 2025 bill-and-hold revenue ($31.8M); growth 11.6%, not 19.1% | High (Critical acceptable) | Found | High | SEC-03, FIN-19, X-01 | Cross-source link made: the 10-K note applied to the quarterly revenue data |
| P02 | $9.4M of the bill-and-hold reversed in Q2 2026; partly corroborates the short seller | High | Found | High | SEC-04, NEWS-03, X-04 | Linked to the short seller's allegation (NEWS-02, conflict C2) |
| P03 | Receivables quality: DSO 63.5 to 86.4 days, allowance cut, contract assets up 142%, Norvale 38% of AR | High | Found | High | FIN-03, SEC-10, SEC-02, X-06 | |
| P04 | Cash conversion collapsed; free cash flow negative | High | Found | High | FIN-04, SEC-10, X-06 | The verifier corrected "negative for 18 months" to 12 months |
| P05 | Material weakness, adverse control opinion, auditor dismissed after flagging Q4 | Critical or High | Found | High | SEC-05, NEWS-05, X-07 | |
| P06 | CFO resignation with a $0.9M payment; rumored dispute over Q4 revenue (a conflict) | Medium or High; rumor at Low or Medium confidence | Found | High; rumor at Low confidence | SEC-06, NEWS-06, X-07; conflict C1 | The verifier corrected "the filing denies any disagreement" |
| P07 | Norvale: 31.1% of revenue, change-of-control termination, own robots, underlying growth about 11% | Critical | Found | Critical | SEC-02, FIN-20, NEWS-07, X-04 | |
| P08 | Vantor: adverse claim construction, $96.4M, injunction on Gen-3, 10-Q leaves out the ruling | Critical | Found | Critical | LIT-01 to LIT-03, SEC-08, SEC-20, X-02, X-03 | The 10-Q omission was confirmed in iteration 2 (SEC-20) |
| P09 | Cyber incident: no Item 1.05 8-K, credits and costs, Pinecrest suit against the cap | High | Found | High | NEWS-08, SEC-14, SEC-24, LIT-09, FIN-22, X-09 | |
| P10 | Securities class action over bill-and-hold; names the CEO and former CFO | High (Medium acceptable) | Found | High | LIT-06, LIT-07, SEC-07 | |
| P11 | Adjusted EBITDA quality: 35% add-backs, restructuring every year, implementation delays | High (Medium acceptable) | Found | High | FIN-05, NEWS-10, FIN-12 | The rise in "other non-recurring items" (1.2 to 9.6) is in FIN-05's full card |
| P12 | Covenant: 2.26x reported vs about 2.67x on the definition; 3.00x step-down; change of control is a default | High | Found | High | SEC-09, FIN-17, FIN-18, X-08; conflict C6 | The run computed 2.65x (2.67x if other income is deducted) and a 3.05x to 3.55x year-end range |
| P13 | Change-of-control payments ($28.6M), single-trigger equity, landlord rent reset, no lead director | Medium | Found | Medium | SEC-12, SEC-13, X-11 | |
| P14 | Business deterioration in 2026: revenue, margin, losses, guidance cut, backlog, retention | High | Found | Critical (guidance cut); Medium (KPIs, margin) | SEC-01, NEWS-01, FIN-02, FIN-08, FIN-10 | Spread across five findings instead of one. No finding states the H1 net loss ($8.9M) or the 23% fall in H1 Adjusted EBITDA, although both are in the financial analyst's tables |
| P15 | Deal model uses the stale March case; about 18.3x on the guidance midpoint | Critical (High acceptable) | Found | Critical | FIN-01, SEC-01, NEWS-01, FIN-23, X-05 | |
| P16 | Bonus paid at 142%; revenue barely above the threshold without bill-and-hold | Medium (High acceptable) | Found | Medium and High | SEC-11, FIN-21, X-07 | |
| P17 | Single-source LiDAR supplier in China; proposed tariff increase to 25% | Medium | Found | Medium | SEC-15, NEWS-11, X-12 | |
| P18 | Goodwill impairment risk ($98.4M last tested before the share price fall) | Low or Medium | **Partially found** | Low | SEC-17, FIN-16, X-13 | Found by three agents at the right severity, but Low findings were not sent for verification and goodwill does not appear in the report |

## Planted positives

| ID | Positive | Result | Matching findings |
|---|---|---|---|
| P19 | FieldOS software: ARR $139.2M (+27%), retention slowing from 118% to 111%, 25.6% of revenue, number 3 in a market growing about 15% a year | Found, and in the report (answer to Q1) | X-15, FIN-08, NEWS-13, NEWS-14 |

## Distractors

| ID | Distractor | How the run rated it | Too high? |
|---|---|---|---|
| D1 | Ruiz wage-and-hour settlement, $3.2M | Low (LIT-11, SEC-18); "accrued and low risk" in the report | No |
| D2 | Delmarco unpaid invoice case, $0.4M | Low (litigation register, low-relevance row) | No |
| D3 | OSHA citation, $48 thousand | Low (litigation register, low-relevance row) | No |
| D4 | Robotics scholarship article | Set aside as having no relevance | No |

## Unsupported findings

- **In the report: 0.** All 61 findings sent to the citation verifier were supported: 44 verified and 17 partially verified. The 17 had their wording corrected before the report (for example "free cash flow negative for 18 months" became 12 months, and "likely before closing" became "could fall between signing and closing").
- **Unverified findings cited for context:** the report also cites 10 Medium, Low or positive findings that were not sent to the verifier (FIN-08, FIN-10, FIN-11, FIN-13, FIN-14, LIT-10, LIT-11, NEWS-10, SEC-12, X-15). The grader spot-checked each against the sources; all hold.

## Findings outside the answer key

The run also reported source-backed points the key does not list, for example:

- the deal brief quoted an October 16 share price but was dated October 12 (a real error made while building the data, caught by the SEC analyst and fixed during the run);
- what else the 10-Q leaves out: the PTAB outcome, the ransomware group's claim and Norvale's plans (SEC-21, SEC-24, SEC-25);
- a projected covenant breach at December 31, 2026 under the credit agreement definition (FIN-18);
- the sale-leak bounce in the "undisturbed" price (NEWS-12, X-14), buybacks funded with the revolver (FIN-13) and an understated share count (FIN-14).

## The three most useful improvements to the agent instructions

1. **Do not let Low findings vanish.** P18 was found three times but never reached the report, because only Critical, High and sample Medium findings are verified and the report draws on verified findings. Fix: add a short list of findings that were not verified (Medium and Low, clearly labeled "not verified") to the report appendix.
2. **Consolidate trends into one cross-source finding.** The 2026 deterioration (P14) was spread across five findings with three different severities, and the headline numbers (H1 net loss, H1 Adjusted EBITDA down 23%) never made it into a finding. Fix: when three or more findings describe the same trend, the lead agent creates one `X-` finding with the headline numbers, so the trend gets one severity and one place in the report.
3. **Apply every verifier correction before Checkpoint 3.** The lead agent corrected the cross-source rows during verification but missed 15 partially verified analyst rows until the report step. Fix: make it an explicit step to rewrite each partially verified row with the verifier's wording, then re-read the verifier reports once to confirm none was missed.

Status: improvements 1 to 3 were applied to `CLAUDE.md` after this run. They take effect from the next run.
