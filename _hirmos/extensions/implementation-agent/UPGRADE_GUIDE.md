# implementation-agent Upgrade Guide

## Upgrading to 1.1.0

This release aligns `implementation-agent` with the HIRMOS front-door flow:

```text
Requirements → System Design → Implementation
```

### What changed

- The regular user command is now:
  - `hirmos implementation`.
- The default public entrypoint is now `implementation`.
- The public Implementation flow composes planning and execution while preserving the planning approval pause.
- `implementation-planning-cycle` and `implementation-execution-cycle` remain reusable internal/advanced entrypoints.
- Implementation completion now uses Evidence-backed Review language.

### Required actions

- Update local docs or scripts that assumed `hirmos implementation` only ran implementation planning.
- For the regular workflow, use `hirmos implementation` and approve continuation after planning before phase execution.
- Keep explicit planning/execution cycle commands only where advanced/manual control is intentionally needed.

### Notes

- The public Implementation command must not proceed from planning to execution without explicit approval.

## Upgrading to 1.0.1

### Required actions
- Review any local conventions that assumed `implementation-execution-cycle` could surface completion before phase review.
- Use the new execution templates under `templates/implementation-execution-cycle/` when extending or reviewing terminal output behavior.

### Notes
- Phase review is now a built-in stage of `implementation-execution-cycle` for non-paused completion states.
- Final surfaced output now distinguishes completed, paused, and failed results through required templates and self-validation, with remaining-gap disclosure inside completed output and a governed failed template.

- implementation-planning-cycle now uses entrypoint-specific completed and paused terminal templates with strict final self-validation.

## Upgrading to 1.0.0

Initial stable version baseline for `implementation-agent`.

### Required actions
- None for a fresh install.

### Notes
- `implementation-agent` now declares its own `version` in `extension.yaml`.
- `implementation-agent` now declares framework compatibility through `requires_core` in `extension.yaml`.
