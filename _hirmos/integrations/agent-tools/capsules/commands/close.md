<!-- HIRMOS-CAPSULE:close:PROD-L8.33C-2 canonical command capsule v1 -->
## hirmos close command capsule

`hirmos close` requires evidence-backed close.

Required behavior:
1. Read accepted scope, session ledger, unresolved items, implementation evidence, and relevant accepted-state pointers.
2. Verify that completion claims match logged evidence.
3. Fail closed when evidence, accepted authority, IU execution authorization, unresolved-item triage, validation, or artifact concordance is missing.
4. Archive/update accepted state only after close criteria are satisfied.
5. Do not use close to backfill missing governance after ungoverned implementation.

<!-- /HIRMOS-CAPSULE:close:PROD-L8.33C-2 canonical command capsule v1 -->
