import yaml

CONFIG = "billing/enforcement/config/plans.yaml"


def load_plans():
    with open(CONFIG, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def evaluate(plan_id: str, meter_id: str, value: int) -> bool:
    cfg = load_plans()
    for plan in cfg.get("plans", []):
        if plan.get("id") == plan_id:
            limit = plan.get("limits", {}).get(meter_id)
            if limit is None:
                return True
            return value <= limit
    return False


if __name__ == "__main__":
    print(evaluate("pilot", "workflow_executions", 50))
