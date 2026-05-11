# requirements-agent Upgrade Guide

## Upgrading to 1.0.0

Initial stable version baseline for `requirements-agent`.

### What changed

- HIRMOS now has a dedicated official Requirements extension for the front-door flow:
  - `Requirements → System Design → Implementation`.
- The Requirements step is backed by:
  - `hirmos requirements`.
- `requirements-agent` owns Requirements production for greenfield HIRMOS workflows.
- `REQUIREMENTS_SOT.md` remains the canonical requirements SOT artifact.
- Requirements-related unresolved items contribute to the project-level canonical unresolved-item inventory.

### Required actions

For fresh installs:
- None.

For workspaces that previously relied on `system-design-agent` to produce Requirements artifacts:
- Run `hirmos requirements` before `hirmos system-design` for the regular greenfield front-door flow.
- Move or reference Requirements inputs under `_hirmos/inputs/requirements-agent/requirements/` when using local runtime input files.
- Continue using `REQUIREMENTS_SOT.md` as the canonical requirements artifact.

### Notes

- Runtime input folders are project runtime surfaces and are not included inside the marketplace extension package.
- `requirements-agent` accepts Requirements input from prompt/session context, optional command argument tail, online attachments, bounded local file references, and hook-derived artifacts.
- The extension does not automatically ingest the full repository by default. Provide bounded files/context or allow the run to pause for scope.
