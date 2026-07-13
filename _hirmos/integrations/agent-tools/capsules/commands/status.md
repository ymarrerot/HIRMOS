<!-- HIRMOS-CAPSULE:status:PROD-L8.33C-2 canonical command capsule v1 -->
## hirmos status command capsule

`hirmos status` is read-only.

Required behavior:
1. Read the active HIRMOS state and relevant session/delivery artifacts.
2. Report the current lifecycle stage, active gate, blocker/conflict if any, and exactly one recommended next command.
3. Report whether baseline authority is accepted and whether IU execution is authorized when IU mode applies.
4. Do not edit product/source files.
5. Do not advance lifecycle state.
6. Do not backfill artifacts to make status appear clean.


Status read-only bootstrap fast path:
- `hirmos status` may run read-only without creating `BOOTSTRAP_REPORT.md`.
- If bootstrap is absent or incomplete, report that advancing commands are blocked until bootstrap passes.
- Do not create bootstrap artifacts, backfill accepted-state artifacts, repair carry-forward registers, or advance lifecycle state during status.

Status minimum read set:
- Idle/post-close: `_hirmos/hirmos.config.json`, `_hirmos/session/SESSION_STATE.json`, `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`, `_hirmos/system/accepted-state/CARRY_FORWARD.md`, and latest archive manifest if referenced or discoverable.
- Active session: add `SESSION_LEDGER.md`, `SESSION_SCOPE.md`, unresolved register when relevant, and IU files only when IU state is relevant.
- Delivery/phase: add delivery or phase files only when pointers indicate active delivery/phase context.

<!-- /HIRMOS-CAPSULE:status:PROD-L8.33C-2 canonical command capsule v1 -->
