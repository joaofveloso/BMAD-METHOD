# Alert Email Template
# Sent to founder for critical issues requiring immediate attention

---
subject: "[BMAD] 🚨 ALERT: {{alert_type}}"
to: "{{founder_email}}"
from: "BMAD Orchestrator <{{smtp_from_address}}>"
priority: "urgent"
---

## 🚨 ALERT: {{alert_title}}

**Severity:** {{severity}}
**Time:** {{timestamp}}
**Requires:** {{action_required}}

---

### Issue Details

{{issue_description}}

---

### Impact

{{#if affected_stories}}
**Affected Stories:**
{{#each affected_stories}}
- STORY-{{id}}: {{title}}
{{/each}}
{{/if}}

{{#if affected_services}}
**Affected Services:**
{{#each affected_services}}
- {{name}}: {{status}}
{{/each}}
{{/if}}

**Business Impact:** {{business_impact}}

---

### Root Cause

{{root_cause_analysis}}

---

### Attempted Resolutions

{{#each resolution_attempts}}
{{@index}}. **{{action}}** - {{result}}
{{/each}}

---

### Recommended Action

{{recommended_action}}

---

## Reply Options

{{#if options}}
{{#each options}}
### {{label}}
{{description}}
```
{{command}}
```

{{/each}}
{{else}}
### ✅ APPROVE
Proceed with recommended action.
```
APPROVE
```

### ❌ REJECT
Do not proceed. Wait for manual intervention.
```
REJECT
```

### 🔍 INVESTIGATE
Provide more details before deciding.
```
INVESTIGATE
```
{{/if}}

---

**⚠️ This alert requires your response.**
Automation is {{automation_status}} until resolved.

---

### Context

- **Correlation ID:** {{correlation_id}}
- **Agent:** {{agent}}
- **Story:** {{story_id}}
- **Iteration:** {{iteration_count}}

---
*Generated automatically by BMAD Orchestrator*
*Immediate response requested.*
