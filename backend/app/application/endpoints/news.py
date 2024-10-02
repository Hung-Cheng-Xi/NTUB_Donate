import logging
from typing import List
from fastapi import APIRouter, Depends

from app.domain.models.news import News
from app.application.schema.news import NewsCreate
from app.infrastructure.repositories.news import NewsRepository

router = APIRouter()


@router.get("/", response_model=List[News])
async def get_news(
    repository: NewsRepository = Depends(),
):
    logging.info("取得 News 資料")
    return await repository.get_all_newss()


@router.post("/", response_model=News)
async def create_news(
    new_news: NewsCreate,
    repository: NewsRepository = Depends(),
):
    logging.info("新增 News 資料到資料庫")
    return await repository.create_news(new_news)
