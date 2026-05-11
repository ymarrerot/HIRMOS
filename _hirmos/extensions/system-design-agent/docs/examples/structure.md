# Example: system-design-agent structure

This example lives inside `system-design-agent` so Core docs do not assume this extension is installed.

This document shows the structural model used by a serious coherent extension family after the regular-user consolidation.

## Why system-design-agent should remain coherent

System Design work shares:

- terminology;
- artifact flow;
- quality expectations;
- reusable lower-level design units.

That makes it a strong candidate for one coherent extension with a default public entrypoint plus narrower reusable entrypoints.

## Example public entrypoints

- default: `system-design`
- `system-design`
- `system-sot`
- `architecture-sot`
- `phases-sot`
- `phase-sot`
- `phase-design-cycle`
- `staged-delivery-targets`

## Example structure

```text
_hirmos/extensions/system-design-agent/
├── README.md
├── extension.yaml
├── entrypoints/
│   ├── system-design.md
│   ├── system-sot.md
│   ├── architecture-sot.md
│   ├── phases-sot.md
│   ├── phase-sot.md
│   ├── phase-design-cycle.md
│   └── staged-delivery-targets.md
├── specs/
│   ├── system-design.spec.md
│   ├── system-sot.spec.md
│   ├── architecture-sot.spec.md
│   ├── phases-sot.spec.md
│   ├── phase-sot.spec.md
│   ├── phase-design-cycle.spec.md
│   └── staged-delivery-targets.spec.md
├── templates/
└── docs/
```

## Key idea

A coherent extension can expose a friendly default public entrypoint while preserving narrower reusable surfaces for advanced users.

