from illuu.kernel.scheduler import Scheduler
from illuu.kernel.workflow_loader import load_workflow
from illuu.kernel.plugin_loader import load_plugins
import illuu.agents as agents

class WorkflowScheduler:

    def __init__(self):
        self.scheduler = Scheduler()
        self.registry = load_plugins(agents)

    def run(self, workflow_file):
        wf, start = load_workflow(workflow_file, self.registry)

        self.scheduler.schedule(start)

        for upstream, downstreams in wf.graph.items():
            for d in downstreams:
                self.scheduler.schedule(d)
