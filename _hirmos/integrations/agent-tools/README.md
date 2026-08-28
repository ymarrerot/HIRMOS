# Agent Tool Integrations

## Purpose

Define the HIRMOS agent/tool integration templates consumed by the published `hirmos init` CLI.

These files are **bootstrap adapters**, not workflow authority and not Core runtime behavior. They are the normal tool-specific bootstrap path created by `hirmos init`.

HIRMOS can still be used without generated integration files through the manual fallback bootstrap instruction:

```text
Read and follow the instructions on _hirmos/AGENTS.md
```

## Scope

`hirmos init` generates thin context/bootstrap files for selected tools from this registry/template surface. It does not:

- invoke agents;
- install tool-native slash commands;
- install deep command/skill packs;
- duplicate HIRMOS agent-instruction doctrine;
- run HIRMOS workflow commands.

## Authority boundary

Every generated integration file must point directly to:

```text
_hirmos/AGENTS.md
```

That file remains the HIRMOS agent instruction authority for the project.

`AGENTS.md` is one supported integration target. It is not the HIRMOS source of truth and other tool-specific files must not depend on it.

## Locked integrations

The locked integration ids are:

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

The target registry is defined in [`registry.json`](./registry.json).

## Managed-block rule

Shared or conventional user-owned targets use the HIRMOS managed block markers. Dedicated HIRMOS-named tool files may be fully HIRMOS-managed later, but the current implementation keeps managed blocks everywhere for one safe update algorithm:

```md
<!-- HIRMOS:START -->
...
<!-- HIRMOS:END -->
```

Rules:

- If the target file exists and already contains a HIRMOS managed block, replace only that block.
- If the target file exists and does not contain a HIRMOS managed block, append a HIRMOS managed block.
- If the target file does not exist, create it with the HIRMOS managed block.
- Never overwrite user-owned content outside the HIRMOS managed block.

See [`managed-blocks.md`](./managed-blocks.md) for the exact update behavior.

See [`docs/hirmos-init-cli-design.md`](./docs/hirmos-init-cli-design.md) for the `hirmos init` CLI implementation design and behavior specification.

## Shared target rule

Some integrations intentionally use the same target file.

For example:

```text
agents -> AGENTS.md
codex -> AGENTS.md
opencode -> AGENTS.md
```

When multiple selected integrations share the same target file, generate or update the HIRMOS managed block only once and record all selected integration ids in `_hirmos/hirmos.config.json`.

## Relationship to workflow commands

Integration files do not define HIRMOS workflow commands.

The command grammar and command resolution remain governed by `_hirmos/core/command-protocol.md`:

```text
hirmos <command>[:entrypoint] [arguments]
```

Workflow commands resolve through installed extension manifests using `hirmos_commands`.

## Pre-edit gate propagation

All registry integrations, including shared-target integrations, must carry the same HIRMOS pre-edit gate through their generated guidance. The current registry targets are `agents`, `claude`, `cursor`, `copilot`, `codex`, `opencode`, `gemini`, `windsurf`, and `kiro`. Shared templates still count for every integration that uses them.

## Continue/status command capsule propagation

All registry integrations must carry the same compact, project-agnostic command capsules for `hirmos start`, `hirmos continue`, `hirmos status`, and `hirmos close`.

The `hirmos continue` capsule must state that `hirmos continue` must classify and gate before it codes, must append a continuation pass record before action, must evaluate whether implementation units are required even when the user does not request them, and must stop at `IU Plan — Review or Change` when IUs are required or requested but no accepted IU plan exists.

The `hirmos status` capsule must state that `hirmos status` is read-only, reports the current gate and exactly one recommended next command, and must not mutate product/source files or backfill artifacts.

This propagation applies to all current registry integrations: `agents`, `claude`, `cursor`, `copilot`, `codex`, `opencode`, `gemini`, `windsurf`, and `kiro`.


## Generated projection model

HIRMOS integration surfaces are generated projections of canonical command capsules. The source authority remains `_hirmos/core/*` and `_hirmos/AGENTS.md`; generated tool surfaces repeat the minimum command gates where the agent is most likely to ingest them.

Projection rules:

- always-on integration files carry compact recognition and safety invariants;
- command files carry the full per-command capsule for explicit command invocation;
- per-command `SKILL.md` packages carry the same full per-command capsule where a tool supports skills;
- HIRMOS does not generate one broad default `hirmos/SKILL.md`;
- commands and skills may duplicate behavior only as generated projection duplication from the same capsule marker.

The currently projected command capsules are `start`, `continue`, `status`, and `close`.
