# Log Analysis Rules

When analyzing server logs, follow these guidelines:

## Categorization
1. **Critical Errors**: Any `[ERROR]` containing "OutOfMemory", "Database", or "Payment". These require immediate attention and should be highlighted in red or bold.
2. **Warnings**: Any `[WARN]` related to "memory" or "disk space". These should be noted as infrastructure warnings.
3. **Routine**: `[INFO]` logs can generally be ignored unless asked specifically about user activity.

## Action Items
Always provide a short "Recommended Action" for any Critical Error found in the logs.
