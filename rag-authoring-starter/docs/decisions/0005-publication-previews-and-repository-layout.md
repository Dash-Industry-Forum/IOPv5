# ADR 0005: Preview publication and repository layout direction

- Status: accepted
- Date: 2026

## Context

The repository now contains buildable Bikeshed sources for all IOP v5 parts, but
most work lives under `rag-authoring-starter/`, a name that no longer reflects the
intended long-term repository structure. Editors also need a way to review branch
content as a web publication before merging to `main`.

GitHub Pages provides one live Pages deployment per repository. This matters for
branch previews: deploying a preview through Pages can temporarily replace the
currently visible Pages deployment until the official publication workflow runs
again.

## Decision: preview publication

Use a staged preview strategy.

### Immediate

Add a manual-only workflow, `.github/workflows/preview-bikeshed.yml`, that builds
the selected branch and deploys it as an unadvertised/noindex GitHub Pages
preview under:

```text
/previews/<preview-name>/
```

This is intended for temporary editorial/publication review only. It is not
private, and it may replace the current Pages deployment until the `main`
publication workflow is run again.

### Longer term

If branch previews become routine, create a separate preview Pages environment
(preferred) or switch to a `gh-pages` branch strategy with stable preview
subdirectories and cleanup of old previews. A separate preview site avoids
confusion between official publication and branch previews.

## Decision: repository layout direction

Keep the current layout for this development branch, but plan a follow-up
repository-layout cleanup before declaring the repository production-ready.

Preferred final layout:

```text
specs/                  canonical Bikeshed sources
rag/                    source manifest, local/derived RAG data, reports
tools/                  ingest, RAG, migration, publication, Metanorma tools
docs/                   roadmap, ADRs, migration notes
authoring/              optional generated/experimental authoring outputs
.github/                workflows and templates
```

In other words, move the contents of `rag-authoring-starter/` up one level once
the project agrees that this repository is no longer merely a starter scaffold.

## Consequences

- The current branch remains stable and buildable without a large path move.
- Workflows and scripts continue using `rag-authoring-starter/` for now.
- A future path move will require updates to:
  - workflows;
  - `build.ps1` / `build_all.py` assumptions;
  - README examples;
  - `AGENTS.md` instructions;
  - local documentation links.
- The move should be done in one dedicated commit to preserve reviewability.
