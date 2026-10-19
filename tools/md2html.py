#!/usr/bin/env python3
"""Convert the diligence report from Markdown to a self-contained, print-friendly HTML file.

Standard library only, so Step 5 works on any computer with Python 3.

  python3 tools/md2html.py output/Project-Falcon-Due-Diligence-Report.md output/Project-Falcon-Due-Diligence-Report.html

Supports the Markdown the report template uses: headings, paragraphs, bold, italic,
inline code, links, nested bulleted and numbered lists, pipe tables, blockquotes,
horizontal rules and fenced code blocks. A line that is a raw block tag (for example
<div class="cover"> or </div>) passes through unchanged, and the Markdown between
the tags is still converted. Inline <p>, <span>, <br>, <strong> and <em> tags pass
through too. The stylesheet in templates/report-style.css is embedded in the page.
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS = ROOT / "templates" / "report-style.css"

INLINE_TAGS = r"(?:p|span|br|strong|em|b|i|sup|sub|a|small|code)"
RAW_INLINE = re.compile(rf"</?{INLINE_TAGS}\b[^<>]*>", re.I)
BLOCK_TAG = re.compile(r"^\s*</?(?:div|p|section|table|figure|hr|br)\b[^<>]*>.*$", re.I)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LIST_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
HR = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")


def inline(text):
    """Convert inline Markdown. Code spans and allowed raw tags are kept as they are."""
    kept = []

    def keep(fragment):
        kept.append(fragment)
        return f"\x00{len(kept) - 1}\x00"

    text = re.sub(r"`([^`]+)`", lambda m: keep(f"<code>{html.escape(m.group(1), quote=False)}</code>"), text)
    text = RAW_INLINE.sub(lambda m: keep(m.group(0)), text)
    text = re.sub(r"&(?![a-zA-Z]+;|#\d+;|#x[0-9a-fA-F]+;)", "&amp;", text)
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"(?<!\w)_(?!\s)(.+?)(?<!\s)_(?!\w)", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: kept[int(m.group(1))], text)


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    return [cell.strip().replace("\\|", "|") for cell in re.split(r"(?<!\\)\|", line)]


def table(lines):
    header, sep, body = split_row(lines[0]), split_row(lines[1]), [split_row(l) for l in lines[2:]]
    aligns = []
    for cell in sep:
        left, right = cell.startswith(":"), cell.endswith(":")
        aligns.append("center" if left and right else "right" if right else "left" if left else None)

    def cells(row, tag):
        out = []
        for i, cell in enumerate(row):
            align = aligns[i] if i < len(aligns) else None
            style = f' style="text-align:{align}"' if align else ""
            out.append(f"<{tag}{style}>{inline(cell)}</{tag}>")
        return "".join(out)

    rows = "\n".join(f"<tr>{cells(r, 'td')}</tr>" for r in body)
    return f"<table>\n<thead><tr>{cells(header, 'th')}</tr></thead>\n<tbody>\n{rows}\n</tbody>\n</table>"


def lists(lines):
    """Build nested <ul>/<ol> from list lines, using indentation for nesting."""
    out, stack = [], []  # stack of (indent, tag)
    for line in lines:
        match = LIST_ITEM.match(line)
        if not match:  # a continuation line belongs to the open item
            if out[-1].endswith("</li>") and out[-1].startswith("<li>"):
                out[-1] = out[-1][: -len("</li>")] + " " + inline(line.strip()) + "</li>"
            else:
                out.append(f"<p>{inline(line.strip())}</p>")
            continue
        indent, marker, content = len(match.group(1).expandtabs(4)), match.group(2), match.group(3)
        tag = "ol" if marker[0].isdigit() else "ul"
        while stack and indent < stack[-1][0]:
            out.append(f"</{stack.pop()[1]}>")
            out.append("</li>")
        if stack and indent == stack[-1][0] and tag != stack[-1][1]:
            out.append(f"</{stack.pop()[1]}>")
        if not stack or indent > stack[-1][0]:
            if stack:  # nest inside the previous item
                out[-1] = out[-1][: -len("</li>")]
            start = f' start="{marker[:-1]}"' if tag == "ol" and not stack and marker[:-1] != "1" else ""
            out.append(f"<{tag}{start}>")
            stack.append((indent, tag))
        out.append(f"<li>{inline(content)}</li>")
    while stack:
        out.append(f"</{stack.pop()[1]}>")
        if stack:
            out.append("</li>")
    return "\n".join(out)


def convert(markdown):
    lines = markdown.splitlines()
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.lstrip().startswith("```"):
            i += 1
            code = []
            while i < len(lines) and not lines[i].lstrip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(code), quote=False)}</code></pre>")
        elif BLOCK_TAG.match(line):
            out.append(line)
            i += 1
        elif HEADING.match(line):
            level, text = HEADING.match(line).groups()
            slug = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", text).lower()).strip("-")
            out.append(f'<h{len(level)} id="{slug}">{inline(text)}</h{len(level)}>')
            i += 1
        elif HR.match(line):
            out.append("<hr>")
            i += 1
        elif line.lstrip().startswith("|") and i + 1 < len(lines) and TABLE_SEP.match(lines[i + 1]):
            block = [line, lines[i + 1]]
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                block.append(lines[i])
                i += 1
            out.append(table(block))
        elif line.lstrip().startswith(">"):
            quoted = []
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                quoted.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append(f"<blockquote>\n{convert(chr(10).join(quoted))}\n</blockquote>")
        elif LIST_ITEM.match(line):
            block = []
            while i < len(lines) and lines[i].strip() and (LIST_ITEM.match(lines[i]) or lines[i].startswith((" ", "\t"))):
                block.append(lines[i])
                i += 1
            # A blank line followed by more list items continues the same list.
            while i + 1 < len(lines) and not lines[i].strip() and LIST_ITEM.match(lines[i + 1]):
                i += 1
                while i < len(lines) and lines[i].strip() and (LIST_ITEM.match(lines[i]) or lines[i].startswith((" ", "\t"))):
                    block.append(lines[i])
                    i += 1
            out.append(lists(block))
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not any(
                p.match(lines[i]) for p in (HEADING, LIST_ITEM, BLOCK_TAG, HR)
            ) and not lines[i].lstrip().startswith((">", "|", "```")):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


def page(markdown):
    match = re.search(r"^#\s+(.+)$", markdown, re.M)
    title = html.escape(re.sub(r"<[^>]+>|[*`]", "", match.group(1))) if match else "Report"
    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{title}</title>\n<style>\n{CSS.read_text(encoding='utf-8')}\n</style>\n</head>\n"
        f"<body>\n{convert(markdown)}\n</body>\n</html>\n"
    )


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    source, target = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    target.write_text(page(source.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"Wrote {target}")


if __name__ == "__main__":
    main()
