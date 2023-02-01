from pydantic import BaseModel

from src.schemas import ProductId, PriceRecord


class GetPriceHistoryRequest(BaseModel):
    product_id: int


class GetPriceHistoryResponse(BaseModel):
    price_history: list[PriceRecord]
