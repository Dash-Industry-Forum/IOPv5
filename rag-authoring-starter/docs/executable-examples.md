# Executable DASH Examples using livesim2 and dash.js

This note defines a common approach for adding executable examples to the DASH-IF
IOP v5 parts.

The goal is not to force an example into every clause. The goal is to provide a
curated set of verified MPD URLs and dash.js launch links for features that are
actually observable in a player or in the MPD.

## Link pattern

Use the dash.js reference player deep-link syntax below:

```text
https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html?stream=<URL-encoded-MPD>&autoLoad=true&autoplay=true&muted=true
```

The reference player uses:

- `stream`: MPD URL.
- `autoLoad=true`: load the MPD when the page opens.
- `autoplay=true`: request playback start.
- `muted=true`: improve compatibility with browser autoplay policies.

Do not use `url=<MPD>` for the current dash.js reference player.

## Example entry requirements

Each executable example should include:

- Part number and feature.
- MPD URL.
- dash.js launch URL, where applicable.
- Expected observable behavior.
- Caveats, such as browser codec support, DRM environment, or event-debugging needs.
- Validation status.

## Per-Part applicability

| Part | Applicability | Recommended approach |
|---|---|---|
| Part 1 Overview | Low | Link to the examples registry rather than duplicating examples. |
| Part 2 Core/CMAF | High | Use livesim2/static DASH examples for SegmentTemplate, SegmentTimeline, Periods, UTCTiming, CMAF alignment. |
| Part 3 On-demand | Medium | Prefer static DASH-IF on-demand assets; use livesim2 only where dynamic behavior is relevant. |
| Part 4 Live/Low-Latency | Very high | Use livesim2 and dash.js launch links. This is the reference pattern. |
| Part 5 Ad insertion | Medium/high | Add verified Period/SCTE-35/event examples only after URL-level validation. |
| Part 6 Content protection | Medium | Prefer ClearKey and clearly mark Widevine/PlayReady environment requirements. |
| Part 7 Video | High | Add codec/representation examples with browser support caveats. |
| Part 8 Audio | High | Add language/channel/role examples with codec support caveats. |
| Part 9 Text | High | Add WebVTT/IMSC/subtitle/caption examples. |
| Part 10 Events | High, but tooling-dependent | Add examples, ideally with an event-debug sample or clear console/debug instructions. |
| Part 11 Additional technologies | Case-by-case | Add examples only where a player-observable behavior exists. |
| Part 12 Conformance/reference tools | High as index | Reference the registry and validation script. |

## Current verified examples

The first verified examples are the Part 4 low-latency livesim2 streams. They are
also listed in `rag/examples/executable-examples.yaml`.

| Part | Feature | MPD | dash.js launch |
|---|---|---|---|
| Part 4 | Basic low-latency live, 3.5 s target | <a href="https://livesim2.dashif.org/livesim2/chunkdur_0.5/ato_7/ltgt_3500/testpic_2s/Manifest.mpd">MPD</a> | <a href="https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html?stream=https%3A%2F%2Flivesim2.dashif.org%2Flivesim2%2Fchunkdur_0.5%2Fato_7%2Fltgt_3500%2Ftestpic_2s%2FManifest.mpd&autoLoad=true&autoplay=true&muted=true">Launch in dash.js</a> |
| Part 4 | Ultra-low-latency live, 2 s target | <a href="https://livesim2.dashif.org/livesim2/chunkdur_0.2/ato_4/ltgt_2000/testpic_2s/Manifest.mpd">MPD</a> | <a href="https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html?stream=https%3A%2F%2Flivesim2.dashif.org%2Flivesim2%2Fchunkdur_0.2%2Fato_4%2Fltgt_2000%2Ftestpic_2s%2FManifest.mpd&autoLoad=true&autoplay=true&muted=true">Launch in dash.js</a> |
| Part 4 | SegmentTimeline low-latency live | <a href="https://livesim2.dashif.org/livesim2/segtimeline_1/chunkdur_0.5/ato_7/ltgt_4000/testpic_2s/Manifest.mpd">MPD</a> | <a href="https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html?stream=https%3A%2F%2Flivesim2.dashif.org%2Flivesim2%2Fsegtimeline_1%2Fchunkdur_0.5%2Fato_7%2Fltgt_4000%2Ftestpic_2s%2FManifest.mpd&autoLoad=true&autoplay=true&muted=true">Launch in dash.js</a> |
| Part 4 | Low-latency live with UTC timing | <a href="https://livesim2.dashif.org/livesim2/utc_direct/chunkdur_0.5/ato_7/ltgt_3500/testpic_2s/Manifest.mpd">MPD</a> | <a href="https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html?stream=https%3A%2F%2Flivesim2.dashif.org%2Flivesim2%2Futc_direct%2Fchunkdur_0.5%2Fato_7%2Fltgt_3500%2Ftestpic_2s%2FManifest.mpd&autoLoad=true&autoplay=true&muted=true">Launch in dash.js</a> |

## Candidate expansion plan

Use the registry as the source of truth and add examples in stages:

1. Seed Part 4 with verified livesim2 links.
2. Add Part 2 examples for SegmentTemplate, SegmentTimeline, Periods, and UTCTiming using verified livesim2 URLs.
3. Add Part 9 text examples using verified text-track assets.
4. Add Part 8 audio examples using browser-safe AAC examples first.
5. Add Part 7 video examples with explicit codec/browser support notes.
6. Add Part 5 ad insertion examples only after confirming current livesim2 ad/SCTE-35 URL syntax.
7. Add Part 6 DRM examples beginning with ClearKey.
8. Add Part 10 event examples with a debug procedure or a small event-observer sample.

## Validation

Run:

```bash
python tools/validation/check_executable_examples.py rag/examples/executable-examples.yaml
```

The checker validates MPD URLs and dash.js launch-link syntax. It does not verify
browser playback success, codec support, DRM license availability, or event
application handling.