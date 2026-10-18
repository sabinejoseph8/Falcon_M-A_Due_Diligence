# Answer key: issues planted in the Project Falcon data

> Used only by `/evaluate`. The lead agent and the analysts must not read this file during a diligence run.

The fictional data contains 18 planted issues, 1 set of planted positives and 4 distractors. Issues marked **Cross-source** can only be fully found by combining two or more sources, which is the job of the lead agent's Observe step.

Expected severity uses the shared rubric. A finding counts as correctly rated if it is within one level of the expected severity, unless a single level is required.

## Planted issues

| ID | Planted issue | Where the evidence is | Expected severity | Cross-source |
|---|---|---|---|---|
| P01 | Q4 2025 included $31.8M of bill-and-hold revenue (20.6% of Q4, 6.3% of FY2025). Excluding it, Q4 growth was about 5.1% (122.6 vs 116.6) and FY2025 growth about 11.6% (470.5 vs 421.7), not 19.1%. | 10-K Note 2; `revenue_quarterly.csv`; `income_statement.csv` | High (Critical acceptable) | Yes |
| P02 | $9.4M of the Q4 2025 bill-and-hold revenue was reversed in Q2 2026 after the products were returned to inventory under a contract amendment with the largest customer. This partly corroborates the short seller's allegation. | 10-Q MD&A; news 2026-05-12 and 2026-08-07 | High | Yes |
| P03 | Receivables quality: net AR up 62% vs revenue up 19%; DSO 63.5 to 86.4 days; allowance cut from 3.8% to 2.1% of gross AR while AR grew; contract assets up 142%; Norvale 38% of gross AR. | `balance_sheet.csv`; `income_statement.csv`; 10-K Notes 5 and 13 | High | Partly |
| P04 | Cash conversion collapsed: operating cash flow fell from $40.8M to $9.7M while net income rose; FY2025 free cash flow was negative $10.1M; H1 2026 operating cash flow negative $4.2M and free cash flow negative $13.0M. | `cash_flow.csv` | High | No |
| P05 | Material weakness over hardware revenue recognition (including bill-and-hold), adverse internal control opinion, still not remediated at June 30, 2026. The previous auditor was dismissed in November 2025 after flagging the weakness and saying it would need expanded procedures for Q4 deals; the replacement is a small regional firm. | 8-K 2025-11-14; 10-K Item 9A; 10-Q Item 4; news 2025-11-18 | Critical or High | Partly |
| P06 | CFO resigned in January 2026 with an unusual $0.9M separation payment for a voluntary resignation. The 8-K says there was no disagreement; anonymous sources say there was a dispute over Q4 revenue timing. This is a conflict between sources, and the dispute claim is a rumor. | 8-K 2026-01-21; DEF 14A; news 2026-01-23 | Medium or High (dispute claim must be labeled Low or Medium confidence) | Yes |
| P07 | Customer concentration and termination risk: Norvale was 31.1% of FY2025 revenue and 38% of AR, has no minimum volumes, its MSA expires September 30, 2027, and it can terminate on 90 days' notice after a change of control. Norvale bought Kinetic Aisle to build its own robots. $24.6M of the bill-and-hold revenue was Norvale's, so Norvale's underlying growth was about 11%, not 32%. | 10-K Items 1 and 1A, Notes 2 and 13; `revenue_by_customer.csv`; news 2026-06-24 | Critical | Yes |
| P08 | Vantor patent case: the July 22, 2026 claim construction order went against Talonfield on the key term; the plaintiff's expert calculates $96.4M in damages; Vantor will seek an injunction on Gen-3 robots (about 70% of hardware revenue, roughly $211M in FY2025); stay denied; trial March 2027; no accrual. The 10-Q filed August 6, 2026 says only that the case "is in discovery" and does not mention the July 22 ruling. | LIT-001; 10-K Items 1 and 3; 10-Q Part II Item 1 | Critical | Yes |
| P09 | April 2026 cyber incident: ransomware group claimed data theft; about 40 customer sites down for up to 3 days; no 8-K Item 1.05 filed; $2.3M of service credits and $1.8M of response costs; Pinecrest (the #4 customer, $17.4M of FY2025 revenue) sued for $12.0M and argues gross negligence to get around the roughly $1.4M liability cap. | News 2026-04-14; 10-Q; LIT-004; `revenue_by_customer.csv` | High | Yes |
| P10 | Securities class action filed June 2026 alleging revenue was inflated through bill-and-hold sales; follows the short seller report; names the CEO and former CFO. | LIT-003; news 2026-05-12; 10-Q | High (Medium acceptable) | Partly |
| P11 | Adjusted EBITDA quality: add-backs were 35% of FY2025 Adjusted EBITDA (34.7 of 98.8); restructuring has been added back every year since 2022; "customer implementation delays" ($4.1M) looks like a normal operating cost; "other non-recurring items" grew from $1.2M to $9.6M. | `adjusted_ebitda_reconciliation.csv`; news 2026-07-30 | High (Medium acceptable) | No |
| P12 | Covenant: the 10-Q reports leverage of 2.26x, which equals 202.5 / 89.7 using full Adjusted EBITDA. Under the credit agreement definition (add-backs capped at 15%), covenant EBITDA is about 75.9 and leverage about 2.67x. The maximum steps down to 3.00x from September 30, 2026, and on the revised guidance the ratio could approach or exceed 3.00x by year-end 2026. A change of control is an event of default, so about $227.5M of debt must be refinanced at closing. | 10-K Note 9; 10-Q; `adjusted_ebitda_reconciliation.csv`; `balance_sheet.csv` | High | Yes |
| P13 | Change-of-control costs and conflicts: $28.6M of executive change-in-control payments, including $17.6M of single-trigger equity acceleration; the CEO's family-owned landlord can reset headquarters rent to "fair market value" through a landlord-selected appraiser on a change of control; no lead independent director. | DEF 14A | Medium | No |
| P14 | Business deterioration in 2026: H1 revenue down 1.7% (Q2 down 4.0%); gross margin 40.8% to 38.0%; H1 net loss of $8.9M; H1 Adjusted EBITDA down 23%; FY2026 guidance cut to $470M to $490M revenue and $70M to $78M Adjusted EBITDA; backlog fell 22% at FY2025 year-end despite a record Q4 (pull-forward signal); software retention fell from 118% to 111%. | 10-Q; `income_statement.csv`; `kpis.csv`; news 2026-08-07 | High | Partly |
| P15 | The deal model uses the stale March 2026 management case ($560M revenue, $118M Adjusted EBITDA). On the revised guidance midpoint ($480M, $74M), EV of about $1,352.8M implies about 18.3x FY2026E Adjusted EBITDA, not 11.5x. | `deal-brief.md`; 10-Q; news 2026-08-07 | Critical (High acceptable) | Yes |
| P16 | 2025 executive bonuses were paid at 142% of target. Without the $31.8M of bill-and-hold revenue, revenue would have been $470.5M, barely above the $470.0M threshold, which gave management an incentive to pull revenue into Q4. The short seller made a similar allegation. | DEF 14A; 10-K Note 2; news 2026-05-12 | Medium (High acceptable) | Yes |
| P17 | Single-source LiDAR supplier in China; proposed tariff increase from 7.5% to 25% (decision expected Q1 2027); estimated 2 to 3 point hit to hardware gross margin; 12 to 18 months to qualify a new supplier. | 10-K Items 1 and 1A; news 2026-09-15 | Medium | Yes |
| P18 | Goodwill impairment risk: $98.4M of goodwill (including $57.4M from Lumora) was last tested on October 1, 2025, before the share price fell about 44% from its high and 2026 results weakened. | 10-K Note 15; news on share price | Low or Medium | Partly |

## Planted positives (should appear as mitigating points)

| ID | Positive | Where |
|---|---|---|
| P19 | FieldOS software: ARR $139.2M (+27%), retention 118% (slowing to 111%), software 25.6% of FY2025 revenue; Talonfield is #3 in North America with about 11% share of a market growing about 15% a year. | 10-K; `kpis.csv`; news 2026-08-20 |

## Distractors (should be rated Low or set aside)

| ID | Distractor | Why it is minor |
|---|---|---|
| D1 | Ruiz wage-and-hour settlement, $3.2M | Settled and already accrued |
| D2 | Delmarco unpaid invoice case, $0.4M | Closed in 2025 |
| D3 | OSHA citation, $48 thousand | Closed and paid |
| D4 | Robotics scholarship article | No diligence relevance |

## Scoring rules

- **Recall:** Found = 1, Partially found = 0.5, Missed = 0. Report overall and for Critical and High issues.
- **Severity accuracy:** share of found issues rated within one level of the expected severity (or at the required level where only one is acceptable).
- **Unsupported findings in the report:** count of report findings the sources do not support. Target: 0.
- **Distractors rated too high:** count of distractors rated Medium or above. Target: 0.
