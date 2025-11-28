# Deployment Complete Email Template
# Sent to founder after successful deployment

---
subject: "[BMAD] ✅ Release {{version}} Deployed Successfully"
to: "{{founder_email}}"
from: "BMAD Orchestrator <{{smtp_from_address}}>"
priority: "normal"
---

## ✅ Release {{version}} Deployed Successfully

**Environment:** {{environment}}
**Deployed At:** {{deployed_at}}
**Duration:** {{deployment_duration}}

---

### Deployment Summary

| Metric | Value |
|--------|-------|
| Version | {{version}} |
| Environment | {{environment}} |
| Strategy | {{deployment_strategy}} |
| Downtime | {{actual_downtime}} |
| Rollback Required | No |

---

### Health Check Results

{{#each health_checks}}
| {{name}} | {{status}} | {{response_time}}ms |
{{/each}}

**Overall Health:** {{overall_health_status}}

---

### Stories Now Live

{{#each stories}}
- **STORY-{{id}}**: {{title}}
{{/each}}

---

### Post-Deployment Metrics

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Response Time | {{metrics.response_time_before}}ms | {{metrics.response_time_after}}ms | {{metrics.response_time_delta}} |
| Error Rate | {{metrics.error_rate_before}}% | {{metrics.error_rate_after}}% | {{metrics.error_rate_delta}} |
| CPU Usage | {{metrics.cpu_before}}% | {{metrics.cpu_after}}% | {{metrics.cpu_delta}} |
| Memory | {{metrics.memory_before}}MB | {{metrics.memory_after}}MB | {{metrics.memory_delta}} |

---

### What's Next

- **Monitoring:** Active for next 24 hours
- **Auto-Rollback:** Enabled if error rate spikes
- **Next Release:** {{next_release_estimate}}

---

### Rollback Info

If issues are discovered, reply with:
```
ROLLBACK {{version}}
```

Rollback will restore version {{previous_version}}.

---

*No action required. This is a confirmation email.*

---
*Generated automatically by BMAD Orchestrator*
