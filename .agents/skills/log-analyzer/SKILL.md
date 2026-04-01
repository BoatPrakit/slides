---
name: log-analyzer
description: A skill to parse server logs and find critical errors. Use this whenever the user asks to analyze server logs, look for errors, or investigate issues using log files.
---

# Log Analyzer

This skill helps you parse server logs to find and categorize critical errors and warnings according to specific guidelines.

## Instructions

1. **Extract Errors First**: When given a log file, DO NOT attempt to read the entire file into your context window. Instead, use the bundled Python script to extract only the error lines.
   ```bash
   python scripts/extract_errors.py <path-to-log-file>
   ```

2. **Categorize Log Entries**: Once you have the relevant lines, categorize them based on these rules:
   - **Critical Errors**: Any `[ERROR]` containing "OutOfMemory", "Database", or "Payment". These require immediate attention and MUST be highlighted in **bold** or <span style="color:red">red</span>.
   - **Warnings**: Any `[WARN]` related to "memory" or "disk space". These should be noted as infrastructure warnings.
   - **Routine**: `[INFO]` logs can generally be ignored unless the user specifically asks about user activity. *(Note: the python script currently only extracts `[ERROR]` lines, so you primarily only need to worry about the Critical Errors. If the user explicitly asks for warnings, you can also extract `[WARN]` lines using `grep` or by modifying the python script)*.

3. **Action Items**: You MUST provide a short **Recommended Action** for any Critical Error found in the logs.

## Output Format

Report your findings back to the user clearly. Example:

### Critical Errors
- **[ERROR] 2026-04-01 OutOfMemory Exception in ProcessManager**
  - *Recommended Action*: Increase JVM heap size or check for memory leaks in ProcessManager.

### Warnings
- [WARN] Low disk space on /var/log.
