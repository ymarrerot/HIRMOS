# Agent-native Integrations

This guide explains the HIRMOS integration-template model for contributors and the `hirmos init` CLI implementation in `_hirmos/tools/cli/`.

Need the concrete template registry? See [`_hirmos/integrations/agent-tools/registry.json`](../registry.json).

Need the CLI design? See [`_hirmos/integrations/agent-tools/docs/hirmos-init-cli-design.md`](./hirmos-init-cli-design.md).

## Goal

The product-facing `hirmos init` command makes a project discoverable to AI coding tools without asking each tool integration to duplicate HIRMOS doctrine.

Integrations are thin bootstrap adapters.

They point the selected tool directly to:

```text
_hirmos/HIRMOS_CORE.md
```

## Locked integration ids

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

## Locked targets

```text
agents    -> AGENTS.md
claude    -> CLAUDE.md
cursor    -> .cursor/rules/hirmos.mdc
copilot   -> .github/copilot-instructions.md
codex     -> AGENTS.md
opencode  -> AGENTS.md
gemini    -> GEMINI.md
windsurf  -> .windsurf/rules/hirmos.md
kiro      -> .kiro/steering/hirmos.md
```

## Authority boundary

`AGENTS.md` is one integration target, not the HIRMOS source of truth.

Every generated integration file must be self-contained and must point directly to `_hirmos/HIRMOS_CORE.md`.

Tool-specific files must not depend on `AGENTS.md`, because some tools may not read or prioritize `AGENTS.md` consistently.

## Managed-block safety

Shared or conventional user-owned targets use a HIRMOS managed block. Dedicated HIRMOS-named tool files may be fully HIRMOS-managed later, but the current implementation keeps managed blocks everywhere for one safe update algorithm.

The CLI must preserve existing user content outside the block.

See [`_hirmos/integrations/agent-tools/managed-blocks.md`](../managed-blocks.md).

## Workflow command boundary

Integrations do not define or install separate slash-command packs.

HIRMOS workflow commands are interpreted after HIRMOS Core is loaded:

```text
hirmos <command>[:entrypoint] [arguments]
```

Command ownership and entrypoint resolution remain manifest-declared through `hirmos_commands`.

## Public onboarding relationship

The regular-user docs should describe `hirmos init` as a terminal CLI command that generates bootstrap adapters. They should describe `hirmos requirements`, `hirmos system-design`, and `hirmos implementation` as HIRMOS workflow commands used inside the AI tool after Core bootstrap, not as CLI shell commands.
