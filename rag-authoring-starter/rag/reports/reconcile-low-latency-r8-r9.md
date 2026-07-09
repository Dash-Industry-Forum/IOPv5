# Reconciliation: Low-Latency CR r8 vs r9 (Part 4 Issue placeholders)

Grounded against `cr-low-latency-live-r8` (PDF) and `cr-low-latency-live-r9`
(DOCX) via the local RAG index. Complements the heuristic structural diff in
`delta-cr-low-latency-live-r8-vs-cr-low-latency-live-r9.md` (which under-reports
shared headings because the two inputs differ in format and clause numbering).

## Nature of the r8 -> r9 change

The dominant change is **structural renumbering / re-homing**, not new normative
text:

- r8 places the low-latency material under clause `6.4.x` (e.g. `6.4.3`
    Low-Latency Adaptation Set, `6.4.4` Segment AS, `6.4.5` Chunked AS).
- r9 re-homes the same material under **`9.X` "DASH Live Services"** to align with
    the MPEG-DASH (ISO/IEC 23009-1) clause 9 structure (e.g. `9.X.4.3` / `9.X.4.4`
    / `9.X.4.5`).
- r9's title is *"Low-latency Modes for DASH: Addition of ..."*, i.e. an additive
    CR onto the r8 baseline.

The core normative requirements (ServiceDescription/Latency, ProducerReferenceTime
constraints, Segment vs Chunked Adaptation Set rules, Resync signalling, the 50% /
30% target-latency segment-duration bounds) are **carried over essentially
unchanged** between r8 and r9 — only the clause anchors move.

## Resolution of the Part 4 `Issue:` placeholders

1. **Addressable Resync Representation (ARR):** neither r8 nor r9 contains
    normative ARR text. "ARR" is a forward-looking concept in the IOPv5 skeleton;
    r8/r9 specify resynchronization via the existing `Resync` element and Resync
    Marker Points (ISO/IEC 23009-1:2020/Amd.1), not a new "ARR" construct. Action:
    keep the ARR definition marked as *to be confirmed against MPEG-DASH*; do not
    fabricate normative ARR requirements. The migrated `Resync` guidance in
    `02-low-latency.inc.md` (`#ll-resync`) already reflects the r8/r9 baseline.

2. **Broadcast TV Profile:** explicitly *"will be provided in a future version"*
    in BOTH r8 (`6.6.4.4`) and r9 (`9.X.6.4.4`, and client-side `9.X.7.1.5`).
    Action: keep as a future-work `Issue:` placeholder; there is nothing to
    migrate yet. Track via a GitHub issue on Part 4.

## Editor follow-ups

- When adopting r9 numbering, prefer the MPEG-DASH-aligned clause 9 homing.
- Revisit ARR only if/when MPEG-DASH or a later CR introduces the construct
    normatively.
- Re-run `tools/ingest/extract_text.py` on a DOCX (not PDF) of r8 if a cleaner
    structural diff is needed; the PDF cover-form pollutes the heading heuristic.
