from typing import Protocol

class ApprovalInput:  # placeholder for typed model
    pass

class ApprovalTicket:  # placeholder for typed model
    pass

class ApprovalDecision:  # placeholder for typed model
    pass

class ApprovalGateway(Protocol):
    def requires_approval(self, input: ApprovalInput) -> bool:
        ...

    def request_approval(self, input: ApprovalInput) -> ApprovalTicket:
        ...

    def resolve(self, ticket_id: str) -> ApprovalDecision:
        ...
