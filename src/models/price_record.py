from .base import BaseSQLModel
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func


class PriceRecordSQLModel(BaseSQLModel):
    __tablename__ = "price_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    price = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), default=func.now())
