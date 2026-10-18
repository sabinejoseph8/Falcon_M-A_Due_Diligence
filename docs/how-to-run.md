# How to run Project Falcon in Claude Code

No coding needed. You type plain-English replies at three checkpoints.

## Before you start

1. Install Claude Code and sign in (see the official setup guide at https://code.claude.com/docs).
2. Download or clone this project folder to your computer.
3. Open a terminal in the project folder (the folder that contains `CLAUDE.md`) and type `claude`.

## Check the setup (1 minute)

- Type `/agents`. You should see five project agents: `sec-filings-analyst`, `news-media-analyst`, `litigation-analyst`, `financial-analyst` and `citation-verifier`.
- Type `/` and look for the project commands: `/diligence`, `/diligence-status`, `/evaluate`, `/reset-memory` and `/run-tests`.
- Type `/run-tests`. Claude runs the automated checks and should report 0 failures (checks that need a finished run are skipped).

## Run the diligence (about 60 to 90 minutes)

| Step | You type | What happens |
|---|---|---|
| Start | `/diligence` | The lead agent reads the deal brief and writes a plan to `memory/plan.md`. |
| Checkpoint 1 | `approve` (or ask for changes) | Four analysts start in parallel: SEC filings, news, litigation, financials. |
| Checkpoint 2 | `proceed`, or `dig deeper on <topic>` | The lead agent shows the red flags and the conflicts between sources. You decide whether to loop again (maximum 3 loops). |
| Checkpoint 3 | `approve report` (or ask for changes) | The citation verifier has checked every key finding. You sign off before the report is written. |
| Report | nothing | The report is saved in `output/` as Markdown, HTML and (if your computer has a PDF tool) PDF. |

Claude Code may ask your permission before some actions (for example converting the report to HTML and PDF). Read the request and approve it if it makes sense.

Claude Code also asks before anything opens `evaluation/answer-key.md`, `examples/` or `runs/`. During a diligence run, **deny** these requests: the agents must not see the answer key or an earlier run. Approve the answer key request only when you run `/evaluate`.

The sample run in `examples/sample-run/` took 69 minutes from the approved plan to sign-off.

At any time, type `/diligence-status` to see where the run is, how many findings there are and what is still open.

## Grade the run

Type `/evaluate` and approve the request to open the answer key. Claude compares the run with `evaluation/answer-key.md` (the issues planted in the fictional data) and writes `evaluation/scorecard.md`.

## Run it again

Type `/reset-memory`. Your previous run is archived in `runs/`, and working memory is cleared.

## If you have no PDF tool

Open `output/Project-Falcon-Due-Diligence-Report.html` in your browser, choose Print, then Save as PDF.

## Tips for your portfolio

- Record your screen during a run (especially the three checkpoints). A two-minute video of the agents working is very persuasive.
- Keep your own scorecard from `/evaluate`, and note what you changed in the agent instructions to improve it.
