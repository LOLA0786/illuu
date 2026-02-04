"""Connector interface and base types."""
from typing import Protocol

class AuthContext:  # placeholder
    pass

class AuthResult:  # placeholder
    pass

class ConnectorConfig:  # placeholder
    pass

class ConnectionHandle:  # placeholder
    pass

class FetchQuery:  # placeholder
    pass

class FetchResult:  # placeholder
    pass

class PushPayload:  # placeholder
    pass

class PushResult:  # placeholder
    pass

class SyncState:  # placeholder
    pass

class SyncResult:  # placeholder
    pass

class RevokeToken:  # placeholder
    pass

class RevokeResult:  # placeholder
    pass

class Connector(Protocol):
    def auth(self, context: AuthContext) -> AuthResult:
        ...

    def connect(self, config: ConnectorConfig) -> ConnectionHandle:
        ...

    def fetch(self, query: FetchQuery) -> FetchResult:
        ...

    def push(self, payload: PushPayload) -> PushResult:
        ...

    def sync(self, state: SyncState) -> SyncResult:
        ...

    def revoke(self, token: RevokeToken) -> RevokeResult:
        ...
