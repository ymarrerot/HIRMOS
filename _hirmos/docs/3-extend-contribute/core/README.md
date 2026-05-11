# Core Guidance

Use this lane when you want a practical explanation of how the Core behaves without reading Core-local authority first. The Core is the minimal orchestration layer of HIRMOS, so these docs are most useful when you need to understand commands, loading, manifests, hooks, and stack mechanics. Most users should arrive here only after getting started or after a real usage question appears.

## Start here

- [Command protocol](command-protocol.md) — the command surface most users actually touch
- [Loading and resolution](loading-and-resolution.md) — how extension surfaces are found and resolved
- [Stacks](stacks.md) — how the active stack affects framework behavior

## Go deeper

- [Architecture](architecture.md) — what the Core owns and what it must not own
- [Extension manifest](extension-manifest.md) — how extensions declare public surfaces
- [Hook System v1](hook-system-v1.md) — how bounded extension composition works
- [Public vs private](public-vs-private.md) — how Core and extension surfaces should be exposed
- [Release packaging](release-packaging.md) — packaging expectations before sharing framework zips

## When this lane is most useful

Use this lane when you already know what you want to do and now need the framework mechanics that support that work safely.

## Need the canonical Core-local rules?

Use this lane for user-facing guidance. When you need the exact Core-local rule, go to the [Core authority](../../../core/authority/core/) for the canonical rule.

## Go next

- **Return to the broader docs hub:** go to the [Documentation hub](../../README.md).
- **Go back to practical framework guidance:** go to [Framework guidance](../framework/README.md).
