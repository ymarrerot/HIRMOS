# Hooks Authoring

Use this page to think about hooks as an extension author: when to expose them, how to name them, and how to keep composition clear without smearing behavior across extensions.

Need the deeper doctrine and Core-local mechanics? See:
- [Extension hooks](../../core/authority/extensions/hooks.md)
- [Extension manifests](../../core/authority/extensions/manifests.md)
- [Hook execution control](../../core/authority/core/hook-execution-control.md)
- [Extension manifest authority](../../core/authority/core/extension-manifest-authority.md)

## Hook System v1 in one view

- owning extensions publish hook points with `exposes_hooks`
- subscriber extensions attach with `hooks`
- v1 supports Action Hooks only
- the Core applies WordPress-style priorities
- hook execution should stay visible in traces and reporting

## When to expose a hook

Expose a hook when another extension may reasonably need to:
- inspect inputs before a step runs
- add optional preprocessing
- generate derived supporting artifacts
- enrich runtime context
- add validation or reporting

## When to subscribe to a hook

Subscribe when your extension adds bounded behavior at a declared seam and does not need to replace the owning workflow.

If your behavior would effectively replace the owning extension, make a new runnable extension instead.

## Choose real seams

Good seams are places where a human can clearly explain:
- what is about to happen
- why optional extension behavior may help here
- what the subscriber is allowed to contribute

## Keep hook behavior visible

If your hook matters, traces and reporting should make that visible.

Aim for clear enrichment, not mysterious magic.
