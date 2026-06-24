# request-intake

## Execution Contract

### Purpose

Capture the User Request and raw source inputs as source material, not governed authority.

### Produces

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/SESSION_EXECUTION.md` updates
- `_hirmos/session/unresolved-items.md` updates when the request is materially ambiguous

### Terminal States

- COMPLETED — request captured with signals, source references, non-authority notice, and handoff questions.
- NEEDS_USER_DECISION — the request is too ambiguous to begin focused system understanding.
- BLOCKED — the request cannot be captured because required source inputs are missing or unreadable.
- NOT_APPLICABLE — command is read-only or does not initiate governed software work.

## Activation triggers

- `hirmos start` includes a User Request.
- A request already exists in conversation context, command context, or uploaded inputs.
- Existing active session state indicates request intake was incomplete or must be refreshed.

## Required inputs

- Command argument, conversation instruction, uploaded inputs, or existing session context.
- No prior active-session artifact is always required beyond bootstrap and command controls.

## Execution controls contributed

- request-intake control
- source-input control when source inputs are mentioned
- unresolved-item control when request ambiguity affects safe continuation

## Method

1. Record the exact User Request if available. If the request must be summarized, preserve the original wording separately when possible.
2. Identify request source: command argument, conversation instruction, uploaded file, existing project artifact, or other context.
3. Inventory source inputs mentioned or available to the run.
4. Extract request signals that should guide focused system-state understanding.
5. Classify each signal as observed from the request, inferred from the request, assumed, or unknown.
6. Record the Initial Non-Authority Notice: User Request and source inputs guide focus but do not become governed requirements, Design authority, or Implementation authorization.
7. Create Handoff to Understand System State questions, separating general system questions from request-focused system questions.
8. Contribute unresolved items when the request cannot safely be interpreted or when source priority is unclear.
9. Record completion, blocker, or not-applicable status in `_hirmos/session/SESSION_EXECUTION.md`.

## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in `unresolved-items.md`, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

## Project Context and Stack Classification

When this capability encounters project-type or stack evidence, record material findings in `DESIGN.md` / `SESSION_SCOPE.md`, `stack-resolution.json` for machine-readable stack routing, or `SESSION_EXECUTION.md` as required by active controls.

User Request labels and prototype technology signals are focus evidence, not final classification authority.
