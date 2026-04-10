from fastapi import FastAPI
from loguru import logger
import os
import uvicorn
from src.apis.routes.health import router as health_router
from src.apis.routes.user import router as user_router

app=FastAPI(title="A agent chat bot")

app.include_router(health_router)
app.include_router(user_router) 


def main():
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    logger.info(f"Starting langgraph-bot on {host}:{port}...")
    uvicorn.run(app, host=host, port=port)





if __name__ == "__main__":
    main()
