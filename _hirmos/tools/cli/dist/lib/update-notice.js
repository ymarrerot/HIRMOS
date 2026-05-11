"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getInstalledCliVersion = getInstalledCliVersion;
exports.normalizeSemver = normalizeSemver;
exports.compareSemver = compareSemver;
exports.buildUpdateNotice = buildUpdateNotice;
exports.formatUpdateNotice = formatUpdateNotice;
exports.getLatestPublishedVersion = getLatestPublishedVersion;
exports.getUpdateNotice = getUpdateNotice;
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
const child_process_1 = require("child_process");
const PACKAGE_NAME = "hirmos";
const DEFAULT_TIMEOUT_MS = 1500;
const ANSI_BOLD = "\u001b[1m";
const ANSI_YELLOW = "\u001b[33m";
const ANSI_RESET = "\u001b[0m";
function getInstalledCliVersion(cliRoot = path_1.default.resolve(__dirname, "../..")) {
    try {
        const packageJsonPath = path_1.default.join(cliRoot, "package.json");
        const raw = fs_1.default.readFileSync(packageJsonPath, "utf8");
        const parsed = JSON.parse(raw);
        return typeof parsed.version === "string" && parsed.version.trim() ? parsed.version.trim() : null;
    }
    catch {
        return null;
    }
}
function normalizeSemver(value) {
    return value.trim().replace(/^v/u, "").split("-")[0];
}
function compareSemver(left, right) {
    const leftParts = normalizeSemver(left).split(".").map((part) => Number.parseInt(part, 10));
    const rightParts = normalizeSemver(right).split(".").map((part) => Number.parseInt(part, 10));
    for (let i = 0; i < 3; i += 1) {
        const leftValue = Number.isFinite(leftParts[i]) ? leftParts[i] : 0;
        const rightValue = Number.isFinite(rightParts[i]) ? rightParts[i] : 0;
        if (leftValue > rightValue)
            return 1;
        if (leftValue < rightValue)
            return -1;
    }
    return 0;
}
function buildUpdateNotice(currentVersion, latestVersion) {
    if (!currentVersion || !latestVersion)
        return null;
    if (compareSemver(latestVersion, currentVersion) <= 0)
        return null;
    return `A newer HIRMOS CLI is available: ${latestVersion}.\nUpdate with: npm install -g ${PACKAGE_NAME}@latest`;
}
function formatUpdateNotice(message, useColor = Boolean(process.stderr.isTTY) && process.env.NO_COLOR === undefined) {
    return useColor ? `${ANSI_BOLD}${ANSI_YELLOW}${message}${ANSI_RESET}` : message;
}
function getLatestPublishedVersion(timeoutMs = DEFAULT_TIMEOUT_MS) {
    if (process.env.HIRMOS_CLI_UPDATE_CHECK === "0" || process.env.HIRMOS_NO_UPDATE_CHECK === "1") {
        return null;
    }
    try {
        const result = (0, child_process_1.spawnSync)("npm", ["view", PACKAGE_NAME, "version", "--silent"], {
            encoding: "utf8",
            stdio: ["ignore", "pipe", "ignore"],
            timeout: timeoutMs
        });
        if (result.error || result.status !== 0)
            return null;
        const version = String(result.stdout ?? "").trim();
        return /^v?\d+\.\d+\.\d+(?:[-+][A-Za-z0-9.-]+)?$/u.test(version) ? version : null;
    }
    catch {
        return null;
    }
}
function getUpdateNotice() {
    return buildUpdateNotice(getInstalledCliVersion(), getLatestPublishedVersion());
}
