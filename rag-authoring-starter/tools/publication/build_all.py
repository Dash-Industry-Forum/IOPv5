#!/usr/bin/env python3
"""Build all Bikeshed specs into an output directory (cross-platform).

Mirrors build.ps1 for CI/Linux: stages shared boilerplate into each spec dir
(Bikeshed chroots includes to the .bs directory), builds every specs/<part>/*.bs,
copies the HTML into --out preserving a flat <part>.html layout, and writes an
index.html overview page (the dashif.org/IOP landing summary).

Usage:
    python tools/publication/build_all.py --out ../dist [--die-on warning]
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]        # rag-authoring-starter/
SPECS = ROOT / "specs"
SHARED = SPECS / "_boilerplate"

# Per-part one-line summaries for the overview page (aligned with, and simplified
# from, https://dashif.org/guidelines/iop-v5/).
PART_SUMMARY = {
    "part01-overview": "Overview, architecture and interfaces: reference architecture, interfaces and functional blocks.",
    "part02-core-cmaf": "Core principles and CMAF mapping: DASH data and timing model and the mapping of CMAF to DASH.",
    "part03-on-demand": "On-demand services: requirements and recommendations for DASH on-demand.",
    "part04-live-low-latency": "Live and low-latency live services: live service offerings including low-latency.",
    "part05-ad-insertion": "Ad insertion: SSAI and SGAI in a CMAF/DASH workflow.",
    "part06-content-protection": "Content protection and security: CENC, key rotation, ECCP and the content-protection schema.",
    "part07-video": "Video: CMAF media profiles and DASH signalling for video tracks.",
    "part08-audio": "Audio: audio interoperability points, coding profiles, packaging and MPD parameters.",
    "part09-text": "Text: subtitle and caption interoperability points and signalling.",
    "part10-events": "Events: MPD and inband events and timed metadata tracks.",
    "part11-additional-technologies": "Additional functionalities: thumbnails, query/token mechanisms, metadata tracks.",
    "part12-conformance-reference-tools": "Conformance and reference tools: validator, dash.js, livesim2 and test assets.",
}


def stage_shared(spec_dir: Path) -> list[Path]:
    staged: list[Path] = []
    if SHARED.is_dir():
        for inc in sorted(SHARED.glob("*.inc.md")):
            dest = spec_dir / f"_shared-{inc.name}"
            shutil.copyfile(inc, dest)
            staged.append(dest)
    return staged


def copy_images(spec_dir: Path, out_dir: Path) -> None:
    """Copy images directories from a spec to the output directory."""
    for img_dir_name in ("images", "Images", "figures", "Figures"):
        src = spec_dir / img_dir_name
        if src.is_dir():
            dst = out_dir / img_dir_name
            dst.mkdir(parents=True, exist_ok=True)
            for img_file in src.iterdir():
                if img_file.is_file():
                    shutil.copy2(img_file, dst / img_file.name)


def build_one(spec_dir: Path, out_dir: Path, die_on: str | None) -> bool:
    bs = next(iter(sorted(spec_dir.glob("*.bs"))), None)
    if not bs:
        return True  # nothing to build here
    staged = stage_shared(spec_dir)
    out_html = out_dir / f"{spec_dir.name}.html"
    cmd = [sys.executable, "-m", "bikeshed"]
    if die_on:
        cmd += ["--die-on", die_on]
    cmd += ["spec", str(bs), str(out_html)]
    try:
        print(f"[build] {spec_dir.name}")
        res = subprocess.run(cmd, cwd=spec_dir)
        ok = res.returncode == 0 and out_html.exists()
        if ok:
            print(f"   -> {out_html} ({out_html.stat().st_size} bytes)")
            copy_images(spec_dir, out_dir)
        else:
            print(f"   !! build failed for {spec_dir.name}", file=sys.stderr)
        return ok
    finally:
        for f in staged:
            f.unlink(missing_ok=True)


def write_index(out_dir: Path, built: list[str]) -> None:
    rows = []
    for name in sorted(PART_SUMMARY):
        summary = PART_SUMMARY[name]
        if name in built:
            link = f'<a href="{name}.html">{name}</a>'
        else:
            link = f'{name} <em>(under development)</em>'
        rows.append(f"    <tr><td>{link}</td><td>{summary}</td></tr>")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>DASH-IF IOP v5 — Overview</title>
<style>
 body {{ font-family: system-ui, sans-serif; max-width: 60rem; margin: 2rem auto; padding: 0 1rem; }}
 table {{ border-collapse: collapse; width: 100%; }}
 td, th {{ border: 1px solid #ccc; padding: .5rem .75rem; text-align: left; vertical-align: top; }}
 th {{ background: #f2f2f2; }}
 em {{ color: #888; }}
</style>
</head>
<body>
<h1>DASH-IF Interoperability Guidelines, Version 5 (IOP V5)</h1>
<p>IOP V5 is a multi-part set of documents. Version 5 is defined for use with
MPEG-DASH (ISO/IEC 23009-1) and constrained to deliver media formatted according
to MPEG CMAF (ISO/IEC 23000-19). This page is generated from the specification
sources; parts marked <em>under development</em> are not yet built here.</p>
<table>
  <thead><tr><th>Part</th><th>Summary</th></tr></thead>
  <tbody>
{chr(10).join(rows)}
  </tbody>
</table>
<p>Source repository:
<a href="https://github.com/Dash-Industry-Forum/IOPv5">Dash-Industry-Forum/IOPv5</a>.</p>
</body>
</html>
"""
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"[index] wrote {out_dir / 'index.html'}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="dist", help="output directory")
    ap.add_argument("--die-on", choices=["nothing", "fatal", "link-error", "warning"],
                    default=None, help="Bikeshed error level that aborts the build")
    args = ap.parse_args()

    out_dir = (ROOT / args.out).resolve() if not Path(args.out).is_absolute() else Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    built: list[str] = []
    failed: list[str] = []
    for spec_dir in sorted(p for p in SPECS.iterdir() if p.is_dir() and p.name != "_boilerplate"):
        if not any(spec_dir.glob("*.bs")):
            continue
        if build_one(spec_dir, out_dir, args.die_on):
            built.append(spec_dir.name)
        else:
            failed.append(spec_dir.name)

    write_index(out_dir, built)

    print(f"\nBuilt {len(built)} spec(s); {len(failed)} failed.")
    if failed:
        print("Failed:", ", ".join(failed), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
