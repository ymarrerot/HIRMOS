import fs from "fs";
import path from "path";
import { spawnSync } from "child_process";

const PACKAGE_NAME = "hirmos";
const DEFAULT_TIMEOUT_MS = 1500;
const ANSI_BOLD = "\u001b[1m";
const ANSI_YELLOW = "\u001b[33m";
const ANSI_RESET = "\u001b[0m";


export function getInstalledCliVersion(cliRoot = path.resolve(__dirname, "../..")): string | null {
  try {
    const packageJsonPath = path.join(cliRoot, "package.json");
    const raw = fs.readFileSync(packageJsonPath, "utf8");
    const parsed = JSON.parse(raw) as { version?: unknown };
    return typeof parsed.version === "string" && parsed.version.trim() ? parsed.version.trim() : null;
  } catch {
    return null;
  }
}

export function normalizeSemver(value: string): string {
  return value.trim().replace(/^v/u, "").split("-")[0];
}

export function compareSemver(left: string, right: string): number {
  const leftParts = normalizeSemver(left).split(".").map((part) => Number.parseInt(part, 10));
  const rightParts = normalizeSemver(right).split(".").map((part) => Number.parseInt(part, 10));

  for (let i = 0; i < 3; i += 1) {
    const leftValue = Number.isFinite(leftParts[i]) ? leftParts[i] : 0;
    const rightValue = Number.isFinite(rightParts[i]) ? rightParts[i] : 0;
    if (leftValue > rightValue) return 1;
    if (leftValue < rightValue) return -1;
  }
  return 0;
}

export function buildUpdateNotice(currentVersion: string | null, latestVersion: string | null): string | null {
  if (!currentVersion || !latestVersion) return null;
  if (compareSemver(latestVersion, currentVersion) <= 0) return null;
  return `A newer HIRMOS CLI is available: ${latestVersion}.\nUpdate with: npm install -g ${PACKAGE_NAME}@latest`;
}

export function formatUpdateNotice(message: string, useColor = Boolean(process.stderr.isTTY) && process.env.NO_COLOR === undefined): string {
  return useColor ? `${ANSI_BOLD}${ANSI_YELLOW}${message}${ANSI_RESET}` : message;
}

export function getLatestPublishedVersion(timeoutMs = DEFAULT_TIMEOUT_MS): string | null {
  if (process.env.HIRMOS_CLI_UPDATE_CHECK === "0" || process.env.HIRMOS_NO_UPDATE_CHECK === "1") {
    return null;
  }

  try {
    const result = spawnSync("npm", ["view", PACKAGE_NAME, "version", "--silent"], {
      encoding: "utf8",
      stdio: ["ignore", "pipe", "ignore"],
      timeout: timeoutMs
    });

    if (result.error || result.status !== 0) return null;
    const version = String(result.stdout ?? "").trim();
    return /^v?\d+\.\d+\.\d+(?:[-+][A-Za-z0-9.-]+)?$/u.test(version) ? version : null;
  } catch {
    return null;
  }
}

export function getUpdateNotice(): string | null {
  return buildUpdateNotice(getInstalledCliVersion(), getLatestPublishedVersion());
}
