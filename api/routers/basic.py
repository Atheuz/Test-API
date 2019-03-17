"""Basic router."""
from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter()


@router.get("/basic/ping", tags=["basic"])
async def ping(request: Request):
    """Ping endpoint."""
    request.app.logger.info("basic-ping", extra={"1": 1})
    return {"message": "pong"}
