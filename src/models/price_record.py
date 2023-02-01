from __future__ import annotations
from .base import BaseSQLModel
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select

from src.schemas import Price, ProductId


class PriceRecordSQLModel(BaseSQLModel):
    __tablename__ = "price_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    price = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), default=func.now())

    @classmethod
    async def create(
        cls,
        db: AsyncSession,
        price: Price,
        product_id: ProductId,
    ) -> PriceRecordSQLModel:
        price_record = PriceRecordSQLModel(price=price, product_id=product_id)
        db.add(price_record)
        await db.flush()
        return price_record

    @classmethod
    async def delete_all_by_product_id(cls, db: AsyncSession, product_id: ProductId):
        await db.execute(delete(cls).where(cls.product_id == product_id))
