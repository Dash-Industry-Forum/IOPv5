<!--
  Shared diagram styling for Mermaid figures.
  Overrides the dashif boilerplate's ".mermaid { display: table }" (which shrinks
  diagrams to content width) so engineering diagrams render at a readable size,
  centered, with a light frame. Include once per spec via a staged copy
  (_shared-diagram-style.inc.md), the same mechanism as the IPR boilerplate.
-->

<style>
/* Render Mermaid diagrams larger and centered rather than shrink-to-content. */
figure.diagram { text-align: center; margin: 1.5em 0; }
figure.diagram pre.mermaid,
figure.diagram .mermaid {
  display: block !important;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 auto !important;
  background: transparent !important;
  text-align: center;
}
figure.diagram svg {
  height: auto !important;
  max-width: 100%;
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
</style>
