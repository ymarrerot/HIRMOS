# request-intake

## Execution Contract

### Purpose

Capture the User Request and raw source inputs as source material, not governed authority.

### Produces

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/SESSION_LEDGER.md` updates
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
9. Record completion, blocker, or not-applicable status in `_hirmos/session/SESSION_LEDGER.md`.

## Required behavior

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

## Project Context and Stack Classification

When this capability encounters project-type or stack evidence, record material findings in `DESIGN.md` / `SESSION_SCOPE.md`, `stack-resolution.json` for machine-readable stack routing, or `SESSION_LEDGER.md` as required by active controls.

User Request labels and prototype technology signals are focus evidence, not final classification authority.
