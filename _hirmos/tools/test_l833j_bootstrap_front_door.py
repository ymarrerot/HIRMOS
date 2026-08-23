#!/usr/bin/env python3
"""Focused checks for PROD-L8.33J bootstrap front-door simplification and authority deduplication."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def check_first_contact_surface() -> None:
    body = (ROOT / 'AGENTS.md').read_text(errors='ignore')
    required = [
        'HIRMOS is an open framework for governed AI-assisted software development',
        'You are operating as a HIRMOS-governed engineering agent for this project',
        'Governance posture rule',
        'First-contact working-copy rules',
        'Bootstrap and command routing',
        'Bootstrap-only request boundary',
        'Required next action',
    ]
    for phrase in required:
        assert phrase in body, phrase
    assert not re.search(r'PROD-L8\.\d+', body, re.I)


def check_bootstrap_repetition_boundary() -> None:
    body = (ROOT / 'core/bootstrap.md').read_text(errors='ignore')
    for step in range(3, 12):
        assert f'## Step {step} —' in body
    quiz = re.search(r'## Step 12 — Bootstrap quiz(.*?)## Step 13 — Bootstrap report', body, re.S)
    assert quiz
    assert len(re.findall(r'^\d+\.', quiz.group(1), re.M)) == 16
    assert '_hirmos/core/templates/session/bootstrap/BOOTSTRAP_REPORT.md' in body
    assert 'Do not maintain a second report schema in this bootstrap procedure' in body
    assert '## Bootstrap Discipline Answer Recovery' not in body
    assert not re.search(r'PROD-L8\.\d+', body, re.I)


def check_status_fast_path_alignment() -> None:
    agents = (ROOT / 'AGENTS.md').read_text(errors='ignore')
    bootstrap = (ROOT / 'core/bootstrap.md').read_text(errors='ignore')
    commands = (ROOT / 'core/protocol/COMMANDS.md').read_text(errors='ignore')
    status = (ROOT / 'core/commands/status.md').read_text(errors='ignore')
    assert 'Full bootstrap is required before the advancing commands `hirmos start`, `hirmos continue`, and `hirmos close`' in agents
    assert '`hirmos status` is the exception' in agents
    assert 'advancing runtime commands are blocked until full bootstrap passes' in bootstrap
    assert 'read-only bootstrap fast path' in bootstrap
    assert '`hirmos status` is the read-only exception' in commands
    assert 'without creating `BOOTSTRAP_REPORT.md`' in commands
    assert 'without creating `_hirmos/session/bootstrap/BOOTSTRAP_REPORT.md`' in status


def check_command_pointer_deduplication() -> None:
    body = (ROOT / 'core/bootstrap.md').read_text(errors='ignore')
    assert '_hirmos/core/commands/<command>.md\n_hirmos/core/commands/<command>.md' not in body
    adaptive = re.search(r'Adaptive files are read later.*?```text\n(.*?)```', body, re.S)
    assert adaptive
    assert adaptive.group(1).count('_hirmos/core/commands/<command>.md') == 1


def main() -> int:
    tests = [
        check_first_contact_surface,
        check_bootstrap_repetition_boundary,
        check_status_fast_path_alignment,
        check_command_pointer_deduplication,
    ]
    failures = []
    for test in tests:
        try:
            test()
            print(f'PASS: {test.__name__}')
        except AssertionError as exc:
            failures.append((test.__name__, str(exc)))
            print(f'FAIL: {test.__name__}: {exc}')
    if failures:
        return 1
    print(f'PASS: PROD-L8.33J focused checks ({len(tests)}/{len(tests)})')
    return 0


if __name__ == '__main__':
    sys.exit(main())
