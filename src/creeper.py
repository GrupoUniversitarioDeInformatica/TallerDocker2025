import os

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import Integer, String, Text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .models import Item, ItemDB

DATABASE_URL = os.getenv(
    "DATABASE_URL", "mysql+asyncmy://user:password@db:3306/fastapi_demo"
)

print(DATABASE_URL)

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class ItemTable(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text, nullable=True)


app = FastAPI(title="Taller de Docker")


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/items", response_model=list[ItemDB])
async def get_all_items(db: AsyncSession = Depends(get_db)) -> list[ItemDB]:
    result = await db.execute(ItemTable.__table__.select())
    return [ItemDB(**row._mapping) for row in result.all()]


@app.post("/items", response_model=ItemDB)
async def create_item(item: Item, db: AsyncSession = Depends(get_db)) -> ItemDB:
    new_item = ItemTable(**item.dict())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return ItemDB.from_orm(new_item)


@app.get("/items/{item_id}", response_model=ItemDB)
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)) -> ItemDB:
    item = await db.get(ItemTable, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemDB.from_orm(item)


@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)) -> None:
    item = await db.get(ItemTable, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found. Could not delete")
    await db.delete(item)
    await db.commit()
