---
description: Run the full due diligence loop (Plan, Act, Observe, Verify, Report) on one target, with human checkpoints
argument-hint: "[target, default falcon] [optional focus, for example: focus on litigation]"
---

Run the due diligence process defined in CLAUDE.md on one target.

Arguments from the user (may be empty): $ARGUMENTS

1. **Pick the target.** If the first word of the arguments names a folder in `targets/`, that is the target and the rest of the arguments are extra instructions. Otherwise the target is `falcon` and all of the arguments are extra instructions. If `targets/<target>/data/deal-brief.md` does not exist, list the folders in `targets/` and stop.
2. **Check for a previous run.** Read `memory/run-log.md`. If it shows a previous run, ask the user whether to continue that run or start fresh. To start fresh, the user can run `/reset-memory` first. When continuing, use the target named in `memory/target.txt`, and tell the user if it differs from the one picked above.
3. **Record the target.** For a fresh run, write the target name (for example `falcon`) as the only line of `memory/target.txt`, and log it in `memory/run-log.md`.

Then begin with Step 1: PLAN, and stop at CHECKPOINT 1.
