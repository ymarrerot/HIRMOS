# 2 — Methodology

HIRMOS methodology is **Current-State-First Orchestrated Development**.

HIRMOS starts from the current system state, turns requests and source material into governed Design authority, realizes accepted Design through Implementation with evidence, and updates durable System State so future sessions do not lose context.

This methodology keeps the rigor of spec-driven development, but does not require perfect upfront specs. A project may be greenfield, brownfield, or somewhere in between; HIRMOS starts by understanding the current system state, then activates the capabilities needed for the session.

## The lifecycle

```text
User Request
↓
Understand System State
→ Design
→ Implementation
→ Update System State
```

The lifecycle is ordered, but not waterfall. If new evidence exposes missing facts, invalid assumptions, unresolved decisions, or implementation gaps, HIRMOS routes the work back to the owning stage instead of silently rewriting authority.

## The core distinction

```text
User Request focuses the work.
Understand System State grounds the work in current project truth.
Design governs what should happen and what is allowed next.
Implementation realizes accepted Design with evidence.
Update System State preserves accepted outcomes as durable system state.
```

## What “current-state-first” means

HIRMOS does not assume that the latest prompt, uploaded file, prototype, ticket, or old document is already the truth.

It first asks: what is true about the system now?

Then it uses the request to focus inspection, design, implementation, validation, and state update.

## What the methodology protects

HIRMOS is designed to prevent common AI-assisted software failure modes:

- implementing against stale assumptions;
- treating raw requirements as accepted authority too early;
- losing decisions across long conversations;
- hiding unresolved questions inside implementation;
- claiming completion without evidence;
- closing a session without updating durable current state;
- starting the next session without knowing what changed.

## Minimum methodology pages

Start with these pages:

- [Current-State-First Work](current-state-first.md)
- [Unresolved Items](unresolved-items.md)

## Deeper methodology references

These pages provide more detail after the first onboarding pass:

- [Artifact Authority](artifact-authority.md)
- [Evidence-Backed Review](evidence-backed-review.md)
- [Durable Current System State](durable-current-system-state.md)
- [Runtime Integration and Production Readiness](runtime-integration-and-production-readiness.md)
- [Autonomous Technical Progress](autonomous-technical-progress.md)
- [Vertical Slice and Status UX](vertical-slice-and-status-ux.md)
- [Close, Archive, and Accepted State](close-archive-and-accepted-state.md)
- [Implementation Evidence and Claim Reconciliation](implementation-evidence-and-claim-reconciliation.md)
- [Requirements and Coverage Mapping](requirements-and-coverage.md)
- [Local Technical Setup and Role Workflow Smoke Checks](local-technical-setup-and-role-workflow-smoke-checks.md)


Scope authority is consolidated by default: `SESSION_SCOPE.md` governs the active session, while durable multi-session work uses `DELIVERY_SCOPE.md` under the delivery roadmap/register.
