from typing import Protocol

class ActionContext:  # placeholder for typed model
    pass

class AuthorizationDecision:  # placeholder for typed model
    pass

class ActionResult:  # placeholder for typed model
    pass

class GovernanceGateway(Protocol):
    def authorize(self, ctx: ActionContext) -> AuthorizationDecision:
        ...

    def proxy_call(self, ctx: ActionContext) -> ActionResult:
        ...
