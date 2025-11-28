# Agent Status Check Email Template
# Sent from orchestrator to agent when no update received
# Used for timeout detection and health monitoring

---
subject: "[BMAD] STATUS CHECK: {{story_id}}"
to: "{{agent_email}}"
from: "BMAD Orchestrator <orchestrator@bmad.local>"
priority: "high"
correlation_id: "{{correlation_id}}"
---

## STATUS CHECK

**Story ID:** {{story_id}}
**Assigned Agent:** {{agent_name}}
**Last Update:** {{last_update_timestamp}}
**Time Since Update:** {{hours_since_update}} hours

---

### Warning

No status update received for **{{hours_since_update}} hours**.

If no response within **1 hour**, this story will be:
1. Marked as timed out
2. Reassigned to another agent
3. Escalated to founder

---

### Story Details

| Field | Value |
|-------|-------|
| Story ID | {{story_id}} |
| Title | {{story_title}} |
| Assigned At | {{assigned_at}} |
| Deadline | {{deadline}} |
| Time Remaining | {{time_remaining}} |

---

### Expected Progress

Based on assignment time, you should be at approximately:
- **Expected:** {{expected_progress}}% complete
- **Status needed:** {{expected_status}}

---

## Required Response

Reply within 1 hour with ONE of:

```
PROGRESS
Status: <in_progress|testing|finalizing>
Percent: <0-100>%
ETA: <hours> hours
Notes: <brief update>
```

```
SUBMITTED
PR: {{pr_url}}
Ready for review.
```

```
BLOCKED
Reason: <what's blocking you>
Need: <what you need to proceed>
```

```
ALIVE
Working on: <current task>
ETA: <hours> hours
```

---

### Failure to Respond

If no response within 1 hour:
- Story will be reassigned
- Incident will be logged
- Founder will be notified

---

*Correlation ID: {{correlation_id}}*
*Timeout Warning: {{timeout_warning_number}} of 2*
