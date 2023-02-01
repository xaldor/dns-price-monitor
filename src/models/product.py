from __future__ import annotations
from .base import BaseSQLModel
from sqlalchemy import Column, Integer, Text, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from typing import Optional, AsyncIterator
from pydantic import AnyHttpUrl


from src.schemas import ProductInfo
from src.exceptions import ProductAlreadyInMonitorList, ProductDoesNotExist

PRODUCT_TITLE_MAX_LEN: int = 256


class ProductSQLModel(BaseSQLModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(PRODUCT_TITLE_MAX_LEN), nullable=False)
    url = Column(Text, nullable=False, unique=True)
    description = Column(Text, nullable=True)
    rating = Column(Float, nullable=True)

    price_history = relationship(
        "PriceRecordSQLModel",
        primaryjoin="PriceRecordSQLModel.product_id == ProductSQLModel.id",
        order_by="PriceRecordSQLModel.timestamp",
    )

    # TODO: Combine `get_by_id` and `get_by_url` into one method
    @classmethod
    async def get_by_id(cls, db: AsyncSession, target_id: int) -> ProductSQLModel:
        product: ProductSQLModel = (
            await db.execute(select(cls).where(cls.id == target_id))
        ).first()
        if not product:
            raise ProductDoesNotExist
        return product

    @classmethod
    async def get_by_url(
        cls, db: AsyncSession, target_url: AnyHttpUrl
    ) -> Optional[ProductSQLModel]:
        product: ProductSQLModel = (
            await db.execute(select(cls).where(cls.url == target_url))
        ).first()
        if not product:
            raise ProductDoesNotExist
        return product

    @classmethod
    async def create(
        cls, db: AsyncSession, product_info: ProductInfo
    ) -> ProductSQLModel:
        try:
            await cls.get_by_url(db, product_info.url)
        except ProductDoesNotExist:
            pass
        else:
            raise ProductAlreadyInMonitorList
        product = ProductSQLModel(**product_info.dict())
        db.add(product)
        await db.flush()
        return product

    @classmethod
    async def delete(cls, db: AsyncSession, target_id: int):
        await db.execute(delete(cls).where(cls.id == target_id))

    @classmethod
    async def get_all(cls, db: AsyncSession) -> AsyncIterator[ProductSQLModel, None]:
        products = await db.stream(select(cls))
        async for product in products:
            yield product.ProductSQLModel
