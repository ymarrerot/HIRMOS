# Large Extension Structure

Small examples are enough for onboarding, but larger workflow extensions need more structure.

## Recommended layout

```text
_hirmos/extensions/some-large-extension/
├── README.md
├── extension.yaml
├── index.md
├── entrypoints/
│   └── some-public-entrypoint.md
├── specs/
│   ├── some-public-entrypoint.spec.md
│   ├── internal-helper.spec.md
├── docs/
├── templates/
├── artifacts/
├── hooks/
└── internal/
```

## Template note

Template folders often work best when they support the [Beyond Clear Instructions](./beyond-clear-instructions.md), especially once a large extension needs intermediate synthesis records or governed surfaced outputs.


The `templates/` folder shown inside a large extension is for local runtime or artifact-shaping templates owned by that extension. Starter or scaffolding templates for creating new framework objects belong under `_hirmos/extensions/_templates/...`, not under `_hirmos/extensions/`.

## Design guidance

- `index.md` is usually the default public runnable surface
- `entrypoints/` are additional named public runnable surfaces when needed
- `specs/` hold extension-local authoritative method and contracts
- `internal/` holds private implementation support
- not every extension-local spec needs to be public
- hooks are for augmentation, not main orchestration

## Why this matters

This structure provides a path for decomposing larger original-framework capabilities into coherent extensions without forcing them into toy layouts.
