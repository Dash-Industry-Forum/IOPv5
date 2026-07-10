param(
    [switch]$RecreateVenv
)

$ErrorActionPreference = 'Stop'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$VenvDir = Join-Path $ScriptDir '.venv'
$PythonExe = Join-Path $VenvDir 'Scripts\python.exe'
$ActivateScript = Join-Path $VenvDir 'Scripts\Activate.ps1'

if ($RecreateVenv -and (Test-Path $VenvDir)) {
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

Write-Host '[mcp-server] starting MCP server...'
python server.py
