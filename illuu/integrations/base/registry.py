"""Connector registry with manifest-based discovery."""
from __future__ import annotations

import importlib
import json
import os
from typing import Dict, Type

from integrations.base.connector import Connector

_REGISTRY: Dict[str, Type[Connector]] = {}


def register(name: str, connector_cls: Type[Connector]) -> None:
    _REGISTRY[name] = connector_cls


def get(name: str) -> Type[Connector] | None:
    return _REGISTRY.get(name)


def load_manifest(path: str | None = None) -> dict:
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "registry", "manifest.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def discover(path: str | None = None) -> None:
    """Load connectors from a local manifest. No external calls."""
    manifest = load_manifest(path)
    for entry in manifest.get("connectors", []):
        name = entry.get("name")
        module_path = entry.get("module")
        class_name = entry.get("class")
        if not name or not module_path or not class_name:
            continue
        module = importlib.import_module(module_path)
        connector_cls = getattr(module, class_name)
        register(name, connector_cls)
