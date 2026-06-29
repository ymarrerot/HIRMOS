#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
errors = []
shared = root / 'core/authority/SHARED_CAPABILITY_CONTROLS.md'
if not shared.exists():
    errors.append('missing shared capability controls file')
else:
    body = shared.read_text(errors='ignore')
    for phrase in ['Required behavior baseline', 'Canonical interaction posture visibility', 'Unresolved-item producer obligation', 'Runtime integration responsibilities']:
        if phrase not in body:
            errors.append(f'shared controls missing {phrase}')
refs = []
missing = []
for ep in (root / 'extensions').glob('**/entrypoints/default.md'):
    body = ep.read_text(errors='ignore')
    if 'SHARED_CAPABILITY_CONTROLS.md' in body:
        refs.append(ep)
    if 'capabilities' in str(ep) and '## Required behavior' in body and 'SHARED_CAPABILITY_CONTROLS.md' not in body:
        missing.append(str(ep.relative_to(root)))
if len(refs) < 15:
    errors.append(f'expected at least 15 shared-control references, found {len(refs)}')
if missing:
    errors.append('capability entrypoints missing shared refs: ' + ', '.join(missing[:5]))
ledger = root / 'core/templates/session/SESSION_LEDGER.md'
if not ledger.exists():
    errors.append('missing SESSION_LEDGER template')
else:
    text = ledger.read_text(errors='ignore')
    for phrase in ['Gate Marker Map', 'PROD-L8.19', 'PROD-L8.21', 'PROD-L8.23', 'PROD-L8.24', 'PROD-L8.30A', 'PROD-L8.31', 'PROD-L8.32K', 'PROD-L8.32L']:
        if phrase not in text:
            errors.append(f'ledger gate map missing {phrase}')
if errors:
    for err in errors:
        print('FAIL:', err)
    sys.exit(1)
print('PASS: L8.32O shared controls and gate marker map fixtures passed (3/3)')
