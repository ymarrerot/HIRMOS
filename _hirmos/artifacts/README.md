# Artifacts

`/_hirmos/artifacts/` groups the framework's project/runtime/generated artifact families under one visible top-level home.

Use this folder when you need to understand where framework and extension runs write:
- runtime working context
- source-of-truth artifacts
- phase artifacts
- prompt artifacts
- result/deliverable artifacts
- implementation-stage operational records

This folder is an artifact-family umbrella. The subfolders inside it still have distinct roles.

## Artifact families

- `/_hirmos/artifacts/context/` — extension-owned runtime working context and related generated context artifacts
- `/_hirmos/artifacts/outputs/` — extension-owned result artifacts and deliverables for human or external/system consumption
- `/_hirmos/artifacts/sot/` — canonical project source-of-truth artifacts
- `/_hirmos/artifacts/phases/` — canonical project phase artifacts
- `/_hirmos/artifacts/prompts/` — canonical implementation prompt artifacts
- `/_hirmos/artifacts/ops/` — canonical implementation-stage operational records

For the authoritative rules that govern this umbrella and the differences between the artifact families, see:
- [Artifacts folder rules](./folder-rules.md)
- [Top-level folder definitions](../core/authority/framework/top-level-folder-definitions.md)


## Core runtime context artifacts

- `_hirmos/artifacts/context/core/bootstrap-report.md` is the Core-owned bootstrap completion report artifact.
- `_hirmos/artifacts/context/<extension-id>/<extension-entrypoint>/RUN_EXECUTION_CONTROLS.md` is the extension-scoped run execution controls artifact.
- `_hirmos/artifacts/context/<extension-id>/<extension-entrypoint>/HOOK_EXECUTION_CONTROL.md` is the extension-scoped hook execution control artifact for hook-aware runs.
