from typing import Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    description: Optional[str] = None


class ItemDB(Item):
    id: str = Field(default_factory=str, alias="_id")
