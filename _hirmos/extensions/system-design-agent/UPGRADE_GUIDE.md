# system-design-agent Upgrade Guide

## Upgrading to 1.1.0

This release aligns `system-design-agent` with the HIRMOS front-door flow:

```text
Requirements → System Design → Implementation
```

### What changed

- The regular user command is now:
  - `hirmos system-design`.
- The default public entrypoint is now `system-design`.
- `system-design-agent` now consumes Requirements outputs produced by `requirements-agent`.
- `system-design-cycle` is retained as a narrowed reusable system-level design subcycle.
- `phase-design-cycle` is required for normal greenfield System Design completion after gated unresolved items are resolved.
- Unresolved-item contribution now targets the project-level canonical inventory:
  - `_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md`.

### Required actions

- Run `hirmos requirements` before `hirmos system-design` in the regular greenfield workflow.
- Update custom docs or local workflows that treated `system-design-agent:system-design-cycle` as the regular user-facing System Design command.
- Update custom integrations that expected `system-design-agent` to produce Requirements artifacts directly.
- Update custom unresolved-item references from system-design-local inventory paths to the project-level inventory path.

### Notes

- Power users may still use retained internal/advanced entrypoints when appropriate, but the regular public System Design command is the default extension command.
- `system-design-agent` should not re-own Requirements production in greenfield HIRMOS workflows.

## Upgrading to 1.0.0

Initial stable version baseline for `system-design-agent`.

### Required actions
- None for a fresh install.

### Notes
- `system-design-agent` now declares its own `version` in `extension.yaml`.
- `system-design-agent` now declares framework compatibility through `requires_core` in `extension.yaml`.
