import path from "path";
import { fail } from "./errors";
import { readJson, readText } from "./filesystem";
import { ManagedBlockMarkers, validateTemplateManagedBlock } from "./managed-blocks";

export interface IntegrationDefinition {
  description: string;
  target: string;
  template: string;
  mode: "managed_block";
  target_class?: string;
  shares_target_with?: string[];
}

export interface IntegrationRegistry {
  schema_version: number;
  managed_block: ManagedBlockMarkers;
  integrations: Record<string, IntegrationDefinition>;
  source?: string;
}

export interface PlannedTargetUpdate {
  target: string;
  targetPath: string;
  templatePath: string;
  templateContent: string;
  integrationIds: string[];
}

export function loadRegistry(hirmosDir: string): IntegrationRegistry {
  const registryPath = path.join(hirmosDir, "integrations/agent-tools", "registry.json");
  const registry = readJson<IntegrationRegistry>(registryPath, "agent integration registry");
  if (!registry || typeof registry !== "object") fail("Agent integration registry is malformed.");
  if (registry.schema_version !== 1) fail(`Unsupported agent integration registry schema_version: ${registry.schema_version}`);
  if (!registry.managed_block?.start || !registry.managed_block?.end) fail("Agent integration registry is missing managed block markers.");
  if (!registry.integrations || typeof registry.integrations !== "object") fail("Agent integration registry is missing integrations.");
  return registry;
}

export function registryOrder(registry: IntegrationRegistry): string[] {
  return Object.keys(registry.integrations);
}

export function normalizeSelectedIntegrations(selected: string[], registry: IntegrationRegistry): string[] {
  const selectedSet = new Set<string>();
  for (const id of selected) {
    if (!registry.integrations[id]) {
      fail(`Unknown integration id: ${id}. Valid integrations: ${registryOrder(registry).join(", ")}`);
    }
    selectedSet.add(id);
  }
  return registryOrder(registry).filter((id) => selectedSet.has(id));
}

export function planTargetUpdates(projectRoot: string, hirmosDir: string, selected: string[], registry: IntegrationRegistry): PlannedTargetUpdate[] {
  const grouped = new Map<string, PlannedTargetUpdate>();

  for (const id of selected) {
    const integration = registry.integrations[id];
    if (integration.mode !== "managed_block") fail(`Unsupported integration mode for ${id}: ${integration.mode}`);

    const templatePath = path.join(hirmosDir, "integrations/agent-tools", integration.template);
    const templateContent = readText(templatePath);
    validateTemplateManagedBlock(templateContent, registry.managed_block, integration.template);

    const existing = grouped.get(integration.target);
    if (existing) {
      if (existing.templateContent !== templateContent) {
        fail(`Integrations sharing target ${integration.target} use different templates. Refusing ambiguous update.`);
      }
      existing.integrationIds.push(id);
      continue;
    }

    grouped.set(integration.target, {
      target: integration.target,
      targetPath: path.resolve(projectRoot, integration.target),
      templatePath,
      templateContent,
      integrationIds: [id]
    });
  }

  return Array.from(grouped.values());
}
