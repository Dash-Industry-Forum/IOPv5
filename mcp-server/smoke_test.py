#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import server


ROOT = Path(__file__).resolve().parents[1]


def check(name: str, ok: bool, details: str = "") -> tuple[str, bool, str]:
    return (name, ok, details)


def main() -> int:
    results: list[tuple[str, bool, str]] = []

    # Basic repository assumptions.
    results.append(check("repo_root", ROOT.exists(), str(ROOT)))
    results.append(check("authoring_root", server.AUTHORING_ROOT.exists(), str(server.AUTHORING_ROOT)))
    results.append(check("specs_root", server.SPECS.exists(), str(server.SPECS)))

    # Tool smoke tests.
    parts = json.loads(server.list_parts())
    results.append(check("list_parts", bool(parts.get("parts")), json.dumps(parts)[:300]))

    docs = json.loads(server.list_documents())
    results.append(check("list_documents", bool(docs.get("documents")), json.dumps(docs)[:300]))

    search = json.loads(server.search_iop("Scope", 3))
    results.append(check("search_iop", "hits" in search, json.dumps(search)[:300]))

    git = json.loads(server.git_status())
    results.append(check("git_status", "branch" in git, json.dumps(git)[:300]))

    broken = json.loads(server.find_broken_refs(5))
    results.append(check("find_broken_refs", "issues" in broken, json.dumps(broken)[:300]))

    report = json.loads(server.search_rag_reports("Metanorma", 3))
    results.append(check("search_rag_reports", "hits" in report, json.dumps(report)[:300]))

    modal = json.loads(server.modal_keyword_report())
    results.append(check("modal_keyword_report", "files" in modal, json.dumps(modal)[:300]))

    failures = [r for r in results if not r[1]]

    print("MCP smoke test results:\n")
    for name, ok, details in results:
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}")
        if details:
            print(f"  {details}")

    if failures:
        print(f"\n{len(failures)} failure(s).")
        return 1

    print("\nAll smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
