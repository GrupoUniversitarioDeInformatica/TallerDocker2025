import os
from typing import Any

from bson import ObjectId
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from .models import Item, ItemDB

app = FastAPI(title="Taller de Docker")
client: AsyncIOMotorClient[dict[str, Any]] = AsyncIOMotorClient(os.getenv("MONGO_URI"))

db = client["fastapi_demo"]
collection = db["items"]


@app.get("/items", response_model=list[ItemDB])
async def get_all_items() -> list[dict[str, Any]]:
    docs: list[dict[str, Any]] = []
    async for doc in collection.find({}):
        doc["_id"] = str(doc["_id"])
        docs.append(doc)

    return docs


@app.post("/items", response_model=ItemDB)
async def create_item(item: Item) -> dict[str, Any]:
    result = await collection.insert_one(item.dict())

    item_db = await collection.find_one({"_id": result.inserted_id})
    assert item_db is not None

    item_db["_id"] = str(item_db["_id"])
    return item_db


@app.get("/items/{item_id}", response_model=ItemDB)
async def read_item(item_id: str) -> dict[str, Any]:
    try:
        oid = ObjectId(item_id)
    except TypeError:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    if not (item := await collection.find_one({"_id": oid})):
        raise HTTPException(status_code=404, detail="Item not found")

    item["_id"] = str(item["_id"])
    return item


@app.delete("/items/{item_id}")
async def delete_item(item_id: str) -> None:
    try:
        oid = ObjectId(item_id)
    except TypeError:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    result = await collection.delete_one({"_id": oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found. Could not delete")
