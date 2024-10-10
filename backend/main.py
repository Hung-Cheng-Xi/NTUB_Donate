import logging
import logging.config
import configparser
from fastapi import FastAPI
from fastapi.routing import APIRoute
from contextlib import asynccontextmanager

from app.core.settings import settings
from app.application.client.endpoints import client_router
from app.application.admin.endpoints import admin_router


def configure_logging():
    config = configparser.ConfigParser()
    config.read('log.ini')
    logging.config.fileConfig('log.ini')
    logging.info(f"Logging configured for {settings.env} environment")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("啟動應用程式")
    yield
    logging.info("關閉應用程式")


def create_app() -> FastAPI:
    configure_logging()

    app = FastAPI(
        lifespan=lifespan,
        openapi_url="/openapi.json" if settings.enable_docs else None,
        docs_url="/docs" if settings.enable_docs else None,
        redoc_url="/redoc" if settings.enable_docs else None,
    )

    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name

    app.include_router(client_router, prefix="/api")
    app.include_router(admin_router, prefix="/api")

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config="log.ini",
    )
