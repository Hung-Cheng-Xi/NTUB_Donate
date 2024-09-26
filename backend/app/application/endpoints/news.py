from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.domain.models.news import News
from app.application.schema.news import NewsCreate
from app.infrastructure.repositories.news import NewsRepository

router = APIRouter()


@router.get("/", response_model=List[News])
async def read_News(db: AsyncSession = Depends(get_db)):
    donation_purpose_repo = NewsRepository(db)
    newss = await donation_purpose_repo.get_all_newss()
    return newss


@router.post("/", response_model=News)
async def create_news(new_news: NewsCreate, db: AsyncSession = Depends(get_db)):
    news_repo = NewsRepository(db)
    created_news = await news_repo.create_news(new_news)
    return created_news
