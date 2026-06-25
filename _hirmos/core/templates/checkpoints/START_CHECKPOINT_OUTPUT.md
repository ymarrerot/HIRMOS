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

## Required continuation semantics

For `delivery_baseline`, the output must say:

```text
If there are no gated delivery decisions requiring user input, `hirmos continue` will treat this delivery baseline as accepted unless you request changes first; it will then activate or amend the delivery, instantiate only the next needed phase/session authority, and pause again for Session Baseline — Review or Change before implementation begins. If gated decisions are listed as pending user input and not reflected in delivery authority, answer them or explicitly adopt the surfaced recommendations before continuing.
```

For `session_baseline`, `phase_session_baseline`, and implementation-capable `minimal_session`, the output must say:

```text
If you run `hirmos continue`, HIRMOS will treat this session baseline as accepted unless you request changes first. It will then instantiate implementation-unit artifacts if needed and begin governed implementation.
```

## Compatibility phrase for minimal/session baseline checkpoints

```text
If you run `hirmos continue`, HIRMOS will treat this recommended baseline as accepted unless you request changes first. It will then follow the focus-specific continuation semantics above.
```

## Compatibility response options for recommended/session baseline

```text
Accept baseline
Change 1: ...
Mark item 2 uncertain
Ask for technical review summary
Stop / do not continue
```

- Do not create or reference full implementation-unit artifacts before the session scope baseline has been accepted or amended.
