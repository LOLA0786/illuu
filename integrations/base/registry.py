"""Connector registry placeholder."""
from typing import Dict, Type
from integrations.base.connector import Connector

_REGISTRY: Dict[str, Type[Connector]] = {}


def register(name: str, connector_cls: Type[Connector]) -> None:
    _REGISTRY[name] = connector_cls


def get(name: str) -> Type[Connector] | None:
    return _REGISTRY.get(name)
