# Project Kestrel: Scorecard

Run graded: the blind run of 2026-10-19 (target `kestrel`, report `output/Project-Kestrel-Due-Diligence-Report.md`, register `memory/findings.md`). Graded with the fixed rules in `/evaluate`, from this run's files only.

## Headline

| Measure | Result |
|---|---|
| Recall, overall | 17.5 / 18 = 97.2% |
| Recall, Critical and High group | 13.0 / 13 = 100.0% |
| Severity accuracy | 18 / 18 = 100.0% |
| Unsupported findings in the report | 0 (target zero) |
| Distractors rated too high | 2 of 4 (D3, D4) |

## Recall by group

| Group | IDs | Score |
|---|---|---|
| Critical and High | P01, P02, P03, P04, P05, P06, P08, P09, P10, P13, P14, P15, P16 | 13.0 / 13 = 100.0% |
| Critical | P01, P02, P03, P04 | 4.0 / 4 = 100.0% |
| High | P05, P06, P08, P09, P10, P13, P14, P15, P16 | 9.0 / 9 = 100.0% |
| Medium | P07, P11, P12, P17 | 4.0 / 4 = 100.0% |
| Low | P18 | 0.5 / 1 = 50.0% |
| Overall | P01 to P18 | 17.5 / 18 = 97.2% |

Denominator check: 13 IDs listed for Critical and High (4 + 9), 4 for Medium, 1 for Low, 18 overall.

## Planted issues

| ID | Planted issue | Group | Result | Matching finding IDs | Highest verified severity | Severity within one level? |
|---|---|---|---|---|---|---|
| P01 | FCA qui tam with DOJ intervention | Critical | Found | X-05, LIT-01, LIT-02, LIT-03, LIT-10 | Critical | Yes |
| P02 | Medicare 0419U cut not in the model | Critical | Found | X-04, NEWS-03, SEC-05, SEC-24, FIN-12, FIN-18 | Critical | Yes |
| P03 | Covenant breach at the Sep 30, 2026 test, before signing | Critical | Found | X-03, SEC-03, SEC-26, NEWS-04, FIN-16, FIN-17 | Critical | Yes |
| P04 | Recurring add-backs; debt sized on them; financing condition at risk | Critical | Found | X-01, X-02, X-12, FIN-01, FIN-02, FIN-07, FIN-10, FIN-22 | Critical | Yes |
| P05 | CID omitted from the 10-K filed 22 days later | High | Found | X-06, SEC-04, SEC-22, LIT-03, LIT-17, NEWS-06 | High | Yes |
| P06 | 14.2 one-off inflates Q4 2025 and FY2025 growth | High | Found | SEC-01, FIN-03, FIN-20, NEWS-07, X-01 | Critical | Yes |
| P07 | Collections deteriorating (DSO, denials, reserve) | Medium | Found | FIN-09, SEC-19, X-01 | High | Yes |
| P08 | Material weakness in the revenue estimate, not remediated | High | Found | SEC-06 | High | Yes |
| P09 | Veltrane (rank 2) winding down ATLAS-3 | High | Found | X-08, SEC-10, SEC-29, NEWS-05, FIN-08, FIN-21 | High | Yes |
| P10 | Orvia change-of-control termination right | High | Found | X-10, SEC-09 | High | Yes |
| P11 | Single-trigger equity, 280G gross-up, bonus on the one-off | Medium | Found | X-13, SEC-14, SEC-15, SEC-31 | Medium | Yes |
| P12 | Related-party lease above market to 2040 | Medium | Found | SEC-16, X-13 | Medium | Yes |
| P13 | Genaro patent case, trial before closing, injunction risk | High | Found | X-07, SEC-17, SEC-21, LIT-04, LIT-05, LIT-12, LIT-13 | High | Yes |
| P14 | Breach called a "network disruption"; 412,300 notified | High | Found | X-06, X-11, SEC-07, SEC-25, NEWS-08, LIT-06, LIT-14 | High | Yes |
| P15 | Short-seller allegations, labeled and partly corroborated | High | Found | NEWS-06, NEWS-07, X-05, LIT-11; report section 5 item 6 | Critical (X-05) | Yes |
| P16 | Stale deal brief; premium no longer anchored | High | Found | X-14, X-09, X-02, NEWS-02, FIN-02, LIT-09 | Critical (X-02) | Yes |
| P17 | Goodwill test of Oct 1, 2025 stale | Medium | Found | X-09, SEC-08, SEC-27, FIN-15 | High | Yes |
| P18 | Minor NC DEQ notice of violation | Low | Partially found | No register ID; noted as Low in the LIT iteration-1 report, the register note and the report (litigation table, appendix 8.3) | Low (as stated in report, not verified) | Yes |

Notes on grading calls:
- P15 is graded Found: Bearhaven's claims are labeled as allegations (NEWS-06), and the run links them to primary sources (speaker fees to the intervened Count II, the "manufactured Q4" claim to the 14.2, the CID rumor to the 10-Q and docket), with a recorded conflict on the fee level (LIT-11).
- P18 is Partially found: the matter is correctly called Low in the report, but it never received a finding ID and was not verified, so it is not a verified finding.
- Severity accuracy for P18 uses the Low severity stated in the report, since no verified finding exists. Excluding P18 gives 17 / 17 = 100.0%.

## Severity accuracy

18 / 18 = 100.0%. Every Found or Partially found issue has a highest matching severity within one level of an accepted severity. The verifier's downgrade of X-07 (Genaro) from Critical to High is within the accepted "High (Critical ok)".

## Unsupported findings

0. The verifier marked 0 of 97 findings Not supported (68 Verified, 29 Partially verified with corrected wording used in the report). No report finding failed to match its cited source.

## Distractors

| ID | Distractor | Run's rating | Too high? |
|---|---|---|---|
| D1 | Hollis wage and hour suit | Low; listed as a positive | No |
| D2 | FDA letter to Corvane Laboratories Pty Ltd | Excluded as unaffiliated; X-16 Low | No |
| D3 | 6.8 sale-leaseback gain | Bundled into FIN-13 (Medium) with the Pell Ridge acquisition; the report also lists the gain's exclusion as a positive | Yes (strict rule: Medium in the register) |
| D4 | 25% reagent tariff | NEWS-11 Medium, with its own Medium row in the risk matrix, although the Helixor protection is noted | Yes |

## Planted positives (not in recall)

| Positive | In report? |
|---|---|
| Hollis dismissed with prejudice, no appeal | Yes (executive summary) |
| Reagent prices fixed incl. tariffs through 2028 | Yes (executive summary) |
| Sale-leaseback gain correctly excluded | Yes (executive summary) |
| Term loan Oct 2029 / revolver Oct 2028, no near-term maturity | Partly: maturities appear in SEC-20 (risk matrix supporting ID) but not among the positives |
| Lab informatics retention 95% | Partly: only in the not-verified FIN-14 line in the appendix |
| Biopharma services revenue grew 2.7% in H1 2026 | No (in the analyst report, not the final report) |

## Three most useful improvements to the agent instructions

1. **Rate neutralized risks Low and list them as positives.** Add a rule to CLAUDE.md and the analyst definitions: when a source shows a risk is offset during the forecast period by a contract or an accounting treatment (for example duties borne by the supplier through 2028, or a gain excluded from EBITDA), rate it Low, put it under positive or mitigating points, and do not give it its own risk matrix row. Both distractors rated too high (D3, D4) fail this test.
2. **Give every matter its own finding ID and keep findings single-topic.** Require analysts to assign an ID to every matter they review, even Low or closed ones (for example LIT-005 and LIT-006 rows of the docket index), so Low items reach the register and can be listed as verified or not verified. Also forbid bundling a benign item with a real issue in one card (FIN-13 combined the acquisition with the sale-leaseback gain, which pulled the gain up to Medium).
3. **Use a positives checklist in the executive summary.** Ask the lead agent to check and report a fixed set of mitigants before writing the report: debt maturities, retention and churn, any segment still growing, items correctly excluded from adjusted metrics, dismissed or closed litigation, and supply protections. In this run three of six planted positives reached the summary; maturities, informatics retention and H1 biopharma growth were in the working files but not in the positives.
