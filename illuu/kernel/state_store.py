import json
import redis

class StateStore:

    def __init__(self):
        self.redis = redis.Redis(decode_responses=True)

    def set(self, key, value):
        self.redis.set(key, json.dumps(value))

    def get(self, key):
        v = self.redis.get(key)
        return json.loads(v) if v else None
