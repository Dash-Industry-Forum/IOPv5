#!/usr/bin/env python3

"""
Install the DASH-IF `dashif` Bikeshed group boilerplate into the local Bikeshed
data directory so `Group: dashif` builds locally (Option B, no Docker).

This *reuses* the DASH-IF-IOP authoring assets (boilerplate + group registration)
rather than replicating document content. Files are fetched from the public
DASH-IF-IOP repo and mapped onto Bikeshed's `org-dashif` convention.

Requires TLS to work — run after building the corporate CA bundle:
    python tools/env/build_ca_bundle.py
    $env:REQUESTS_CA_BUNDLE = "<...>/build-tools/corp-ca-bundle.pem"
    $env:SSL_CERT_FILE      = $env:REQUESTS_CA_BUNDLE
    python tools/env/install_dashif_boilerplate.py
"""

from __future__ import annotations

import os
from pathlib import Path

RAW = "https://raw.githubusercontent.com/Dash-Industry-Forum/DASH-IF-IOP/master/data/boilerplate/dashif"
FILES = [
    "defaults.include",
    "header.include",
    "logo.include",
    "status.include",
    "copyright.include",
]


def bikeshed_boilerplate_dir() -> Path:
    import bikeshed

    return Path(bikeshed.__file__).parent / "spec-data" / "boilerplate"


def main() -> None:
    import requests  # type: ignore

    dest = bikeshed_boilerplate_dir() / "org-dashif"
    dest.mkdir(parents=True, exist_ok=True)

    ok = 0
    for name in FILES:
        try:
            resp = requests.get(f"{RAW}/{name}", timeout=30)
        except Exception as exc:
            print(f"[warn] {name}: request failed ({exc})")
            continue
        if resp.status_code == 200:
            (dest / name).write_text(resp.text, encoding="utf-8")
            print(f"[ok]   {name} -> {dest / name}")
            ok += 1
        else:
            print(f"[skip] {name}: HTTP {resp.status_code} (may not exist upstream)")

    # Register the group in Bikeshed's doctypes.kdl so `Group: dashif` resolves.
    doctypes = bikeshed_boilerplate_dir() / "doctypes.kdl"
    text = doctypes.read_text(encoding="utf-8") if doctypes.exists() else ""
    if "dashif" not in text.lower():
        addition = (
            '\norg "dashif" {\n'
            '    group "dashif"\n'
            '    status "LD" "Living Document"\n'
            '    status "CR" "Community Review"\n'
            '    status "TS" "Technical Specification"\n'
            '}\n'
        )
        doctypes.write_text(text + addition, encoding="utf-8")
        print(f"[ok]   registered 'dashif' org in {doctypes.name}")
    else:
        print(f"[info] 'dashif' already present in {doctypes.name}")

    print(f"\n[done] installed {ok} boilerplate file(s) into org-dashif")


if __name__ == "__main__":
    main()
