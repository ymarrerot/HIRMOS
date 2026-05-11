import fs from "fs";
import path from "path";
import { fail } from "./errors";
import { pathExists } from "./filesystem";

export function validateProjectRoot(projectRoot: string): void {
  if (!pathExists(projectRoot)) {
    fail(`Project path does not exist: ${projectRoot}`);
  }
  if (!fs.statSync(projectRoot).isDirectory()) {
    fail(`Project path is not a directory: ${projectRoot}`);
  }
}

export function validateHirmosFramework(projectRoot: string): void {
  const required = [
    "_hirmos/HIRMOS_CORE.md",
    "_hirmos/project.json",
    "_hirmos/integrations/agent-tools/registry.json"
  ];

  for (const relative of required) {
    const absolute = path.join(projectRoot, relative);
    if (!pathExists(absolute)) {
      fail(`Required HIRMOS file is missing: ${relative}`);
    }
  }

  const templatesDir = path.join(projectRoot, "_hirmos", "integrations/agent-tools", "templates");
  if (!pathExists(templatesDir) || !fs.statSync(templatesDir).isDirectory()) {
    fail("Required HIRMOS directory is missing: _hirmos/integrations/agent-tools/templates/");
  }
}
