#!/usr/bin/env python3
"""
Workflow Manager for Email Processing
BACKLOG → WIP → DONE loop for all agents
"""

import os
import json
import shutil
import time
from datetime import datetime
from pathlib import Path

class WorkflowManager:
    def __init__(self, shared_path="./shared"):
        self.shared_path = Path(shared_path)
        self.containers = ["founder", "orchestrator", "backend", "frontend", "mobile", "qa", "devops", "researcher"]
        self.backlog_dir = self.shared_path / "BACKLOG"
        self.backlog_dir.mkdir(exist_ok=True)

    def create_task_email(self, task_name, description, assigned_to=None, priority="normal"):
        """Create a new task email and add it to BACKLOG"""
        timestamp = datetime.now().isoformat()
        task_id = f"task_{int(time.time())}_{task_name.replace(' ', '_')}"

        email_data = {
            "id": task_id,
            "task_name": task_name,
            "description": description,
            "assigned_to": assigned_to,  # None = anyone can claim
            "priority": priority,
            "status": "BACKLOG",
            "created_at": timestamp,
            "claimed_by": None,
            "started_at": None,
            "completed_at": None
        }

        email_file = self.backlog_dir / f"{task_id}.json"
        with open(email_file, 'w') as f:
            json.dump(email_data, f, indent=2)

        print(f"✅ Task created: {task_name} -> BACKLOG/{task_id}.json")
        return task_id

    def claim_next_task(self, agent_name):
        """Agent claims the next available task from BACKLOG"""
        if not os.path.exists(self.backlog_dir):
            return None

        available_tasks = []
        for filename in sorted(os.listdir(self.backlog_dir)):
            if filename.endswith('.json'):
                with open(self.backlog_dir / filename, 'r') as f:
                    task = json.load(f)

                # Check if task is available for this agent
                if (task['status'] == 'BACKLOG' and
                    (task['assigned_to'] is None or task['assigned_to'] == agent_name)):
                    available_tasks.append((filename, task))

        if not available_tasks:
            return None

        # Pick the highest priority task
        available_tasks.sort(key=lambda x: (
            0 if x[1]['priority'] == 'high' else
            1 if x[1]['priority'] == 'normal' else 2,
            x[1]['created_at']
        ))

        filename, task = available_tasks[0]

        # Move task to agent's WIP folder
        agent_wip_dir = self.shared_path / agent_name / "WIP"
        agent_wip_dir.mkdir(exist_ok=True, parents=True)

        # Update task status
        task['status'] = 'WIP'
        task['claimed_by'] = agent_name
        task['started_at'] = datetime.now().isoformat()

        # Write to WIP
        wip_file = agent_wip_dir / filename
        with open(wip_file, 'w') as f:
            json.dump(task, f, indent=2)

        # Remove from BACKLOG
        os.remove(self.backlog_dir / filename)

        print(f"🚀 {agent_name} claimed task: {task['task_name']}")
        return task

    def complete_task(self, agent_name, task_id):
        """Agent completes a task and moves it to DONE"""
        agent_wip_dir = self.shared_path / agent_name / "WIP"
        agent_done_dir = self.shared_path / agent_name / "DONE"
        agent_done_dir.mkdir(exist_ok=True, parents=True)

        task_file = agent_wip_dir / f"{task_id}.json"
        if not task_file.exists():
            print(f"❌ Task {task_id} not found in {agent_name}'s WIP")
            return False

        # Update task status
        with open(task_file, 'r') as f:
            task = json.load(f)

        task['status'] = 'DONE'
        task['completed_at'] = datetime.now().isoformat()

        # Move to DONE
        done_file = agent_done_dir / f"{task_id}.json"
        with open(done_file, 'w') as f:
            json.dump(task, f, indent=2)

        # Remove from WIP
        os.remove(task_file)

        print(f"✅ {agent_name} completed task: {task['task_name']}")
        return True

    def get_workflow_status(self):
        """Get current status of all tasks"""
        status = {
            "BACKLOG": 0,
            "WIP": {},
            "DONE": {}
        }

        # Count BACKLOG tasks
        if os.path.exists(self.backlog_dir):
            status["BACKLOG"] = len([f for f in os.listdir(self.backlog_dir) if f.endswith('.json')])

        # Count WIP and DONE tasks per agent
        for agent in self.containers:
            status["WIP"][agent] = 0
            status["DONE"][agent] = 0

            for folder in ["WIP", "DONE"]:
                agent_dir = self.shared_path / agent / folder
                if os.path.exists(agent_dir):
                    status[folder][agent] = len([f for f in os.listdir(agent_dir) if f.endswith('.json')])

        return status

    def has_work_remaining(self):
        """Check if there are tasks in BACKLOG or WIP"""
        status = self.get_workflow_status()

        # Check if any BACKLOG tasks
        if status["BACKLOG"] > 0:
            return True

        # Check if any WIP tasks
        total_wip = sum(status["WIP"].values())
        if total_wip > 0:
            return True

        return False

# CLI interface
if __name__ == "__main__":
    import sys

    workflow = WorkflowManager()

    if len(sys.argv) < 2:
        print("Usage: workflow_manager.py <command> [args...]")
        print("Commands: create, claim, complete, status, has_work")
        sys.exit(1)

    command = sys.argv[1]

    if command == "create" and len(sys.argv) >= 4:
        task_name = sys.argv[2]
        description = sys.argv[3]
        assigned_to = sys.argv[4] if len(sys.argv) > 4 else None
        priority = sys.argv[5] if len(sys.argv) > 5 else "normal"
        workflow.create_task_email(task_name, description, assigned_to, priority)

    elif command == "claim" and len(sys.argv) >= 3:
        agent_name = sys.argv[2]
        task = workflow.claim_next_task(agent_name)
        if task:
            print(f"Claimed: {task['task_name']}")
        else:
            print("No available tasks to claim")

    elif command == "complete" and len(sys.argv) >= 4:
        agent_name = sys.argv[2]
        task_id = sys.argv[3]
        workflow.complete_task(agent_name, task_id)

    elif command == "status":
        status = workflow.get_workflow_status()
        print(f"BACKLOG: {status['BACKLOG']} tasks")
        print("WIP tasks:")
        for agent, count in status['WIP'].items():
            if count > 0:
                print(f"  {agent}: {count} tasks")
        print("DONE tasks:")
        for agent, count in status['DONE'].items():
            if count > 0:
                print(f"  {agent}: {count} tasks")

    elif command == "has_work":
        has_work = workflow.has_work_remaining()
        print("yes" if has_work else "no")

    else:
        print("Invalid command or arguments")
