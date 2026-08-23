#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.33H implementation completion convergence."""
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


def copy_hirmos(prefix: str) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix=prefix))
    shutil.copytree(HIRMOS, tmp / '_hirmos', ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
    return tmp


def run_validator(hirmos_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(hirmos_dir / 'tools/validate.py')],
        cwd=hirmos_dir,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def test_core_requires_same_pass_implementation_completion_convergence() -> None:
    for rel, phrases in {
        'core/authority/INTERACTION_POSTURE.md': [
            'Same-stage convergence and pause minimality',
            'It must not stop merely because project-file edits or IU execution finished',
            'Pause only when the next safe step depends on meaningful user-owned input',
        ],
        'core/commands/continue.md': [
            'PROD-L8.33H Implementation Completion Convergence',
            'authorization gate, not a mandatory terminal pause',
            'recommend `hirmos close`',
            'Recovery rule for a bare `hirmos continue`',
        ],
        'core/protocol/COMMAND_STATE_MACHINE.md': [
            'Implementation completion convergence rule',
            'two planned user pauses before execution',
            'Purposeful continue rendering',
        ],
        'extensions/implementation-agent/entrypoints/default.md': [
            'Same-pass implementation convergence',
            'Model-owned review is not by itself a user-owned pause',
        ],
        'extensions/implementation-agent/capabilities/session-implementation-review/entrypoints/default.md': [
            'Invocation timing',
            'does not require a separate user request',
        ],
    }.items():
        for phrase in phrases:
            assert_contains(HIRMOS / rel, phrase)


def test_user_docs_preserve_two_planned_pauses_and_conditional_extra_pause() -> None:
    assert_contains(HIRMOS / 'docs/1-use-hirmos/getting-started/quickstart.md', 'two planned pauses before execution')
    assert_contains(HIRMOS / 'docs/1-use-hirmos/getting-started/quickstart.md', 'An extra pause is warranted only when the review needs user-owned evidence/decision')
    assert_contains(HIRMOS / 'docs/1-use-hirmos/getting-started/commands.md', 'A third `hirmos continue` pause is conditional')
    assert_contains(HIRMOS / 'docs/1-use-hirmos/examples/delivery-baseline-and-phase-session.md', 'A separate pre-close `hirmos continue` is not a routine third pause')


def test_cursor_projection_contains_completion_convergence_rule() -> None:
    project = copy_hirmos('hirmos-l833h-cursor-')
    try:
        result = subprocess.run(
            ['node', str(CLI), 'init', str(project), '--integration', 'cursor', '--offline'],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        assert result.returncode == 0, result.stdout
        assert_contains(project / '.cursor/commands/hirmos-continue.md', 'Implementation completion convergence')
        assert_contains(project / '.cursor/commands/hirmos-continue.md', 'recommend `hirmos close`')
        assert_contains(project / '.cursor/skills/hirmos-continue/SKILL.md', 'infer close-preparation / implementation-completion review')
    finally:
        shutil.rmtree(project, ignore_errors=True)


def test_validator_rejects_missing_convergence_rule() -> None:
    project = copy_hirmos('hirmos-l833h-validator-')
    try:
        command = project / '_hirmos/core/commands/continue.md'
        command.write_text(command.read_text().replace('PROD-L8.33H Implementation Completion Convergence', 'Implementation Completion'))
        result = run_validator(project / '_hirmos')
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.33H' in result.stdout, result.stdout
    finally:
        shutil.rmtree(project, ignore_errors=True)


if __name__ == '__main__':
    tests = [
        test_core_requires_same_pass_implementation_completion_convergence,
        test_user_docs_preserve_two_planned_pauses_and_conditional_extra_pause,
        test_cursor_projection_contains_completion_convergence_rule,
        test_validator_rejects_missing_convergence_rule,
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
    print(f'PASS: PROD-L8.33H focused fixtures ({len(tests)}/{len(tests)})')
