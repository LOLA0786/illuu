import redis
import json
import threading

class EventBus:
    def __init__(self, host="localhost", port=6379):
        try:
            self.redis = redis.Redis(host=host, port=port, decode_responses=True)
            self.redis.ping()
        except Exception:
            self.redis = None
            print("⚠️ Redis not available, event bus disabled")

    def publish(self, channel, message):
        if not self.redis:
            return
        self.redis.publish(channel, json.dumps(message))

    def subscribe(self, channel, handler):
        if not self.redis:
            return

        pubsub = self.redis.pubsub()
        pubsub.subscribe(channel)

        def listen():
            for msg in pubsub.listen():
                if msg["type"] == "message":
                    handler(json.loads(msg["data"]))

        thread = threading.Thread(target=listen, daemon=True)
        thread.start()
