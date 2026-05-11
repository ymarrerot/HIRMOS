#!/usr/bin/env node
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const args_1 = require("./lib/args");
const errors_1 = require("./lib/errors");
const init_1 = require("./commands/init");
const update_notice_1 = require("./lib/update-notice");
function main() {
    try {
        const parsed = (0, args_1.parseArgs)(process.argv.slice(2));
        if (parsed.command === "help") {
            process.stdout.write((0, args_1.helpText)());
            return;
        }
        if (parsed.command === "init") {
            if (!parsed.offline) {
                const updateNotice = (0, update_notice_1.getUpdateNotice)();
                if (updateNotice)
                    process.stderr.write(`${(0, update_notice_1.formatUpdateNotice)(updateNotice)}

`);
            }
            const summary = (0, init_1.runInit)({
                projectPath: parsed.projectPath,
                integrations: parsed.integrations,
                source: parsed.source,
                version: parsed.version,
                offline: parsed.offline
            });
            process.stdout.write(summary);
            return;
        }
    }
    catch (error) {
        if (error instanceof errors_1.HirmosCliError) {
            process.stderr.write(`ERROR: ${error.message}\n`);
            process.exitCode = 1;
            return;
        }
        process.stderr.write(`ERROR: ${error?.message ?? String(error)}\n`);
        process.exitCode = 1;
    }
}
if (require.main === module) {
    main();
}
