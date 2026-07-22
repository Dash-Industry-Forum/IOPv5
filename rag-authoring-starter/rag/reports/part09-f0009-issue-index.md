# F-0009 Part 9 text conformance issue index

Generated: 2026-07-22

This issue index converts `rag/reports/part09-conformance-coverage.md` into
implementation-oriented work items for Part 9 text, caption, and subtitle
conformance coverage.

Related source:

```text
specs/part09-text/09-text.inc.md
rag/reports/reconcile-part09-text.md
rag/reports/part09-conformance-coverage.md
specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part9-text-conformance
docs/governance/feature-registry.md#F-0009
```

## Issue F-0009-T1: Validator coverage for CMAF text media profiles

### Scope

Implement or confirm validator checks for CMAF text media profiles and MPD
signalling for text Adaptation Sets.

### Source coverage

```text
P9-COV-001
specs/part09-text/09-text.inc.md#text-cmaf-media-profiles
```

### Validator targets

- Check `AdaptationSet@mimeType` for text media:
  - `application/mp4`,
  - `application/ttml+xml`,
  - `text/vtt`,
  - WebVTT/TTML variants used by the current source text.
- Check `Representation@codecs` values for:
  - IMSC1 Text (`im1t`, `stpp.ttml.im1t`),
  - IMSC1 Image (`im1i`, `stpp.ttml.im1i`),
  - WebVTT (`cwvt`, `wvtt`),
  - CTA 608/708 carried in video where signalled by accessibility descriptors.
- Check CMAF brand/profile consistency where segment metadata is available.

### Test assets

- Positive: one valid fixture per supported text profile.
- Negative: mismatched `@mimeType`/`@codecs`, missing codecs, unsupported text
  codec, and profile/brand mismatch where detectable.

### Initial local implementation

Validator-start script:

```text
tools/validation/validate_part9_text_mpd.py
```

Initial fixtures:

```text
specs/part09-text/examples/text/valid-text-tracks.mpd
specs/part09-text/examples/text/invalid-text-tracks.mpd
```

### Acceptance criteria

- Validator emits deterministic findings for MPD-level signalling errors.
- Gaps requiring segment-level inspection are documented as such.

## Issue F-0009-T2: Validator coverage for text-track Adaptation Set signalling

### Scope

Implement or confirm checks for text Adaptation Set signalling, language,
role/accessibility, and selection-related MPD attributes.

### Source coverage

```text
P9-COV-002
specs/part09-text/09-text.inc.md#text-tracks
```

### Validator targets

- `AdaptationSet@contentType` / `@mimeType` consistency for text tracks.
- `AdaptationSet@lang` presence and syntax where required.
- `Role` descriptor values for subtitle/caption/easy-reader variants.
- `Accessibility` descriptor presence and syntax for captions and accessibility
  services.
- `@selectionPriority` syntax where used.

### Test assets

- Multiple alternative text Adaptation Sets differing by:
  - language,
  - role,
  - accessibility,
  - codec,
  - selection priority.

### Initial local implementation

The validator-start script and initial fixtures listed in F-0009-T1 also cover
the first MPD-level T2 signalling checks for language, role/accessibility, codec,
and selection priority.

### Acceptance criteria

- Positive multi-track asset validates.
- Negative fixtures isolate missing/invalid language, role/accessibility, and
  codec signalling.

## Issue F-0009-T3: CTA 608/708 caption signalling coverage

### Scope

Cover CTA 608/708 closed-caption signalling carried in video Adaptation Sets.

### Source coverage

```text
P9-COV-003
specs/part09-text/09-text.inc.md#video-tracks
specs/part09-text/09-text.inc.md#codecs-cea608
```

### Validator targets

- Check the video Adaptation Set `Accessibility` descriptor scheme URI used for
  CTA 608/708 signalling.
- Validate CEA-608 `@value` patterns:
  - `CC1=eng`,
  - `CC1=eng;CC3=spa`,
  - single-language shorthand where allowed,
  - multi-channel cases where shorthand is not used.

### Reference-player targets

- Confirm dash.js exposes video-carried captions where supported.
- Confirm selection behavior for multiple channel/language mappings.

### Test assets

- Positive CTA 608/708-in-video assets.
- Negative syntax assets for malformed channel/language mappings.

### Initial local implementation

The Part 9 text MPD validator now checks CEA-608 and CEA-708 video-carried
caption Accessibility descriptor syntax and duplicate channel/service entries.

Initial fixtures:

```text
specs/part09-text/examples/cea-captions/valid-cea608-multichannel.mpd
specs/part09-text/examples/cea-captions/valid-cea608-shorthand.mpd
specs/part09-text/examples/cea-captions/valid-cea708-service.mpd
specs/part09-text/examples/cea-captions/invalid-cea608-channel.mpd
specs/part09-text/examples/cea-captions/invalid-cea608-duplicate-channel.mpd
specs/part09-text/examples/cea-captions/invalid-cea708-service.mpd
specs/part09-text/examples/cea-captions/invalid-cea708-duplicate-service.mpd
```

## Issue F-0009-T4: IMSC1 and WebVTT storage/sample coverage

### Scope

Identify and add sample coverage for IMSC1 and WebVTT text tracks.

### Source coverage

```text
P9-COV-004
specs/part09-text/09-text.inc.md#codecs-imsc1
```

### Coverage targets

- ISO BMFF encapsulated IMSC1.
- Standalone XML IMSC1 where retained for compatibility.
- WebVTT in ISO BMFF and/or standalone delivery where specified.
- Converted CEA-608/708-to-IMSC1 cases where applicable.

### Acceptance criteria

- Test assets exist or are explicitly referenced from DASH-IF Test Assets.
- dash.js playback/rendering support is either confirmed or tracked as a
  reference-player gap.

## Issue F-0009-T5: Chunks, gaps, and empty-document test assets

### Scope

Cover text-track chunking and gap behavior.

### Source coverage

```text
P9-COV-005
specs/part09-text/09-text.inc.md#chunks-and-gaps
```

### Validator targets

- Detect text-track chunking that conflicts with Part 9 guidance where MPD or
  segment metadata makes this possible.
- Check that periods with no rendered text still provide continuous empty
  documents where required.

### Test assets

- Empty-document gap assets.
- Periods with no text content.
- Short-duration IMSC1 segments respecting HRM.

### Acceptance criteria

- Validator feasibility is documented for MPD-only versus segment-level checks.
- At least one positive and one negative asset are identified or planned.

## Issue F-0009-T6: Client text-track selection behavior coverage

### Scope

Create dash.js/reference-client test coverage for Part 9 client selection
behavior.

### Source coverage

```text
P9-COV-006
specs/part09-text/09-text.inc.md#client-recommendations
```

### Reference-player targets

- Preferred language selection.
- Unsupported `EssentialProperty` handling.
- Unsupported codec handling.
- Absent/null/`und` language behavior.
- Unsupported `Role` behavior.
- `@selectionPriority` behavior.

### Test assets

- Multi-track positive assets.
- Negative/edge-case selection assets.

### Acceptance criteria

- Each selection rule maps to a dash.js sample/test or an explicit coverage gap.

## Issue F-0009-T7: Cross-part alignment with Parts 2, 7, and 12

### Scope

Reconcile Part 9 text signalling with overlapping requirements in Parts 2, 7,
and 12.

### Source coverage

```text
P9-COV-007
```

### Alignment targets

- Part 2 Adaptation Set and role/accessibility signalling.
- Part 7 open-caption/video-carried text behavior.
- Part 12 conformance and reference-tool mapping.

### Acceptance criteria

- Overlapping terminology and anchors are consistent.
- Part 12 links to the Part 9 issue/test matrix.
- Any unresolved overlaps are listed as explicit migration gaps.

## Recommended execution order

1. F-0009-T1 and F-0009-T2 for validator-facing MPD checks.
2. F-0009-T3 for CTA 608/708 signalling.
3. F-0009-T4 and F-0009-T5 for asset inventory and gap coverage.
4. F-0009-T6 for reference-player behavior.
5. F-0009-T7 as the final Part 9 cross-part alignment pass.

## Validation

After changes to Part 9 or Part 12 source, run:

```powershell
python tools/publication/check_links.py
python tools/metanorma/bikeshed_to_adoc.py specs/part09-text/part09-text.bs --out authoring/metanorma/generated/part09-text.adoc
python tools/metanorma/bikeshed_to_adoc.py specs/part12-conformance-reference-tools/part12-conformance-reference-tools.bs --out authoring/metanorma/generated/part12-conformance-reference-tools.adoc
```
