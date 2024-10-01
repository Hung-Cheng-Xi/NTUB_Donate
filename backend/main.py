import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.config import settings
from app.application.endpoints import main_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting the app")
    yield
    logging.info("Shutting down the app")

app = FastAPI(
    lifespan=lifespan,
    openapi_url="/openapi.json" if settings.enable_docs else None,
    docs_url="/docs" if settings.enable_docs else None,
    redoc_url="/redoc" if settings.enable_docs else None
)

app.include_router(main_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config="log.ini",
    )
