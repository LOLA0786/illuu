from typing import Protocol

class RiskInput:  # placeholder for typed model
    pass

class RiskScore:  # placeholder for typed model
    pass

class RiskEngine(Protocol):
    def score(self, input: RiskInput) -> RiskScore:
        ...
