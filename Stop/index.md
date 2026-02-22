# Stop

## Example: Prompt-based hook to check tasks are complete

[`check-tasks-are-complete.json`](check-tasks-are-complete.json).

For a decision that requires judgment rather than deterministic rules, use a `type: "prompt"` hook.

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

## Example: Verify unit tests succeed

[`verify-unit-tests-succeed.json`](verify-unit-tests-succeed.json)

For a decision that requires inspecting files or running commands, use a `type: "agent"` hook.

Unlike prompt hooks which make a single LLM call, agent hooks spawn a subagent
that can read files, search code, and use other tools to verify conditions
before returning a decision.

Agent hooks use the same `"ok" / "reason"` response format as prompt hooks, but
with a longer default timeout of 60 seconds and up to 50 tool-use turns.
