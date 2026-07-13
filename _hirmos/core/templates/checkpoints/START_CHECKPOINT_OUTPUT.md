# START_CHECKPOINT_OUTPUT.md

Status: governed checkpoint output selector template.
Purpose: select the correct user-facing checkpoint output after `hirmos start`, based on `SESSION_STATE.json.session_focus` and active authority.

This template is not a session artifact. It prevents free-form checkpoint output and routes the pause to the correct governed checkpoint template.

## Checkpoint selection

| `session_focus` | Active authority | Required checkpoint template | Required heading |
|---|---|---|---|
| `minimal_session` | `_hirmos/session/SESSION_SCOPE.md` if bounded output authority is needed | `SESSION_BASELINE_CHECKPOINT_OUTPUT.md` | `Recommended Baseline — Review or Change` or `Session Baseline — Review or Change` |
| `session_baseline` | `_hirmos/session/SESSION_SCOPE.md` | `SESSION_BASELINE_CHECKPOINT_OUTPUT.md` | `Session Baseline — Review or Change` |
| `delivery_baseline` | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | `DELIVERY_BASELINE_CHECKPOINT_OUTPUT.md` | `Delivery Baseline — Review or Change` |
| `phase_session_baseline` | `_hirmos/session/SESSION_SCOPE.md` adopting active delivery/phase | `SESSION_BASELINE_CHECKPOINT_OUTPUT.md` | `Session Baseline — Review or Change` |

## General hard rules

- Do not use one checkpoint format for all focuses.
- Do not treat delivery-level unresolved items as session-level unresolved items.
- During `delivery_baseline`, source unresolved disclosure from `_hirmos/system/delivery/<delivery-id>/unresolved-items.md#Current Checkpoint Feed`.
- During `session_baseline` or `phase_session_baseline`, source unresolved disclosure from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed` when that artifact exists.
- Do not create or reference concrete future `PHASE-xx.md` paths unless those files exist.
- Do not create or reference full implementation-unit artifacts before the relevant baseline has been accepted or amended.
- Recommend exactly one next governed command when the baseline is acceptable: `hirmos continue`.
- When IU mode is expected, label that next step as `IU Planning`, not implementation or IU execution.

## Canonical interaction posture density

Use `_hirmos/core/authority/INTERACTION_POSTURE.md`: simple by default, transparent by design, rigorous underneath, and progressively disclosed. Checkpoint output must stay concise while including artifact paths for governed claims. Increase visible detail only when risk, blocker state, validation failure, route-back, or user request requires it.

## Required continuation semantics

For `delivery_baseline`, the output must say:

```text
If there are no gated delivery decisions requiring user input, `hirmos continue` will treat this delivery baseline as accepted unless you request changes first; it will then activate or amend the delivery, instantiate only the next needed phase/session authority, and pause again for Session Baseline — Review or Change before implementation begins. If gated decisions are listed as pending user input and not reflected in delivery authority, answer them or explicitly adopt the surfaced recommendations before continuing.
```

For `session_baseline`, `phase_session_baseline`, and implementation-capable `minimal_session`, the output must say:

```text
If you run `hirmos continue`, HIRMOS will treat this session baseline as accepted unless you request changes first. If implementation units are required, the next step is IU Planning only: HIRMOS will create or verify the full IU files, run active generated-artifact validation, and pause for IU Plan — Review or Change. It will not edit project files or begin IU execution until you later accept the IU plan. If no IU mode is required, HIRMOS will follow the lightweight implementation path allowed by the accepted baseline.
```

## Compatibility phrase for minimal/session baseline checkpoints

```text
If you run `hirmos continue`, HIRMOS will treat this recommended baseline as accepted unless you request changes first; implementation still cannot begin until the applicable implementation gate is satisfied. It will then follow the focus-specific continuation semantics above.
```

## Compatibility response options for recommended/session baseline

```text
To continue from this pause:
hirmos continue "Accept baseline"
hirmos continue "Change item 1: <your change>"
hirmos continue "Mark item 2 uncertain"
hirmos continue "Ask for technical review summary"

To stop without continuing:
Reply exactly: Stop / do not continue
```

- Do not create or reference full implementation-unit artifacts before the session scope baseline has been accepted or amended. Do not edit project/source files during `hirmos start`; detailed implementation instructions are scope input, not implementation authorization.
- Do not describe the next baseline-acceptance continuation as implementation when IU mode applies; describe it as IU Planning and a pause for IU Plan review.

## Optional artifact creation note

Do not create empty optional artifacts for future work. Name expected future artifact paths only as expected paths until the governed boundary creates them. If an optional artifact is not applicable, say so explicitly.
