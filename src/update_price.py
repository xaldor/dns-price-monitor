from fastapi.concurrency import run_in_threadpool

from src.database import get_database_session
from sqlalchemy.ext.asyncio import AsyncSession

from src.dns import get_dns_scraper, DNSWebScraper

from src.models import ProductSQLModel, PriceRecordSQLModel
from src.schemas import Product, ProductUrl, Price


def get_price(url: ProductUrl) -> Price:
    dns_gen = get_dns_scraper()
    dns: DNSWebScraper = dns_gen.__next__()
    price = dns.get_product_price(url)
    for _ in dns_gen:
        pass
    return price


async def update_price():
    db_session_gen = get_database_session()
    db: AsyncSession = await db_session_gen.__anext__()
    async for product in ProductSQLModel.get_all(db):
        product = Product.from_orm(product)
        current_price = await run_in_threadpool(get_price, url=product.url)
        price_record = await PriceRecordSQLModel.create(db, current_price, product.id)
    async for _ in db_session_gen:
        pass
