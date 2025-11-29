# QA Review Request Email Template

# Sent from orchestrator to qa-agent when PR is submitted

# Machine-parseable format for autonomous processing

---

subject: "[BMAD] REVIEW: PR#{{pr_number}} - {{story_id}}"
to: "qa@bmad.local"
from: "BMAD Orchestrator <orchestrator@bmad.local>"
priority: "normal"
correlation_id: "{{correlation_id}}"

---

## REVIEW REQUEST

**Story ID:** {{story_id}}
**PR:** #{{pr_number}}
**Author Agent:** {{author_agent}}
**Submitted At:** {{submitted_at}}

---

### PR Details

| Field      | Value               |
| ---------- | ------------------- |
| Repository | {{repository}}      |
| Branch     | `{{branch_name}}`   |
| Target     | `{{target_branch}}` |
| PR URL     | {{pr_url}}          |
| Diff URL   | {{diff_url}}        |

---

### Story Summary

**Title:** {{story_title}}
**Type:** {{story_type}}

{{story_description}}

---

### Acceptance Criteria

{{#each acceptance_criteria}}

- [ ] {{this}}
      {{/each}}

---

### Files Changed

{{#each files_changed}}

- `{{path}}` (+{{additions}} / -{{deletions}})
  {{/each}}

**Total:** {{total_files}} files, +{{total_additions}} / -{{total_deletions}}

---

### Review Checklist

Please verify:

1. [ ] Code meets acceptance criteria
2. [ ] Tests cover the changes
3. [ ] No security vulnerabilities
4. [ ] Code follows project patterns
5. [ ] No hardcoded secrets or credentials
6. [ ] Error handling is appropriate

---

### Technical Context

**Stack:** {{tech_stack}}
**Related Stories:** {{#each related_stories}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}

---

## Expected Response Commands

Reply with ONE of:

```
QA PASS
All acceptance criteria verified.
```

```
QA FAIL
Reason: <detailed reason>
Issues:
- <issue 1>
- <issue 2>
```

---

_Correlation ID: {{correlation_id}}_
_Review requested by BMAD Orchestrator_
