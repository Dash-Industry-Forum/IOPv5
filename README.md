# DASH-IF IOP v5 Authoring Workspace

This repository is the DASH Industry Forum workspace for authoring, migrating,
building, and reviewing the multi-part **DASH-IF Interoperability Guidelines,
Version 5 (IOP v5)**.

The current authoring path is **Bikeshed-first**: each part is maintained as
Markdown/Bikeshed source and built to HTML. A Metanorma/AsciiDoc proof of concept
is being evaluated for possible DOC/PDF generation, but Bikeshed Markdown remains
the canonical source unless the project decides otherwise.

## Quick Links

| Resource | URL |
|----------|-----|
| Official publication | https://dashif.org/Guidelines/iop-v5/ |
| Preview (current branch) | https://dashif.org/IOPv5/previews/tstockhammer-rag-workflow/ |
| Issue tracker | https://github.com/Dash-Industry-Forum/IOPv5/issues |
| DASH-IF Identifier Registry | https://dashif.org/identifiers/introduction/ |
| DASH-IF Codec Registry | https://dashif.org/codecs/introduction/ |

## What is in this repository

```text
.github/workflows/
  build-pr.yml                 PR build check for all specs
  publish-bikeshed.yml         GitHub Pages publication workflow from main
  preview-bikeshed.yml         manual temporary Pages preview for review branches

rag-authoring-starter/
  specs/
    _boilerplate/              shared IPR/modal-verbs and diagram/table CSS
    part01-overview/           Part 1: Overview, Architecture and Interfaces
    part02-core-cmaf/          Part 2: Core Principles and CMAF Mapping
    part03-on-demand/          Part 3: On-Demand Services
    part04-live-low-latency/   Part 4: Live and Low-Latency Services
    part05-ad-insertion/       Part 5: Ad Insertion and Content Replacement
    part06-content-protection/ Part 6: Content Protection and Security
    part07-video/              Part 7: Video
    part08-audio/              Part 8: Audio
    part09-text/               Part 9: Text (Subtitle)
    part10-events/             Part 10: Events
    part11-additional-technologies/
                               Part 11: Additional Functionalities
    part12-conformance-reference-tools/
                               Part 12: Conformance and Reference Tools

  tools/
    env/                       local Bikeshed/DASH-IF boilerplate setup
    ingest/                    source inventory and text/image extraction
    rag/                       local offline chunk/index/query tools
    migration/                 source delta/migration helpers
    publication/               build and publication checks (build_all.py)
    validation/                per-part MPD validation scripts
    metanorma/                 experimental Bikeshed-to-AsciiDoc tooling

  rag/
    sources.yaml               source manifest
    corpus/                    local source documents (mostly gitignored)
    chunks/, indexes/          derived RAG artifacts (gitignored/generated)
    reports/                   migration/status reports (see below)

AGENTS.md                      conventions for AI agents working in this repo
PULL_REQUEST_TEMPLATE.md       PR template with checklist
```

## Current part status

All 12 parts are in the Bikeshed authoring workspace as Working Draft documents.
The publication infrastructure (CI workflow, `build_all.py`, shared boilerplate,
image copying) is operational.

| Part | Title | WD Version | Status |
|------|-------|-----------|--------|
| 1 | Overview, Architecture and Interfaces | 0.3 | Substantially complete: architecture, registries, review workflow |
| 2 | Core Principles and CMAF Mapping | 0.1 | Substantial content: full timing model, CMAF mapping, Period splitting |
| 3 | On-Demand Services | 0.1 | Skeleton with initial MPD requirements |
| 4 | Live and Low-Latency Services | 0.3 | Live services + low-latency (CR r8/r9) migrated |
| 5 | Ad Insertion and Content Replacement | 0.12 | Substantial: IF-0 through IF-9 migrated from published v5.0.0 |
| 6 | Content Protection and Security | — | Substantial: DRM workflows, license model, ECCP |
| 7 | Video | — | Substantial: codec profiles, CMAF signalling |
| 8 | Audio | — | Substantial: codec profiles, CMAF signalling |
| 9 | Text (Subtitle) | — | Reconciled against published Part 9 FINAL |
| 10 | Events | 0.4 | Events model, timed metadata, cross-refs to Parts 4 and 5 |
| 11 | Additional Functionalities | 0.1 | Skeleton with issue placeholders only |
| 12 | Conformance and Reference Tools | 0.6 | Substantially complete; conformance mappings for all parts |

For a detailed per-part status with done/remaining checklists, see:

```text
rag-authoring-starter/rag/reports/iop-v5-authoring-status.md
```

## Authoring conventions

Each part follows this structure:

```text
rag-authoring-starter/specs/<part-folder>/
  <part-folder>.bs        Bikeshed metadata, bibliography, shared includes
  NN-*.inc.md             authored prose in Bikeshed-flavoured Markdown
  images/ or Images/      static images and triaged extracted images
  Diagrams/               Mermaid/PlantUML/draw.io sources where applicable
```

### Bikeshed metadata

Every `.bs` file uses the following custom metadata fields:

```
!Repository: <a href="https://github.com/Dash-Industry-Forum/IOPv5">Dash-Industry-Forum/IOPv5</a>
!Issue Tracking: File issues at <a href="...">IOPv5 GitHub</a>. Use label <code>Part N</code>.
!Document Status: Working Draft (x.y). See Part 1 §1 for versioning.
```

### Rules of thumb

- Edit `.bs` and `.inc.md` source files, not generated HTML.
- Keep source provenance in comments or `Issue:` notes when migrating from drafts,
  v4.3, MPEG, or other input documents.
- Use local RAG queries before adding normative technical text, and cite source
  ids/chunks in comments or issue notes where useful.
- Use `<table class="data"><caption>...</caption>` for data tables. Do **not**
  wrap data tables in `<figure>`.
- Use `<figure class="diagram">` only for actual diagrams/images. Do not hardcode
  `Figure 1:` in captions; Bikeshed auto-numbers figures.
- Modal keywords such as ***shall***, ***should***, and ***may*** are formatted
  consistently in authored spec text using `<span class=modal-keyword>...</span>`.
  Run `python tools/publication/wrap_modals.py` after broad edits to normalize
  modal-keyword presentation.
- Every section that has subsections **must not** have hanging paragraphs (text
  between the section heading and the first subsection heading). Add a
  `### General ### {#section-id-general}` subsection if needed.
- Cross-part references should eventually use stable anchors throughout the part
  set. This is an open editorial task; avoid inventing conflicting anchor names.
- Add examples where they clarify interoperability behaviour. Missing examples
  should be tracked as issues or in the relevant part's open-issues table.

## DASH-IF Registries

DASH-IF maintains two registries that are authoritative for identifiers and
codecs used in DASH-IF compliant services:

- **[DASH-IF Identifier Registry](https://dashif.org/identifiers/introduction/)**
  — `@schemeIdUri` values, profile URIs, and other string identifiers.
  Source: [Dash-Industry-Forum/Identifiers](https://github.com/Dash-Industry-Forum/Identifiers)
- **[DASH-IF Codec Registry](https://dashif.org/codecs/introduction/)**
  — `@codecs` strings and CMAF profiles.
  Source: [Dash-Industry-Forum/Codecs](https://github.com/Dash-Industry-Forum/Codecs)

To register a new identifier, use the
[DASH-IF Identifier Registration Form](https://docs.google.com/forms/d/e/1FAIpQLSfoMH4BL-1VwEpnVrYSnlvzwdO_7VAFeP1OfifxKW7nXVeWjg/viewform)
or file an issue at [Dash-Industry-Forum/Identifiers/issues](https://github.com/Dash-Industry-Forum/Identifiers/issues).

See Part 1 §4 (DASH-IF Registries) for the full description and registration
workflow.

## Contributing and Reviewing

### Filing issues

All issues, bugs, and feature requests for DASH-IF IOP v5 should be submitted
through the single IOPv5 issue tracker:

```text
https://github.com/Dash-Industry-Forum/IOPv5/issues
```

Use the label `Part N` or the title prefix `[Part N]:` to identify the relevant
part (e.g. `[Part 2]: Clarify @timescale requirement`).

### Submitting pull requests

1. Fork the IOPv5 repository.
2. Create a branch from `main` with a descriptive name.
3. Edit the relevant `.inc.md` or `.bs` files in `rag-authoring-starter/specs/`.
4. Build locally to verify (see below).
5. Submit a pull request against `main`. Reference the issue(s) the PR addresses.

### Review phases

- **Working Draft**: file issues or PRs at any time.
- **WG Review**: WG members review the release candidate; file issues or PRs.
- **Community Review**: anyone may file issues with label `Community Review`.

See Part 1 §1.4 (Contributing and Reviewing) for the full workflow.

## Local setup

From `rag-authoring-starter/`:

```powershell
pip install -r requirements.txt
pip install bikeshed
python tools/env/build_ca_bundle.py
$env:REQUESTS_CA_BUNDLE = "$PWD\build-tools\corp-ca-bundle.pem"
$env:SSL_CERT_FILE      = $env:REQUESTS_CA_BUNDLE
python -m bikeshed update
python tools/env/install_dashif_boilerplate.py
```

The CA bundle step is needed on machines behind a corporate TLS-intercepting
proxy. Do not disable TLS verification.

## Building locally

Build all parts into `dist/`:

```powershell
cd rag-authoring-starter
python tools/publication/build_all.py --out ../dist
```

Build one part in place:

```powershell
cd rag-authoring-starter
./build.ps1 part02-core-cmaf
```

Open the result:

```text
dist/index.html
```

The generated `dist/` directory and `specs/**/*.html` files are build outputs and
are gitignored.

## Publication checks

Run before committing:

```powershell
cd rag-authoring-starter
python tools/publication/check_links.py
```

This checks authored sources for broken local links, duplicate headings, and
modal-keyword counts.

## RAG / migration tooling

The local RAG flow is offline-first and provenance-oriented:

```powershell
cd rag-authoring-starter
python tools/ingest/build_inventory.py
python tools/ingest/extract_text.py
python tools/ingest/extract_images.py
python tools/rag/chunk.py
python tools/rag/build_index.py
python tools/rag/query.py "SegmentTemplate SegmentTimeline" --part part02-core-cmaf
python tools/migration/delta_report.py dashif-iop-v4-3 dashif-iop-v5-part2-draft
```

Many corpus documents are access-controlled and intentionally gitignored. Do not
commit unpublished DASH-IF drafts, proprietary MPEG documents, or extracted
binary images unless publication rights are confirmed.

## GitHub Actions and GitHub Pages publication

Three workflows are present:

### Pull-request build

```text
.github/workflows/build-pr.yml
```

Runs on pull requests to `main` when spec sources or the workflow change. It:

1. installs Python and Bikeshed,
2. updates Bikeshed data,
3. installs the DASH-IF Bikeshed boilerplate/group,
4. builds all specs into `dist/`, and
5. uploads the `dist` folder as a workflow artifact.

Use this for review builds before merging.

### Temporary branch preview

```text
.github/workflows/preview-bikeshed.yml
```

This is the immediate review environment. It is manual-only (`workflow_dispatch`)
and is intended for publication-style review of a branch before merge.

It builds the selected branch and deploys a **temporary preview-only** GitHub
Pages artifact with a URL path such as:

```text
https://dashif.org/IOPv5/previews/tstockhammer-rag-workflow/
```

Important limitations:

- The URL is unadvertised and pages are marked `noindex,nofollow`, but the
  preview is **not private**.
- GitHub Pages has one live deployment per repository. While a preview deployment
  is active, it replaces the repository Pages deployment until the main
  publication workflow is run again.
- Do not use preview deployments for confidential drafts or access-controlled
  material.

Use this workflow when colleagues need a real browser/publication view without
checking out the repository or downloading artifacts.

### GitHub Pages publication

```text
.github/workflows/publish-bikeshed.yml
```

Runs on pushes to `main` that touch spec sources, and can also be run manually
with `workflow_dispatch`. It:

1. builds all specs into `dist/`,
2. uploads `dist` as a Pages artifact, and
3. deploys it using `actions/deploy-pages`.

For publication to work, repository administrators must enable GitHub Pages with
**Source: GitHub Actions** in the repository settings. The expected public URL is:

```text
https://dashif.org/Guidelines/iop-v5/
```

Recommended workflow policy:

- Pull requests build and expose artifacts for review.
- Manual branch previews are allowed for temporary publication-style review.
- Only `main` is the official publication source.
- After a temporary preview, rerun the main publication workflow to restore the
  official Pages deployment.

## Document Status and Versioning

IOP v5 uses a **two-branch model**:

- **`main` branch** — Working Draft. All development happens here. Preview
  publications are built from `main`.
- **`stable` branch** — Approved/stable. Updated when a version is formally
  approved. Official publications are built from `stable`.

Version numbers:
- `0.x` — Working Draft
- `1.0-rc` — WG Review release candidate
- `1.0-beta` — Community Review
- `1.x` — Approved

See Part 1 §1.2 (Stable and Development Versions) for the full workflow.

## Metanorma / AsciiDoc experiment

A proof-of-concept converter is under:

```text
rag-authoring-starter/tools/metanorma/bikeshed_to_adoc.py
```

The intended model is:

```text
Bikeshed Markdown source  ->  generated AsciiDoc  ->  Metanorma HTML/DOC/PDF
```

Bikeshed Markdown remains canonical. Generated AsciiDoc should not become a
second edited source of truth unless the project explicitly changes policy.

## Issue tracking

Use GitHub issues for migration and editorial work. Recommended title format:

```text
[Part 2] Complete SegmentTemplate parameter table
[Part 11] Migrate trick-mode text from v4.3 clause 3.2.9
```

## Status reports

Current status and remaining tasks:

```text
rag-authoring-starter/rag/reports/iop-v5-authoring-status.md   ← primary status (2026-07-28)
rag-authoring-starter/rag/reports/project-status-update-2026-07-21.md
rag-authoring-starter/rag/reports/editorial-backlog.md
rag-authoring-starter/rag/reports/part05-f0010-issue-index.md
```

The `iop-v5-authoring-status.md` report contains:
- Per-part done/remaining checklists for all 12 parts
- Infrastructure status table
- Cross-cutting remaining tasks (high/medium/low priority)