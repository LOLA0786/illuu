import time
from fastapi import HTTPException

# Max requests per tenant per window
RATE_LIMIT = 60
WINDOW_SECONDS = 60

# In-memory store
request_log = {}

def check_rate_limit(tenant_id: str):
    current_time = time.time()

    if tenant_id not in request_log:
        request_log[tenant_id] = []

    # Remove expired timestamps
    request_log[tenant_id] = [
        ts for ts in request_log[tenant_id]
        if current_time - ts < WINDOW_SECONDS
    ]

    if len(request_log[tenant_id]) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    request_log[tenant_id].append(current_time)
