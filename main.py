import os
from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from loguru import logger

from src.apis.routes.health import router as health_router
from src.apis.routes.user import router as user_router
from src.db.database import check_db_connection, close_db_engine


load_dotenv()


@asynccontextmanager
async def lifespan(_: FastAPI):
    await check_db_connection()
    yield
    await close_db_engine()


app = FastAPI(title="A agent chat bot", lifespan=lifespan)

app.include_router(health_router)
app.include_router(user_router)


def load_config():
    load_dotenv()


def main():
    load_config()
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    logger.info(f"Starting langgraph-bot on {host}:{port}...")
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
