from illuu.kernel.task_queue import TaskQueue

class Scheduler:
    def __init__(self):
        self.queue = TaskQueue()

    def schedule(self, agent_name):
        print(f"Scheduling {agent_name}")
        self.queue.push({"agent": agent_name})
