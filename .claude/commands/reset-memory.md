---
description: Archive the current run and its scorecard, then reset working memory for a fresh diligence run
---

1. Create a folder `runs/<YYYY-MM-DD_HHMM>/` using the current date and time.
2. Move the current contents of `memory/` and `output/` into that folder (keep the subfolder names). Leave `output/.gitkeep` in place.
3. If `evaluation/scorecard.md` exists, move it to `runs/<YYYY-MM-DD_HHMM>/evaluation/scorecard.md` with a shell `mv` command, without opening it. Each run keeps its own grade, the next `/evaluate` cannot overwrite it, and the next run cannot read it.
4. Copy the blank templates from `templates/memory/` into `memory/`, and make sure `output/` is empty apart from `.gitkeep`.
5. Confirm what was archived, including whether a scorecard was moved, and that memory is now blank.

Do not touch `data/`, `.claude/` or `evaluation/answer-key.md`. The scorecard is the only file that leaves `evaluation/`.
