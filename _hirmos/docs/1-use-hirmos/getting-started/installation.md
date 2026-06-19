# Installation

HIRMOS installs into a target project as one project-local framework folder:

```text
_hirmos/
```

The installed framework folder is self-contained and should live beside your project files.

## Install with the CLI

Install the HIRMOS CLI from npm:

```bash
npm install -g hirmos
```

Then initialize HIRMOS inside your project:

```bash
cd /your/project/path
hirmos init
```

The CLI installs the framework payload and selected AI-tool integration files. It does not own the framework method, session lifecycle, or integration templates.

For the complete CLI guide, including version checks, updates, `--integration`, `--source`, `--version`, and `--offline`, see [CLI Reference](../../reference/cli-reference.md).

The canonical integration registry and templates live inside the framework payload:

```text
_hirmos/integrations/agent-tools/
```

## Supported AI-tool integrations

HIRMOS supports these integration targets:

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

Some tools intentionally share the same generated instruction file. For example, `agents`, `codex`, and `opencode` can share `AGENTS.md` where that is the tool-facing instruction surface.

## Manual install

You can also copy the release package's `_hirmos/` folder into the target project root.

Manual installation does not generate tool-specific integration files. In that case, initialize the AI tool with this fallback bootstrap prompt:

```text
Read and follow _hirmos/AGENTS.md
```

## What the project root should look like

```text
your-project/
├── your existing project files
├── AGENTS.md or other tool integration files
└── _hirmos/
    ├── AGENTS.md
    ├── hirmos.config.json
    ├── core/
    ├── docs/
    ├── extensions/
    ├── inputs/
    ├── integrations/
    ├── session/
    ├── system/
    ├── stacks/
    └── tools/
```

Do not copy development-only work areas into a normal target project. The installed `_hirmos/` folder is the runtime authority for the framework.

## Framework workflow commands

After bootstrap, the common HIRMOS workflow commands are:

```text
hirmos start "<your request>"
hirmos continue
hirmos status
hirmos close
```

These are agent-facing HIRMOS commands used inside the AI-tool conversation. They are not terminal CLI commands. See [Framework Command Reference](../../reference/framework-command-reference.md).

## Validate an installation

If Python is available, you can check the installed framework surface with:

```bash
python3 _hirmos/tools/validate.py
```

Validation checks the installed framework structure and key static rules. It does not prove that a particular run was correct; active run correctness depends on session artifacts, execution controls, unresolved-item disposition, and evidence.

## Runtime state

A fresh installation includes minimal runtime folders. Active session artifacts are created from templates when HIRMOS commands require them. Do not edit templates as if they were runtime evidence.
