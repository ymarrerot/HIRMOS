#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.32Z start non-implementation boundary; expected at least 3 L8.32Z focused cases."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
HIRMOS = HERE.parent


def make_bootstrap_report() -> str:
    rows = []
    for i in range(1, 17):
        rows.append(
            f"Q{i}. fixture question — Answer: fixture answer {i}; Source: _hirmos/core/bootstrap.md; Answer basis: ANSWERED_FROM_CORE_PROTOCOLS"
        )
    return "\n".join([
        "# Bootstrap Report",
        "",
        "Status: PASSED",
        "Purpose: fixture bootstrap report for focused validator tests.",
        "",
        "## Runtime Bootstrap Summary",
        "| Field | Value / pointer |",
        "|---|---|",
        "| Status | PASSED |",
        "",
        "## Bootstrap Discipline Answers",
        "| Question | Answer | Source | Answer basis |",
        "|---|---|---|---|",
        *rows,
        "",
        "## Allowed Next Action",
        "hirmos continue",
        "",
    ])


def make_copy() -> Path:
    tmp = Path(tempfile.mkdtemp(prefix='hirmos-l832z-'))
    dst = tmp / '_hirmos'
    shutil.copytree(HIRMOS, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
    for rel in ['session', 'system/history']:
        path = dst / rel
        if path.exists():
            shutil.rmtree(path)
    (dst / 'session').mkdir(parents=True, exist_ok=True)
    (dst / 'session' / '.gitkeep').write_text('')
    (dst / 'session' / 'implementation-units').mkdir(parents=True, exist_ok=True)
    (dst / 'session' / 'implementation-units' / '.gitkeep').write_text('')
    (dst / 'session' / 'bootstrap').mkdir(parents=True, exist_ok=True)
    (dst / 'session' / 'bootstrap' / '.gitkeep').write_text('')
    (dst / 'session' / 'bootstrap' / 'BOOTSTRAP_REPORT.md').write_text(make_bootstrap_report())
    (dst / 'system' / 'history' / 'sessions').mkdir(parents=True, exist_ok=True)
    (dst / 'system' / 'history' / 'sessions' / '.gitkeep').write_text('')
    (dst / 'session' / 'unresolved-items.md').write_text((dst / 'core/templates/session/unresolved-items.md').read_text())
    write_state(dst, status='active', lifecycle_stage='implementation_readiness', continuation_pass=0)
    return dst


def write_state(root: Path, *, status: str, lifecycle_stage: str, continuation_pass: int) -> None:
    state = json.loads((root / 'core/templates/session/SESSION_STATE.json').read_text())
    state.update({
        'status': status,
        'session_id': '2026-07-06-001' if status != 'idle' else '',
        'session_focus': 'single_session' if status == 'active' else 'idle',
        'lifecycle_stage': lifecycle_stage,
        'active_authority': '_hirmos/session/SESSION_SCOPE.md' if status == 'active' else None,
        'continuation_pass': continuation_pass,
        'pending_correction': False,
        'allowed_next_commands': ['hirmos continue', 'hirmos status'] if status == 'active' else ['hirmos start', 'hirmos status'],
        'recommended_next_command': 'hirmos continue' if status == 'active' else 'hirmos start',
        'updated_at': '2026-07-06T00:00:00Z',
    })
    (root / 'session' / 'SESSION_STATE.json').write_text(json.dumps(state, indent=2) + '\n')


def write_scope(root: Path, *, accepted: bool, iu_required: bool = False) -> None:
    status = 'ACCEPTED' if accepted else 'UNDER_BASELINE_REVIEW'
    baseline = 'YES' if accepted else 'NO'
    iu = 'YES' if iu_required else 'NO'
    edit_auth = 'AUTHORIZED_WITHOUT_IU' if accepted and not iu_required else ('REQUIRES_IU_EXECUTION_AUTHORIZATION' if iu_required else 'NOT_AUTHORIZED')
    (root / 'session' / 'SESSION_SCOPE.md').write_text(f"""# Session Scope

Status: active-session Main Artifact.
Purpose: fixture scope for L8.32Z.

## 1. Session Identity

- Session ID: 2026-07-06-001
- Scope status: {status}

## 3. Authorized Scope / Outcome

- Authorized outcome: fixture product change
- Project-file mutation authorized before baseline acceptance: NO
- Baseline acceptance authority recorded: {baseline}
- Material project/source edit authorization: {edit_auth}

## 10. Implementation Boundary and IU Planning Pointers

- Implementation units required: {iu}
- Accepted baseline authority is required before any material project/source edit.
""")


def write_ledger(root: Path, *, baseline_accepted: bool, material_edit: bool, iu_authorized: bool = False) -> None:
    ledger = (root / 'core/templates/session/SESSION_LEDGER.md').read_text()
    register_marker = '|---:|---|---|---|---|---|---|---|---|\n'
    gate_marker = '| BASELINE_ACCEPTED_OR_AMENDED | material project/source edits | PENDING / PASS / BLOCKED / NOT_APPLICABLE | user continuation + `SESSION_SCOPE.md` status | Continuation Pass Register | implementation readiness or IU planning |'
    if baseline_accepted:
        ledger = ledger.replace(register_marker, register_marker + '| 1 | hirmos continue | ACCEPTANCE_ONLY | BASELINE_ACCEPTED | BASELINE_ACCEPTED | SESSION_SCOPE.md SESSION_LEDGER.md | fixture | PASS | hirmos continue |\n', 1)
        ledger = ledger.replace(gate_marker, '| BASELINE_ACCEPTED_OR_AMENDED | material project/source edits | PASS | user continuation + `SESSION_SCOPE.md` status | Continuation Pass Register | implementation readiness or IU planning |')
    if iu_authorized:
        ledger += '\nIU_EXECUTION_AUTHORIZED: PASS\n'
    if material_edit:
        ledger += '\n## Material Edit Start Record\n\n- Material project/source edits: YES\n- Material project-file edits: YES\n- Files/areas about to be edited: fixture source files\n- Active gate validator result: PASS\n'
    (root / 'session' / 'SESSION_LEDGER.md').write_text(ledger)


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(root / 'tools/validate.py')], cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def test_material_edit_before_baseline_acceptance_fails() -> None:
    root = make_copy()
    try:
        write_scope(root, accepted=False)
        write_ledger(root, baseline_accepted=False, material_edit=True)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.32Z material edit before accepted baseline authority' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_material_edit_after_baseline_acceptance_without_iu_passes() -> None:
    root = make_copy()
    try:
        write_state(root, status='active', lifecycle_stage='implementation', continuation_pass=1)
        write_scope(root, accepted=True, iu_required=False)
        write_ledger(root, baseline_accepted=True, material_edit=True)
        result = run_validator(root)
        assert result.returncode == 0, result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_iu_mode_still_requires_iu_execution_authorized() -> None:
    root = make_copy()
    try:
        write_state(root, status='active', lifecycle_stage='implementation', continuation_pass=1)
        write_scope(root, accepted=True, iu_required=True)
        write_ledger(root, baseline_accepted=True, material_edit=True, iu_authorized=False)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.32Z IU-mode material edit before IU_EXECUTION_AUTHORIZED' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


if __name__ == '__main__':
    tests = [
        test_material_edit_before_baseline_acceptance_fails,
        test_material_edit_after_baseline_acceptance_without_iu_passes,
        test_iu_mode_still_requires_iu_execution_authorized,
    ]
    failures = 0
    for test in tests:
        try:
            test()
            print(f'PASS: {test.__name__}')
        except Exception as exc:
            failures += 1
            print(f'FAIL: {test.__name__}: {exc}')
    if failures:
        sys.exit(1)
    print(f'PASS: PROD-L8.32Z focused fixtures ({len(tests)}/{len(tests)})')
