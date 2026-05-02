# Core Authority

This folder contains the active authoritative Core-local doctrine.

Use these files when you need to understand how the Core behaves, interprets, validates, or resolves framework mechanics.

For the local ownership rules of this folder, see [Folder rules](./folder-rules.md).

For operational Core runtime behavior and bootstrap framing, read [/_hirmos/core/README.md](../README.md).

## Active Core-local authority files

- `folder-rules.md`
- `installation-model.md`
- `validation-and-ordering.md`
- `hook-execution-control.md`
- `identity-display-execution-control.md`
- `extension-manifest-authority.md`
- `stack-system.md`
- `entrypoint-execution-contract.md`
- `runtime-trace-rules.md`

## Reading guidance

For most Core doctrine questions, start with:
1. `folder-rules.md`
2. the specific Core authority file relevant to the question at hand

Not every file in this folder must be read directly during bootstrap. Some files are direct bootstrap dependencies for normal Core operation; others are narrower doctrine references consulted when the active task needs them.

## Execution-control doctrine

- `identity-display-execution-control.md` governs `Identity display execution control`.
- `hook-execution-control.md` governs `Hook execution control`.
