"""Define cat model."""
import datetime
import uuid

from pydantic import BaseModel


class Cat(BaseModel):
    """Cat schema."""

    id: uuid.UUID = uuid.uuid4()
    name: str
    breed: str
    birthdate: datetime.datetime
    outdoor: bool
