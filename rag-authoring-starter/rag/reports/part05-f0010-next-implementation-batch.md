# F-0010 Part 5 next implementation batch

Generated: 2026-07-22

This batch resumes Part 5 after the initial validator and fixture expansion. It collects the next executable work that should follow the current IF-3/IF-4/IF-5 validator-start commits.

## Current implementation baseline

Implemented local validator starts:

```text
tools/validation/validate_part5_scte35_events.py
tools/validation/validate_part5_ad_content_mpd.py
tools/validation/validate_part5_if5_spliced_mpd.py
```

Implemented local fixture roots:

```text
specs/part05-ad-insertion/examples/scte35/
specs/part05-ad-insertion/examples/table4/
specs/part05-ad-insertion/examples/table5/
```

Current inventory:

```text
rag/reports/part05-f0010-test-vector-inventory.md
```

## Batch P5-N1: SCTE-35 payload fixture hardening

### Goal

Move from command-type parsing to payload-aware SCTE-35 opportunity modelling.

### Work

- Add explicit fixtures for:
  - `time_signal()` with splice time,
  - `time_signal()` with segmentation descriptor,
  - segmentation start/end pair,
  - legacy `splice_insert()` out-of-network signal,
  - `splice_insert()` break duration,
  - unsupported command type,
  - malformed table ID,
  - descriptor mismatch.
- Add validator-level parse summaries to the output path, while keeping existing finding format stable.

### Acceptance

- Existing positive fixture remains `OK`.
- Each negative fixture maps to one deterministic error/warning.
- Inventory identifies which SCTE-35 checks are MPD-only and which require binary payload interpretation.

## Batch P5-N2: IF-5 scenario-to-reference-player preparation

### Goal

Prepare current IF-5 MPD scenarios for dash.js/reference-player testing.

### Work

- Add a scenario manifest index mapping each MPD to:
  - expected Period sequence,
  - ad role(s),
  - slate usage,
  - EventStream treatment,
  - expected reference-player behavior.
- Distinguish structural MPD-only checks from future media playback checks.
- Add placeholders for clear/encrypted media assets for IF-9.

### Acceptance

- Scenario inventory is traceable from Part 12.
- Each scenario has validator status and playback status fields.
- IF-9 dependencies on Part 6 are explicit.

## Batch P5-N3: Table/Figure closure

### Goal

Close M1 visual-review planning gaps without blocking validator work.

### Work

- Produce a final status table for Figures 1, 3, 4, 5, 6, and 7.
- Produce final status for Tables 1-5.
- Identify which items are already source-authoritative and which require DOCX/PDF visual confirmation.

### Acceptance

- `part05-f0010-table-figure-hardening.md` has a closed/open/deferred status per item.
- Part 12 no longer claims visual closure for any item still awaiting review.