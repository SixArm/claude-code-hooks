# Check tasks are complete

This example shows how to check tasks are complete.

For a decision that requires judgment rather than deterministic rules, use a
`type: "prompt"` hook.

Instead of running a shell command, Claude Code sends your prompt and the hook’s
input data to a Claude model (Haiku by default) to make the decision. You can
specify a different model with the model field if you need more capability.

The model’s only job is to return a yes/no decision as JSON:

- "ok": true: the action proceeds

- "ok": false: the action is blocked. The model’s "reason" is fed back to Claude so it can adjust.

This example uses a Stop hook to ask the model whether all requested tasks are
complete. If the model returns `"ok": false`, Claude keeps working and uses the
reason as its next instruction.

Add the content from here into `~/.claude/settings.json`, or use the interactive
way to configure it by using the Claude Code command `/hooks`.
