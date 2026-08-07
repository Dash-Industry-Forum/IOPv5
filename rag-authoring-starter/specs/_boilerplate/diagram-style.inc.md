<!--
  Shared diagram styling for Mermaid figures.

  Two problems this file fixes:

  1. Label text overflowing / being clipped inside nodes ("ABR Encode" instead of
     "ABR Encoder"). Mermaid source is authored inside `<pre class=mermaid>`, and
     Bikeshed styles `pre` with a monospace font. Mermaid measures node widths
     using its own configured (sans-serif) font, but anything that inherits from
     the `pre` renders in monospace, which is substantially wider. Measured width
     then no longer matches rendered width, so labels spill out of their boxes and
     get clipped. Forcing a sans-serif stack on the Mermaid container - and on the
     `foreignObject` label wrappers used when `htmlLabels` is enabled - keeps the
     measured and rendered metrics aligned.

  2. Diagrams being distorted by `width: 100% !important` on the SVG. Mermaid
     already emits its own sizing when `useMaxWidth` is set; forcing the width on
     top of that stretches the diagram independently of the label geometry. We
     now constrain with `max-width` only and let Mermaid own the intrinsic size.

  Also overrides the dashif boilerplate's `.mermaid { display: table }` (which
  shrinks diagrams to content width) so engineering diagrams render at a readable
  size, centered. Include once per spec via a staged copy
  (_shared-diagram-style.inc.md), the same mechanism as the IPR boilerplate.

  NOTE: Mermaid renders client-side. If a viewer blocks scripts (for example an
  email preview pane), the Mermaid source is shown as literal text instead of a
  diagram. That is expected and is not a build problem.
-->

<style>
/* Keep the sans-serif stack in sync with the `fontFamily` used in the
   `%%{init: ...}%%` directives in the spec sources. */
figure.diagram {
  text-align: center;
  margin: 1.5em 0;
  max-width: 100%;
  overflow-x: auto;
}

/* Render Mermaid diagrams larger and centered rather than shrink-to-content. */
figure.diagram pre.mermaid,
figure.diagram .mermaid {
  display: block !important;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 auto !important;
  padding: 0 !important;
  background: transparent !important;
  border: 0 !important;
  text-align: center;
  overflow: visible !important;
  /* Defeat the monospace `pre` font so Mermaid's measured label widths match
     what the browser actually paints. */
  font-family: system-ui, "Segoe UI", Arial, sans-serif !important;
  font-size: 16px !important;
  line-height: 1.25 !important;
  white-space: normal !important;
  tab-size: initial;
}

/* Let Mermaid own the intrinsic size; only constrain the upper bound. */
figure.diagram .mermaid svg,
figure.diagram svg {
  width: auto !important;
  max-width: min(100%, 1100px) !important;
  height: auto !important;
  overflow: visible !important;
}

/* `htmlLabels: true` puts label text inside `foreignObject > div`, which
   inherits the container font. Keep it sans-serif, let it wrap, and never clip. */
figure.diagram .mermaid foreignObject,
figure.diagram .mermaid foreignObject > div,
figure.diagram .mermaid foreignObject span,
figure.diagram .mermaid .nodeLabel,
figure.diagram .mermaid .edgeLabel,
figure.diagram .mermaid .cluster-label,
figure.diagram .mermaid .label {
  font-family: system-ui, "Segoe UI", Arial, sans-serif !important;
  white-space: normal !important;
  overflow: visible !important;
  overflow-wrap: break-word;
  word-break: normal;
  text-overflow: clip;
  line-height: 1.25;
}

/* Edge labels sit on top of connectors; keep their backing plate opaque so the
   text stays legible, but do not let it clip the text. */
figure.diagram .mermaid .edgeLabel rect,
figure.diagram .mermaid .edgeLabel .label-container {
  overflow: visible !important;
}

figure.diagram figcaption {
  margin-top: .6em;
  font-style: italic;
  color: #444;
}

/* Data-table captions: styled like a table title, NOT a figure. */
table.data > caption {
  caption-side: top;
  text-align: left;
  font-weight: 600;
  margin-bottom: .35em;
  color: #222;
}

/* Modal-keyword emphasis: consistent bold+italic, but no color/no box. */
.modal-keyword,
strong em.modal-keyword,
em strong.modal-keyword {
  font-weight: 700;
  font-style: italic;
  color: inherit;
}
</style>