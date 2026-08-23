<!-- HIRMOS-CAPSULE:close:PROD-L8.33C-2 canonical command capsule v1 -->
## hirmos close command capsule

`hirmos close` requires evidence-backed close.

Required behavior:
1. Read accepted scope, session ledger, unresolved items, implementation evidence, and relevant accepted-state pointers.
2. Verify that completion claims match logged evidence.
3. Fail closed when evidence, accepted authority, IU execution authorization, unresolved-item triage, validation, or artifact concordance is missing.
4. Archive/update accepted state only after close criteria are satisfied.
5. Display a Carry-Forward Attention block before claiming close success.
6. Write active carry-forward rows with global `CF-YYYYMMDD-NNN` IDs, source refs, approval/deferral source, and future resolution instruction.
7. For accepted-state maintenance close, verify removed Active rows have matching Resolved rows in `CARRY_FORWARD.md` and no historical archives were mutated.
5. Do not use close to backfill missing governance after ungoverned implementation.

<!-- /HIRMOS-CAPSULE:close:PROD-L8.33C-2 canonical command capsule v1 -->
