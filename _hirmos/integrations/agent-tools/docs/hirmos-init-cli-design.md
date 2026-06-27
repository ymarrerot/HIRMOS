# hirmos init CLI Implementation Design

## Status

**Phase:** DP-3A — CLI implementation design 
**Status:** Implemented through DP-3B and extended by DP-3C remote release install 
**Implementation scope:** Behavior contract for the published `hirmos init` CLI. Maintainer implementation source is outside the public repository surface.

## Purpose

Define the product-facing TypeScript CLI design for:

```bash
hirmos init [project-path] [--integration <ids>] [--source <path>] [--version <version>] [--offline]
```

The CLI exists to make an installed HIRMOS project discoverable to agent-native tools. It does not replace the HIRMOS agent instructions and does not run HIRMOS workflows.

## Product boundary

`hirmos init` is a developer-product entrypoint.

It must:

- make HIRMOS discoverable to selected agent tools;
- preserve user-owned files through managed blocks;
- update `_hirmos/hirmos.config.json` with installed integration metadata;
- keep the canonical HIRMOS agent instruction authority at `_hirmos/AGENTS.md`.

It must not:

- invoke Claude, Cursor, Copilot, Codex, Gemini, OpenCode, Windsurf, Kiro, or any other agent;
- run HIRMOS workflow commands;
- generate slash-command packs;
- duplicate HIRMOS agent-instruction doctrine in integration files;
- make `_hirmos/integrations/agent-tools/` part of Core runtime behavior.

## Package and ownership boundary

The public framework payload owns the integration registry and templates consumed by `hirmos init`:

```text
_hirmos/integrations/agent-tools/
```

The CLI implementation source is maintained outside the public repository surface. Public docs should describe the CLI behavior specification, not local maintainer source paths.

Do not place CLI implementation authority under:

```text
_hirmos/core/
_hirmos/integrations/agent-tools/
_hirmos/extensions/
```

Rationale:

- `_hirmos/core/` is framework/bootstrap authority, not product CLI source.
- `_hirmos/integrations/agent-tools/` contains integration templates consumed by the CLI, not the CLI implementation.
- `_hirmos/extensions/` contains workflow capabilities.
- local maintainer automation remains outside the public repository surface.

## CLI implementation note

The CLI is implemented and released as product tooling by the maintainer. The public repository documents the expected behavior of `hirmos init`; it does not expose the local maintainer workspace source layout for the CLI.

## Command surface

The CLI implements:

```bash
hirmos init [project-path] [--integration <comma-separated-list>] [--source <path>] [--version <version>] [--offline]
```

Defaults:

```text
project-path = .
integration = agents
source = existing _hirmos/ inside project-path, otherwise latest GitHub release
version = latest
```

Accepted integration ids:

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

Special integration shorthands are deferred.

Do not implement framework workflow commands as terminal CLI commands:

```bash
hirmos start
hirmos status
hirmos continue
hirmos close
```

Those commands are interpreted inside the AI-agent conversation after HIRMOS bootstrap. The terminal CLI remains focused on installation and integration setup for this release.

## Source behavior

### Existing project mode

If the target project already contains:

```text
_hirmos/AGENTS.md
```

then `hirmos init` uses the existing `_hirmos/` folder and does not reinstall HIRMOS.

### Local source mode

If `_hirmos/` does not exist and `--source` is provided, DP-3B should support source paths that are either:

```text
/path/to/hirmos-framework.zip
/path/to/folder-containing-_hirmos
/path/to/_hirmos
```

The installer should copy the `_hirmos/` payload into the target project.

### Remote release install

If `_hirmos/` does not exist and `--source` is not provided, the CLI downloads the HIRMOS framework release package from GitHub Releases.

Supported forms:

```bash
hirmos init
hirmos init --version latest
hirmos init --version 1.3.1
hirmos init --version v1.3.1
```

`--source` remains the deterministic local/offline path. `--offline` disables remote download and requires an existing `_hirmos/` or `--source`.

## Init algorithm

For `hirmos init`:

1. Resolve `project-path` to an absolute path.
2. If `_hirmos/` is missing:
   - install/copy `_hirmos/` from `--source` when provided;
   - fail clearly in `--offline` mode when no usable local source exists;
   - otherwise download `hirmos-framework.zip` from GitHub Releases using `--version` or `latest`.
3. Verify required framework files exist:
   - `_hirmos/AGENTS.md`
   - `_hirmos/hirmos.config.json`
   - `_hirmos/integrations/agent-tools/registry.json`
   - `_hirmos/integrations/agent-tools/templates/`
4. Parse and normalize selected integrations.
5. Read `_hirmos/integrations/agent-tools/registry.json`.
6. Validate every selected integration exists in the registry.
7. Deduplicate selected integrations while preserving registry order.
8. Group selected integrations by target path.
9. For each unique target path:
   - resolve target relative to project root;
   - load the registry template;
   - apply the managed-block update algorithm;
   - create parent directories as needed.
10. Merge selected integration ids into `_hirmos/hirmos.config.json`.
11. Print concise result summary and next steps.

## Integration target update behavior

The CLI must consume:

```text
_hirmos/integrations/agent-tools/registry.json
_hirmos/integrations/agent-tools/templates/
```

It must not hardcode integration targets in CLI source except as defensive tests.

If multiple selected integrations share the same target path, the target file is updated once.

Example:

```bash
hirmos init --integration agents,codex,opencode
```

Updates:

```text
AGENTS.md
```

Records:

```json
{
  "integrations": {
    "installed": ["agents", "codex", "opencode"]
  }
}
```

## Managed-block algorithm

Use the markers from registry:

```md
<!-- HIRMOS:START -->
<!-- HIRMOS:END -->
```

For each generated target:

1. Confirm rendered template contains exactly one complete HIRMOS managed block.
2. If target file does not exist:
   - create parent directories;
   - write rendered template as the full file.
3. If target file exists and contains exactly one HIRMOS managed block:
   - replace only that block;
   - preserve all content before and after it.
4. If target file exists and contains no HIRMOS managed block:
   - append the rendered block with safe spacing;
   - preserve all existing content.
5. If target file contains multiple or malformed HIRMOS blocks:
   - fail clearly;
   - do not modify the file.

The CLI must never overwrite user-owned content outside the HIRMOS managed block.

## `_hirmos/hirmos.config.json` merge behavior

The CLI must treat `_hirmos/hirmos.config.json` as project-local HIRMOS configuration metadata.

It is not runtime truth and not workflow authority. It must not configure user-facing interaction modes; HIRMOS uses the single canonical interaction posture authority.

Expected shape:

```json
{
  "schema_version": 1,
  "hirmos": {
    "framework_path": "_hirmos"
  },
  "stack": {
    "active_stack": "generic"
  },
  "integrations": {
    "installed": []
  }
}
```

Merge rules:

- parse JSON strictly;
- fail clearly if invalid;
- preserve unknown fields;
- preserve existing `stack`, `hirmos`, and unknown fields;
- create `integrations.installed` if missing;
- append selected integration ids if missing;
- do not remove existing integration ids;
- normalize installed integration order according to registry order;
- preserve ids already present but unknown to the current registry only if they are already installed;
- write formatted JSON with two-space indentation and a trailing newline.
- interaction posture is not configurable through project config; HIRMOS uses the canonical posture authority in `_hirmos/core/authority/INTERACTION_POSTURE.md`.

Example:

Before:

```json
{
  "schema_version": 1,
  "hirmos": {
    "framework_path": "_hirmos"
  },
  "stack": {
    "active_stack": "generic"
  },
  "integrations": {
    "installed": ["agents"]
  }
}
```

Command:

```bash
hirmos init --integration claude,cursor,copilot
```

After:

```json
{
  "schema_version": 1,
  "hirmos": {
    "framework_path": "_hirmos"
  },
  "stack": {
    "active_stack": "generic"
  },
  "integrations": {
    "installed": ["agents", "claude", "cursor", "copilot"]
  }
}
```

## Output behavior

### First initialization

If no integrations were previously installed, print:

```text
HIRMOS initialized.

Installed integrations:
- agents

Next step:
Open your AI coding tool in this project. The generated integration file is the normal bootstrap path. Then run a HIRMOS workflow command inside the AI-agent conversation, for example:

```text
hirmos start "<your request>"
hirmos status
hirmos continue
hirmos close
```

Fallback initialization:
If your tool does not automatically pick up the selected agent/tool integration files, copy and paste this prompt into your agent:

```text
Read and follow the instructions on _hirmos/AGENTS.md.
```

To add more integrations later:
hirmos init --integration claude,cursor,copilot
```

### Adding integrations later

If integrations were already installed, print:

```text
HIRMOS integrations updated.

Added:
- claude
- cursor
- copilot

Already installed:
- agents
```

Avoid printing a long first-run tutorial on every re-run.

## Error behavior

The CLI should fail closed and preserve files when a blocking condition appears.

Blocking errors include:

- target project path does not exist;
- missing `_hirmos/` and no `--source` provided;
- malformed source package;
- missing `_hirmos/AGENTS.md`;
- invalid `_hirmos/hirmos.config.json` JSON;
- invalid integration id;
- malformed registry;
- template missing or lacking exactly one managed block;
- target file contains malformed or multiple HIRMOS managed blocks.

Use clear, actionable messages. Do not partially update project config if integration file generation failed.

## Atomicity expectation

DP-3B should implement best-effort atomic behavior:

1. Validate all inputs first.
2. Render all target updates in memory.
3. Validate project config merge in memory.
4. Write integration files.
5. Write `_hirmos/hirmos.config.json` last.

If a write fails, surface the file path and stop.

Full transactional rollback is deferred, but avoid predictable partial writes by validating before writing.

## Validation commands for CLI implementation

Minimum validation:

```bash
npm test
npm run build
hirmos init <fixture> --integration agents
hirmos init <fixture> --integration claude,cursor,copilot
hirmos init <fixture> --integration agents,codex,opencode
python3 -m json.tool <fixture>/_hirmos/hirmos.config.json
python3 <fixture>/_hirmos/tools/validate.py
```

Fixture cases:

```text
fresh project with existing _hirmos/
project without _hirmos/ using --source zip
project without _hirmos/ using --source folder
existing AGENTS.md without HIRMOS block
existing AGENTS.md with HIRMOS block
malformed AGENTS.md with duplicate HIRMOS blocks
shared target agents,codex,opencode
invalid integration id
invalid hirmos.config.json
```

## Release packaging impact

The public framework package includes the framework payload consumed by `hirmos init`. CLI implementation source is maintained outside the public repository surface.

The Core package must continue to include:

```text
_hirmos/integrations/agent-tools/
```

because installed projects need the registry and templates for idempotent `hirmos init` re-runs.

The public repository may include:

```text
```

for npm publishing and contributor visibility.

## CLI implementation checklist

- [x] Implement `hirmos init` argument parsing.
- [x] Implement local `_hirmos/` verification.
- [x] Implement `--source` zip/folder install.
- [x] Implement registry loading from `_hirmos/integrations/agent-tools/registry.json`.
- [x] Implement managed-block update algorithm.
- [x] Implement shared-target deduplication.
- [x] Implement `_hirmos/hirmos.config.json` merge.
- [x] Add unit tests for managed-block and project config merge behavior.
- [x] Add fixture/integration tests for init scenarios.
- [x] Update README/docs after CLI behavior was validated.

## Non-goals

- No direct agent invocation.
- No shell workflow commands for Requirements/System Design/Implementation.
- No tool-native slash command generation.
- No extension installation.
- No integration removal command.
- No package publishing automation.


## General run preflight note

Installed projects should treat missing generated integration files as general run preflight issues, not special run-category failures. If a user installed from `dist` without generating an integration, HIRMOS can still bootstrap through `_hirmos/AGENTS.md` when that fallback is sufficient, but integration-specific affordances require the corresponding `hirmos init --integration <tool>` output and registry/templates.
