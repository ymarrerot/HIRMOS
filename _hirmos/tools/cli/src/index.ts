#!/usr/bin/env node
import { parseArgs, helpText } from "./lib/args";
import { HirmosCliError } from "./lib/errors";
import { runInit } from "./commands/init";
import { formatUpdateNotice, getUpdateNotice } from "./lib/update-notice";

function main(): void {
  try {
    const parsed = parseArgs(process.argv.slice(2));
    if (parsed.command === "help") {
      process.stdout.write(helpText());
      return;
    }

    if (parsed.command === "init") {
      if (!parsed.offline) {
        const updateNotice = getUpdateNotice();
        if (updateNotice) process.stderr.write(`${formatUpdateNotice(updateNotice)}

`);
      }

      const summary = runInit({
        projectPath: parsed.projectPath,
        integrations: parsed.integrations,
        source: parsed.source,
        version: parsed.version,
        offline: parsed.offline
      });
      process.stdout.write(summary);
      return;
    }
  } catch (error: any) {
    if (error instanceof HirmosCliError) {
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
