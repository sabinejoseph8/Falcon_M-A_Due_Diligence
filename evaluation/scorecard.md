# Scorecard: Project Falcon diligence run (graded run 3, blind)

- Run date: 2026-10-18 (run log `memory/run-log.md`; previous run archived to `runs/2026-10-18_1336/` before this run)
- Graded: 2026-10-18 against `evaluation/answer-key.md` (18 planted issues, 1 planted positive, 4 distractors)
- Inputs graded: `memory/findings.md` (89 findings: 64 verified or partially verified, 25 not verified), `memory/analyst-reports/verification_citation-verifier.md`, `output/Project-Falcon-Due-Diligence-Report.md`
- Setup: frozen (no edits to CLAUDE.md, `.claude/`, `tests/` or `data/` during the run)

## Headline scores

| Metric | Result | Target |
|---|---|---|
| Recall, overall | **17.0 / 18 = 94.4%** (16 Found, 2 Partially found, 0 Missed) | High |
| Recall, Critical and High issues (13) | **13.0 / 13 = 100%** | 100% |
| Recall, Critical (3: P07, P08, P15) | 3.0 / 3 = 100% | |
| Recall, High (10: P01 to P05, P09 to P12, P14) | 10.0 / 10 = 100% | |
| Recall, Medium (4: P06, P13, P16, P17) | 3.5 / 4 = 87.5% | |
| Recall, Low or Medium (1: P18) | 0.5 / 1 = 50% | |
| Severity accuracy (found or partially found issues within one level) | **18 / 18 = 100%** | 100% |
| Unsupported findings that reached the report | **0** (verifier: 49 Verified, 15 Partially verified with corrected wording used, 0 Rejected) | 0 |
| Distractors rated Medium or above | **0 / 4** | 0 |
| Planted positive (P19) shown as a mitigating point | Partially (software growth, ARR and market growth appear inside X-06 and the Q1 answer, but the report has no mitigating-points section) | Yes |

Recall bands use each issue's primary expected severity in the answer key. P05 ("Critical or High") is counted as High; P06 ("Medium or High") as Medium.

## Planted issues

| ID | Planted issue (short) | Expected severity | Result | Run severity | Matching finding IDs | Notes |
|---|---|---|---|---|---|---|
| P01 | $31.8m Q4 2025 bill-and-hold; Q4 growth 5.1%, FY2025 11.6% | High (Critical ok) | Found | Critical | X-02, SEC-02, FIN-20, FIN-02 | Exact figures; cross-source link made (10-K amount applied to quarterly data). Verified. |
| P02 | $9.4m reversed in Q2 2026 with the largest customer; partly corroborates short seller | High | Found | Critical | SEC-02, SEC-22, NEWS-02, X-03 | Verifier softened NEWS-02 to "consistent with, but does not prove". Largest customer = Norvale labeled an inference. |
| P03 | Receivables quality: AR +62%, DSO 63.5 to 86.4, allowance 3.8% to 2.1%, contract assets +142%, Norvale 38% of AR | High | Found | High | FIN-05, SEC-09, NEWS-07, X-04 | All elements present across verified findings. |
| P04 | Cash conversion collapse; FCF -$10.1m FY2025, H1 2026 OCF -$4.2m, FCF -$13.0m | High | Found | High | FIN-06, SEC-09 | Verified. |
| P05 | Material weakness, adverse ICFR, unremediated; auditor dismissed after flagging it and expanded Q4 procedures | Critical or High | Found | High | SEC-03, SEC-04, SEC-23, NEWS-03, X-03 | "Small regional firm" detail in the analyst card but not in the report; minor. |
| P06 | CFO exit with $0.9m payment; 8-K says no disagreement vs anonymous dispute claim (rumor) | Medium or High | Found | High (NEWS-04), Medium (SEC-10) | NEWS-04, SEC-10, X-03 | Conflict recorded; dispute labeled rumor with Low confidence, as required. |
| P07 | Norvale 31.1%, 38% AR, no minimums, MSA to Sept 2027, change-of-control exit, Kinetic Aisle, $24.6m bill-and-hold, underlying growth about 11% | Critical | Found | Critical | X-04, SEC-06, NEWS-05, FIN-08, FIN-22, SEC-22 | Every element present and combined in one X- finding. |
| P08 | Vantor: Markman loss July 22, $96.4m, injunction on Gen-3 (about 70% of hardware, about $211m), stay denied, no accrual; 10-Q silent on the ruling | Critical | Found | Critical | X-05, LIT-F01 to LIT-F05, SEC-07, SEC-20, SEC-21 | Disclosure-timing gap found in iteration 2 by a targeted follow-up. |
| P09 | Cyber incident: ransomware claim, 40 sites, no 8-K 1.05, $2.3m credits, $1.8m costs, Pinecrest (#4, $17.4m) sues for $12.0m vs about $1.4m cap | High | Found | High (NEWS-06), Medium (X-09, LIT-F08) | NEWS-06, X-09, LIT-F08, SEC-08, X-11, FIN-24 | All facts present. The combined X-09 was rated Medium; NEWS-06 carries High. |
| P10 | Securities class action on bill-and-hold; follows short report; names CEO and former CFO | High (Medium ok) | Found | High | LIT-F06, LIT-F07, SEC-07 | Allegations labeled. |
| P11 | Add-backs 35% of FY2025; restructuring every year; implementation delays; other non-recurring 1.2 to 9.6 | High (Medium ok) | Found | High | FIN-04, X-08, NEWS-08 | The growth of "other non-recurring items" is not called out explicitly; main point found. |
| P12 | Covenant 2.26x = 202.5 / 89.7 uncapped; 2.67x under 15% cap; 3.00x step-down; change-of-control default, $227.5m refinance | High | Found | High | X-07, SEC-15, SEC-16, SEC-17, FIN-18, FIN-19, SEC-06, X-12 | Exact match, including the back-solve. Also tested the stricter 3.65x reading. |
| P13 | $28.6m change-in-control payments incl. $17.6m single-trigger; CEO family landlord rent reset; no lead independent director | Medium | Found | Medium | SEC-10, SEC-12 | Verified (SEC-12 corrected to "controlled by Mr. Hale and his family"). |
| P14 | 2026 deterioration: H1 -1.7%, Q2 -4.0%, GM 40.8% to 38.0%, net loss, H1 Adj. EBITDA -23%, guidance cut, backlog -22% at FY2025, NRR 118% to 111% | High | Found | High | X-06, FIN-03, FIN-10, SEC-09, NEWS-01, SEC-01 | Trend combined in one X- finding. H1 Adj. EBITDA -23% not stated as a headline number. |
| P15 | Deal model uses stale March case; 18.3x guidance EBITDA, not 11.5x | Critical (High ok) | Found | Critical | X-01, SEC-01, NEWS-01, FIN-01, FIN-25 | Top red flag in the report. |
| P16 | Bonus at 142%; revenue ex bill-and-hold $470.5m vs $470.0m threshold | Medium (High ok) | Found | High (FIN-21), Medium (SEC-11) | FIN-21, SEC-11, X-03 | Run also found the Adjusted EBITDA threshold would be missed (margin assumed). |
| P17 | Single-source China LiDAR; tariff 7.5% to 25%; 2 to 3 point margin hit; 12 to 18 months to requalify | Medium | Partially found | Medium | SEC-13, NEWS-09 | Both halves found by separate analysts, but never combined into an X- finding and not verified, so only in the report's "not verified" list. |
| P18 | Goodwill $98.4m last tested Oct 1, 2025, before share price fell about 44% | Low or Medium | Partially found | Low / Medium | SEC-13, FIN-15 | Impairment risk noted after the guidance cut; the share price decline link was not made. Not verified. |

## Planted positive

| ID | Positive | Result | Where |
|---|---|---|---|
| P19 | FieldOS ARR $139.2m (+27%), retention 118% slowing to 111%, software 25.6% of revenue; #3 with about 11% share of a market growing about 15% | Partially shown | Analyst reports list these as positives; the report mentions software and services growth, ARR and the 15% market only inside X-06 and the Q1 answer. No explicit mitigating-points section. |

## Distractors

| ID | Distractor | Run rating | Too high? |
|---|---|---|---|
| D1 | Ruiz settlement $3.2m | Low (LIT-F09, not verified); included only as a debt-like item in the closing cash bridge (X-12) | No |
| D2 | Delmarco $0.4m | Low, listed as closed in the litigation table | No |
| D3 | OSHA $48 thousand | Low, listed as closed | No |
| D4 | Scholarship article | Low (NEWS-13), no related-party angle found | No |

## Unsupported findings

None reached the report. The verifier checked 64 findings (all 53 Critical and High plus 11 Medium) and rejected none. All 15 Partially verified findings appear in the report with the verifier's corrected wording, including two material corrections the analysts got wrong: the closing cash bridge ($263.5m overstated to $234.9m gross after removing single-trigger equity) and adjusted H1 2026 revenue (234.3, not 233.9). The 25 unverified findings are labeled "not verified" in the appendix.

## Three most useful improvements to the agent instructions

1. **Make the lead pair up Medium findings across sources before verification.** P17 was missed only because the SEC analyst's single-source LiDAR disclosure (SEC-13) and the news analyst's tariff proposal (NEWS-09) were never combined. Add to Step 3: "Before Checkpoint 2, scan every Medium finding for a partner finding from another source on the same topic; combine pairs into an `X-` finding and send all `X-` findings to the verifier." This would also have caught P18 (goodwill plus share price fall).
2. **Add a required "Mitigating points" subsection to the report template.** All four analysts listed positives (FieldOS ARR and retention, market share and market growth, collections recovering), but the template has no place for them, so they were scattered. Add under the executive summary or each workstream: "Positive and mitigating points, each with a finding ID or source citation."
3. **Add a "stale tests and dates" check to the lead's cross-source analysis.** List every point-in-time test or estimate in the filings (goodwill impairment test date, credit-loss allowance, covenant compliance, guidance date, deal model date) and compare each with later events in other sources (share price moves, guidance cuts, court rulings). This run did it well for the deal model and the 10-Q, but not for the goodwill test (P18). Also ask the trend `X-` finding to state headline EBITDA and net loss changes (for example H1 Adjusted EBITDA -23%).
