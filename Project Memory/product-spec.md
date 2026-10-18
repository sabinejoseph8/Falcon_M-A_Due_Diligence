# Product Spec: Project Falcon

**Status:** Agreed, version 1.0 (October 18, 2026: you asked to proceed to the tech spec and progress plan).

## Overview

Project Falcon is an AI "due diligence team" for M&A deals. A person gives it a deal brief and a set of sources about a target company. A lead agent plans the work, four specialist agents research the sources in parallel, the lead agent connects what they find, an independent checker verifies every important claim, and the person approves the work at three checkpoints. The output is an Investment Committee-ready report.

It is also a portfolio piece. It shows that someone who does not write code can design, control and measure an agentic workflow for high-stakes work. The target company, Talonfield Systems, and all data are fictional.

## Goals

1. Cut the first pass of due diligence from weeks of manual research to one supervised session.
2. Catch the red flags that only appear when sources are combined, such as an event a company left out of its filings.
3. Keep a human in control of every important step, with a clear audit trail.
4. Prove quality with a score, not a claim, by testing against planted red flags.
5. Give hiring managers a project they can understand in two minutes and inspect in depth.

## Users

| User | What they do | Sign-in |
|---|---|---|
| **Operator** (deal team analyst or associate; you, for the portfolio) | Starts a run, answers the three checkpoints, reads the report, grades the run | Uses their own Claude Code account. No other sign-in. |
| **Decision maker** (Investment Committee member, deal lead) | Reads the report and decides | None. Receives the PDF. |
| **Portfolio reviewer** (recruiter, hiring manager, interviewer) | Reads the README, diagram, sample report and case study | None. Views the public project or the PDF. |

## User stories

**Starting a run**
- As an operator, I can start a full diligence run with one command, so I don't need to remember steps.
- As an operator, I am asked whether to continue or start fresh if a previous run exists, so I never mix two runs by accident.

**Planning and approval**
- As an operator, I see the plan (questions, hypotheses, assignments) before any research starts, so I can correct the scope early.

**Research**
- As an operator, I see which specialists are working and when each one reports, so I know the run is progressing.
- As a decision maker, I can trust that every finding names its source, so I can check anything myself.

**Reviewing red flags**
- As an operator, I see the most serious findings and the conflicts between sources at one stop, so I can decide whether to dig deeper.

**Verification and sign-off**
- As an operator, I see which findings were verified, corrected or rejected before the report is written, so nothing unsupported reaches the committee.

**The report**
- As a decision maker, I get a clear recommendation, the top red flags, answers to the committee's questions and recommended deal protections, so I can decide quickly.
- As a decision maker, I can tell facts from allegations and rumors, so I weigh them correctly.

**Status and audit**
- As an operator, I can ask for the status of a run at any time.
- As anyone reviewing the work, I can read every finding, decision and checkpoint in plain files.

**Grading and re-running**
- As an operator, I can grade a run against the answer key and see what was missed.
- As an operator, I can archive a run and start a clean one.

**Portfolio**
- As a portfolio reviewer, I can understand the problem, the architecture and the results from the README in two minutes.
- As the builder, I keep first-person interview notes that tell the story of the project.

## Functional requirements

**Running a diligence**
- **R1.** One command starts a run. If no previous run exists, it begins with the plan. If one exists, it asks whether to continue or start fresh.
- **R2.** The plan is saved before any research. It maps all six committee questions to specialists, lists 2 to 4 hypotheses, gives each specialist a task list, and states the 3-loop limit.
- **R3.** Checkpoint 1: the run stops after the plan and does nothing until the operator approves or asks for changes.
- **R4.** Four specialists (SEC filings, news and media, litigation, financial) work in parallel. Each reads only its own source.
- **R5.** While specialists work, the operator sees which ones are running and is told when each reports (loading state).
- **R6.** Every finding has an ID, a severity (Critical, High, Medium, Low), a confidence level (High, Medium, Low), a source file and section or row, and a status (Open, Verified, Partially verified, Rejected).
- **R7.** Findings are never deleted. Only their status changes.
- **R8.** Each specialist's full report is saved unedited before it is summarized.
- **R9.** The lead agent compares sources and records cross-source findings, conflicts, disclosure gaps and stale assumptions.
- **R10.** The research loop runs at most 3 times. Every extra loop is logged with its reason.
- **R11.** Checkpoint 2: the run stops and shows a table of Critical and High findings, the main conflicts and what is still open. It waits for "proceed" or "dig deeper on <topic>".
- **R12.** An independent checker verifies every Critical and High finding and at least three Medium findings, and gives each a verdict.
- **R13.** Findings judged Not supported are kept in the register but left out of the report.
- **R14.** Checkpoint 3: the run stops and shows the verification results and the draft recommendation. It waits for approval.
- **R15.** The report has nine parts: cover, executive summary, answers to the six questions, risk matrix, workstream detail, cross-source insights, deal protections, open questions, appendix.
- **R16.** The report is saved as Markdown, as a web page and, when the computer has a PDF tool, as a PDF. Without a PDF tool, the operator is told how to save the web page as a PDF (error state).

**Status, grading and reset**
- **R17.** A status command shows the current step, loops used, findings by severity and status, and the top open questions. With no run, it says so (empty state).
- **R18.** A grading command scores the latest run: recall overall and for Critical and High issues, severity accuracy, unsupported findings and distractors rated too high. It asks permission before opening the answer key. With no run, it tells the operator to run a diligence first (empty state).
- **R19.** A reset command archives the current run with a date and time, and restores blank working memory. It never changes the sources, the answer key or the setup.

**Safety and quality**
- **R20.** The agents cannot use the web and cannot change source files.
- **R21.** The specialists can only read files.
- **R22.** Allegations and rumors are always labeled as such.
- **R23.** If a specialist fails or returns findings without sources, the lead agent asks again once. If that fails, the gap is recorded as an open question (error state).
- **R24.** If a source file is missing or empty, the specialist reports it under "Files reviewed" and as a gap (error state).
- **R25.** All outputs use plain English, US$ millions with one decimal place, and no em dashes.

**Portfolio**
- **R26.** The project includes a README with the problem, the architecture diagram, how a run works, sample results and how to run it.
- **R27.** The project includes a complete sample run: working memory, report PDF and scorecard.
- **R28.** The project keeps `interview-notes.md` in first person, updated after significant features, major bug fixes and meaningful design changes.

## Layout and responsiveness

- **Desktop:** runs happen in Claude Code in a terminal. Checkpoint messages fit in a normal terminal window, with tables of no more than 5 columns.
- **Report (PDF):** US Letter, portrait, printable in color or black and white. Tables repeat their header row across pages.
- **Report (web page):** readable on a phone. Text reflows, and wide tables scroll sideways instead of shrinking.
- **README and diagram:** read well on GitHub on desktop and phone. The diagram is legible when zoomed on a phone.

## Out of scope for v1

- Live connections to real sources (SEC EDGAR, news services, court systems, data rooms).
- Real client or real company data.
- A custom web app or dashboard.
- Several people working on one run at the same time.
- A full valuation model (for example a discounted cash flow model).
- Legal, accounting or investment advice.
- Scheduled or continuous monitoring of a target.

## Future features (and what v1 does to leave room)

| Future feature | What v1 does now |
|---|---|
| Real sources through connectors | Each source sits behind one specialist and one folder, so a source can be swapped without changing the others. |
| More specialists (tax, people, IP, ESG) | Every specialist uses the same finding format and rubrics. |
| Several deals at once | The deal brief is a single file, and each run is archived separately. |
| Excel data pack for the committee | Key numbers are already collected in one working dataset. |
| Better scores over time | The grading command and answer key make improvements measurable. |

## Success criteria (checkable by using it)

1. An operator can finish a full run with three replies (approve, proceed, approve report) in under 45 minutes.
2. Every run stops at all three checkpoints and does nothing until the operator replies.
3. The report contains all nine parts, and every finding in it names a source.
4. Grading the sample run shows: at least 80% recall on Critical and High issues, zero unsupported findings in the report, and zero distractors rated Medium or above. (Default targets.)
5. No source file changes during a run.
6. A reviewer can explain the project after two minutes with the README.

## Decisions

| Date | Decision |
|---|---|
| 2026-10-17 | Build with Claude Code features only. No Agent SDK and no application code. |
| 2026-10-17 | Use Claude Code rather than Cowork or Managed Agents (control, readability, and the data-retention options for real client data). |
| 2026-10-18 | Use a fictional public company (Talonfield Systems) with simulated sources and planted red flags. |
| 2026-10-18 | Organize specialists by source to match the architecture: SEC filings, news, litigation, financials. |
| 2026-10-18 | Three mandatory human checkpoints and a 3-loop limit. |
| 2026-10-18 | Add an independent citation checker and an answer key with a grading command. |
| 2026-10-18 | Keep first-person interview notes for the project story. |

## Open questions (with recommended defaults)

1. **Should `interview-notes.md` be public?** Recommended default: no. Keep it out of the public project, because it is your interview preparation.
2. **Where will the portfolio live?** Recommended default: a public GitHub repository, plus the one-page case study PDF to attach to applications.
3. **Which roles is it aimed at?** Recommended default: both AI product roles and M&A or finance roles, with the README leading on the problem and the results.
