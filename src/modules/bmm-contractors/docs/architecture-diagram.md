# BMAD Autonomous AI Coding Pipeline Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           BMAD AUTONOMOUS PIPELINE                               │
│                    Shared Folder Task Workflow (BACKLOG → WIP → DONE)           │
└─────────────────────────────────────────────────────────────────────────────────┘

                                    ┌──────────────┐
                                    │   FOUNDER    │
                                    │   (Human)    │
                                    │              │
                                    │ Creates new  │
                                    │ stories/epics│
                                    └──────┬───────┘
                                           │
                                           │ Submits tasks
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              /workspace/shared/                                  │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                            BACKLOG/                                      │   │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │   │
│  │  │ task_001.json│ │ task_002.json│ │ task_003.json│ │ task_004.json│   │   │
│  │  │              │ │              │ │              │ │              │   │   │
│  │  │ priority:high│ │ priority:norm│ │ priority:norm│ │ priority:low │   │   │
│  │  │ assigned:null│ │ assigned:back│ │ assigned:null│ │ assigned:null│   │   │
│  │  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                       │                                         │
│                    ┌──────────────────┼──────────────────┐                     │
│                    │                  │                  │                      │
│                    ▼                  ▼                  ▼                      │
│  ┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐       │
│  │     backend/        │ │     frontend/       │ │       qa/           │       │
│  │  ┌───────┐ ┌──────┐│ │  ┌───────┐ ┌──────┐│ │  ┌───────┐ ┌──────┐│       │
│  │  │  WIP/ │ │ DONE/││ │  │  WIP/ │ │ DONE/││ │  │  WIP/ │ │ DONE/││       │
│  │  └───────┘ └──────┘│ │  └───────┘ └──────┘│ │  └───────┘ └──────┘│       │
│  └─────────────────────┘ └─────────────────────┘ └─────────────────────┘       │
│                                                                                 │
│  ┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐       │
│  │     mobile/         │ │     devops/         │ │    researcher/      │       │
│  │  ┌───────┐ ┌──────┐│ │  ┌───────┐ ┌──────┐│ │  ┌───────┐ ┌──────┐│       │
│  │  │  WIP/ │ │ DONE/││ │  │  WIP/ │ │ DONE/││ │  │  WIP/ │ │ DONE/││       │
│  │  └───────┘ └──────┘│ │  └───────┘ └──────┘│ │  └───────┘ └──────┘│       │
│  └─────────────────────┘ └─────────────────────┘ └─────────────────────┘       │
│                                                                                 │
│  ┌─────────────────────┐ ┌─────────────────────┐                               │
│  │     founder/        │ │   orchestrator/     │                               │
│  │  ┌───────┐ ┌──────┐│ │  ┌───────┐ ┌──────┐│                               │
│  │  │  WIP/ │ │ DONE/││ │  │  WIP/ │ │ DONE/││                               │
│  │  └───────┘ └──────┘│ │  └───────┘ └──────┘│                               │
│  └─────────────────────┘ └─────────────────────┘                               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Task Lifecycle Flow

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                              TASK LIFECYCLE                                     │
└────────────────────────────────────────────────────────────────────────────────┘

    ┌─────────┐         ┌─────────┐         ┌─────────┐         ┌─────────┐
    │ CREATE  │────────▶│ BACKLOG │────────▶│   WIP   │────────▶│  DONE   │
    └─────────┘         └─────────┘         └─────────┘         └─────────┘
         │                   │                   │                   │
         │                   │                   │                   │
    ┌────▼────┐         ┌────▼────┐         ┌────▼────┐         ┌────▼────┐
    │ Founder │         │  Agent  │         │  Agent  │         │  Agent  │
    │ creates │         │ claims  │         │ works   │         │completes│
    │  task   │         │  task   │         │ on task │         │  task   │
    └─────────┘         └─────────┘         └─────────┘         └─────────┘


    BACKLOG/task_001.json        backend/WIP/task_001.json      backend/DONE/task_001.json
    ┌──────────────────┐         ┌──────────────────┐           ┌──────────────────┐
    │ {                │         │ {                │           │ {                │
    │  "id": "task_001"│  ───▶   │  "id": "task_001"│   ───▶    │  "id": "task_001"│
    │  "status":"BACKLOG"        │  "status": "WIP" │           │  "status": "DONE"│
    │  "claimed_by":null│        │  "claimed_by":   │           │  "claimed_by":   │
    │  "started_at":null│        │    "backend"     │           │    "backend"     │
    │ }                │         │  "started_at":   │           │  "completed_at": │
    └──────────────────┘         │    "2024-..."    │           │    "2024-..."    │
                                 │ }                │           │ }                │
                                 └──────────────────┘           └──────────────────┘
```

## Agent Container Architecture

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                         CONTAINERIZED AI AGENTS                                 │
└────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  FOUNDER        │  │  ORCHESTRATOR   │  │  BACKEND        │  │  FRONTEND       │
│  Container      │  │  Container      │  │  Container      │  │  Container      │
│  192.168.56.10  │  │  192.168.56.11  │  │  192.168.56.12  │  │  192.168.56.13  │
│                 │  │                 │  │                 │  │                 │
│  ┌───────────┐  │  │  ┌───────────┐  │  │  ┌───────────┐  │  │  ┌───────────┐  │
│  │ Claude    │  │  │  │ Claude    │  │  │  │ Claude    │  │  │  │ Claude    │  │
│  │ Code      │  │  │  │ Code      │  │  │  │ Code      │  │  │  │ Code      │  │
│  └─────┬─────┘  │  │  └─────┬─────┘  │  │  └─────┬─────┘  │  │  └─────┬─────┘  │
│        │        │  │        │        │  │        │        │  │        │        │
│  ┌─────▼─────┐  │  │  ┌─────▼─────┐  │  │  ┌─────▼─────┐  │  │  ┌─────▼─────┐  │
│  │agent_     │  │  │  │agent_     │  │  │  │agent_     │  │  │  │agent_     │  │
│  │worker.py  │  │  │  │worker.py  │  │  │  │worker.py  │  │  │  │worker.py  │  │
│  └─────┬─────┘  │  │  └─────┬─────┘  │  │  └─────┬─────┘  │  │  └─────┬─────┘  │
│        │        │  │        │        │  │        │        │  │        │        │
└────────┼────────┘  └────────┼────────┘  └────────┼────────┘  └────────┼────────┘
         │                    │                    │                    │
         └────────────────────┴────────────────────┴────────────────────┘
                                       │
                              ┌────────▼────────┐
                              │  SHARED VOLUME  │
                              │ /workspace/shared│
                              │                 │
                              │  workflow_      │
                              │  manager.py     │
                              └─────────────────┘

┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  MOBILE         │  │  QA             │  │  DEVOPS         │  │  RESEARCHER     │
│  Container      │  │  Container      │  │  Container      │  │  Container      │
│  192.168.56.14  │  │  192.168.56.15  │  │  192.168.56.16  │  │  192.168.56.17  │
│                 │  │                 │  │                 │  │                 │
│  ┌───────────┐  │  │  ┌───────────┐  │  │  ┌───────────┐  │  │  ┌───────────┐  │
│  │ Claude    │  │  │  │ Claude    │  │  │  │ Claude    │  │  │  │ Claude    │  │
│  │ Code      │  │  │  │ Code      │  │  │  │ Code      │  │  │  │ Code      │  │
│  └───────────┘  │  │  └───────────┘  │  │  └───────────┘  │  │  └───────────┘  │
└─────────────────┘  └─────────────────┘  └─────────────────┘  └─────────────────┘
```

## Workflow Manager Operations

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                         workflow_manager.py                                     │
└────────────────────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────────────────┐
    │                            COMMANDS                                      │
    └─────────────────────────────────────────────────────────────────────────┘

    ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
    │     CREATE     │     │     CLAIM      │     │    COMPLETE    │
    │                │     │                │     │                │
    │ python3        │     │ python3        │     │ python3        │
    │ workflow_      │     │ workflow_      │     │ workflow_      │
    │ manager.py     │     │ manager.py     │     │ manager.py     │
    │ create         │     │ claim          │     │ complete       │
    │ "Task Name"    │     │ backend        │     │ backend        │
    │ "Description"  │     │                │     │ task_001       │
    └───────┬────────┘     └───────┬────────┘     └───────┬────────┘
            │                      │                      │
            ▼                      ▼                      ▼
    ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
    │ Creates JSON   │     │ Moves task     │     │ Moves task     │
    │ in BACKLOG/    │     │ BACKLOG/ →     │     │ WIP/ → DONE/   │
    │                │     │ agent/WIP/     │     │                │
    └────────────────┘     └────────────────┘     └────────────────┘

    ┌────────────────┐     ┌────────────────┐
    │     STATUS     │     │   HAS_WORK     │
    │                │     │                │
    │ python3        │     │ python3        │
    │ workflow_      │     │ workflow_      │
    │ manager.py     │     │ manager.py     │
    │ status         │     │ has_work       │
    └───────┬────────┘     └───────┬────────┘
            │                      │
            ▼                      ▼
    ┌────────────────┐     ┌────────────────┐
    │ Shows counts   │     │ Returns yes/no │
    │ per agent      │     │ if work exists │
    └────────────────┘     └────────────────┘
```

## Agent Worker Loop

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                          agent_worker.py Loop                                   │
└────────────────────────────────────────────────────────────────────────────────┘

                              ┌─────────────┐
                              │   START     │
                              │  Worker     │
                              └──────┬──────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │  Has current task?    │
                         └───────────┬───────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    │ NO                              │ YES
                    ▼                                 ▼
          ┌─────────────────┐               ┌─────────────────┐
          │  Claim next     │               │  Process task   │
          │  task from      │               │  (AI coding)    │
          │  BACKLOG        │               │                 │
          └────────┬────────┘               └────────┬────────┘
                   │                                  │
          ┌────────┴────────┐                        │
          │ Task claimed?   │                        │
          └────────┬────────┘                        │
                   │                                  │
      ┌────────────┴────────────┐                    │
      │ NO                      │ YES                │
      ▼                         ▼                    │
┌─────────────┐         ┌─────────────┐              │
│ Has work    │         │ Set as      │              │
│ remaining?  │         │ current     │              │
└──────┬──────┘         │ task        │              │
       │                └──────┬──────┘              │
  ┌────┴────┐                  │                     │
  │NO    YES│                  │                     ▼
  ▼         ▼                  │          ┌─────────────────┐
┌─────┐  ┌─────┐               │          │  Complete task  │
│SLEEP│  │WAIT │               │          │  Move to DONE   │
│ 5s  │  │ 1s  │               │          └────────┬────────┘
└──┬──┘  └──┬──┘               │                   │
   │        │                  │                   │
   └────────┴──────────────────┴───────────────────┘
                      │
                      ▼
              ┌─────────────┐
              │   LOOP      │
              │  (continue) │
              └─────────────┘
```

## Task JSON Structure

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                          TASK JSON FORMAT                                       │
└────────────────────────────────────────────────────────────────────────────────┘

task_1732900000_implement_user_auth.json
┌─────────────────────────────────────────────────────────────────────────────┐
│ {                                                                            │
│   "id": "task_1732900000_implement_user_auth",                              │
│   "task_name": "Implement User Authentication",                              │
│   "description": "Add JWT-based authentication with refresh tokens",         │
│   "assigned_to": "backend",           // null = any agent can claim          │
│   "priority": "high",                 // high | normal | low                 │
│   "status": "BACKLOG",                // BACKLOG | WIP | DONE                │
│   "created_at": "2024-11-29T10:00:00.000Z",                                 │
│   "claimed_by": null,                 // Agent name when claimed             │
│   "started_at": null,                 // Timestamp when moved to WIP         │
│   "completed_at": null                // Timestamp when moved to DONE        │
│ }                                                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Agent Roles & Responsibilities

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                          AGENT SPECIALIZATIONS                                  │
└────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│  FOUNDER (Human Interface)                                                      │
│  ─────────────────────────                                                      │
│  • Creates new stories and epics                                                │
│  • Approves releases and deployments                                            │
│  • Provides guidance on blocked items                                           │
│  • Reviews daily summaries                                                      │
│  • Makes priority decisions                                                     │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│  ORCHESTRATOR (Traffic Controller)                                              │
│  ─────────────────────────────────                                              │
│  • Routes tasks to appropriate agents                                           │
│  • Monitors pipeline health                                                     │
│  • Handles escalations                                                          │
│  • Coordinates multi-agent workflows                                            │
│  • Generates daily summaries for founder                                        │
└─────────────────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────┐  ┌───────────────────────────────┐
│  BACKEND                      │  │  FRONTEND                     │
│  ────────                     │  │  ─────────                    │
│  • Java/Spring development    │  │  • React/TypeScript           │
│  • API implementation         │  │  • UI components              │
│  • Database migrations        │  │  • State management           │
│  • Unit/integration tests     │  │  • E2E tests                  │
│  • OpenAPI documentation      │  │  • Accessibility              │
└───────────────────────────────┘  └───────────────────────────────┘

┌───────────────────────────────┐  ┌───────────────────────────────┐
│  MOBILE                       │  │  QA                           │
│  ───────                      │  │  ──                           │
│  • Android/Kotlin             │  │  • Code review                │
│  • Jetpack Compose            │  │  • Test coverage              │
│  • Offline-first sync         │  │  • Quality gates              │
│  • Device compatibility       │  │  • Security scans             │
└───────────────────────────────┘  └───────────────────────────────┘

┌───────────────────────────────┐  ┌───────────────────────────────┐
│  DEVOPS                       │  │  RESEARCHER                   │
│  ───────                      │  │  ───────────                  │
│  • Infrastructure as Code     │  │  • Technical documentation    │
│  • CI/CD pipelines            │  │  • API documentation          │
│  • Deployment automation      │  │  • Architecture decisions     │
│  • Monitoring setup           │  │  • Research reports           │
└───────────────────────────────┘  └───────────────────────────────┘
```

## Self-Healing Loop

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                         SELF-HEALING WORKFLOW                                   │
└────────────────────────────────────────────────────────────────────────────────┘

    Agent claims task
          │
          ▼
    ┌─────────────┐
    │  Implement  │
    │  Solution   │
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐     ┌─────────────┐
    │  Run Local  │────▶│   PASS?     │
    │  Tests      │     └──────┬──────┘
    └─────────────┘            │
                          ┌────┴────┐
                          │NO    YES│
                          ▼         ▼
                   ┌──────────┐  ┌──────────┐
                   │Iteration │  │ Submit   │
                   │ < 3?     │  │ PR       │
                   └────┬─────┘  └──────────┘
                        │
                   ┌────┴────┐
                   │NO    YES│
                   ▼         ▼
            ┌──────────┐  ┌──────────┐
            │ Escalate │  │  Retry   │
            │ to       │  │  with    │
            │ Founder  │  │  fixes   │
            └──────────┘  └────┬─────┘
                               │
                               └────────────▶ Back to Implement


    Max 3 iterations before escalation
    Each iteration includes:
    • Analysis of failure
    • Targeted fixes
    • Re-run tests
```

## Verification Protocol

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                       VERIFICATION PROTOCOL                                     │
│                  (All agents must follow)                                       │
└────────────────────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────────────────┐
    │  BEFORE CLAIMING SUCCESS:                                                │
    │                                                                          │
    │  ✓ "It works"           →  Run actual command, show output               │
    │  ✓ "Tests pass"         →  Execute tests, show passing results           │
    │  ✓ "Build succeeds"     →  Run build, show success output                │
    │  ✓ "Config complete"    →  Verify config is loaded and functional        │
    │  ✓ "Deployment done"    →  Access deployed resource, confirm working     │
    │                                                                          │
    │  NEVER:                                                                  │
    │  ✗ Claim something "works" without actual verification                   │
    │  ✗ Celebrate success before confirming functionality                     │
    │  ✗ Tell users "just try it" without testing first                       │
    │  ✗ Present theories as confirmed facts                                   │
    └─────────────────────────────────────────────────────────────────────────┘

    Status Report Format:
    ┌─────────────────────────────────────────────────────────────────────────┐
    │  VERIFIED:                                                               │
    │  - [x] Unit tests pass - 47/47 tests passing                            │
    │  - [x] Build successful - ./gradlew build exit code 0                   │
    │  - [x] API endpoint responds - GET /api/users returns 200               │
    │                                                                          │
    │  NOT YET VERIFIED:                                                       │
    │  - [ ] Load testing - configured but not executed                        │
    │  - [ ] Production deployment - staging only                              │
    └─────────────────────────────────────────────────────────────────────────┘
```

## File Structure

```
/workspace/shared/
├── BACKLOG/                          # Unclaimed tasks
│   ├── task_001_user_auth.json
│   ├── task_002_dashboard.json
│   └── task_003_api_docs.json
│
├── workflow_manager.py               # Task lifecycle manager
├── agent_worker.py                   # Automated worker script
│
├── founder/
│   ├── WIP/                          # Tasks founder is working on
│   └── DONE/                         # Completed founder tasks
│
├── orchestrator/
│   ├── WIP/
│   └── DONE/
│
├── backend/
│   ├── WIP/
│   │   └── task_004_api.json         # Currently implementing
│   └── DONE/
│       └── task_000_setup.json       # Completed
│
├── frontend/
│   ├── WIP/
│   └── DONE/
│
├── mobile/
│   ├── WIP/
│   └── DONE/
│
├── qa/
│   ├── WIP/
│   └── DONE/
│
├── devops/
│   ├── WIP/
│   └── DONE/
│
└── researcher/
    ├── WIP/
    └── DONE/
```

## Quick Start Commands

```bash
# Create a new task
python3 /workspace/shared/workflow_manager.py create "Implement Login" "Add JWT auth" backend high

# Check status
python3 /workspace/shared/workflow_manager.py status

# Claim a task (as an agent)
python3 /workspace/shared/workflow_manager.py claim backend

# Complete a task
python3 /workspace/shared/workflow_manager.py complete backend task_123_implement_login

# Run automated worker
python3 /workspace/shared/agent_worker.py backend
```
