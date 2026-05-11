# HIRMOS CLI

Product-facing HIRMOS CLI.

Implemented command:

```bash
hirmos init [project-path] [--integration <ids>] [--source <path>] [--version <version>] [--offline]
```

The CLI makes an installed HIRMOS project discoverable to selected agent-native tools by generating thin bootstrap integration files from `_hirmos/integrations/agent-tools/`.

It does not invoke agents, run HIRMOS workflows, install extensions, or generate slash-command packs.

## Usage

From a project root:

```bash
hirmos init
```

If `_hirmos/` is not present, the CLI downloads the latest HIRMOS framework release package and installs `_hirmos/` before generating integrations.

This defaults to:

```text
project-path = .
integration = agents
source = existing _hirmos/ in the project, otherwise latest GitHub release
version = latest
```

Generate specific integrations:

```bash
hirmos init --integration claude,cursor,copilot
```

Initialize another project path:

```bash
hirmos init /path/to/project --integration agents,claude
```

Install a specific HIRMOS release:

```bash
hirmos init --version 1.3.1
```

Install `_hirmos/` from a local source folder or release zip instead of downloading:

```bash
hirmos init /path/to/project --source /path/to/hirmos-framework.zip --integration agents
```

Disable remote download and require an existing `_hirmos/` or local `--source`:

```bash
hirmos init --offline
```

## CLI update notice

When `hirmos init` runs online, it checks whether a newer published HIRMOS CLI version is available on npm. If a newer version exists, the CLI prints a non-blocking message such as:

```text
A newer HIRMOS CLI is available: 1.3.2.
Update with: npm install -g hirmos@latest
```

The notice does not stop initialization. Network failures, registry errors, or timeouts are ignored.

Use `--offline` to disable both remote framework download and the update check. To disable only the update notice while keeping remote framework download available, run:

```bash
HIRMOS_CLI_UPDATE_CHECK=0 hirmos init
```

## Supported integrations

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

Some integrations share the same target file. For example, `agents`, `codex`, and `opencode` all use `AGENTS.md` as the safe generic bootstrap target.

## Managed-block behavior

For existing files, the CLI updates only the HIRMOS managed block:

```md
<!-- HIRMOS:START -->
...
<!-- HIRMOS:END -->
```

If the file exists and has no HIRMOS block, the CLI appends one. User-owned content outside the block is preserved.

## Project config behavior

The CLI merges selected integration IDs into:

```text
_hirmos/project.json
```

under:

```json
{
  "integrations": {
    "installed": []
  }
}
```

Re-running `hirmos init --integration ...` is additive and does not remove previously recorded integrations.

## Workflow commands are not CLI commands

These are HIRMOS workflow commands to use inside the AI tool after HIRMOS Core has loaded:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

The CLI implements `hirmos init`.
