# Status: Part 2 / Part 3 drafting and all-part Bikeshed conversion

## Completed in this pass

- **Part 2 — Core Principles and CMAF Mapping**
  - Created `specs/part02-core-cmaf/part02-core-cmaf.bs`.
  - Created `specs/part02-core-cmaf/01-core-cmaf.inc.md`.
  - Drafted a substantive working version covering:
    - scope and references;
    - CMAF structural model and CMAF-to-DASH mapping principles;
    - DASH-IF Media Presentation and MPD model;
    - DASH timing model;
    - Representation and Segment signalling;
    - SegmentTemplate modes and segment-list computation;
    - Subsegment information;
    - media-presentation-time mapping;
    - Good Multi-Period CMAF Content;
    - bandwidth signalling;
    - static/dynamic service split;
    - MPD updates;
    - MPD and Segment locations;
    - gap handling;
    - content annotation/media mapping;
    - a table of open issues and work items.
  - Grounding: `dashif-iop-v5-part2-draft#10..#129`, v4.3 timing/on-demand basics
    (`dashif-iop-v4-3#30..#42`, `#74..#90`, `#192..#206`, `#242..#247`), and the
    current MPEG-DASH/CMAF baselines.

- **Part 3 — On-Demand Services**
  - Created `specs/part03-on-demand/part03-on-demand.bs`.
  - Created `specs/part03-on-demand/01-on-demand.inc.md`.
  - Drafted a working version covering:
    - common static/on-demand MPD requirements;
    - segment information derivation;
    - on-demand services using live-profile segment structures;
    - on-demand services using MPEG-DASH On-Demand profile structures;
    - service-offering requirements;
    - client operation;
    - mixed on-demand content;
    - a table of open issues and work items.
  - Grounding: DASH-IF IOP v4.3 on-demand clauses `dashif-iop-v4-3#72..#90`.

- **Parts 5–11 conversion shells**
  - Added `.bs` and `.inc.md` files for Parts 5 through 11 using the same shared
    boilerplate, IPR include, diagram/table styling, metadata, bibliography, issue
    tracking, and change-history pattern as Parts 1, 2, 3, 4, and 12.
  - These are conversion shells: they build and provide migration placeholders, but
    their substantive normative content still needs to be migrated part by part.

## Open Part 2 topics to progress

These are also listed inside Part 2 itself:

- Reconstruct the CMAF content model figure or equivalent table.
- Recreate the SegmentTemplate parameter table (mandatory/optional/defaults for
  Number+Duration, Number+SegmentTimeline, Time+SegmentTimeline).
- Port or retire detailed segment-list computation formulae from v4.3/Part 2 draft.
- Complete Subsegment/CMAF Chunk treatment and align with Part 4 low-latency.
- Complete Good Multi-Period CMAF Content requirements and profile signalling.
- Reconcile bandwidth-signalling text with current MPEG-DASH and validator needs.
- Deduplicate static/dynamic/MPD-update rules with Parts 3 and 4.
- Complete Location/BaseURL guidance.
- Complete gap-handling normative rules.
- Reconcile content annotation and client processing reference model with Parts 7–10.

## Open Part 3 topics to progress

These are also listed inside Part 3 itself:

- Rebuild the v4.3 on-demand/live-profile MPD and Segment information table.
- Confirm the IOP v5 status of `http://dashif.org/guidelines/dash-if-ondemand`.
- Review `sidx`/Indexed Self-Initializing Media Segment constraints against current
  ISO BMFF and MPEG-DASH.
- Confirm the IOP v5 status of the mixed-on-demand profile URI.
- Decide whether trick-mode requirements remain in Part 3 or move to Part 11.

## Verification

- `./build.ps1` builds all 12 parts successfully.
- `python tools/publication/build_all.py --out ../dist` builds all 12 parts and
  generates the overview index successfully.
- `python tools/publication/check_links.py` passes: 32 files checked, no issues.
