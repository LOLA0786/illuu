"""Compatibility shim for moved connectors."""
import os

_CONNECTOR_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "integrations", "adapters", "vault_connectors")
)
__path__ = [_CONNECTOR_PATH]
