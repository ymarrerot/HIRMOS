# HIRMOS Core

This folder contains the minimal framework core runtime surfaces.

For authoritative Core-local doctrine, read [Core authority](./authority/core/README.md).
For the centralized authority system, read [Authority overview](./authority/README.md).

## What lives here

`/_hirmos/core/` contains:
- bootstrap-facing runtime files used directly by the framework core
- command interpretation and execution-model files
- the centralized authority system under `/_hirmos/core/authority/`

## Reading rule

When Core is executing or resolving a command, it should read:
1. the relevant files in `/_hirmos/core/`
2. the relevant authoritative doctrine in `/_hirmos/core/authority/core/`
3. any other authoritative doctrine referenced from those files when needed

Not every file in `/_hirmos/core/` and `/_hirmos/core/authority/` must be read directly during bootstrap.

## Key Core runtime files

- `/_hirmos/core/core-rules.md`
- `/_hirmos/core/command-protocol.md`
- `/_hirmos/core/execution-model.md`

## Key Core-local authority files

- `/_hirmos/core/authority/core/extension-manifest-authority.md`
- `/_hirmos/core/authority/core/hook-execution-control.md`
- `/_hirmos/core/authority/core/entrypoint-execution-contract.md`
- `/_hirmos/core/authority/core/stack-system.md`

## Deeper Core-local authority

- `/_hirmos/core/authority/core/installation-model.md`
- `/_hirmos/core/authority/core/validation-and-ordering.md`
- `/_hirmos/core/authority/core/stack-system.md#stack-package-contract`
- `/_hirmos/core/authority/core/folder-rules.md`
- `/_hirmos/core/authority/core/identity-display-execution-control.md#runtime-identity-declaration`
- `/_hirmos/core/authority/core/identity-display-execution-control.md`
- `/_hirmos/core/authority/core/runtime-trace-rules.md`
- `/_hirmos/core/authority/core/README.md`


## Bootstrap runtime surface

- `/_hirmos/core/bootstrap.md` is the assembled runtime bootstrap path.
- `/_hirmos/core/bootstrap_supporting-notes.md` is the synced maintenance companion for bootstrap decomposition and source mapping.
