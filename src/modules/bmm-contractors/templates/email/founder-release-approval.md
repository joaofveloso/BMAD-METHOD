# Release Approval Request Email Template
# Sent to founder when release candidate is ready

---
subject: "[BMAD] Release {{version}} Ready for Approval"
to: "{{founder_email}}"
from: "BMAD Orchestrator <{{smtp_from_address}}>"
priority: "high"
---

## Release {{version}} Ready for Approval

**ACTION REQUIRED:** Please review and approve/reject this release.

---

### Release Summary

- **Version:** {{version}}
- **Type:** {{release_type}} ({{semver_bump}})
- **Stories Included:** {{story_count}}
- **Created:** {{created_at}}

---

### Changes Included

{{#each stories}}
#### STORY-{{id}}: {{title}}
- **Type:** {{type}}
- **Agent:** {{agent}}
- **Cycle Time:** {{cycle_time}}h

{{/each}}

---

### Quality Gates

| Check | Status | Details |
|-------|--------|---------|
| Test Coverage | {{test_coverage_status}} | {{test_coverage}}% |
| All Tests Pass | {{tests_status}} | {{test_count}} tests |
| Security Scan | {{security_status}} | {{security_issues}} issues |
| Code Review | {{review_status}} | {{review_iterations}} iterations |
| Performance | {{performance_status}} | {{performance_delta}} |

**Overall:** {{#if all_gates_pass}}✅ All gates passed{{else}}⚠️ Some gates have warnings{{/if}}

---

### Deployment Plan

- **Target Environment:** {{target_environment}}
- **Strategy:** {{deployment_strategy}}
- **Estimated Downtime:** {{estimated_downtime}}
- **Rollback Ready:** {{rollback_ready}}

---

### Risk Assessment

{{#if risks}}
{{#each risks}}
- **{{severity}}:** {{description}}
{{/each}}
{{else}}
No significant risks identified.
{{/if}}

---

### Changelog

```
{{changelog}}
```

---

## Reply Options

**Reply with ONE of the following:**

### ✅ APPROVE
Deploy this release to production.
```
APPROVE
```

### ❌ REJECT
Cancel this release. Include reason.
```
REJECT <reason>
```

### ⏸️ DELAY
Hold release for later. Include new target date.
```
DELAY <date>
```

### ❓ QUESTION
Ask for more information before deciding.
```
QUESTION <your question>
```

---

**⏰ This approval request expires in 24 hours.**
If no response, release will be held for manual review.

---
*Generated automatically by BMAD Orchestrator*
