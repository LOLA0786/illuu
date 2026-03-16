from api.app import app


def test_openapi_contains_unified_and_legacy_paths():
    spec = app.openapi()
    paths = spec.get("paths", {})

    # Unified routes
    assert "/memory/ingest" in paths
    assert "/memory/query" in paths
    assert "/memory/health" in paths
    assert "/intent/inject-intent" in paths
    assert "/intent/verify-intent" in paths
    assert "/intent/health" in paths
    assert "/vault/execute" in paths
    assert "/vault/health" in paths
    assert "/governance/health" in paths

    # Legacy root routes
    assert "/ingest" in paths
    assert "/query" in paths
    assert "/inject-intent" in paths
    assert "/verify-intent" in paths
    assert "/execute" in paths
    assert "/health" in paths
