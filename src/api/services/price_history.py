from .base import AsyncApiService
from ..schemas.price_history import GetPriceHistoryRequest, GetPriceHistoryResponse

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_database_session

from src.models import ProductSQLModel
from src.schemas import PriceRecord


class GetPriceHistory(AsyncApiService):
    def __init__(self, db: AsyncSession = Depends(get_database_session)):
        self.__db = db

    async def process(self, data: GetPriceHistoryRequest) -> GetPriceHistoryResponse:
        db = self.__db
        price_history = ProductSQLModel.get_price_history(db, data.product_id)
        return GetPriceHistoryResponse(
            price_history=[PriceRecord.from_orm(p) async for p in price_history]
        )
