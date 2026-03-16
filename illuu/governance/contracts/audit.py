from typing import Protocol

class AuditEvent:  # placeholder for typed model
    pass

class LedgerRef:  # placeholder for typed model
    pass

class AuditLogger(Protocol):
    def record(self, event: AuditEvent) -> LedgerRef:
        ...
