import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.database import create_db_and_tables
from app.application.endpoints.user import router as user_router
from app.application.endpoints.donation import router as donation_router


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

app.include_router(user_router)
app.include_router(donation_router)
