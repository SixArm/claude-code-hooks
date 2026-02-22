# PostToolUse

## Example: Auto-format code after edits

Automatically run Prettier on every file Claude edits, so formatting stays
consistent without manual intervention.

This hook uses the `PostToolUse` event with an `Edit|Write` matcher, so it runs
only after file-editing tools. The command extracts the edited file path with `jq`
and passes it to `prettier`.

Add the content from here into `~/.claude/settings.json`, or use the interactive
way to configure it by using the Claude Code command `/hooks`.
