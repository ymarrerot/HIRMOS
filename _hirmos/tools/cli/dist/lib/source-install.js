"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.ensureHirmosInstalled = ensureHirmosInstalled;
exports.buildReleaseDownloadUrl = buildReleaseDownloadUrl;
exports.normalizeReleaseVersion = normalizeReleaseVersion;
const fs_1 = __importDefault(require("fs"));
const os_1 = __importDefault(require("os"));
const path_1 = __importDefault(require("path"));
const child_process_1 = require("child_process");
const errors_1 = require("./errors");
const filesystem_1 = require("./filesystem");
const RELEASE_OWNER = "ymarrerot";
const RELEASE_REPO = "HIRMOS";
const RELEASE_ASSET = "hirmos-framework.zip";
function ensureHirmosInstalled(projectRoot, options) {
    const hirmosDir = path_1.default.join(projectRoot, "_hirmos");
    if ((0, filesystem_1.pathExists)(hirmosDir)) {
        return { installed: false, sourceDescription: null };
    }
    if (options.source) {
        installFromSource(projectRoot, options.source);
        return { installed: true, sourceDescription: options.source };
    }
    if (options.offline) {
        (0, errors_1.fail)(`Missing _hirmos/ in ${projectRoot}. Offline mode requires an existing _hirmos/ or --source <path-to-hirmos-framework.zip-or-folder>.`);
    }
    const version = normalizeReleaseVersion(options.version);
    const url = buildReleaseDownloadUrl(version);
    const tmp = fs_1.default.mkdtempSync(path_1.default.join(os_1.default.tmpdir(), "hirmos-release-"));
    const zipPath = path_1.default.join(tmp, RELEASE_ASSET);
    try {
        downloadFile(url, zipPath);
        installFromZip(projectRoot, zipPath);
        return { installed: true, sourceDescription: version === "latest" ? "latest GitHub release" : `GitHub release ${version}` };
    }
    finally {
        fs_1.default.rmSync(tmp, { recursive: true, force: true });
    }
}
function buildReleaseDownloadUrl(version) {
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
function normalizeReleaseVersion(version) {
    const trimmed = version.trim();
    if (!trimmed || trimmed === "latest")
        return "latest";
    return trimmed.startsWith("v") ? trimmed : `v${trimmed}`;
}
function installFromSource(projectRoot, source) {
    if (!(0, filesystem_1.pathExists)(source)) {
        (0, errors_1.fail)(`Source path does not exist: ${source}`);
    }
    const stat = fs_1.default.statSync(source);
    if (stat.isDirectory()) {
        installFromDirectory(projectRoot, source);
        return;
    }
    if (stat.isFile() && source.toLowerCase().endsWith(".zip")) {
        installFromZip(projectRoot, source);
        return;
    }
    (0, errors_1.fail)(`Unsupported --source. Expected a .zip, a folder containing _hirmos, or an _hirmos folder: ${source}`);
}
function installFromDirectory(projectRoot, sourceDir) {
    const sourceHirmos = path_1.default.basename(sourceDir) === "_hirmos" ? sourceDir : path_1.default.join(sourceDir, "_hirmos");
    if (!(0, filesystem_1.pathExists)(sourceHirmos) || !fs_1.default.statSync(sourceHirmos).isDirectory()) {
        (0, errors_1.fail)(`Source folder does not contain _hirmos/: ${sourceDir}`);
    }
    copyHirmos(projectRoot, sourceHirmos);
}
function installFromZip(projectRoot, zipPath) {
    const tmp = fs_1.default.mkdtempSync(path_1.default.join(os_1.default.tmpdir(), "hirmos-cli-"));
    try {
        try {
            extractZip(zipPath, tmp);
        }
        catch (error) {
            (0, errors_1.fail)(`Unable to extract framework zip. Ensure the zip is valid and an extraction command is available: ${error.message}`);
        }
        const sourceHirmos = findHirmosDir(tmp);
        if (!sourceHirmos) {
            (0, errors_1.fail)(`Framework zip does not contain an _hirmos/ folder: ${zipPath}`);
        }
        copyHirmos(projectRoot, sourceHirmos);
    }
    finally {
        fs_1.default.rmSync(tmp, { recursive: true, force: true });
    }
}
function findHirmosDir(root) {
    const direct = path_1.default.join(root, "_hirmos");
    if ((0, filesystem_1.pathExists)(direct) && fs_1.default.statSync(direct).isDirectory())
        return direct;
    const entries = fs_1.default.readdirSync(root, { withFileTypes: true });
    for (const entry of entries) {
        if (!entry.isDirectory())
            continue;
        const candidate = path_1.default.join(root, entry.name, "_hirmos");
        if ((0, filesystem_1.pathExists)(candidate) && fs_1.default.statSync(candidate).isDirectory())
            return candidate;
    }
    return null;
}
function copyHirmos(projectRoot, sourceHirmos) {
    const target = path_1.default.join(projectRoot, "_hirmos");
    if ((0, filesystem_1.pathExists)(target)) {
        (0, errors_1.fail)(`Refusing to overwrite existing _hirmos/: ${target}`);
    }
    (0, filesystem_1.ensureDir)(projectRoot);
    fs_1.default.cpSync(sourceHirmos, target, { recursive: true, errorOnExist: true });
    validateCopiedHirmos(projectRoot);
}
function validateCopiedHirmos(projectRoot) {
    const required = ["_hirmos/HIRMOS_CORE.md", "_hirmos/VERSION", "_hirmos/project.json"];
    for (const relative of required) {
        if (!(0, filesystem_1.pathExists)(path_1.default.join(projectRoot, relative))) {
            fs_1.default.rmSync(path_1.default.join(projectRoot, "_hirmos"), { recursive: true, force: true });
            (0, errors_1.fail)(`Installed framework is incomplete; missing ${relative}. Removed partial _hirmos/ install.`);
        }
    }
}
function extractZip(zipPath, destination) {
    if (process.platform === "win32") {
        (0, child_process_1.execFileSync)("powershell", ["-NoProfile", "-Command", "Expand-Archive", "-LiteralPath", zipPath, "-DestinationPath", destination, "-Force"], { stdio: "ignore" });
        return;
    }
    (0, child_process_1.execFileSync)("unzip", ["-q", zipPath, "-d", destination], { stdio: "ignore" });
}
function downloadFile(url, destination) {
    (0, filesystem_1.ensureDir)(path_1.default.dirname(destination));
    try {
        if (process.platform === "win32") {
            (0, child_process_1.execFileSync)("powershell", [
                "-NoProfile",
                "-Command",
                "$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri $args[0] -OutFile $args[1]",
                url,
                destination
            ], { stdio: "ignore" });
        }
        else {
            (0, child_process_1.execFileSync)("curl", ["-fL", "--retry", "2", "--connect-timeout", "20", "--max-time", "120", "-o", destination, url], { stdio: "ignore" });
        }
    }
    catch (error) {
        (0, errors_1.fail)(`Unable to download HIRMOS release from ${url}. Use --source for a local release package or --offline to disable downloads. ${error.message}`);
    }
    if (!(0, filesystem_1.pathExists)(destination) || fs_1.default.statSync(destination).size === 0) {
        (0, errors_1.fail)(`Downloaded HIRMOS release is empty or missing: ${destination}`);
    }
}
