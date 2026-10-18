---
description: Grade the latest diligence run against the answer key of planted issues
---

You are grading this system's latest diligence run. This is the only command allowed to read `evaluation/answer-key.md`.

1. Read `evaluation/answer-key.md` (Claude Code will ask the user to approve this, by design), `memory/findings.md`, and the report in `output/`.
2. For each planted issue in the answer key, decide whether the run found it:
   - **Found:** the main point is in the verified findings, with a correct citation.
   - **Partially found:** some of it was found, or it was found but with the wrong severity, a missing cross-source link or a weak citation.
   - **Missed:** not found.
3. For each distractor in the answer key, check whether the run wrongly rated it Medium or above.
4. Check for false findings: any finding in the report that the sources do not support (use the verifier results in memory).
5. Write `evaluation/scorecard.md` with:
   - recall overall and by severity (Found counts as 1, Partially found as 0.5);
   - severity accuracy (share of found issues rated within one level of the answer key);
   - unsupported findings that reached the report (target: zero);
   - distractors rated too high;
   - a table of every planted issue with its result and the matching finding IDs;
   - the three most useful improvements to the agent instructions.
6. Show the user a short summary.

Do not change the answer key or the data.
