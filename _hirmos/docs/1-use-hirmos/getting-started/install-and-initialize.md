# Install and Initialize HIRMOS

Use this guide when you want the productized first-run path for a project.

HIRMOS has two layers that are easy to confuse:

```text
hirmos init
```

is a **terminal CLI command**. It makes an installed HIRMOS project discoverable to agent-native tools.

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

are **HIRMOS workflow commands**. Use them inside your AI tool after HIRMOS Core has loaded. They are not terminal shell commands.

## 1. Install the CLI

Install the HIRMOS CLI:

```bash
npm install -g hirmos
```

Then from the project root, run:

```bash
hirmos init
```

If `_hirmos/` is missing, `hirmos init` downloads the latest HIRMOS framework release package and installs `_hirmos/` into the project. If `_hirmos/` already exists, it uses the local framework files and only updates integrations.

This defaults to:

```text
project-path = .
integration = agents
source = existing _hirmos/ in the project, otherwise latest GitHub release
version = latest
```

It creates or updates `AGENTS.md` with a HIRMOS managed block that points the agent directly to:

```text
_hirmos/HIRMOS_CORE.md
```

To add tool-specific bootstrap files, rerun `hirmos init` with integrations:

```bash
hirmos init --integration claude,cursor,copilot
```


To install a specific HIRMOS framework release, use:

```bash
hirmos init --version 1.3.1
```

To install from a local release package or local framework folder instead of downloading, use:

```bash
hirmos init /path/to/project --source /path/to/hirmos-framework.zip --integration agents
```

To disable remote download and require an existing `_hirmos/` or `--source`, use:

```bash
hirmos init --offline
```

Supported integration IDs are:

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

`hirmos init` is idempotent. Re-running it merges the selected integrations into `_hirmos/project.json` and preserves user-owned content outside HIRMOS managed blocks.

## 3. Start the AI session

Open your AI tool in the project.

If the selected tool reads the generated integration file, it should discover that the project uses HIRMOS.

For the safest first run, you can still explicitly tell the AI tool:

```text
Read and follow the instructions on _hirmos/HIRMOS_CORE.md
```

This remains the canonical fallback and the canonical bootstrap authority.

## 4. Run HIRMOS workflow commands inside the AI tool

After Core has loaded, use the HIRMOS workflow commands as agent-facing instructions:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

These commands resolve through installed extension manifests. They are not executed by the CLI.

## What `hirmos init` does not do

`hirmos init` does not:

- invoke agents;
- run Requirements, System Design, or Implementation;
- install slash-command packs;
- replace HIRMOS Core;
- overwrite user-owned content outside HIRMOS managed blocks.

## Go next

- Continue to [Quickstart](quickstart.md).
- Read [Use HIRMOS in 3 Steps](use-hirmos-in-3-steps.md).
- Read [Core commands](core-commands.md) when you need the HIRMOS workflow command syntax.
