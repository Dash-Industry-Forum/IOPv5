#!/usr/bin/env python3
"""Proof-of-concept Bikeshed/Markdown to Metanorma AsciiDoc converter.

This intentionally supports the subset used by Part 12 and is not a general
Bikeshed parser. Bikeshed remains the canonical source; generated AsciiDoc should
be treated as derived output unless explicitly reviewed.

Usage:
    python tools/metanorma/bikeshed_to_adoc.py \
        specs/part12-conformance-reference-tools/part12-conformance-reference-tools.bs \
        --out ../authoring/metanorma/generated/part12-conformance-reference-tools.adoc
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def parse_metadata(bs_text: str) -> dict[str, list[str]]:
    m = re.search(r"<pre class=metadata>(.*?)</pre>", bs_text, re.S | re.I)
    meta: dict[str, list[str]] = {}
    if not m:
        return meta
    for raw in m.group(1).splitlines():
        line = raw.strip()
        if not line or ":" not in line:
            continue
        key, val = line.split(":", 1)
        meta.setdefault(key.strip(), []).append(val.strip())
    return meta


def parse_biblio(bs_text: str) -> dict[str, dict[str, str]]:
    m = re.search(r"<pre class=biblio>(.*?)</pre>", bs_text, re.S | re.I)
    if not m:
        return {}
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return {}


def include_files(bs_path: Path, bs_text: str) -> str:
    parts: list[str] = []
    for path in re.findall(r"<pre class=include>\s*path:\s*([^\s<]+)\s*</pre>", bs_text, re.S | re.I):
        if path.startswith("_shared-"):
            continue
        inc = bs_path.parent / path
        if inc.exists():
            parts.append(inc.read_text(encoding="utf-8"))
    return "\n\n".join(parts)


def render_bibliography(biblio: dict[str, dict[str, str]]) -> str:
    if not biblio:
        return ""
    lines = ["", "[bibliography]", "== Bibliography", ""]
    for key, item in sorted(biblio.items()):
        title = item.get("title", key)
        publisher = item.get("publisher", "")
        date = item.get("date", "")
        href = item.get("href", "")
        suffix = ", ".join(x for x in [publisher, date] if x)
        text = f"* [[[{key}]]] _{title}_"
        if suffix:
            text += f", {suffix}"
        if href:
            text += f", {href}"
        text += "."
        lines.append(text)
    return "\n".join(lines) + "\n"


def convert_inline(s: str) -> str:
    s = html.unescape(s)
    # Bikeshed xrefs/dfns -> AsciiDoc emphasis/plain text
    s = re.sub(r"\[=([^=]+)=\]", r"`\1`", s)
    s = re.sub(r"<dfn(?:\s+[^>]*)?>(.*?)</dfn>", r"\1", s, flags=re.I | re.S)
    s = re.sub(r"\[\[!?([A-Za-z0-9_-]+)\]\]", r"<<\1>>", s)
    # Markdown links -> AsciiDoc links
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\2[\1]", s)
    # Bold / emphasis simple cases
    s = re.sub(r"\*\*([^*]+)\*\*", r"*\1*", s)
    # Backticks are valid monospace in AsciiDoc too for simple cases.
    return s


def convert_table(block: str) -> str:
    cap = re.search(r"<caption>(.*?)</caption>", block, re.S | re.I)
    title = convert_inline(re.sub(r"\s+", " ", cap.group(1)).strip()) if cap else "Table"
    rows = re.findall(r"<tr>(.*?)(?=<tr>|</table>)", block, re.S | re.I)
    out = [f".{title}", "[cols=\"1,1,1\",options=\"header\"]", "|==="]
    for i, row in enumerate(rows):
        cells = re.findall(r"<t[hd][^>]*>(.*?)(?=<t[hd]|$)", row, re.S | re.I)
        cells = [convert_inline(re.sub(r"<[^>]+>", "", c).strip()) for c in cells]
        if not cells:
            continue
        if i == 0:
            out[1] = f"[cols=\"{','.join(['1'] * len(cells))}\",options=\"header\"]"
        out.append("|" + " |".join(cells))
    out.append("|===")
    return "\n".join(out)


def convert_figures(md: str) -> str:
    def repl(m: re.Match[str]) -> str:
        body = m.group(1)
        cap = re.search(r"<figcaption>(.*?)</figcaption>", body, re.S | re.I)
        title = convert_inline(re.sub(r"\s+", " ", cap.group(1)).strip()) if cap else "Diagram"
        mer = re.search(r"<pre class=mermaid>(.*?)</pre>", body, re.S | re.I)
        if mer:
            src = mer.group(1).strip()
            # Drop Mermaid init directive for Metanorma/AsciiDoc readability.
            src = re.sub(r"^%%\{init:.*?\}%%\s*", "", src, flags=re.S)
            return f".{title}\n[mermaid]\n....\n{src}\n...."
        return f".{title}\n[NOTE]\n====\nFigure conversion not implemented.\n===="

    return re.sub(r"<figure[^>]*>(.*?)</figure>", repl, md, flags=re.S | re.I)


def convert_definition_lists(md: str) -> str:
    # Convert Bikeshed definition-list pairs of the form ': term' + ':: definition'
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith(": "):
            term = convert_inline(line[2:].strip())
            out.append(f"{term}::")
            i += 1
            if i < len(lines) and lines[i].startswith("::"):
                out.append(convert_inline(lines[i][2:].strip()))
                i += 1
                while i < len(lines) and (lines[i].startswith("    ") or lines[i].strip() == ""):
                    out.append(convert_inline(lines[i].strip()))
                    i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def convert_markdown(md: str) -> str:
    # Remove comments.
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    md = convert_figures(md)
    # Tables.
    md = re.sub(r"<table class=\"data\">(.*?)</table>", lambda m: convert_table(m.group(0)), md, flags=re.S | re.I)
    md = convert_definition_lists(md)

    out: list[str] = []
    for raw in md.splitlines():
        line = raw.rstrip()
        # Headings: # Title # {#id}
        hm = re.match(r"^(#{1,6})\s+(.+?)\s+#+\s+\{#([^}]+)\}\s*$", line)
        if hm:
            level = len(hm.group(1)) + 1  # Metanorma title is level 0, sections start ==
            title = convert_inline(hm.group(2))
            anchor = hm.group(3)
            out.append(f"[[{anchor}]]")
            out.append("=" * level + f" {title}")
            continue
        if line.startswith("Issue:"):
            out.extend(["[NOTE]", "====", convert_inline(line), "===="])
            continue
        out.append(convert_inline(line))
    return "\n".join(out).strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("bs", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    bs_path = args.bs
    bs_text = bs_path.read_text(encoding="utf-8")
    meta = parse_metadata(bs_text)
    body = include_files(bs_path, bs_text)
    biblio = parse_biblio(bs_text)

    title = meta.get("Title", [bs_path.stem])[0]
    rev = meta.get("Revision", ["0.1"])[0]
    editors = meta.get("Editor", [])
    abstract = meta.get("Abstract", [""])[0]
    shortname = meta.get("Shortname", [bs_path.stem])[0]
    part_match = re.search(r"part0?(\d+)", shortname, re.I)
    docnumber = f"IOP-v5-Part{int(part_match.group(1)):02d}" if part_match else f"IOP-v5-{shortname}"

    header = [
        f"= {title}",
        ":doctype: standard",
        f":docnumber: {docnumber}",
        f":revnumber: {rev}",
        ":mn-document-class: generic",
        # Generic Metanorma in the tested winget package supports html/doc/xml;
        # PDF is tested separately with another flavour because generic reported
        # "pdf format is not supported for this standard".
        ":mn-output-extensions: html,doc,xml",
        ":technical-committee: DASH-IF Technical Working Group",
        ":copyright-holder: DASH Industry Forum",
        ":language: en",
        ":sectnums:",
        ":toc: left",
        "",
    ]
    for idx, ed in enumerate(editors, 1):
        header.append(f":fullname_{idx}: {ed.split(',')[0].strip()}")
    if abstract:
        header += ["", "[abstract]", "== Abstract", convert_inline(abstract), ""]

    adoc = "\n".join(header) + "\n" + convert_markdown(body) + render_bibliography(biblio)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(adoc, encoding="utf-8")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
