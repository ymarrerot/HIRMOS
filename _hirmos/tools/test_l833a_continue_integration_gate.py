#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.33A continue command integration gate; expected at least 3 L8.33A focused cases."""
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
    tmp = Path(tempfile.mkdtemp(prefix='hirmos-l833a-'))
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
    write_state(dst, continuation_pass=1)
    return dst


def write_state(root: Path, *, continuation_pass: int) -> None:
    state = json.loads((root / 'core/templates/session/SESSION_STATE.json').read_text())
    state.update({
        'status': 'active',
        'session_id': '2026-07-07-001',
        'session_focus': 'single_session',
        'lifecycle_stage': 'implementation',
        'active_authority': '_hirmos/session/SESSION_SCOPE.md',
        'continuation_pass': continuation_pass,
        'pending_correction': False,
        'allowed_next_commands': ['hirmos continue', 'hirmos status'],
        'recommended_next_command': 'hirmos continue',
        'updated_at': '2026-07-07T00:00:00Z',
    })
    (root / 'session' / 'SESSION_STATE.json').write_text(json.dumps(state, indent=2) + '\n')


def write_scope(root: Path, *, iu_required: bool, no_iu_rationale: str = '') -> None:
    required = 'REQUIRED' if iu_required else 'NOT_REQUIRED'
    rationale = no_iu_rationale if no_iu_rationale else ('NOT_APPLICABLE' if iu_required else 'PENDING')
    (root / 'session' / 'SESSION_SCOPE.md').write_text(f"""# Session Scope

Status: active-session Main Artifact.
Purpose: fixture scope for L8.33A.

## 1. Session Identity

- Session ID: 2026-07-07-001
- Scope status: ACCEPTED
- Baseline acceptance authority recorded: YES
- Material project/source edit authorization: {'REQUIRES_IU_EXECUTION_AUTHORIZATION' if iu_required else 'AUTHORIZED_WITHOUT_IU'}

## PROD-L8.33A Continue Implementation Gate

- `hirmos continue` implementation authority: classify and gate before coding.
- IU required/requested decision: {required}
- IU plan status: {'PENDING' if iu_required else 'NOT_APPLICABLE'}
- No-IU rationale, if applicable: {rationale}
- Material project/source edit authority: BLOCKED until accepted baseline authority exists and, when IU mode applies, `IU_EXECUTION_AUTHORIZED` is recorded after IU plan review.
""")


def write_ledger(root: Path, *, iu_requested: bool, iu_plan_accepted: bool, iu_authorized: bool, material_edit: bool) -> None:
    ledger = (root / 'core/templates/session/SESSION_LEDGER.md').read_text()
    marker = '|---:|---|---|---|---|---|---|---|---|\n'
    row = '| 1 | hirmos continue | {} | BASELINE_ACCEPTED | BASELINE_ACCEPTED | SESSION_SCOPE.md SESSION_LEDGER.md | fixture | PASS | hirmos continue |\n'.format('IU_EXECUTION_AUTHORIZATION' if iu_authorized else 'ACCEPTANCE_ONLY')
    ledger = ledger.replace(marker, marker + row, 1)
    ledger += '\nBASELINE_ACCEPTED_OR_AMENDED: PASS\n'
    if iu_requested:
        ledger += '\nIU Planning requested by user. IU Plan — Review or Change required before material edits.\n'
    if iu_plan_accepted:
        ledger += '\nIU_PLAN_ACCEPTED: PASS\n'
    if iu_authorized:
        ledger += '\nIU_EXECUTION_AUTHORIZED: PASS\n'
    if material_edit:
        ledger += '\n## Material Edit Start Record\n\n- Material project/source edits: YES\n- Material project-file edits: YES\n- Files/areas about to be edited: fixture source files\n- Active gate validator result: PASS\n'
    (root / 'session' / 'SESSION_LEDGER.md').write_text(ledger)


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(root / 'tools/validate.py')], cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def test_continue_with_requested_ius_and_same_pass_material_edit_fails() -> None:
    root = make_copy()
    try:
        write_scope(root, iu_required=True)
        write_ledger(root, iu_requested=True, iu_plan_accepted=False, iu_authorized=False, material_edit=True)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.33A material edit before accepted IU plan and IU_EXECUTION_AUTHORIZED' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_continue_without_ius_requires_recorded_no_iu_rationale_before_material_edit() -> None:
    root = make_copy()
    try:
        write_scope(root, iu_required=False, no_iu_rationale='PENDING')
        write_ledger(root, iu_requested=False, iu_plan_accepted=False, iu_authorized=False, material_edit=True)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.33A material edit without recorded no-IU rationale' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_continue_with_ius_accepted_and_authorized_passes() -> None:
    root = make_copy()
    try:
        write_scope(root, iu_required=True)
        write_ledger(root, iu_requested=True, iu_plan_accepted=True, iu_authorized=True, material_edit=True)
        result = run_validator(root)
        assert result.returncode == 0, result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_integration_missing_status_capsule_fails() -> None:
    root = make_copy()
    try:
        p = root / 'integrations/agent-tools/templates/cursor.mdc'
        p.write_text(p.read_text().replace('## hirmos status command gate', '## hirmos current-state report'))
        # Keep session clean so failure comes from static integration gate.
        write_scope(root, iu_required=True)
        write_ledger(root, iu_requested=True, iu_plan_accepted=True, iu_authorized=True, material_edit=False)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.33A integration cursor template missing command capsule phrase' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


if __name__ == '__main__':
    tests = [
        test_continue_with_requested_ius_and_same_pass_material_edit_fails,
        test_continue_without_ius_requires_recorded_no_iu_rationale_before_material_edit,
        test_continue_with_ius_accepted_and_authorized_passes,
        test_integration_missing_status_capsule_fails,
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
    print(f'PASS: PROD-L8.33A focused fixtures ({len(tests)}/{len(tests)})')
