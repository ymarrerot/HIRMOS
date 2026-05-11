# Managed Block Update Rules

## Purpose

Define the file-update behavior for `hirmos init` when it generates agent/tool integration files.

These rules are intentionally simple so v1 can be implemented safely before any direct agent invocation or tool-native command-pack generation exists.

## Markers

HIRMOS-managed integration content is delimited by:

```md
<!-- HIRMOS:START -->
```

and:

```md
<!-- HIRMOS:END -->
```

## Update algorithm

For each selected integration id:

1. Load `_hirmos/integrations/agent-tools/registry.json`.
2. Confirm the integration id exists in `integrations`.
3. Resolve the target path relative to the project root.
4. Load the target template from `_hirmos/integrations/agent-tools/templates/`.
5. Ensure the rendered template contains exactly one HIRMOS managed block.
6. If the target file does not exist:
   - create parent directories;
   - write the rendered template.
7. If the target file exists and contains exactly one HIRMOS managed block:
   - replace only the existing HIRMOS managed block;
   - preserve all content before and after the block.
8. If the target file exists and contains no HIRMOS managed block:
   - append two newlines if needed;
   - append the rendered HIRMOS managed block;
   - preserve all existing file content.
9. If the target file exists and contains malformed or multiple HIRMOS managed blocks:
   - fail clearly;
   - do not rewrite the file automatically.

## Shared-target behavior

If multiple selected integrations resolve to the same target path, update the target file once.

Example:

```text
agents,codex,opencode -> AGENTS.md
```

The generated HIRMOS block remains the same. `_hirmos/project.json` still records each selected integration id.

## Project config update

After successful integration file updates, merge the selected integrations into:

```json
{
  "integrations": {
    "installed": []
  }
}
```

Rules:

- preserve already-installed integration ids;
- append newly selected integration ids in normalized registry order;
- do not remove previously installed ids unless a future explicit remove command exists;
- do not reset unrelated `_hirmos/project.json` fields;
- fail clearly if `_hirmos/project.json` is invalid JSON.

## Non-goals

The managed-block updater must not:

- run agents;
- execute HIRMOS workflow commands;
- create or modify extension manifests;
- infer unsupported integration ids;
- overwrite user-owned content outside HIRMOS managed blocks;
- install tool-native command packs in v1.
