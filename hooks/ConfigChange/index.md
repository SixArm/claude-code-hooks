# ConfigChange

This directory is for Claude Code `ConfigChange` hook examples.

The matcher filters by configuration type: `user_settings`, `project_settings`,
`local_settings`, `policy_settings`, or `skills`. To block a change from taking
effect, exit with code 2 or return `{"decision": "block"}`. See the
`ConfigChange` reference for the full input schema.
