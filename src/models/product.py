from .base import BaseSQLModel
from sqlalchemy import Column, Integer, Text, String, Float
from sqlalchemy.orm import relationship

PRODUCT_TITLE_MAX_LEN: int = 256


class ProductSQLModel(BaseSQLModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(256), nullable=False)
    url = Column(Text, nullable=False, unique=True)
    description = Column(Text, nullable=True)
    rating = Column(Float, nullable=True)

    price_history = relationship(
        "PriceRecordSQLModel",
        primaryjoin="PriceRecordSQLModel.product_id == ProductSQLModel.id",
        order_by="PriceRecordSQLModel.timestamp",
    )
