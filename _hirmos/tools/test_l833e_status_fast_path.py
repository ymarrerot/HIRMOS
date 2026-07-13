#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.33E status read-only bootstrap fast path and minimum read set."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
HIRMOS = HERE.parent
ROOT = HIRMOS.parent.parent
CLI = ROOT / 'tools/cli/dist/index.js'


def assert_contains(path: Path, phrase: str) -> None:
    assert path.exists(), f'missing {path}'
    body = path.read_text(errors='ignore')
    assert phrase in body, f'{path} missing {phrase!r}'


def test_status_core_surface_declares_read_only_bootstrap_fast_path() -> None:
    status = HIRMOS / 'core/commands/status.md'
    for phrase in [
        'Status read-only bootstrap fast path',
        'without creating `_hirmos/session/bootstrap/BOOTSTRAP_REPORT.md`',
        'Bootstrap completion remains required before advancing commands',
        'Status minimum read set',
        '_hirmos/system/accepted-state/CARRY_FORWARD.md',
    ]:
        assert_contains(status, phrase)


def test_status_capsule_projects_fast_path_and_minimum_reads() -> None:
    capsule = HIRMOS / 'integrations/agent-tools/capsules/commands/status.md'
    for phrase in [
        'Status read-only bootstrap fast path',
        'without creating `BOOTSTRAP_REPORT.md`',
        'Status minimum read set',
        'Active session: add `SESSION_LEDGER.md`',
    ]:
        assert_contains(capsule, phrase)


def test_cursor_status_skill_contains_fast_path_after_cli_projection() -> None:
    tmp = Path(tempfile.mkdtemp(prefix='hirmos-l833e-project-'))
    try:
        shutil.copytree(HIRMOS, tmp / '_hirmos', ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
        result = subprocess.run(['node', str(CLI), 'init', str(tmp), '--integration', 'cursor', '--offline'], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        assert result.returncode == 0, result.stdout
        assert_contains(tmp / '.cursor/skills/hirmos-status/SKILL.md', 'Status read-only bootstrap fast path')
        assert_contains(tmp / '.cursor/commands/hirmos-status.md', 'Status minimum read set')
        assert not (tmp / '.cursor/skills/hirmos/SKILL.md').exists(), 'must not generate broad HIRMOS skill'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    tests = [
        test_status_core_surface_declares_read_only_bootstrap_fast_path,
        test_status_capsule_projects_fast_path_and_minimum_reads,
        test_cursor_status_skill_contains_fast_path_after_cli_projection,
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
    print(f'PASS: PROD-L8.33E focused fixtures ({len(tests)}/{len(tests)})')
