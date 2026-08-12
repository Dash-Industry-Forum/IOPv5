# ISO/IEC 23009-1 (6th edition, 2026 merged r5) — Feature extraction

Source in RAG: `rag/corpus/mpeg/ISO_IEC_23009-1_2026_merged_r5.docx`
Chunks: `rag/chunks/iso-iec-23009-1-2026-merged-r5.jsonl` (376 chunks)

Status: **working extraction — early draft.** This note collects the features
added to MPEG DASH (ISO/IEC 23009-1) across editions, based on clause 4 (Overview)
and clause 5 (Media Presentation Description), and links each feature to the clause(s)
that define it. It is intended to seed the Part 13 feature inventory. Descriptions are
paraphrased from the 6th edition text; clause numbers use the 6th edition numbering
unless otherwise noted.

## Method

- Clause 4 (Overview) was read for the DASH system description, client model,
    data model, and protocols framing.
- Subclause 5.2.3 ("Elements and Attributes added in revisions and amendments") is the
    authoritative, per-edition list of schema additions and is used as the backbone for
    "what was added when".
- Each added element/attribute was mapped to its defining clause in clause 5 using the
    chunk heading map (`tools/iso_dash_scan.py` output).

## Per-edition schema additions (from subclause 5.2.3)

### 2nd edition (ISO/IEC 23009-1:2014) additions

| Element / attribute | Feature area | Defining clause (6th ed.) |
|---|---|---|
| `MPD@publishTime` | MPD identification / updates | 5.3.1 |
| `MPD.EssentialProperty`, `MPD.SupplementalProperty` | Generic descriptors | 5.8.1–5.8.3 |
| `Period.AssetIdentifier` | Asset identification (ad insertion continuity) | 5.3.8 / 5.8.5 |
| `Period.EventStream` | MPD events | 5.10.2 (MPD Events) |
| `Period.SupplementalProperty` | Generic descriptors | 5.8.3 |
| `RepresentationBase.InbandEventStream` | Inband events | 5.10.3 (Inband Event Signalling) |
| `SegmentBase@availabilityTimeOffset`, `@availabilityTimeComplete` | Low-latency availability timing | 5.3.9.5 |
| `BaseURL@availabilityTimeOffset`, `@availabilityTimeComplete` | Low-latency availability timing | 5.6 (Base URL) / 5.3.9.5 |
| `Subset@id` | Subsets | 5.3.7 |
| `SegmentTimeline.S@n` | Segment timeline addressing | 5.3.9.6 |

### 3rd edition (ISO/IEC 23009-1:2019) additions

| Element / attribute | Feature area | Defining clause (6th ed.) |
|---|---|---|
| `MPD.UTCTiming` | UTC timing | 5.8.5 (UTCTiming scheme) |
| `Period.GroupLabel` | Labels / group labels | 5.3.10 |
| `Period.Preselection` | Preselections | 5.3.11 |
| `Period.EmptyAdaptationSet` | Preselections / empty adaptation set | 5.3.11 |
| `RepresentationBase.Switching` | Switching signalling | 5.3.5 |
| `RepresentationBase.RandomAccess` | Random access signalling | 5.3.5 |
| `RepresentationBase.GroupLabel`, `.Label` | Labels / group labels | 5.3.10 |
| `RepresentationBase@selectionPriority` | Selection priority | 5.3.5 |
| `Representation@tag` | Representation tagging | 5.3.5 |
| `Representation@associationId`, `@associationType` | Representation association | 5.3.5 |
| `SegmentBase@presentationDuration` | Segment base timing | 5.3.9 |
| `SegmentBase@timeShiftBufferDepth` | Time-shift buffer signalling | 5.3.9 |
| `SegmentTimeline.S@n`, `S@k` | Segment timeline addressing | 5.3.9.6 |

### 4th edition (ISO/IEC 23009-1, 2020) additions

| Element / attribute | Feature | Defining clause (6th ed.) |
|---|---|---|
| `MPD.ServiceDescription`, `Period.ServiceDescription` | Service Description | Annex K |
| `MPD.InitializationSet`, `MPD.InitializationGroup`, `MPD.InitializationPresentation` | Initialization Set / Group / Presentation | 5.3.12 |
| `AdaptationSet@initializationSetRef` | Initialization Set reference | 5.3.12 |
| `MPD.LeapSecondInformation` | Leap seconds | 5.13 |
| `EventStream@presentationTimeOffset` | Events (PTO for MPD events) | 5.10.2 |
| `Event@contentEncoding` | Events (encoded event content) | 5.10.2 |
| `RepresentationBase.ProducerReferenceTime` | Producer Reference Time | 5.12 |
| `RepresentationBase.ContentPopularityRate` | Content Popularity Rate | 5.14 |
| `Preselection@order` | Preselections | 5.3.11 |
| `SegmentBase.FailoverContent` | Failover content signalling | 5.3.9.7 (was 5.3.9.7/5.3.9.8 across editions) |
| `SegmentBase@eptDelta` | Segment base timing | 5.3.9 |
| `MultiSegmentBase@endNumber` | Segment addressing bounds | 5.3.9 |
| `BaseURL@timeShiftBufferDepth` | Time-shift buffer signalling | 5.6 |

### 5th edition (ISO/IEC 23009-1:2022) additions

| Element / attribute | Feature | Defining clause (6th ed.) |
|---|---|---|
| `MPD.ContentProtection`, `Period.ContentProtection` | Content protection at MPD/Period level | 5.8.4 |
| `MPD.PatchLocation` | MPD Patch framework | 5.15 |
| `AdaptationSet@initializationPrincipal` | Initialization principal | 5.3.12 |
| `RepresentationBase.Resync` | Resynchronization | 5.3.13 (and 6.3.2.5) |
| `RepresentationBase@containerProfiles` | Container profile signalling | 5.3.5 |
| `Representation.ExtendedBandwidth` | Variable/extended bandwidth signalling | 5.3.5 |
| `ContentProtection@ref`, `@refId` | Content protection reference | 5.8.4 |
| `ContentProtection@robustness` | Content protection robustness | 5.8.4 |
| `RepresentationBase.OutputProtection` | Output protection | 5.8.4 (Output protection) |

### 6th edition (ISO/IEC 23009-1:2025) additions

| Element / attribute | Feature | Defining clause (6th ed.) |
|---|---|---|
| `MPD.ContentSteering` | Content Steering | Annex K.3.6 (+ 5.6.5) |
| `RequestParam` | Improved query parameters / header extensions | Annex I |
| `Location@serviceLocation`, `PatchLocation@serviceLocation` | Location + Content Steering service location | 5.3.1.2 / 5.15 / Annex K.3.6 |
| `SegmentSequenceProperties` | Segment Sequences | 5.3.9.7 (Segment Sequences) |
| `SegmentTemplate@tolerance` | Segment template timing tolerance | 5.3.9.6 |
| `SegmentTemplate.Pattern`, `S@p`, `S@pE`, `S@ssp` | Duration Patterns / enhanced segment sequence addressing | 5.3.9.6.5 (Duration Patterns; scheme `urn:mpeg:dash:pattern:2024`) |
| `ServiceDescription.ContentSteering` | Content Steering via Service Description | Annex K.3.6 |
| `ServiceDescription.ClientDataReporting` | CMCD reporting via Service Description | Annex K.3.7 |
| `ServiceDescription.PlaybackRestrictions` | Event and playback restrictions | Annex K.3.8 |
| `Event.InsertPresentation`, `Event.ReplacePresentation` | Alternative Media Presentation insertion events | 5.16 |
| `Event.ServiceDescription`, `Event.SelectionInfo` | Alternative Media Presentation event metadata | 5.16 |
| `Event.EssentialProperty`, `Event.SupplementalProperty` | Event-level descriptors | 5.10 / 5.16 |

## Clause-5 feature clauses located in the 6th edition (chunk map)

The following clause-5 sections were located and are the primary sources for
feature descriptions and signalling. (Chunk indices refer to
`rag/chunks/iso-iec-23009-1-2026-merged-r5.jsonl`.)

| Feature | Clause (6th ed.) | Chunks |
|---|---|---|
| Linked Periods | 5.3.2.6 | 39–41 |
| Preselection | 5.3.11 | 96–103 |
| Initialization Set, Group and Presentation | 5.3.12 | 104–112 |
| Duration Patterns | 5.3.9.6.5 | 85–87 |
| Segment Sequences | 5.3.9.7 | 88–91 |
| Failover Content Signalling | 5.3.9.7 | 91–93 |
| Resynchronization | 5.3.13 | 112–114 |
| MPD updates / Patch location | 5.4 / 5.15 | 115–119, 210–219 |
| Base URL Processing | 5.6 | 120–124 |
| Content protection / robustness | 5.8.4 | 131–163 |
| Output protection (+ schemes) | 5.8.4.x / 5.8.5.x | 146–164 |
| Main and External Stream Representations (EDRAP/ESR) | 5.8.x | 165–167 |
| Supplementary video services + descriptor | 5.8.5.16 | 168–171 |
| DASH metrics descriptor | 5.9 | 172–174 |
| Events (MPD, Inband, emsg box) | 5.10 | 175–189 |
| DASH-specific events / Callback / Period Event | 5.10.4 | 190–196 |
| MPD Chaining | 5.11 | 197–199 |
| Producer Reference Time | 5.12 | 200–201 |
| Leap seconds | 5.13 | 202–205 |
| Content Popularity Rate | 5.14 | 206–209 |
| MPD Patch Framework + patch document | 5.15 | 210–219 |
| Alternative Media Presentations (+ reference/HRM processing) | 5.16 | 220–236 |

## Candidate features for the Part 13 inventory (edition-tagged)

The following consolidated feature list (feature ID → edition introduced → clause)
is proposed as the DASH-core basis for the Part 13 inventory. Support-lens and
DVB-relevance columns are maintained separately in the inventory.

| Feature ID | Feature | Edition | Primary clause (6th ed.) |
|---|---|---|---|
| `utc-timing` | UTCTiming | 3rd | 5.8.5 (UTCTiming) |
| `preselections` | Preselections | 3rd | 5.3.11 |
| `random-access-signalling` | RandomAccess signalling | 3rd | 5.3.5 |
| `switching-signalling` | Switching signalling | 3rd | 5.3.5 |
| `labels-group-labels` | Labels and Group Labels | 3rd | 5.3.10 |
| `service-description` | Service Description | 4th | Annex K |
| `initialization-set-group-presentation` | Initialization Set/Group/Presentation | 4th | 5.3.12 |
| `producer-reference-time` | Producer Reference Time | 4th | 5.12 |
| `leap-seconds` | Leap seconds | 4th | 5.13 |
| `content-popularity-rate` | Content Popularity Rate | 4th | 5.14 |
| `failover-content` | Failover Content Signalling | 4th | 5.3.9.7 |
| `availability-time-offset` | Availability Time Offset | 2nd/4th | 5.3.9.5 |
| `mpd-content-protection` | MPD/Period-level ContentProtection | 5th | 5.8.4 |
| `mpd-patching` | MPD Patch Framework | 5th | 5.15 |
| `resync` | Resynchronization | 5th | 5.3.13 / 6.3.2.5 |
| `extended-bandwidth` | Extended/variable bitrate bandwidth signalling | 5th | 5.3.5 |
| `output-protection` | Output protection + robustness | 5th | 5.8.4 |
| `container-profiles` | Container profile signalling | 5th | 5.3.5 |
| `content-steering` | Content Steering | 6th | Annex K.3.6 (+5.6.5) |
| `segment-sequences` | Segment Sequences | 6th | 5.3.9.7 |
| `duration-patterns` | Duration Patterns | 6th | 5.3.9.6.5 |
| `cmcd-reporting` | CMCD reporting via Service Description | 6th | Annex K.3.7 |
| `playback-restrictions` | Event & playback restrictions | 6th | Annex K.3.8 |
| `request-params` | Improved query parameters / header extensions | 6th | Annex I |
| `alternative-media-presentation` | Alternative Media Presentations + insertion events | 6th | 5.16 |
| `supplementary-video` | Supplementary video services + descriptor | 5th/6th | 5.8.5.16 |
| `edrap-esr` | Main and External Stream Representations (EDRAP/ESR) | 6th | 5.8.x |

## Notes and open items

- Clause numbers shift across editions (e.g. Failover Content moved between
    5.3.9.7 and 5.3.9.8; Resync references both 5.3.13 and 6.3.2.5). The table above uses
    the 6th-edition numbering as located in this merged draft; exact subclause numbers
    should be re-verified against the final published 6th edition.
- Segment-format and profile additions (clause 6, 7, 8; e.g. ISO BMFF Advanced Linear,
    List, Single-Period Static profiles, ARI tracks in Annex M) are out of scope for
    clause 4/5 but are relevant candidates and are tracked via the DVB feature review in
    Part 13.
- ARI (Addressable Resource Index) tracks, nonlinear playback (Annex L), and multi-key
    encryption are Annex-level / segment-level features not surfaced by the clause-5
    schema-addition list and should be added from the relevant annex clauses.