# Notification

## Example: Get notified when Claude needs input.

Get a desktop notification whenever Claude finishes working and needs your
input, so you can switch to other tasks without checking the terminal.

This hook uses the `Notification` event, which fires when Claude is waiting for
input or permission. Each tab below uses the platform’s native notification
command.

Add the content from here into `~/.claude/settings.json`, or use the interactive
way to configure it by using the Claude Code command `/hooks`.
