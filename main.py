from fastapi import FastAPI
from loguru import logger
from src.apis.routes.health import router as health_router
from src.apis.routes.user import router as user_router

app=FastAPI(title="A agent chat bot")

app.include_router(health_router)
app.include_router(user_router) 


def main():
    logger.info("Starting langgraph-bot...")





if __name__ == "__main__":
    main()
