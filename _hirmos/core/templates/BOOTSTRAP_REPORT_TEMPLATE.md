# BOOTSTRAP REPORT TEMPLATE

Artifact path: `_hirmos/artifacts/context/core/bootstrap-report.md`

## Quiz-only gate purpose

This report records the result of the embedded open-book, section-targeted, grounded quiz gate in `_hirmos/core/bootstrap.md` that must pass before bootstrap may grant readiness.

Locked rule:

> At the slightest uncertainty, do not answer from memory. You must re-read the relevant section before answering.

## Required report fields

- `BOOTSTRAP_STATUS`
- `QUIZ_GATE_MODE`
- `QUIZ_GATE_STATUS`
- `QUIZ_GATE_READY_FOR_BOOTSTRAP`
- `QUIZ_GATE_FAIL_CLOSED_REASON`
- `CORE_BOUNDARY_CONFIRMED`
- `COMMAND_SURFACE_CONFIRMED`
- `OUTER_EXECUTION_LIFECYCLE_CONFIRMED`
- `RUN_EXECUTION_CONTROLS_ARTIFACT_CONFIRMED`
- `IDENTITY_DISPLAY_EXECUTION_CONTROL_CONFIRMED`
- `RUNNABLE_EXTENSION_EXECUTION_CONTROL_CONFIRMED`
- `HOOK_EXECUTION_CONTROL_CONFIRMED`
- `STACK_RESOLUTION_CONFIRMED`
- `CUMULATIVE_WORKING_COPY_DISCIPLINE_CONFIRMED`
- `REREAD_UNDER_UNCERTAINTY_RULE_CONFIRMED`
- `FAIL_CLOSED_TRIGGERED`
- `NEXT_ALLOWED_STATE`

## Completion rules

- `QUIZ_GATE_MODE` must be `quiz-only`.
- `BOOTSTRAP_STATUS` = `COMPLETE` only if the quiz gate passes and every required confirmation is satisfied; otherwise `FAIL_CLOSED`.
- `QUIZ_GATE_STATUS` = `PASS` only if the quiz demonstrates grounded, materially accurate understanding of the framework sections required for safe bootstrap completion; otherwise `FAIL`.
- `QUIZ_GATE_READY_FOR_BOOTSTRAP` = `YES` only if `QUIZ_GATE_STATUS` = `PASS`.
- `QUIZ_GATE_FAIL_CLOSED_REASON` must explain the material misunderstanding, ungrounded answer pattern, or reread-discipline failure when the quiz gate fails.
- `CORE_BOUNDARY_CONFIRMED` = `YES` only if Core-owned and extension-owned responsibilities were read and accepted without conflict.
- `COMMAND_SURFACE_CONFIRMED` = `YES` only if the allowed command surface was read and understood before command interpretation.
- `OUTER_EXECUTION_LIFECYCLE_CONFIRMED` = `YES` only if the run execution lifecycle and fail-closed model were read and understood.
- `RUN_EXECUTION_CONTROLS_ARTIFACT_CONFIRMED` = `YES` only if `RUN_EXECUTION_CONTROLS.md` was created or refreshed, initialized, and treated as mandatory.
- `IDENTITY_DISPLAY_EXECUTION_CONTROL_CONFIRMED` = `YES` only if the identity display execution control and required wrapper rules were read and understood.
- `RUNNABLE_EXTENSION_EXECUTION_CONTROL_CONFIRMED` = `YES` only if runnable extension execution resolution and extension-defined mandatory run artifacts were understood.
- `HOOK_EXECUTION_CONTROL_CONFIRMED` = `YES` only if hook-aware execution, hook truth, and `HOOK_EXECUTION_CONTROL.md` requirements were read and understood.
- `STACK_RESOLUTION_CONFIRMED` = `YES` only if active stack resolution rules were read and understood.
- `CUMULATIVE_WORKING_COPY_DISCIPLINE_CONFIRMED` = `YES` only if active cumulative working-copy discipline, intended-vs-completed distinction, and fail-closed continuity handling were read and understood.
- `REREAD_UNDER_UNCERTAINTY_RULE_CONFIRMED` = `YES` only if the runtime accepted and followed the locked reread rule during the quiz gate.
- `FAIL_CLOSED_TRIGGERED` = `YES` if any required verification item is incomplete, untrue, or missing, or if the quiz gate fails.
- `NEXT_ALLOWED_STATE` must state either `Wait for Orchestrator command.` or `Bootstrap failed closed. Do not begin substantive command execution.`

## Quiz gate operational rules

- This is an open-book, section-targeted, grounded gate.
- At the slightest uncertainty, do not answer from memory. You must re-read the relevant section before answering.
- Answers must be grounded in the actual framework files for this run.
- Generic best-practice answers are insufficient if they do not reflect the framework’s actual rules and distinctions.
- Repeated ungrounded answers, repeated reread-discipline failures, or any material misunderstanding of a critical governance area must fail the quiz gate.

## Quiz Gate Results

For each question, record:
- `Question ID`
- `Section target`
- `Answer summary`
- `Groundedness status: grounded | partially grounded | ungrounded`
- `Correctness status: correct | partially correct | incorrect`
- `Reread needed: yes | no`
- `Reread actually performed: yes | no | unknown`
- `Scoring notes`

## Quiz Gate Interpretation

Record:
- `Strengths`
- `Failure points`
- `Material misunderstandings`
- `Allowed to continue bootstrap: yes | no`

## Canonical report shape

```text
BOOTSTRAP_STATUS: <COMPLETE | FAIL_CLOSED>
QUIZ_GATE_MODE: quiz-only
QUIZ_GATE_STATUS: <PASS | FAIL>
QUIZ_GATE_READY_FOR_BOOTSTRAP: <YES | NO>
QUIZ_GATE_FAIL_CLOSED_REASON: <text | none>
CORE_BOUNDARY_CONFIRMED: <YES | NO>
COMMAND_SURFACE_CONFIRMED: <YES | NO>
OUTER_EXECUTION_LIFECYCLE_CONFIRMED: <YES | NO>
RUN_EXECUTION_CONTROLS_ARTIFACT_CONFIRMED: <YES | NO>
IDENTITY_DISPLAY_EXECUTION_CONTROL_CONFIRMED: <YES | NO>
RUNNABLE_EXTENSION_EXECUTION_CONTROL_CONFIRMED: <YES | NO>
HOOK_EXECUTION_CONTROL_CONFIRMED: <YES | NO>
STACK_RESOLUTION_CONFIRMED: <YES | NO>
CUMULATIVE_WORKING_COPY_DISCIPLINE_CONFIRMED: <YES | NO>
REREAD_UNDER_UNCERTAINTY_RULE_CONFIRMED: <YES | NO>
FAIL_CLOSED_TRIGGERED: <YES | NO>
NEXT_ALLOWED_STATE: <state>
```
