# build.ps1 — local Bikeshed build wrapper for the IOPv5 workspace (Windows/PowerShell)
#
# Adapts the DASH-IF-IOP build workflow to a local `bikeshed` install (Option B,
# no Docker) and to a corporate TLS-intercepting proxy.
#
# Usage:
#   ./build.ps1                       # build every specs/<part> that has a .bs file
#   ./build.ps1 part04-live-low-latency
#   ./build.ps1 part04-live-low-latency -Watch
#
# Prerequisites (one-time):
#   pip install -r requirements.txt
#   python tools/env/build_ca_bundle.py          # writes build-tools/corp-ca-bundle.pem
#   python tools/env/install_dashif_boilerplate.py
#   # then, with the CA bundle env vars set (this script sets them):
#   python -m bikeshed update

param(
    [string]$Part = "",
    [switch]$Watch
)

$ErrorActionPreference = "Stop"
$Root = $PSScriptRoot

# Point Python/requests at the merged corporate CA bundle so TLS verification
# works behind the proxy (see tools/env/build_ca_bundle.py).
$Bundle = Join-Path $Root "build-tools/corp-ca-bundle.pem"
if (Test-Path $Bundle) {
    $env:REQUESTS_CA_BUNDLE = $Bundle
    $env:SSL_CERT_FILE = $Bundle
} else {
    Write-Warning "CA bundle not found at $Bundle. If bikeshed fails on TLS, run: python tools/env/build_ca_bundle.py"
}

function Build-One([string]$dir) {
    $bs = Get-ChildItem -Path $dir -Filter *.bs -File | Select-Object -First 1
    if (-not $bs) { Write-Host "[skip] no .bs in $dir"; return }
    $out = [System.IO.Path]::ChangeExtension($bs.FullName, ".html")

    # Stage shared boilerplate into the spec dir (Bikeshed chroots includes to
    # the .bs directory, so parent-dir includes are not allowed). The DASH-IF-IOP
    # container does the equivalent via its Makefile. Staged copies are prefixed
    # with '_shared-' and removed after the build.
    $sharedDir = Join-Path $specsRoot "_boilerplate"
    $staged = @()
    if (Test-Path $sharedDir) {
        Get-ChildItem -Path $sharedDir -Filter *.inc.md -File | ForEach-Object {
            $dest = Join-Path $dir "_shared-$($_.Name)"
            Copy-Item $_.FullName $dest -Force
            $staged += $dest
        }
    }

    try {
        if ($Watch) {
            Write-Host "[watch] $($bs.Name) (Ctrl-C to stop)"
            python -m bikeshed watch $bs.FullName $out
        } else {
            Write-Host "[build] $($bs.Name)"
            python -m bikeshed spec $bs.FullName $out
            if (Test-Path $out) { Write-Host "   -> $out ($((Get-Item $out).Length) bytes)" }
        }
    } finally {
        # Clean up staged boilerplate (skip in watch mode, which stays running).
        if (-not $Watch) { $staged | ForEach-Object { Remove-Item $_ -ErrorAction SilentlyContinue } }
    }
}

$specsRoot = Join-Path $Root "specs"
if ($Part) {
    Build-One (Join-Path $specsRoot $Part)
} else {
    Get-ChildItem -Path $specsRoot -Directory | Where-Object { $_.Name -ne "_boilerplate" } | ForEach-Object {
        if (Get-ChildItem -Path $_.FullName -Filter *.bs -File -ErrorAction SilentlyContinue) {
            Build-One $_.FullName
        }
    }
}
