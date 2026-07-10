# DASH-IF IOP v5 Authoring Workspace

This repository is the DASH Industry Forum workspace for authoring, migrating,
building, and reviewing the multi-part **DASH-IF Interoperability Guidelines,
Version 5 (IOP v5)**.

The current authoring path is **Bikeshed-first**: each part is maintained as
Markdown/Bikeshed source and built to HTML. A Metanorma/AsciiDoc proof of concept
is being evaluated for possible DOC/PDF generation, but Bikeshed Markdown remains
the canonical source unless the project decides otherwise.

## What is in this repository

```text
.github/workflows/
  build-pr.yml                 PR build check for all specs
  publish-bikeshed.yml         GitHub Pages publication workflow

rag-authoring-starter/
  specs/
    _boilerplate/              shared IPR/modal-verbs and diagram/table CSS
    part01-overview/           Part 1 source and generated local HTML
    part02-core-cmaf/          Part 2 source: core principles and CMAF mapping
    part03-on-demand/          Part 3 source: on-demand services
    part04-live-low-latency/   Part 4 source: live and low-latency services
    part05-ad-insertion/       Part 5 source/shell: ad insertion
    part06-content-protection/ Part 6 source/shell: content protection
    part07-video/              Part 7 source/shell: video
    part08-audio/              Part 8 source/shell: audio
    part09-text/               Part 9 source/shell: text/subtitles
    part10-events/             Part 10 source/shell: events
    part11-additional-technologies/
                               Part 11 source/shell: additional technologies
    part12-conformance-reference-tools/
                               Part 12 source: conformance and tools

  tools/
    env/                       local Bikeshed/DASH-IF boilerplate setup
    ingest/                    source inventory and text/image extraction
    rag/                       local offline chunk/index/query tools
    migration/                 source delta/migration helpers
    publication/               build and publication checks
    metanorma/                 experimental Bikeshed-to-AsciiDoc tooling

  rag/
    sources.yaml               source manifest
    corpus/                    local source documents (mostly gitignored)
    chunks/, indexes/          derived RAG artifacts (gitignored/generated)
    reports/                   migration/status reports

AGENTS.md                      conventions for AI agents working in this repo
authoring/metanorma/           experimental generated AsciiDoc / outputs (local)
```

## Current part status

| Part | Title | Status in this repo |
|---|---|---|
| 1 | Overview, Architecture and Interfaces | Drafted and building |
| 2 | Core Principles and CMAF Mapping | Initial substantive draft; many open technical issues tracked in the part |
| 3 | On-Demand Services | Initial draft from v4.3 on-demand clauses |
| 4 | Live and Low-Latency Live Services | Drafted and building; more v4.3 live detail remains to migrate |
| 5 | Ad Insertion and Content Replacement | Bikeshed/Markdown shell; substantive migration pending |
| 6 | Content Protection and Security | Bikeshed/Markdown shell; substantive migration pending |
| 7 | Video | Bikeshed/Markdown shell; substantive migration pending |
| 8 | Audio | Bikeshed/Markdown shell; substantive migration pending |
| 9 | Text | Bikeshed/Markdown shell; substantive migration pending |
| 10 | Events | Bikeshed/Markdown shell; substantive migration pending |
| 11 | Additional Technologies | Bikeshed/Markdown shell seeded with trick-mode, thumbnails, metadata-track and registration-process work items |
| 12 | Conformance and Reference Tools | Drafted and building |

## Authoring conventions

Each part follows this structure:

```text
rag-authoring-starter/specs/<part-folder>/
  <part-folder>.bs        Bikeshed metadata, bibliography, shared includes
  NN-*.inc.md             authored prose in Bikeshed-flavoured Markdown
  Images/                 static images and triaged extracted images
  Diagrams/               Mermaid/PlantUML/draw.io sources where applicable
```

Rules of thumb:

- Edit `.bs` and `.inc.md` source files, not generated HTML.
- Keep source provenance in comments or `Issue:` notes when migrating from drafts,
  v4.3, MPEG, or other input documents.
- Use local RAG queries before adding normative technical text, and cite source
  ids/chunks in comments or issue notes where useful.
- Use `<table class="data"><caption>...</caption>` for data tables. Do **not**
  wrap data tables in `<figure>`.
- Use `<figure class="diagram">` only for actual diagrams/images. Do not hardcode
  `Figure 1:` in captions; Bikeshed auto-numbers figures.
- Modal keywords such as ***shall***, ***should***, and ***may*** should be
  lightly emphasized where this improves readability, especially in explanatory
  lists. Do not over-format every occurrence if it makes prose noisy.
- Cross-part references should eventually use stable anchors throughout the part
  set. This is an open editorial task; avoid inventing conflicting anchor names.
- Add examples where they clarify interoperability behaviour. Missing examples
  should be tracked as issues or in the relevant part's open-issues table.

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

Build all parts in place:

```powershell
cd rag-authoring-starter
./build.ps1
```

Build one part:

```powershell
cd rag-authoring-starter
./build.ps1 part02-core-cmaf
```

Build the publication bundle into repository-root `dist/`:

```powershell
cd rag-authoring-starter
python tools/publication/build_all.py --out ../dist
```

Open:

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

Two workflows are present:

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
**Source: GitHub Actions** in the repository settings. After deployment, GitHub
shows the Pages URL in the workflow summary. The expected public URL is typically
of the form:

```text
https://dash-industry-forum.github.io/IOPv5/
```

Recommended workflow policy:

- Pull requests build and expose artifacts for review.
- Only `main` publishes to GitHub Pages.
- Branch previews can be added later if needed, but are not enabled by default.

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

The current experiment targets Part 12 first because it is relatively small and
self-contained. Early findings are documented in `rag-authoring-starter/docs/decisions/0004-bikeshed-vs-metanorma.md`
and follow-up reports under `rag-authoring-starter/rag/reports/`.

## Issue tracking

Use GitHub issues for migration and editorial work. Recommended title format:

```text
[Part 2] Complete SegmentTemplate parameter table
[Part 11] Migrate trick-mode text from v4.3 clause 3.2.9
```

Current issue/backlog seed material is tracked in:

```text
rag-authoring-starter/rag/reports/part02-part03-all-parts-status.md
rag-authoring-starter/rag/reports/editorial-backlog.md
```
