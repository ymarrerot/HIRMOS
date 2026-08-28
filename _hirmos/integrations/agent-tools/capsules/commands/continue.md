<!-- HIRMOS-CAPSULE:continue:PROD-L8.33C-2 canonical command capsule v1 -->
## hirmos continue command capsule

`hirmos continue` must classify and gate before it codes.

Before any product/source edit or implementation claim, the agent must:
1. Read `_hirmos/session/SESSION_STATE.json`, `_hirmos/session/SESSION_SCOPE.md`, and `_hirmos/session/SESSION_LEDGER.md` when present.
2. Classify the continue request as acceptance, amendment, IU planning, IU execution authorization, correction, validation, route-back, close preparation, or blocked.
3. Append the continuation pass record to `SESSION_LEDGER.md` before acting.
4. If the request changes accepted authority, append the corresponding authority delta to `SESSION_SCOPE.md` before implementation continues.
5. Evaluate whether implementation units are required or requested.

IU planning rules:
- If the user requests implementation units and no accepted IU plan exists, create or revise the IU plan and stop at `IU Plan — Review or Change`.
- If the user does not request implementation units, still evaluate whether IUs are required by scope, risk, multi-file impact, validation complexity, or governance value.
- If IUs are required, baseline acceptance authorizes IU Planning only. It does not authorize product/source edits.
- Product/source edits in IU mode require a later explicit continuation that records `IU_EXECUTION_AUTHORIZED` after IU plan review.
- Never create IU files after material implementation to show compliance.

If implementation units are not required, record a concise no-IU rationale in the existing session governance artifacts before implementation begins.

Governed automated testing and test integrity:
- Before software implementation, use the accepted Session Scope / sealed IU testing posture; reuse repository-native test tooling.
- Material isolated deterministic behavior normally requires meaningful unit tests when practical; use stronger component/integration/runtime evidence where appropriate.
- Do not weaken, skip, delete, trivialize, over-mock, or loosen still-valid behavioral tests merely to obtain PASS.
- When behavior changes or disappears, update/remove obsolete tests and trace the test delta to the changed authority; clean stale/orphan tests in the same governed scope when practical.
- For reproducible defects, add a focused regression test when practical; HIRMOS has no universal numeric coverage threshold.

Implementation completion convergence:
- IU execution authorization is not a mandatory stop after edits finish.
- After all authorized implementation work/IUs execute, continue through applicable validation, IU review, unresolved-item review, and session implementation review in the same pass when inputs are available.
- If aggregate review supports completion, move to `implementation_complete` and recommend `hirmos close`.
- Pause only when review needs user-owned evidence/decision or hits a blocker/correction; then recommend one purpose-specific `hirmos continue "..."` invocation.
- If a bare `hirmos continue` arrives with all authorized work already executed and session review still pending, infer close-preparation / implementation-completion review from current state.

<!-- /HIRMOS-CAPSULE:continue:PROD-L8.33C-2 canonical command capsule v1 -->

Accepted-state maintenance rules:
- For `ACCEPTED_STATE_MAINTENANCE` / `CARRY_FORWARD_RESOLUTION`, enforce accepted-state-only writes.
- Move a carry-forward item from Active to Resolved only with matching global `CF-YYYYMMDD-NNN` ID, source ref, resolution basis, evidence posture, and authority/evidence pointer.
- Do not mutate historical archives or product/source files.
