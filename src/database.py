from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from fastapi.encoders import jsonable_encoder
from typing import AsyncGenerator

from src.settings import POSTGRES_URL


engine: AsyncEngine = create_async_engine(
    url=str(POSTGRES_URL), json_serializer=jsonable_encoder
)


async def get_database_session() -> AsyncGenerator[AsyncSession, None]:
    """Generates async database session. Intended to be used as a dependency."""
    # NOTE: Such form of combining two context managers ensures
    # that `session.rollback()` happens in case of any exception been raised,
    # and `session.close()` at the end of working with session.
    async with AsyncSession(engine) as session, session.begin():
        yield session
