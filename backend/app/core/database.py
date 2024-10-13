from typing import AsyncGenerator
from urllib.parse import quote_plus
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

from app.core.settings import settings


def get_database_url(async_mode: bool = True) -> str:
    user = settings.postgres_user
    password = settings.postgres_password
    host = settings.postgres_host
    port = settings.postgres_port
    database = settings.postgres_db
    encoded_password = quote_plus(password)

    if async_mode:
        return (
            f"postgresql+asyncpg://{user}:{
                encoded_password}@{host}:{port}/{database}"
        )
    else:
        return (
            f"postgresql://{user}:{
                encoded_password}@{host}:{port}/{database}"
        )


DATABASE_URL = get_database_url()

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
