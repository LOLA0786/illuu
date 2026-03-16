"""Mock connector for tests and local validation."""
from integrations.base.connector import (
    AuthContext,
    AuthResult,
    Connector,
    ConnectorConfig,
    ConnectionHandle,
    FetchQuery,
    FetchResult,
    PushPayload,
    PushResult,
    RevokeResult,
    RevokeToken,
    SyncResult,
    SyncState,
)


class MockConnector(Connector):
    def auth(self, context: AuthContext) -> AuthResult:
        return AuthResult()

    def connect(self, config: ConnectorConfig) -> ConnectionHandle:
        return ConnectionHandle()

    def fetch(self, query: FetchQuery) -> FetchResult:
        return FetchResult()

    def push(self, payload: PushPayload) -> PushResult:
        return PushResult()

    def sync(self, state: SyncState) -> SyncResult:
        return SyncResult()

    def revoke(self, token: RevokeToken) -> RevokeResult:
        return RevokeResult()
