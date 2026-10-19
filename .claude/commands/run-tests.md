---
description: Run the project's automated checks (and optionally check a saved diligence run)
argument-hint: "[optional run folder, for example: examples/sample-run]"
---

Run the automated checks with Python 3:

- If the user gave a run folder ("$ARGUMENTS" is not empty), run `python3 tests/run_all.py --run "$ARGUMENTS"` (keep the quotes, because the project path can contain spaces).
- Otherwise run `python3 tests/run_all.py`.

Then summarize in plain English: how many checks passed, failed or were skipped, grouped by phase, and for each failure what it means and how to fix it. Do not change any files.

If Python 3 is not installed, say so and point the user to the manual verification steps in `Project Memory/progress.md`.
