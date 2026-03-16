from illuu.kernel.config import load_config
from illuu.kernel.plugin_loader import load_plugins
import illuu.agents as agents

def run_dev():
    config = load_config()
    plugins = load_plugins(agents)

    enabled = config.get("agents", {}).get("enabled", [])

    for name in enabled:
        if name in plugins:
            print(f"Running agent: {name}")
            plugins[name]["run"]()
