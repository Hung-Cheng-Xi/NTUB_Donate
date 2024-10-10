from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.news import News
from app.application.client.schemas.news import NewsCreate

from app.infrastructure.repositories.base import BaseRepository


class NewsRepository(BaseRepository[News]):
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db_session)]):
        super().__init__(session)

    async def create_news(self, news_create: NewsCreate) -> News:
        """新增一筆最新消息"""
        news = News(**news_create.model_dump())
        return await self.create_instance(news)

    async def get_news_by_id(self, news_id: int) -> News:
        """根據最新消息 ID 取得最新消息"""
        return await self.get_by_id(news_id, News)

    async def get_all_newss(self) -> list[News]:
        """取得所有最新消息"""
        return await self.get_all(News)

    async def update_news(self, news_id: int, updated_news: News) -> News:
        """更新一筆最新消息"""
        news = updated_news.model_dump()
        return await self.update_instance(news_id, news, News)

    async def patch_news(self, news_id: int, updated_news: News) -> News:
        """部分更新一筆最新消息"""
        news = updated_news.model_dump()
        return await self.patch_instance(news_id, news, News)

    async def delete_news(self, news_id: int) -> bool:
        """刪除一筆最新消息"""
        return await self.delete_instance(news_id, News)
