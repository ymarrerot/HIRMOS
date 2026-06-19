# HIRMOS Upgrade Guide

This guide explains how to think about upgrading or replacing an existing project’s HIRMOS framework payload.

The framework version source of truth is `_hirmos/hirmos.config.json` under `framework.version`.

## Before upgrading or replacing `_hirmos/`

1. Commit or back up your current project.
2. Review active HIRMOS session artifacts under `_hirmos/session/`.
3. Avoid replacing `_hirmos/` in the middle of an unresolved implementation session when possible.
4. Review the changelog for user-visible framework changes.

## Upgrading from 1.0.1 to 1.0.2

HIRMOS 1.0.2 is a documentation and release-note alignment update. It does not introduce a breaking framework migration.

Recommended posture:

1. Finish or pause any active HIRMOS session before replacing `_hirmos/`.
2. Commit or back up the current project.
3. Install the newer framework payload with the CLI or by replacing `_hirmos/` from `hirmos-framework.zip`.
4. Use `_hirmos/docs/reference/cli-reference.md` for terminal CLI usage.
5. Use `_hirmos/docs/reference/framework-command-reference.md` for AI-tool framework workflow commands.

User-visible changes:

- Public lifecycle wording is standardized as `User Request → Understand System State → Design → Implementation → Update System State`.
- CLI usage now has a dedicated complete reference document.
- Framework workflow commands and terminal CLI commands are documented separately.

No session artifact migration is required.

## Upgrading from 1.0.0 to 1.0.1

HIRMOS 1.0.1 is a documentation, release-packaging, and CLI-publishing guidance update. It does not introduce a breaking framework migration.

Recommended posture:

1. Finish or pause any active HIRMOS session before replacing `_hirmos/`.
2. Commit or back up the current project.
3. Install the newer framework payload with the CLI or by replacing `_hirmos/` from `hirmos-framework.zip`.
4. Review `_hirmos/CHANGELOG.md` for user-visible changes.

CLI note: the framework version and npm CLI package version may differ. To update the terminal CLI, run:

```bash
npm install -g hirmos@latest
```

## Installing HIRMOS 1.0

HIRMOS 1.0 is the initial public baseline. It is organized around current-state-first orchestration and governed session artifacts.

Expect the framework payload to include:

- `_hirmos/AGENTS.md`
- `_hirmos/README.md`
- `_hirmos/hirmos.config.json`
- `_hirmos/CHANGELOG.md`
- `_hirmos/UPGRADE_GUIDE.md`
- `_hirmos/core/`
- `_hirmos/docs/`
- `_hirmos/extensions/`
- `_hirmos/integrations/agent-tools/`
- `_hirmos/inputs/`
- `_hirmos/session/`
- `_hirmos/system/accepted-state/`
- `_hirmos/tools/validate.py`

## Command model

Use the terminal CLI for installation:

```bash
hirmos init
```

Use workflow commands inside the AI coding tool conversation:

```text
hirmos start
hirmos status
hirmos continue
hirmos close
```

Those workflow commands are not terminal CLI commands.

## Integration files

`hirmos init` installs `_hirmos/` and generates integration files for the AI tools you select, such as `AGENTS.md`, `CLAUDE.md`, Cursor rules, Copilot instructions, Gemini instructions, Windsurf rules, and Kiro steering files.

If an AI tool does not load the generated integration file, use the fallback bootstrap prompt:

```text
Read and follow _hirmos/AGENTS.md
```

## Versioning model

HIRMOS does not use a separate `_hirmos/VERSION` file.

Use:

```text
_hirmos/hirmos.config.json
```

for the framework version, and use:

```text
_hirmos/CHANGELOG.md
_hirmos/UPGRADE_GUIDE.md
```

for release notes and migration guidance.

## Recommended upgrade posture

For existing projects, prefer installing HIRMOS into a clean branch, then compare generated `_hirmos/` files against the existing project before merging.
