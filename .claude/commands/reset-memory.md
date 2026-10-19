---
description: Archive the current run and its scorecard, then reset working memory for a fresh diligence run
---

1. Create a folder `runs/<YYYY-MM-DD_HHMM>/` using the current date and time.
2. Read the target name from `memory/target.txt` (use `falcon` if the file does not exist). Below, `<target>` means that name.
3. Move the current contents of `memory/` and `output/` into that folder (keep the subfolder names). `memory/target.txt` moves with them, so the run folder records which target it used; if the file did not exist, write `<target>` to `runs/<YYYY-MM-DD_HHMM>/memory/target.txt`. Leave `output/.gitkeep` in place.
4. If `targets/<target>/evaluation/scorecard.md` exists, move it to `runs/<YYYY-MM-DD_HHMM>/evaluation/scorecard.md` with a shell `mv` command, without opening it. Each run keeps its own grade, the next `/evaluate` cannot overwrite it, and the next run cannot read it.
5. Copy the blank templates from `templates/memory/` into `memory/`, and make sure `output/` is empty apart from `.gitkeep`.
6. Confirm what was archived, including the target and whether a scorecard was moved, and that memory is now blank.

Do not touch `targets/*/data/`, `.claude/` or any `targets/*/evaluation/answer-key.md`. The scorecard is the only file that leaves a target's `evaluation/` folder.
