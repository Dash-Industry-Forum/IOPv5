#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
AUTHORING_ROOT = ROOT / "rag-authoring-starter"
SPECS = AUTHORING_ROOT / "specs"
REPORTS = AUTHORING_ROOT / "rag" / "reports"
METANORMA_REPORT = REPORTS / "metanorma-part12-poc-status.md"

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
MODALS = ("shall", "should", "may", "must", "shall not", "should not")

mcp = FastMCP("DASH-IF-IOP")


def _run(command: list[str], cwd: Path | None = None) -> dict[str, Any]:
    proc = subprocess.run(
        command,
        cwd=str(cwd or ROOT),
        capture_output=True,
        text=True,
        shell=False,
    )
    return {
        "command": command,
        "cwd": str(cwd or ROOT),
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def _authored_files() -> list[Path]:
    if not SPECS.exists():
        return []
    return sorted(
        p for p in SPECS.rglob("*")
        if p.is_file() and p.suffix in {".md", ".bs"}
    )


def _report_files() -> list[Path]:
    if not REPORTS.exists():
        return []
    return sorted(p for p in REPORTS.rglob("*.md") if p.is_file())


def _is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def _part_dirs() -> list[Path]:
    if not SPECS.exists():
        return []
    return sorted(p for p in SPECS.iterdir() if p.is_dir() and p.name.startswith("part"))


@mcp.tool()
def search_iop(query: str, limit: int = 10) -> str:
    """Search authored IOP source files for a text/regex query."""
    rx = re.compile(query, re.IGNORECASE)
    hits: list[dict[str, Any]] = []
    for path in _authored_files():
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                hits.append({
                    "path": str(path.relative_to(ROOT)),
                    "line": line_no,
                    "text": line.strip(),
                })
                if len(hits) >= limit:
                    return json.dumps({"query": query, "hits": hits}, indent=2)
    return json.dumps({"query": query, "hits": hits}, indent=2)


@mcp.tool()
def read_clause(path: str, start_line: int | None = None, end_line: int | None = None) -> str:
    """Read a source file relative to the repository root, optionally by line range."""
    target = (ROOT / path).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return json.dumps({"error": "path escapes repository root"}, indent=2)
    if not target.exists() or not target.is_file():
        return json.dumps({"error": f"file not found: {path}"}, indent=2)
    text = target.read_text(encoding="utf-8", errors="replace").splitlines()
    s = 1 if start_line is None else max(1, start_line)
    e = len(text) if end_line is None else min(len(text), end_line)
    excerpt = "\n".join(f"{i}: {text[i-1]}" for i in range(s, e + 1))
    return json.dumps({"path": path, "start_line": s, "end_line": e, "text": excerpt}, indent=2)


@mcp.tool()
def list_parts() -> str:
    """List available part directories under specs/."""
    parts = [p.name for p in _part_dirs()]
    return json.dumps({"parts": parts}, indent=2)


@mcp.tool()
def list_documents(part: str | None = None) -> str:
    """List authored source documents, optionally filtered by part-folder substring."""
    docs = []
    for path in _authored_files():
        rel = str(path.relative_to(ROOT))
        if part and part not in rel:
            continue
        docs.append(rel)
    return json.dumps({"part": part, "documents": docs}, indent=2)


@mcp.tool()
def search_part(part: str, query: str, limit: int = 10) -> str:
    """Search within a specific part directory only."""
    part_root = SPECS / part
    if not part_root.exists() or not part_root.is_dir():
        return json.dumps({"error": f"part not found: {part}"}, indent=2)
    rx = re.compile(query, re.IGNORECASE)
    hits: list[dict[str, Any]] = []
    for path in sorted(p for p in part_root.rglob("*") if p.is_file() and p.suffix in {".md", ".bs"}):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                hits.append({
                    "path": str(path.relative_to(ROOT)),
                    "line": line_no,
                    "text": line.strip(),
                })
                if len(hits) >= limit:
                    return json.dumps({"part": part, "query": query, "hits": hits}, indent=2)
    return json.dumps({"part": part, "query": query, "hits": hits}, indent=2)


@mcp.tool()
def build_iop(part: str | None = None) -> str:
    """Build all parts, or one part by folder name, using the local Bikeshed workflow."""
    if not AUTHORING_ROOT.exists():
        return json.dumps({"error": "rag-authoring-starter not found in this checkout"}, indent=2)
    if part:
        result = _run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "build.ps1", part], cwd=AUTHORING_ROOT)
    else:
        result = _run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "build.ps1"], cwd=AUTHORING_ROOT)
    return json.dumps(result, indent=2)


@mcp.tool()
def build_part(part: str) -> str:
    """Build one part by folder name, e.g. part12-conformance-reference-tools."""
    return build_iop(part)


@mcp.tool()
def build_and_validate_part(part: str) -> str:
    """Build one part and run repository publication checks."""
    build = json.loads(build_part(part))
    validate = json.loads(validate_links())
    return json.dumps({"build": build, "validate_links": validate}, indent=2)


@mcp.tool()
def build_publication_bundle() -> str:
    """Build the publication bundle into repository-root dist/."""
    script = AUTHORING_ROOT / "tools" / "publication" / "build_all.py"
    if not script.exists():
        return json.dumps({"error": "build_all.py not found"}, indent=2)
    result = _run(["python", str(script), "--out", "../dist"], cwd=AUTHORING_ROOT)
    return json.dumps(result, indent=2)


@mcp.tool()
def validate_links() -> str:
    """Run the repository publication checker over authored specs."""
    checker = AUTHORING_ROOT / "tools" / "publication" / "check_links.py"
    if not checker.exists():
        return json.dumps({"error": "check_links.py not found"}, indent=2)
    result = _run(["python", str(checker)], cwd=AUTHORING_ROOT)
    return json.dumps(result, indent=2)


@mcp.tool()
def find_broken_refs(limit: int = 100) -> str:
    """Return broken relative links and duplicate headings from authored specs."""
    issues: list[str] = []
    for path in _authored_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(AUTHORING_ROOT)
        headings: Counter[str] = Counter()
        for line in text.splitlines():
            m = HEADING.match(line.strip())
            if m:
                headings[m.group(2).strip().lower()] += 1
        for title, count in headings.items():
            if count > 1:
                issues.append(f"{rel}: duplicate heading '{title}' ({count}x)")
        for match in LINK.finditer(text):
            target = match.group(1).split(" ")[0].split("#")[0]
            if not target or _is_external(target):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                issues.append(f"{rel}: broken link target -> {target}")
        if len(issues) >= limit:
            break
    return json.dumps({"issues": issues[:limit], "count": len(issues[:limit])}, indent=2)


@mcp.tool()
def wrap_modals() -> str:
    """Run the modal-keyword normalization helper over authored sources."""
    script = AUTHORING_ROOT / "tools" / "publication" / "wrap_modals.py"
    if not script.exists():
        return json.dumps({"error": "wrap_modals.py not found"}, indent=2)
    result = _run(["python", str(script)], cwd=AUTHORING_ROOT)
    return json.dumps(result, indent=2)


@mcp.tool()
def modal_keyword_report(part: str | None = None) -> str:
    """Return modal keyword counts for authored spec files."""
    report: list[dict[str, Any]] = []
    for path in _authored_files():
        rel = str(path.relative_to(ROOT))
        if part and part not in rel:
            continue
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        counts = {modal: len(re.findall(rf"\b{re.escape(modal)}\b", text)) for modal in MODALS}
        counts = {k: v for k, v in counts.items() if v}
        if counts:
            report.append({"path": rel, "counts": counts})
    return json.dumps({"part": part, "files": report}, indent=2)


@mcp.tool()
def generate_issue_seed(part: str, topic: str) -> str:
    """Generate a simple GitHub issue seed using part context and open-issues text."""
    issues = json.loads(read_open_issues(part))
    title = f"[{part}] {topic}" if not part.lower().startswith("part") else f"[{part}] {topic}"
    body = {
        "title": title,
        "body": (
            f"## Summary\n\n{topic}\n\n"
            f"## Part\n\n{part}\n\n"
            f"## Context\n\n"
            + issues.get("text", "Open issues section not found; inspect the part manually.")
            + "\n\n## Proposed action\n\n- [ ] review source material\n- [ ] update authored text\n- [ ] add examples if applicable\n- [ ] run build and publication checks\n"
        ),
    }
    return json.dumps(body, indent=2)


@mcp.tool()
def read_open_issues(part: str) -> str:
    """Read the Open Issues and Work Items section for a given part, if present."""
    part_root = SPECS / part
    if not part_root.exists() or not part_root.is_dir():
        return json.dumps({"error": f"part not found: {part}"}, indent=2)
    section_lines: list[str] = []
    found = False
    for path in sorted(p for p in part_root.glob("*.inc.md")):
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, line in enumerate(lines):
            if "Open Issues and Work Items" in line or "open-issues" in line.lower():
                found = True
                section_lines.append(f"FILE: {path.relative_to(ROOT)}")
                for j in range(i, min(i + 40, len(lines))):
                    section_lines.append(f"{j+1}: {lines[j]}")
                break
        if found:
            break
    if not found:
        return json.dumps({"part": part, "error": "open issues section not found"}, indent=2)
    return json.dumps({"part": part, "text": "\n".join(section_lines)}, indent=2)


@mcp.tool()
def read_change_history(part: str) -> str:
    """Read the Change History section for a given part, if present."""
    part_root = SPECS / part
    if not part_root.exists() or not part_root.is_dir():
        return json.dumps({"error": f"part not found: {part}"}, indent=2)
    section_lines: list[str] = []
    found = False
    for path in sorted(p for p in part_root.glob("*.inc.md")):
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, line in enumerate(lines):
            if "Change History" in line or "change-history" in line.lower():
                found = True
                section_lines.append(f"FILE: {path.relative_to(ROOT)}")
                for j in range(i, min(i + 30, len(lines))):
                    section_lines.append(f"{j+1}: {lines[j]}")
                break
        if found:
            break
    if not found:
        return json.dumps({"part": part, "error": "change history section not found"}, indent=2)
    return json.dumps({"part": part, "text": "\n".join(section_lines)}, indent=2)


@mcp.tool()
def part_status_report(part: str) -> str:
    """Summarize documents, open issues, change history, and modal counts for one part."""
    docs = json.loads(list_documents(part))
    issues = json.loads(read_open_issues(part))
    history = json.loads(read_change_history(part))
    modals = json.loads(modal_keyword_report(part))
    return json.dumps(
        {
            "part": part,
            "documents": docs.get("documents", []),
            "open_issues": issues.get("text") or issues.get("error"),
            "change_history": history.get("text") or history.get("error"),
            "modal_counts": modals.get("files", []),
        },
        indent=2,
    )


@mcp.tool()
def search_rag_reports(query: str, limit: int = 10) -> str:
    """Search Markdown reports under rag/reports/."""
    rx = re.compile(query, re.IGNORECASE)
    hits: list[dict[str, Any]] = []
    for path in _report_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                hits.append({
                    "path": str(path.relative_to(ROOT)),
                    "line": line_no,
                    "text": line.strip(),
                })
                if len(hits) >= limit:
                    return json.dumps({"query": query, "hits": hits}, indent=2)
    return json.dumps({"query": query, "hits": hits}, indent=2)


@mcp.tool()
def metanorma_status() -> str:
    """Return current status of the local Metanorma experiment."""
    if METANORMA_REPORT.exists():
        text = METANORMA_REPORT.read_text(encoding="utf-8", errors="replace")
        return json.dumps(
            {
                "report": str(METANORMA_REPORT.relative_to(ROOT)),
                "summary": text[:4000],
            },
            indent=2,
        )
    converter = AUTHORING_ROOT / "tools" / "metanorma" / "bikeshed_to_adoc.py"
    return json.dumps(
        {
            "report_exists": False,
            "converter_exists": converter.exists(),
            "converter": str(converter.relative_to(ROOT)),
        },
        indent=2,
    )


@mcp.tool()
def git_status() -> str:
    """Return a concise git status summary for the repository."""
    status = _run(["git", "status", "--short"], cwd=ROOT)
    branch = _run(["git", "branch", "--show-current"], cwd=ROOT)
    return json.dumps(
        {
            "branch": branch["stdout"].strip(),
            "returncode": status["returncode"],
            "status": [line for line in status["stdout"].splitlines() if line.strip()],
            "stderr": status["stderr"],
        },
        indent=2,
    )


if __name__ == "__main__":
    mcp.run()
