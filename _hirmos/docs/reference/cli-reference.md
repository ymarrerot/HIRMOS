# CLI Reference

This is the complete user-facing guide for the HIRMOS terminal CLI.

The HIRMOS CLI installs the HIRMOS framework payload and AI-tool integration files into a project. It does not execute the HIRMOS workflow itself. Framework workflow commands such as `hirmos start`, `hirmos status`, `hirmos continue`, and `hirmos close` are used inside the AI coding tool after HIRMOS has been bootstrapped.

## Install the CLI

Install the latest published CLI from npm:

```bash
npm install -g hirmos
```

Check the installed CLI version:

```bash
hirmos --version
```

Check the latest published CLI version on npm:

```bash
npm view hirmos version
```

Update the CLI to the latest published version:

```bash
npm install -g hirmos@latest
```

## Command syntax

```bash
hirmos init [project-path] [--integration <ids>] [--source <path>] [--version <version>] [--offline]
```

`project-path` is optional. When omitted, HIRMOS initializes the current working directory.

## Basic install into a project

From the project root:

```bash
hirmos init
```

Or from another directory:

```bash
hirmos init ./your-project
```

A normal install adds a project-local `_hirmos/` folder and selected AI-tool integration files.

## What `hirmos init` does

`hirmos init` prepares a project to use HIRMOS by:

1. installing `_hirmos/` if the project does not already have it;
2. validating that the framework payload is complete enough for initialization;
3. generating or updating selected AI-tool integration files using managed HIRMOS blocks;
4. recording selected integrations in `_hirmos/hirmos.config.json`.

## Select AI-tool integrations

Use `--integration` with comma-separated integration IDs.

Supported integration IDs:

```text
agents
claude
cursor
copilot
codex
opencode
gemini
windsurf
kiro
```

Default:

```bash
hirmos init
```

The default installs the generic `agents` integration.

Examples:

```bash
hirmos init --integration agents,claude,cursor
hirmos init ./my-project --integration agents,copilot,codex,opencode
hirmos init ./my-project --integration agents,claude,gemini,windsurf,kiro
```

Some tools intentionally share the same generated file. For example, `agents`, `codex`, and `opencode` can use `AGENTS.md` as a shared bootstrap surface.

## Install a specific framework release

By default, `hirmos init` downloads the latest HIRMOS framework release from GitHub when the target project does not already have `_hirmos/`.

To install a specific framework release:

```bash
hirmos init --version 1.1.2
```

`hirmos init --version X.Y.Z` resolves the GitHub framework release tag `vX.Y.Z` and downloads the corresponding `hirmos-framework.zip` release asset.

## Use a local source package

Use `--source` when you want to install from a local framework payload instead of downloading from GitHub.

`--source` may point to:

- an `_hirmos/` directory;
- a folder containing `_hirmos/`;
- a `hirmos-framework.zip` release package.

Examples:

```bash
hirmos init ./my-project --source ./hirmos-framework.zip
hirmos init ./my-project --source ./_hirmos
hirmos init ./my-project --source ./local-framework-folder
```

## Offline mode

Use `--offline` to disable remote release downloads and CLI update checks.

Offline mode requires either an existing `_hirmos/` folder in the target project or an explicit `--source`.

Example:

```bash
hirmos init ./my-project --source ./hirmos-framework.zip --offline
```

If `_hirmos/` is missing and no source is provided, offline mode fails clearly instead of attempting a network download.

## CLI update notice

When `hirmos init` runs online, it checks whether a newer published HIRMOS CLI version is available on npm. If a newer version exists, the CLI prints a non-blocking update notice with the update command.

Disable the update check for one command:

```bash
HIRMOS_CLI_UPDATE_CHECK=0 hirmos init
```

Offline mode also skips the update check.

## After initialization

Open the project in the selected AI coding tool. The generated integration file is the normal bootstrap path for that tool.

If the integration file is not available or the tool did not load it, use this fallback bootstrap prompt inside the agent conversation:

```text
Read and follow _hirmos/AGENTS.md
```

Then use HIRMOS framework workflow commands inside the AI-agent conversation, for example:

```text
hirmos start "Add Google login"
hirmos status
hirmos continue
hirmos close
```

Those workflow commands are governed by the framework instructions and active session artifacts. They are not terminal CLI commands.

## Installed framework payload alignment

The CLI installs the packaged `_hirmos/` payload exactly as shipped by the framework release. Current framework releases include:

```text
_hirmos/session/SESSION_SCOPE.md
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/history/sessions/<session-id>/ARCHIVE_MANIFEST.md
```

The CLI package version is independent from the framework payload version. A framework-only documentation, template, or validator update does not require a CLI version bump unless the terminal `hirmos init` behavior changes.
