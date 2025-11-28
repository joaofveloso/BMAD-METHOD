# Quality Check Request Email Template
# Sent from orchestrator to metrics system when PR is submitted
# Machine-parseable format for autonomous processing

---
subject: "[BMAD] QUALITY CHECK: PR#{{pr_number}} - {{story_id}}"
to: "metrics@bmad.local"
from: "BMAD Orchestrator <orchestrator@bmad.local>"
priority: "normal"
correlation_id: "{{correlation_id}}"
---

## QUALITY CHECK REQUEST

**Story ID:** {{story_id}}
**PR:** #{{pr_number}}
**Author Agent:** {{author_agent}}

---

### PR Information

| Field | Value |
|-------|-------|
| Repository | {{repository}} |
| Branch | `{{branch_name}}` |
| Base Branch | `{{base_branch}}` |
| PR URL | {{pr_url}} |
| Commit SHA | {{head_sha}} |

---

### Required Checks

Execute the following quality gates:

1. **Test Execution**
   - Run all tests
   - Report pass/fail count
   - Report coverage percentage

2. **Code Coverage**
   - Minimum threshold: {{min_coverage}}%
   - Check diff coverage

3. **Static Analysis**
   - Linting ({{linter}})
   - Code style check
   - Complexity analysis

4. **Security Scan**
   - Dependency vulnerabilities
   - Secret detection
   - OWASP checks

5. **Build Verification**
   - Compile/build success
   - No warnings treated as errors

---

### Thresholds

| Metric | Minimum | Blocking |
|--------|---------|----------|
| Test Coverage | {{min_coverage}}% | Yes |
| Test Pass Rate | 100% | Yes |
| Lint Errors | 0 | Yes |
| Security Critical | 0 | Yes |
| Security High | {{max_security_high}} | Yes |

---

## Expected Response Commands

Reply with ONE of:

```
QUALITY PASS
Coverage: {{coverage}}%
Tests: {{passed}}/{{total}} passed
Lint: 0 errors
Security: No issues
```

```
QUALITY FAIL
Failures:
- TYPE: <failure_type>
  SEVERITY: <critical|high|medium|low>
  FILE: <file_path>
  LINE: <line_number>
  MESSAGE: <description>
  FIX: <suggested_fix>
```

---

*Correlation ID: {{correlation_id}}*
*Check requested by BMAD Orchestrator*
