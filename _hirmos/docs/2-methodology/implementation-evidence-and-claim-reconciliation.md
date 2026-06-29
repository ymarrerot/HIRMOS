# Implementation Evidence and Claim Reconciliation

HIRMOS treats implementation claims as evidence-backed claims, not just model assertions.

## Evidence levels

Implementation work may produce several kinds of evidence:

- code diff evidence;
- static validation evidence;
- build/test/lint evidence;
- runtime smoke evidence;
- user-observed runtime evidence;
- production-readiness evidence when production readiness is actually in scope.

A claim must match the evidence level. A local MVP can be accepted as local runtime work without claiming production readiness.

## IU evidence

When implementation units are used, each IU should record:

- requested outcome;
- files/artifacts changed;
- checks performed;
- evidence produced;
- unit result;
- review result.

`SESSION_LEDGER.md` should point to IU/evidence records instead of duplicating all evidence detail.

## Claim reconciliation

Before completion or close claims, HIRMOS must reconcile:

- accepted scope;
- implementation results;
- validation output;
- unresolved items;
- production/runtime limitations;
- carry-forward items.

If evidence is missing or contradictory, HIRMOS should report blocked or partial status rather than overclaiming.

## Generated-run validation boundary

Generated HIRMOS artifacts are part of the run. They must satisfy generated-run mechanical gates before HIRMOS claims a clean implementation or close.

## No retrospective compliance

HIRMOS must not implement first and then backfill governance artifacts as if they authorized the work. Retrospective correction may honestly document what happened, but it does not turn an unauthorized action into a clean gate pass.

## IU Planning before IU Execution

When IU mode applies:

```text
Session Baseline accepted → IU Planning only
IU Plan accepted → IU Execution
```

Material project-file edits require IU execution authorization.


## Command and environment evidence wording

A claim should say whether the logged command passed, failed, was not run, or was user environment verified. User environment verified evidence is useful, but it should be labeled separately from commands the agent actually ran.

## PROD-L8.23 Generated-Run Validation Boundary

Generated session archives are part of the evidence record. HIRMOS must validate active and archived generated artifacts before claiming a clean generated-run result.

## PROD-L8.24 Retrospective Compliance Boundary

The active ledger must prove pre-execution authorization. Backfilled artifacts can document a correction honestly, but they cannot convert unauthorized implementation into a clean pre-execution gate pass.

## PROD-L8.31 Generated-Run Mechanical Gates

HIRMOS must report all generated-run gate failures instead of hiding failures behind a generic completion claim.
