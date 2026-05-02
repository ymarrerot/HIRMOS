# Docs Authoring Contract

## Purpose

Define the authoring contract for user-facing docs under `/_hirmos/docs/`.

This contract exists to keep HIRMOS docs useful for onboarding and practical use instead of drifting into thin reference wrappers for authority files.

## Scope

This contract applies to user-facing docs under:
- `/_hirmos/docs/`
- `/_hirmos/docs/framework/`
- `/_hirmos/docs/core/`
- `/_hirmos/docs/extensions/`
- `/_hirmos/docs/orchestrator/`
- `/_hirmos/docs/examples/`

It complements folder rules and document-role rules. It does not replace them.

## Core rule

User-facing docs must provide standalone practical value.

A doc under `/_hirmos/docs/` may reference authoritative doctrine, but it must still help a reader understand what to do, how to think about the topic, or where to go next without requiring an immediate jump into authority files.

## What docs should do

Docs should:
- orient humans quickly
- teach with low-to-high cognitive load when possible
- provide a practical mental model before deeper detail
- route readers by task, depth, or next step
- summarize only the minimum rule detail needed for safe use
- point to authoritative sources when canonical precision is needed

## What docs must not become

Docs under `/_hirmos/docs/` must not become:
- thin wrappers that mostly say “see the authority file”
- duplicate doctrine homes
- silent alternate versions of authoritative rules
- passive topic containers with no clear user job
- structure-heavy walkthroughs that front-load folder law before practical use

## Doctrine leakage test

When a user-facing doc contains doctrinal material, apply this test:

1. Is this inline doctrine really necessary for the reader to use or understand the topic safely?
2. If no, replace it with a short user-facing explanation and a reference to the authoritative source.
3. If yes, keep only the minimum needed and avoid copying broader doctrinal structure into the doc.

## Layer-aware behavior

Docs may live in conceptual lanes, but they should still behave like guided user lanes.

That means:
- `getting-started/` should optimize for first successful use
- framework, core, extension, and orchestrator docs should still route by depth and next step
- lane README files should help readers start, go next, and go deeper without assuming they want the full doctrine first

## Selective SDLC anchoring

Use SDLC anchoring when it gives readers a clearer practical frame for where HIRMOS fits into familiar software work.

Use it selectively.

Do not add SDLC language to every doc by default. Prefer it where it helps readers place workflow stages, handoffs, or extension purpose more naturally.

## Authoritative references

When a user-facing doc needs to point to authoritative doctrine:
- keep the practical explanation first
- place the deeper canonical reference second
- prefer one clear reference over many scattered doctrine links

## Related doctrine

- [Cross-folder rules](../shared/cross-folder-rules.md)
- [Framework document roles](./framework-document-roles.md)
- [Document design principles](../shared/document-design-principles.md)
