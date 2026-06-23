#!/usr/bin/env python3
from pathlib import Path
import json, sys, re

root = Path(__file__).resolve().parents[1]

def fail(message: str):
    print('FAIL: ' + message)
    sys.exit(1)

required = [
    'AGENTS.md',
    'tools/test_validator_regressions.py',
    'tools/fixtures/README.md',
    'README.md',
    'LICENSE',
    'hirmos.config.json',
    'CHANGELOG.md',
    'UPGRADE_GUIDE.md',
    'inputs/README.md',
    'inputs/uploads/README.md',
    'inputs/prototypes/README.md',
    'inputs/references/README.md',
    'core/bootstrap.md',
    'core/authority/LIFECYCLE.md',
    'core/authority/ONBOARDING_PRINCIPLES.md',
    'core/authority/INTERACTION_MODES.md',
    'core/authority/ARTIFACT_MODEL.md',
    'core/authority/EXECUTION_CONTROL_GOVERNANCE.md',
    'core/authority/BEYOND_CLEAR_SPECS.md',
    'core/protocol/COMMANDS.md',
    'core/protocol/COMMAND_STATE_MACHINE.md',
    'core/protocol/UNRESOLVED_ITEMS.md',
    'core/protocol/VALIDATION_AND_EVIDENCE.md',
    'core/protocol/CLAIM_RECONCILIATION.md',
    'core/protocol/INSTALLATION_PACKAGING.md',
    'core/protocol/SESSION_ARTIFACTS.md',
    'core/protocol/GOVERNED_CHECKPOINTS.md',
    'core/protocol/CAPABILITY_ROUTING.md',
    'core/protocol/PROJECT_TYPES.md',
    'core/protocol/DELIVERY_GOVERNANCE.md',
    'core/protocol/PHASE_LIFECYCLE.md',
    'core/protocol/STACKS.md',
    'core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md',
    'core/protocol/VERTICAL_SLICE_AND_STATUS_UX.md',
    'core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md',
    'core/protocol/CURRENT_SYSTEM_STATE.md',
    'core/protocol/REQUIREMENTS.md',
    'core/templates/session/REQUIREMENTS.md',
    'system/accepted-state/REQUIREMENTS.md',
    'docs/2-methodology/requirements-and-coverage.md',
    'core/protocol/AUTONOMOUS_TECHNICAL_PROGRESS.md',
    'core/protocol/LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md',
    'core/templates/session/EVIDENCE.md',
    'core/templates/session/EVIDENCE.md',
    'docs/2-methodology/local-technical-setup-and-role-workflow-smoke-checks.md',
    'core/commands/start.md',
    'core/commands/continue.md',
    'core/commands/status.md',
    'core/commands/close.md',
    'core/templates/session/SESSION_EXECUTION.md',
    'core/templates/session/SESSION_SCOPE.md',
    'core/templates/session/unresolved-items.md',
    'core/templates/session/implementation-units/IU.md',
    'core/templates/system/CURRENT_SYSTEM_STATE.md',
    'core/templates/system/delivery/DELIVERY_PLAN.md',
    'core/templates/system/delivery/DELIVERY_SCOPE.md',
    'core/templates/system/delivery/phases/PHASE.md',
    'core/templates/system/history/sessions/ARCHIVE_MANIFEST.md',
    'core/templates/session/stack-resolution.json',
    'core/templates/session/bootstrap/BOOTSTRAP_REPORT.md',
    'core/templates/session/DESIGN.md',
    'core/templates/session/EVIDENCE.md',
    'session/SESSION_STATE.json',
    'session/implementation-units/.gitkeep',
    'system/accepted-state/CURRENT_SYSTEM_STATE.md',
    'system/accepted-state/CARRY_FORWARD.md',
    'system/accepted-state/DECISION_LOG.md',
    'system/history/sessions/.gitkeep',
    'system/delivery/.gitkeep',
    'docs/README.md',
    'docs/1-use-hirmos/getting-started/installation.md',
    'docs/1-use-hirmos/README.md',
    'docs/1-use-hirmos/getting-started/README.md',
    'docs/1-use-hirmos/getting-started/quickstart.md',
    'docs/1-use-hirmos/getting-started/first-real-run.md',
    'docs/1-use-hirmos/getting-started/commands.md',
    'docs/1-use-hirmos/getting-started/working-with-existing-projects.md',
    'docs/1-use-hirmos/getting-started/multi-session-work.md',
    'docs/2-methodology/README.md',
    'docs/2-methodology/current-state-first.md',
    'docs/2-methodology/unresolved-items.md',
    'docs/2-methodology/evidence-backed-review.md',
    'docs/2-methodology/durable-current-system-state.md',
    'docs/2-methodology/implementation-evidence-and-claim-reconciliation.md',
    'docs/2-methodology/artifact-authority.md',
    'docs/3-extend-contribute/README.md',
    'docs/3-extend-contribute/framework-structure.md',
    'docs/3-extend-contribute/capabilities-and-entrypoints.md',
    'docs/3-extend-contribute/validation.md',
    'docs/reference/README.md',
    'docs/reference/artifact-model.md',
    'docs/reference/cli-reference.md',
    'docs/reference/framework-command-reference.md',
    'docs/reference/integration-tools.md',
    'docs/reference/runtime-surfaces.md',
    'docs/reference/glossary.md',
    'docs/reference/stacks.md',
    'docs/reference/interaction-modes.md',
]
missing = [p for p in required if not (root / p).exists()]
if missing:
    print('FAIL: missing required files:')
    for p in missing:
        print(f'- {p}')
    sys.exit(1)


# CLI init integration-source checks. The terminal CLI depends on this shipped
# registry/templates surface to generate supported AI-tool integration files.
EXPECTED_AGENT_INTEGRATIONS = {'agents','claude','cursor','copilot','codex','opencode','gemini','windsurf','kiro'}
agent_registry_path = root / 'integrations/agent-tools/registry.json'
agent_templates_dir = root / 'integrations/agent-tools/templates'
if not agent_registry_path.exists():
    print('FAIL: missing CLI init integration registry: integrations/agent-tools/registry.json')
    sys.exit(1)
if not agent_templates_dir.is_dir():
    print('FAIL: missing CLI init integration templates directory: integrations/agent-tools/templates')
    sys.exit(1)
try:
    agent_registry = json.loads(agent_registry_path.read_text())
except Exception as exc:
    print(f'FAIL: integration registry is not valid JSON: {exc}')
    sys.exit(1)
actual_integrations = set((agent_registry.get('integrations') or {}).keys())
if actual_integrations != EXPECTED_AGENT_INTEGRATIONS:
    print(f'FAIL: integration registry ids mismatch; expected {sorted(EXPECTED_AGENT_INTEGRATIONS)}, got {sorted(actual_integrations)}')
    sys.exit(1)
managed = agent_registry.get('managed_block') or {}
for integration_id, definition in (agent_registry.get('integrations') or {}).items():
    template_rel = definition.get('template')
    target = definition.get('target')
    mode = definition.get('mode')
    if not template_rel or not target or mode != 'managed_block':
        print(f'FAIL: integration {integration_id} must define target, template, and managed_block mode')
        sys.exit(1)
    template_path = root / 'integrations/agent-tools' / template_rel
    if not template_path.exists():
        print(f'FAIL: integration {integration_id} template missing: integrations/agent-tools/{template_rel}')
        sys.exit(1)
    template_body = template_path.read_text(errors='ignore')
    if managed.get('start') not in template_body or managed.get('end') not in template_body:
        print(f'FAIL: integration {integration_id} template missing managed block markers: {template_rel}')
        sys.exit(1)


# Docs/onboarding checks
readme_body = (root / 'docs/README.md').read_text()
for phrase in ['Use HIRMOS', 'Learn the methodology', 'Extend or contribute', 'Reference']:
    if phrase not in readme_body:
        print(f'FAIL: docs/README.md missing docs lane: {phrase}')
        sys.exit(1)

installed_readme = root / 'README.md'
installed_readme_body = installed_readme.read_text()
for phrase in ['Why HIRMOS exists', 'Simple by default', 'hirmos start', 'Understand System State']:
    if phrase not in installed_readme_body:
        print(f'FAIL: installed _hirmos/README.md missing onboarding phrase: {phrase}')
        sys.exit(1)

for rel, phrases in {
    'docs/1-use-hirmos/getting-started/quickstart.md': ['Bootstrap', 'hirmos start', 'hirmos continue', 'hirmos close'],
    'docs/1-use-hirmos/getting-started/first-real-run.md': ['User Request', 'Understand System State', 'Design', 'Implementation', 'Update System State'],
    'docs/1-use-hirmos/getting-started/working-with-existing-projects.md': ['current-state-first', 'brownfield', 'mixed'],
    'docs/1-use-hirmos/getting-started/multi-session-work.md': ['single-session', 'multi-session', 'DELIVERY_PLAN.md'],
    'docs/2-methodology/current-state-first.md': ['General System State Understanding', 'Focused System State Understanding'],
    'docs/2-methodology/unresolved-items.md': ['continuation-control records', 'Producer Contributions'],
    'docs/reference/artifact-model.md': ['Source inputs', '_hirmos/inputs/', 'inputs/uploads', 'Active session artifacts', 'Accepted system state'],
    'docs/3-extend-contribute/framework-structure.md': ['Public repository surface', 'Framework version metadata', 'Docs vs protocols'],
    'docs/3-extend-contribute/capabilities-and-entrypoints.md': ['Canonical entrypoint surfaces', 'Execution contract'],
    'docs/3-extend-contribute/validation.md': ['Public repository validation', 'Maintainer validation'],
    'docs/reference/cli-reference.md': ['hirmos init [project-path]', '--integration', '--source', '--version', '--offline'],
    'docs/reference/framework-command-reference.md': ['Framework workflow commands', 'hirmos start', 'hirmos continue', 'hirmos close'],
    'docs/reference/integration-tools.md': ['Supported integrations', 'canonical integration registry'],
}.items():
    body = (root / rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: {rel} missing docs phrase: {phrase}')
            sys.exit(1)

# Source inputs surface checks. Inputs are raw source material and remain non-authoritative until reconciled.
for rel in ['inputs/README.md', 'inputs/uploads/README.md', 'inputs/prototypes/README.md', 'inputs/references/README.md']:
    body = (root / rel).read_text(errors='ignore')
    if 'not' not in body.lower() or 'authority' not in body.lower():
        print(f'FAIL: {rel} must state that source inputs are not authority')
        sys.exit(1)

design_method = (root/'extensions/design-agent/entrypoints/default.md').read_text(errors='ignore')
for phrase in ['_hirmos/inputs/', '_hirmos/inputs/uploads/', 'raw source material']:
    if phrase not in design_method:
        print(f'FAIL: design-agent default entrypoint missing source-input surface phrase: {phrase}')
        sys.exit(1)

requirements_design_entrypoint = (root/'extensions/design-agent/capabilities/requirements-design/entrypoints/default.md').read_text(errors='ignore')
for phrase in ['_hirmos/inputs/', '_hirmos/inputs/uploads/', 'DESIGN.md source matrix']:
    if phrase not in requirements_design_entrypoint:
        print(f'FAIL: requirements-design entrypoint missing source-input surface phrase: {phrase}')
        sys.exit(1)

cfg = json.loads((root/'hirmos.config.json').read_text())
expected_version = '1.0.4'
if cfg.get('framework',{}).get('version') != expected_version:
    print('FAIL: framework.version must match expected framework version')
    sys.exit(1)

if 'hirmos start' not in (root/'core/protocol/COMMANDS.md').read_text():
    print('FAIL: COMMANDS.md must define hirmos start')
    sys.exit(1)

beyond_clear_specs = (root/'core/authority/BEYOND_CLEAR_SPECS.md').read_text()
for phrase in ['Clear Specs', 'Strict local self-validation', 'Fail closed on material defects', 'Required controls', 'When not to overapply it']:
    if phrase not in beyond_clear_specs:
        print(f'FAIL: BEYOND_CLEAR_SPECS.md missing preserved doctrine phrase: {phrase}')
        sys.exit(1)

# Guard against references to non-shipping development zones in framework prose.
for term in ['_' + 'internal/', '_' + 'workspace/']:
    for path in root.rglob('*'):
        if path.is_file() and path.suffix in {'.md', '.json'}:
            if term in path.read_text(errors='ignore'):
                print(f'FAIL: shipped file references non-shipping path {term!r}: {path.relative_to(root)}')
                sys.exit(1)


# Command execution and control integrity checks.
session_execution = (root/'core/templates/session/SESSION_EXECUTION.md').read_text()
for phrase in [
    'Command Resolution',
    'Active Execution Controls',
    'Baseline Control Families',
    'Control Self-Validation',
    'Fail-Closed Conditions',
    'Continuation Boundary Log',
    'Route-Back Records',
    'Readiness Gates',
    'SESSION_SCOPE.md',
    'unresolved-items.md',
    'PENDING',
    'BLOCKED',
]:
    if phrase not in session_execution:
        print(f'FAIL: SESSION_EXECUTION.md missing required command/control integrity phrase: {phrase}')
        sys.exit(1)

for cmd in ['start','continue','status','close']:
    p = root/'core/commands'/f'{cmd}.md'
    body = p.read_text()
    for phrase in ['Execution contract', 'Terminal states', 'Required behavior']:
        if phrase.lower() not in body.lower():
            print(f'FAIL: command spec {cmd}.md missing {phrase}')
            sys.exit(1)

if 'Status: core protocol.' not in (root/'core/protocol/COMMANDS.md').read_text():
    print('FAIL: COMMANDS.md protocol status missing')
    sys.exit(1)

command_state_machine = (root/'core/protocol/COMMAND_STATE_MACHINE.md').read_text()
for phrase in [
    'Canonical lifecycle stages',
    'SESSION_STATE.json schema',
    'Command transition matrix',
    'Mandatory start pause rule',
    'Cumulative continue pass model',
    'Exactly-one-next-command rule',
    'Fail-closed command behavior',
]:
    if phrase not in command_state_machine:
        print(f'FAIL: COMMAND_STATE_MACHINE.md missing command-state phrase: {phrase}')
        sys.exit(1)

for rel in ['core/templates/session/SESSION_STATE.json', 'session/SESSION_STATE.json']:
    state_obj = json.loads((root/rel).read_text())
    for field in ['schema_version','status','session_id','lifecycle_stage','continuation_pass','pending_correction','allowed_next_commands','recommended_next_command','blocking_reason','created_at','updated_at']:
        if field not in state_obj:
            print(f'FAIL: {rel} missing SESSION_STATE field: {field}')
            sys.exit(1)
    forbidden_fields = ['session_title', 'active_command', 'last_command']
    for field in forbidden_fields:
        if field in state_obj:
            print(f'FAIL: {rel} contains removed SESSION_STATE field: {field}')
            sys.exit(1)
    if state_obj.get('schema_version') != 'session-state-v1':
        print(f'FAIL: {rel} schema_version must be ')
        sys.exit(1)
    if state_obj.get('status') == 'idle' and state_obj.get('lifecycle_stage') != 'idle':
        print(f'FAIL: {rel} idle status must use lifecycle_stage idle')
        sys.exit(1)
    if state_obj.get('recommended_next_command') not in state_obj.get('allowed_next_commands', []):
        print(f'FAIL: {rel} recommended_next_command must be in allowed_next_commands')
        sys.exit(1)



# command-state semantic enforcement
SUPPORTED_COMMANDS = {'hirmos start', 'hirmos status', 'hirmos continue', 'hirmos close'}
LEGAL_TRANSITIONS = {
    ('idle', 'idle'): {'hirmos start', 'hirmos status'},
    ('active', 'bootstrap'): {'hirmos continue', 'hirmos status'},
    ('active', 'system_state_understanding'): {'hirmos continue', 'hirmos status'},
    ('active', 'session_scope'): {'hirmos continue', 'hirmos status'},
    ('active', 'design'): {'hirmos continue', 'hirmos status'},
    ('active', 'implementation_readiness'): {'hirmos continue', 'hirmos status'},
    ('active', 'implementation'): {'hirmos continue', 'hirmos status'},
    ('active', 'implementation_complete'): {'hirmos close', 'hirmos status', 'hirmos continue'},
    ('active', 'correction_requested'): {'hirmos continue', 'hirmos status'},
    ('active', 'close_ready'): {'hirmos close', 'hirmos status'},
    ('blocked', 'blocked'): {'hirmos status', 'hirmos continue', 'hirmos close'},
}
IDLE_ALLOWED_FILES = {
    Path('.gitkeep'),
    Path('SESSION_STATE.json'),
    Path('bootstrap/.gitkeep'),
    Path('implementation-units/.gitkeep'),
}
ACTIVE_REQUIRED_ROOT_FILES = {
    'SESSION_STATE.json',
    'SESSION_SCOPE.md',
    'SESSION_EXECUTION.md',
    'unresolved-items.md',
}
PROHIBITED_SUPPORT_ARTIFACT_NAMES = {
    'archive-manifest.md',
    'claim-reconciliation.md',
    'close-checklist.md',
    'evidence-review.md',
    'implementation-readiness.md',
    'local-runtime-evidence.md',
    'project-context.md',
    'prototype-ingestion.md',
    'request-intake.md',
    'role-workflow-smoke.md',
    'runtime-integration-readiness.md',
    'SESSION_SCOPE.md close verification',
    'session-implementation-review.md',
    'source-materials.md',
    'system-state-update.md',
    'system-state.md',
    'technical-review.md',
}
DEPRECATED_SESSION_SURFACES = {
    'SESSION_SCOPE_CONTRACT.md',
    'SESSION_SCOPE_REVIEW.md',
    'UNRESOLVED_ITEMS.md',
    'IMPLEMENTATION_UNIT_PLAN.md',
    'IMPLEMENTATION_UNIT_REQUEST.md',
    'IMPLEMENTATION_UNIT_EXECUTION.md',
    'IMPLEMENTATION_UNIT_REVIEW.md',
    'RETRY_REQUEST.md',
}

DEPRECATED_REFERENCE_MARKERS = {
    'SESSION_CONTRACT.md',
    'SESSION_CONTRACT',
    'session_contract',
    'SESSION_SCOPE_CONTRACT',
    'SESSION_SCOPE_REVIEW',
    'CURRENT_STATE_INTAKE',
    'WORK_OBJECTIVE_INFERENCE',
    'CURRENT_SYSTEM_UPDATE_PROPOSAL',
    'CURRENT_SYSTEM_UPDATE_APPLICATION',
    'PROVIDER_COMPOSITION_PLAN',
    'DECISION_SCOPE_ASSESSMENT',
    'IMPLEMENTATION_UNIT_PLAN',
    'IMPLEMENTATION_UNIT_REQUEST',
    'IMPLEMENTATION_UNIT_EXECUTION',
    'IMPLEMENTATION_UNIT_REVIEW',
    'RETRY_REQUEST',
    'ACCEPTED_STATE_INDEX',
    'implementation-units.md',
    'hirmos build',
    'build/status/continue/close',
}

DEPRECATED_REFERENCE_EXEMPT_FILES = {
    Path('tools/validate.py'),
    Path('tools/test_validator_regressions.py'),
}


def _validate_no_deprecated_references_outside_tooling():
    text_suffixes = {'.md', '.json', '.yaml', '.yml', '.txt', '.py'}
    for candidate in root.rglob('*'):
        if not candidate.is_file():
            continue
        rel = candidate.relative_to(root)
        if rel in DEPRECATED_REFERENCE_EXEMPT_FILES:
            continue
        if '.git' in rel.parts or '__pycache__' in rel.parts:
            continue
        if candidate.suffix not in text_suffixes:
            continue
        body = candidate.read_text(errors='ignore')
        for marker in DEPRECATED_REFERENCE_MARKERS:
            if marker in body:
                print(f'FAIL: deprecated artifact/command reference {marker!r} found in {rel}')
                sys.exit(1)


def _validate_strict_necessity_support_surface():
    support_template_dir = root / 'core/templates/session/support'
    if support_template_dir.exists():
        print('FAIL: core/templates/session/support must not exist after support directory removal; use core/templates/session/stack-resolution.json for stack routing state')
        sys.exit(1)

    active_support_dir = root / 'session/support'
    if active_support_dir.exists():
        print('FAIL: session/support must not exist after support directory removal; use session/stack-resolution.json when stack routing state is needed')
        sys.exit(1)

    stack_resolution_template = root / 'core/templates/session/stack-resolution.json'
    if not stack_resolution_template.exists():
        print('FAIL: missing root stack-resolution template: core/templates/session/stack-resolution.json')
        sys.exit(1)

    if (root / 'session/stack-resolution.json').exists():
        try:
            json.loads((root / 'session/stack-resolution.json').read_text())
        except json.JSONDecodeError as exc:
            print(f'FAIL: session/stack-resolution.json is not valid JSON: {exc}')
            sys.exit(1)

def _validate_session_state_semantics(state_path: Path, active_session_dir: Path | None = None):
    state_obj = json.loads(state_path.read_text())
    for removed_field in ['session_title', 'active_command', 'last_command']:
        if removed_field in state_obj:
            print(f'FAIL: {state_path.relative_to(root)} contains removed SESSION_STATE field: {removed_field}')
            sys.exit(1)
    status = state_obj.get('status')
    stage = state_obj.get('lifecycle_stage')
    allowed = state_obj.get('allowed_next_commands')
    recommended = state_obj.get('recommended_next_command')
    blocking_reason = state_obj.get('blocking_reason')
    continuation_pass = state_obj.get('continuation_pass')

    if status not in {'idle', 'active', 'blocked'}:
        print(f'FAIL: {state_path.relative_to(root)} status must be idle, active, or blocked')
        sys.exit(1)
    if stage not in {'idle','bootstrap','system_state_understanding','session_scope','design','implementation_readiness','implementation','implementation_complete','correction_requested','close_ready','closed','blocked'}:
        print(f'FAIL: {state_path.relative_to(root)} lifecycle_stage is not canonical: {stage!r}')
        sys.exit(1)
    if not isinstance(allowed, list) or not allowed:
        print(f'FAIL: {state_path.relative_to(root)} allowed_next_commands must be a non-empty list')
        sys.exit(1)
    if any(cmd not in SUPPORTED_COMMANDS for cmd in allowed):
        print(f'FAIL: {state_path.relative_to(root)} allowed_next_commands contains unsupported command: {allowed}')
        sys.exit(1)
    if recommended not in SUPPORTED_COMMANDS:
        print(f'FAIL: {state_path.relative_to(root)} recommended_next_command is not a supported governed command: {recommended!r}')
        sys.exit(1)
    if recommended not in allowed:
        print(f'FAIL: {state_path.relative_to(root)} recommended_next_command must be included in allowed_next_commands')
        sys.exit(1)
    if not isinstance(continuation_pass, int) or continuation_pass < 0:
        print(f'FAIL: {state_path.relative_to(root)} continuation_pass must be a non-negative integer')
        sys.exit(1)

    if status == 'idle':
        if stage != 'idle':
            print(f'FAIL: {state_path.relative_to(root)} idle status must use lifecycle_stage idle')
            sys.exit(1)
        if state_obj.get('session_id') or blocking_reason:
            print(f'FAIL: {state_path.relative_to(root)} idle state must not retain active session identity or blocking_reason')
            sys.exit(1)
        if continuation_pass != 0 or state_obj.get('pending_correction') is not False:
            print(f'FAIL: {state_path.relative_to(root)} idle state must have continuation_pass 0 and pending_correction false')
            sys.exit(1)
    elif status == 'active':
        if stage in {'idle','closed','blocked'}:
            print(f'FAIL: {state_path.relative_to(root)} active status cannot use lifecycle_stage {stage}')
            sys.exit(1)
        if not state_obj.get('session_id'):
            print(f'FAIL: {state_path.relative_to(root)} active state requires session_id')
            sys.exit(1)
    elif status == 'blocked':
        if stage != 'blocked':
            print(f'FAIL: {state_path.relative_to(root)} blocked status must use lifecycle_stage blocked')
            sys.exit(1)
        if not blocking_reason:
            print(f'FAIL: {state_path.relative_to(root)} blocked state requires blocking_reason')
            sys.exit(1)

    legal = LEGAL_TRANSITIONS.get((status, stage))
    if legal is None:
        print(f'FAIL: {state_path.relative_to(root)} illegal status/lifecycle combination: {status}/{stage}')
        sys.exit(1)
    if not set(allowed).issubset(legal):
        print(f'FAIL: {state_path.relative_to(root)} allowed_next_commands {allowed} are illegal for {status}/{stage}; expected subset of {sorted(legal)}')
        sys.exit(1)
    if stage == 'implementation_readiness' and recommended != 'hirmos continue':
        print(f'FAIL: {state_path.relative_to(root)} implementation_readiness must recommend hirmos continue')
        sys.exit(1)
    if stage == 'implementation_complete' and not state_obj.get('pending_correction') and recommended != 'hirmos close':
        print(f'FAIL: {state_path.relative_to(root)} implementation_complete without pending_correction must recommend hirmos close')
        sys.exit(1)

    if active_session_dir is not None and active_session_dir.exists():
        all_files = {p.relative_to(active_session_dir) for p in active_session_dir.rglob('*') if p.is_file()}
        root_files = {p.name for p in active_session_dir.iterdir() if p.is_file()}
        deprecated_present = sorted(DEPRECATED_SESSION_SURFACES.intersection(root_files))
        if deprecated_present:
            print(f'FAIL: deprecated session artifact(s) present: {deprecated_present}')
            sys.exit(1)
        if status == 'idle':
            stale = sorted(str(p) for p in all_files - IDLE_ALLOWED_FILES)
            if stale:
                print('FAIL: idle session contains stale active-session artifacts:')
                for item in stale:
                    print(f'- session/{item}')
                sys.exit(1)
            for required_idle in IDLE_ALLOWED_FILES:
                if not (active_session_dir / required_idle).exists():
                    print(f'FAIL: idle session scaffold missing required sentinel: session/{required_idle}')
                    sys.exit(1)
        elif status == 'active':
            missing_active = sorted(name for name in ACTIVE_REQUIRED_ROOT_FILES if not (active_session_dir/name).exists())
            if missing_active:
                print(f'FAIL: active session missing canonical root artifact(s): {missing_active}')
                sys.exit(1)
            for dirname in ['implementation-units','bootstrap']:
                if not (active_session_dir/dirname).is_dir():
                    print(f'FAIL: active session missing canonical directory: session/{dirname}')
                    sys.exit(1)

_validate_session_state_semantics(root/'core/templates/session/SESSION_STATE.json')
_validate_session_state_semantics(root/'session/SESSION_STATE.json', root/'session')


# delivery governance semantic enforcement
def _read_optional_text(path: Path) -> str:
    return path.read_text(errors='ignore') if path.exists() else ''


def _extract_hirmos_path(body: str, pattern: str) -> str | None:
    match = re.search(pattern, body)
    return match.group(0) if match else None


def _canonicalize_hirmos_path(path_text: str | None) -> Path | None:
    if not path_text:
        return None
    p = path_text.strip().strip('`').lstrip('/')
    if p.startswith('_hirmos/'):
        p = p[len('_hirmos/'):]
    return Path(p)


def _extract_label_value(body: str, label: str) -> str | None:
    patterns = [
        rf'^{re.escape(label)}\s*:\s*([^\n|]+)',
        rf'\|\s*{re.escape(label)}\s*\|\s*([^|\n]+)\|',
    ]
    for pattern in patterns:
        match = re.search(pattern, body, re.I | re.M)
        if match:
            value = match.group(1).strip().strip('`')
            if value:
                return value.split()[0].strip('`').strip()
    return None


def _field_has_concrete_value(body: str, label: str) -> bool:
    pattern = rf'^{re.escape(label)}[^\S\n]*:[^\S\n]*(.+)$'
    for match in re.finditer(pattern, body, re.I | re.M):
        value = match.group(1).strip()
        if value and value.upper() not in {'PENDING','TODO','TBD','UNKNOWN','NOT_ASSESSED'}:
            return True
    # Also allow table rows where the actual-result column is PASS.
    row_pattern = rf'\|\s*[^|]*{re.escape(label)}[^|]*\|[^|]*\|\s*PASS\s*\|'
    return bool(re.search(row_pattern, body, re.I))



def _has_recorded_carry_forward(body: str) -> bool:
    if re.search(r'Carry-forward status\s*:\s*RECORDED', body, re.I):
        return True
    if re.search(r'Carry-forward (delivery obligations|required)\s*:\s*(yes|recorded)', body, re.I):
        return True
    if re.search(r'Carry-forward target\s*:\s*(?!\s*$).+', body, re.I | re.M):
        return True
    # Accept a non-empty table row under a carry-forward section in fixture/docs contexts.
    if re.search(r'\|\s*[^|\s][^|]*\|\s*(OPEN|PARTIAL|BLOCKED|DEFERRED)', body, re.I):
        return True
    return False


def _extract_resulting_phase_status(system_state_update: str, phase_body: str) -> str | None:
    for label in ['Resulting phase lifecycle status', 'New lifecycle status', 'Resulting lifecycle status']:
        value = _extract_label_value(system_state_update, label)
        if value:
            return value
    value = _extract_label_value(phase_body, 'Lifecycle status')
    return value


def _validate_phase_progress_carry_forward(phase_rel: Path, stage: str | None, close_controls: str, session_execution: str, session_review: str) -> None:
    if stage not in {'implementation_complete', 'close_ready'}:
        return
    phase_body = _read_optional_text(root / phase_rel)
    if 'Phase Progress Ledger' not in phase_body:
        print('FAIL: phase progress missing Phase Progress Ledger in durable phase')
        sys.exit(1)
    if ' Phase Progress / Carry-Forward Record' not in session_execution:
        print('FAIL: phase progress missing carry-forward record in SESSION_EXECUTION.md')
        sys.exit(1)
    if ' Phase Progress / Carry-Forward Review' not in session_review:
        print('FAIL: phase progress missing carry-forward review in SESSION_SCOPE.md close verification')
        sys.exit(1)

    resulting_status = _extract_resulting_phase_status(close_controls, phase_body)
    if resulting_status in {'PARTIAL', 'BLOCKED', 'DEFERRED'}:
        if re.search(r'Carry-forward required\s*:\s*yes', close_controls, re.I) and not re.search(r'Carry-forward status\s*:\s*RECORDED', close_controls, re.I):
            print(f'FAIL: phase progress {resulting_status} outcome missing carry-forward obligations')
            sys.exit(1)
        combined = '\n'.join([close_controls, phase_body, session_review])
        if not _has_recorded_carry_forward(combined):
            print(f'FAIL: phase progress {resulting_status} outcome missing carry-forward obligations')
            sys.exit(1)
    if resulting_status == 'ACCEPTED':
        # Accepted is allowed, but accepted status must not coexist with unresolved carry-forward required markers.
        if re.search(r'Carry-forward required\s*:\s*yes', close_controls, re.I) and not _has_recorded_carry_forward(close_controls):
            print('FAIL: phase progress accepted outcome contradicts required carry-forward without recorded target')
            sys.exit(1)


def _validate_phase_acceptance_enforcement(phase_rel: Path, stage: str | None, close_controls: str, session_execution: str, session_review: str) -> None:
    if stage not in {'implementation_complete', 'close_ready'}:
        return
    phase_body = _read_optional_text(root / phase_rel)
    resulting_status = _extract_resulting_phase_status(close_controls, phase_body)
    if resulting_status != 'ACCEPTED':
        return

    phase_type = _extract_label_value(phase_body, 'Phase type') or 'UNKNOWN'
    combined = '\n'.join([phase_body, close_controls, session_execution, session_review])

    required_pairs = [
        ('phase body', phase_body, ' Phase Acceptance Evidence Gate'),
        ('session execution', session_execution, ' Phase Acceptance Enforcement Record'),
        ('session scope review', session_review, ' Phase Acceptance Review'),
        ('close controls', close_controls, ' Phase Acceptance Transaction'),
    ]
    for label, body, phrase in required_pairs:
        if phrase not in body:
            print(f'FAIL: phase acceptance accepted outcome missing {phrase} in {label}')
            sys.exit(1)

    acceptance_complete = any(re.search(pattern, combined, re.I) for pattern in [
        r'Phase acceptance evidence status\s*:\s*COMPLETE',
        r'Acceptance gate status\s*:\s*PASS',
        r'Phase acceptance status\s*:\s*ACCEPTED',
    ])
    if not acceptance_complete:
        print('FAIL: phase acceptance accepted outcome missing complete acceptance evidence')
        sys.exit(1)

    if not re.search(r'Phase acceptance verdict\s*:\s*ACCEPTED', session_review, re.I):
        print('FAIL: phase acceptance accepted outcome missing ACCEPTED verdict in SESSION_SCOPE.md close verification')
        sys.exit(1)

    if re.search(r'Unresolved adopted work remaining\s*:\s*yes', combined, re.I):
        print('FAIL: phase acceptance accepted outcome has unresolved adopted work remaining')
        sys.exit(1)
    remaining_work = _extract_label_value(close_controls, 'Remaining adopted work')
    if remaining_work and remaining_work not in {'NONE', 'DEFERRED_WITH_RATIONALE'}:
        print('FAIL: phase acceptance accepted outcome has remaining adopted work not reconciled')
        sys.exit(1)

    if phase_type in {'GREENFIELD', 'MIXED'}:
        if not re.search(r'Greenfield acceptance evidence\s*:\s*COMPLETE', combined, re.I):
            print('FAIL: greenfield phase acceptance missing COMPLETE greenfield acceptance evidence')
            sys.exit(1)
    if phase_type in {'BROWNFIELD', 'MIXED'}:
        if not re.search(r'Brownfield acceptance evidence\s*:\s*COMPLETE', combined, re.I):
            print('FAIL: brownfield phase acceptance missing COMPLETE brownfield acceptance evidence')
            sys.exit(1)



def _validate_phase_lifecycle_status_report(session_execution: str) -> None:
    if ' Phase Lifecycle Status Report Record' not in session_execution:
        return
    section = session_execution.split(' Phase Lifecycle Status Report Record', 1)[1]
    section = section.split('\n## ', 1)[0]
    required_labels = [
        'Phase lifecycle status',
        'Phase type',
        'Phase Entry Gate status',
        'Phase Progress Ledger status',
        'Carry-forward status',
        'Phase Acceptance Evidence Gate status',
        'Greenfield status group',
        'Brownfield status group',
        'Status Blocked By Phase Lifecycle Conflict',
        'Exactly one recommended next command',
    ]
    for label in required_labels:
        if not _field_has_concrete_value(section, label):
            print(f'FAIL: Phase Lifecycle Status Report missing required field: {label}')
            sys.exit(1)
    next_match = re.search(r'^Exactly one recommended next command\s*:\s*(hirmos (?:start|status|continue|close))\s*$', section, re.I | re.M)
    if not next_match or next_match.group(1).lower() not in SUPPORTED_COMMANDS:
        print('FAIL: Phase Lifecycle Status Report must contain exactly one supported governed next command')
        sys.exit(1)


def _validate_phase_entry_gate(phase_text_path: str, phase_rel: Path, stage: str | None) -> None:
    phase_body = _read_optional_text(root / phase_rel)
    lifecycle_status = _extract_label_value(phase_body, 'Lifecycle status')
    phase_type = _extract_label_value(phase_body, 'Phase type')

    if stage != 'implementation_readiness':
        return

    if not lifecycle_status:
        print('FAIL: phase entry gate missing lifecycle status')
        sys.exit(1)
    if lifecycle_status not in {'READY_FOR_ADOPTION', 'ACTIVE', 'PARTIAL'}:
        print(f'FAIL: phase entry gate lifecycle status does not support implementation adoption: {lifecycle_status}')
        sys.exit(1)

    if not phase_type:
        print('FAIL: phase entry gate missing phase type')
        sys.exit(1)
    if phase_type == 'UNKNOWN':
        print('FAIL: phase entry gate UNKNOWN phase type blocks implementation readiness')
        sys.exit(1)
    if phase_type not in {'GREENFIELD', 'BROWNFIELD', 'MIXED'}:
        print(f'FAIL: phase entry gate non-canonical phase type: {phase_type}')
        sys.exit(1)

    if ' Phase Entry Gate' not in phase_body and 'Phase Entry Gate' not in phase_body:
        print('FAIL: delivery-governed active session missing Phase Entry Gate in durable phase')
        sys.exit(1)
    if not re.search(r'Entry gate status\s*:\s*PASS', phase_body, re.I):
        print('FAIL: phase entry gate status must be PASS before implementation_readiness')
        sys.exit(1)
    if not re.search(r'Entry criteria (status|satisfied)\s*:\s*(SATISFIED|PASS|YES)', phase_body, re.I):
        print('FAIL: phase entry gate entry criteria satisfied evidence is missing')
        sys.exit(1)

    if phase_type in {'GREENFIELD', 'MIXED'}:
        for label in ['MVP boundary', 'Primary user/workflow slice', 'Architecture dependency status', 'Out-of-scope expansion guard']:
            if not _field_has_concrete_value(phase_body, label):
                print(f'FAIL: greenfield phase entry gate missing concrete control: {label}')
                sys.exit(1)
    if phase_type in {'BROWNFIELD', 'MIXED'}:
        for label in ['Preservation baseline', 'Affected existing surfaces', 'Regression-sensitive behavior', 'Do-not-touch boundaries']:
            if not _field_has_concrete_value(phase_body, label):
                print(f'FAIL: brownfield phase entry gate missing concrete control: {label}')
                sys.exit(1)


def _validate_delivery_governance_active_session(active_session_dir: Path) -> None:
    state_path = active_session_dir / 'SESSION_STATE.json'
    if not state_path.exists():
        return
    state_obj = json.loads(state_path.read_text())
    if state_obj.get('status') != 'active':
        return

    stage = state_obj.get('lifecycle_stage')
    session_scope = _read_optional_text(active_session_dir / 'SESSION_SCOPE.md')
    current_state = _read_optional_text(root / 'system/accepted-state/CURRENT_SYSTEM_STATE.md')
    session_execution = _read_optional_text(active_session_dir / 'SESSION_EXECUTION.md')
    evidence_text = _read_optional_text(active_session_dir / 'EVIDENCE.md')
    session_review = session_scope
    close_controls = '\n'.join([session_execution, evidence_text, session_scope])

    classification_yes = bool(re.search(r'(Answer|Classification answer|Delivery governance active)\s*:\s*YES', session_scope, re.I))
    classification_uncertain = bool(re.search(r'(Answer|Classification answer|Delivery governance active)\s*:\s*UNCERTAIN', session_scope, re.I))

    if stage == 'implementation_readiness' and classification_uncertain:
        print('FAIL: Delivery-Need Classification UNCERTAIN cannot reach implementation_readiness')
        sys.exit(1)

    if not classification_yes:
        return

    if 'Active Durable Phase Adoption' not in session_scope or not re.search(r'Adoption status\s*:\s*ADOPTED|Phase adoption\s*:\s*ADOPTED|ADOPTED', session_scope, re.I):
        print('FAIL: delivery-governed active session missing adopted durable phase evidence in SESSION_SCOPE.md')
        sys.exit(1)

    if re.search(r'_hirmos/system/delivery/[A-Za-z0-9._-]+/DELIVERY_PLAN\.md', session_scope):
        print('FAIL: delivery-governed active session cites legacy per-delivery DELIVERY_PLAN.md; use durable roadmap/register _hirmos/system/delivery/DELIVERY_PLAN.md')
        sys.exit(1)

    plan_text_path = _extract_hirmos_path(session_scope, r'_hirmos/system/delivery/DELIVERY_PLAN\.md')
    scope_text_path = _extract_hirmos_path(session_scope, r'_hirmos/system/delivery/[A-Za-z0-9._-]+/DELIVERY_SCOPE\.md')
    phase_text_path = _extract_hirmos_path(session_scope, r'_hirmos/system/delivery/[A-Za-z0-9._-]+/phases/PHASE-[A-Za-z0-9._-]+\.md')
    plan_rel = _canonicalize_hirmos_path(plan_text_path)
    scope_rel = _canonicalize_hirmos_path(scope_text_path)
    phase_rel = _canonicalize_hirmos_path(phase_text_path)

    if plan_rel is None or scope_rel is None or phase_rel is None:
        print('FAIL: delivery-governed active session must cite durable Delivery Plan, Delivery Scope, and Phase paths')
        sys.exit(1)
    if not (root / plan_rel).exists():
        print(f'FAIL: delivery-governed active session missing durable plan: {plan_text_path}')
        sys.exit(1)
    if not (root / scope_rel).exists():
        print(f'FAIL: delivery-governed active session missing durable delivery scope: {scope_text_path}')
        sys.exit(1)
    if not (root / phase_rel).exists():
        print(f'FAIL: delivery-governed active session missing durable phase: {phase_text_path}')
        sys.exit(1)

    _validate_phase_entry_gate(phase_text_path, phase_rel, stage)
    _validate_phase_lifecycle_status_report(session_execution)
    _validate_phase_progress_carry_forward(phase_rel, stage, close_controls, session_execution, session_review)
    _validate_phase_acceptance_enforcement(phase_rel, stage, close_controls, session_execution, session_review)

    if plan_text_path not in current_state or scope_text_path not in current_state or phase_text_path not in current_state:
        print('FAIL: delivery pointer mismatch between SESSION_SCOPE.md and CURRENT_SYSTEM_STATE.md')
        sys.exit(1)

    if stage in {'implementation_complete', 'close_ready'}:
        if 'Close-Time Delivery / Phase Status Transaction' not in close_controls:
            print('FAIL: delivery close missing status transaction in SESSION_EXECUTION.md or EVIDENCE.md')
            sys.exit(1)
        if not re.search(r'DELIVERY_STATUS_UPDATE_APPLIED|DELIVERY_STATUS_UNCHANGED_VERIFIED', close_controls):
            print('FAIL: delivery close status transaction must record applied or unchanged verification')
            sys.exit(1)


_validate_delivery_governance_active_session(root/'session')

for rel, phrases in {
    'core/protocol/COMMAND_STATE_MACHINE.md': ['Validator obligations', 'legal command transition matrix', 'active/idle session folder consistency', 'recommended command legality'],
    'core/templates/session/SESSION_EXECUTION.md': ['Machine Command State Concordance', 'Ledger Integrity Self-Validation', 'Continuation Pass Register', 'Control Mutation Ledger'],
    'core/commands/start.md': ['Command-state gate', 'Fail-Closed', 'Mandatory implementation-readiness pause'],
    'core/commands/continue.md': ['Command-state gate', 'append a new continuation pass record', 'Fail-Closed'],
    'core/commands/close.md': ['Command-state gate', 'stale active-session artifacts', 'Close Blocked'],
    'core/commands/status.md': ['Command-state reporting', 'without mutating files'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: command-state enforcement surface {rel} missing {phrase}')
            sys.exit(1)


_validate_no_deprecated_references_outside_tooling()
_validate_strict_necessity_support_surface()
regression_runner = (root/'tools/test_validator_regressions.py').read_text()
regression_docs = (root/'tools/fixtures/README.md').read_text()
for phrase in [
    'Regression fixtures for HIRMOS command-state validation',
    'idle stale SESSION_SCOPE',
    'unsupported legacy command',
    'accepted-state index reappears',
]:
    if phrase not in regression_runner:
        print(f'FAIL: validator regression runner missing fixture phrase: {phrase}')
        sys.exit(1)
for phrase in [
    'HIRMOS Validator Regression Fixtures',
    'valid baseline passes validation',
    'idle session with stale active artifacts fails',
    'legacy accepted-state index files must not reappear',
]:
    if phrase not in regression_docs:
        print(f'FAIL: validator fixtures README missing phrase: {phrase}')
        sys.exit(1)

print('PASS: HIRMOS validator fixture static check')

print('PASS: HIRMOS command-state semantic enforcement static check')

for rel, phrases in {
    'core/protocol/COMMANDS.md': ['Command state machine discipline', ' command protocol application', 'Mandatory start pause rule', 'Cumulative continue pass rule', 'Exactly-one-next-command rule'],
    'core/commands/start.md': ['Mandatory implementation-readiness pause', 'must not begin implementation during `hirmos start`'],
    'core/commands/continue.md': ['Cumulative continuation pass model', 'append a new continuation pass record'],
    'core/commands/status.md': ['Command-state reporting'],
    'core/commands/close.md': ['Command-state close transition'],
    'core/templates/session/SESSION_EXECUTION.md': ['Machine Command State Concordance', 'Continuation Pass Register', 'Exactly-one-next-command rule'],
    'core/templates/session/SESSION_SCOPE.md': ['Scope Amendments'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: command-state integration: {rel} missing {phrase}')
            sys.exit(1)



# Artifact template quality checks after governance-tax cleanup

_session_execution_template = (root/'core/templates/session/SESSION_EXECUTION.md').read_text()
if _session_execution_template.count('## Current Continuation Snapshot') != 1:
    print('FAIL: SESSION_EXECUTION.md must contain exactly one Current Continuation Snapshot section')
    sys.exit(1)
if _session_execution_template.find('## Current Continuation Snapshot') > _session_execution_template.find('## Command Resolution'):
    print('FAIL: Current Continuation Snapshot must appear before Command Resolution')
    sys.exit(1)
if 'Next safe governed command' not in _session_execution_template or 'What the next model must not do' not in _session_execution_template:
    print('FAIL: Current Continuation Snapshot must preserve next-command and must-not-do continuation controls')
    sys.exit(1)
_design_template = (root/'core/templates/session/DESIGN.md').read_text()
if _design_template.count('## Runtime Integration and Production Readiness Design') != 1:
    print('FAIL: DESIGN.md must contain exactly one Runtime Integration and Production Readiness Design heading')
    sys.exit(1)
_contract_template = (root/'core/templates/session/SESSION_SCOPE.md').read_text()
_nonblank_contract = [line.strip() for line in _contract_template.splitlines() if line.strip()]
if len(_nonblank_contract) < 4 or _nonblank_contract[1] != 'Status: active-session Main Artifact.':
    print('FAIL: SESSION_SCOPE.md must place status/purpose before delivery-shape sections')
    sys.exit(1)
_unresolved_template = (root/'core/templates/session/unresolved-items.md').read_text()
if 'including `NON_GATING` items' not in _unresolved_template or 'Non-gating items are governed decisions or assumptions' not in _unresolved_template:
    print('FAIL: unresolved-items.md must preserve full-detail treatment for material non-gating items')
    sys.exit(1)


# command protocol update checks
for rel, phrases in {
    'core/commands/start.md': ['Command-state gate', 'Required state mutation', 'status` is `idle`', 'final start state'],
    'core/commands/continue.md': ['Command-state gate', 'Required state mutation', 'increment `SESSION_STATE.json.continuation_pass`', 'bare `hirmos continue` is rejected'],
    'core/commands/status.md': ['Command-state gate', 'without mutating files', 'recommended_next_command'],
    'core/commands/close.md': ['Command-state gate', 'Required state mutation', 'archived `SESSION_STATE.json` normalized', 'stale active-session artifacts'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: command protocol update: {rel} missing {phrase}')
            sys.exit(1)

# Contract-centered session spine checks
for rel, phrases in {
}.items():
    body = (root / rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: {rel} missing contract-centered spine phrase: {phrase}')
            sys.exit(1)

state = json.loads((root / 'session/SESSION_STATE.json').read_text())
if 'allowed_next_commands' not in state or 'recommended_next_command' not in state:
    print('FAIL: session/SESSION_STATE.json missing command-state fields')
    sys.exit(1)



# durable delivery governance checks
for rel, phrases in {
    'core/protocol/DELIVERY_GOVERNANCE.md': ['Delivery Shape Decision Gate', 'smallest sufficient governed delivery shape', 'SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS', 'DELIVERY_SCOPE.md'],
    'core/templates/system/delivery/DELIVERY_PLAN.md': ['Delivery Shape Source', 'Delivery Index', 'Delivery Coverage Matrix', 'Status Update Log'],
    'core/templates/system/delivery/DELIVERY_SCOPE.md': ['Authorized Outcome', 'Scoped Requirements', 'Production-Shaped Engineering Gate', 'Delivery Close Verification'],
    'core/templates/system/delivery/phases/PHASE.md': ['Phase Contract', 'Source Delivery Scope', 'Binary Exit Criteria', 'Session Handoff'],
    'core/templates/session/SESSION_SCOPE.md': ['Delivery Shape Decision', 'smallest sufficient governed delivery shape', 'Selected shape justification'],
    'core/templates/session/SESSION_EXECUTION.md': ['Delivery Shape Decision Gate Execution', 'Gate status: PASS | BLOCKED | NOT_ASSESSED'],
    'core/protocol/PROJECT_TYPES.md': ['Delivery shape fields', 'Delivery governance required: YES / NO / UNCERTAIN'],
    'core/protocol/COMMAND_STATE_MACHINE.md': ['Delivery Shape Decision state gate', 'must not recommend `hirmos continue`'],
    'core/commands/start.md': ['Delivery Shape Decision Gate', 'smallest governed delivery shape'],
    'core/templates/system/CURRENT_SYSTEM_STATE.md': ['Active Development Context', 'Delivery roadmap:', 'Active delivery scope:', 'Active phase:'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: delivery governance surface {rel} missing {phrase}')
            sys.exit(1)

for forbidden in ['core/templates/session/DELIVERY_PLAN.md','core/templates/session/DELIVERY_STATUS.md','core/templates/session/PHASE_PLAN.md','core/templates/session/PHASE_CONTRACT.md','core/templates/session/DELIVERY_UNIT_CONTRACT.md']:
    if (root/forbidden).exists():
        print(f'FAIL: session-local delivery template must not remain canonical: {forbidden}')
        sys.exit(1)



# delivery / phase capability rewire checks
for rel, phrases in {
    'core/protocol/DELIVERY_GOVERNANCE.md': ['Delivery / Phase Capability Routing', 'delivery-design → phase-contracting → session-scope → implementation-readiness', 'single-session safety evidence'],
    'extensions/design-agent/extension.json': ['phase-contracting', 'session-scope'],
    'extensions/design-agent/entrypoints/default.md': ['Durable Delivery / Phase Capability Rewire', 'delivery-design', 'phase-contracting', 'session-scope', 'implementation-readiness'],
    'extensions/design-agent/capabilities/delivery-design/capability.json': ['Delivery Shape Decision selects a durable delivery shape', '_hirmos/system/delivery/DELIVERY_PLAN.md', '_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md'],
    'extensions/design-agent/capabilities/phase-contracting/capability.json': ['_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md', '_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md', 'session-scope source-readiness control'],
    'extensions/design-agent/capabilities/session-scope/capability.json': ['durable phase', 'single-session safety evidence'],
    'extensions/design-agent/capabilities/implementation-readiness/capability.json': ['durable delivery coverage when required', 'Delivery Shape Decision gate'],
    'core/templates/session/SESSION_EXECUTION.md': ['Delivery / Phase Capability Routing Log', 'delivery-design', 'phase-contracting', 'session-scope', 'implementation-readiness'],
    'core/templates/session/SESSION_SCOPE.md': ['Delivery / Phase Capability Routing Evidence', 'delivery-design', 'phase-contracting', 'implementation-readiness'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: delivery capability rewire {rel} missing {phrase}')
            sys.exit(1)

for forbidden_rel in [
    'extensions/design-agent/capabilities/session-scope-contract',
    'extensions/design-agent/capabilities/phase-planning',
]:
    if (root/forbidden_rel).exists():
        print(f'FAIL: removed pre-delivery-capability-alignment design capability path still exists: {forbidden_rel}')
        sys.exit(1)

for forbidden in ['session-scope-contract', 'phase-planning']:
    for path in [root/'extensions/design-agent', root/'core/protocol/DELIVERY_GOVERNANCE.md']:
        paths = path.rglob('*') if path.is_dir() else [path]
        for candidate in paths:
            if candidate.is_file() and candidate.suffix in {'.md','.json'}:
                if forbidden in candidate.read_text(errors='ignore'):
                    print(f'FAIL: deprecated delivery capability reference {forbidden!r}: {candidate.relative_to(root)}')
                    sys.exit(1)

print('PASS: HIRMOS delivery / phase capability rewire static check')


# Current System State delivery pointer integration checks
for rel, phrases in {
    'core/templates/system/CURRENT_SYSTEM_STATE.md': ['Active Development Context and Delivery Pointers', 'Delivery governance active', 'Active phase lifecycle status', 'Active phase type', 'Next recommended delivery', 'Next recommended delivery scope', 'Next recommended phase', 'Pointer update rules'],
    'system/accepted-state/CURRENT_SYSTEM_STATE.md': ['Active Development Context and Delivery Pointers', 'Delivery governance active', 'Active phase lifecycle status', 'Active phase type', 'Next recommended delivery', 'Next recommended delivery scope', 'Next recommended phase'],
    'core/protocol/CURRENT_SYSTEM_STATE.md': ['Active Development Context and Delivery Pointers', 'Required pointer fields', 'Next recommended delivery', 'Future sessions must read these pointers'],
    'core/protocol/DELIVERY_GOVERNANCE.md': ['Current System State pointer rule', 'Required pointer fields', 'Next recommended delivery', 'Close-time pointer update is mandatory', 'hirmos start` and Understand System State must inspect these pointers', 'project-type neutral'],
    'core/templates/session/SESSION_SCOPE.md': ['Current System State delivery pointer basis', 'Next recommended delivery', 'Pointer consistency result'],
    'core/templates/session/SESSION_EXECUTION.md': ['Current System State Delivery Pointer Concordance', 'Next recommended delivery', 'delivery-governed implementation must not proceed'],
    'core/commands/start.md': ['Current System State Delivery Pointer Precheck', 'Next recommended delivery', 'must not default to a single-session path'],
    'core/commands/status.md': ['Durable Delivery Pointer Reporting', 'Next recommended delivery', 'Status Blocked By Delivery Pointer Conflict'],
    'core/commands/continue.md': ['Durable Delivery Pointer Concordance', 'Next recommended delivery', 'delivery governance reconciliation'],
    'core/commands/close.md': ['Durable Delivery Pointer Close Requirement', 'Next recommended delivery', 'Close is blocked if'],
    'docs/2-methodology/durable-current-system-state.md': ['Active delivery pointers', 'Future sessions must inspect these pointers'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: current-system-state delivery pointer integration {rel} missing {phrase}')
            sys.exit(1)

print('PASS: HIRMOS current-system-state delivery pointer integration static check')


# Session Scope durable phase adoption enforcement checks
for rel, phrases in {
    'core/protocol/DELIVERY_GOVERNANCE.md': ['Durable Phase Adoption Rule', 'adopt exactly one durable phase file', 'Adoption status: ADOPTED / NOT_APPLICABLE / BLOCKED', 'multiple adopted active phase files'],
    'core/templates/session/SESSION_SCOPE.md': ['Active Durable Phase Adoption', 'Does `SESSION_SCOPE.md` adopt exactly one active durable `PHASE-xx.md`', 'Adopted phase scope', 'Phase exclusions / deferrals'],
    'core/templates/session/SESSION_EXECUTION.md': ['Durable Phase Adoption Gate', 'Exactly one durable phase adopted', 'Phase items mapped to Session Scope items'],
    'core/commands/start.md': ['Durable Phase Adoption Pre-Implementation Gate', 'adopts exactly one durable phase file'],
    'core/commands/continue.md': ['Durable Phase Adoption Continuation Check', 'must not silently switch to a different phase'],
    'core/commands/status.md': ['Durable Phase Adoption Status Reporting', 'Status must not imply implementation authorization'],
    'core/commands/close.md': ['Durable Phase Adoption Close Requirement', 'one adopted phase in `SESSION_SCOPE.md`'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: session scope phase adoption enforcement {rel} missing {phrase}')
            sys.exit(1)

print('PASS: HIRMOS session scope phase adoption enforcement static check')

# Close-time Delivery Plan / Phase status update enforcement checks
for rel, phrases in {
    'core/protocol/DELIVERY_GOVERNANCE.md': ['Close-Time Delivery Plan / Phase Status Update Enforcement', 'Required close-time status authority chain', 'Close is blocked if Delivery Plan status'],
    'core/templates/system/delivery/DELIVERY_PLAN.md': ['Close-Time Delivery Status Update Contract', 'Delivery Status Update Log'],
    'core/templates/system/delivery/DELIVERY_SCOPE.md': ['Delivery Close Verification', 'Session Adoption Rules', 'Phase Plan'],
    'core/templates/system/delivery/phases/PHASE.md': ['Close-Time Phase Status Update Contract', 'Phase Acceptance Review records the closed session', 'Binary Exit Criterion'],
    'core/templates/session/SESSION_EXECUTION.md': [' Close-Time Delivery Status Execution Log', 'durable delivery status updates remain pending'],
    'core/templates/system/CURRENT_SYSTEM_STATE.md': [' Close-Time Delivery Pointer Refresh Rule', 'explicitly verified unchanged'],
    'core/protocol/CURRENT_SYSTEM_STATE.md': [' Close-Time Delivery Pointer Refresh', 'not refreshed or explicitly verified unchanged'],
    'core/commands/close.md': [' Durable Delivery Status Close Requirement', 'update durable delivery status before normal close success', 'archive manifest may record the transaction'],
    'core/commands/status.md': [' Delivery Status Concordance Reporting', 'Status Blocked By Delivery Status Conflict'],
    'core/commands/continue.md': [' Delivery Status Continuation Guard', 'route back to delivery status reconciliation'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: close-time delivery status enforcement {rel} missing {phrase}')
            sys.exit(1)

print('PASS: HIRMOS close-time delivery plan / phase status update enforcement static check')


# Phase lifecycle state model and template checks
for rel, phrases in {
    'core/protocol/PHASE_LIFECYCLE.md': ['Current-State-First Principle', 'Canonical Phase Lifecycle Statuses', 'Canonical Phase Types', 'UNKNOWN` blocks implementation readiness', 'Universal Phase Lifecycle Fields', 'Type-Specific Control Groups', ' Fail-Closed Rules'],
    'core/protocol/DELIVERY_GOVERNANCE.md': ['Phase Lifecycle State Model', 'Lifecycle status: NOT_STARTED | READY_FOR_ADOPTION | ACTIVE | BLOCKED | PARTIAL | READY_FOR_ACCEPTANCE | ACCEPTED | DEFERRED | SUPERSEDED | CANCELLED', 'Phase type: GREENFIELD | BROWNFIELD | MIXED | UNKNOWN', 'Greenfield phases activate', 'Brownfield phases activate', 'Mixed phases activate both control groups'],
    'core/templates/system/delivery/DELIVERY_SCOPE.md': ['Phase Plan', 'READY_FOR_ADOPTION', 'READY_FOR_ACCEPTANCE', 'DEFERRED', 'CANCELLED'],
    'core/templates/system/delivery/phases/PHASE.md': [' Phase Lifecycle State Model', 'Current-State Basis', 'Universal Lifecycle Requirements', 'Greenfield Controls', 'Brownfield Controls', 'Mixed Phase Rule', 'Carry-Forward Items', 'Lifecycle status: NOT_STARTED'],
    'core/templates/system/CURRENT_SYSTEM_STATE.md': [' Phase Lifecycle Pointer Rule', 'Active phase lifecycle status', 'Active phase type', 'UNKNOWN phase type must not support implementation readiness'],
    'system/accepted-state/CURRENT_SYSTEM_STATE.md': [' Phase Lifecycle Pointer Rule', 'Active phase lifecycle status', 'Active phase type', 'UNKNOWN phase type must not support implementation readiness'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: phase lifecycle state model/template {rel} missing {phrase}')
            sys.exit(1)

phase_template = (root/'core/templates/system/delivery/phases/PHASE.md').read_text()
for status in ['NOT_STARTED','READY_FOR_ADOPTION','ACTIVE','BLOCKED','PARTIAL','READY_FOR_ACCEPTANCE','ACCEPTED','DEFERRED','SUPERSEDED','CANCELLED']:
    if status not in phase_template:
        print(f'FAIL: PHASE.md missing canonical lifecycle status: {status}')
        sys.exit(1)
for phase_type in ['GREENFIELD','BROWNFIELD','MIXED','UNKNOWN']:
    if phase_type not in phase_template:
        print(f'FAIL: PHASE.md missing canonical phase type: {phase_type}')
        sys.exit(1)
print('PASS: HIRMOS phase lifecycle state model and templates static check')


# Phase Entry Gate enforcement checks
for rel, phrases in {
    'core/protocol/PHASE_LIFECYCLE.md': [' Phase Entry Gate Enforcement', 'Universal Phase Entry Gate Checks', 'Greenfield Phase Entry Gate', 'Brownfield Phase Entry Gate', 'Mixed Phase Entry Gate', ' Fail-Closed Rules'],
    'core/protocol/DELIVERY_GOVERNANCE.md': [' Phase Entry Gate Routing', 'Delivery-Need Classification Gate', 'Phase Entry Gate', 'If the result is `BLOCKED` or `UNCERTAIN`'],
    'core/templates/system/delivery/phases/PHASE.md': [' Phase Entry Gate', 'Entry gate status: PENDING / PASS / BLOCKED / UNCERTAIN', 'Greenfield Entry Gate Controls', 'Brownfield Entry Gate Controls'],
    'core/templates/session/SESSION_SCOPE.md': [' Phase Entry Gate Evidence', 'Phase Entry Gate status: PASS / BLOCKED / UNCERTAIN / NOT_APPLICABLE'],
    'core/templates/session/SESSION_EXECUTION.md': [' Phase Entry Gate Execution Log', 'Implementation readiness authorized: YES / NO'],
    'core/commands/start.md': [' Phase Entry Gate Enforcement', 'Phase Entry Gate', 'lifecycle status', 'phase type'],
    'core/commands/continue.md': [' Phase Entry Gate Enforcement', 'Phase Entry Gate', 'lifecycle status', 'phase type'],
    'core/commands/status.md': [' Phase Entry Gate Enforcement', 'Phase Entry Gate', 'lifecycle status', 'phase type'],
    'core/commands/close.md': [' Phase Entry Gate Enforcement', 'Phase Entry Gate', 'lifecycle status', 'phase type'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: phase entry gate enforcement {rel} missing {phrase}')
            sys.exit(1)
print('PASS: HIRMOS phase entry gate enforcement static check')


# Phase Progress / Carry-Forward enforcement checks
for rel, phrases in {
    'core/protocol/PHASE_LIFECYCLE.md': [' Phase Progress / Carry-Forward Enforcement', 'Phase Progress Ledger', 'Carry-Forward Enforcement', 'Greenfield Progress Rules', 'Brownfield Progress Rules', ' Fail-Closed Rules'],
    'core/protocol/DELIVERY_GOVERNANCE.md': [' Phase Progress / Carry-Forward Routing', 'Phase Progress Ledger', 'Carry-Forward Items', 'CURRENT_SYSTEM_STATE.md active/next phase pointers'],
    'core/templates/system/delivery/phases/PHASE.md': [' Phase Progress Ledger', ' Carry-Forward Enforcement', 'Carry-forward status: NONE / RECORDED / BLOCKED / NOT_APPLICABLE', 'Greenfield Progress Controls', 'Brownfield Progress Controls'],
    'core/templates/session/SESSION_SCOPE.md': [' Phase Progress and Carry-Forward Control', 'Previous Phase Progress Ledger inspected', 'Carry-forward required if not accepted'],
    'core/templates/session/SESSION_EXECUTION.md': [' Phase Progress / Carry-Forward Record', 'Adopted phase progress reviewed', 'Carry-forward obligations recorded'],
    'core/templates/system/CURRENT_SYSTEM_STATE.md': [' Phase Progress Pointer Rule', 'still-active phase', 'explicit carry-forward target'],
    'system/accepted-state/CURRENT_SYSTEM_STATE.md': [' Phase Progress Pointer Rule', 'still-active phase', 'explicit carry-forward target'],
    'core/commands/start.md': [' Phase Progress / Carry-Forward Enforcement', 'Phase Progress Ledger', 'Carry-Forward Items'],
    'core/commands/continue.md': [' Phase Progress / Carry-Forward Enforcement', 'Phase Progress Ledger', 'Carry-Forward Items'],
    'core/commands/status.md': [' Phase Progress / Carry-Forward Enforcement', 'Phase Progress Ledger', 'Carry-Forward Items'],
    'core/commands/close.md': [' Phase Progress / Carry-Forward Enforcement', 'Phase Progress Ledger', 'Carry-Forward Items'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: phase progress/carry-forward enforcement {rel} missing {phrase}')
            sys.exit(1)

print('PASS: HIRMOS phase progress/carry-forward enforcement static check')


# Phase Acceptance enforcement checks
for rel, phrases in {
    'core/protocol/PHASE_LIFECYCLE.md': [' Phase Acceptance Enforcement', 'Phase Acceptance Evidence Gate', 'Greenfield Acceptance Rules', 'Brownfield Acceptance Rules', ' Fail-Closed Rules'],
    'core/protocol/DELIVERY_GOVERNANCE.md': [' Phase Acceptance Routing', 'Phase Acceptance Evidence Gate', 'CURRENT_SYSTEM_STATE.md active/next phase pointers'],
    'core/templates/system/delivery/phases/PHASE.md': [' Phase Acceptance Evidence Gate', 'Greenfield Acceptance Evidence', 'Brownfield Acceptance Evidence', 'Mixed Acceptance Evidence'],
    'core/templates/session/SESSION_SCOPE.md': [' Phase Acceptance Control', 'Phase acceptance will be evaluated through Phase Acceptance Evidence Gate'],
    'core/templates/session/SESSION_EXECUTION.md': [' Phase Acceptance Enforcement Record', 'Phase Acceptance Evidence Gate inspected'],
    'core/templates/system/CURRENT_SYSTEM_STATE.md': [' Phase Acceptance Pointer Rule', 'last accepted phase'],
    'system/accepted-state/CURRENT_SYSTEM_STATE.md': [' Phase Acceptance Pointer Rule', 'last accepted phase'],
    'core/commands/start.md': [' Phase Acceptance Enforcement', 'Phase Acceptance Evidence Gate'],
    'core/commands/continue.md': [' Phase Acceptance Enforcement', 'Phase Acceptance Evidence Gate'],
    'core/commands/status.md': [' Phase Acceptance Enforcement', 'what acceptance evidence is missing'],
    'core/commands/close.md': [' Phase Acceptance Enforcement', ' Phase Acceptance Evidence Gate is PASS'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: phase acceptance enforcement {rel} missing {phrase}')
            sys.exit(1)
print('PASS: HIRMOS phase acceptance enforcement static check')



# CLI / Status UX phase lifecycle reporting checks
for rel, phrases in {
    'core/protocol/PHASE_LIFECYCLE.md': [' CLI / Status UX Phase Lifecycle Reporting', 'Phase Lifecycle Status Report', 'Phase Entry Gate status', 'Phase Acceptance Evidence Gate status', 'Status Blocked By Phase Lifecycle Conflict', 'Exactly-One-Next-Command'],
    'core/protocol/DELIVERY_GOVERNANCE.md': [' Phase Lifecycle Status Reporting', 'CURRENT_SYSTEM_STATE.md` delivery pointers', 'Phase Progress Ledger status', 'Status Blocked By Phase Lifecycle Conflict'],
    'core/commands/status.md': [' CLI / Status UX Phase Lifecycle Reporting', 'Phase Lifecycle Status Report', 'Greenfield status group', 'Brownfield status group', 'Exactly one recommended next command'],
    'core/templates/session/SESSION_EXECUTION.md': [' Phase Lifecycle Status Report Record', 'Phase lifecycle status', 'Phase Acceptance Evidence Gate status', 'Exactly one recommended next command'],
    'core/templates/system/CURRENT_SYSTEM_STATE.md': [' Phase Lifecycle Status Pointer Rule', 'Phase Lifecycle Status Report', 'pointer concordance'],
    'system/accepted-state/CURRENT_SYSTEM_STATE.md': [' Phase Lifecycle Status Pointer Rule', 'Phase Lifecycle Status Report', 'pointer concordance'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: CLI/status phase lifecycle reporting {rel} missing {phrase}')
            sys.exit(1)
print('PASS: HIRMOS CLI/status phase lifecycle reporting static check')


# delivery governance validator regression fixture checks
for rel, phrases in {
    'tools/test_validator_regressions.py': ['delivery governed active readiness passes', 'delivery missing durable plan fails', 'delivery uncertain at readiness fails', 'delivery pointer mismatch fails', 'delivery close missing status transaction fails', 'delivery close applied status passes', 'phase entry gate valid brownfield passes', 'phase entry gate valid mixed passes', 'phase missing lifecycle status fails', 'phase blocked lifecycle status fails', 'phase unknown type fails', 'greenfield phase missing MVP boundary fails', 'brownfield phase missing preservation baseline fails', 'mixed phase missing brownfield controls fails', 'phase partial close missing carry-forward fails', 'phase partial close with carry-forward passes', 'phase accepted missing acceptance evidence fails', 'phase accepted with acceptance evidence passes', 'phase lifecycle status report missing fields fails', 'phase lifecycle status report complete passes'],
    'tools/fixtures/README.md': [' Delivery Governance Regression Fixtures', 'Delivery-Need Classification', 'durable Delivery Plan', 'Close-Time Delivery / Phase Status Transaction', ' Phase Entry Gate Regression Fixtures', ' Phase Progress / Carry-Forward Regression Fixtures', ' Phase Acceptance Regression Fixtures', ' Phase Lifecycle Validator Regression Fixtures', 'phase lifecycle status report missing fields fails'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase not in body:
            print(f'FAIL: delivery governance regression surface {rel} missing {phrase}')
            sys.exit(1)
print('PASS: HIRMOS phase lifecycle validator regression fixture static check')



print('PASS: HIRMOS durable delivery templates and classification gate static check')

print('PASS: HIRMOS core authority/bootstrap static check')


# Session artifact template checks
session_artifacts = (root/'core/protocol/SESSION_ARTIFACTS.md').read_text()
for phrase in [
    'Snapshot-backed checkpoint rule',
    'Artifact Instantiation Log',
    'A governed session is active only when',
    'Delivery governance artifacts',
    'durable system artifacts',
    'PHASE-xx.md',
    'Archive and reset',
]:
    if phrase not in session_artifacts:
        print(f'FAIL: SESSION_ARTIFACTS.md missing session artifact phrase: {phrase}')
        sys.exit(1)

template_expectations = {
    'SESSION_SCOPE.md': ['Authorized Scope', 'Delivery Shape Decision', 'smallest sufficient governed delivery shape', 'Unresolved Items Control', 'Session Satisfaction Review and Close Verification', 'Fail-closed result'],
    'unresolved-items.md': ['Producer Contributions', 'Active Gated Items', 'Disposition History', 'Protocol authority'],
    'implementation-units/IU.md': ['Unit Contract', 'Execution Record', 'Unit Review', 'Does the actual implementation satisfy 100%', 'Retry Decision', 'Evidence from Failed Attempt', 'Escalation Condition'],
    'DESIGN.md': ['Current-State Basis', 'Governed Requirements', 'Delivery Shape Decision', 'Technical Review and Implementation Readiness Basis'],
    'EVIDENCE.md': ['Command Evidence', 'Runtime and Critical-Flow Evidence', 'Production-Shaped Engineering Evidence', 'Claim Reconciliation Summary', 'Close / Archive Evidence'],
    'SESSION_EXECUTION.md': ['Active Execution Controls', 'Artifact Instantiation Log', 'Close / Archive / Reset Invariant Controls'],
}

for name, phrases in template_expectations.items():
    body = (root/'core/templates/session'/name).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: template {name} missing session artifact phrase: {phrase}')
            sys.exit(1)



# Artifact template quality checks after governance-tax cleanup
_design_template = (root/'core/templates/session/DESIGN.md').read_text()
if _design_template.count('## Runtime Integration and Production Readiness Design') != 1:
    print('FAIL: DESIGN.md must contain exactly one Runtime Integration and Production Readiness Design heading')
    sys.exit(1)
_contract_template = (root/'core/templates/session/SESSION_SCOPE.md').read_text()
_nonblank_contract = [line.strip() for line in _contract_template.splitlines() if line.strip()]
if len(_nonblank_contract) < 4 or _nonblank_contract[1] != 'Status: active-session Main Artifact.':
    print('FAIL: SESSION_SCOPE.md must place status/purpose before delivery-shape sections')
    sys.exit(1)
_unresolved_template = (root/'core/templates/session/unresolved-items.md').read_text()
if 'including `NON_GATING` items' not in _unresolved_template or 'Non-gating items are governed decisions or assumptions' not in _unresolved_template:
    print('FAIL: unresolved-items.md must preserve full-detail treatment for material non-gating items')
    sys.exit(1)


# command protocol update checks
for rel, phrases in {
    'core/commands/start.md': ['Command-state gate', 'Required state mutation', 'status` is `idle`', 'final start state'],
    'core/commands/continue.md': ['Command-state gate', 'Required state mutation', 'increment `SESSION_STATE.json.continuation_pass`', 'bare `hirmos continue` is rejected'],
    'core/commands/status.md': ['Command-state gate', 'without mutating files', 'recommended_next_command'],
    'core/commands/close.md': ['Command-state gate', 'Required state mutation', 'archived `SESSION_STATE.json` normalized', 'stale active-session artifacts'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: command protocol update: {rel} missing {phrase}')
            sys.exit(1)

# Contract-centered session spine checks
for rel, phrases in {
}.items():
    body = (root / rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: {rel} missing contract-centered spine phrase: {phrase}')
            sys.exit(1)

state = json.loads((root / 'session/SESSION_STATE.json').read_text())
if 'allowed_next_commands' not in state or 'recommended_next_command' not in state:
    print('FAIL: session/SESSION_STATE.json missing command-state fields')
    sys.exit(1)



# durable delivery governance checks
for rel, phrases in {
    'core/protocol/DELIVERY_GOVERNANCE.md': ['Delivery Shape Decision Gate', 'smallest sufficient governed delivery shape', 'SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS', 'DELIVERY_SCOPE.md'],
    'core/templates/system/delivery/DELIVERY_PLAN.md': ['Delivery Shape Source', 'Delivery Index', 'Delivery Coverage Matrix', 'Status Update Log'],
    'core/templates/system/delivery/DELIVERY_SCOPE.md': ['Authorized Outcome', 'Scoped Requirements', 'Production-Shaped Engineering Gate', 'Delivery Close Verification'],
    'core/templates/system/delivery/phases/PHASE.md': ['Phase Contract', 'Source Delivery Scope', 'Binary Exit Criteria', 'Session Handoff'],
    'core/templates/session/SESSION_SCOPE.md': ['Delivery Shape Decision', 'smallest sufficient governed delivery shape', 'Selected shape justification'],
    'core/templates/session/SESSION_EXECUTION.md': ['Delivery Shape Decision Gate Execution', 'Gate status: PASS | BLOCKED | NOT_ASSESSED'],
    'core/protocol/PROJECT_TYPES.md': ['Delivery shape fields', 'Delivery governance required: YES / NO / UNCERTAIN'],
    'core/protocol/COMMAND_STATE_MACHINE.md': ['Delivery Shape Decision state gate', 'must not recommend `hirmos continue`'],
    'core/commands/start.md': ['Delivery Shape Decision Gate', 'smallest governed delivery shape'],
    'core/templates/system/CURRENT_SYSTEM_STATE.md': ['Active Development Context', 'Delivery roadmap:', 'Active delivery scope:', 'Active phase:'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: delivery governance surface {rel} missing {phrase}')
            sys.exit(1)

for forbidden in ['core/templates/session/DELIVERY_PLAN.md','core/templates/session/DELIVERY_STATUS.md','core/templates/session/PHASE_PLAN.md','core/templates/session/PHASE_CONTRACT.md','core/templates/session/DELIVERY_UNIT_CONTRACT.md']:
    if (root/forbidden).exists():
        print(f'FAIL: session-local delivery template must not remain canonical: {forbidden}')
        sys.exit(1)



# delivery / phase capability rewire checks
for rel, phrases in {
    'core/protocol/DELIVERY_GOVERNANCE.md': ['Delivery / Phase Capability Routing', 'delivery-design → phase-contracting → session-scope → implementation-readiness', 'single-session safety evidence'],
    'extensions/design-agent/extension.json': ['phase-contracting', 'session-scope'],
    'extensions/design-agent/entrypoints/default.md': ['Durable Delivery / Phase Capability Rewire', 'delivery-design', 'phase-contracting', 'session-scope', 'implementation-readiness'],
    'extensions/design-agent/capabilities/delivery-design/capability.json': ['Delivery Shape Decision selects a durable delivery shape', '_hirmos/system/delivery/DELIVERY_PLAN.md', '_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md'],
    'extensions/design-agent/capabilities/phase-contracting/capability.json': ['_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md', '_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md', 'session-scope source-readiness control'],
    'extensions/design-agent/capabilities/session-scope/capability.json': ['durable phase', 'single-session safety evidence'],
    'extensions/design-agent/capabilities/implementation-readiness/capability.json': ['durable delivery coverage when required', 'Delivery Shape Decision gate'],
    'core/templates/session/SESSION_EXECUTION.md': ['Delivery / Phase Capability Routing Log', 'delivery-design', 'phase-contracting', 'session-scope', 'implementation-readiness'],
    'core/templates/session/SESSION_SCOPE.md': ['Delivery / Phase Capability Routing Evidence', 'delivery-design', 'phase-contracting', 'implementation-readiness'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: delivery capability rewire {rel} missing {phrase}')
            sys.exit(1)

for forbidden_rel in [
    'extensions/design-agent/capabilities/session-scope-contract',
    'extensions/design-agent/capabilities/phase-planning',
]:
    if (root/forbidden_rel).exists():
        print(f'FAIL: removed pre-delivery-capability-alignment design capability path still exists: {forbidden_rel}')
        sys.exit(1)

for forbidden in ['session-scope-contract', 'phase-planning']:
    for path in [root/'extensions/design-agent', root/'core/protocol/DELIVERY_GOVERNANCE.md']:
        paths = path.rglob('*') if path.is_dir() else [path]
        for candidate in paths:
            if candidate.is_file() and candidate.suffix in {'.md','.json'}:
                if forbidden in candidate.read_text(errors='ignore'):
                    print(f'FAIL: deprecated delivery capability reference {forbidden!r}: {candidate.relative_to(root)}')
                    sys.exit(1)

print('PASS: HIRMOS delivery / phase capability rewire static check')

print('PASS: HIRMOS durable delivery templates and classification gate static check')

print('PASS: HIRMOS core authority/bootstrap static check')


# Capability and entrypoint checks
capability_routing = (root/'core/protocol/CAPABILITY_ROUTING.md').read_text()
for phrase in [
    'Routing order',
    'Capability decisions',
    'Entrypoint execution contract',
    'Capability completion rule',
    'Unresolved-item producer rule',
]:
    if phrase not in capability_routing:
        print(f'FAIL: CAPABILITY_ROUTING.md missing capability/entrypoint phrase: {phrase}')
        sys.exit(1)

expected_extensions = {
    'system-state-agent': ['request-intake','source-material-ingestion','prototype-ingestion','understand-system-state','update-system-state'],
    'design-agent': ['requirements-design','system-design','delivery-design','phase-contracting','session-scope','technical-review','implementation-readiness'],
    'implementation-agent': ['implementation-unit-planning','implementation-execution','implementation-unit-review','validation-review','retry-escalation','session-implementation-review'],
}
for ext, caps in expected_extensions.items():
    ext_dir = root/'extensions'/ext
    manifest_path = ext_dir/'extension.json'
    if not manifest_path.exists():
        print(f'FAIL: extension manifest missing: {manifest_path.relative_to(root)}')
        sys.exit(1)
    manifest = json.loads(manifest_path.read_text())
    if manifest.get('id') != ext:
        print(f'FAIL: extension id mismatch for {ext}')
        sys.exit(1)
    for field in ['summary','lifecycle_stages','capabilities','entrypoints','runtime']:
        if field not in manifest:
            print(f'FAIL: extension manifest {ext} missing field: {field}')
            sys.exit(1)
    if sorted(manifest.get('capabilities', [])) != sorted(caps):
        print(f'FAIL: extension manifest capabilities mismatch for {ext}')
        sys.exit(1)
    default_ep = ext_dir / manifest['entrypoints']['default']
    if not default_ep.exists():
        print(f'FAIL: extension default entrypoint missing: {default_ep.relative_to(root)}')
        sys.exit(1)
    body = default_ep.read_text()
    for phrase in ['Execution Contract','Purpose','Produces','Terminal States','Required behavior']:
        if phrase.lower() not in body.lower():
            print(f'FAIL: extension entrypoint {default_ep.relative_to(root)} missing {phrase}')
            sys.exit(1)
    for cap in caps:
        cap_dir = ext_dir/'capabilities'/cap
        cap_manifest_path = cap_dir/'capability.json'
        if not cap_manifest_path.exists():
            print(f'FAIL: capability manifest missing: {cap_manifest_path.relative_to(root)}')
            sys.exit(1)
        cap_manifest = json.loads(cap_manifest_path.read_text())
        for field in ['id','extension','summary','lifecycle_stage','entrypoints','activation','requires_artifacts','produces_artifacts','execution_controls','unresolved_items']:
            if field not in cap_manifest:
                print(f'FAIL: capability manifest {ext}/{cap} missing field: {field}')
                sys.exit(1)
        if cap_manifest['id'] != cap or cap_manifest['extension'] != ext:
            print(f'FAIL: capability manifest identity mismatch: {ext}/{cap}')
            sys.exit(1)
        cap_ep = cap_dir / cap_manifest['entrypoints']['default']
        if not cap_ep.exists():
            print(f'FAIL: capability entrypoint missing: {cap_ep.relative_to(root)}')
            sys.exit(1)
        ep_body = cap_ep.read_text()
        for phrase in ['Execution Contract','Purpose','Produces','Terminal States','Activation triggers','Required inputs','Execution controls contributed','Required behavior','Interaction-mode visibility']:
            if phrase not in ep_body:
                print(f'FAIL: capability entrypoint {cap_ep.relative_to(root)} missing {phrase}')
                sys.exit(1)

if 'Capability / Stage Activity Summary' not in (root/'core/templates/session/SESSION_EXECUTION.md').read_text():
    print('FAIL: SESSION_EXECUTION.md missing capability activity summary')
    sys.exit(1)

print('PASS: HIRMOS capability/entrypoint static check')


# System-state-agent method checks
system_state_method = root/'extensions/system-state-agent/entrypoints/default.md'
if not system_state_method.exists():
    print('FAIL: system-state-agent default entrypoint missing')
    sys.exit(1)
method_body = system_state_method.read_text()
for phrase in [
    'User Request and source inputs are focus inputs, not authority',
    'Prototype and POC materials are evidence, not authority',
    'general system understanding and request-focused system understanding',
    'observed, inferred, assumed, unknown, blocked, and not applicable',
    'Update System State consumes reviewed outcomes',
]:
    if phrase not in method_body:
        print(f'FAIL: system-state-agent default entrypoint missing system-state-agent phrase: {phrase}')
        sys.exit(1)

system_state_entrypoints = {
    'request-intake': ['Method', 'Initial Non-Authority Notice', 'Handoff to Understand System State'],
    'source-material-ingestion': ['Method', 'Source Material Inventory', 'Prototype / POC Routing'],
    'prototype-ingestion': ['Method', 'observed behavior from intended behavior', 'Implementation Details That Are Evidence Only'],
    'understand-system-state': ['Method', 'general and focused system-state understanding', 'Handoff to Design'],
    'update-system-state': ['Method', 'accepted outcomes', 'archive', 'future sessions'],
}
for cap, phrases in system_state_entrypoints.items():
    ep = root/'extensions/system-state-agent/capabilities'/cap/'entrypoints/default.md'
    body = ep.read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: system-state-agent capability {cap} missing system-state-agent phrase: {phrase}')
            sys.exit(1)

system_state_templates = {
}
for name, phrases in system_state_templates.items():
    body = (root/'core/templates/session'/name).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: system-state template {name} missing system-state-agent phrase: {phrase}')
            sys.exit(1)

if 'System-State Capability Summary' not in (root/'core/templates/session/SESSION_EXECUTION.md').read_text():
    print('FAIL: SESSION_EXECUTION.md missing system-state capability summary')
    sys.exit(1)

print('PASS: HIRMOS system-state-agent method/template static check')


# Design-agent method/template checks
design_method = root/'extensions/design-agent/entrypoints/default.md'
if not design_method.exists():
    print('FAIL: design-agent default entrypoint missing')
    sys.exit(1)
design_method_body = design_method.read_text()
for phrase in [
    'Requirement inputs are source material, not requirements authority',
    'Design owns governed requirements, system/application design, delivery structure, technical review, Session Scope, and implementation readiness',
    'Design may satisfy requirements/design/planning requests',
    'Durable Delivery Plan',
    'PHASE-xx.md',
    'Session Scope is downstream implementation authority',
    'Design may route back to Understand System State',
]:
    if phrase not in design_method_body:
        print(f'FAIL: design-agent default entrypoint missing design-agent phrase: {phrase}')
        sys.exit(1)

design_entrypoints = {
    'requirements-design': ['Method', 'Separate requirement inputs from governed requirements authority', 'Map each material requirement to source evidence and system-state findings'],
    'system-design': ['Method', 'Design from governed requirements, not raw requirement inputs alone', 'technical review'],
    'delivery-design': ['Method', 'Delivery Plan', 'Map Delivery Plan items to governed requirements'],
    'phase-contracting': ['Method', 'Phase Contract', 'durable delivery'],
    'session-scope': ['Method', 'Session Scope', 'implementation unit planning, implementation unit review, session implementation review, and Update System State'],
    'technical-review': ['Method', 'Third-party review pointers', 'challenge/change path'],
    'implementation-readiness': ['Method', 'snapshot-backed checkpoint control', 'Session Scope authorizes exactly what Implementation may do'],
}
for cap, phrases in design_entrypoints.items():
    ep = root/'extensions/design-agent/capabilities'/cap/'entrypoints/default.md'
    body = ep.read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: design-agent capability {cap} missing design-agent phrase: {phrase}')
            sys.exit(1)

design_templates = {
    'DESIGN.md': ['Design Source Matrix', 'Governed Requirements', 'Delivery Structure Decision', 'Implementation Authorization Inputs'],
}
for name, phrases in design_templates.items():
    body = (root/'core/templates/session'/name).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: design template {name} missing design-agent phrase: {phrase}')
            sys.exit(1)

if 'Design Capability Summary' not in (root/'core/templates/session/SESSION_EXECUTION.md').read_text():
    print('FAIL: SESSION_EXECUTION.md missing Design Capability Summary')
    sys.exit(1)

print('PASS: HIRMOS design-agent method/template static check')


# Implementation-agent method/template checks
implementation_method = root/'extensions/implementation-agent/entrypoints/default.md'
if not implementation_method.exists():
    print('FAIL: implementation-agent default entrypoint missing')
    sys.exit(1)
implementation_method_body = implementation_method.read_text()
for phrase in [
    'Implementation is governed realization of accepted Design, not merely code editing',
    'An Implementation Unit is an execution contract, not a generic task or prompt',
    'The Session Scope Implementation Unit Plan must cover 100% of authorized implementation scope',
    'Implementation execution performs only the work authorized by the target `IU-xx.md` artifact',
    'Implementation is incomplete without evidence',
    'Retry must be evidence-based and bounded',
    'Implementation routes back when it discovers',
    'Implementation may claim completion only when',
]:
    if phrase not in implementation_method_body:
        print(f'FAIL: implementation-agent default entrypoint missing implementation-agent phrase: {phrase}')
        sys.exit(1)

implementation_entrypoints = {
    'implementation-unit-planning': ['Method', 'implementation-units/IU-xx.md', 'collectively cover 100%'],
    'implementation-execution': ['Method', 'Read the target `IU-xx.md` artifact directly', 'modify only files/areas authorized'],
    'implementation-unit-review': ['Method', 'Unit review is local, specific, and evidence-based', 'A unit is not complete until local review is recorded'],
    'validation-review': ['Method', 'Validation review must distinguish run evidence from claims', 'not-run or not-applicable checks'],
    'retry-escalation': ['Method', 'Retry is not a second attempt at arbitrary implementation', 'route back instead of retrying'],
}
for cap, phrases in implementation_entrypoints.items():
    ep = root/'extensions/implementation-agent/capabilities'/cap/'entrypoints/default.md'
    body2 = ep.read_text()
    for phrase in phrases:
        if phrase not in body2:
            print(f'FAIL: implementation-agent capability {cap} missing implementation-agent phrase: {phrase}')
            sys.exit(1)

implementation_templates = {
    'implementation-units/IU.md': ['Unit Contract', 'Execution Record', 'Unit Review', 'Does the actual implementation satisfy 100%', 'Request-to-Result Review', 'Retry / Route-Back Decision', 'Not Run / Not Applicable Checks', 'Retry Decision', 'Evidence from Failed Attempt', 'Escalation Condition'],
    'EVIDENCE.md': ['Evidence Claims', 'Not Run / Not Applicable', 'Scope Coverage', 'Evidence Limitations'],
}
for name, phrases in implementation_templates.items():
    body3 = (root/'core/templates/session'/name).read_text()
    for phrase in phrases:
        if phrase not in body3:
            print(f'FAIL: implementation template {name} missing implementation-agent phrase: {phrase}')
            sys.exit(1)

if 'Implementation Capability Summary' not in (root/'core/templates/session/SESSION_EXECUTION.md').read_text():
    print('FAIL: SESSION_EXECUTION.md missing Implementation Capability Summary')
    sys.exit(1)

print('PASS: HIRMOS implementation-agent method/template static check')


# Unresolved items and governed checkpoint checks
unresolved_protocol = (root/'core/protocol/UNRESOLVED_ITEMS.md').read_text()
for phrase in [
    'Producer contribution',
    'ITEMS_FOUND',
    'Anti-overmerge rule',
    'Current checkpoint feed',
    'Disposition and revalidation',
    'Field completeness rule',
    'Minimum fields',
    'directly review `_hirmos/session/unresolved-items.md`',
    'Summaries in `SESSION_SCOPE.md`',
    'Missing minimum fields are not harmless omissions',
]:
    if phrase not in unresolved_protocol:
        print(f'FAIL: unresolved-items.md protocol missing unresolved/checkpoint phrase: {phrase}')
        sys.exit(1)

for phrase in [
    'id;', 'title;', 'description;', 'source evidence;', 'classification;',
    'decision owner;', 'visibility mode;', 'affected lifecycle boundary;',
    'current status;', 'current recommendation;', 'downstream impact;',
    'disposition history;', 'revalidation point;'
]:
    if phrase not in unresolved_protocol:
        print(f'FAIL: unresolved-items.md protocol missing minimum field: {phrase}')
        sys.exit(1)

lower_unresolved_template = (root/'core/templates/session/unresolved-items.md').read_text()
for phrase in [
    'Register Controls',
    'Required Item Detail Blocks',
    'This register is authoritative for unresolved-item details',
    'Detail block present?',
    'Last direct review boundary',
    'resolved items have Disposition History with “what changed”',
]:
    if phrase not in lower_unresolved_template:
        print(f'FAIL: canonical unresolved-items.md template missing governance phrase: {phrase}')
        sys.exit(1)

for phrase in [
    'Source producer/capability:', 'Options / valid answer shape when user input is required:',
    'Assumption if carried:', 'Downstream impact:', 'Revalidation point:', 'Disposition history reference:'
]:
    if phrase not in lower_unresolved_template:
        print(f'FAIL: canonical unresolved-items.md template missing item detail field: {phrase}')
        sys.exit(1)

session_scope_template = (root/'core/templates/session/SESSION_SCOPE.md').read_text()
for phrase in [
    'This section is only a control summary',
    'HIRMOS must not infer unresolved-item details from this summary',
    'This summary must not contain item-level detail rows',
    'Last direct register review boundary',
]:
    if phrase not in session_scope_template:
        print(f'FAIL: SESSION_SCOPE.md unresolved control missing governance phrase: {phrase}')
        sys.exit(1)

session_execution_template = (root/'core/templates/session/SESSION_EXECUTION.md').read_text()
for phrase in [
    'Unresolved Register Direct Review Log',
    'Register reviewed directly?',
    'SESSION_SCOPE.md` unresolved summary is not sufficient',
]:
    if phrase not in session_execution_template:
        print(f'FAIL: SESSION_EXECUTION.md missing unresolved direct-review control phrase: {phrase}')
        sys.exit(1)

for method in root.glob('extensions/*-agent/entrypoints/default.md'):
    body = method.read_text()
    for phrase in [
        'MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`',
        'record exactly one producer outcome',
        'current status',
        'revalidation point',
    ]:
        if phrase not in body:
            print(f'FAIL: extension default entrypoint missing hardened unresolved producer discipline phrase {phrase}: {method.relative_to(root)}')
            sys.exit(1)

for cap_ep in root.glob('extensions/*-agent/capabilities/*/entrypoints/default.md'):
    body = cap_ep.read_text()
    for phrase in [
        'MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`',
        'record exactly one producer outcome',
        'ITEMS_FOUND',
        'NONE_FOUND',
        'NOT_APPLICABLE',
        'BLOCKED',
        'current status',
        'downstream impact',
        'revalidation point',
    ]:
        if phrase not in body:
            print(f'FAIL: capability entrypoint missing hardened unresolved producer phrase {phrase}: {cap_ep.relative_to(root)}')
            sys.exit(1)

checkpoint_protocol = (root/'core/protocol/GOVERNED_CHECKPOINTS.md').read_text()
for phrase in [
    'Checkpoint types',
    'Required Current Continuation Snapshot',
    'Domain Expert rendering',
    'Unresolved-item checkpoint rule',
    'Checkpoint completion',
]:
    if phrase not in checkpoint_protocol:
        print(f'FAIL: GOVERNED_CHECKPOINTS.md missing unresolved/checkpoint phrase: {phrase}')
        sys.exit(1)

unresolved_template = (root/'core/templates/session/unresolved-items.md').read_text()
for phrase in [
    'Producer Contributions',
    'ITEMS_FOUND',
    'Reconciliation Worklist',
    'Current Checkpoint Feed',
    'Downstream Revalidation History',
]:
    if phrase not in unresolved_template:
        print(f'FAIL: unresolved-items.md template missing unresolved/checkpoint phrase: {phrase}')
        sys.exit(1)

session_execution = (root/'core/templates/session/SESSION_EXECUTION.md').read_text()
for phrase in ['Governed Continuation Summary', 'Current Continuation Snapshot status', 'Unresolved item status']:
    if phrase not in session_execution:
        print(f'FAIL: SESSION_EXECUTION.md missing governed checkpoint phrase: {phrase}')
        sys.exit(1)

for method in root.glob('extensions/*-agent/entrypoints/default.md'):
    if 'Unresolved-item producer discipline' not in method.read_text():
        print(f'FAIL: extension default entrypoint missing unresolved producer discipline: {method.relative_to(root)}')
        sys.exit(1)

print('PASS: HIRMOS unresolved/checkpoint static check')


# Stack/project-type/delivery-unit integration checks
project_types = (root/'core/protocol/PROJECT_TYPES.md').read_text()
for phrase in [
    'greenfield',
    'brownfield_large_change',
    'Delivery governance required',
    'Project type is a routing classification',
    'Large or multi-session work requires governed delivery decomposition',
]:
    if phrase not in project_types:
        print(f'FAIL: PROJECT_TYPES.md missing stack/project-type/delivery-governance phrase: {phrase}')
        sys.exit(1)

stacks_protocol = (root/'core/protocol/STACKS.md').read_text()
for phrase in [
    'single-stack by default and multi-stack aware by evidence',
    'Stack contexts are optional',
    'Repository evidence overrides request preference',
    'Evidence command priority',
    'each Implementation Unit artifact must name exactly one primary stack context',
]:
    if phrase not in stacks_protocol:
        print(f'FAIL: STACKS.md missing stack/project-type/delivery-unit phrase: {phrase}')
        sys.exit(1)

# Source inputs surface checks. Inputs are raw source material and remain non-authoritative until reconciled.
for rel in ['inputs/README.md', 'inputs/uploads/README.md', 'inputs/prototypes/README.md', 'inputs/references/README.md']:
    body = (root / rel).read_text(errors='ignore')
    if 'not' not in body.lower() or 'authority' not in body.lower():
        print(f'FAIL: {rel} must state that source inputs are not authority')
        sys.exit(1)

design_method = (root/'extensions/design-agent/entrypoints/default.md').read_text(errors='ignore')
for phrase in ['_hirmos/inputs/', '_hirmos/inputs/uploads/', 'raw source material']:
    if phrase not in design_method:
        print(f'FAIL: design-agent default entrypoint missing source-input surface phrase: {phrase}')
        sys.exit(1)

requirements_design_entrypoint = (root/'extensions/design-agent/capabilities/requirements-design/entrypoints/default.md').read_text(errors='ignore')
for phrase in ['_hirmos/inputs/', '_hirmos/inputs/uploads/', 'DESIGN.md source matrix']:
    if phrase not in requirements_design_entrypoint:
        print(f'FAIL: requirements-design entrypoint missing source-input surface phrase: {phrase}')
        sys.exit(1)

cfg = json.loads((root/'hirmos.config.json').read_text())
if 'stack_contexts' not in cfg.get('stack', {}):
    print('FAIL: hirmos.config.json missing stack.stack_contexts')
    sys.exit(1)

for stack_id in cfg.get('stack', {}).get('available_stacks', []):
    sd = root/'stacks'/stack_id
    for name in ['stack.json','STACK_OVERVIEW.md','ENGINEERING_STACK_STANDARDS.md','STACK_COMMANDS.md','STACK_ARCHITECTURE_GUIDANCE.md','EXECUTION_STACK_RULES.md','EVIDENCE_COMMANDS.md']:
        if not (sd/name).exists():
            print(f'FAIL: stack package {stack_id} missing {name}')
            sys.exit(1)

design_context = (root/'core/templates/session/DESIGN.md').read_text()
for phrase in ['Project-Type Classification','Stack Classification','Stack Contexts','Delivery Routing Impact']:
    if phrase not in design_context:
        print(f'FAIL: DESIGN.md missing stack/project-type/delivery routing phrase: {phrase}')
        sys.exit(1)

stack_resolution = json.loads((root/'core/templates/session/stack-resolution.json').read_text())
for field in ['active_stack','selection_source','confidence','evidence','stack_path','missing_surfaces','conflicts','decision','stack_contexts','notes']:
    if field not in stack_resolution:
        print(f'FAIL: stack-resolution.json missing field: {field}')
        sys.exit(1)

i9_template_checks = {
    'implementation-units/IU.md': ['Stack Context', 'Cross-stack unit'],
    'EVIDENCE.md': ['Evidence by Stack Context', 'repository evidence first'],
    '../system/delivery/DELIVERY_PLAN.md': ['Delivery-Need Classification Source', 'Delivery Coverage Matrix'],
    'SESSION_EXECUTION.md': ['Project Context / Stack Summary'],
}
for name, phrases in i9_template_checks.items():
    body = (root/'core/templates/session'/name).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: template {name} missing stack/project-type/delivery-unit phrase: {phrase}')
            sys.exit(1)

for method in ['system-state-agent','design-agent','implementation-agent']:
    body = (root/'extensions'/method/'entrypoints/default.md').read_text().lower()
    for phrase in ['project type', 'stack']:
        if phrase.lower() not in body.lower():
            print(f'FAIL: {method} default entrypoint missing project/stack language')
            sys.exit(1)

print('PASS: HIRMOS stack/project-type/delivery-unit static check')


# Validation tooling and installation packaging checks
install_protocol = (root/'core/protocol/INSTALLATION_PACKAGING.md').read_text()
for phrase in [
    'Package shape',
    'Included surfaces',
    'Excluded surfaces',
    'Runtime preservation on install',
    'Packaging verification',
]:
    if phrase not in install_protocol:
        print(f'FAIL: INSTALLATION_PACKAGING.md missing validation/packaging phrase: {phrase}')
        sys.exit(1)

readme = (root/'README.md').read_text()
for phrase in ['Why HIRMOS exists', 'How HIRMOS works', 'hirmos start', 'fallback bootstrap prompt']:
    if phrase not in readme:
        print(f'FAIL: README.md missing validation/packaging phrase: {phrase}')
        sys.exit(1)

installation_doc = (root/'docs/1-use-hirmos/getting-started/installation.md').read_text()
for phrase in ['_hirmos/', 'Manual install', 'Runtime state']:
    if phrase not in installation_doc:
        print(f'FAIL: docs/1-use-hirmos/getting-started/installation.md missing validation/packaging phrase: {phrase}')
        sys.exit(1)

# Guard against obsolete shipped framework mechanisms and diagnostics.
for path in root.rglob('*'):
    if not path.is_file():
        continue
    rel = str(path.relative_to(root))
    if rel == 'tools/validate.py':
        continue
    if path.suffix not in {'.md', '.json', '.py'}:
        continue
    body = path.read_text(errors='ignore')
    forbidden = [
        'SOC runtime rows',
        'canonical surfaced-output hashes',
        'dogfooding transcript',
        'self-review runtime requirement',
        '_workspace/',
        '_internal/',
    ]
    for phrase in forbidden:
        if phrase in body:
            print(f'FAIL: forbidden shipped-framework phrase {phrase!r} found in {rel}')
            sys.exit(1)



# Runtime integration and production-readiness checks
runtime_protocol = (root/'core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md').read_text()
for phrase in [
    'LOCAL_OR_DEMO_SAFE_PROGRESS',
    'PRODUCTION_READY_BEFORE_COMPLETE',
    'DEMO_FIXTURE',
    'LOCAL_REAL_INTEGRATION',
    'PRODUCTION_PROVIDER_INTEGRATION',
    'Domain Expert visibility rule',
    'A passing build or typecheck does not prove local runtime integration or production readiness',
]:
    if phrase not in runtime_protocol:
        print(f'FAIL: RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md missing runtime integration/production-readiness phrase: {phrase}')
        sys.exit(1)

runtime_template = (root/'core/templates/session/DESIGN.md').read_text() + '\n' + (root/'core/templates/session/EVIDENCE.md').read_text()
for phrase in [
    'Material Integration Areas',
    'Recommended Production Options',
    'Current-Session Authorization',
    'Production Readiness Checkpoint Basis',
    'Update System State Carry-Forward',
]:
    if phrase not in runtime_template:
        print(f'FAIL: DESIGN.md/EVIDENCE.md missing runtime integration/production-readiness phrase: {phrase}')
        sys.exit(1)

for rel, phrases in {
    'core/authority/INTERACTION_MODES.md': ['Runtime integration visibility', 'primary HIRMOS recommendation'],
    'core/protocol/VALIDATION_AND_EVIDENCE.md': ['Runtime integration evidence', 'production-provider verification'],
    'core/protocol/SESSION_ARTIFACTS.md': ['Runtime integration readiness artifact'],
    'core/protocol/GOVERNED_CHECKPOINTS.md': ['Production readiness checkpoints'],
    'core/templates/session/DESIGN.md': ['Runtime Integration and Production Readiness Design'],
    'core/templates/session/implementation-units/IU.md': ['Runtime Integration Posture'],
    'core/templates/session/implementation-units/IU.md': ['Runtime Integration Execution Evidence'],
    'core/templates/session/implementation-units/IU.md': ['Runtime Integration Review'],
    'core/templates/session/EVIDENCE.md': ['Runtime Integration Evidence Review'],
    'core/templates/session/SESSION_EXECUTION.md': ['Runtime Integration / Production Readiness Summary'],
    'extensions/design-agent/entrypoints/default.md': ['Runtime integration and production-readiness design discipline'],
    'extensions/implementation-agent/entrypoints/default.md': ['Runtime integration implementation discipline'],
    'extensions/system-state-agent/entrypoints/default.md': ['Runtime integration system-state signals'],
    'docs/2-methodology/runtime-integration-and-production-readiness.md': ['current implementation level'],
}.items():
    body_i12 = (root/rel).read_text()
    for phrase in phrases:
        if phrase not in body_i12:
            print(f'FAIL: {rel} missing runtime integration/production-readiness phrase: {phrase}')
            sys.exit(1)

print('PASS: HIRMOS runtime integration/production-readiness static check')



# Vertical slice and status UX checks
for rel, phrases in {
    'core/protocol/VERTICAL_SLICE_AND_STATUS_UX.md': [
        'Delivery status model',
        'Next command recommendation rule',
        'Next phase recommendation rule',
        'Status command rule',
        'Close output rule',
    ],
    'core/templates/system/delivery/DELIVERY_PLAN.md': [
        'Delivery Decomposition',
        'Active Development Context',
        'Delivery Navigation',
        'Next recommended delivery',
        'Delivery Status Update Log',
    ],
    'core/templates/session/SESSION_EXECUTION.md': [
        'Vertical Slice / Delivery Status Summary',
        'Command Output Summary',
        'Next recommended delivery',
        'Next recommended phase',
    ],
    'core/protocol/COMMANDS.md': [
        'Vertical slice and status UX discipline',
        'recommend exactly one primary next command',
    ],
    'docs/2-methodology/vertical-slice-and-status-ux.md': [
        'Delivery Units',
        'Simple by default',
        'Rigorous underneath',
        'Progressive disclosure',
    ],
}.items():
    body = (root / rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: {rel} missing vertical slice and status UX phrase: {phrase}')
            sys.exit(1)

print('PASS: HIRMOS validation/packaging static check')


# Close/archive accepted-state integrity checks
close_protocol = (root/'core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md').read_text()
for phrase in [
    'Close transaction model',
    'Accepted-state records',
    'Archive manifest',
    'Post-close verification',
    'Abort close',
]:
    if phrase not in close_protocol:
        print(f'FAIL: CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md missing close/archive accepted-state integrity phrase: {phrase}')
        sys.exit(1)

for rel, phrases in {
    'core/templates/session/SESSION_EXECUTION.md': ['Close / Archive / Accepted-State Integrity Summary', 'Post-close status consistency'],
    'core/commands/close.md': ['Accepted-state integrity gate', 'CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md'],
    'core/commands/status.md': ['Post-close status behavior', 'integrity conflict'],
    'core/protocol/SESSION_ARTIFACTS.md': ['Close / archive integrity extension', 'Archive history is not accepted state by itself'],
    'core/authority/ARTIFACT_MODEL.md': ['Accepted state and archive distinction'],
    'core/protocol/VALIDATION_AND_EVIDENCE.md': ['Close and archive evidence'],
    'extensions/system-state-agent/entrypoints/default.md': ['Close / archive integrity discipline'],
    'docs/2-methodology/close-archive-and-accepted-state.md': ['governed state transaction'],
    'docs/reference/artifact-model.md': ['Archive history vs accepted state'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: {rel} missing close/archive accepted-state integrity phrase: {phrase}')
            sys.exit(1)

for rel in ['system/accepted-state/CARRY_FORWARD.md', 'system/history/sessions/.gitkeep']:
    if not (root/rel).exists():
        print(f'FAIL: missing close/archive system scaffold: {rel}')
        sys.exit(1)

print('PASS: HIRMOS close/archive accepted-state integrity static check')



# Implementation evidence and claim reconciliation checks
claim_protocol = (root/'core/protocol/CLAIM_RECONCILIATION.md').read_text()
for phrase in [
    'Claim status values',
    'CLAIMED_NOT_LOGGED',
    'USER_ENVIRONMENT_VERIFIED',
    'Final-file reconciliation',
    'Completion downgrade rule',
]:
    if phrase not in claim_protocol:
        print(f'FAIL: CLAIM_RECONCILIATION.md missing claim reconciliation phrase: {phrase}')
        sys.exit(1)

claim_template = (root/'core/templates/session/EVIDENCE.md').read_text()
for phrase in [
    'Claim Summary',
    'Final-File Reconciliation',
    'Command / Log Reconciliation',
    'Runtime Verification Reconciliation',
    'Downgraded Claims',
]:
    if phrase not in claim_template:
        print(f'FAIL: EVIDENCE.md missing claim reconciliation phrase: {phrase}')
        sys.exit(1)

for rel, phrases in {
    'core/protocol/VALIDATION_AND_EVIDENCE.md': ['Claim reconciliation', 'CLAIMED_NOT_LOGGED', 'USER_ENVIRONMENT_VERIFIED'],
    'core/protocol/SESSION_ARTIFACTS.md': ['Claim reconciliation artifact', 'final files'],
    'core/protocol/COMMANDS.md': ['Claim reconciliation command rule', 'chat-only summaries'],
    'core/authority/EXECUTION_CONTROL_GOVERNANCE.md': ['Claim reconciliation control'],
    'core/protocol/GOVERNED_CHECKPOINTS.md': ['Claim reconciliation checkpoint rule'],
    'core/templates/session/EVIDENCE.md': ['Claim Reconciliation', 'CLAIMED_NOT_LOGGED'],
    'core/templates/session/implementation-units/IU.md': ['Claim Reconciliation', 'PASS_WITH_LIMITATIONS'],
    'core/templates/session/SESSION_EXECUTION.md': ['Claim Reconciliation Summary', 'claim reconciliation control'],
    'extensions/implementation-agent/entrypoints/default.md': ['Claim reconciliation discipline', 'user-environment verification'],
    'extensions/design-agent/entrypoints/default.md': ['Claim reconciliation inputs'],
    'extensions/system-state-agent/entrypoints/default.md': ['Claim reconciliation during state update'],
    'docs/2-methodology/implementation-evidence-and-claim-reconciliation.md': ['logged command passed', 'user environment verified'],
}.items():
    text = (root/rel).read_text()
    for phrase in phrases:
        if phrase not in text:
            print(f'FAIL: {rel} missing claim reconciliation phrase: {phrase}')
            sys.exit(1)

print('PASS: HIRMOS implementation evidence/claim reconciliation static check')


# Autonomous technical progress / progressive disclosure checks
autonomy = (root/'core/protocol/AUTONOMOUS_TECHNICAL_PROGRESS.md').read_text()
for phrase in [
    'attempt local technical progress before deferring',
    'Attempt-before-ask rule',
    'Progressive technical disclosure',
    'Technical decision recording',
    'PRODUCTION_PROVIDER_INTEGRATION',
]:
    if phrase not in autonomy:
        print(f'FAIL: AUTONOMOUS_TECHNICAL_PROGRESS.md missing autonomous technical progress phrase: {phrase}')
        sys.exit(1)

for rel, phrases in {
    'extensions/implementation-agent/entrypoints/default.md': ['Autonomous technical progress discipline', 'Attempt safe local technical progress before deferring it'],
    'extensions/design-agent/entrypoints/default.md': ['Autonomous technical authorization discipline', 'authorize safe local/default technical progress'],
    'extensions/system-state-agent/entrypoints/default.md': ['Autonomous technical discovery discipline', 'package scripts'],
    'core/templates/session/SESSION_SCOPE.md': ['Autonomous Technical Progress Authorization'],
    'core/authority/INTERACTION_MODES.md': ['Autonomous technical progress visibility'],
    'core/protocol/GOVERNED_CHECKPOINTS.md': ['Autonomous technical decision checkpoints'],
    'core/protocol/COMMANDS.md': ['Autonomous technical progress command rule'],
    'docs/2-methodology/autonomous-technical-progress.md': ['Autonomous Technical Progress'],
}.items():
    body = (root/rel).read_text()
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: {rel} missing autonomous technical progress phrase: {phrase}')
            sys.exit(1)

for stack in ['generic','nextjs-typescript','python-backend']:
    body = (root/'stacks'/stack/'STACK_COMMANDS.md').read_text()
    if 'Autonomous technical progress guidance' not in body:
        print(f'FAIL: stack {stack} missing autonomous progress guidance')
        sys.exit(1)

print('PASS: HIRMOS autonomous technical progress/progressive disclosure static check')


# Consolidated durable invariant checks.
# These checks are organized by current framework responsibilities, not by historical implementation-plan labels.

def require_phrases(group, mapping):
    for rel, phrases in mapping.items():
        body = (root/rel).read_text()
        for phrase in phrases:
            if phrase.lower() not in body.lower():
                print(f'FAIL: {group}: {rel} missing required phrase: {phrase}')
                sys.exit(1)
    print(f'PASS: HIRMOS {group} static check')

require_phrases('archive/session-state integrity', {
    'core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md': ['Normalize the archived session state', 'pre_close_session_state_recorded', 'Close-time validator gate'],
    'core/templates/session/SESSION_EXECUTION.md': ['archive-session-state-normalized'],
    'core/commands/close.md': ['Archive and session-state integrity invariant', 'Normalize the archived `SESSION_STATE.json`'],
})

require_phrases('durable current-system-state merge and accepted-state invariants', {
    'core/protocol/CURRENT_SYSTEM_STATE.md': ['canonical accepted current truth', 'Required accepted-state artifacts', 'Accepted-state tracks', 'Close blocking rules', 'Accepted-state navigation and latest-close metadata live in `CURRENT_SYSTEM_STATE.md`', 'Accepted-State Artifact Invariants'],
    'core/templates/system/CURRENT_SYSTEM_STATE.md': ['Product State', 'Delivery State', 'Runtime Integration State', 'Production Readiness State'],
    'system/accepted-state/CURRENT_SYSTEM_STATE.md': ['canonical merged current truth', 'Production Readiness State', 'Accepted-State Artifact Invariants:'],
    'system/accepted-state/CARRY_FORWARD.md': ['Active Carry-Forward Items', 'Active-Only Rule', 'Do not maintain a closed carry-forward table', 'Accepted-State Artifact Invariants:'],
    'system/accepted-state/DECISION_LOG.md': ['Active Accepted Decisions', 'Superseded Decisions', 'Accepted-State Artifact Invariants:'],
    'core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md': ['CURRENT_SYSTEM_STATE.md', 'DECISION_LOG.md', 'accepted-state invariant'],
    'core/templates/session/SESSION_EXECUTION.md': ['Current-State Execution Controls', 'Invariant / Canonical Value Controls'],
    'core/commands/close.md': ['Durable current-system-state merge invariant', 'accepted-state navigation and latest-close metadata'],
    'core/commands/status.md': ['accepted current-state status', 'status invariant and canonical-value reporting'],
    'extensions/system-state-agent/entrypoints/default.md': ['current-state method responsibilities', 'accepted-state invariant and canonical-value responsibilities'],
    'docs/2-methodology/durable-current-system-state.md': ['Durable Current System State', 'supporting artifacts', 'Accepted-state invariants and canonical values'],
})

for rel in ['system/accepted-state/CURRENT_SYSTEM_STATE.md', 'system/accepted-state/CARRY_FORWARD.md', 'system/accepted-state/DECISION_LOG.md', 'core/templates/system/CURRENT_SYSTEM_STATE.md']:
    body = (root/rel).read_text()
    for phrase in ['Accepted-State Artifact Invariants:', 'Use canonical runtime posture values', 'Use canonical evidence states']:
        if phrase.lower() not in body.lower():
            print(f'FAIL: accepted-state invariant block: {rel} missing required phrase: {phrase}')
            sys.exit(1)
print('PASS: HIRMOS accepted-state invariant block preservation static check')

# contract-centered artifact model contract-centered artifact model checks
for rel in ['system/accepted-state/CURRENT_SYSTEM_STATE.md', 'core/templates/system/CURRENT_SYSTEM_STATE.md']:
    body = (root/rel).read_text()
    for phrase in ['Accepted-State Navigation and Latest Close', 'accepted-state navigation, latest-close metadata, and current truth cannot drift']:
        if phrase.lower() not in body.lower():
            print(f'FAIL: accepted-state navigation: {rel} missing required phrase: {phrase}')
            sys.exit(1)
for rel in ['system/accepted-state/CARRY_FORWARD.md', 'core/protocol/CURRENT_SYSTEM_STATE.md']:
    body = (root/rel).read_text()
    for phrase in ['active', 'closed carry-forward history']:
        if phrase.lower() not in body.lower():
            print(f'FAIL: carry-forward active-only rule: {rel} missing required phrase: {phrase}')
            sys.exit(1)
print('PASS: HIRMOS accepted-state simplification static check')


session_dir = root / 'session'
allowed_idle_files = {
    '.gitkeep',
    'SESSION_STATE.json',
    'bootstrap/.gitkeep',
    'implementation-units/.gitkeep',
}
required_idle_files = set(allowed_idle_files)
actual_session_files = {
    str(path.relative_to(session_dir))
    for path in session_dir.rglob('*')
    if path.is_file()
}
missing_idle = sorted(required_idle_files - actual_session_files)
if missing_idle:
    fail('session scaffold missing idle sentinel(s): ' + ', '.join(missing_idle))

session_state_path = session_dir / 'SESSION_STATE.json'
session_state = json.loads(session_state_path.read_text())
if session_state.get('status') == 'idle':
    stale = sorted(actual_session_files - allowed_idle_files)
    if stale:
        fail('session scaffold invariant: active-session artifact(s) present while SESSION_STATE.status is idle: ' + ', '.join(stale))
else:
    for rel in ['SESSION_SCOPE.md', 'SESSION_EXECUTION.md', 'unresolved-items.md']:
        if rel not in actual_session_files:
            fail(f'active session missing canonical root artifact: {rel}')

required_canonical_templates = [
    'core/templates/session/SESSION_SCOPE.md',
    'core/templates/session/SESSION_EXECUTION.md',
    'core/templates/session/unresolved-items.md',
    'core/templates/session/implementation-units/IU.md',
]
for rel in required_canonical_templates:
    if not (root / rel).exists():
        fail(f'canonical template missing: {rel}')

carry = (root / 'system/accepted-state/CARRY_FORWARD.md').read_text()
for forbidden_heading in ['Closed Carry-Forward Items', 'Resolved Carry-Forward Items', 'Completed Carry-Forward Items']:
    if forbidden_heading.lower() in carry.lower():
        fail(f'CARRY_FORWARD.md must be active-only; found heading: {forbidden_heading}')

current = (root / 'system/accepted-state/CURRENT_SYSTEM_STATE.md').read_text()
for phrase in [
    'Accepted-State Navigation and Latest Close',
    'Accepted-State Artifact Invariants:',
    'accepted-state navigation, latest-close metadata, and current truth cannot drift',
]:
    if phrase.lower() not in current.lower():
        fail(f'CURRENT_SYSTEM_STATE.md missing accepted-state navigation/current-state phrase: {phrase}')

# Session close verification must be embedded in the Session Scope under the strict-necessity model.
session_scope = (root / 'core/templates/session/SESSION_SCOPE.md').read_text()
execution_template = (root / 'core/templates/session/SESSION_EXECUTION.md').read_text()
for phrase in [
    'Session Satisfaction Review and Close Verification',
    'Promised work register',
    'Verified work register',
    'Promised vs verified coverage matrix',
    'Does the actual completed work satisfy 100% of `SESSION_SCOPE.md`?',
    'Fail-closed result',
]:
    if phrase.lower() not in session_scope.lower():
        fail(f'SESSION_SCOPE.md missing embedded close verification phrase: {phrase}')
for phrase in [
    'Close / Archive / Reset Invariant Controls',
    'Fail-closed rule',
]:
    if phrase not in execution_template:
        fail(f'SESSION_EXECUTION.md missing strict-necessity close execution phrase: {phrase}')

# Unresolved register must remain a governed root artifact and must not be replaced by SESSION_SCOPE summary.
unresolved_template = (root / 'core/templates/session/unresolved-items.md').read_text()
for phrase in [
    'This register is authoritative for unresolved-item details',
    'Required Item Detail Blocks',
    'Disposition History',
    'Revalidation point:',
]:
    if phrase not in unresolved_template:
        fail(f'unresolved-items.md missing governed-register phrase: {phrase}')
for phrase in [
    'This section is only a control summary',
    'HIRMOS must not infer unresolved-item details from this summary',
    'This summary must not contain item-level detail rows',
]:
    if phrase not in session_scope:
        fail(f'SESSION_SCOPE.md unresolved control summary too weak/missing phrase: {phrase}')

# Implementation-unit consolidation must be structural.
iu_template = (root / 'core/templates/session/implementation-units/IU.md').read_text()
for phrase in [
    'Unit Contract',
    'Execution Record',
    'Unit Review',
    'Retries',
    'Does the actual implementation satisfy 100% of this implementation unit contract?',
]:
    if phrase not in iu_template:
        fail(f'IU.md missing consolidated implementation-unit phrase: {phrase}')

# Reference docs must state the canonical runtime surfaces without compatibility guidance.
runtime_surfaces = (root / 'docs/reference/runtime-surfaces.md').read_text()
for phrase in [
    '_hirmos/session/SESSION_SCOPE.md',
    '_hirmos/session/unresolved-items.md',
    'self-contained `implementation-units/IU-xx.md`',
    'accepted-state navigation in `CURRENT_SYSTEM_STATE.md`',
]:
    if phrase not in runtime_surfaces:
        fail(f'runtime-surfaces doc missing canonical reference: {phrase}')



# SESSION_EXECUTION command ledger integrity checks.
execution_template = (root / 'core/templates/session/SESSION_EXECUTION.md').read_text()
command_state_protocol = (root / 'core/protocol/COMMAND_STATE_MACHINE.md').read_text()
continue_command = (root / 'core/commands/continue.md').read_text()
close_command = (root / 'core/commands/close.md').read_text()
status_command = (root / 'core/commands/status.md').read_text()

for phrase in [
    'Append-Only Ledger Covenant',
    'Forbidden edits:',
    'Control Mutation Ledger',
    'Ledger Integrity Self-Validation',
    'Were all previous continuation pass records preserved?',
    'Continuation pass append requirements:',
    'SESSION_STATE.json.continuation_pass',
]:
    if phrase not in execution_template:
        fail(f' SESSION_EXECUTION.md missing append-only ledger phrase: {phrase}')

for phrase in [
    'SESSION_EXECUTION append-only ledger requirements',
    'every `hirmos continue` appends a continuation pass record',
    'control status changes are appended to a control mutation ledger',
    'implementation-complete and close claims require ledger integrity self-validation',
]:
    if phrase not in command_state_protocol:
        fail(f' COMMAND_STATE_MACHINE.md missing ledger invariant phrase: {phrase}')

for phrase in [
    'Append-only ledger gate',
    'identify the latest recorded continuation pass number',
    'compare it to `SESSION_STATE.json.continuation_pass`',
    'append the control mutation and ledger integrity records',
    'Do not replace an earlier continuation pass',
]:
    if phrase not in continue_command:
        fail(f' hirmos continue command missing ledger discipline phrase: {phrase}')

for phrase in [
    'ledger integrity self-validation',
    'latest pass number concordant with `SESSION_STATE.json.continuation_pass`',
]:
    if phrase not in close_command:
        fail(f' hirmos close command missing ledger close phrase: {phrase}')

for phrase in [
    'must report ledger integrity',
    'It must not mutate the ledger',
]:
    if phrase not in status_command:
        fail(f' hirmos status command missing ledger status phrase: {phrase}')

print('PASS: HIRMOS SESSION_EXECUTION command ledger integrity static check')

# extended execution-ledger alignment Beyond Clear Specs alignment for SESSION_EXECUTION.
for phrase in [
    'Beyond Clear Specs Application',
    'execution-control subset of `_hirmos/core/authority/BEYOND_CLEAR_SPECS.md`',
    'clear execution controls for each lifecycle boundary',
    'strict local self-validation before surfacing readiness',
    'fail-closed behavior when the ledger',
]:
    if phrase not in execution_template:
        fail(f'extended execution-ledger alignment SESSION_EXECUTION.md missing Beyond Clear Specs alignment phrase: {phrase}')

for phrase in [
    'Beyond Clear Specs alignment for command execution',
    'Command execution applies the execution-control subset',
    'minimum execution-control subset needed to keep command transitions honest',
]:
    if phrase not in command_state_protocol:
        fail(f'extended execution-ledger alignment COMMAND_STATE_MACHINE.md missing Beyond Clear Specs alignment phrase: {phrase}')

for name, body in [('continue', continue_command), ('close', close_command)]:
    for phrase in [
        'Beyond Clear Specs execution-control subset',
        'clear command/boundary controls',
        'strict self-validation before surfaced claims',
        'fail-closed behavior when the active artifacts do not support the claim',
    ]:
        if phrase not in body:
            fail(f'extended execution-ledger alignment hirmos {name} command missing Beyond Clear Specs execution-control phrase: {phrase}')

print('PASS: HIRMOS extended execution-ledger alignment Beyond Clear Specs SESSION_EXECUTION alignment static check')

print('PASS: HIRMOS session scaffold semantic validator and fixture realignment static check')

print('PASS: HIRMOS no-deprecated-reference cleanup static check')


# canonical entrypoint surface cleanup checks
capability_routing = (root/'core/protocol/CAPABILITY_ROUTING.md').read_text()
for phrase in [
    'Canonical capability entrypoint surface',
    'entrypoints/default.md',
    'Legacy redirect wrappers',
    'entrypoint.md` are not allowed',
    'without the complete execution contract',
]:
    if phrase not in capability_routing:
        print(f'FAIL: CAPABILITY_ROUTING.md missing canonical entrypoint phrase: {phrase}')
        sys.exit(1)

legacy_entrypoint_wrappers = sorted(root.glob('extensions/*-agent/capabilities/*/entrypoint.md'))
if legacy_entrypoint_wrappers:
    rels = ', '.join(str(p.relative_to(root)) for p in legacy_entrypoint_wrappers)
    print(f'FAIL: legacy capability entrypoint wrapper(s) are not allowed after: {rels}')
    sys.exit(1)

for manifest in root.glob('extensions/*-agent/capabilities/*/capability.json'):
    data = json.loads(manifest.read_text())
    entrypoints = data.get('entrypoints', {})
    if entrypoints.get('default') != 'entrypoints/default.md':
        print(f'FAIL: capability manifest must point default entrypoint to entrypoints/default.md: {manifest.relative_to(root)}')
        sys.exit(1)
    if any(value == 'entrypoint.md' for value in entrypoints.values()):
        print(f'FAIL: capability manifest references removed legacy entrypoint.md wrapper: {manifest.relative_to(root)}')
        sys.exit(1)

print('PASS: HIRMOS canonical entrypoint surface cleanup static check')

# PROD-L4 runtime command / capability routing checks
for rel, phrases in {
    'core/protocol/CAPABILITY_ROUTING.md': ['PROD-L4 delivery-shape routing matrix', 'delivery-design → session-scope → implementation-readiness', 'delivery-design → phase-contracting → session-scope → implementation-readiness', 'Fail-closed rule: if the Delivery Shape Decision is `UNCERTAIN`'],
    'core/protocol/COMMANDS.md': ['PROD-L4 command-to-capability routing behavior', 'hirmos start` must perform Delivery Shape Decision routing', 'hirmos close` must reconcile the route'],
    'core/protocol/DELIVERY_GOVERNANCE.md': ['PROD-L4 runtime command and capability route binding', 'session-scope → implementation-readiness', 'implementation-readiness` must fail closed'],
    'core/commands/start.md': ['PROD-L4 delivery-route runtime behavior', 'must not create a per-delivery `DELIVERY_PLAN.md`'],
    'core/commands/continue.md': ['PROD-L4 delivery-route continuation behavior', 'must not expand delivery scope silently'],
    'core/commands/status.md': ['PROD-L4 delivery-route status reporting', 'Status Blocked By Delivery Route Conflict'],
    'core/commands/close.md': ['PROD-L4 delivery-route close reconciliation', 'route claims and durable artifacts disagree'],
    'extensions/design-agent/entrypoints/default.md': ['PROD-L4 delivery route selection', 'MULTI_SESSION_DELIVERY_WITH_PHASE_FILES → delivery-design → phase-contracting → session-scope → implementation-readiness'],
    'extensions/design-agent/capabilities/delivery-design/entrypoints/default.md': ['PROD-L4 runtime route obligations', 'must not compensate for missing authority'],
    'extensions/design-agent/capabilities/phase-contracting/entrypoints/default.md': ['PROD-L4 runtime route obligations', 'must not compensate for missing authority'],
    'extensions/design-agent/capabilities/session-scope/entrypoints/default.md': ['PROD-L4 runtime route obligations', 'must not compensate for missing authority'],
    'extensions/design-agent/capabilities/implementation-readiness/entrypoints/default.md': ['PROD-L4 runtime route obligations', 'must not compensate for missing authority'],
    'docs/reference/runtime-surfaces.md': ['PROD-L4 runtime command and capability routing', 'hirmos status` reports route readiness'],
}.items():
    body = (root/rel).read_text(errors='ignore')
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: PROD-L4 runtime routing {rel} missing {phrase}')
            sys.exit(1)
print('PASS: HIRMOS PROD-L4 runtime command / capability routing static check')

# PROD-L5 validator and regression fixture migration checks
command_state_protocol = (root/'core/protocol/COMMAND_STATE_MACHINE.md').read_text(errors='ignore')
for phrase in [
    'session_scope',
    '| active | session_scope | `hirmos continue`, `hirmos status` |',
]:
    if phrase not in command_state_protocol:
        print(f'FAIL: PROD-L5 command-state lifecycle migration missing phrase: {phrase}')
        sys.exit(1)
if 'session_contract' in command_state_protocol:
    print('FAIL: PROD-L5 command-state lifecycle migration still references session_contract')
    sys.exit(1)

regression_text = (root/'tools/test_validator_regressions.py').read_text(errors='ignore')
for phrase in [
    'single-session NOT_APPLICABLE readiness passes',
    'delivery missing DELIVERY_SCOPE fails',
    'delivery legacy per-delivery plan path fails',
]:
    if phrase not in regression_text:
        print(f'FAIL: PROD-L5 regression suite missing migrated fixture: {phrase}')
        sys.exit(1)

validator_text = (root/'tools/validate.py').read_text(errors='ignore')
for phrase in [
    'missing durable delivery scope',
    'legacy per-delivery DELIVERY_PLAN.md',
    'durable roadmap/register _hirmos/system/delivery/DELIVERY_PLAN.md',
]:
    if phrase not in validator_text:
        print(f'FAIL: PROD-L5 validator missing delivery-scope migration guard: {phrase}')
        sys.exit(1)

print('PASS: HIRMOS PROD-L5 validator and regression fixture migration static check')

# PROD-L6 accepted-state and history/archive alignment checks
for rel, phrases in {
    'core/templates/system/history/sessions/ARCHIVE_MANIFEST.md': ['history-only archive manifest', 'Archived Session State Normalization', 'Active-Session Reset Verification', 'Post-Close Concordance'],
    'core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md': ['PROD-L6 accepted-state/history alignment', 'ARCHIVE_MANIFEST.md is history-only', 'Current System State delivery pointers refreshed'],
    'core/protocol/CURRENT_SYSTEM_STATE.md': ['PROD-L6 accepted-state delivery pointer model', 'Delivery roadmap: `_hirmos/system/delivery/DELIVERY_PLAN.md`', 'Active delivery scope:', 'Archive manifest concordance'],
    'core/templates/system/CURRENT_SYSTEM_STATE.md': ['Delivery roadmap: none / `_hirmos/system/delivery/DELIVERY_PLAN.md`', 'Active delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`', 'Archive manifest concordance'],
    'system/accepted-state/CURRENT_SYSTEM_STATE.md': ['Delivery roadmap: none / `_hirmos/system/delivery/DELIVERY_PLAN.md`', 'Active delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`', 'Archive manifest concordance'],
    'core/commands/status.md': ['Delivery roadmap path', 'Active delivery scope path', 'Status Blocked By Delivery Pointer Conflict'],
    'core/commands/close.md': ['PROD-L6 accepted-state/history/archive alignment', 'ARCHIVE_MANIFEST.md', 'Current System State delivery pointers'],
    'docs/2-methodology/close-archive-and-accepted-state.md': ['ARCHIVE_MANIFEST.md', 'history-only archive manifest', 'accepted-state concordance'],
    'docs/reference/artifact-model.md': ['ARCHIVE_MANIFEST.md', 'Delivery roadmap/register', 'Delivery scope authority'],
}.items():
    body = (root/rel).read_text(errors='ignore')
    for phrase in phrases:
        if phrase.lower() not in body.lower():
            print(f'FAIL: PROD-L6 accepted-state/history alignment {rel} missing {phrase}')
            sys.exit(1)

for rel in ['core/templates/system/CURRENT_SYSTEM_STATE.md', 'system/accepted-state/CURRENT_SYSTEM_STATE.md']:
    body = (root/rel).read_text(errors='ignore')
    if '_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md' in body or re.search(r'_hirmos/system/delivery/[A-Za-z0-9._-]+/DELIVERY_PLAN\.md', body):
        print(f'FAIL: PROD-L6 accepted-state delivery pointer model has legacy per-delivery plan path in {rel}')
        sys.exit(1)

regression_text = (root/'tools/test_validator_regressions.py').read_text(errors='ignore')
for phrase in ['accepted-state legacy per-delivery plan pointer fails', 'archive manifest missing normalization fails']:
    if phrase not in regression_text:
        print(f'FAIL: PROD-L6 regression suite missing fixture: {phrase}')
        sys.exit(1)

print('PASS: HIRMOS PROD-L6 accepted-state and history/archive alignment static check')


# PROD-L8 legacy surface removal and first-version alignment checks
first_version_forbidden_markers = [
    'REQUIREMENTS_BASELINE.md',
    'REQUIREMENTS_BASELINE',
    'SESSION_CONTRACT.md',
    'SESSION_CONTRACT',
    'session_contract',
    'legacy-compatible',
    'During PROD-L migration',
    'PROD-L scope-authority transition',
    'current artifact model',
    'Existing archived sessions do not need migration',
    'No breaking framework migration',
]
project_specific_forbidden_markers = [
    'MenuGen',
    'SAM.gov',
    'Hermes',
    'OpenSpec',
    'AI-assisted content-processing',
    'content-processing web app',
    'payment checkout',
    'credit/usage',
    'credits/usage',
    'credit-like allowance',
]
first_version_excluded = {
    'tools/validate.py',
    'tools/test_validator_regressions.py',
}
text_suffixes = {'.md', '.json', '.txt', '.yml', '.yaml'}
for candidate in root.rglob('*'):
    if not candidate.is_file():
        continue
    rel = str(candidate.relative_to(root))
    if rel in first_version_excluded:
        continue
    if candidate.suffix not in text_suffixes:
        continue
    body = candidate.read_text(errors='ignore')
    for marker in first_version_forbidden_markers + project_specific_forbidden_markers:
        if marker in body:
            fail(f'PROD-L8 first-version/project-agnostic surface contains forbidden marker {marker!r}: {rel}')
for legacy_path in [
    root/'core/protocol/REQUIREMENTS_BASELINE.md',
    root/'core/templates/session/REQUIREMENTS_BASELINE.md',
    root/'system/accepted-state/REQUIREMENTS_BASELINE.md',
    root/'core/templates/session/SESSION_CONTRACT.md',
]:
    if legacy_path.exists():
        fail(f'PROD-L8 legacy artifact path still exists: {legacy_path.relative_to(root)}')
for required_path in [
    root/'core/protocol/REQUIREMENTS.md',
    root/'core/templates/session/REQUIREMENTS.md',
    root/'system/accepted-state/REQUIREMENTS.md',
    root/'docs/2-methodology/requirements-and-coverage.md',
]:
    if not required_path.exists():
        fail(f'PROD-L8 canonical requirements path missing: {required_path.relative_to(root)}')
print('PASS: HIRMOS PROD-L8 legacy surface removal and first-version alignment static check')


# PROD-L8.5 session execution ledger slimming and responsibility realignment checks
execution_template = (root / 'core/templates/session/SESSION_EXECUTION.md').read_text()
execution_lines = execution_template.splitlines()
if len(execution_lines) > 575:
    fail(f'PROD-L8.5 SESSION_EXECUTION.md is too large for the slim ledger model: {len(execution_lines)} lines')
for phrase in [
    'active-session execution ledger',
    'must not own scope, requirements, design decisions, evidence details, unresolved-item details, accepted-state truth, or archive transaction details',
    'Pointer-only summary',
    'Pointers only. Evidence details belong in `EVIDENCE.md`',
    'Detailed archive transaction belongs in `ARCHIVE_MANIFEST.md`',
    'Use this only when a separate `REQUIREMENTS.md` authority exists',
]:
    if phrase not in execution_template:
        fail(f'PROD-L8.5 SESSION_EXECUTION.md missing slim-ledger phrase: {phrase}')
for forbidden in [
    '## Requirements Baseline Controls',
    '## Production-Shaped Engineering Gate Execution',
    '## Material Artifact References',
    '## Evidence Log\n\n| Seq | Evidence type',
]:
    if forbidden in execution_template:
        fail(f'PROD-L8.5 SESSION_EXECUTION.md retains broad/duplicative authority section: {forbidden}')
if execution_template.count('## Phase Progress / Carry-Forward Record') != 1:
    fail('PROD-L8.5 SESSION_EXECUTION.md must contain exactly one Phase Progress / Carry-Forward Record section')
if execution_template.count('## Phase Acceptance Enforcement Record') != 1:
    fail('PROD-L8.5 SESSION_EXECUTION.md must contain exactly one Phase Acceptance Enforcement Record section')
print('PASS: HIRMOS PROD-L8.5 session execution ledger slimming static check')
