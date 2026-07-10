# Local MCP server for DASH-IF IOP v5

This is a very small local MCP server intended for AI-assisted authoring in the
IOPv5 repository. It is deliberately simple: a Python script running on your
machine and exposing a few repository-specific tools.

## Tools

### Core tools

- `search_iop(query, limit=10)`
  Search authored source files under `rag-authoring-starter/specs/`.
- `read_clause(path, start_line=None, end_line=None)`
  Read a specific clause/source file or a line range.
- `build_iop(part=None)`
  Run the local Bikeshed build (`build.ps1`).
- `build_part(part)`
  Build one part by folder name.
- `git_status()`
  Return a concise git status summary.

### Next-step authoring tools

- `list_parts()`
  List available part directories.
- `list_documents(part=None)`
  List authored `.bs`/`.md` source documents, optionally filtered by part.
- `search_part(part, query, limit=10)`
  Search within one specific part only.
- `read_open_issues(part)`
  Return the open-issues/work-items section for a part when present.
- `modal_keyword_report(part=None)`
  Return modal keyword counts across authored files.
- `validate_links()`
  Run the repository publication checker.
- `find_broken_refs(limit=100)`
  Return broken relative links and duplicate headings from authored specs.
- `search_rag_reports(query, limit=10)`
  Search Markdown reports under `rag-authoring-starter/rag/reports/`.
- `build_and_validate_part(part)`
  Build one part and run publication checks.
- `build_publication_bundle()`
  Build the publication bundle into repository-root `dist/`.
- `wrap_modals()`
  Run the modal-keyword normalization helper.
- `generate_issue_seed(part, topic)`
  Generate a simple GitHub issue title/body seed from part context.
- `read_change_history(part)`
  Return the change-history section for a part when present.
- `part_status_report(part)`
  Summarize documents, open issues, change history, and modal counts for one part.
- `metanorma_status()`
  Return the current status of the local Metanorma experiment/report.

## Setup

From the repository root:

```powershell
cd mcp-server
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

A helper startup script is also provided:

```powershell
cd mcp-server
./start.ps1
```

To recreate the virtual environment from scratch:

```powershell
cd mcp-server
./start.ps1 -RecreateVenv
```

If the corporate TLS environment requires it, keep using the same CA bundle
approach already documented for Bikeshed.

## Run

Manual start:

```powershell
cd mcp-server
.\.venv\Scripts\Activate.ps1
python server.py
```

Convenience start:

```powershell
cd mcp-server
./start.ps1
```

## VS Code / MCP client configuration example

A ready-made example file is included:

```text
mcp-server/vscode-mcp-config.example.json
```

Adjust the path to your local checkout. Example:

```json
{
  "mcpServers": {
    "iopv5": {
      "command": "python",
      "args": [
        "C:\\Users\\tsto\\OneDrive - Qualcomm\\Projects\\DASH-IF\\IOP\\IOPv5\\mcp-server\\server.py"
      ]
    }
  }
}
```

## Smoke test

A small local smoke test is included:

```powershell
cd mcp-server
.\.venv\Scripts\Activate.ps1
python smoke_test.py
```

This checks that the repository paths are present and that a representative set
of MCP tool functions can be invoked locally.

## Notes

- This server is local-only. It is not intended as a shared or deployed service.
- It assumes the canonical authored source currently lives under
  `rag-authoring-starter/` on the working branch.
- The first version intentionally exposes only read/build/status tools to keep
  the agent interaction predictable.
