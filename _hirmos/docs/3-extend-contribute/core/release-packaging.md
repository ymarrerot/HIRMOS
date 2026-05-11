# Release Packaging

Use this page when you need the practical packaging shape for sharing HIRMOS itself, a workspace, or an extension zip. In SDLC terms, this matters near handoff, distribution, installation, or release moments rather than during everyday workflow authoring.

Need the canonical installation and versioning rules? See [_hirmos/core/authority/core/installation-model.md](../../../core/authority/core/installation-model.md) and the [Versioning contract](../../../core/authority/framework/versioning-contract.md).

Use different zip profiles for different purposes.

## Framework release zip

Use when you want to distribute the framework itself.

Should include:
- framework files
- installed extensions
- installed stack packages
- framework docs
- framework version files (`_hirmos/VERSION`, [_hirmos/CHANGELOG.md](../../../CHANGELOG.md), [_hirmos/UPGRADE_GUIDE.md](../../../UPGRADE_GUIDE.md))

Should exclude avoidable packaging noise such as:
- `.DS_Store`
- `__MACOSX`
- editor temp files

## Review or test zip

Use when you want another reviewer or LLM to inspect a working state.

May include:
- generated runtime artifacts
- current design or implementation outputs
- a bounded project workspace when needed for review

Should still avoid avoidable packaging noise when practical.

## Full workspace zip

Use when the framework plus the host application workspace must travel together for execution or review.

May include:
- framework
- generated artifacts
- application repository
- working project files

Be explicit that this is a full workspace package, not a clean framework release package.

## Typical exclusion patterns
When preparing clean framework or review packages, exclude avoidable noise such as `.DS_Store`, `__MACOSX`, editor temp files, and other platform-specific metadata unless a full workspace package intentionally preserves them.