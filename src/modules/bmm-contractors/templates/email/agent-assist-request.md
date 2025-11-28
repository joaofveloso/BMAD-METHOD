# Agent Assist Request Email Template
# Sent from orchestrator to helper agent when another agent is blocked
# Machine-parseable format for autonomous processing

---
subject: "[BMAD] ASSIST: {{blocked_agent}} needs help with {{story_id}}"
to: "{{helper_agent_email}}"
from: "BMAD Orchestrator <orchestrator@bmad.local>"
priority: "high"
correlation_id: "{{correlation_id}}"
---

## ASSISTANCE REQUEST

**Requesting Agent:** {{blocked_agent}}
**Story ID:** {{story_id}}
**Blocker Type:** {{blocker_type}}

---

### Blocker Details

{{blocker_description}}

---

### Context

**Story Title:** {{story_title}}
**Story Type:** {{story_type}}

**What {{blocked_agent}} was trying to do:**
{{blocked_action}}

**Where they got stuck:**
- File: `{{blocked_file}}`
{{#if blocked_line}}- Line: {{blocked_line}}{{/if}}

---

### Requested Help

{{help_request}}

---

### Related Information

{{#if related_files}}
**Related Files:**
{{#each related_files}}
- `{{this}}`
{{/each}}
{{/if}}

{{#if error_message}}
**Error Message:**
```
{{error_message}}
```
{{/if}}

---

### Your Scope

**What to do:**
{{assistance_scope}}

**What NOT to do:**
- Do not take over the entire story
- Do not modify files outside the assistance scope
- Do not merge any changes

---

### Handoff Instructions

After providing assistance:
1. Push any helper code/config to branch `{{assist_branch}}`
2. Reply with assistance details

---

## Expected Response Commands

Reply with ONE of:

```
ASSISTED
Action: <what you did>
Branch: {{assist_branch}}
Files: <files modified>
Notes: <any notes for blocked agent>
```

```
CANNOT ASSIST
Reason: <why you cannot help>
Suggestion: <alternative approach>
```

```
QUESTION
Need clarification: <question>
```

---

*Correlation ID: {{correlation_id}}*
*Original story correlation: {{original_correlation_id}}*
