"""Cat router."""
from uuid import UUID

from fastapi import APIRouter
from starlette.requests import Request

from api.actions import storage
from api.models.cat import Cat


router = APIRouter()


@router.post("/cat", tags=["cat"])
async def set_cat(cat: Cat, request: Request):
    """Create a cat resource."""
    cat_id = storage.upsert(cat, request)
    return {"cat_id": cat_id}


@router.get("/cat/{cat_id}", tags=["cat"], response_model=Cat)
async def get_cat(cat_id: UUID, request: Request):
    """Create a cat resource."""
    cat = storage.get(cat_id, request)
    return cat
