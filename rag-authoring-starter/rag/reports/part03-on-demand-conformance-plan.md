# Part 3 On-Demand conformance planning baseline

Generated: 2026-07-22

This report starts the structured migration/conformance baseline for Part 3, On-Demand services.

## Primary source

```text
specs/part03-on-demand/01-on-demand.inc.md
```

## Initial conformance buckets

| ID | Area | Validator target | Test asset target | Cross-part dependency |
|---|---|---|---|---|
| P3-COV-001 | Static MPD and on-demand profile signalling | Check static presentation type, profile signalling, duration, and BaseURL/segment addressing. | Minimal valid on-demand asset and invalid profile/timing fixtures. | Part 2. |
| P3-COV-002 | Segment availability and addressing | Check SegmentBase/SegmentTemplate/SegmentTimeline use for on-demand assets. | Positive/negative addressing fixtures. | Part 2. |
| P3-COV-003 | Multi-period on-demand constraints | Check Period start/duration continuity where applicable. | Multi-period on-demand fixtures. | Parts 2, 5. |
| P3-COV-004 | Random access and seeking support | MPD-only indicators plus reference-player playback checks. | dash.js seek test streams. | Part 12. |
| P3-COV-005 | Test asset database mapping | Link available on-demand assets to conformance buckets. | Test Assets Database references. | Part 12. |

## Recommended issue breakdown

1. `F-0003: On-Demand static MPD validator coverage`
2. `F-0003: On-Demand segment addressing fixtures`
3. `F-0003: Multi-period On-Demand continuity fixtures`
4. `F-0003: dash.js seek/random-access sample coverage`
5. `F-0003: Part 12 On-Demand conformance mapping`

## Immediate next implementation step

Create an MPD-only validator-start plan and fixture pair:

```text
tools/validation/validate_part3_on_demand_mpd.py
specs/part03-on-demand/examples/valid-on-demand.mpd
specs/part03-on-demand/examples/invalid-on-demand.mpd
```

## Known limitations

Reference-player seek and random-access behavior requires media assets, not only MPD fixtures.