"""Storage actions."""
import json
from uuid import UUID

from starlette.requests import Request

from api.models.cat import Cat


def upsert(cat: Cat, request: Request):
    """Upsert the cat to storage."""
    to_set = cat.json()
    cat_id = str(cat.id)
    result = request.app.redis.set(cat_id, to_set)
    if result:
        return cat.id


def get(id: UUID, request: Request):
    """Get the cat with the given `id` from storage."""
    cat_id = str(id)
    loaded_cat = request.app.redis.get(cat_id)
    return json.loads(loaded_cat)
