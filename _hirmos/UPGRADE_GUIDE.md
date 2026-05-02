# HIRMOS Upgrade Guide

This file is the concrete upgrade guidance surface for the framework.

For the authoritative framework-wide versioning doctrine, see:
- [Versioning contract](./core/authority/framework/versioning-contract.md)

## Upgrading to 1.1.0

This release promotes the new assembled bootstrap as the primary runtime bootstrap path, simplifies the supporting Core authority graph, and renames the "Clear Instructions Are Not Enough" pattern surfaces to **Beyond Clear Instructions**.

### What changed

#### Bootstrap and Core runtime
- `/_hirmos/core/bootstrap.md` is now the assembled runtime bootstrap path.
- `/_hirmos/core/bootstrap_supporting-notes.md` now carries synchronized maintenance notes for the assembled bootstrap.
- `/_hirmos/core/templates/BOOTSTRAP_REPORT_TEMPLATE.md` now defines the canonical bootstrap completion report shape.
- `/_hirmos/artifacts/context/core/bootstrap-report.md` is the canonical bootstrap report artifact path.
- `/_hirmos/core/authority/core/identity-display-execution-control.md` replaced the older fragmented terminal-output / runtime-identity / run-result doctrine surfaces.
- `/_hirmos/core/authority/core/hook-execution-control.md` is now the live Core authority surface for hook-aware execution.
- `/_hirmos/core/templates/IDENTITY_DISPLAY_EXECUTION_CONTROL_TEMPLATE.md` replaces `terminal-output-wrapper.md`.
- `/_hirmos/core/templates/HOOK_EXECUTION_CONTROL_TEMPLATE.md` replaces `HOOK_EXECUTION_MAP_TEMPLATE.md`.

#### Authority simplification
Removed and replaced:
- `framework/governance-model.md` -> `framework/framework-operating-model.md`
- `framework/framework-readme-role.md` -> `framework/framework-document-roles.md#framework-readme-role`
- `extensions/extension-readme-role.md` -> `extensions/extension-document-roles.md#extension-readme-role`
- `core/run-result-contract.md` -> `core/identity-display-execution-control.md#terminal-run-states`
- `core/runtime-identity-contract.md` -> `core/identity-display-execution-control.md#runtime-identity-declaration`
- `core/stack-package-authority.md` -> `core/stack-system.md#stack-package-contract`

#### Beyond Clear Instructions rename
- `/_hirmos/core/authority/extensions/clear-instructions-are-not-enough.md` -> `/_hirmos/core/authority/extensions/beyond-clear-instructions.md`
- `/_hirmos/docs/extensions/clear-instructions-are-not-enough.md` -> `/_hirmos/docs/extensions/beyond-clear-instructions.md`

### Required actions
- Update live references in local notes, custom docs, and extension materials that still point to the removed files listed above.
- Update any bootstrap-related guidance to use the assembled bootstrap path and the bootstrap report artifact path.
- Update any references to the old "Clear Instructions Are Not Enough" file surfaces so they point to **Beyond Clear Instructions**.

### Notes
- Historical generated outputs may still mention older names or older file paths. Those are historical artifacts unless a live framework file points to them.
- The assembled bootstrap remains the primary runtime reading path. The supporting decomposition exists underneath it for maintenance, not as the primary bootstrap path.

## Upgrading to 1.0.0

This is the initial stable versioning baseline for HIRMOS.

### What was added
- `_hirmos/VERSION`
- [_hirmos/CHANGELOG.md](./CHANGELOG.md)
- [_hirmos/UPGRADE_GUIDE.md](./UPGRADE_GUIDE.md)
- `version` in every installed extension manifest
- `requires_core` in every installed extension manifest
- extension-level `CHANGELOG.md`
- extension-level `UPGRADE_GUIDE.md`

### Required actions
- None for a fresh install.

### Notes
- Compatibility is currently declared only through `requires_core` in each extension manifest.
- Extension manifests no longer use `spec_version` in the public Hirmos contract.
