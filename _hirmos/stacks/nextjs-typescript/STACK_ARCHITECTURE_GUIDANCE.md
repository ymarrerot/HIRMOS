# Next.js TypeScript Stack Architecture Guidance

Status: stack guidance.
Purpose: guide production-shaped architecture choices for Next.js TypeScript applications.

Stack guidance is not repository authority. Repository evidence and accepted HIRMOS system state govern actual commands, structure, and constraints.

## Recommended architecture posture

Prefer the simplest architecture that preserves production shape. Do not choose a shortcut merely because it is faster if it changes the architecture class of the solution.

For a Next.js application that performs long-running provider, AI, import/export, media, batch, or other delayed work, the preferred production-shaped flow is:

```text
user action → server action/API route → persisted job/state record → worker/cron/queue processor → persisted result → polling/status UI
```

Avoid:

```text
user action → awaited long-running provider/batch work → delayed request response
```

unless explicitly authorized as a prototype/demo limitation.

## Persistence

When production is expected to use PostgreSQL, local development should normally use PostgreSQL too. SQLite is acceptable for explicitly scoped demos, tests, or very small local-only tools, but it should not be presented as production-shaped for an app expected to deploy on PostgreSQL.

## Background jobs

A production-shaped bounded slice may use a lightweight worker or cron route instead of a full queue platform, but it should still have:

- durable job records;
- status transitions;
- retry/error state;
- claim/lock or idempotency behavior when repeated processing is possible;
- UI status/polling where user-visible work is delayed.

## Service boundaries

Use focused server-side modules for:

- database access;
- provider calls;
- file/storage operations;
- usage/quota/accounting;
- job processing.

This keeps implementation replaceable and evidence easier to inspect.

## Close-review architecture questions

Before accepting a Next.js implementation, HIRMOS should be able to answer:

1. Does local infrastructure mirror intended production infrastructure where practical?
2. Are long-running operations outside synchronous request paths?
3. Are metered-state/billing mutations safe under concurrency or explicitly limited?
4. Are provider boundaries and environment requirements clear?
5. Are secrets/runtime artifacts excluded from handoff/release outputs?
6. Is there evidence for the critical user flow, not only a build passing?
