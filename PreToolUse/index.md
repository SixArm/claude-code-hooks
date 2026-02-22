# PreToolUse

## Example: Block edits to protected files

Prevent Claude from modifying sensitive files like `.env`, `package-lock.json`,
or anything in `.git/`.

Claude receives feedback explaining why the edit was blocked, so it can adjust
its approach.

This example uses a separate script file that the hook calls. The script checks
the target file path against a list of protected patterns and exits with code 2
to block the edit.

Add the content from here into `~/.claude/settings.json`, or use the interactive
way to configure it by using the Claude Code command `/hooks`.
