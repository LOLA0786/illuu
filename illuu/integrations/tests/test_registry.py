from integrations.base import registry


def test_manifest_discovery_registers_mock():
    registry.discover()
    cls = registry.get("mock")
    assert cls is not None
