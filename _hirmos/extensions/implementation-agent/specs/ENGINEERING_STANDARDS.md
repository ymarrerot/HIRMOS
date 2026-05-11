# ENGINEERING_STANDARDS

## Purpose

Define reusable implementation-side engineering standards for `implementation-agent`.

This file is the generic implementation engineering standards layer that applies regardless of the selected stack. It complements, but does not replace, stack-specific guidance loaded through `_hirmos/project.json` and the selected stack package.

These standards must be read, followed, and held together with strong stack awareness before prompt implementation work begins.

## Scope

These standards apply to implementation planning when prompt boundaries or verification strategy are being shaped, and they apply directly to prompt execution inside `implementation-agent:implementation-execution-cycle`.

Stack-specific language, framework, package-manager, runtime, and tooling expectations must come from the selected stack package.

## Core principles

- Prefer simple, reviewable implementations over clever abstractions.
- Keep diffs small, auditable, and phase-bounded.
- Favor explicit behavior over hidden behavior.
- Do not introduce silent fallbacks for important business logic.
- Preserve determinism where practical.
- Optimize for maintainability, testability, and safe AI-assisted iteration.
- Do not silently broaden approved implementation scope.

## Strong stack-awareness rule

Before implementation begins, load and apply the active stack package surfaces resolved through `_hirmos/project.json`, including at minimum:

- `STACK_OVERVIEW.md`
- `ENGINEERING_STACK_STANDARDS.md`
- `STACK_COMMANDS.md`
- `EXECUTION_STACK_RULES.md`
- `STACK_ARCHITECTURE_GUIDANCE.md` when it materially affects implementation shape

This generic standards file does not authorize stack-specific assumptions to be invented from memory.

## Application structure

- Keep framework and implementation bootstrapping minimal and easy to inspect.
- Do not write to the local filesystem at runtime unless the selected stack package and the approved project architecture explicitly allow it.
- Prefer implementation shapes that are easy to trace from entry boundary to business logic and back to verification.

## API and server boundaries

- Treat API boundaries as untrusted input boundaries.
- Validate request payloads and externally sourced inputs using the stack- or project-approved validation approach.
- Return consistent error shapes from application-owned APIs when the surface is owned by the project.
- Keep handlers thin; move business logic into testable modules where that boundary exists.
- Avoid hidden side effects inside route handlers, jobs, or boundary adapters.
- Make idempotency expectations explicit for mutation flows when relevant.

## Approved-scope discipline

- Implementation must stay inside the currently approved prompt and phase contract.
- Local corrective retries must remain bounded to the failed execution unit unless governed escalation says otherwise.
- Implementation may replan execution inside approved scope, but it must not redesign upstream approved scope.
- If the approved implementation contract is materially incomplete, contradictory, or no longer locally recoverable, stop and surface the issue truthfully instead of silently compensating.

## Boundary discipline

- Validate unknown external input before use.
- Treat API boundaries, job boundaries, CLI boundaries, and storage boundaries as untrusted input boundaries.
- Keep stack-specific validation libraries and patterns in the selected stack package.

## Architecture and authority discipline

- Do not silently change architecture, contracts, or approved design authority through implementation-side convenience edits.
- If accepted implementation work reveals architecture drift, stale design truth, or missing upstream decisions, flag it explicitly in the governed run outputs.
- Do not treat implementation convenience as approval to rewrite authoritative design artifacts.

## Schema and contract discipline

- No silent schema changes.
- Any change affecting stored data, public APIs, event payloads, or inter-package interfaces must be made explicit in the implementation evidence and review chain.
- Prefer backward-compatible changes when practical.
- When a breaking contract change is necessary, make that explicit and keep verification and follow-up obligations visible in the same execution record.

## Logging and observability

- Use structured logs for server-side execution when logging is introduced.
- Avoid noisy logs that hide important failures.
- Never log secrets, tokens, or sensitive customer data.
- Include stable identifiers that help trace a request or workflow when available.
- Prefer auditable error messages over vague catch-all failures.

## Error handling

- No silent exceptions.
- Do not swallow errors to make flows appear successful.
- Catch errors where meaningful recovery or classification is possible.
- If the system cannot safely proceed, fail clearly and preserve enough context for debugging and review.
- User-facing messages should be safe and concise; internal logs and evidence should preserve useful technical detail.

## Package and module layout

- Organize code so responsibilities are easy to find and reason about.
- Keep public package surfaces explicit where package boundaries exist, using a stable project-appropriate entry surface when one exists.
- Keep internal modules internal unless a stable public surface is needed.
- Prefer composition over deep inheritance.
- Avoid circular dependencies.

## Testing standards

- Add or update tests for meaningful behavior changes.
- Keep tests aligned with actual contracts and expected behavior.
- Prefer focused unit tests for logic-heavy modules.
- Add integration tests when behavior depends on multiple modules or boundaries working together.
- Do not remove meaningful coverage without replacing it appropriately.
- Use repository-local commands when they exist; otherwise use the active stack command surface truthfully.

## Fixtures and coverage integrity

Goal: tests should not pass because fixtures were weakened or coverage was quietly reduced.

Hard rules:

- Do not weaken fixtures only to satisfy current behavior.
- Do not replace realistic fixture data with trivial placeholders solely to avoid failures.
- Do not delete tests or assertions unless the prior behavior is no longer valid and replacement coverage is added in the same change.
- If a behavior change invalidates older tests, update tests to reflect the new contract and preserve the regression-detection intent.

Whenever tests or fixtures change, the execution record must explain:

- which fixtures changed and why realism was preserved or improved
- what coverage changed and where equivalent or updated coverage now exists

## Dependency discipline

- Prefer the smallest dependency that solves the real problem.
- Avoid adding libraries for minor conveniences when the platform already provides a good solution.
- Prefer widely adopted, well-maintained libraries for important boundaries.
- Document non-obvious dependency choices in governed outputs when the tradeoff matters.

## Security and secrets

- Never hardcode secrets.
- Read secrets from environment configuration or the project-approved secret manager.
- Avoid exposing server secrets to the client.
- Treat authentication, authorization, and external system access as explicit boundaries.
- Do not assume internal traffic is automatically trustworthy.

## Performance and scaling

- Start simple and measure before optimizing.
- Do not introduce caches, queues, background workers, or distributed coordination without a clear reason.
- If performance-oriented infrastructure is introduced, make invalidation, retry, and failure behavior explicit.

## AI-assisted implementation expectations

- AI-generated code must be reviewed with the same care as hand-written code.
- Preserve human-readable structure and naming.
- Do not accept generated code that adds architecture or behavior outside approved scope.
- When uncertainty exists, prefer explicit surfaced uncertainty over speculative implementation.

## Exception policy

Any deviation from these standards requires a written exception in the governed execution record before the deviation is treated as acceptable.

Template:
`Exception: <path or module> deviates because <reason>. Scope: <what differs>. Risk: <what could go wrong>. Mitigation: <how maintainability, determinism, and reviewability are preserved>. Approval: <where this was approved>.`
