from illuu.kernel.event_bus import EventBus

bus = EventBus()

def register():
    return {
        "name": "example_agent",
        "run": run
    }

def handle_event(data):
    print("Agent received event:", data)

def run():
    print("Example agent running")

    bus.subscribe("test_event", handle_event)
    bus.publish("test_event", {"msg": "hello from agent"})
