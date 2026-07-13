# HIRMOS Validator Regression Fixtures

This directory documents the validator regression fixture runner:

`_hirmos/tools/test_validator_regressions.py`

The runner mutates temporary copies of the framework and verifies that
`validate.py` passes known-good states and fails closed for known-bad states.

## Command-State Regression Fixtures

The suite covers idle scaffold cleanliness, active-session canonical artifacts,
unsupported legacy command detection, and implementation-readiness command
legality.

## Delivery Governance Regression Fixtures

The suite also covers Delivery-Need Classification, durable Delivery Plan and
Phase availability, Current System State delivery pointer concordance, and
Close-Time Delivery / Phase Status Transaction enforcement.

The delivery-governance cases intentionally verify that:

- a delivery-governed active readiness fixture passes when its durable Delivery Plan,
  Phase file, Session Scope, and Current System State pointers agree;
- a missing durable Delivery Plan fails closed;
- an UNCERTAIN Delivery-Need Classification cannot reach implementation readiness;
- a Session Scope / Current System State delivery pointer mismatch fails closed;
- a delivery-governed close without a Close-Time Delivery / Phase Status Transaction fails;
- a delivery-governed close with `DELIVERY_STATUS_UPDATE_APPLIED` passes.

## Retained Fixture Summary

- valid baseline passes validation
- idle session with stale active artifacts fails
- legacy accepted-state index files must not reappear

## Phase Entry Gate Regression Fixtures

The validator regression suite includes Phase Entry Gate cases for delivery-governed sessions:

- phase entry gate valid greenfield passes
- phase missing lifecycle status fails
- phase blocked lifecycle status fails
- phase unknown type fails
- greenfield phase missing MVP boundary fails
- brownfield phase missing preservation baseline fails
- mixed phase missing brownfield controls fails

These fixtures protect the rule that HIRMOS must not default to implementation readiness when a durable multi-session phase is not actually adoptable.

## Phase Progress / Carry-Forward Regression Fixtures

The validator regression suite includes Phase Progress / Carry-Forward cases for delivery-governed close:

- phase partial close missing carry-forward fails
- phase partial close with carry-forward passes

These fixtures protect the rule that HIRMOS must not close a multi-session phase as partial, blocked, or deferred unless durable carry-forward obligations are recorded in the phase progress/carry-forward surfaces.

## Phase Acceptance Regression Fixtures

The regression suite verifies that a delivery-governed phase cannot move to `ACCEPTED` unless the Phase Acceptance Evidence Gate is complete. Required cases include:

- phase accepted missing acceptance evidence fails
- phase accepted with acceptance evidence passes

These fixtures protect the rule that acceptance is a durable Delivery Plan / Phase / Current System State transition, not a narrative claim in chat or archive.

## Phase Lifecycle Validator Regression Fixtures

 formalizes the phase lifecycle regression suite across greenfield, brownfield, and mixed multi-session delivery work. The suite now includes positive and negative cases that verify phase lifecycle enforcement remains current-state-first and does not collapse complex multi-session work into unsafe single-session implementation.

Additional cases include:

- phase entry gate valid brownfield passes
- phase entry gate valid mixed passes
- phase lifecycle status report missing fields fails
- phase lifecycle status report complete passes

These fixtures protect the phase lifecycle stack from regressions in phase type handling, phase status reporting, and exactly-one-next-command visibility.

- legacy capability entrypoint wrapper fails

## Canonical Entrypoint Surface Cleanup

The fixture suite verifies that legacy capability-level `entrypoint.md` redirect wrappers fail validation. Canonical runnable capability entrypoints must live only at `entrypoints/default.md`.

## PROD-L8.12 Phase/Session Baseline Freshness Fixtures

The regression suite also verifies post-delivery-baseline continuation concordance:

- table-only Phase Entry Gate entry criteria evidence fails because scalar `Entry criteria status` is required;
- phase/session baseline with completed `phase-baseline` and `session-scope` routing rows passes;
- phase/session baseline with stale PENDING routing rows fails;
- phase/session baseline with `DELIVERY_PLAN.md` current phase left as `none` fails.

- delivery baseline active wording fails — protects status-aware delivery wording before baseline acceptance.


## PROD-L8.31 Generated-Run Mechanical Gate Fixtures

The regression suite now includes negative generated-run fixtures for the L8.31 mechanical gates:

- incomplete bootstrap answers fail the generated-session start gate;
- planned implementation units with no IU files fail closed;
- thin or placeholder IU files fail closed even when the transcript claims compliance;
- lifecycle completion claims fail without `Active generated-artifact validation result: PASS`;
- lifecycle completion claims fail without a generated-run mechanical gate record;
- `APPROVED_CARRY_FORWARD` fails without an explicit approval/deferral source;
- delivery/current-state pointer divergence is reported as a generated-run gate failure.

These fixtures protect the rule that generated-run compliance must be mechanically evidenced in artifacts, not merely narrated in the transcript.


## PROD-L8.32K Runtime Boundary Fixtures

Focused fixtures prove that IU planning and IU execution remain separate. A generated IU-mode session that creates IU files but records material project-file edits or lifecycle transition claims before `IU_EXECUTION_AUTHORIZED` must fail validation. Packet-first runtime and active gate validator invocation are protected as static/runtime surfaces.


## PROD-L8.32L JIT / Derived Pointer Fixtures

Focused fixtures verify that optional active artifacts are absent-valid until applicable, delivery/phase/archive pointers can be derived from filesystem source artifacts, and implementation-unit file lists are derived only after IU materialization.


## PROD-L8.32S Runtime Command Surface Unification Fixtures

Focused fixtures verify that the obsolete packet wrapper layer has been removed, `_hirmos/core/commands/*.md` is the canonical compact command runtime authority, and active framework files do not route through the obsolete packet wrapper layer.

## PROD-L8.32Z Start Non-Implementation Boundary Fixtures

Focused fixtures verify that the start command cannot edit project/source files before accepted baseline authority. They also verify that baseline acceptance does not weaken IU mode: when implementation units are required, material edits still require IU plan review and `IU_EXECUTION_AUTHORIZED`.

## PROD-L8.33A Continue Command Integration Gate Fixtures

Focused fixtures protect that `hirmos continue` must classify and gate before coding, must stop at IU plan review when IUs are requested or required and no accepted IU plan exists, and must treat `hirmos status` as read-only. Integration templates for all nine supported tools must include direct continue/status command capsules.

