# BMAD Verification Protocol

**Mandatory operational standard for all BMAD agents, workflows, and modules.**

All agents must follow this protocol before claiming success or completion.

---

## Core Principle

**Never claim success without actual verification.**

---

## Never Assume Without Verification

- Do not claim something "works" when only basic connectivity was tested
- Do not celebrate success before confirming actual functionality
- Do not provide confident "status: Working!" without real verification
- Do not present theories as confirmed facts

## Never Make Premature Celebrations

- Do not use celebration language when only solving half the problem
- Do not declare "SUCCESS!" when only addressing symptoms, not root causes
- Do not move on until the core issue is actually resolved

## Never Skip Critical Verification Steps

- Do not tell users "just try it" when you should test it yourself first
- Do not provide credentials without verifying they actually work
- Do not give access URLs without confirming they resolve to working interfaces
- Test the actual end-to-end flow, not just individual components

## Never Present Incomplete Solutions as Complete

- Do not hide the actual current state behind optimistic language
- Do not let desire to be helpful override factual accuracy
- State clearly what was verified vs. what remains untested
- Distinguish between "configured" and "confirmed working"

---

## Verification Checklist

Before claiming any task is complete, verify:

| Claim | Required Verification |
|-------|----------------------|
| "It works" | Run the actual command/test and show output |
| "Credentials are valid" | Authenticate with them and confirm access |
| "Service is running" | Query it and get a successful response |
| "Configuration complete" | Verify the config is loaded and functional |
| "Tests pass" | Run tests and show passing output |
| "Build succeeds" | Execute build and show success output |
| "Deployment complete" | Access the deployed resource and confirm |

---

## Reporting Standard

When reporting status, always distinguish:

```
VERIFIED:
- [x] SMTP connection to mail.email:587 - tested, authenticated successfully
- [x] Email sent to founder@mail.email - received and confirmed

NOT YET VERIFIED:
- [ ] IMAP polling every 60 seconds - configured but not tested
- [ ] Auto-merge on quality pass - workflow defined but not executed
```

---

## Violation Response

Violation of this protocol is a critical operational failure requiring:

1. Immediate correction of any false claims
2. Clear disclosure of what was actually verified
3. Completion of missing verification steps
4. Updated status report with accurate state

---

## Engineering Principles

These principles are mandatory for all architectural and implementation decisions.

### Simplicity First

1. Boring solutions outperform complex ones.
2. Defaults are better than options.
3. Abstractions must pay rent or be removed.
4. Grep-able code beats clever code.
5. Fewer moving parts beats modern stacks.
6. If a system requires a README to understand, it's too fancy.

### Architecture Constraints

7. Data beats framework magic.
8. Keep interfaces small and contracts stable.
9. Products dictate architecture, not engineer preferences.
10. Complexity moves; choose where it lives.
11. Build the narrowest system that can work.
12. Boundaries matter more than microservices vs monoliths.
13. The simplest topology that works is the correct one.
14. Flat files beat distributed systems when scale allows.
15. Architecture evolves by necessity, not imagination.

### Operational Reality

16. Logs before metrics before traces.
17. Reproducibility is more important than elegance.
18. Throughput matters more than latency.
19. Systems must survive losing the smartest engineer.
20. Temporary hacks become permanent; build them well.
21. Expensive components must be optional.
22. Tooling should behave like plumbing.
23. Systems should degrade gracefully when dependencies fail.
24. Manual steps are production liabilities.

### Consistency & Constraints

25. Constraints reduce chaos.
26. One language per layer reduces cognitive load.
27. One framework per problem avoids fragmentation.
28. No platform until scripts fail.
29. No multi-agent system unless isolation is mandatory.
30. Deterministic schemas beat inference and heuristics.
31. Make constraints explicit and enforceable.
32. Freedom without constraints creates operational noise.

### Configuration & State

33. Hardcoded behavior is cheaper than over-configuration.
34. Configuration is a liability until proven otherwise.
35. Global state is the enemy of reproducibility.
36. Schema ownership is stronger than framework ownership.

### Testing & Verification

37. Tests define behavior, not implementation.
38. Observability grows only after basic logging is healthy.
39. Favor deterministic pipelines over dynamic ones.
40. Batching and idempotency beat retries and hope.
41. Favor explicit data flow over invisible behavior.
42. Choose predictable performance over clever performance.

### Risk & Ownership

43. If a change touches more than two components, the boundary is wrong.
44. Don't architect for speculative features.
45. If only one person understands it, it's a risk.

---

**This protocol applies to all BMAD modules, agents, and workflows without exception.**
