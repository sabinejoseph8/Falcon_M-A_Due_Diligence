---
description: Archive the current run and reset working memory for a fresh diligence run
---

1. Create a folder `runs/<YYYY-MM-DD_HHMM>/` using the current date and time.
2. Move the current contents of `memory/` and `output/` into that folder (keep the subfolder names).
3. Copy the blank templates from `templates/memory/` into `memory/`, and recreate an empty `output/` folder.
4. Confirm what was archived and that memory is now blank.

Do not touch `data/`, `evaluation/` or `.claude/`.
