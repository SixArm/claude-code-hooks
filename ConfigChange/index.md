# ConfigChange

The matcher filters by configuration type: `user_settings`, `project_settings`,
`local_settings`, `policy_settings`, or `skills`. To block a change from taking
effect, exit with code 2 or return `{"decision": "block"}`. See the
`ConfigChange` reference for the full input schema.

## Example: Audit configuration changes

Track when settings or skills files change during a session. The `ConfigChange`
event fires when an external process or editor modifies a configuration file, so
you can log changes for compliance or block unauthorized modifications.

This example appends each change to an audit log.

Add the content from here into `~/.claude/settings.json`, or use the interactive
way to configure it by using the Claude Code command `/hooks`.
