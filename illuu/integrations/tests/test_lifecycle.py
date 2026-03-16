from integrations.base.lifecycle import run_lifecycle
from integrations.mocks.mock_connector import MockConnector


def test_lifecycle_runs_without_error():
    connector = MockConnector()
    assert run_lifecycle(connector) is None
