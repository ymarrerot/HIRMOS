# Command Protocol

## Purpose

Define the HIRMOS command surface, command matching rules, and Core-local command resolution behavior.

Use [Execution controls](./authority/core/execution-controls.md) for the canonical outer command path and run-scoped execution-controls lifecycle, [Identity display execution control](./authority/core/identity-display-execution-control.md) for surfaced-output validity and runtime identity declaration, [Hook execution control](./authority/core/hook-execution-control.md) for hook-aware execution, and [Entrypoint execution contract](./authority/core/entrypoint-execution-contract.md) for runnable entrypoint execution contracts.

## First-contact bootstrap

Before any `hirmos` workflow command can be trusted in a new AI session, initialize HIRMOS with the explicit bootstrap instruction:

```text
Read and follow the instructions on _hirmos/HIRMOS_CORE.md
```

That instruction loads `_hirmos/HIRMOS_CORE.md`, which then loads the bootstrap path and this command protocol.

## Supported command surface

### Workflow commands

```text
hirmos <command> [arguments...]
hirmos <command>:<entrypoint> [arguments...]
```

Examples:

```text
hirmos requirements
hirmos system-design
hirmos implementation
hirmos system-design:phase-design-cycle
```

Workflow commands are resolved through installed extension manifests. They are not hardcoded in agent integration files.

### Core utility commands

```text
hirmos list extensions
hirmos describe extension <id>
hirmos describe extension <id>:<entrypoint>
hirmos explain <command> [arguments...]
hirmos explain <command>:<entrypoint> [arguments...]
```

Core utility commands are resolved by Core directly. They do not use extension workflow command resolution, except that `hirmos explain ...` resolves the target workflow command to show the plan without executing it.

## Command matching rules

- Inputs beginning with `hirmos` are attempted HIRMOS commands.
- After removing the `hirmos` prefix and any immediately following whitespace, match the remaining text against the supported command surface.
- If a `hirmos` input does not match a supported command form, fail clearly.
- Do not reinterpret a malformed `hirmos` input as ordinary prose or best-effort conversation.
- The Core does not invent aliases.
- Unknown command names fail clearly.
- Harmless trailing punctuation immediately after an otherwise valid command may be ignored when doing so does not convert an unsupported form into a supported command.
- Normalization must not infer missing command words, repair malformed structure, or reinterpret prose as a command once `hirmos` matching fails.

## Workflow command resolution

For:

```text
hirmos <command> [arguments...]
```

Core must:

1. parse `<command>` and any trailing argument tail;
2. inspect installed extension manifests for `hirmos_commands.<command>`;
3. fail clearly if no installed extension declares the command;
4. fail closed and surface a conflict if multiple installed extensions declare the command;
5. load and validate the owning extension manifest;
6. confirm the owning extension includes `runnable` in `types`;
7. resolve the command's declared `entrypoint`;
8. validate required dependencies declared in `requires`;
9. resolve the active stack from `_hirmos/project.json` and the selected stack package;
10. follow [Execution controls](./authority/core/execution-controls.md) for the outer command path and any run execution controls added for this run;
11. read and honor the resolved entrypoint's `Execution Contract` section;
12. pass the captured argument tail to the active entrypoint and execute the workflow.

For:

```text
hirmos <command>:<entrypoint> [arguments...]
```

Core must first resolve `<command>` to the owning extension through `hirmos_commands.<command>`, then resolve `<entrypoint>` from the owning extension's `entrypoints` map. The named entrypoint must exist and remain public according to the extension manifest and local docs.

This allows user-friendly commands such as `hirmos system-design:phase-design-cycle` without introducing a separate `hirmos extension <extension-id>` command lane.

## Entrypoint arguments

Workflow commands may include an optional argument tail after the resolved command or command entrypoint.

Rules:

- Core resolves only the HIRMOS command name and optional entrypoint selector;
- any remaining trailing text is treated as the entrypoint argument tail;
- Core does not assign semantic meaning to that tail;
- argument parsing and validation belong to the owning extension;
- if an entrypoint requires parameters, its entry file and local extension spec must document them clearly.

Examples:

```text
hirmos implementation Phase 1
hirmos system-design:phase-design-cycle target-phase
hirmos explain system-design:phase-design-cycle target-phase
```

## Core utility command semantics

### `hirmos list extensions`

List installed extensions showing:

- extension id;
- types;
- summary;
- declared HIRMOS workflow commands, if present.

### `hirmos describe extension <id>`

Describe one installed extension.

The response should include:

- extension id;
- types;
- summary;
- default entrypoint if present;
- named public entrypoints if present;
- declared HIRMOS workflow commands if present;
- declared dependencies if present;
- exposed hooks if present;
- hook subscriptions if present.

### `hirmos describe extension <id>:<entrypoint>`

Describe one named public entrypoint exposed by an installed extension.

The response should include:

- extension id;
- target entrypoint name;
- resolved relative file path;
- extension summary;
- extension types;
- any exposed hooks relevant to that entrypoint;
- the entrypoint's execution-contract summary: purpose, produces, and terminal states.

### `hirmos explain <command> [arguments...]` and `hirmos explain <command>:<entrypoint> [arguments...]`

Show the resolved run plan without executing it.

The response should include:

- the owning extension id;
- the resolved entry file;
- the active stack id;
- any exposed hooks relevant to the active entrypoint;
- matching hook subscriptions;
- hook order;
- the execution controls that would be added according to [Execution controls](./authority/core/execution-controls.md).

## Manifest-declared HIRMOS commands

Extensions expose workflow commands through `extension.yaml`:

```yaml
hirmos_commands:
  <command-name>:
    description: <short user-facing description>
    entrypoint: <entrypoint-id>
    visibility: public | advanced | internal
    regular_user_safe: true | false
    arguments: <optional argument guidance>
```

Rules:

- `command-name` must be lowercase and may use hyphens.
- `entrypoint` must resolve to `entry` or a key in `entrypoints`.
- Regular-user commands should use stable workflow language, not internal file names.
- Advanced/internal commands may exist but should be marked accordingly.
- If multiple installed extensions declare the same command, Core must pause and surface the conflict.

## Dependency behavior

`requires` is the extension-level hard dependency field.

Rules:

- every id listed in `requires` must refer to an installed extension;
- if a required extension is missing, fail clearly;
- `requires` does not currently express entrypoint-level dependencies;
- hook subscriptions are optional integration declarations unless the target extension is also listed in `requires`;
- an installed extension may declare hook subscriptions for hook points exposed by another extension without making that other extension a hard installation dependency.

## Installation package runtime-folder boundary

Installation packages must keep extension source files separate from project-level runtime folders.

Rules:

- Extension installation packages must not ship project-level runtime folders.
- Extension installation packages should contain the extension folder that installs under `_hirmos/extensions/<extension-id>/`.
- Runtime folders such as `_hirmos/inputs/<extension-id>/`, `_hirmos/artifacts/context/<extension-id>/`, and `_hirmos/artifacts/outputs/<extension-id>/` are project runtime surfaces, not extension package contents.
- Framework-level project context folders such as `_hirmos/artifacts/context/project/` may be included by the framework install package because they are cross-extension project coordination namespaces, not extension-owned runtime folders.
- Extensions may document required runtime folders in their docs.
- The current `extension.yaml` manifest contract does not define a runtime-folder declaration field. Do not add runtime-folder declarations to `extension.yaml` unless the manifest authority is explicitly extended.
- Core/entrypoints must create missing runtime folders during init or first run.

## Hook-aware execution

Hook System v1 supports Action Hooks only. When a command/run is hook-aware, [Execution controls](./authority/core/execution-controls.md) adds `Hook execution control`, and [Hook execution control](./authority/core/hook-execution-control.md) governs that control.

## Surfaced output reminder

Surfaced chat-facing output is governed through `Identity display execution control` under [Execution controls](./authority/core/execution-controls.md) and [Identity display execution control](./authority/core/identity-display-execution-control.md).
