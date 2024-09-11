from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.core.config import create_db_and_tables

from app.application.endpoints.hero import router as hero_router 

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(hero_router)
