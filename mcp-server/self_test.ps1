param(
    [switch]$RecreateVenv,
    [switch]$StartServer
)

$ErrorActionPreference = 'Stop'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$VenvDir = Join-Path $ScriptDir '.venv'
$PythonExe = Join-Path $VenvDir 'Scripts\python.exe'
$ActivateScript = Join-Path $VenvDir 'Scripts\Activate.ps1'

if ($RecreateVenv -and (Test-Path $VenvDir)) {
    Write-Host '[mcp-server] removing existing virtual environment...'
    Remove-Item -Recurse -Force $VenvDir
}

if (-not (Test-Path $PythonExe)) {
    Write-Host '[mcp-server] creating virtual environment...'
    python -m venv .venv
}

Write-Host '[mcp-server] activating virtual environment...'
. $ActivateScript

Write-Host '[mcp-server] installing requirements...'
pip install -r requirements.txt

Write-Host '[mcp-server] running smoke test...'
python smoke_test.py
if ($LASTEXITCODE -ne 0) {
    throw 'Smoke test failed.'
}

if ($StartServer) {
    Write-Host '[mcp-server] starting MCP server...'
    python server.py
}
else {
    Write-Host '[mcp-server] self-test completed successfully.'
    Write-Host '[mcp-server] to start the server now, run:'
    Write-Host '  ./start.ps1'
    Write-Host 'or:'
    Write-Host '  ./self_test.ps1 -StartServer'
}
