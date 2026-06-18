# HIRMOS Upgrade Guide

This guide explains how to think about upgrading or replacing an existing project’s HIRMOS framework payload.

The framework version source of truth is `_hirmos/hirmos.config.json` under `framework.version`.

## Before upgrading or replacing `_hirmos/`

1. Commit or back up your current project.
2. Review active HIRMOS session artifacts under `_hirmos/session/`.
3. Avoid replacing `_hirmos/` in the middle of an unresolved implementation session when possible.
4. Review the changelog for user-visible framework changes.

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
