#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.32S runtime command surface unification.

The former _hirmos/core/runtime/*.packet.md layer is intentionally removed.
The compact runtime command authority now lives directly under _hirmos/core/commands/.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def test_runtime_directory_removed() -> None:
    if (ROOT / 'core/runtime').exists():
        fail('core/runtime still exists; command runtime authority must live in core/commands')


def test_commands_are_canonical_authority() -> None:
    for name in ['start', 'continue', 'status', 'close']:
        path = ROOT / 'core/commands' / f'{name}.md'
        if not path.exists():
            fail(f'missing command authority file: {path.relative_to(ROOT)}')
        body = path.read_text(errors='ignore')
        for phrase in [
            'Status: compact command authority.',
            'PROD-L8.32S Runtime Command Surface Unification',
            'This file is the canonical compact command runtime authority',
            'read this command file first',
        ]:
            if phrase not in body:
                fail(f'{path.relative_to(ROOT)} missing phrase: {phrase}')
        for forbidden in [
            'Primary runtime surface:',
            'Do not use this slim command file as a substitute for the packet',
            'Runtime Packet:',
        ]:
            if forbidden in body:
                fail(f'{path.relative_to(ROOT)} retained obsolete packet-wrapper wording: {forbidden}')


def test_no_active_packet_references() -> None:
    allowed = {ROOT / 'CHANGELOG.md', ROOT / 'UPGRADE_GUIDE.md', ROOT / 'tools/validate.py', ROOT / 'tools/test_l832s_command_surface_unification.py'}
    for path in ROOT.rglob('*'):
        if not path.is_file() or path in allowed:
            continue
        try:
            body = path.read_text(errors='ignore')
        except UnicodeDecodeError:
            continue
        if path.match('core/commands/*.md'):
            # The command files may mention the removed runtime packet layer only in the L8.32S removal note.
            continue
        for token in ['_hirmos/core/runtime/', 'core/runtime/', '.packet.md']:
            if token in body:
                fail(f'obsolete runtime packet reference in {path.relative_to(ROOT)}: {token}')


def main() -> None:
    tests = [test_runtime_directory_removed, test_commands_are_canonical_authority, test_no_active_packet_references]
    for test in tests:
        test()
    print(f'PASS: PROD-L8.32S command surface unification fixtures passed ({len(tests)}/{len(tests)})')


if __name__ == '__main__':
    main()
