"""Compatibility shim for moved adapters."""
import os

_ADAPTER_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "integrations", "adapters", "memory_adapters")
)
__path__ = [_ADAPTER_PATH]
