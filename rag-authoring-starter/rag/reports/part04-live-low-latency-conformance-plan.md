# Part 4 Live and Low-Latency conformance planning baseline

Generated: 2026-07-22

This report starts the structured migration/conformance baseline for Part 4, Live and Low-Latency services.

## Primary source

```text
specs/part04-live-low-latency/00-live-services.inc.md
specs/part04-live-low-latency/02-low-latency.inc.md
```

## Initial conformance buckets

| ID | Area | Validator target | Test asset target | Cross-part dependency |
|---|---|---|---|---|
| P4-COV-001 | Dynamic MPD live profile signalling | Check dynamic type, AST, MUP, TSBD, UTCTiming, and live profile attributes. | Minimal live MPD fixtures. | Part 2. |
| P4-COV-002 | Segment availability and timing | Check SegmentTimeline, availability windows, PTO, and duration/timescale consistency. | livesim2-generated deterministic live streams. | Part 12/livesim2. |
| P4-COV-003 | Low-latency signalling | Check ServiceDescription, latency targets, availabilityTimeOffset, and chunked transfer indicators where MPD-detectable. | Low-latency positive/negative fixtures. | Part 2, Part 12. |
| P4-COV-004 | Client live edge behavior | Reference-player checks for live latency, catch-up, seek window, and rebuffer behavior. | dash.js/livesim2 tests. | Part 12. |
| P4-COV-005 | Cross-part interaction | Align live constraints with ad insertion and text tracks. | Combined live + ad/text fixtures. | Parts 5 and 9. |

## Recommended issue breakdown

1. `F-0004: Live dynamic MPD validator coverage`
2. `F-0004: Segment availability and timing fixtures`
3. `F-0004: Low-latency MPD signalling coverage`
4. `F-0004: livesim2 deterministic live test mapping`
5. `F-0004: dash.js live edge and latency behavior coverage`

## Immediate next implementation step

Create an MPD-only validator-start plan and fixture pair:

```text
tools/validation/validate_part4_live_mpd.py
specs/part04-live-low-latency/examples/valid-live.mpd
specs/part04-live-low-latency/examples/invalid-live.mpd
```

## Known limitations

Actual low-latency chunking, transport behavior, and live-edge behavior require livesim2 and dash.js execution rather than MPD-only checks.