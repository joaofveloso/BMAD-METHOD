# DevOps Deployment Request Email Template
# Sent from orchestrator to devops-agent when release is approved
# Machine-parseable format for autonomous processing

---
subject: "[BMAD] DEPLOY: Release {{version}} to {{environment}}"
to: "devops@bmad.local"
from: "BMAD Orchestrator <orchestrator@bmad.local>"
priority: "high"
correlation_id: "{{correlation_id}}"
---

## DEPLOYMENT REQUEST

**Version:** {{version}}
**Environment:** {{environment}}
**Approved By:** {{approved_by}}
**Approved At:** {{approved_at}}

---

### Release Details

| Field | Value |
|-------|-------|
| Version | {{version}} |
| Previous Version | {{previous_version}} |
| Git Tag | `{{git_tag}}` |
| Commit | {{release_commit}} |
| Stories Included | {{story_count}} |

---

### Stories in This Release

{{#each stories}}
- **{{id}}**: {{title}} ({{type}})
{{/each}}

---

### Deployment Configuration

**Strategy:** {{deployment_strategy}}
**Rollback Available:** Yes (to {{previous_version}})
**Health Check Required:** Yes

{{#if deployment_config}}
### Custom Configuration

```yaml
{{deployment_config}}
```
{{/if}}

---

### Pre-Deployment Checklist

Execute before deployment:

1. [ ] Backup current state
2. [ ] Verify infrastructure health
3. [ ] Check database migrations
4. [ ] Prepare rollback procedure
5. [ ] Notify monitoring systems

---

### Deployment Steps

1. Pull release artifacts (tag: `{{git_tag}}`)
2. Execute pre-deployment scripts
3. Deploy to {{environment}}
4. Run health checks
5. Verify service endpoints
6. Monitor for 15 minutes

---

### Health Check Endpoints

{{#each health_endpoints}}
- `{{method}}` {{url}} - Expected: {{expected_status}}
{{/each}}

---

### Monitoring Window

**Duration:** 15 minutes post-deployment
**Metrics to Watch:**
- Error rate (threshold: < 1%)
- Response time (threshold: < {{max_response_time}}ms)
- CPU usage (threshold: < 80%)
- Memory usage (threshold: < 85%)

---

### Rollback Triggers

Auto-rollback if:
- Error rate > 5% for 5 minutes
- Service health check fails 3 consecutive times
- Critical alert triggered

---

## Expected Response Commands

Reply with ONE of:

```
DEPLOYING
Started deployment to {{environment}}
ETA: <minutes> minutes
```

```
DEPLOYED
Version: {{version}}
Environment: {{environment}}
Duration: <minutes> minutes
Health: PASS
Endpoints: All responding
```

```
DEPLOY FAILED
Reason: <reason>
Rolled back to: {{previous_version}}
Action needed: <action>
```

```
BLOCKED
Reason: <reason>
Cannot proceed until: <condition>
```

---

*Correlation ID: {{correlation_id}}*
*Deployment requested by BMAD Orchestrator*
*Founder approval: {{approval_id}}*
