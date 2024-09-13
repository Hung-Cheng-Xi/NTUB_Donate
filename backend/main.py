import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import create_db_and_tables
from app.application.endpoints.asset import router as asset_router
from app.application.endpoints.vulnerability_threat import router as vulnerability_threat_router
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting the app")
    await create_db_and_tables()
    yield
    logging.info("Shutting down the app")

app = FastAPI(
    lifespan=lifespan,
    openapi_url="/openapi.json" if settings.enable_docs else None,
    docs_url="/docs" if settings.enable_docs else None,
    redoc_url="/redoc" if settings.enable_docs else None
)

app.include_router(asset_router)
app.include_router(vulnerability_threat_router)
