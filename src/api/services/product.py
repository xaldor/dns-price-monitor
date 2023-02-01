from .base import AsyncApiService
from ..schemas.product import (
    AddProductRequest,
    AddProductResponse,
    RemoveProductRequest,
    RemoveProductResponse,
    GetAllProductsRequest,
    GetAllProductsResponse,
)

from fastapi import Depends
from fastapi.concurrency import run_in_threadpool
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_database_session
from src.dns import get_dns_scraper, DNSWebScraper

from src.schemas import Product, ProductInfo
from src.models import ProductSQLModel, PriceRecordSQLModel

from src.exceptions import ProductAlreadyInMonitorList
from src.logger import logger


class AddProduct(AsyncApiService):
    """API service that adds product into the monitor list"""

    def __init__(
        self,
        db: AsyncSession = Depends(get_database_session),
        dns: DNSWebScraper = Depends(get_dns_scraper),
    ):
        self.__db = db
        self.__dns = dns

    def __call__(self):
        return self

    async def process(self, data: AddProductRequest) -> AddProductResponse:
        db, dns = self.__db, self.__dns
        extracted_product_info: ProductInfo = await run_in_threadpool(
            lambda: dns.get_product(data.url)
        )
        try:
            db_product: ProductSQLModel = await ProductSQLModel.create(
                db, extracted_product_info
            )
        except ProductAlreadyInMonitorList:
            logger.debug(
                f"Trying to add to monitor list product, that already is there: {extracted_product_info.title}"
            )
            raise
        else:
            return AddProductResponse(product=Product.from_orm(db_product))


class RemoveProduct(AsyncApiService):
    def __init__(self, db: AsyncSession = Depends(get_database_session)):
        self.__db = db

    def __call__(self):
        return self

    async def process(self, data: RemoveProductRequest) -> RemoveProductResponse:
        db = self.__db
        await PriceRecordSQLModel.delete_all_by_product_id(db, data.id)
        await ProductSQLModel.delete(db, data.id)
        return RemoveProductResponse()


class GetAllProducts(AsyncApiService):
    def __init__(self, db: AsyncSession = Depends(get_database_session)):
        self.__db = db

    def __call__(self):
        return self

    async def process(self, data: GetAllProductsRequest) -> GetAllProductsResponse:
        db = self.__db
        return GetAllProductsResponse(
            products=[
                Product.from_orm(product_orm)
                async for product_orm in ProductSQLModel.get_all(db)
            ]
        )
