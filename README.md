# Claude Code hooks

Claude Code hooks as example that you can use and alter as you wish.

<https://code.claude.com/docs/en/hooks-guide>

Start Claude code then enter `/hooks` like this:

```sh
➜ claude

 ▐▛███▜▌   Claude Code v2.1.39
▝▜█████▛▘  Opus 4.6 · Claude Max
  ▘▘ ▝▝

❯ /hooks
───────────────────────────────────────────────────────────────────────────────────────
 Hooks

   1.  PreToolUse - Before tool execution
   2.  PostToolUse - After tool execution
   3.  PostToolUseFailure - After tool execution fails
   4.  Notification - When notifications are sent
   5.  UserPromptSubmit - When the user submits a prompt
   6.  SessionStart - When a new session is started
   7.  Stop - Right before Claude concludes its response
   8.  SubagentStart - When a subagent (Task tool call) is started
   9.  SubagentStop - Right before a subagent (Task tool call) concludes its response
   10. PreCompact - Before conversation compaction
   11. SessionEnd - When a session is ending
   12. PermissionRequest - When a permission dialog is displayed
   13. Setup - Repo setup hooks for init and maintenance
   14. TeammateIdle - When a teammate is about to go idle
   15. TaskCompleted - When a task is being marked as completed
   16. Disable all hooks
```
