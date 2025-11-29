# Agent Revision Request Email Template

# Sent from orchestrator to AI coding agents when quality gates fail

# Machine-parseable format for autonomous processing

---

subject: "[BMAD] REVISION: {{story_id}} - Iteration {{iteration}}/3"
to: "{{agent_email}}"
from: "BMAD Orchestrator <orchestrator@bmad.local>"
priority: "high"
correlation_id: "{{correlation_id}}"

---

## REVISION REQUIRED

**Story ID:** {{story_id}}
**PR:** #{{pr_number}}
**Iteration:** {{iteration}} of 3

---

### Failure Summary

**Status:** Quality Gate Failed
**Failed Checks:** {{failed_check_count}}

---

### Required Fixes

{{#each failures}}

#### {{@index}}. {{type}}

**Severity:** {{severity}}
**File:** `{{file}}`
{{#if line}}**Line:** {{line}}{{/if}}

**Issue:**
{{description}}

{{#if suggested_fix}}
**Suggested Fix:**

```{{language}}
{{suggested_fix}}
```

{{/if}}

---

{{/each}}

### Quality Gate Results

| Check    | Status              | Details                    |
| -------- | ------------------- | -------------------------- |
| Tests    | {{test_status}}     | {{test_details}}           |
| Coverage | {{coverage_status}} | {{coverage_percent}}%      |
| Linting  | {{lint_status}}     | {{lint_errors}} errors     |
| Security | {{security_status}} | {{security_issues}} issues |

---

### Instructions

1. Fix all REQUIRED issues listed above
2. Push changes to branch `{{branch_name}}`
3. Reply with `SUBMITTED` when ready for re-review

---

### Self-Healing Guidance

{{#if self_healing_hints}}
{{#each self_healing_hints}}

- {{this}}
  {{/each}}
  {{/if}}

---

### Escalation Warning

{{#if iteration_equals_2}}
**WARNING:** This is iteration 2 of 3. One more failure will escalate to founder.
{{/if}}

{{#if iteration_equals_3}}
**FINAL ATTEMPT:** This must pass or the story will be escalated to the founder.
{{/if}}

---

## Expected Response Commands

Reply with ONE of:

```
SUBMITTED
PR: {{pr_url}}
```

Fixes pushed, ready for re-review.

```
BLOCKED <reason>
```

Cannot fix due to blocker.

```
QUESTION <question>
```

Need clarification on failure.

---

_Correlation ID: {{correlation_id}}_
_Iteration {{iteration}} of 3_
