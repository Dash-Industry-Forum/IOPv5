# Part 2 Core CMAF conformance planning baseline

Generated: 2026-07-22

This report starts the structured migration/conformance baseline for Part 2, Core CMAF. It connects Part 2 source requirements to validators, test assets, and cross-part dependencies.

## Primary source

```text
specs/part02-core-cmaf/01-core-cmaf.inc.md
```

## Initial conformance buckets

| ID | Area | Validator target | Test asset target | Cross-part dependency |
|---|---|---|---|---|
| P2-COV-001 | CMAF profile and MPD profile signalling | Check profile URNs, `@profiles`, CMAF-compatible segment signalling. | Minimal CMAF on-demand and live presentations. | Parts 3, 4, 5, 9. |
| P2-COV-002 | Adaptation Set and Representation baseline | Check required MPD attributes, Representation codecs/bandwidth, SegmentTemplate/SegmentTimeline consistency. | Positive/negative MPD structure fixtures. | Parts 7, 8, 9. |
| P2-COV-003 | Segment addressing and timing | Check SegmentTemplate, SegmentTimeline, duration/timescale, PTO constraints where applicable. | Multi-period timing fixtures and boundary fixtures. | Parts 3, 4, 5. |
| P2-COV-004 | CMAF switching/connectivity assumptions | Check signalling that enables seamless switching where mechanically detectable. | Multi-representation switching sets. | Parts 4, 5, 7, 8. |
| P2-COV-005 | Cross-part terminology and anchors | Ensure reusable definitions are stable. | Not applicable. | All parts, especially Part 12. |

## Recommended issue breakdown

1. `F-0002: validator baseline for Core CMAF MPD profile and segment signalling`
2. `F-0002: Adaptation Set and Representation structural fixtures`
3. `F-0002: timing and segment addressing conformance coverage`
4. `F-0002: switching/connectivity alignment with Parts 4, 5, 7, and 8`
5. `F-0002: Part 12 conformance mapping for Core CMAF`

## Immediate next implementation step

Create a small validator-start script or extend existing validation helpers to cover MPD-only Part 2 checks:

```text
tools/validation/validate_part2_core_cmaf_mpd.py
specs/part02-core-cmaf/examples/valid-core-cmaf.mpd
specs/part02-core-cmaf/examples/invalid-core-cmaf.mpd
```

## Known limitations

Segment-level CMAF brand and chunk constraints require media parsing beyond the initial MPD-only validator-start scope.