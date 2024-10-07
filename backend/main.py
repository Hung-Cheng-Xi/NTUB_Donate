import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

from fastapi.routing import APIRoute

from app.core.config import settings
from app.application.client.endpoints import client_router
from app.application.admin.endpoints import admin_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting the app")
    yield
    logging.info("Shutting down the app")

app = FastAPI(
    lifespan=lifespan,
    openapi_url="/openapi.json" if settings.enable_docs else None,
    docs_url="/docs" if settings.enable_docs else None,
    redoc_url="/redoc" if settings.enable_docs else None,
)


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


app.include_router(client_router, prefix="/api")
app.include_router(admin_router, prefix="/api")
use_route_names_as_operation_ids(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config="log.ini",
    )
