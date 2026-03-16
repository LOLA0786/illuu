class AgentRegistry:
    def __init__(self):
        self._agents = {}

    def register(self, agent):
        name = agent["name"]
        self._agents[name] = agent

    def get(self, name):
        return self._agents.get(name)

    def list(self):
        return list(self._agents.keys())

    def all(self):
        return self._agents
