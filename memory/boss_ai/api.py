from fastapi import FastAPI
from orchestrator.core import BossAI
from uaal.engine import UAAL
import requests

app = FastAPI(title="Boss AI")
boss = BossAI()
uaal = UAAL()

# Example policy
uaal.register_policy(
    action="query_knowledge",
    rules={"requires_human": False}
)

KNOWLEDGE_VAULT_URL = "http://knowledge-vault:8000"

@app.post("/task")
def submit_task(task: dict):
    plan = boss.submit_task(task)

    allowed, reason = uaal.authorize(
        agent_id="boss-ai",
        action="query_knowledge",
        payload=task
    )

    if not allowed:
        return {"error": "UAAL_BLOCKED", "reason": reason}

    kv_response = requests.get(
        f"{KNOWLEDGE_VAULT_URL}/query",
        params={"q": task["intent"]}
    )

    boss.finalize(task["id"])

    return {
        "plan": plan,
        "knowledge_results": kv_response.json()
    }
