# F-0010 M1 GitHub issue creation bundle

Generated: 2026-07-21

Purpose: copy/paste-ready GitHub issues for the M1 work package.

Note: GitHub CLI (`gh`) is not available in the current environment, so issues
need to be created manually in:

```text
https://github.com/Dash-Industry-Forum/IOPv5/issues
```

Common labels:

```text
feature:F-0010
part-5
ad-insertion
conformance
```

## Issue 1

Title:

```text
[Part 5][F-0010-H1] Harden figures against published DOCX/PDF
```

Body:

```markdown
## Scope

Harden the published Part 5 figures against the original DOCX/PDF.

Figures:

- Figure 1: IF-1a/IF-1b/IF-1c architecture context
- Figure 3: Abstracted Media Model with Splice Points
- Figure 4: CMAF Encoder and Packager Options
- Figure 5: CMAF Fragment to DASH Mapping for Option 1 and 3
- Figure 6: Recommended Ad Content Format
- Figure 7: MPD Manipulator Operation: Conforming IF-5 output

## Source reports

- `rag/reports/part05-f0010-m1-visual-validator-start.md`
- `rag/reports/part05-f0010-table-figure-hardening.md`

## Acceptance criteria

- Each figure has final status: extracted, redrawn, intentionally deferred, or omitted with reason.
- IF-1a/IF-1b/IF-1c labels are confirmed or corrected.
- Source anchors are updated or issue notes remain explicit.
```

## Issue 2

Title:

```text
[Part 5][F-0010-H2] Reconstruct Table 2 row layout from DOCX/PDF
```

Body:

```markdown
## Scope

Reconstruct published Part 5 Table 2, "DASH-IF Main live content MPD", from visual DOCX/PDF inspection.

## Source reports

- `rag/reports/part05-f0010-table2-reconstruction.md`
- `rag/reports/part05-f0010-m1-visual-validator-start.md`

## Acceptance criteria

- Complete Table 2 row layout is captured or formally deferred with reason.
- Column headings, row hierarchy, Use values, modal keywords, and notes are reviewed.
- IF-2 source prose is cross-checked against Table 2.
- Part 12 conformance mapping is updated if Table 2 changes validator/test expectations.
```

## Issue 3

Title:

```text
[Part 5][F-0010-H3] Visually review Table 4 DASH-IF ad content MPD
```

Body:

```markdown
## Scope

Visually review reconstructed Part 5 Table 4 against the published DOCX/PDF.

## Source anchors

- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4d-ad-content-storage`

## Source reports

- `rag/reports/part05-f0010-table4-validator-matrix.md`
- `rag/reports/part05-f0010-m1-table4-table5-visual-review-start.md`

## Acceptance criteria

- Table 4 row set is confirmed or corrected.
- Row hierarchy and `Use` values are confirmed.
- Modal strength is confirmed.
- Validator matrix is updated if row details change.
- F-0010-B1 is unblocked.
```

## Issue 4

Title:

```text
[Part 5][F-0010-H4] Visually review Table 5 IF-5 multi-Period ad insertion
```

Body:

```markdown
## Scope

Visually review reconstructed Part 5 Table 5 against the published DOCX/PDF.

## Source anchors

- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-media-presentation-requirements`

## Source reports

- `rag/reports/part05-f0010-table5-validator-matrix.md`
- `rag/reports/part05-f0010-m1-table4-table5-visual-review-start.md`

## Acceptance criteria

- Table 5 row set is confirmed or corrected.
- Main-content and ad-content rows are verified.
- Current two-table source split is accepted or revised.
- Validator matrix is updated if row details change.
- F-0010-C1 is unblocked.
```

## Issue 5

Title:

```text
[Part 5][F-0010-H5] Decide Table 4/Table 5 canonical reuse strategy
```

Body:

```markdown
## Scope

Decide whether Table 4 and Table 5 should share a canonical requirement table/module or remain separate.

## Inputs

- F-0010-H3 Table 4 visual review
- F-0010-H4 Table 5 visual review
- `rag/reports/part05-f0010-table4-validator-matrix.md`
- `rag/reports/part05-f0010-table5-validator-matrix.md`

## Acceptance criteria

- Shared rows are identified.
- Validator module reuse strategy is documented.
- Source table duplication is accepted or revised.
- Part 12 mapping reflects the decision.
```

## Issue 6

Title:

```text
[Part 5][F-0010-A1] Implement MPD-level SCTE-35 EventStream checks
```

Body:

```markdown
## Scope

Implement MPD-level validator checks for IF-3 SCTE-35 opportunity signalling.

## Source reports

- `rag/reports/part05-f0010-scte35-validator-matrix.md`
- `rag/reports/part05-f0010-m1-visual-validator-start.md`

## Initial checks

- Allowed SCTE-35 EventStream schemes.
- `xml+bin` Binary presence.
- Base64 validation.
- Event timing parseability.
- Duplicate Event `@id` warning.

## Acceptance criteria

- Positive and negative MPD-level examples are identified.
- Payload-aware checks are left to F-0010-A2 if no SCTE-35 parser is available.
- Part 12 mapping is updated.
```

## Issue 7

Title:

```text
[Part 5][F-0010-B1] Implement DASH-IF ad content MPD structural validator checks
```

Body:

```markdown
## Scope

Implement structural validator checks for DASH-IF ad content MPDs based on Table 4.

## Source reports

- `rag/reports/part05-f0010-table4-validator-matrix.md`
- `rag/reports/part05-f0010-validator-implementation-issues.md`

## Initial checks

- Static MPD type.
- CMAF profile.
- Forbidden dynamic MPD attributes.
- Exactly one Period.
- `Period@duration`.
- Period-level `BaseURL`.
- AdaptationSet/Representation presence.
- Forbidden `UTCTiming` and `LeapSecondInformation`.

## Acceptance criteria

- Checks are implemented or implementation-ready.
- Negative vectors are listed for each deterministic error.
- Part 12 mapping is updated.
```

## Issue 8

Title:

```text
[Part 5][F-0010-C1] Implement IF-5 multi-Period structural validator checks
```

Body:

```markdown
## Scope

Implement structural validator checks for IF-5 multi-Period MPDs.

## Source reports

- `rag/reports/part05-f0010-table5-validator-matrix.md`
- `rag/reports/part05-f0010-validator-implementation-issues.md`

## Initial checks

- Period presence.
- Main Period `@start`.
- Monotonic Period starts.
- AdaptationSet/Representation presence.
- `AdaptationSet@contentType`.
- SegmentList absence.
- Live/dynamic `UTCTiming`.
- Reuse Table 4 checks for source ad-content MPDs.

## Acceptance criteria

- Checks are implemented or implementation-ready.
- Scenario checks are separated from deterministic MPD checks.
- Part 12 mapping is updated.