---
description: Grade the latest diligence run against the target's answer key of planted issues
argument-hint: "[target, default falcon]"
---

You are grading this system's latest diligence run. This is the only command allowed to read a target's `evaluation/answer-key.md`.

**Target:** the target is "$ARGUMENTS" if that names a folder in `targets/`; if it is empty, use the name in `memory/target.txt`, or `falcon` if that file does not exist. If `memory/target.txt` names a different target from the one given, tell the user and stop: a run can only be graded against its own answer key. Below, `<target>` means that name.

1. Read `targets/<target>/evaluation/answer-key.md` (Claude Code will ask the user to approve this, by design), `memory/findings.md`, and the report in `output/`.
2. For each planted issue in the answer key, decide whether the run found it:
   - **Found:** the main point is in the verified findings, with a correct citation.
   - **Partially found:** some of it was found, or it was found but with the wrong severity, a missing cross-source link or a weak citation.
   - **Missed:** not found.
   Use the fixed grading rules below for every number.
3. For each distractor in the answer key, check whether the run wrongly rated it Medium or above.
4. Check for false findings: any finding in the report that the sources do not support (use the verifier results in memory).
5. Write `targets/<target>/evaluation/scorecard.md` with:
   - recall overall, for the Critical and High group, and for each severity group, with the IDs in each group listed;
   - severity accuracy;
   - unsupported findings that reached the report (target: zero);
   - distractors rated too high;
   - a table of every planted issue with its result and the matching finding IDs;
   - the three most useful improvements to the agent instructions.
6. Show the user a short summary.

Do not change the answer key or the data.

## Fixed grading rules

Apply these exactly, so every run is graded the same way:

- **Severity group:** each planted issue belongs to the first severity listed in its expected severity in the answer key. For example, "Critical or High" counts as Critical and "Medium (High ok)" counts as Medium.
- **Critical and High group:** every issue whose first-listed severity is Critical or High. Count it from the answer key each time, and list its IDs in the scorecard.
- **Scoring:** Found = 1, Partially found = 0.5, Missed = 0. Write every recall figure as numerator / denominator = percentage, with one decimal place, and check that each denominator equals the number of IDs listed for that group.
- **Severity accuracy:** a Found or Partially found issue counts if the highest severity among its matching verified findings is within one level of a severity the answer key accepts for it. Missed issues are left out.
- **Distractors:** too high means rated Medium or above anywhere in the register or the report.
- **Unsupported findings:** a finding in the report that the verifier marked Not supported, or that you cannot match to its cited source.
- **Positives:** say whether the planted positives appear in the report, but leave them out of recall.
- Grade from this run's files only. Do not open earlier scorecards or runs.
