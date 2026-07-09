# Migration gap: v4.3 Live Services → Part 4

Records what has been migrated from the DASH-IF IOP v4.3 Live Services clause
(~18,300 words across 23 subsections, `dashif-iop-v4-3#91..#174`) into
`specs/part04-live-low-latency/00-live-services.inc.md`, and what remains, so
nothing is silently dropped. Rerun the analysis with:

    python -c "import json;rows=[json.loads(l) for l in open('rag/chunks/dashif-iop-v4-3.jsonl',encoding='utf-8')]; ..."

## Migrated (v0.2)

| v4.3 subsection | Status | Notes |
|---|---|---|
| Live Services / Introduction | done | Modernised; dropped 2012/2014-edition and simple/main-live framing. |
| Overview: Dynamic and Live Media Presentations | done | Dynamic service types as definitions. |
| Dynamic Segment Download / Background | done | |
| Segment Availability Timing Model | done | SAST/SAET availability rules. |
| Segment Information Derivation | done (summarised) | MPD/Period/Representation derivation, EPT; full formulae abbreviated. |
| Service Offering Requirements (general) | partial | Core MPD requirements ported; the full 3,088-word rule set not yet complete. |
| Live Service Offering including MPD Updates | done (core) | |
| MPD- and Segment-based Live Service Offering | done (core) | |
| Availability Time Synchronization | done | UTCTiming schemes, service + client rules. |
| Client Operation / Joining, Initial Buffering, Playout | done (core) | Joining/buffer/live-edge recommendations. |
| Provisioning of Live Content in On-Demand Mode | stub | See Issue in file + DASH-IF Live-to-VoD guideline. |

## Not yet migrated (tracked for subsequent passes)

| v4.3 subsection | Approx words | Priority | Target |
|---|---|---|---|
| Service Offering Requirements and Guidelines (full detail) | 3,088 | High | Complete the detailed authoring rules and tables. |
| Segment Information Derivation (exact formulae) | 1,838 | High | Port the precise `@t/@d/@r` and SAST/SAET equations, if not deferred to 23009-1. |
| Client Operation, Requirements and Guidelines (full) | 1,766 | High | Expand beyond the core section now present. |
| Tools for Robust Operations | 1,227 | Medium | Redundancy/failover; overlaps DASH-IF Live Media Ingest. |
| Dynamic Service Offering Guidelines | 1,194 | Medium | Worked examples with parameter tables. |
| Reliable and Consistent-Delay Live Service | 969 | Medium | May be superseded by Low-Latency clause; reconcile. |
| Provisioning of Live Content in On-Demand Mode | 923 | Medium | Reconcile with DASH-IF Live-to-VoD guideline. |
| Joining, Initial Buffering and Playout (full detail) | 947 | Medium | Expand beyond core recommendations. |
| Content Offering with Segment Timeline | 736 | Medium | Variable durations, gaps, `$Time$` template. |
| Trick Mode for Live Services | 605 | Low | Signalling of trick-mode Adaptation Sets. |
| Content Offering with Periods | 496 | Low | Multi-period worked example. |
| Simple/Main Live Operation | 419 | drop | Intentionally removed (obsolete IOP framing). |

## Alignment requirement

All migrated Live text must be checked against the **current** MPEG-DASH edition
(ISO/IEC 23009-1). Where v4.3 restates 23009-1 timing formulae verbatim, prefer a
concise summary plus a normative reference to 23009-1 rather than duplicating and
risking divergence.
