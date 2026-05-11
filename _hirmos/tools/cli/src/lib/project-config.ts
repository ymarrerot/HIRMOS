import path from "path";
import { readJson, writeJson } from "./filesystem";
import { IntegrationRegistry, registryOrder } from "./integration-registry";

export interface ProjectConfig {
  schema_version?: number;
  hirmos?: Record<string, unknown>;
  stack?: Record<string, unknown>;
  integrations?: {
    installed?: string[];
    [key: string]: unknown;
  };
  [key: string]: unknown;
}

export interface ProjectConfigMergeResult {
  config: ProjectConfig;
  previousInstalled: string[];
  added: string[];
  alreadyInstalled: string[];
  installed: string[];
  wasFirstInitialization: boolean;
}

export function loadProjectConfig(projectRoot: string): ProjectConfig {
  return readJson<ProjectConfig>(path.join(projectRoot, "_hirmos", "project.json"), "_hirmos/project.json");
}

export function mergeProjectConfig(config: ProjectConfig, selected: string[], registry: IntegrationRegistry): ProjectConfigMergeResult {
  const previousInstalled = Array.isArray(config.integrations?.installed)
    ? config.integrations!.installed!.filter((id): id is string => typeof id === "string")
    : [];

  const previousSet = new Set(previousInstalled);
  const selectedSet = new Set(selected);
  const added = selected.filter((id) => !previousSet.has(id));
  const alreadyInstalled = selected.filter((id) => previousSet.has(id));

  const knownOrder = registryOrder(registry);
  const allKnown = knownOrder.filter((id) => previousSet.has(id) || selectedSet.has(id));
  const unknownExisting = previousInstalled.filter((id) => !registry.integrations[id]);
  const installed = [...allKnown, ...unknownExisting];

  const nextConfig: ProjectConfig = {
    ...config,
    integrations: {
      ...(config.integrations ?? {}),
      installed
    }
  };

  return {
    config: nextConfig,
    previousInstalled,
    added,
    alreadyInstalled,
    installed,
    wasFirstInitialization: previousInstalled.length === 0
  };
}

export function writeProjectConfig(projectRoot: string, config: ProjectConfig): void {
  writeJson(path.join(projectRoot, "_hirmos", "project.json"), config);
}
