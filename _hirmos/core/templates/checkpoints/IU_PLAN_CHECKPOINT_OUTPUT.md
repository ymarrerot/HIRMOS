# IU_PLAN_CHECKPOINT_OUTPUT.md

Status: governed output template.
Purpose: govern the pause after IU planning/materialization and before IU execution.

This template is not a session artifact. It prevents HIRMOS from collapsing IU planning and IU execution into one continuation.

## Required heading

```text
IU Plan — Review or Change
```

## Required response shape

### IU plan created

- Session authority: `_hirmos/session/SESSION_SCOPE.md`
- IU authority directory: `_hirmos/session/implementation-units/`
- Session ledger: `_hirmos/session/SESSION_LEDGER.md`
- Active generated-artifact validation result: PASS | FAIL | BLOCKED | NOT_RUN

### Implementation units ready for review

List each IU as a compact pointer only:

| IU | One-line objective | Authority file | Status |
|---|---|---|---|
| IU-xx | | `_hirmos/session/implementation-units/IU-xx.md` | SEALED / BLOCKED |

### Boundary statement

Say this explicitly:

```text
IU planning is complete. IU execution has not started. No material project-file edits are authorized until you accept the IU plan.
```

### How to respond

```text
To begin implementation execution:
hirmos continue "Accept IU plan and begin IU execution"

To change the IU plan:
hirmos continue "Change IU-01: <your change>"
hirmos continue "Split IU-02: <reason>"
hirmos continue "Mark IU-03 uncertain: <reason>"

To stop without continuing:
Do not run `hirmos continue`. Reply exactly: Stop / do not continue
```

## Hard rules

- This checkpoint occurs after full IU files exist and before material project-file edits.
- It must not claim implementation started or completed.
- It must not summarize IU contracts in detail; point to each `IU-xx.md` authority file.
- It must show active generated-artifact validation status.
- The next execution command must explicitly mention IU execution authorization.

## Optional artifact creation note

Do not create empty optional artifacts for future work. Name expected future artifact paths only as expected paths until the governed boundary creates them. If an optional artifact is not applicable, say so explicitly.
