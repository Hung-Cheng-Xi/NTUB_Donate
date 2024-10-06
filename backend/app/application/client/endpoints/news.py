import logging
from typing import List
from fastapi import APIRouter, Depends

from app.domain.models.news import News
from app.application.client.schemas.news import NewsCreate
from app.infrastructure.repositories.news import NewsRepository

router = APIRouter()


@router.get("/", response_model=List[News])
async def get_all_news(
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


@router.get("/{news_id}", response_model=News)
async def get_news(
    news_id: int,
    repository: NewsRepository = Depends(),
):
    logging.info("取得 News 資料")
    return await repository.get_news_by_id(news_id)


@router.put("/{news_id}", response_model=News)
async def update_news(
    news_id: int,
    new_news: NewsCreate,
    repository: NewsRepository = Depends(),
):
    logging.info("更新 News 資料")
    return await repository.update_news(news_id, new_news)


@router.patch("/{news_id}", response_model=News)
async def patch_news(
    news_id: int,
    new_news: NewsCreate,
    repository: NewsRepository = Depends(),
):
    logging.info("部分更新 News 資料")
    return await repository.patch_news(news_id, new_news)


@router.delete("/{news_id}", response_model=News)
async def delete_news(
    news_id: int,
    repository: NewsRepository = Depends(),
):
    logging.info("刪除 News 資料")
    return await repository.delete_news(news_id)
