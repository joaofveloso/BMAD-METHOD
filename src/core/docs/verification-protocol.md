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

**This protocol applies to all BMAD modules, agents, and workflows without exception.**
