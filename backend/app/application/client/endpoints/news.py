import logging
from typing import List, Annotated
from fastapi import APIRouter, Depends

from app.domain.models.news import News
from app.infrastructure.repositories.news import NewsRepository

router = APIRouter()


@router.get("/", response_model=List[News])
async def get_all_news(
    repository: Annotated[NewsRepository, Depends()]
):
    logging.info("取得 News 資料")
    return await repository.get_all_newss()


@router.get("/{news_id}", response_model=News)
async def get_news(
    news_id: int,
    repository: Annotated[NewsRepository, Depends()]
):
    logging.info("取得 News 資料")
    return await repository.get_news_by_id(news_id)
