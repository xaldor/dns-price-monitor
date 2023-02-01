from pydantic import BaseModel, conint
from datetime import datetime
from typing import TypeAlias

from src.schemas import ProductId

PriceRecordId: TypeAlias = int
Price: TypeAlias = conint(ge=0)  # type: ignore
PriceRecordTimestamp: TypeAlias = datetime


class PriceRecordInfo(BaseModel):
    price: Price
    timestamp: PriceRecordTimestamp


class PriceRecord(PriceRecordInfo):
    id: PriceRecordId
    product_id: ProductId

    class Config:
        orm_mode = True
