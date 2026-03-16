from collections import defaultdict
from illuu.kernel.scheduler import Scheduler

class WorkflowEngine:
    def __init__(self):
        self.graph = defaultdict(list)
        self.scheduler = Scheduler()

    def add_edge(self, src, dst):
        self.graph[src].append(dst)

    def trigger(self, start_agent):
        print(f"Triggering workflow at {start_agent}")
        self.scheduler.schedule(start_agent)

    def on_complete(self, agent_name):
        next_nodes = self.graph.get(agent_name, [])
        for n in next_nodes:
            print(f"Scheduling downstream agent: {n}")
            self.scheduler.schedule(n)
