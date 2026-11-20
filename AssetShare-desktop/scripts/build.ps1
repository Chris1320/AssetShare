#!/usr/bin/env pwsh

[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$Target = "all"
)

$ErrorActionPreference = "Stop"

$ProjectDir = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$OutputDirNuitka = Join-Path $ProjectDir "build-nuitka"
$OutputDirWheel = Join-Path $ProjectDir "dist"

function Show-Help {
    $scriptName = Split-Path -Leaf $PSCommandPath
    @"
Usage: $scriptName [OPTIONS]

OPTIONS:
  all       Build wheel and Nuitka standalone package
  wheel     Build wheel package (.whl) via uv build
  nuitka    Compile standalone Windows executable and ZIP archive using Nuitka
  help      Show this help message
"@
}

function Invoke-CheckedCommand {
    param(
        [Parameter(Mandatory)]
        [string]$FilePath,
        [Parameter()]
        [string[]]$ArgumentList = @()
    )

    & $FilePath @ArgumentList
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code ${LASTEXITCODE}: $FilePath $($ArgumentList -join ' ')"
    }
}

function Build-Wheel {
    Write-Host "==> Building wheel package via uv build..."
    New-Item -ItemType Directory -Path $OutputDirWheel -Force | Out-Null
    Invoke-CheckedCommand -FilePath "uv" -ArgumentList @(
        "build",
        "--wheel",
        "--no-create-gitignore",
        "--out-dir", $OutputDirWheel
    )
    Write-Host "==> Wheel built in $OutputDirWheel"
}

function Build-Nuitka {
    Write-Host "==> Building standalone executable via Nuitka..."
    New-Item -ItemType Directory -Path $OutputDirNuitka -Force | Out-Null
    New-Item -ItemType Directory -Path $OutputDirWheel -Force | Out-Null

    $version = (& uv run -q python -c "import tomllib, pathlib; print(tomllib.loads(pathlib.Path('pyproject.toml').read_text(encoding='utf-8'))['project']['version'])").Trim()
    if ($LASTEXITCODE -ne 0 -or -not $version) {
        throw "Failed to read project version from pyproject.toml."
    }

    $nuitkaFlags = @(
        "run",
        "nuitka",
        "--mode=standalone",
        "--windows-console-mode=disable",
        "--enable-plugin=pyside6",
        "--assume-yes-for-downloads",
        "--output-dir=$OutputDirNuitka",
        "./src/assetshare"
    )

    Invoke-CheckedCommand -FilePath "uv" -ArgumentList $nuitkaFlags

    $distSource = Join-Path $OutputDirNuitka "assetshare.dist\*"
    $archivePath = Join-Path $OutputDirWheel "assetshare-desktop-v$version-windows.zip"

    Write-Host "==> Creating ZIP package at $archivePath..."
    Compress-Archive -Path $distSource -DestinationPath $archivePath -Force

    Write-Host "==> Compiled successfully!"
}

Push-Location $ProjectDir
try {
    switch ($Target.ToLowerInvariant()) {
        "all" {
            Build-Wheel
            Build-Nuitka
        }
        "wheel" {
            Build-Wheel
        }
        "nuitka" {
            Build-Nuitka
        }
        "help" {
            Show-Help
            exit 0
        }
        default {
            Write-Error "Unknown build target or option '$Target'"
            Write-Host ""
            Show-Help
            exit 1
        }
    }
}
finally {
    Pop-Location
}
