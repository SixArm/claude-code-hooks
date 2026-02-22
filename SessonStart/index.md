# SessionStart

## Example: Re-inject context after compaction

When Claude’s context window fills up, compaction summarizes the conversation to
free space. This can lose important details. Use a `SessionStart` hook with a
compact matcher to re-inject critical context after every compaction.

Any text your command writes to stdout is added to Claude’s context. This
example reminds Claude of project conventions and recent work.

You can replace the echo with any command that produces dynamic output, like `git
log --oneline -5` to show recent commits. For injecting context on every session
start, consider using `CLAUDE.md` instead. For environment variables, see
`CLAUDE_ENV_FILE` in the reference.

Add the content from here into `~/.claude/settings.json`, or use the interactive
way to configure it by using the Claude Code command `/hooks`.
