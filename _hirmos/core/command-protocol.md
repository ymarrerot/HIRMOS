# Command Protocol

## Purpose

Describe the operational command behavior of the Core.

Use [Execution controls](./authority/core/execution-controls.md) for the sole canonical outer command path and run-scoped execution-controls lifecycle, [Identity display execution control](./authority/core/identity-display-execution-control.md) for surfaced-output validity and runtime identity declaration, [Hook execution control](./authority/core/hook-execution-control.md) for hook-aware execution, and [Entrypoint execution contract](./authority/core/entrypoint-execution-contract.md) for runnable entrypoint execution contracts.

## Run execution controls

For running any command, Core follows [Execution controls](./authority/core/execution-controls.md) as the sole canonical owner of the outer command path and `RUN_EXECUTION_CONTROLS.md` lifecycle.

This file references that model but does not restate the outer command-execution sequence.

## Entrypoint Arguments

`cmd: run extension ...` and `cmd: explain run extension ...` may include an optional argument tail after the resolved extension target.

Rules:
- the core resolves only the extension id and optional entrypoint name;
- any remaining trailing text is treated as the entrypoint argument tail;
- the core does not assign semantic meaning to that tail;
- argument parsing and validation belong to the owning extension;
- if an entrypoint requires parameters, its entry file and local extension spec must document them clearly.

Examples:
```text
cmd: run extension some-extension:some-entrypoint target-value
cmd: explain run extension some-extension:some-entrypoint target-value
```

## Installation package runtime-folder boundary

Installation packages must keep extension source files separate from project-level runtime folders.

Rules:
- Extension installation packages must not ship project-level runtime folders.
- Extension installation packages should contain the extension folder that installs under `_hirmos/extensions/<extension-id>/`.
- Runtime folders such as `_hirmos/inputs/<extension-id>/`, `_hirmos/artifacts/context/<extension-id>/`, and `_hirmos/artifacts/outputs/<extension-id>/` are project runtime surfaces, not extension package contents.
- Extensions may document required runtime folders in their docs.
- The current `extension.yaml` manifest contract does not define a runtime-folder declaration field. Do not add runtime-folder declarations to `extension.yaml` unless the manifest authority is explicitly extended.
- Core/entrypoints must create missing runtime folders during init or first run.

Invalid installation package shape for a standalone extension:

```text
_hirmos/
├── inputs/<extension-id>/
├── artifacts/context/<extension-id>/
└── extensions/<extension-id>/
```

Valid installation package shape for a standalone extension:

```text
<extension-id>/
├── README.md
├── extension.yaml
├── entrypoints/
├── specs/
├── templates/
├── docs/
├── CHANGELOG.md
└── UPGRADE_GUIDE.md
```

After installation, the extension folder lives at `_hirmos/extensions/<extension-id>/`. Runtime folders may then be created under `_hirmos/inputs/` and `_hirmos/artifacts/` by the responsible Core/entrypoint path.

## Command Semantics

### `cmd: run extension <id> [arguments...]`

Run the default public entrypoint of one installed runnable extension, optionally passing an opaque argument tail to that entrypoint.

Under uncertainty, apply the bootstrap Step 0 — Framework-wide uncertainty rule before interpreting, validating, or dispatching the command.

Interpretation:
1. resolve the target extension id;
2. capture any trailing argument tail for the active entrypoint;
3. load and validate the target manifest;
4. confirm the target declares `types: [runnable]` or otherwise includes `runnable` in `types`;
5. resolve the default public entrypoint from `entry`;
6. validate required dependencies declared in `requires`;
7. resolve the active stack from `_hirmos/STACK_CONFIG.json` and the selected stack package;
8. follow [Execution controls](./authority/core/execution-controls.md) for the outer command path and any run execution controls added for this run;
9. read and honor the resolved entrypoint's `Execution Contract` section as defined by [Entrypoint execution contract](./authority/core/entrypoint-execution-contract.md);
10. pass the captured argument tail to the active entrypoint and execute the workflow.

### `cmd: run extension <id>:<entrypoint> [arguments...]`

Run one named public entrypoint exposed by an installed runnable extension, optionally passing an opaque argument tail to that entrypoint.

Interpretation:
1. resolve the target extension id;
2. capture any trailing argument tail for the active entrypoint;
3. load and validate the target manifest;
4. confirm the target declares `types: [runnable]` or otherwise includes `runnable` in `types`;
5. resolve the named public entrypoint from `entrypoints.<entrypoint>`;
6. validate required dependencies declared in `requires`;
7. resolve the active stack from `_hirmos/STACK_CONFIG.json` and the selected stack package;
8. follow [Execution controls](./authority/core/execution-controls.md) for the outer command path and any run execution controls added for this run;
9. read and honor the resolved entrypoint's `Execution Contract` section as defined by [Entrypoint execution contract](./authority/core/entrypoint-execution-contract.md);
10. pass the captured argument tail to the active entrypoint and execute the workflow.

### `cmd: describe extension <id>`

Describe one installed extension.

The response should include:
- extension id;
- types;
- summary;
- default entrypoint if present;
- named public entrypoints if present;
- declared dependencies if present;
- exposed hooks if present;
- hook subscriptions if present.

### `cmd: describe extension <id>:<entrypoint>`

Describe one named public entrypoint exposed by an installed extension.

The response should include:
- extension id;
- target entrypoint name;
- resolved relative file path;
- extension summary;
- extension types;
- any exposed hooks relevant to that entrypoint;
- the entrypoint's execution-contract summary: purpose, produces, and terminal states.

### `cmd: list extensions`

List installed extensions showing:
- extension id;
- types;
- summary.

### `cmd: explain run extension <id> [arguments...]` and `cmd: explain run extension <id>:<entrypoint> [arguments...]`

Show the resolved run plan without executing it.

The response should include:
- the resolved entry file;
- the active stack id;
- any exposed hooks relevant to the active entrypoint;
- matching hook subscriptions;
- hook order;
- the execution controls that would be added according to [Execution controls](./authority/core/execution-controls.md).

## Hook-aware execution

Hook System v1 supports Action Hooks only. When a command/run is hook-aware, [Execution controls](./authority/core/execution-controls.md) adds `Hook execution control`, and [Hook execution control](./authority/core/hook-execution-control.md) governs that control.

## Surfaced output reminder

Surfaced chat-facing output is governed through `Identity display execution control` under [Execution controls](./authority/core/execution-controls.md) and [Identity display execution control](./authority/core/identity-display-execution-control.md).


# Core Command Surface

## Purpose

Define the public command surface that the Core exposes and the Core-local rules that govern command matching and dependency interpretation.

## Supported Commands

```text
cmd: list extensions
cmd: describe extension <id>
cmd: describe extension <id>:<entrypoint>
cmd: run extension <id> [arguments...]
cmd: run extension <id>:<entrypoint> [arguments...]
cmd: explain run extension <id> [arguments...]
cmd: explain run extension <id>:<entrypoint> [arguments...]
```

## Core command invocation prefix

- Inputs beginning with `cmd:` are attempted Core commands.
- After removing the `cmd:` prefix and any immediately following whitespace, match the remaining text against the exact public Core command surface.
- If the remaining text does not match a supported command form, fail clearly.
- Do not reinterpret a `cmd:` input as ordinary prose or best-effort conversation.

Rules:
- command words after `cmd:` are lowercase;
- extension ids must match manifest ids;
- entrypoint names must match manifest `entrypoints` keys when used;
- the Core does not invent aliases;
- harmless trailing punctuation immediately after an otherwise valid command, such as `.`, `:`, or `;`, may be ignored during command normalization when doing so does not convert an unsupported form into a supported command;
- normalization must not infer missing command words, repair malformed structure, or reinterpret prose as a command once `cmd:` matching fails.

## Exact Public-Surface Matching

- Commands must use the exact manifest-declared extension id and named public entrypoint after the `cmd:` prefix is removed.
- Bare historical command phrases are not part of the public Core command surface.
- The Core does not infer aliases from extension-spec filenames or workflow nicknames.
- Unknown names fail clearly.
- Once a `cmd:` input is matched to a supported Core command form, follow [Execution controls](./authority/core/execution-controls.md) for the outer execution lifecycle before surfacing command-valid completion.

## Invalid command guidance

When a `cmd:` input fails exact public-surface matching, the runtime should surface clear invalid-command guidance that recommends only the supported public command forms.

It must not recommend old bare-command forms such as `list extensions`, `describe extension <id>`, or `describe extension <id>:<entrypoint>`.

Recommended guidance examples:
- `cmd: list extensions`
- `cmd: describe extension <id>`
- `cmd: describe extension <id>:<entrypoint>`

## Dependency Behavior

`requires` is currently the only extension-level hard dependency field.

Rules:
- every id listed in `requires` must refer to an installed extension;
- if a required extension is missing, fail clearly;
- `requires` does not currently express entrypoint-level dependencies;
- hook subscriptions are optional integration declarations unless the target extension is also listed in `requires`;
- an installed extension may declare hook subscriptions for hook points exposed by another extension without making that other extension a hard installation dependency.

## Dependency scope

`requires` validates required installed extensions before execution begins.

Hook subscriptions do not create hard dependencies by themselves. If the hook-owning extension is not installed or the active run does not resolve the subscribed hook point, the subscription remains dormant and must not make unrelated commands fail.

`requires` does not currently support entrypoint-level dependency declarations.

## Boundary note

This authority file defines the public command surface and Core-local dependency interpretation.
It does not define the stepwise operational runtime sequence for command execution. That behavior belongs in `/_hirmos/core/authority/core/execution-controls.md` and `/_hirmos/core/execution-model.md`.
