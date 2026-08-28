# Methodology Overview

HIRMOS is current-state-first software development orchestration for AI-assisted work. Its methodology starts from a simple premise: serious software work needs governed execution.

Governed execution means the work has an accountable trail of context, decisions, scope, evidence, and accepted outcomes. This is not mainly a workaround for unreliable models. It is a permanent discipline for changing software systems safely.

AI-assisted development makes the discipline more important because work moves faster, decisions are compressed, and implementation can span many sessions, tools, files, and model runs. Current model failure modes make the need visible today, but the governance requirement remains even as models improve.

The lifecycle is:

```text
Understand System State → Design → Implementation → Update System State
```

The lifecycle is stable. The work shape changes depending on the request.

## Work-shape routing

| Work shape | Methodology posture | Governance reason |
|---|---|---|
| Small bounded work | keep artifacts light and session-scoped | enough scope, evidence, and close history for one governed session |
| Requirements/design work | satisfy Design without forcing implementation | preserve reviewable decisions before code changes |
| Single-session implementation | accept session scope before implementation | make scope and validation expectations explicit before edits |
| Larger delivery | create durable delivery authority before phase/session work | preserve continuity across sessions and future implementation slices |
| IU implementation | plan implementation units, pause, then execute only after IU plan acceptance | separate implementation planning from execution authority |

## Governance-first method

HIRMOS methodology should explain practices in this order:

1. **Governance requirement** — what serious software work must make accountable.
2. **Practical example** — where the requirement appears in real AI-assisted work.
3. **Consequence** — what fails if the requirement is missing.
4. **HIRMOS mechanism** — which lifecycle boundary, artifact, command, or validation rule carries the responsibility.
5. **Evidence** — how the run proves the responsibility was satisfied.

Current AI-agent reliability issues are useful context, but they should not be the foundation of the methodology. The foundation is durable governance.

## Core ideas

- [Current-State-First Work](current-state-first.md)
- [Artifact Authority](artifact-authority.md)
- [Unresolved Items](unresolved-items.md)
- [Evidence-Backed Review](evidence-backed-review.md)
- [Runtime Integration and Production Readiness](runtime-integration-and-production-readiness.md)
- [Implementation Evidence and Claim Reconciliation](implementation-evidence-and-claim-reconciliation.md)
  - includes governed automated-testing posture, test lifecycle consistency, and anti-weakening review

## Simplification doctrine

HIRMOS should not add artifacts just to appear rigorous. Governance must earn its context cost.

Prefer:

- source authority over duplicate summaries;
- derived pointer indexes over mutable status mirrors;
- compact ledgers over prose-heavy execution reports;
- just-in-time artifact creation over empty future obligations.

The goal is not more process. The goal is the smallest structure that preserves accountable execution.
