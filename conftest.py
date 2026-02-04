import os
import sys
import importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))

# Ensure repo root is first on sys.path
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

INTENT = os.path.join(ROOT, "intent")
VAULT = os.path.join(ROOT, "vault")
MEMORY = os.path.join(ROOT, "memory")

for path in [INTENT, MEMORY, VAULT]:
    if path not in sys.path:
        sys.path.append(path)

# Force governance package to resolve from repo root, not vault/governance.py
_governance_init = os.path.join(ROOT, "governance", "__init__.py")
if os.path.isfile(_governance_init):
    spec = importlib.util.spec_from_file_location("governance", _governance_init)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    module.__path__ = [os.path.join(ROOT, "governance")]
    sys.modules["governance"] = module

if "tests" in sys.modules:
    del sys.modules["tests"]
