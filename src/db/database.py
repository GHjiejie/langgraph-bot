import os
from functools import lru_cache
from typing import AsyncGenerator

from dotenv import load_dotenv
from loguru import logger
from sqlalchemy import text
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


load_dotenv()


def get_database_url() -> str | URL:
    database_url = os.getenv("MYSQL_DATABASE_URL")
    if database_url:
        return database_url

    mysql_host = os.getenv("MYSQL_HOST", "127.0.0.1")
    mysql_port = int(os.getenv("MYSQL_PORT", "3306"))
    mysql_user = os.getenv("MYSQL_USER", "root")
    mysql_password = os.getenv("MYSQL_PASSWORD", "")
    mysql_database = (
        os.getenv("MYSQL_DATABASE")
        or os.getenv("MYSQL_DB")
        or "langgraph_bot"
    )

    return URL.create(
        "mysql+asyncmy",
        username=mysql_user,
        password=mysql_password,
        host=mysql_host,
        port=mysql_port,
        database=mysql_database,
        query={"charset": "utf8mb4"},
    )


@lru_cache
def get_db_engine():
    return create_async_engine(
        get_database_url(),
        echo=False,
        pool_pre_ping=True,
    )


@lru_cache
def get_session_factory():
    return async_sessionmaker(
        bind=get_db_engine(),
        class_=AsyncSession,
        expire_on_commit=False,
    )


async def check_db_connection() -> None:
    engine = get_db_engine()
    try:
        async with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))
        logger.info("Database connection check passed.")
    except Exception:
        logger.exception("Database connection check failed.")
        raise


async def close_db_engine() -> None:
    await get_db_engine().dispose()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    session_factory = get_session_factory()
    async with session_factory() as session:
        yield session
