<div align="center">
    <img src="./assets/logo.svg" alt="AssetShare Logo" width="200">
    <h1>AssetShare</h1>
    <p>Multi-User Digital Asset Management (DAM) System</p>
</div>

[![codecov](https://codecov.io/gh/Chris1320/AssetShare/graph/badge.svg?token=03722ScIu1)](https://codecov.io/gh/Chris1320/AssetShare)

**AssetShare** is a multi-user Digital Asset Management (DAM) system that allows
you to upload, manage, and share digital assets for media production.

> [!warning]
> This project is still in development and may not be stable. Use at your own risk.

## Requirements

| Requirement   | AssetShare Server        | AssetShare Web           | AssetShare Desktop |
| ------------- | ------------------------ | ------------------------ | ------------------ |
| Docker/Podman | >= `29.9.3` / >= `5.8.9` | >= `29.9.3` / >= `5.8.9` |                    |
| uv            | >= `0.13.7`              |                          | >= `0.13.7`        |
| Python        | `3.14`                   |                          | `3.15`             |
| Bun           |                          | >= `1.4.2`               |                    |

## Installation

### AssetShare Server (with AssetShare Web)

1. Make sure you have Docker or Podman installed on your system.
2. Clone the repository.
3. Adjust the configuration files.
4. Start the containers using Compose.

```bash
git clone https://github.com/Chris1320/AssetShare.git
cd AssetShare
# Edit the configuration files as needed
docker compose up -d
# or if using Podman...
podman compose up -d
```

### AssetShare Desktop

AssetShare Desktop is mainly developed for Windows, but it should work on Linux
as well.

You can download the latest version of AssetShare Desktop from the
[releases page](https://github.com/Chris1320/AssetShare/releases) or manually
run/build it from source.

1. Make sure you have Python and uv installed on your system.
2. Clone the repository.
3. Run the desktop application.

```powershell
git clone https://github.com/Chris1320/AssetShare.git
Set-Location AssetShare\AssetShare-desktop\src
uv run -m assetshare
```

To create a standalone executable, run the build script in `AssetShare-desktop/scripts/`:

```powershell
git clone https://github.com/Chris1320/AssetShare.git
Set-Location AssetShare\AssetShare-desktop
& .\scripts\build.ps1 nuitka
```

## Development

![Codecov Graph](https://codecov.io/gh/Chris1320/AssetShare/graphs/sunburst.svg?token=03722ScIu1)
