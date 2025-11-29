#!/usr/bin/env python3
"""
Agent Worker Script - Runs inside each container
Participates in BACKLOG → WIP → DONE workflow
"""

import os
import sys
import json
import time
import signal
import random
from datetime import datetime
from pathlib import Path

class AgentWorker:
    def __init__(self, agent_name, shared_path="/workspace/shared"):
        self.agent_name = agent_name
        self.shared_path = Path(shared_path)
        self.running = True
        self.current_task = None

        # Set up signal handler for graceful shutdown
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, signum, frame):
        print(f"\n{self.agent_name}: Received shutdown signal, finishing current task...")
        self.running = False

    def claim_next_task(self):
        """Try to claim a task from BACKLOG"""
        workflow_manager = self.shared_path / "workflow_manager.py"
        if not os.path.exists(workflow_manager):
            print(f"{self.agent_name}: workflow_manager.py not found")
            return None

        # Use Python to import and run the workflow manager
        sys.path.insert(0, str(self.shared_path))
        try:
            from workflow_manager import WorkflowManager
            workflow = WorkflowManager(str(self.shared_path))
            return workflow.claim_next_task(self.agent_name)
        except Exception as e:
            print(f"{self.agent_name}: Error claiming task: {e}")
            return None

    def complete_current_task(self):
        """Complete the current task"""
        if not self.current_task:
            return False

        sys.path.insert(0, str(self.shared_path))
        try:
            from workflow_manager import WorkflowManager
            workflow = WorkflowManager(str(self.shared_path))
            success = workflow.complete_task(self.agent_name, self.current_task['id'])
            if success:
                self.current_task = None
            return success
        except Exception as e:
            print(f"{self.agent_name}: Error completing task: {e}")
            return False

    def process_task(self, task):
        """Simulate processing a task (replace with actual work)"""
        task_name = task['task_name']
        print(f"{self.agent_name}: 🔄 Processing task: {task_name}")

        # Simulate work time (1-5 seconds for demo)
        work_time = random.uniform(1, 5)
        print(f"{self.agent_name}: ⏳ Working for {work_time:.1f} seconds...")

        # Do some "work" (can be replaced with actual processing logic)
        time.sleep(work_time)

        print(f"{self.agent_name}: ✅ Task completed: {task_name}")
        return True

    def has_work_available(self):
        """Check if there's work in BACKLOG or any WIP"""
        workflow_manager = self.shared_path / "workflow_manager.py"
        if not os.path.exists(workflow_manager):
            return False

        sys.path.insert(0, str(self.shared_path))
        try:
            from workflow_manager import WorkflowManager
            workflow = WorkflowManager(str(self.shared_path))
            return workflow.has_work_remaining()
        except Exception:
            return False

    def run(self):
        """Main worker loop"""
        print(f"{self.agent_name}: 🚀 Agent worker started")
        print(f"{self.agent_name}: Monitoring shared path: {self.shared_path}")

        while self.running:
            try:
                # If no current task, try to claim one
                if not self.current_task:
                    print(f"{self.agent_name}: 🔍 Looking for work...")
                    task = self.claim_next_task()
                    if task:
                        self.current_task = task
                        print(f"{self.agent_name}: 📋 Claimed task: {task['task_name']}")
                    else:
                        # No tasks available, wait a bit
                        if not self.has_work_available():
                            print(f"{self.agent_name}: 😴 No work available, sleeping...")
                            time.sleep(5)
                        else:
                            time.sleep(1)
                        continue

                # Process current task
                if self.current_task:
                    success = self.process_task(self.current_task)
                    if success:
                        # Complete the task
                        if self.complete_current_task():
                            print(f"{self.agent_name}: ✅ Task completed and moved to DONE")
                        else:
                            print(f"{self.agent_name}: ⚠️ Task processed but failed to move to DONE")
                    else:
                        print(f"{self.agent_name}: ❌ Task processing failed")
                        # Still try to complete it to avoid infinite loops
                        self.complete_current_task()

            except KeyboardInterrupt:
                print(f"\n{self.agent_name}: Keyboard interrupt, shutting down...")
                break
            except Exception as e:
                print(f"{self.agent_name}: ❌ Error in worker loop: {e}")
                time.sleep(1)

        print(f"{self.agent_name}: 👋 Agent worker stopped")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: agent_worker.py <agent_name>")
        print("Agent names: founder, orchestrator, backend, frontend, mobile, qa, devops, researcher")
        sys.exit(1)

    agent_name = sys.argv[1]
    agent = AgentWorker(agent_name)
    agent.run()
