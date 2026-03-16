"""
Universal Agent Action Layer (UAAL)
"""

class UAAL:

    def __init__(self):
        self.policies = {}

    def register_policy(self, action: str, rules: dict):
        self.policies[action] = rules

    def authorize(self, agent_id: str, action: str, payload: dict):
        rules = self.policies.get(action)

        if not rules:
            return False, "No policy defined"

        if rules.get("requires_human"):
            return False, "Human approval required"

        return True, "Authorized"
