import json
from datetime import datetime


def emit(tenant_id: str, meter_id: str, value: float):
    event = {
        "tenant_id": tenant_id,
        "meter_id": meter_id,
        "value": value,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
    print(json.dumps(event))


if __name__ == "__main__":
    emit("tenant-demo", "workflow_executions", 1)
