# Integration Tools Reference

HIRMOS is installed into a project so supported AI coding tools can read the same framework bootstrap and workflow instructions.

## Supported integrations

The supported integration targets are:

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

Some tools intentionally share the same generated file. For example, `agents`, `codex`, and `opencode` can use `AGENTS.md` as the shared bootstrap surface.

## Canonical integration source

The canonical integration registry and templates live in the framework payload:

```text
_hirmos/integrations/agent-tools/
  registry.json
  templates/
```

The published CLI reads this framework-owned surface during first installation and framework updates.

```text
The published CLI uses the integration templates during `hirmos init` and `hirmos update`; it does not own them.
The canonical integration registry/templates live in the framework payload under `_hirmos/integrations/agent-tools/`.
```

## Generated integration files

Depending on selected integrations, `hirmos init` may generate files such as the following; `hirmos update` reconciles the already-recorded integration set against the upgraded framework:

```text
AGENTS.md
CLAUDE.md
.cursor/rules/hirmos.mdc
.github/copilot-instructions.md
GEMINI.md
.windsurf/rules/hirmos.md
.kiro/steering/hirmos.md
```

Each generated file should point the AI tool back to the HIRMOS bootstrap and workflow model.

## Integration responsibility

Integration files should do three things:

1. bootstrap the AI tool into HIRMOS by pointing it to `_hirmos/AGENTS.md`;
2. expose the correct HIRMOS workflow command model;
3. avoid duplicating full framework protocol content.

The integration file is the normal doorway. Directly prompting the tool to read `_hirmos/AGENTS.md` is a fallback for manual installs or tools that did not load the generated integration file. The framework payload remains the source of truth.

## CLI responsibility

The CLI should:

- install or update the framework payload;
- preserve project-owned HIRMOS state during updates;
- read the framework-owned integration registry/templates;
- generate selected integrations on init and reconcile recorded integrations on update;
- preserve user files safely;
- validate required framework files and the upgraded installation.

The CLI should not own lifecycle semantics, capability behavior, or AI-agent workflow execution.

