import logging
from typing import Annotated, List

from app.application.admin.schemas.news import NewsCreate, NewsInfo
from app.domain.models.news import News
from app.infrastructure.repositories.news import NewsRepository
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/", response_model=List[NewsInfo])
async def get_news(
    repository: Annotated[NewsRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> List[NewsInfo]:
    logging.info("取得分頁的 News 資料")
    return await repository.get_news(skip, limit)


@router.post("/", response_model=News)
async def create_new(
    new_news: NewsCreate,
    repository: Annotated[NewsRepository, Depends()]
):
    logging.info("新增 News 資料到資料庫")
    return await repository.create_new(new_news)


@router.get("/{news_id}", response_model=News)
async def get_new(
    news_id: int,
    repository: Annotated[NewsRepository, Depends()]
):
    logging.info("取得 New 資料")
    return await repository.get_new(news_id)


@router.put("/{news_id}", response_model=News)
async def update_new(
    news_id: int,
    new_news: NewsCreate,
    repository: Annotated[NewsRepository, Depends()]
):
    logging.info("更新 News 資料")
    return await repository.update_new(news_id, new_news)


@router.patch("/{news_id}", response_model=News)
async def patch_new(
    news_id: int,
    new_news: NewsCreate,
    repository: Annotated[NewsRepository, Depends()]
):
    logging.info("部分更新 News 資料")
    return await repository.patch_new(news_id, new_news)


@router.delete("/{news_id}", response_model=News)
async def delete_new(
    news_id: int,
    repository: Annotated[NewsRepository, Depends()]
):
    logging.info("刪除 News 資料")
    return await repository.delete_new(news_id)
