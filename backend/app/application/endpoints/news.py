import logging
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.news import News
from app.application.schema.news import NewsCreate
from app.infrastructure.repositories.news import NewsRepository

router = APIRouter()


@router.get("/", response_model=List[News])
async def read_News(db: AsyncSession = Depends(get_db_session)):
    donation_purpose_repo = NewsRepository(db)
    newss = await donation_purpose_repo.get_all_newss()
    logging.info("取得 News 資料")
    return newss


@router.post("/", response_model=News)
async def create_news(new_news: NewsCreate, db: AsyncSession = Depends(get_db_session)):
    news_repo = NewsRepository(db)
    created_news = await news_repo.create_news(new_news)
    logging.info("新增 News 資料到資料庫")
    return created_news
