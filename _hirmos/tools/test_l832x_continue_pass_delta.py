#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.32X continue pass delta recording."""
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
    tmp = Path(tempfile.mkdtemp(prefix='hirmos-l832x-'))
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
    (dst / 'session' / 'SESSION_SCOPE.md').write_text(
        '# Session Scope\n\nDelivery governance active: NO\n\n## Scope Amendments\n\n'
        'Record every scope change after initial session scope approval. Reuse this section for continuation authority deltas; do not create a separate amendment artifact.\n\n'
        '| Amendment ID | Trigger / continue pass | Change | User approval / evidence | Impact on criteria / validation / close satisfaction | Ledger pointer |\n'
        '|---|---|---|---|---|---|\n'
    )
    (dst / 'session' / 'SESSION_LEDGER.md').write_text((dst / 'core/templates/session/SESSION_LEDGER.md').read_text())
    (dst / 'session' / 'unresolved-items.md').write_text((dst / 'core/templates/session/unresolved-items.md').read_text())
    write_state(dst, continuation_pass=0, status='idle', lifecycle_stage='idle')
    return dst


def write_state(root: Path, *, continuation_pass: int, status: str = 'active', lifecycle_stage: str = 'implementation') -> None:
    state = json.loads((root / 'core/templates/session/SESSION_STATE.json').read_text())
    state.update({
        'status': status,
        'session_id': '2026-06-29-001' if status != 'idle' else '',
        'session_focus': 'single_session' if status == 'active' else 'idle',
        'lifecycle_stage': lifecycle_stage,
        'active_authority': '_hirmos/session/SESSION_SCOPE.md' if status == 'active' else None,
        'continuation_pass': continuation_pass,
        'pending_correction': False,
        'allowed_next_commands': ['hirmos continue', 'hirmos status'] if status == 'active' else ['hirmos start', 'hirmos status'],
        'recommended_next_command': 'hirmos continue' if status == 'active' else 'hirmos start',
        'updated_at': '2026-06-29T00:00:00Z',
    })
    (root / 'session' / 'SESSION_STATE.json').write_text(json.dumps(state, indent=2) + '\n')


def write_pass_register(root: Path, rows: list[tuple[int, str]]) -> None:
    ledger = (root / 'core/templates/session/SESSION_LEDGER.md').read_text()
    marker = '|---:|---|---|---|---|---|---|---|---|\n'
    additions = ''.join(
        f'| {num} | hirmos continue | {ptype} | NO_SCOPE_CHANGE | NO_SCOPE_CHANGE | SESSION_LEDGER.md | validation output | PASS | hirmos continue |\n'
        for num, ptype in rows
    )
    if marker not in ledger:
        raise AssertionError('template marker missing')
    (root / 'session' / 'SESSION_LEDGER.md').write_text(ledger.replace(marker, marker + additions, 1))


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(root / 'tools/validate.py')], cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def test_active_continue_pass_register_matches_state_passes() -> None:
    root = make_copy()
    try:
        write_state(root, continuation_pass=3)
        write_pass_register(root, [(1, 'SCOPE_AMENDMENT'), (2, 'IU_EXECUTION_AUTHORIZATION'), (3, 'CORRECTIVE_PASS')])
        result = run_validator(root)
        assert result.returncode == 0, result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_active_continue_pass_register_mismatch_fails() -> None:
    root = make_copy()
    try:
        write_state(root, continuation_pass=3)
        write_pass_register(root, [(1, 'SCOPE_AMENDMENT')])
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.32X continuation pass mismatch' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


def test_archived_continue_pass_register_mismatch_fails() -> None:
    root = make_copy()
    try:
        shutil.rmtree(root / 'session')
        (root / 'session').mkdir(parents=True, exist_ok=True)
        (root / 'session' / '.gitkeep').write_text('')
        (root / 'session' / 'implementation-units').mkdir(parents=True)
        (root / 'session' / 'implementation-units' / '.gitkeep').write_text('')
        (root / 'session' / 'bootstrap').mkdir(parents=True)
        (root / 'session' / 'bootstrap' / '.gitkeep').write_text('')
        write_state(root, continuation_pass=0, status='idle', lifecycle_stage='idle')
        session_dir = root / 'system/history/sessions/2026-06-29-001'
        session_dir.mkdir(parents=True, exist_ok=True)
        state = json.loads((root / 'core/templates/session/SESSION_STATE.json').read_text())
        state.update({'status': 'closed', 'session_id': '2026-06-29-001', 'lifecycle_stage': 'closed', 'continuation_pass': 3})
        (session_dir / 'SESSION_STATE.json').write_text(json.dumps(state, indent=2) + '\n')
        ledger = (root / 'core/templates/session/SESSION_LEDGER.md').read_text()
        marker = '|---:|---|---|---|---|---|---|---|---|\n'
        ledger = ledger.replace(marker, marker + '| 1 | hirmos continue | SCOPE_AMENDMENT | authority changed | AUTHORITY_DELTA_APPENDED | SESSION_SCOPE.md | evidence | PASS | hirmos continue |\n', 1)
        (session_dir / 'SESSION_LEDGER.md').write_text(ledger)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.32X archived continuation pass mismatch' in result.stdout
    finally:
        shutil.rmtree(root.parent, ignore_errors=True)


if __name__ == '__main__':
    tests = [
        test_active_continue_pass_register_matches_state_passes,
        test_active_continue_pass_register_mismatch_fails,
        test_archived_continue_pass_register_mismatch_fails,
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
    print(f'PASS: PROD-L8.32X focused fixtures ({len(tests)}/{len(tests)})')
