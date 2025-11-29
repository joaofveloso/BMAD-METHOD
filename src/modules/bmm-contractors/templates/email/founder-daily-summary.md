# Daily Summary Email Template

# Sent to founder every morning with pipeline status

---

subject: "[BMAD] Daily Summary - {{date}}"
to: "{{founder_email}}"
from: "BMAD Orchestrator <{{smtp_from_address}}>"
priority: "normal"

---

## Pipeline Status - {{date}}

### Summary

- **Stories Completed Today:** {{stories_completed_today}}
- **Stories In Progress:** {{stories_in_progress}}
- **Stories Blocked:** {{stories_blocked}}
- **Releases Deployed:** {{releases_deployed}}

---

### Agent Performance

| Agent | Stories | Cycle Time | Pass Rate | Status |
| ----- | ------- | ---------- | --------- | ------ |

{{#each agents}}
| {{icon}} {{name}} | {{stories_completed}} | {{avg_cycle_time}}h | {{pass_rate}}% | {{status}} |
{{/each}}

---

### Completed Stories

{{#if completed_stories}}
{{#each completed_stories}}

- **STORY-{{id}}**: {{title}} ({{agent}}, {{cycle_time}}h)
  {{/each}}
  {{else}}
  No stories completed today.
  {{/if}}

---

### In Progress

{{#if in_progress_stories}}
{{#each in_progress_stories}}

- **STORY-{{id}}**: {{title}}
  - Agent: {{agent}}
  - Started: {{started_at}}
  - Progress: {{progress}}%
    {{/each}}
    {{else}}
    No stories in progress.
    {{/if}}

---

### Blocked Items

{{#if blocked_items}}
**ACTION REQUIRED:**

{{#each blocked_items}}

#### STORY-{{id}}: {{title}}

- **Blocked Since:** {{blocked_since}}
- **Reason:** {{blocker_reason}}
- **Agent:** {{agent}}

Reply with: `UNBLOCK STORY-{{id}} <instructions>` to provide guidance.

---

{{/each}}
{{else}}
No blocked items.
{{/if}}

---

### Quality Metrics

- **First-Time Pass Rate:** {{first_time_pass_rate}}%
- **Average Cycle Time:** {{avg_cycle_time}} hours
- **Self-Healing Success:** {{self_healing_success_rate}}%
- **Escalation Rate:** {{escalation_rate}}%

---

### Upcoming

- **Stories Ready for Assignment:** {{stories_ready}}
- **Pending Releases:** {{pending_releases}}
- **Scheduled Deployments:** {{scheduled_deployments}}

---

### Quick Commands

Reply to this email with:

- `STATUS` - Get immediate status update
- `PAUSE` - Pause all automation
- `RESUME` - Resume automation
- `PRIORITY STORY-{id} high` - Change story priority

---

_Generated automatically by BMAD Orchestrator_
_Pipeline running autonomously. Reply only if action needed._
