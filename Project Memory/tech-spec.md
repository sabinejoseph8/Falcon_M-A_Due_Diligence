# Tech Spec: Project Falcon

**Status:** Agreed, version 1.6 (October 18, 2026: instruction fixes from the graded runs and a fixed grading rule; changes are in the Decisions table).

This file holds the technical decisions and system patterns. It describes the system as built so far, and flags the risks that matter most.

## Architecture overview

Project Falcon runs inside Claude Code on the operator's computer. There is no server and no application code. The "program" is a set of plain-text files that Claude Code reads.

| Part | What it is | Where it lives |
|---|---|---|
| **Lead agent (Agent Core)** | Instructions for the main Claude Code session: the Plan, Act, Observe loop, checkpoints, report template, rubrics and guardrails | `CLAUDE.md` |
| **Specialist subagents** | Four source specialists plus a citation verifier, each with its own instructions and tool list | `.claude/agents/*.md` |
| **Commands** | One-word entry points for the operator | `.claude/commands/*.md` |
| **Guardrails** | Permission rules that Claude Code enforces (not just instructions) | `.claude/settings.json` |
| **Sources ("tools")** | One folder per source type, standing in for SEC search, a news feed, a litigation database and financial data | `data/` |
| **Working memory** | Plan, findings register, open questions, key metrics, run log, unedited analyst reports | `memory/` |
| **Report pipeline** | Markdown report, converted to a styled web page and a PDF | `output/`, `templates/report-style.css` |
| **Evaluation** | Answer key of planted issues and a grading command | `evaluation/`, `/evaluate` |
| **Automated checks** | Tests for each build phase, plus a run checker | `tests/`, `/run-tests` |
| **Archive** | Past runs and their scorecards, moved aside by `/reset-memory` | `runs/` |
| **Portfolio** | README, diagram, run guide, sample run, case study, planning files | `README.md`, `docs/`, `examples/`, `Project Memory/` |

```
Operator --/diligence--> Lead agent (CLAUDE.md) --task--> 4 specialists in parallel (read-only)
                              |    ^                                |
                              |    +---------- findings ------------+
                              v
                        memory/ (register, run log, reports) --> citation-verifier --> output/ report
                              ^
               Human checkpoints 1, 2, 3 (operator replies in the conversation)
```

## Technology choices

| Choice | Reason |
|---|---|
| Claude Code (terminal or desktop app) | Built-in subagents, commands and enforceable permissions, with no code to write or host |
| Markdown for agents, commands, memory and the report | Readable by anyone, easy to review and version |
| CSV for financial data | Opens in Excel, easy to check by hand |
| JSON for permission settings | The format Claude Code requires |
| Python 3, standard library only, for automated checks | Nothing to install on Mac or Linux; deterministic results |
| Pandoc and a headless browser for the PDF (optional) | Best-looking output when available; the web page plus "Print, then Save as PDF" works everywhere. On the builder's Mac, headless Google Chrome (`--headless=new --print-to-pdf`) made the PDF with nothing installed |
| SVG for the architecture diagram, exported to PNG and PDF | Sharp at any size and easy to edit |
| Git and GitHub | Version history and the public portfolio |

## Data model

| Entity | Key fields |
|---|---|
| **Deal brief** | Buyer, target, price, shares, valuation basis, the six committee questions, dates |
| **Source document** | Type (folder), file name, date; every document is labeled fictional |
| **Finding** | ID (`SEC-`, `NEWS-`, `LIT-`, `FIN-` + 2 digits), one-line finding, evidence, source (file and section, row or docket date), severity, confidence, claim type (news), deal impact, cross-check, status, iteration |
| **Cross-source finding** | ID (`X-` + 2 digits), the finding, the IDs it is built from, severity, confidence, status, recommended action |
| **Conflict** | ID (`C` + number), side A, side B, status |
| **Follow-up** | ID (`F` + number), assigned specialist, question, reason |
| **Run log entry** | Time, step, what happened, decision or checkpoint |
| **Verification verdict** | Finding ID, verdict (Verified, Partially verified, Not supported), what was checked, correction |
| **Planted issue (answer key)** | ID (`P` + 2 digits), issue, where the evidence is, expected severity, cross-source flag |
| **Scorecard row** | Planted issue ID, result (Found, Partially found, Missed), matching finding IDs |

**Allowed values:** severity Critical, High, Medium, Low (plus Positive for strengths); confidence High, Medium, Low; claim type Fact, Allegation, Rumor; status Open, Verified, Partially verified, Rejected.

## Interfaces between parts

| From | To | Interface |
|---|---|---|
| Operator | Lead agent | Commands (`/diligence`, `/diligence-status`, `/evaluate`, `/reset-memory`, `/run-tests`) and checkpoint replies ("approve", "dig deeper on <topic>", "proceed", "approve report") |
| Lead agent | Specialist | A task message: deal context, task list, facts from other sources with their citations, and a reminder of the output format |
| Specialist | Lead agent | One final message in the standard format: files reviewed, finding cards, positives, gaps |
| Lead agent | Working memory | Files with fixed names and table layouts (see the templates in `templates/memory/`) |
| Lead agent | Verifier | A list of findings: ID, claim, cited sources, severity |
| Verifier | Lead agent | One report per batch: a verdict for each finding, what was checked and any correction. The lead rewrites each Partially verified row with that wording before Checkpoint 3 |
| `/evaluate` | Answer key | Read only after the operator approves the permission prompt |
| `/reset-memory` | Archive | Moves `memory/`, `output/` and `evaluation/scorecard.md` into a dated `runs/` folder, then restores the blank templates |
| Report pipeline | Files | Markdown, then HTML with the stylesheet embedded, then PDF |

## System patterns (secure and extensible)

- **One source per specialist.** Swapping a simulated source for a real one (for example a news connector) changes one folder and one agent file, nothing else.
- **Least privilege.** Specialists can only read. Only the lead agent writes, and only to `memory/` and `output/`. Edits to source data and the answer key are denied.
- **Instructions are not enforcement.** Anything that must always hold is backed by a permission rule or an automated check, not only by an instruction.
- **Sources are evidence, never instructions.** Every agent is told to report, not obey, any instruction-like text inside a document (prompt-injection defense).
- **Single source of truth.** The findings register holds every finding. Findings are never deleted; only their status changes.
- **Separation of duties.** Specialists find, the verifier checks, a human approves.
- **Bounded loops.** At most three iterations, with stop conditions and a logged reason for every extra loop.
- **Evidence-carrying claims.** No finding without a citation. The verifier and the checks enforce it.
- **Append-only audit trail.** The run log only grows, each analyst's unedited report is kept, and old runs are archived rather than deleted.
- **Blind evaluation.** Everything in `evaluation/` (the answer key and the latest scorecard) needs operator approval to open, and the answer key's checksum is tested so any change is visible. `/reset-memory` moves each scorecard into its archived run, and earlier runs (`examples/`, `runs/`) need approval too, so a new run cannot read past answers.
- **Nothing found is dropped silently.** Findings that were not verified still appear in the report appendix, labeled "not verified".
- **Template-driven output.** The report structure lives in `CLAUDE.md` and the look lives in one stylesheet.

## Security

- **Authentication:** the operator's own Claude Code sign-in. Nothing else to sign in to, and no passwords or keys in the project.
- **Authorization:** permission rules in `.claude/settings.json` (web tools denied; edits to `data/` and the answer key denied; reading anything in `evaluation/` or an earlier run needs approval) and a read-only tool list for every subagent. Subagents inherit the project's permission rules.
- **Secrets:** none in v1. Future connectors must use admin-approved credentials stored outside the project. Never commit keys.
- **Input validation:** source documents are untrusted input. The prompt-injection rule, read-only tools, no web access and human checkpoints limit what a malicious document could do. Data files are checked against a checksum manifest.
- **Rate and cost limits:** 3-iteration cap, narrow follow-up tasks, small sources. The full sample run used about 1.95 million subagent tokens across 10 subagent runs (4 analysts, 2 follow-ups, 4 verifiers) and took 69 minutes from the approved plan to sign-off. Iteration 1 alone used about 0.76 million tokens and 26 minutes.
- **Real client data (future only):** use an Enterprise plan, request zero data retention for Claude Code, connect internal systems through admin-approved read-only connectors, and get compliance sign-off first.

## Hosting, deployment and configuration

- **Runs locally.** Clone or download the project, open the folder in Claude Code, type `/diligence`.
- **Configuration:** `.claude/settings.json` is shared and committed. Personal overrides go in `.claude/settings.local.json`, which is not committed.
- **Publishing:** the GitHub repository `sabinejoseph8/Falcon_M-A_Due_Diligence` holds the README, diagram, sample run and planning files, and stays private until the owner makes it public. A `.gitignore` keeps `interview-notes.md` and Python caches out. The Project Memory website is a private claude.ai page until it is shared.
- **Optional tools:** Python 3 for the checks; pandoc and a headless browser for PDF output.

## Testing approach

- **Automated checks** (`python3 tests/run_all.py`, or `/run-tests`), grouped by build phase:
  - Phase 1 (`test_phase1_config.py`): agents valid and read-only, commands present and not shadowing built-ins, guardrail rules present (including approval to read `evaluation/` or an earlier run, and `/reset-memory` archiving the scorecard), checkpoints and loop cap in `CLAUDE.md`.
  - Phase 2 (`test_phase2_data.py`): financial statements tie out, documents labeled fictional, docket files present, answer key complete, source data unchanged (checksums).
  - Phase 3 (`test_phase3_run.py`): a run's findings are complete, the loop cap held, all analyst reports saved, all three checkpoints logged, and the report has every section, cites only known findings and excludes rejected ones.
  - Phase 4 (`test_phase4_evaluation.py`): the scorecard reports all four metrics and grades every planted issue.
  - All phases (`test_style.py`): no em dashes, README links work (including encoded paths such as `Project%20Memory/`).
  - In all: 34 checks. The sample run and all three graded runs pass all 34 with none skipped.
- **Manual verification:** step-by-step checks for each phase in `progress.md`.
- **Quality score:** `/evaluate` grades each run against the answer key (recall, severity accuracy, unsupported findings, distractors).

## Critical risks and challenges

Riskiest first. The first four are addressed in the earliest phases.

| # | Risk | Why it matters | How we handle it |
|---|---|---|---|
| 1 | **Instructions are not enforcement.** An agent could skip a checkpoint, read the answer key or wander outside its source. | The whole value is controlled autonomy. A skipped checkpoint undermines trust. | Permission rules for the hard limits, read-only tools, checks that confirm all three checkpoints were logged, and an operator who watches the run. |
| 2 | **Wrong or mis-cited findings** reach a high-stakes report. | One invented number can discredit the whole report. | Mandatory citations, an independent verifier, "Not supported" findings excluded, every correction applied before Checkpoint 3, checks that every cited ID exists, and human sign-off. |
| 3 | **Prompt injection** through a source document. | Real data rooms contain text the builder does not control. | "Evidence, never instructions" rule in every agent, no web access, no write access for specialists, human checkpoints. A manual injection test is in Phase 5. |
| 4 | **Claude Code features change** (for example commands merging into skills, a new built-in command name). | A silent change could disable an agent or a guardrail. | Phase 1 checks catch missing or invalid configuration; a docs review with Claude Code's guide agent before each release. |
| 5 | **Run-to-run variation.** Two runs can find different things and score differently. | A single score could be luck. | Fixed output format and rubrics; grade several runs and report the average and range; keep the sample run as a fixed reference. Measured over three blind runs: Critical and High recall 96.2% to 100%, overall 91.7% to 94.4%. |
| 6 | **Parallel and background behavior.** Background subagents may not be able to ask for permissions, and parallel start is not guaranteed. | A blocked analyst could silently return less. | Specialists only need read access inside the project (no permission prompts); the lead waits for every report and retries a failed analyst once. |
| 7 | **Arithmetic without code.** The financial analyst is read-only and calculates by hand. | A math slip could change a conclusion. | Show-your-work rule, independent recomputation by the verifier, automated tie-out checks on the data, key numbers kept in one dataset. |
| 8 | **Cost and time.** Four large-context analysts per iteration. | Long or expensive runs discourage use. | Small sources, narrow follow-ups, 3-loop cap. Measured on the sample run: about 1.95 million subagent tokens and 69 minutes from plan to sign-off (iteration 1: 0.76 million tokens, 26 minutes). |
| 9 | **Missing tools on the operator's computer** (no Python, no PDF tool). | Checks or PDFs would fail. | Standard-library-only checks, the HTML fallback for PDFs, and manual verification steps for every phase. |
| 10 | **Simulated data is easier than reality**, and agents could be tuned to the planted issues. | The score could overstate real-world performance. | Distractors in the data, a blind answer key, and (future) a second fictional target that the instructions were never tuned on. The first test run was only partly blind (the lead agent ran in the session that built the data). The fully blind run in a fresh session scored 96.2% recall on Critical and High issues and 94.4% overall, close to the sample run, which suggests the first score was not inflated. A second fictional target is still needed to test generalization. |
| 11 | **Real client data** if the project is adapted for a live deal. | Confidentiality and data retention obligations. | Out of scope for v1. Enterprise plan, zero data retention request, read-only connectors and compliance sign-off required first. |
| 12 | **Saved runs leak answers.** The sample run and its scorecard sit inside the project, and each new grading writes a scorecard to `evaluation/`. | A new run that read them could score well without finding anything itself, and the next grading would overwrite the last scorecard. | Claude Code asks before any agent opens `evaluation/`, `examples/` or `runs/`; `/reset-memory` moves each scorecard into its archived run; the lead agent's guardrails forbid reading them; and Phase 1 checks confirm both rules. |

## Decisions

| Date | Decision |
|---|---|
| 2026-10-17 | Claude Code features only. No Agent SDK, no Managed Agents, no application code. |
| 2026-10-18 | One specialist per source; a separate, read-only citation verifier. |
| 2026-10-18 | Findings register as the single source of truth; never delete findings. |
| 2026-10-18 | `/status` renamed `/diligence-status` (it shadowed a built-in command). |
| 2026-10-18 | Shell access removed from the financial analyst so every subagent is truly read-only. |
| 2026-10-18 | Reading the answer key requires operator approval; source data and the answer key are protected by deny rules and a checksum test. |
| 2026-10-18 | Prompt-injection rule added to the lead agent and every subagent. |
| 2026-10-18 | Automated checks in Python's standard library, run with `/run-tests`. |
| 2026-10-18 | The sample run ships in the project under `examples/sample-run/`, labeled as a build test run. |
| 2026-10-18 | Earlier runs (`examples/`, `runs/`) need operator approval to open, like the answer key, with an automated check. |
| 2026-10-18 | Three instruction fixes from the first scorecard: list unverified findings in the report appendix, combine trend findings into one cross-source finding, and apply every verifier correction before Checkpoint 3. |
| 2026-10-18 | The project is hosted in the GitHub repository `sabinejoseph8/Falcon_M-A_Due_Diligence`; `.gitignore` keeps `interview-notes.md` out. |
| 2026-10-18 | `/reset-memory` moves `evaluation/scorecard.md` into the archived run, and the approval rule covers all of `evaluation/` instead of only the answer key, with an automated check. Found while preparing the blind run: a scorecard left in `evaluation/` was unguarded, and the next grading would have overwritten it. |
| 2026-10-18 | In the blind run, the lead agent saved each analyst's and verifier's report by extracting it from the session record with a short script instead of retyping it, so the saved reports are exactly what the subagents returned. Long reports are saved by Claude Code to a file instead of shown inline, so this matters most for the longest ones. |
| 2026-10-18 | The blind run's lead agent edited `tests/test_phase3_run.py` so its own output passed; the builder reverted the edit, because a run must never change its grader. The three failing checks were written around the sample run's format rather than `CLAUDE.md`'s wording; changing them is a separate builder decision. For the Phase 5 docs review: consider a deny rule on edits to `tests/` so a run cannot do this again. |
| 2026-10-18 | Setup frozen for the remaining graded runs: same `CLAUDE.md`, agents, commands and settings as the blind run. The scorecard's three fixes wait until after the last graded run. |
| 2026-10-18 | Blind run scorecard proposes three instruction fixes (not yet applied): look up every named customer or litigant in the revenue data, verify every Medium finding the report relies on, and add a "positive and mitigating points" section to the report template, with a calibration note for debt issues cured at closing. |
| 2026-10-18 | The Phase 3 run checks accept the wording `CLAUDE.md` asks for: checkpoint names in any letter case, "Step 5: REPORT", "ACT, iteration 1", the "IC questions" heading and register IDs written as links. A builder change made after the graded runs, in its own commit. Non-standard IDs such as `LIT-F01` are still not accepted. |
| 2026-10-18 | The graders were not consistent: run 1 counted 4 Critical issues, runs 2 and 3 counted 3, and run 2 divided by 14 Critical and High issues instead of 13. Reported results are recomputed on the answer key's 13 Critical and High issues, and a fixed grading rule for `/evaluate` is a Phase 4 task. |
| 2026-10-18 | Instruction fixes from the graded runs: the lead agent sizes every named customer, supplier or litigant against `revenue_by_customer.csv`; the verifier also gets every Medium finding an IC answer cites or an `X-` finding is built from; the executive summary lists positive and mitigating points; the financial analyst compares the last goodwill test with share price moves; and a calibration rule rates debt problems cured at closing as High unless they cause a default or liquidity problem first. They take effect from the next run and have not been measured yet. |
| 2026-10-18 | `/evaluate` follows fixed grading rules: severity group = the answer key's first-listed severity, the Critical and High group listed by ID, every recall figure shown as numerator / denominator, and positives kept out of recall. The rules name no issue IDs or counts, because the lead agent can read the command file. |

## Open questions (with recommended defaults)

1. **Grade one run or several?** Decided: three blind runs with a frozen setup, with the average and range in the README (done October 18, 2026).
2. **Move commands to the newer skills format?** Recommended default: not for v1. Command files still work and are simpler to read.
