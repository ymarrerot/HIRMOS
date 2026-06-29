# Methodology Overview

HIRMOS is current-state-first software development orchestration for AI-assisted work.

The lifecycle is:

```text
Understand System State → Design → Implementation → Update System State
```

The lifecycle is stable. The work shape changes depending on the request.

## Work-shape routing

| Work shape | Methodology posture |
|---|---|
| Small bounded work | keep artifacts light and session-scoped |
| Requirements/design work | satisfy Design without forcing implementation |
| Single-session implementation | accept session scope before implementation |
| Larger delivery | create durable delivery authority before phase/session work |
| IU implementation | plan IUs, pause, then execute only after IU plan acceptance |

## Core ideas

- [Current-State-First Work](current-state-first.md)
- [Artifact Authority](artifact-authority.md)
- [Unresolved Items](unresolved-items.md)
- [Evidence-Backed Review](evidence-backed-review.md)
- [Runtime Integration and Production Readiness](runtime-integration-and-production-readiness.md)
- [Implementation Evidence and Claim Reconciliation](implementation-evidence-and-claim-reconciliation.md)

## Simplification doctrine

HIRMOS should not add artifacts just to appear rigorous. Governance must earn its context cost.

Prefer:

- source authority over duplicate summaries;
- derived pointer indexes over mutable status mirrors;
- compact ledgers over prose-heavy execution reports;
- just-in-time artifact creation over empty future obligations.
