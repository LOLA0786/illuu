import redis
import json

class TaskQueue:
    def __init__(self, host="localhost", port=6379):
        self.redis = redis.Redis(host=host, port=port, decode_responses=True)

    def push(self, task):
        self.redis.rpush("illuu_tasks", json.dumps(task))

    def pop(self):
        data = self.redis.blpop("illuu_tasks")
        if data:
            return json.loads(data[1])
