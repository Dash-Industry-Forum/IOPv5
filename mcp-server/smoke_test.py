#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import server

ROOT = Path(__file__).resolve().parents[1]


class Result(dict):
    pass


def result(name: str, status: str, details: str = "") -> Result:
    return Result(name=name, status=status, details=details)


def main() -> int:
    results: list[Result] = []

    results.append(result("repo_root", "PASS" if ROOT.exists() else "FAIL", str(ROOT)))
    results.append(
        result(
            "authoring_root",
            "PASS" if server.AUTHORING_ROOT.exists() else "WARN",
            str(server.AUTHORING_ROOT),
        )
    )
    results.append(
        result(
            "specs_root",
            "PASS" if server.SPECS.exists() else "WARN",
            str(server.SPECS),
        )
    )

    try:
        git = json.loads(server.git_status())
        results.append(result("git_status", "PASS" if "branch" in git else "FAIL", json.dumps(git)[:300]))
    except Exception as exc:
        results.append(result("git_status", "FAIL", repr(exc)))

    try:
        parts = json.loads(server.list_parts())
        status = "PASS" if parts.get("parts") else "WARN"
        results.append(result("list_parts", status, json.dumps(parts)[:300]))
    except Exception as exc:
        results.append(result("list_parts", "FAIL", repr(exc)))

    try:
        docs = json.loads(server.list_documents())
        status = "PASS" if docs.get("documents") else "WARN"
        results.append(result("list_documents", status, json.dumps(docs)[:300]))
    except Exception as exc:
        results.append(result("list_documents", "FAIL", repr(exc)))

    try:
        search = json.loads(server.search_iop("Scope", 3))
        status = "PASS" if search.get("hits") else "WARN"
        results.append(result("search_iop", status, json.dumps(search)[:300]))
    except Exception as exc:
        results.append(result("search_iop", "FAIL", repr(exc)))

    try:
        broken = json.loads(server.find_broken_refs(5))
        status = "PASS" if "issues" in broken else "FAIL"
        results.append(result("find_broken_refs", status, json.dumps(broken)[:300]))
    except Exception as exc:
        results.append(result("find_broken_refs", "FAIL", repr(exc)))

    try:
        report = json.loads(server.search_rag_reports("Metanorma", 3))
        status = "PASS" if report.get("hits") else "WARN"
        results.append(result("search_rag_reports", status, json.dumps(report)[:300]))
    except Exception as exc:
        results.append(result("search_rag_reports", "FAIL", repr(exc)))

    try:
        modal = json.loads(server.modal_keyword_report())
        status = "PASS" if modal.get("files") else "WARN"
        results.append(result("modal_keyword_report", status, json.dumps(modal)[:300]))
    except Exception as exc:
        results.append(result("modal_keyword_report", "FAIL", repr(exc)))

    failures = [r for r in results if r["status"] == "FAIL"]
    warnings = [r for r in results if r["status"] == "WARN"]

    print("MCP smoke test results:\n")
    for r in results:
        print(f"[{r['status']}] {r['name']}")
        if r["details"]:
            print(f"  {r['details']}")

    if failures:
        print(f"\n{len(failures)} failure(s), {len(warnings)} warning(s).")
        return 1

    if warnings:
        print(f"\nSmoke test completed with {len(warnings)} warning(s).")
        return 0

    print("\nAll smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

