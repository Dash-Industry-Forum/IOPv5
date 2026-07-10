#!/usr/bin/env python3
"""Wrap DASH-IF modal keywords consistently in authored spec sources.

The project convention is to render shall/shall not/should/should not/may as a
light bold-italic modal keyword. This script updates `.inc.md` files in specs/ by
wrapping standalone occurrences outside comments, code spans, and HTML tags:

    <span class=modal-keyword>shall</span>

It is intentionally conservative and idempotent for already wrapped spans.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPECS = ROOT / "specs"

MODALS = ["shall not", "should not", "shall", "should", "may"]
PLACEHOLDER = "\uE000{}\uE001"

SPAN_RE = re.compile(r"<span\s+class=modal-keyword>.*?</span>", re.I | re.S)
CODE_RE = re.compile(r"`[^`]*`")
TAG_RE = re.compile(r"<[^>]+>")


def protect(pattern: re.Pattern[str], text: str, protected: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        protected.append(m.group(0))
        return PLACEHOLDER.format(len(protected) - 1)
    return pattern.sub(repl, text)


def restore(text: str, protected: list[str]) -> str:
    for i, val in enumerate(protected):
        text = text.replace(PLACEHOLDER.format(i), val)
    return text


def wrap_segment(segment: str) -> str:
    # Protect existing spans first so the script is idempotent.
    protected: list[str] = []
    segment = protect(SPAN_RE, segment, protected)
    segment = protect(CODE_RE, segment, protected)
    segment = protect(TAG_RE, segment, protected)

    for modal in MODALS:
        pat = re.compile(rf"\b{re.escape(modal)}\b", re.I)

        def repl(m: re.Match[str]) -> str:
            word = m.group(0)
            return f"<span class=modal-keyword>{word}</span>"

        segment = pat.sub(repl, segment)

    return restore(segment, protected)


def wrap_text(text: str) -> str:
    out: list[str] = []
    pos = 0
    for m in re.finditer(r"<!--.*?-->", text, re.S):
        out.append(wrap_segment(text[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(wrap_segment(text[pos:]))
    return "".join(out)


def main() -> int:
    changed = 0
    for path in sorted(SPECS.glob("part*/**/*.inc.md")):
        old = path.read_text(encoding="utf-8")
        new = wrap_text(old)
        if new != old:
            path.write_text(new, encoding="utf-8")
            print(f"updated {path.relative_to(ROOT)}")
            changed += 1
    print(f"updated {changed} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
