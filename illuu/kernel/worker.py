from illuu.kernel.task_queue import TaskQueue
from illuu.kernel.plugin_loader import load_plugins
import illuu.agents as agents
import traceback

def start_worker():
    queue = TaskQueue()
    registry = load_plugins(agents)

    print("Worker started")

    while True:
        task = queue.pop()

        try:
            agent_name = task["agent"]
            agent = registry.get(agent_name)

            if agent:
                print(f"Worker running {agent_name}")
                agent["run"]()

        except Exception:
            traceback.print_exc()
