# Feature registry (Features × Parts matrix)

This is the tracked matrix of cross-cutting **features** referenced in
`rag-authoring-starter/docs/decisions/0005-status-lifecycle-and-feature-branches.md`.
A feature is a discrete, independently reviewable unit of work that targets
one or more parts. Once a feature reaches **Approved**, it is **Integrated**
into each target part (each gets a `MINOR` version bump and a Change History
row referencing the feature id), and the feature's status becomes
**Integrated** here.

Status values: `Proposed`, `Skeleton`, `Draft`, `WG Review`, `Community
Review`, `Approved`, `Integrated`, `Withdrawn`.

## How to add a feature

1. Add a row to the table below with a new `F-00NN` id.
2. Fill in target parts (use part numbers, comma-separated).
3. Link a tracking issue once one exists.
4. Move the feature through the statuses above as work progresses.
5. On Integration, update each target part's Change History table and version,
   and set this row's status to `Integrated` with the integration date.

## Registry

| Feature | Title | Status | Target parts | Owner | Tracking issue | Notes |
|---|---|---|---|---|---|---|
| F-0001 | Low-latency chunk signalling alignment (audio) | Proposed | 8, 4, 2 | — | — | Align Part 8 segmenting/chunking guidance with Part 4 low-latency model; see Part 8 §"Segmenting and low-latency considerations". |
| F-0002 | Immersive/object-based audio guidance | Proposed | 8, 11 | — | — | Decide ownership between Part 8 (audio-native) and Part 11 (additional technologies) before drafting normative text. |
| F-0003 | Audio selection/accessibility signalling conventions | Proposed | 8, 1, 2 | — | — | Role/accessibility/label combination rules; needs Part 1/2 selection-model alignment. |
| F-0004 | Event taxonomy (MPD / inband / timed metadata) | Proposed | 10, 12 | — | — | Formalize the three event signalling categories introduced in Part 10 and link to Part 12 conformance assets. |
| F-0005 | Event timing model clarification | Proposed | 10, 2 | — | — | Timing semantics relative to Period/segment boundaries; likely needs Part 2 core timing model input. |
| F-0006 | Conformance mapping pass (all parts) | Proposed | 2, 4, 5, 6, 7, 8, 9, 10, 11 | — | — | Systematic pass linking each part's requirements to Part 12 validators/test-assets/reference-player expectations. |
| F-0007 | Cross-part anchor and terminology harmonization | Proposed | All | — | — | Repo-wide editorial pass; see `editorial-backlog` topics in program backlog. |
| F-0008 | PDF/DOC publication path decision | Proposed | All | — | — | Depends on Metanorma PoC outcome (`0004-bikeshed-vs-metanorma.md`); not part-specific but affects all parts' publication pipeline. |
| F-0009 | Part 9 text-track conformance coverage | Skeleton | 9, 12 | — | — | Turn the initial Part 9 conformance mapping into concrete validator, dash.js, and Test Assets coverage for CMAF text profiles, text/video Adaptation Set signalling, CTA 608/708, IMSC1, chunks/gaps, and client text-track selection. |
| F-0010 | Part 5 ad-insertion conformance and cross-part indexing | Skeleton | 1, 2, 5, 6, 10, 12 | — | — | Track Part 5 ad-insertion migration follow-through: conformance mapping, cross-part index entries, Part 2 period/continuity alignment, Part 6 protection alignment, Part 10 event/callback alignment, and Part 12 validator/test-assets coverage. |

> This table starts empty of real owners/issues intentionally — it is the
> mechanism, seeded with the concrete candidates that came out of the Part 8
> and Part 10 work so far. Replace "Proposed" rows with real tracking issues
> as they are opened.

## Matrix view (features × parts)

`x` = target part for that feature.

| Feature | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 | P11 | P12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F-0001 | | x | | x | | | | x | | | | |
| F-0002 | | | | | | | | x | | | x | |
| F-0003 | x | x | | | | | | x | | | | |
| F-0004 | | | | | | | | | | x | | x |
| F-0005 | | x | | | | | | | | x | | |
| F-0006 | | x | x | x | x | x | x | x | x | x | x | |
| F-0007 | x | x | x | x | x | x | x | x | x | x | x | x |
| F-0008 | x | x | x | x | x | x | x | x | x | x | x | x |
| F-0009 | | | | | | | | | x | | | x |
| F-0010 | x | x | | | x | x | | | | x | | x |
