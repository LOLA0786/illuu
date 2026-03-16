import yaml
from illuu.kernel.workflow_engine import Workflow

def load_workflow(path, registry):
    with open(path) as f:
        data = yaml.safe_load(f)

    wf = Workflow()

    for name, agent in registry.all().items():
        wf.add_agent(name, agent)

    for edge in data["workflow"]["edges"]:
        wf.add_dependency(edge["from"], edge["to"])

    return wf, data["workflow"]["start"]
