# F-0009 Part 9 text and caption test-vector inventory

Generated: 2026-07-22

This inventory tracks local Part 9 validator-start fixtures and planned test asset coverage for text, subtitle, and caption conformance.

## Validator tools

| Bucket | Validator | Scope |
|---|---|---|
| F-0009-T1/T2 | `tools/validation/validate_part9_text_mpd.py` | Text Adaptation Set MIME/codec/language/role/accessibility and selection-priority signalling. |
| F-0009-T3 | `tools/validation/validate_part9_text_mpd.py` | CTA 608/708 video-carried caption Accessibility signalling. |

## Current fixtures

| Bucket | Fixture | Expected result | Coverage |
|---|---|---|---|
| F-0009-T1/T2 | `specs/part09-text/examples/text/valid-text-tracks.mpd` | Pass | IMSC1 subtitle, WebVTT caption, CEA-608 video-carried caption signalling. |
| F-0009-T1/T2 | `specs/part09-text/examples/text/invalid-text-tracks.mpd` | Fail/warn | Invalid selection priority, unrecognized role, missing MIME type/codecs/lang, invalid CEA-608 value. |
| F-0009-T3 | `specs/part09-text/examples/cea-captions/valid-cea608-multichannel.mpd` | Pass | CEA-608 `CC1=eng;CC3=spa`. |
| F-0009-T3 | `specs/part09-text/examples/cea-captions/valid-cea608-shorthand.mpd` | Pass | CEA-608 language-only shorthand. |
| F-0009-T3 | `specs/part09-text/examples/cea-captions/valid-cea708-service.mpd` | Pass | CEA-708 `SERVICE1=eng;SERVICE2=spa`. |
| F-0009-T3 | `specs/part09-text/examples/cea-captions/invalid-cea608-channel.mpd` | Fail | Invalid CEA-608 channel. |
| F-0009-T3 | `specs/part09-text/examples/cea-captions/invalid-cea608-duplicate-channel.mpd` | Fail | Duplicate CEA-608 channel. |
| F-0009-T3 | `specs/part09-text/examples/cea-captions/invalid-cea708-service.mpd` | Fail | Invalid CEA-708 service number. |
| F-0009-T3 | `specs/part09-text/examples/cea-captions/invalid-cea708-duplicate-service.mpd` | Fail | Duplicate CEA-708 service. |

## Planned fixture expansion

### F-0009-T4 IMSC1/WebVTT storage

- ISO BMFF IMSC1 Text (`stpp.ttml.im1t`).
- ISO BMFF IMSC1 Image (`stpp.ttml.im1i`).
- ISO BMFF WebVTT (`wvtt`/`cwvt`).
- Standalone XML TTML/IMSC1 compatibility case.
- Unsupported codec negative fixture.

### F-0009-T5 chunks and gaps

- Empty-document Period gap.
- Period without text content but continuous empty text track.
- Short-duration IMSC1 segment sequence respecting HRM.
- Negative chunking/gap fixture where detectable from MPD signalling.

### F-0009-T6 client selection

- Preferred language selection.
- `und`/missing language fallback.
- Unsupported Role fallback.
- Unsupported EssentialProperty case.
- `selectionPriority` ordering.

## Segment-level limitations

The current validator is MPD-only. The following require segment parsing or reference-player playback:

- CMAF brand/profile verification,
- IMSC1 HRM conformance,
- actual empty-document payload content,
- WebVTT cue parsing,
- client rendering and selection behavior.