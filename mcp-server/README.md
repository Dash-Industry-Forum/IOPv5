# Local MCP server for DASH-IF IOP v5

This is a very small local MCP server intended for AI-assisted authoring in the
IOPv5 repository. It is deliberately simple: a Python script running on your
machine and exposing a few repository-specific tools.

## MVP tools

- `search_iop(query, limit=10)`
  Search authored source files under `rag-authoring-starter/specs/`.
- `read_clause(path, start_line=None, end_line=None)`
  Read a specific clause/source file or a line range.
- `build_iop(part=None)`
  Run the local Bikeshed build (`build.ps1` or `build_all.py`).
- `git_status()`
  Return a concise git status summary.

## Setup

From the repository root:

```powershell
cd mcp-server
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install mcp
```

If the corporate TLS environment requires it, keep using the same CA bundle
approach already documented for Bikeshed.

## Run

```powershell
cd mcp-server
.\.venv\Scripts\Activate.ps1
python server.py
```

## VS Code / MCP client configuration example

Adjust the path to your local checkout.

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

## Notes

- This server is local-only. It is not intended as a shared or deployed service.
- It assumes the canonical authored source currently lives under
  `rag-authoring-starter/` on the working branch.
- The first version intentionally exposes only read/build/status tools to keep
  the agent interaction predictable.
