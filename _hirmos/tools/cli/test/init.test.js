const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const childProcess = require('node:child_process');

const cli = path.resolve(__dirname, '../dist/index.js');
const privateRoot = path.resolve(__dirname, '../../../../');

function tempProject() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'hirmos-cli-test-'));
  fs.cpSync(path.join(privateRoot, '_hirmos'), path.join(dir, '_hirmos'), { recursive: true });
  return dir;
}

function run(args, cwd) {
  return childProcess.spawnSync(process.execPath, [cli, ...args], { cwd, encoding: 'utf8' });
}

test('init creates default AGENTS.md and records agents integration', () => {
  const project = tempProject();
  const result = run(['init', project], project);
  assert.equal(result.status, 0, result.stderr);
  assert.match(fs.readFileSync(path.join(project, 'AGENTS.md'), 'utf8'), /_hirmos\/HIRMOS_CORE\.md/);
  const config = JSON.parse(fs.readFileSync(path.join(project, '_hirmos/project.json'), 'utf8'));
  assert.deepEqual(config.integrations.installed, ['agents']);
});

test('init adds multiple integrations and preserves existing AGENTS content', () => {
  const project = tempProject();
  fs.writeFileSync(path.join(project, 'AGENTS.md'), '# Existing Agent Notes\n', 'utf8');
  const first = run(['init', project, '--integration', 'agents'], project);
  assert.equal(first.status, 0, first.stderr);
  const second = run(['init', project, '--integration', 'claude,cursor,copilot'], project);
  assert.equal(second.status, 0, second.stderr);
  assert.match(fs.readFileSync(path.join(project, 'AGENTS.md'), 'utf8'), /# Existing Agent Notes/);
  assert.ok(fs.existsSync(path.join(project, 'CLAUDE.md')));
  assert.ok(fs.existsSync(path.join(project, '.cursor/rules/hirmos.mdc')));
  assert.ok(fs.existsSync(path.join(project, '.github/copilot-instructions.md')));
  const config = JSON.parse(fs.readFileSync(path.join(project, '_hirmos/project.json'), 'utf8'));
  assert.deepEqual(config.integrations.installed, ['agents', 'claude', 'cursor', 'copilot']);
});

test('shared target integrations update AGENTS.md once while recording all selected ids', () => {
  const project = tempProject();
  const result = run(['init', project, '--integration', 'agents,codex,opencode'], project);
  assert.equal(result.status, 0, result.stderr);
  const agents = fs.readFileSync(path.join(project, 'AGENTS.md'), 'utf8');
  assert.equal((agents.match(/<!-- HIRMOS:START -->/g) || []).length, 1);
  const config = JSON.parse(fs.readFileSync(path.join(project, '_hirmos/project.json'), 'utf8'));
  assert.deepEqual(config.integrations.installed, ['agents', 'codex', 'opencode']);
});

test('invalid integration fails clearly', () => {
  const project = tempProject();
  const result = run(['init', project, '--integration', 'unknown'], project);
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /Unknown integration id/);
});

test('source folder install copies _hirmos when target project lacks it', () => {
  const project = fs.mkdtempSync(path.join(os.tmpdir(), 'hirmos-cli-source-test-'));
  const result = run(['init', project, '--source', privateRoot, '--integration', 'agents'], project);
  assert.equal(result.status, 0, result.stderr);
  assert.ok(fs.existsSync(path.join(project, '_hirmos/HIRMOS_CORE.md')));
  assert.ok(fs.existsSync(path.join(project, 'AGENTS.md')));
});


test('offline mode fails clearly when _hirmos is missing and no source is provided', () => {
  const project = fs.mkdtempSync(path.join(os.tmpdir(), 'hirmos-cli-offline-test-'));
  const result = run(['init', project, '--offline'], project);
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /Offline mode requires/);
});
