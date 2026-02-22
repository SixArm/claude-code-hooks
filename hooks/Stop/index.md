# Stop

This directory is for Claude Code `Stop` hook examples.

This hook happens just before Claude concludes its response.

## Prompt-type hook

For a decision that requires judgment, use a `type: "prompt"` hook.

Claude Code sends your prompt and the hook’s input data to a Claude model (Haiku
by default) to make the decision. You can specify a different model with the
model field if you need more capability.

The model’s only job is to return a yes/no decision as JSON:

- "ok": true: the action proceeds

- "ok": false: the action is blocked. The model’s "reason" is fed back to Claude so it can adjust.

## Agent-type hook

For a decision that requires complex thinking, use a `type: "agent"` hook.

An agent-type hook spawns a subagent that can read files, search code, and use
other tools to verify conditions before returning a decision.

Agent hooks use the same `"ok" / "reason"` response format as prompt-type hooks,
but with a longer default timeout of 60 seconds and up to 50 tool-use turns.
