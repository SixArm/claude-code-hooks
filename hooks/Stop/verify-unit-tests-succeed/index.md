# Verify unit tests succeed

This example shows how to verify unit tests succeed.

For a decision that requires complex thinking, use a `type: "agent"` hook.

An agent-type hook spawns a subagent that can read files, search code, and use
other tools to verify conditions before returning a decision.

Agent hooks use the same `"ok" / "reason"` response format as prompt-type hooks,
but with a longer default timeout of 60 seconds and up to 50 tool-use turns.

The model’s only job is to return a yes/no decision as JSON:

- "ok": true: the action proceeds

- "ok": false: the action is blocked. The model’s "reason" is fed back to Claude so it can adjust.

This example uses a Stop hook to ask the agent whether all unit tests succeed.
If the model returns `"ok": false`, Claude keeps working and uses the reason as
its next instruction.

Add the content from here into `~/.claude/settings.json`, or use the interactive
way to configure it by using the Claude Code command `/hooks`.
