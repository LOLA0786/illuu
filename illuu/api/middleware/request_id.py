import uuid
from typing import Callable
from fastapi import Request
from starlette.responses import Response

async def request_id_middleware(request: Request, call_next: Callable) -> Response:
    request.state.request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    response = await call_next(request)
    response.headers["X-Request-ID"] = request.state.request_id
    return response
