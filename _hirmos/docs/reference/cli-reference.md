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
hirmos update [project-path] [--source <path>] [--version <version>] [--offline]
```

`project-path` is optional. When omitted, HIRMOS uses the current working directory.

Use `hirmos init` for first installation and integration selection. Use `hirmos update` to upgrade an existing project-local HIRMOS framework without replacing project-owned HIRMOS state.

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

## Update an existing HIRMOS project

For a normal upgrade, update the terminal CLI first, then run the framework update from an **idle HIRMOS session boundary**:

```bash
npm install -g hirmos@latest
cd /your/project/path
hirmos update
```

CLI **1.3.8 or newer** is required for the first-class `hirmos update` command. Projects already on an older HIRMOS framework can update directly after the CLI itself has been upgraded.

To target a specific framework release:

```bash
hirmos update --version X.Y.Z
```

`hirmos update` requires Python 3 because it runs the HIRMOS validator against the staged and installed framework. If Python 3 is unavailable, the update fails closed without reporting success.

`hirmos update` performs a state-preserving framework update transaction:

1. requires an existing valid `_hirmos/` installation and fails closed if a HIRMOS session is active;
2. downloads or stages the requested framework release and validates it before touching the installed framework;
3. replaces framework-owned surfaces such as `core/`, `docs/`, `extensions/`, `integrations/`, `stacks/`, `tools/`, and framework-owned root files;
4. preserves `_hirmos/system/`, `_hirmos/session/`, and `_hirmos/inputs/` exactly;
5. merges `_hirmos/hirmos.config.json` so new framework metadata/defaults are adopted while project-local stack settings, integration selection, and unknown project fields are preserved;
6. reconciles integration projections by removing obsolete generated command/skill surfaces and obsolete managed blocks without deleting surrounding user content, then regenerates the integrations already recorded in project configuration from the upgraded framework payload;
7. runs `_hirmos/tools/validate.py`; and
8. rolls back the installed framework and generated integration files if a post-swap update step fails.

If a session is active, close it under the currently installed framework first. Updating governance rules in the middle of a normal governed session is intentionally not the default path.

After a successful update, open a **new AI-agent context** so the upgraded bootstrap and integration projections are loaded.

`--integration` is intentionally an `init` option, not an `update` option. `hirmos update` reprojects the integrations already recorded in `_hirmos/hirmos.config.json`; use `hirmos init --integration ...` separately when you want to add integrations.

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

## Install or update a specific framework release

By default, `hirmos init` downloads the latest HIRMOS framework release from GitHub when the target project does not already have `_hirmos/`. `hirmos update` downloads the latest release when upgrading an existing installation.

To install or update to a specific framework release:

```bash
hirmos init --version X.Y.Z
hirmos update --version X.Y.Z
```

`--version X.Y.Z` resolves the GitHub framework release tag `vX.Y.Z` and downloads the corresponding `hirmos-framework.zip` release asset. `hirmos update` refuses a downgrade to an older semantic framework version.

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
hirmos update ./my-project --source ./hirmos-framework.zip
hirmos update ./my-project --source ./_hirmos
```

## Offline mode

Use `--offline` to disable remote release downloads and CLI update checks.

For `hirmos init`, offline mode requires either an existing `_hirmos/` folder in the target project or an explicit `--source`. For `hirmos update`, offline mode requires an explicit local `--source`, because an update needs a replacement framework payload.

Examples:

```bash
hirmos init ./my-project --source ./hirmos-framework.zip --offline
hirmos update ./my-project --source ./hirmos-framework.zip --offline
```

If `_hirmos/` is missing and no source is provided, offline mode fails clearly instead of attempting a network download.



## CLI update notice

When `hirmos init` or `hirmos update` runs online, it checks whether a newer published HIRMOS CLI version is available on npm. If a newer version exists, the CLI prints a non-blocking update notice with the update command.

Disable the update check for one command:

```bash
HIRMOS_CLI_UPDATE_CHECK=0 hirmos init
HIRMOS_CLI_UPDATE_CHECK=0 hirmos update
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

The CLI installs the packaged `_hirmos/` payload as shipped by the framework release. A fresh install contains the idle runtime scaffold plus canonical templates; active session/delivery artifacts are created just in time by governed framework commands. Key shipped surfaces include:

```text
_hirmos/session/SESSION_STATE.json
_hirmos/core/templates/session/SESSION_SCOPE.md
_hirmos/core/templates/session/SESSION_LEDGER.md
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/core/templates/system/delivery/DELIVERY_SCOPE.md
_hirmos/core/templates/system/delivery/phases/PHASE.md
```

Existing-project updates preserve live `_hirmos/system/`, `_hirmos/session/`, and `_hirmos/inputs/` rather than replacing them with release scaffolds.

The CLI package version is independent from the framework payload version. A framework-only documentation, template, or validator update does not require a CLI version bump unless terminal CLI behavior changes. CLI 1.3.8 is the first release that includes the state-preserving `hirmos update` command.
