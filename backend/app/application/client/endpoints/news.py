import logging
from typing import List, Annotated
from fastapi import APIRouter, Depends

from app.domain.models.news import News
from app.infrastructure.repositories.news import NewsRepository
from app.application.admin.schemas.news import NewsInfo

router = APIRouter()


@router.get("/", response_model=List[NewsInfo])
async def get_news(
    repository: Annotated[NewsRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> List[NewsInfo]:
    logging.info("取得分頁的 News 資料")
    return await repository.get_news(skip, limit)


@router.get("/{news_id}", response_model=News)
async def get_new(
    news_id: int,
    repository: Annotated[NewsRepository, Depends()]
):
    logging.info("取得 News 資料")
    return await repository.get_new(news_id)
