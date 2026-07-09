# ADR 0002: Diagrams, Metanorma option, and agent governance

- Status: accepted
- Date: 2025

## Context

Three related questions arose while standing up the authoring workflow:

1. The source Word documents embed figures (including Office `.emf` vector art
   that does not render on the web). We need a diagram strategy.
2. Metanorma was raised as an alternative or complementary authoring path,
   possibly with a custom "flavour".
3. The Qualabs `sgai-for-mpeg-dash` repo was cited as a good example of RAG-based
   execution and tooling (not content) worth learning from.

## Decision

### Diagrams (tiered)

- **Mermaid** is the default for new/redrawn diagrams: text-based, diffable in
  PRs, renders in both Bikeshed (`<pre class=mermaid>`) and GitHub markdown, and
  is explicitly supported by the DASH-IF authoring guide.
- **PlantUML** (`Diagrams/*.wsd`) for formal UML, matching the DASH-IF convention.
- **draw.io** exported as `*.drawio.svg` for bespoke figures that fit no diagram
  grammar (the SVG is both viewable and re-editable).
- **Keep original raster** only for screenshots/photos not worth redrawing.
- `tools/ingest/extract_images.py` pulls embedded images out of each source DOCX
  into `specs/<part>/Images/` with a triage manifest flagging EMF/WMF for
  redrawing. Extracted originals are gitignored until triaged.

### Bikeshed vs Metanorma

- **Bikeshed remains the canonical path** (Option B: local `bikeshed`, no Docker),
  reusing the DASH-IF-IOP `specs/<part>/<part>.bs` + `.inc.md` convention.
- **Metanorma is tracked as a complementary evaluation**, not adopted yet. It is
  AsciiDoc-based, produces HTML/PDF/DOC, validates structure against a schema, and
  supports organization "flavours"/"tastes". A DASH-IF flavour/taste would be a
  larger investment (Ruby toolchain, gem or Docker, custom flavour repo). Given
  the corporate TLS-proxy constraints and that DASH-IF already uses Bikeshed, the
  proof-of-concept stays parked under `authoring/dashif-metanorma-template/`.
  Revisit if PDF/DOC fidelity or schema validation become hard requirements.

### Agent governance (adapted from Qualabs)

- Added `AGENTS.md` at the workspace root: directory-layering rules, the
  run-in-order toolchain, grounding expectations (local RAG as our offline
  NotebookLM), authoring convention, and environment caveats (proxy/TLS, no
  Docker, PowerShell path quoting).
- Added a project rule so the conventions apply automatically in future sessions.
- We deliberately did **not** copy Qualabs' content, prompts, or spec; only the
  execution patterns (governance layer, one-directional data flow, grounded
  authoring, versioned artefacts).

## Consequences

- Contributors and agents have an explicit "how to act" contract, addressing the
  original "the agent does not act" problem.
- Diagram sources become diffable and tool-independent where possible.
- The Metanorma decision is deferred but documented, keeping the door open.
