#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.32Q delivery concordance simplification.

These tests protect the simplification-first solution: remove duplicated mutable
status surfaces, derive delivery completion posture, and label archived pre-close
machine state explicitly.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
HIRMOS = HERE.parent
VALIDATOR = HIRMOS / 'tools' / 'validate.py'


def make_copy() -> Path:
    tmp = Path(tempfile.mkdtemp(prefix='hirmos-l832q-'))
    dst = tmp / '_hirmos'
    shutil.copytree(HIRMOS, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
    # Fixture isolation: this test must run both from the framework package and
    # from an installed generated project. Remove live generated project state
    # before creating synthetic cases so unrelated archives/delivery rows cannot
    # interfere with focused Q assertions.
    for rel in [
        'system/delivery',
        'system/history',
        'session',
    ]:
        path = dst / rel
        if path.exists():
            shutil.rmtree(path)
    (dst / 'system' / 'delivery').mkdir(parents=True, exist_ok=True)
    (dst / 'system' / 'delivery' / '.gitkeep').write_text('')
    (dst / 'system' / 'history' / 'sessions').mkdir(parents=True, exist_ok=True)
    (dst / 'system' / 'history' / 'sessions' / '.gitkeep').write_text('')
    (dst / 'session' / 'bootstrap').mkdir(parents=True, exist_ok=True)
    (dst / 'session' / 'bootstrap' / '.gitkeep').write_text('')
    (dst / 'session' / 'implementation-units').mkdir(parents=True, exist_ok=True)
    (dst / 'session' / 'implementation-units' / '.gitkeep').write_text('')
    (dst / 'session' / '.gitkeep').write_text('')
    (dst / 'session' / 'SESSION_STATE.json').write_text('''{
  "schema_version": "session-state-v1",
  "status": "idle",
  "session_id": "",
  "lifecycle_stage": "idle",
  "continuation_pass": 0,
  "pending_correction": false,
  "allowed_next_commands": ["hirmos start", "hirmos status"],
  "recommended_next_command": "hirmos start",
  "blocking_reason": null,
  "created_at": null,
  "updated_at": null,
  "_derived_command_state": {
    "status": "DERIVED_CACHE",
    "source_ledger_event": null,
    "source_runtime_packet": null,
    "active_gate_validator_result": null,
    "validity": "UNVERIFIED"
  },
  "_jit_artifact_creation_notice": "Optional active artifacts are absent until their owning concern becomes applicable."
}
''')
    accepted_state = dst / 'system' / 'accepted-state'
    accepted_state.mkdir(parents=True, exist_ok=True)
    template_css = dst / 'core' / 'templates' / 'system' / 'CURRENT_SYSTEM_STATE.md'
    if template_css.exists():
        shutil.copyfile(template_css, accepted_state / 'CURRENT_SYSTEM_STATE.md')
    return dst


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(root / 'tools' / 'validate.py')], cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def write_delivery(root: Path, *, active_scope: bool = False, status_log: bool = False, parent_active: bool = False, proposed_rows: bool = False) -> None:
    delivery_root = root / 'system' / 'delivery'
    delivery_root.mkdir(parents=True, exist_ok=True)
    delivery = delivery_root / 'menugen-mvp'
    phase_dir = delivery / 'phases'
    phase_dir.mkdir(parents=True, exist_ok=True)
    (delivery_root / 'DELIVERY_PLAN.md').write_text(
        '# Delivery Plan\n\n## Delivery Index\n\n| Delivery ID | Name | Status | Scope file |\n|---|---|---|---|\n| menugen-mvp | MenuGen | completed | _hirmos/system/delivery/menugen-mvp/DELIVERY_SCOPE.md |\n| PHASE-01 | MenuGen phase | accepted | _hirmos/system/delivery/menugen-mvp/DELIVERY_SCOPE.md |\n\n'
        + ('## Delivery Status Update Log\n\n- stale narrative log\n' if status_log else '## Delivery Status Pointer Index\n\n| Delivery | Current status label | Owning status source | Latest evidence pointer | Notes |\n|---|---|---|---|---|\n| menugen-mvp | complete | DELIVERY_SCOPE.md | archive | derived |\n')
    )
    status = 'Status: ACTIVE\n' if active_scope else 'Authority status: BASELINED\n'
    rows = '| FR-001 | Upload | MUST | PHASE-01 | PROPOSED |\n' if proposed_rows else '| FR-001 | Upload | MUST | PHASE-01 |\n'
    header = '| ID | Requirement | Priority | Covered by phase(s) | Status |\n|---|---|---|---|---|\n' if proposed_rows else '| ID | Requirement | Priority | Covered by phase(s) |\n|---|---|---|---|\n'
    (delivery / 'DELIVERY_SCOPE.md').write_text(
        f'# Delivery Scope\n\n{status}\n## Scoped Requirements\n\n### Functional requirements\n\n{header}{rows}\n\n## Delivery Close Verification\n\nClose result: ACCEPTED\n'
    )
    parent = 'Parent delivery status: ACTIVE\n' if parent_active else 'Parent delivery status source: derived from roadmap/register and current-state pointers\n'
    (phase_dir / 'PHASE-01.md').write_text(f'''# Phase Scope

Lifecycle status: ACCEPTED
{parent}
## PROD-L8.24 Generated Phase Review Gate Validation

Actual final codebase reviewed: YES
Scope coverage result: PASS
Runtime evidence level: USER_ENVIRONMENT_VERIFIED
Production evidence level: NOT_CLAIMED
Final phase review result: PASS
Why this result is honest: fixture phase contains completed local evidence only.
What is not claimed: production readiness.
''')
    (root / 'system' / 'accepted-state').mkdir(parents=True, exist_ok=True)
    css = root / 'system' / 'accepted-state' / 'CURRENT_SYSTEM_STATE.md'
    css.write_text((css.read_text(errors='ignore') if css.exists() else '# Current System State\n') + '\n\nDerived delivery result: menugen-mvp complete\n')


def test_delivery_scope_active_conflict_fails() -> None:
    root = make_copy()
    try:
        write_delivery(root, active_scope=True)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.32Q delivery completion conflict' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_delivery_status_update_log_fails() -> None:
    root = make_copy()
    try:
        write_delivery(root, status_log=True)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'Delivery Status Update Log' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_pre_close_archive_concordance_label_passes() -> None:
    root = make_copy()
    try:
        write_delivery(root)
        arch = root / 'system' / 'history' / 'sessions' / 'session-001'
        arch.mkdir(parents=True, exist_ok=True)
        (arch / 'SESSION_STATE.json').write_text('{"status":"archived","created_at":"2026-06-28T00:00:00Z","updated_at":"2026-06-28T00:00:00Z","run_context":{"mode":"fixture"}}\n')
        (arch / 'PRE_CLOSE_SESSION_STATE.json').write_text('{"status":"active","lifecycle_stage":"implementation_complete"}\n')
        (arch / 'bootstrap').mkdir(parents=True, exist_ok=True)
        boot = '\n'.join([
            f'Q{i}\nAnswer: fixture answer {i}\nSource: current fixture artifacts\nAnswer basis: ANSWERED_FROM_CURRENT_ARTIFACTS\n'
            for i in range(1, 17)
        ])
        (arch / 'bootstrap' / 'BOOTSTRAP_REPORT.md').write_text(boot)
        (arch / 'SESSION_LEDGER.md').write_text('# Session Ledger\n\n## Pre-Close Machine Command State Concordance\n\nSource: PRE_CLOSE_SESSION_STATE.json\n\n| Status | active |\n| Lifecycle | implementation_complete |\n\nActive generated-artifact validation result: PASS\n\n## PROD-L8.31 Generated-Run Mechanical Gate Record\n\nActive gate validator result: PASS\nMechanical gate decision: PASS\n\n## Archived Session State Concordance\n\nArchived SESSION_STATE.json: archived\n')
        result = run_validator(root)
        assert result.returncode == 0, result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_parent_delivery_active_conflict_fails() -> None:
    root = make_copy()
    try:
        write_delivery(root, parent_active=True)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'phase mirrors stale parent delivery ACTIVE' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_proposed_requirement_rows_after_completion_fail() -> None:
    root = make_copy()
    try:
        write_delivery(root, proposed_rows=True)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'PROPOSED requirement/status rows' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


if __name__ == '__main__':
    tests = [
        test_delivery_scope_active_conflict_fails,
        test_delivery_status_update_log_fails,
        test_pre_close_archive_concordance_label_passes,
        test_parent_delivery_active_conflict_fails,
        test_proposed_requirement_rows_after_completion_fail,
    ]
    failures = []
    for test in tests:
        try:
            test()
            print(f'PASS: {test.__name__}')
        except Exception as exc:
            failures.append((test.__name__, exc))
            print(f'FAIL: {test.__name__}: {exc}')
    if failures:
        raise SystemExit(1)
    print(f'PASS: PROD-L8.32Q delivery concordance fixtures — {len(tests)}/{len(tests)}')
