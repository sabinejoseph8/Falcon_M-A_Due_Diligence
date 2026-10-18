"""Shared helpers for the Project Falcon checks. Standard library only."""
import hashlib
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "tests" / "data_manifest.json"
EM_DASH = "—"


def run_dir():
    """Folder holding a diligence run (memory/ and output/). Set with run_all.py --run."""
    return (ROOT / os.environ.get("FALCON_RUN_DIR", ".")).resolve()


def read(path):
    return pathlib.Path(path).read_text(encoding="utf-8")


def frontmatter(path):
    """Return the YAML frontmatter of a Markdown file as a dict of simple key: value pairs."""
    match = re.match(r"^---\n(.*?)\n---\n", read(path), re.S)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields


def table_rows(text):
    """Return the body rows of every Markdown table as lists of cells (separator rows removed)."""
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("|") and line.endswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            rows.append(cells)
    return rows


def protected_files():
    """Source data and the answer key: files that must never change during a run."""
    files = sorted(p for p in (ROOT / "data").rglob("*") if p.is_file())
    files.append(ROOT / "evaluation" / "answer-key.md")
    return files


def checksums():
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected_files()}


def write_manifest():
    MANIFEST.write_text(json.dumps(checksums(), indent=2) + "\n", encoding="utf-8")
