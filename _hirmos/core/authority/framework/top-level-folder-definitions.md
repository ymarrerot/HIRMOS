# Top-Level Folder Definitions

## Purpose

Define the authoritative meaning of the top-level framework surfaces directly under `_hirmos/`.

Use this file when you need the canonical definition of what each governed top-level surface means, what it owns, and how extensions are allowed to write into the framework-owned folder model.

## Scope and usage rule

This file is framework-wide authoritative doctrine.

Use it as the authoritative source when:
- deciding what a top-level folder means
- deciding whether an artifact belongs in `inputs`, `artifacts/context`, `artifacts/outputs`, `artifacts/sot`, `artifacts/phases`, `artifacts/prompts`, or `artifacts/ops`
- reviewing whether an extension is using the correct top-level framework folder
- updating user-facing guidance that summarizes these surfaces

Secondary guidance may summarize these meanings, but must not silently redefine them.

## Top-level framework surface definitions

### `_hirmos/core/authority/`

Central home for framework-authoritative doctrine.

This surface hosts four internal authority lanes:
- `shared/`
- `core/`
- `framework/`
- `extensions/`

It is not a user-facing docs lane.

### `_hirmos/core/`

The minimal framework core and its core-owned runtime surfaces, including the centralized authority system under `_hirmos/core/authority/`.

### `_hirmos/extensions/`

Installed extensions.

### `_hirmos/stacks/`

Installed stack packages.

### `_hirmos/integrations/`

HIRMOS-owned integration surfaces for connecting HIRMOS to external tools, environments, and future interoperability adapters.

Current v1 child surface:

```text
_hirmos/integrations/agent-tools/
```

`_hirmos/integrations/agent-tools/` owns agent/IDE/tool bootstrap integration templates, the integration registry, managed-block rules, and contributor guidance consumed by the product-facing `hirmos init` CLI.

This surface is a productization and tool-discovery adapter surface. It is not Core runtime behavior, not extension behavior, and not a replacement for `_hirmos/HIRMOS_CORE.md`.

### `_hirmos/tools/`

HIRMOS-maintained developer tooling that belongs to HIRMOS but is not Core runtime authority and not extension workflow behavior.

Current v1 child surface:

```text
_hirmos/tools/cli/
```

`_hirmos/tools/cli/` owns the TypeScript implementation of the product-facing `hirmos init` CLI.

### `_hirmos/extensions/_templates/`

Central starter and scaffolding templates, including framework starter templates such as extension starters.

### `_hirmos/inputs/`

Raw extension-owned runtime inputs.

### `_hirmos/artifacts/outputs/`

Extension-owned result artifacts and deliverables intended for human consumption, approval, handoff, or external/system consumption.

### `_hirmos/artifacts/context/`

Normalized runtime context artifacts. Extension-owned context belongs under `_hirmos/artifacts/context/<extension-id>/...`; project-level cross-extension context belongs under `_hirmos/artifacts/context/project/`; flat `_hirmos/artifacts/context/` remains reserved for framework-global artifacts.

### `_hirmos/artifacts/sot/`

Authoritative source-of-truth artifacts.

### `_hirmos/artifacts/phases/`

Generated phase contracts.

### `_hirmos/artifacts/prompts/`

This is a flat canonical implementation-execution lane owned by the implementation authority currently in use.

Generated execution prompts.

### `_hirmos/artifacts/ops/`

This is a flat canonical implementation-execution lane owned by the implementation authority currently in use.

Governed operational runtime artifacts produced during the implementation stage of the Software Development Lifecycle.

This folder is intended for execution-oriented extensions such as an installed implementation-focused extension. It includes run evidence, execution reviews, retries, and other downstream-consumable operational records.

### `_hirmos/project.json`

Project-local HIRMOS configuration metadata, including active stack selection and installed agent integration metadata.

This file is configuration metadata. It is not runtime truth, not artifact authority, and not a replacement for `_hirmos/HIRMOS_CORE.md`.

## Ownership and write boundaries

### Framework ownership of top-level surfaces

The top-level folders directly under `_hirmos/` are framework-owned.

Extensions may participate inside governed framework surfaces, but they do not own the top-level surface definitions themselves.

### Extension write lanes inside governed surfaces

Extensions may write inside the governed folders the framework provides, such as:
- `_hirmos/inputs/<extension-id>/...`
- `_hirmos/artifacts/outputs/<extension-id>/...`
- `_hirmos/artifacts/context/<extension-id>/...`
- `_hirmos/artifacts/ops/...`

### New top-level folder creation rule

Extensions should not invent new top-level operational folders like `_hirmos/client/`, `_hirmos/reports/`, or `_hirmos/exports/`.

If a new top-level folder is ever truly needed, it should be introduced as a framework decision, not by one extension acting alone.

## Classification rule for generated artifacts

When deciding where a generated artifact belongs, first classify its role.

A simple rule of thumb:
- raw intake belongs in `inputs`
- normalized working state belongs in `context`
- produced result surfaces belong in `outputs`
- implementation-stage operational runtime records belong in `ops`
- authoritative project or design truth belongs in `sot`
- bounded downstream delivery contracts belong in `phases`
- generated execution instructions belong in `prompts`

## Related doctrine

Related authoritative doctrine:
- `framework/source-of-truth-model.md`
- `framework/framework-operating-model.md`
- `framework/framework-operating-model.md`

Related user-facing guidance may summarize these rules, but this file remains the authoritative source.
