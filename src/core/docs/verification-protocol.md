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

| Claim                    | Required Verification                       |
| ------------------------ | ------------------------------------------- |
| "It works"               | Run the actual command/test and show output |
| "Credentials are valid"  | Authenticate with them and confirm access   |
| "Service is running"     | Query it and get a successful response      |
| "Configuration complete" | Verify the config is loaded and functional  |
| "Tests pass"             | Run tests and show passing output           |
| "Build succeeds"         | Execute build and show success output       |
| "Deployment complete"    | Access the deployed resource and confirm    |

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

## Agent Workflow Instructions - Task Management System

All agents must participate in the shared folder task workflow system.

### System Overview

Tasks flow through three stages: **BACKLOG → WIP → DONE**

- All tasks are stored as JSON files in the shared directory `/workspace/shared/`
- Each agent has their own workspace: `/workspace/shared/<agent_name>/`

### Folder Structure

```
/workspace/shared/
├── BACKLOG/           # All unassigned tasks go here
├── founder/           # Founder workspace
│   ├── WIP/          # Tasks currently in progress
│   └── DONE/         # Completed tasks
├── orchestrator/
├── backend/
├── frontend/
├── mobile/
├── qa/
├── devops/
└── researcher/
```

### Method 1: Manual Commands

```bash
cd /workspace/shared

# See all available tasks in BACKLOG
ls BACKLOG/

# Claim your next available task (highest priority first)
python3 workflow_manager.py claim <your_name>

# See your current WIP tasks
ls <your_name>/WIP/

# Complete a task (move it to DONE)
python3 workflow_manager.py complete <your_name> <task_id>

# Check overall workflow status
python3 workflow_manager.py status

# Check if there's still work available
python3 workflow_manager.py has_work
```

### Method 2: Automated Worker

```bash
cd /workspace/shared

# Start your automated worker (runs continuously)
python3 agent_worker.py <your_name>

# Worker will:
# 1. Automatically claim available tasks
# 2. Process them with simulated work
# 3. Complete tasks and move to DONE
# 4. Continue until no work remains
```

### Task Lifecycle

**1. Claiming Tasks**

- Tasks are claimed by priority: high → normal → low
- If assigned specifically to you, only you can claim it
- If unassigned, any agent can claim it
- System automatically moves task from `BACKLOG/` to `<your_name>/WIP/`

**2. Working on Tasks**

- Task details stored in JSON at: `<your_name>/WIP/<task_id>.json`
- Contains: task name, description, priority, timestamps
- You can modify the task file to track your progress
- Never move files manually - always use the workflow manager

**3. Completing Tasks**

- Use: `python3 workflow_manager.py complete <your_name> <task_id>`
- System automatically moves task from `WIP/` to `DONE/`
- Updates completion timestamp
- Task is now considered finished

### Agent Identities

| Agent        | Role                                        |
| ------------ | ------------------------------------------- |
| founder      | Project leadership and architecture         |
| orchestrator | System coordination and workflow management |
| backend      | Server-side development and APIs            |
| frontend     | User interface and client-side development  |
| mobile       | Mobile application development              |
| qa           | Quality assurance and testing               |
| devops       | Infrastructure and deployment               |
| researcher   | Research and analysis tasks                 |

### Workflow Completion

The system continues until:

- No tasks remain in `BACKLOG/`
- No tasks remain in any agent's `WIP/`
- All tasks are in various agents' `DONE/` folders

### Example Session

```bash
# 1. Check what's available
python3 workflow_manager.py status

# 2. Claim your next task
python3 workflow_manager.py claim frontend

# Output: 🚀 frontend claimed task: Design new landing page

# 3. Do your work (inspect task file)
cat frontend/WIP/task_123_Design_new_landing_page.json

# 4. Complete when done
python3 workflow_manager.py complete frontend task_123_Design_new_landing_page

# Output: ✅ frontend completed task: Design new landing page
```

### Important Rules

- **Always use workflow manager** - never move files manually
- **Check status first** before claiming tasks
- **Complete your WIP tasks** before claiming new ones
- **One task at a time** per agent (unless parallel work is needed)
- **Respect task assignments** - don't claim tasks assigned to others

### Getting Help

```bash
# See all available commands
python3 workflow_manager.py
python3 agent_worker.py

# Check current state
python3 workflow_manager.py status
python3 workflow_manager.py has_work
```

---

**This protocol applies to all BMAD modules, agents, and workflows without exception.**
