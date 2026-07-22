# Conformance validator-start dashboard

Generated: 2026-07-22

This dashboard tracks the local MPD-level validator-start coverage across the active IOP v5 migration parts.

| Part | Feature ID | Planning report | Validator tool | Fixture root | Current status | Next action | Runtime dependency | Part 12 synchronized? |
|---|---|---|---|---|---|---|---|---|
| Part 2 Core CMAF | F-0002 / P2-COV-001..005 | `rag/reports/part02-core-cmaf-conformance-plan.md` | `tools/validation/validate_part2_core_cmaf_mpd.py` | `specs/part02-core-cmaf/examples/` | MPD validator-start and positive/negative fixtures added. | Expand CMAF timing/switching cases and identify segment-level brand checks. | Segment parser for CMAF brands/chunks. | Yes, validator-start table. |
| Part 3 On-Demand | F-0003 / P3-COV-001..005 | `rag/reports/part03-on-demand-conformance-plan.md` | `tools/validation/validate_part3_on_demand_mpd.py` | `specs/part03-on-demand/examples/` | MPD validator-start and positive/negative fixtures added. | Add SegmentBase and multi-period on-demand fixtures. | dash.js seek/random-access playback. | Yes, validator-start table. |
| Part 4 Live/Low-Latency | F-0004 / P4-COV-001..005 | `rag/reports/part04-live-low-latency-conformance-plan.md` | `tools/validation/validate_part4_live_mpd.py` | `specs/part04-live-low-latency/examples/` | MPD validator-start and positive/negative fixtures added. | Add SegmentTimeline, ATO, ServiceDescription, and livesim2 deterministic cases. | livesim2 and dash.js live-edge behavior. | Yes, validator-start table. |
| Part 5 Ad Insertion | F-0010 | `rag/reports/part05-f0010-test-vector-inventory.md`; `rag/reports/part05-f0010-next-implementation-batch.md` | `tools/validation/validate_part5_scte35_events.py`; `tools/validation/validate_part5_ad_content_mpd.py`; `tools/validation/validate_part5_if5_spliced_mpd.py` | `specs/part05-ad-insertion/examples/` | IF-3/IF-4/IF-5 validator-start coverage exists. | Create IF-5 scenario manifest and harden SCTE-35 payload fixtures. | dash.js playback, livesim2 SGAI, Part 6 EME/DRM. | Yes, validator-start table. |
| Part 9 Text | F-0009 | `rag/reports/part09-f0009-issue-index.md`; `rag/reports/part09-f0009-test-vector-inventory.md` | `tools/validation/validate_part9_text_mpd.py` | `specs/part09-text/examples/` | Text and CTA caption MPD validator-start coverage exists. | Add IMSC1/WebVTT/gap fixtures and selection behavior cases. | Segment parser and dash.js rendering/selection. | Yes, validator-start table. |

## Validation command set

```powershell
python tools/validation/validate_part2_core_cmaf_mpd.py specs/part02-core-cmaf/examples/valid-core-cmaf.mpd specs/part02-core-cmaf/examples/invalid-core-cmaf.mpd
python tools/validation/validate_part3_on_demand_mpd.py specs/part03-on-demand/examples/valid-on-demand.mpd specs/part03-on-demand/examples/invalid-on-demand.mpd
python tools/validation/validate_part4_live_mpd.py specs/part04-live-low-latency/examples/valid-live.mpd specs/part04-live-low-latency/examples/invalid-live.mpd
python tools/publication/check_links.py
```
