import fs from "fs";
import os from "os";
import path from "path";
import { execFileSync } from "child_process";
import { fail } from "./errors";
import { ensureDir, pathExists } from "./filesystem";

const RELEASE_OWNER = "ymarrerot";
const RELEASE_REPO = "HIRMOS";
const RELEASE_ASSET = "hirmos-framework.zip";

export interface EnsureHirmosInstalledOptions {
  source?: string;
  version: string;
  offline: boolean;
}

export interface EnsureHirmosInstalledResult {
  installed: boolean;
  sourceDescription: string | null;
}

export function ensureHirmosInstalled(projectRoot: string, options: EnsureHirmosInstalledOptions): EnsureHirmosInstalledResult {
  const hirmosDir = path.join(projectRoot, "_hirmos");
  if (pathExists(hirmosDir)) {
    return { installed: false, sourceDescription: null };
  }

  if (options.source) {
    installFromSource(projectRoot, options.source);
    return { installed: true, sourceDescription: options.source };
  }

  if (options.offline) {
    fail(`Missing _hirmos/ in ${projectRoot}. Offline mode requires an existing _hirmos/ or --source <path-to-hirmos-framework.zip-or-folder>.`);
  }

  const version = normalizeReleaseVersion(options.version);
  const url = buildReleaseDownloadUrl(version);
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "hirmos-release-"));
  const zipPath = path.join(tmp, RELEASE_ASSET);
  try {
    downloadFile(url, zipPath);
    installFromZip(projectRoot, zipPath);
    return { installed: true, sourceDescription: version === "latest" ? "latest GitHub release" : `GitHub release ${version}` };
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }
}

export function buildReleaseDownloadUrl(version: string): string {
  const normalized = normalizeReleaseVersion(version);
  const overrideBase = process.env.HIRMOS_CLI_RELEASE_BASE_URL;
  if (overrideBase) {
    const trimmed = overrideBase.replace(/\/+$/u, "");
    return `${trimmed}/${normalized}/${RELEASE_ASSET}`;
  }

  if (normalized === "latest") {
    return `https://github.com/${RELEASE_OWNER}/${RELEASE_REPO}/releases/latest/download/${RELEASE_ASSET}`;
  }

  return `https://github.com/${RELEASE_OWNER}/${RELEASE_REPO}/releases/download/${normalized}/${RELEASE_ASSET}`;
}

export function normalizeReleaseVersion(version: string): string {
  const trimmed = version.trim();
  if (!trimmed || trimmed === "latest") return "latest";
  return trimmed.startsWith("v") ? trimmed : `v${trimmed}`;
}

function installFromSource(projectRoot: string, source: string): void {
  if (!pathExists(source)) {
    fail(`Source path does not exist: ${source}`);
  }

  const stat = fs.statSync(source);
  if (stat.isDirectory()) {
    installFromDirectory(projectRoot, source);
    return;
  }

  if (stat.isFile() && source.toLowerCase().endsWith(".zip")) {
    installFromZip(projectRoot, source);
    return;
  }

  fail(`Unsupported --source. Expected a .zip, a folder containing _hirmos, or an _hirmos folder: ${source}`);
}

function installFromDirectory(projectRoot: string, sourceDir: string): void {
  const sourceHirmos = path.basename(sourceDir) === "_hirmos" ? sourceDir : path.join(sourceDir, "_hirmos");
  if (!pathExists(sourceHirmos) || !fs.statSync(sourceHirmos).isDirectory()) {
    fail(`Source folder does not contain _hirmos/: ${sourceDir}`);
  }
  copyHirmos(projectRoot, sourceHirmos);
}

function installFromZip(projectRoot: string, zipPath: string): void {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "hirmos-cli-"));
  try {
    try {
      extractZip(zipPath, tmp);
    } catch (error: any) {
      fail(`Unable to extract framework zip. Ensure the zip is valid and an extraction command is available: ${error.message}`);
    }

    const sourceHirmos = findHirmosDir(tmp);
    if (!sourceHirmos) {
      fail(`Framework zip does not contain an _hirmos/ folder: ${zipPath}`);
    }
    copyHirmos(projectRoot, sourceHirmos);
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }
}

function findHirmosDir(root: string): string | null {
  const direct = path.join(root, "_hirmos");
  if (pathExists(direct) && fs.statSync(direct).isDirectory()) return direct;

  const entries = fs.readdirSync(root, { withFileTypes: true });
  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const candidate = path.join(root, entry.name, "_hirmos");
    if (pathExists(candidate) && fs.statSync(candidate).isDirectory()) return candidate;
  }
  return null;
}

function copyHirmos(projectRoot: string, sourceHirmos: string): void {
  const target = path.join(projectRoot, "_hirmos");
  if (pathExists(target)) {
    fail(`Refusing to overwrite existing _hirmos/: ${target}`);
  }
  ensureDir(projectRoot);
  fs.cpSync(sourceHirmos, target, { recursive: true, errorOnExist: true });
  validateCopiedHirmos(projectRoot);
}

function validateCopiedHirmos(projectRoot: string): void {
  const required = ["_hirmos/HIRMOS_CORE.md", "_hirmos/VERSION", "_hirmos/project.json"];
  for (const relative of required) {
    if (!pathExists(path.join(projectRoot, relative))) {
      fs.rmSync(path.join(projectRoot, "_hirmos"), { recursive: true, force: true });
      fail(`Installed framework is incomplete; missing ${relative}. Removed partial _hirmos/ install.`);
    }
  }
}

function extractZip(zipPath: string, destination: string): void {
  if (process.platform === "win32") {
    execFileSync("powershell", ["-NoProfile", "-Command", "Expand-Archive", "-LiteralPath", zipPath, "-DestinationPath", destination, "-Force"], { stdio: "ignore" });
    return;
  }

  execFileSync("unzip", ["-q", zipPath, "-d", destination], { stdio: "ignore" });
}

function downloadFile(url: string, destination: string): void {
  ensureDir(path.dirname(destination));

  try {
    if (process.platform === "win32") {
      execFileSync("powershell", [
        "-NoProfile",
        "-Command",
        "$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri $args[0] -OutFile $args[1]",
        url,
        destination
      ], { stdio: "ignore" });
    } else {
      execFileSync("curl", ["-fL", "--retry", "2", "--connect-timeout", "20", "--max-time", "120", "-o", destination, url], { stdio: "ignore" });
    }
  } catch (error: any) {
    fail(`Unable to download HIRMOS release from ${url}. Use --source for a local release package or --offline to disable downloads. ${error.message}`);
  }

  if (!pathExists(destination) || fs.statSync(destination).size === 0) {
    fail(`Downloaded HIRMOS release is empty or missing: ${destination}`);
  }
}
