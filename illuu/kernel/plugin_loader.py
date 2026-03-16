import importlib
import pkgutil
from illuu.kernel.agent_registry import AgentRegistry

registry = AgentRegistry()

def load_plugins(package):
    for _, name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package.__name__}.{name}")

        if hasattr(module, "register"):
            agent = module.register()
            registry.register(agent)

    return registry
