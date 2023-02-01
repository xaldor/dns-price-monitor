from pydantic import BaseModel, conint
from datetime import datetime
from typing import TypeAlias


PriceRecordId: TypeAlias = int
Price: TypeAlias = conint(ge=0)
PriceRecordTimestamp: TypeAlias = datetime


class PriceRecordInfo(BaseModel):
    price: Price
    timestamp: PriceRecordTimestamp


class PriceRecord(PriceRecordInfo):
    id: PriceRecordId

    class Config:
        orm_mode = True
