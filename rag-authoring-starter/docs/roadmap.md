# DASH-IF IOP v5 RAG Authoring Roadmap

## Objective

Make `Dash-Industry-Forum/IOPv5` the primary workspace for DASH-IF IOP v5 source authoring, migration, publication, issue tracking, and RAG-assisted development.

## Phase 0: Governance and inventory

- Establish repository structure.
- Add source manifest.
- Generate document inventory.
- Define labels, issue templates, and document status vocabulary.
- Identify public versus private corpus inputs.

## Phase 1: Authoring baseline

- Keep Bikeshed as the initial canonical authoring path.
- Maintain a Metanorma proof-of-concept template for evaluation.
- Add DASH-IF cover page, IPR notice, modal verbs, and change-history boilerplate.
- Create one folder per IOP v5 part.

## Phase 2: RAG corpus and index

- Extract text from DOCX/PDF sources.
- Chunk by headings and section numbers.
- Preserve status and provenance metadata.
- Build a local vector index.
- Provide CLI queries for cross-document comparison and migration support.

## Phase 3: Part 4 pilot

Pilot `Part 4: Live and Low-Latency Services`.

Primary inputs:

- IOP v5 Part 4 draft.
- Low Latency CR r8.
- Low Latency CR r9.
- MPEG DASH 2026 merged draft.
- CMAF 2024.

Expected pilot outputs:

- r8/r9 delta report.
- list of section conflicts and unresolved editor notes.
- migration recommendations for Addressable Resync Representations and Segment Sequence related text.
- first Bikeshed source draft for Part 4.

## Phase 4: Published part baselines

Import or reference published baselines for:

- Part 1
- Part 5
- Part 6
- Part 7
- Part 8
- Part 9
- Part 10

Each imported part should include:

- source status,
- publication URL,
- bug tracker,
- maintainer,
- known pending updates.

## Phase 5: v4.3 migration

Create a mapping from v4.3 sections to v5 parts.

Initial mapping:

| v4.3 area | v5 target |
|---|---|
| Usage of MPEG-DASH | Part 2, Part 3, Part 11 |
| Live Services | Part 4 |
| Ad Insertion | Part 5 |
| Media Coding Technologies | Parts 7, 8, 9 |
| Content Protection and Security | Part 6 |
| Trick modes and thumbnails | Part 11 |
| Events | Part 10 |
| Conformance and test tools | Part 12 |

## Phase 6: Website and publication automation

- Maintain `website/iop-v5.md`.
- Maintain `website/publication-manifest.yaml`.
- Generate build artefacts for HTML/PDF.
- Add link checks.
- Add reference checks.
- Add normative keyword and terminology checks.