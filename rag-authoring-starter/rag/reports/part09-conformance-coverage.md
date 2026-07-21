# Part 9 text-track conformance coverage checklist

Generated: 2026-07-21

This report expands feature `F-0009` from
`docs/governance/feature-registry.md` into a concrete coverage checklist for
DASH-IF IOP v5 Part 9, *Text*.

Related source locations:

- Part 9 source: `specs/part09-text/09-text.inc.md`
- Part 9 reconciliation: `rag/reports/reconcile-part09-text.md`
- Part 12 conformance mapping:
  `specs/part12-conformance-reference-tools/01-conformance.inc.md`
  / `#tools-part9-text-conformance`
- Feature registry: `docs/governance/feature-registry.md` / `F-0009`

## Objective

Turn the initial Part 9 conformance mapping into actionable validator, dash.js,
and Test Assets coverage work.

This report is intentionally a planning/checklist artifact. It does not assert
that the listed validator or reference-player checks already exist. The next
step is to reconcile each row against actual DASH-IF Conformance Validator,
dash.js, livesim2, and Test Assets Database coverage.

## Coverage matrix

| ID | Part 9 feature | Requirement/source area | Validator coverage target | dash.js / reference-player target | Test Assets target | Current status | Next action |
|---|---|---|---|---|---|---|---|
| P9-COV-001 | CMAF text media profiles | `#text-cmaf-media-profiles`; Table 1 | Check `@mimeType`, `@codecs`, CMAF file brand/profile consistency for IMSC1 Text, IMSC1 Image, WebVTT, and CTA 608/708-in-video cases where detectable. | Confirm dash.js can expose/select supported text tracks signalled with IMSC1/WebVTT CMAF profiles. | Add or identify assets for `im1t`/`stpp.ttml.im1t`, `im1i`/`stpp.ttml.im1i`, `cwvt`/`wvtt`, and `ccea` in video. | Planned | Inventory validator support for text CMAF profile checks and identify existing test vectors. |
| P9-COV-002 | Text-track Adaptation Set signalling | `#text-tracks`; Table 2 | Check text Adaptation Set `@mimeType`, `@codecs`, `@lang`, `Accessibility`, and `Role` usage against Part 9 requirements. | Confirm client selection uses language, role/accessibility, codec support, and selection priority where applicable. | Add or identify assets with alternative subtitle/caption/easyreader tracks differing by language, codec, role, and accessibility. | Planned | Compare Part 9 Table 2 rows against current validator MPD checks. |
| P9-COV-003 | CTA 608/708 closed captions in video tracks | `#video-tracks`; `#codecs-cea608`; Table 3 | Check video Adaptation Set `Accessibility` descriptor for CTA 608/708 closed-caption signalling, including scheme URI and `@value` syntax for CEA-608. | Confirm reference-player behaviour with video-carried captions and user selection/exposure where supported. | Add or identify assets for `CC1=eng;CC3=spa`, single-language shorthand, and multi-channel cases where language-only shorthand is not used. | Planned | Inventory SCTE caption-service signalling support in validator and dash.js sample assets. |
| P9-COV-004 | IMSC1 storage and signalling | `#codecs-imsc1`; IMSC1 signalling table | Check MPD signalling for IMSC1 text tracks, including `application/ttml+xml` standalone XML and `application/mp4` ISO BMFF encapsulation. | Confirm playback/rendering of supported IMSC1 text tracks and graceful handling of unsupported IMSC1 feature subsets. | Add or identify ISO BMFF IMSC1 and standalone XML IMSC1 assets, including converted CEA-608/708-to-IMSC1 cases where applicable. | Planned | Determine which IMSC1 variants are currently supported in dash.js samples and validator test vectors. |
| P9-COV-005 | Chunks and gaps | `#chunks-and-gaps` | Check that text tracks are not chunked contrary to Part 9 guidance where this can be detected, and that periods with no text content still provide continuous empty documents. | Confirm clients handle empty text documents/gaps without track-selection or rendering failures. | Add or identify assets with periods of no text content and empty documents conforming to ISO/IEC 14496-30, plus short-duration IMSC1 segments respecting HRM. | Planned | Identify validator feasibility for text chunking/gap checks and required test assets. |
| P9-COV-006 | Client text-track selection | `#client-recommendations` | Validator documents signalling inputs; client selection behaviour is primarily a reference-player/test-case target. | Confirm dash.js selection handling for unsupported `EssentialProperty`, unsupported codecs, absent/null/`und` language, preferred language filtering, unsupported Role values, and `@selectionPriority`. | Add or identify multi-track assets covering positive and negative selection cases. | Planned | Map each Part 9 selection step to a dash.js sample/test or file a coverage issue. |
| P9-COV-007 | Cross-part alignment | Part 9 references to Parts 2, 7, and 12 | Ensure validator checks align with Part 2 core Adaptation Set rules and Part 7 video-track text/open-caption guidance. | Confirm client behaviour does not conflict with Part 2 selection model or Part 7 video behaviour. | Add or identify combined audio/video/text presentations that exercise cross-part interactions. | Planned | Review Part 2 and Part 7 requirements that overlap with Part 9 signalling. |

## Suggested issue breakdown

When GitHub issues are opened, use one issue per coverage cluster rather than one
large umbrella issue:

1. `F-0009: validator coverage for Part 9 CMAF text profiles and text Adaptation Sets`
2. `F-0009: validator and sample coverage for CTA 608/708 in video tracks`
3. `F-0009: IMSC1/WebVTT text-track sample coverage in dash.js and Test Assets`
4. `F-0009: chunks/gaps and empty-document test assets`
5. `F-0009: client text-track selection behaviour coverage`
6. `F-0009: cross-part alignment with Parts 2, 7, and 12`

## Validation notes

This report should be kept in sync with:

- `docs/governance/feature-registry.md` (`F-0009`)
- `specs/part12-conformance-reference-tools/01-conformance.inc.md`
- `rag/reports/reconcile-part09-text.md`

After editing related Part 9 or Part 12 source, run:

```powershell
python tools/publication/check_links.py
```

Bikeshed HTML build validation remains dependent on resolving the corporate
TLS/Bikeshed remote-data update issue already documented in the Part 6
reconciliation report.