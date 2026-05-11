# Agent Integration Generation Examples

## Default initialization

Command:

```bash
hirmos init
```

Default behavior:

```text
project-path = .
integration = agents
source = existing _hirmos/ in project
```

Expected generated or updated file:

```text
AGENTS.md
```

Expected `_hirmos/project.json` integration state after success:

```json
{
  "integrations": {
    "installed": ["agents"]
  }
}
```

## Add selected integrations

Command:

```bash
hirmos init --integration claude,cursor,copilot
```

Expected generated or updated files:

```text
CLAUDE.md
.cursor/rules/hirmos.mdc
.github/copilot-instructions.md
```

Expected behavior:

- preserve any existing `integrations.installed` values;
- add `claude`, `cursor`, and `copilot` if missing;
- do not remove previously installed integrations;
- do not overwrite user content outside HIRMOS managed blocks.

## Shared AGENTS.md target

Command:

```bash
hirmos init --integration agents,codex,opencode
```

Expected generated or updated file:

```text
AGENTS.md
```

Expected behavior:

- update the HIRMOS managed block in `AGENTS.md` once;
- record all three selected integrations in `_hirmos/project.json`.

## Existing target file without HIRMOS block

Before:

```md
# Project agent guidance

Use pnpm for local commands.
```

After `hirmos init --integration agents`:

````md
# Project agent guidance

Use pnpm for local commands.

<!-- HIRMOS:START -->
## HIRMOS

This project uses HIRMOS.

For HIRMOS work, read and follow:

```text
_hirmos/HIRMOS_CORE.md
```

That file is the HIRMOS bootstrap authority for this project.

Do not treat this integration file as a replacement for HIRMOS Core.
<!-- HIRMOS:END -->
````

## Existing target file with HIRMOS block

If the target file already contains a HIRMOS managed block, `hirmos init` replaces only the content from `<!-- HIRMOS:START -->` through `<!-- HIRMOS:END -->`.

All user-owned content before and after the block remains unchanged.
