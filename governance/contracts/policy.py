from typing import Protocol

class PolicyInput:  # placeholder for typed model
    pass

class PolicyDecision:  # placeholder for typed model
    pass

class PolicyEngine(Protocol):
    def evaluate(self, input: PolicyInput) -> PolicyDecision:
        ...
