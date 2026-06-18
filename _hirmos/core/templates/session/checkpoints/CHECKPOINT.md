# Governed Checkpoint

Status: active-session checkpoint artifact.
Purpose: provide an artifact-backed basis for user-facing checkpoint output.

Recommended active-session path:

```text
_hirmos/session/checkpoints/CHECKPOINT_<checkpoint-id>.md
```

## Checkpoint Identity

- Checkpoint ID:
- Checkpoint type:
- Created during command:
- Lifecycle boundary:
- Interaction mode:
- Terminal state:
- Next allowed action:

Allowed checkpoint types:

```text
NEEDS_USER_DECISION
IMPLEMENTATION_READINESS
IMPLEMENTATION_COMPLETE
UPDATE_SYSTEM_STATE_READINESS
BLOCKED_FAIL_CLOSED
REQUEST_NOT_GOVERNABLE
STATUS_ONLY
```

## Backing Artifacts

List only artifacts that exist and contain non-placeholder content.

| Artifact | Role in checkpoint | Verified non-placeholder? |
|---|---|---|

## Execution Controls Summary

| Control | Status | Evidence | Notes |
|---|---|---|---|

## Unresolved Items Summary

| Category | Item IDs | Checkpoint effect |
|---|---|---|
| Gated | | |
| Non-gating carried | | |
| Technical review | | |
| Resolved/disposed | | |

## Domain Expert View

Use this section as the source for compact user-facing output in `domain_expert` mode.

### What HIRMOS understood / completed

### What HIRMOS needs from you

### Recommended baseline, if safe

### Important assumptions being carried

### Technical review pointer, if relevant

### What happens next

### How to change, stop, or ask for details

## Technical Supervisor View

Use this section when the interaction mode is `technical_supervisor`.

### Artifacts to inspect

### Assumptions and risks

### Validation / evidence status

### Implementation or update-state implications

## Framework Diagnostics View

Use this section when the interaction mode is `framework_diagnostics`.

### Lifecycle boundary and command state

### Capability routing

### Execution controls

### Route-back or blocker details

## Self-Check Before Surfacing

- [ ] Checkpoint artifact exists when required.
- [ ] `SESSION_EXECUTION.md` Checkpoint Log references this checkpoint.
- [ ] All claims are backed by existing non-placeholder artifacts.
- [ ] Gated unresolved items are surfaced or marked resolved.
- [ ] Non-gating assumptions are carried with scope and revalidation point.
- [ ] User-facing output matches the active interaction mode.
- [ ] Terminal state and next allowed action are clear.


## Runtime Integration Checkpoint Content

Use when production readiness, real runtime integration, or material provider/database/auth decisions are involved.

- Current implementation level:
- HIRMOS primary recommendation:
- Alternatives:
- Why this is recommended:
- Decision owner:
- Technical review path:
- Blockers before production readiness:
- What HIRMOS will do next if accepted:

## Progressive Technical Disclosure

Use when autonomous technical decisions or production-readiness decisions must be surfaced.

### Domain Expert Summary

- Technical decision or recommendation:
- Why HIRMOS recommends it:
- What HIRMOS already handled safely:
- What remains blocked or needs review:
- One primary next action:

### Technical Supervisor Details

- Alternatives considered:
- Evidence:
- Risks:
- Review trigger:
- Production-readiness impact:
