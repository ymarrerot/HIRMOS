import fs from "fs";
import path from "path";
import { fail } from "./errors";

export function ensureDir(dirPath: string): void {
  fs.mkdirSync(dirPath, { recursive: true });
}

export function readText(filePath: string): string {
  return fs.readFileSync(filePath, "utf8");
}

export function writeText(filePath: string, content: string): void {
  ensureDir(path.dirname(filePath));
  fs.writeFileSync(filePath, content, "utf8");
}

export function readJson<T>(filePath: string, label: string): T {
  try {
    return JSON.parse(readText(filePath)) as T;
  } catch (error: any) {
    fail(`Invalid ${label} JSON at ${filePath}: ${error.message}`);
  }
}

export function writeJson(filePath: string, value: unknown): void {
  writeText(filePath, `${JSON.stringify(value, null, 2)}\n`);
}

export function assertInsideProject(projectRoot: string, targetPath: string): void {
  const relative = path.relative(projectRoot, targetPath);
  if (relative.startsWith("..") || path.isAbsolute(relative)) {
    fail(`Refusing to write outside the project root: ${targetPath}`);
  }
}

export function pathExists(filePath: string): boolean {
  return fs.existsSync(filePath);
}
