#!/usr/bin/env python3
"""
Build a CA bundle that trusts the corporate TLS-intercepting proxy.

Behind a proxy that re-signs TLS (Zscaler / Netskope / Blue Coat / Qualcomm etc.),
Python `requests` (used by Bikeshed) fails with:
    SSLCertVerificationError: self-signed certificate in certificate chain

This tool builds a merged CA bundle so tools that honour REQUESTS_CA_BUNDLE /
SSL_CERT_FILE can verify again, WITHOUT disabling verification.

Strategy, most-robust first:
  1. Try to export the Windows trust store via `wincertstore` (if installed) or
     `certifi_win32`-style enumeration; merge Root + CA store certs onto certifi.
  2. Fall back to grabbing the chain the proxy actually presents for a known host
     using the stdlib `ssl` module in a permissive handshake, and append the
     unique PEM certs to certifi's bundle.

Output: build-tools/corp-ca-bundle.pem (merged: certifi + corporate roots).

Usage:
    python tools/env/build_ca_bundle.py
    python tools/env/build_ca_bundle.py --host raw.githubusercontent.com
"""

from __future__ import annotations

import argparse
import ssl
import socket
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "build-tools" / "corp-ca-bundle.pem"

PROBE_HOSTS = [
    "raw.githubusercontent.com",
    "api.csswg.org",
    "www.w3.org",
    "pypi.org",
]


def load_certifi() -> str:
    import certifi

    return Path(certifi.where()).read_text(encoding="utf-8")


def windows_store_pems() -> list[str]:
    """Best-effort export of Windows ROOT + CA stores as PEM strings."""
    pems: list[str] = []
    try:
        import wincertstore  # type: ignore
    except Exception:
        return pems

    for store_name in ("ROOT", "CA"):
        try:
            with wincertstore.CertSystemStore(store_name) as store:
                for cert in store.itercerts(usage=wincertstore.SERVER_AUTH):
                    pems.append(cert.get_pem().strip())
        except Exception:
            continue
    return pems


def proxy_chain_pems(host: str, port: int = 443) -> list[str]:
    """Return every cert in the chain the server/proxy presents for host.

    Uses a permissive context only to *read* the chain (not to trust it for
    real traffic). Requires Python built with the getpeercertchain support;
    falls back to the leaf cert if the full chain is unavailable.
    """
    pems: list[str] = []
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with socket.create_connection((host, port), timeout=15) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                # Python 3.13 exposes the verified chain; otherwise use leaf.
                get_chain = getattr(ssock, "get_verified_chain", None) or getattr(
                    ssock, "get_unverified_chain", None
                )
                if get_chain:
                    for cert in get_chain():
                        der = cert.public_bytes(getattr(cert, "DER", 0)) if hasattr(cert, "public_bytes") else None
                        if der is None:
                            # _ssl.Certificate objects: use .public_bytes(Encoding)
                            try:
                                pems.append(cert.get_info() and ssl.DER_cert_to_PEM_cert(cert.public_bytes(ssl._ssl.ENCODING_DER)))  # type: ignore
                            except Exception:
                                pass
                        else:
                            pems.append(ssl.DER_cert_to_PEM_cert(der))
                if not pems:
                    der = ssock.getpeercert(binary_form=True)
                    if der:
                        pems.append(ssl.DER_cert_to_PEM_cert(der))
    except Exception as exc:
        print(f"  [warn] could not read chain from {host}: {exc}")
    return [p.strip() for p in pems if p]


def dedupe(pems: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for pem in pems:
        key = pem.replace("\r", "").strip()
        if key and key not in seen:
            seen.add(key)
            out.append(key)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", help="Extra host to probe for the proxy chain")
    args = parser.parse_args()

    base = load_certifi()
    extra: list[str] = []

    win = windows_store_pems()
    if win:
        print(f"[ok] exported {len(win)} cert(s) from the Windows trust store")
        extra.extend(win)
    else:
        print("[info] wincertstore not available; falling back to chain probing")
        print("       (install with: pip install wincertstore  — recommended)")

    hosts = ([args.host] if args.host else []) + PROBE_HOSTS
    for host in hosts:
        chain = proxy_chain_pems(host)
        if chain:
            print(f"[ok] read {len(chain)} cert(s) from the chain for {host}")
            extra.extend(chain)

    extra = dedupe(extra)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    merged = base.rstrip() + "\n\n# --- corporate / proxy roots (auto-added) ---\n\n" + "\n\n".join(extra) + "\n"
    OUT.write_text(merged, encoding="utf-8")
    print(f"\n[done] wrote merged bundle: {OUT.relative_to(ROOT)}")
    print(f"       certifi base + {len(extra)} extra cert(s)")
    print("\nNext: point tools at it (PowerShell, current session):")
    print(f"  $env:REQUESTS_CA_BUNDLE = \"{OUT}\"")
    print(f"  $env:SSL_CERT_FILE      = \"{OUT}\"")


if __name__ == "__main__":
    main()
