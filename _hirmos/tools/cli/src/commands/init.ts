import fs from "fs";
import path from "path";
import { assertInsideProject, readText, writeText } from "../lib/filesystem";
import { loadRegistry, normalizeSelectedIntegrations, planTargetUpdates } from "../lib/integration-registry";
import { updateManagedBlock } from "../lib/managed-blocks";
import { loadProjectConfig, mergeProjectConfig, writeProjectConfig } from "../lib/project-config";
import { ensureHirmosInstalled } from "../lib/source-install";
import { validateHirmosFramework, validateProjectRoot } from "../lib/validation";

export interface RunInitOptions {
  projectPath: string;
  integrations: string[];
  source?: string;
  version: string;
  offline: boolean;
}

export function runInit(options: RunInitOptions): string {
  const projectRoot = path.resolve(options.projectPath);
  validateProjectRoot(projectRoot);
  const installResult = ensureHirmosInstalled(projectRoot, {
    source: options.source,
    version: options.version,
    offline: options.offline
  });
  validateHirmosFramework(projectRoot);

  const hirmosDir = path.join(projectRoot, "_hirmos");
  const registry = loadRegistry(hirmosDir);
  const selected = normalizeSelectedIntegrations(options.integrations, registry);
  const plannedTargets = planTargetUpdates(projectRoot, hirmosDir, selected, registry);
  const currentConfig = loadProjectConfig(projectRoot);
  const mergeResult = mergeProjectConfig(currentConfig, selected, registry);

  const renderedWrites = plannedTargets.map((target) => {
    assertInsideProject(projectRoot, target.targetPath);
    const existing = fs.existsSync(target.targetPath) ? readText(target.targetPath) : null;
    const nextContent = updateManagedBlock(existing, target.templateContent, registry.managed_block, target.target);
    return {
      path: target.targetPath,
      relative: target.target,
      content: nextContent,
      integrationIds: target.integrationIds
    };
  });

  for (const write of renderedWrites) {
    writeText(write.path, write.content);
  }
  writeProjectConfig(projectRoot, mergeResult.config);

  return formatInitSummary(mergeResult.wasFirstInitialization, selected, mergeResult.added, mergeResult.alreadyInstalled, renderedWrites.map((item) => item.relative), installResult);
}

function formatInitSummary(first: boolean, selected: string[], added: string[], alreadyInstalled: string[], targets: string[], installResult: { installed: boolean; sourceDescription: string | null }): string {
  const lines: string[] = [];

  if (first) {
    lines.push("HIRMOS initialized.", "");
    if (installResult.installed && installResult.sourceDescription) {
      lines.push(`Installed framework from ${installResult.sourceDescription}.`, "");
    }
    lines.push("Installed integrations:");
    for (const id of selected) lines.push(`- ${id}`);
    lines.push("", "Generated or updated files:");
    for (const target of targets) lines.push(`- ${target}`);
    lines.push("", "Next step:");
    lines.push("Open your AI coding tool in this project and run a HIRMOS workflow command, for example:");
    lines.push("");
    lines.push("hirmos requirements");
    lines.push("hirmos system-design");
    lines.push("hirmos implementation");
    lines.push("");
    lines.push("Fallback initialization:");
    lines.push("If your tool does not automatically pick up the selected agent/tool integration files, copy and paste this prompt into your agent:");
    lines.push("");
    lines.push("Read and follow the instructions on _hirmos/HIRMOS_CORE.md.");
    lines.push("", "To add more integrations later:");
    lines.push("hirmos init --integration claude,cursor,copilot");
    return `${lines.join("\n")}\n`;
  }

  lines.push("HIRMOS integrations updated.", "");
  if (added.length > 0) {
    lines.push("Added:");
    for (const id of added) lines.push(`- ${id}`);
    lines.push("");
  }
  if (alreadyInstalled.length > 0) {
    lines.push("Already installed:");
    for (const id of alreadyInstalled) lines.push(`- ${id}`);
    lines.push("");
  }
  lines.push("Generated or updated files:");
  for (const target of targets) lines.push(`- ${target}`);
  return `${lines.join("\n").replace(/\n+$/u, "")}\n`;
}
