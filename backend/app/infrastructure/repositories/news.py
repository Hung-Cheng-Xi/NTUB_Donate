from app.application.admin.schemas.news import NewsCreate, NewsInfo
from app.domain.models.news import News
from app.infrastructure.repositories.base import BaseRepository


class NewsRepository(BaseRepository[News]):
    async def create_new(self, news_create: NewsCreate) -> News:
        """新增一筆最新消息"""
        news = News(**news_create.model_dump())
        return await self.create_instance(news)

    async def get_new(self, news_id: int) -> News:
        """根據最新消息 ID 取得最新消息"""
        return await self.get_by_id(news_id, News)

    async def get_news(self, skip: int, limit: int) -> list[NewsInfo]:
        """取得分頁的最新消息"""
        news = await self.get_paginated_all(News, skip, limit)
        return [NewsInfo.model_dump(new) for new in news]

    async def update_new(self, news_id: int, updated_news: News) -> News:
        """更新一筆最新消息"""
        news = updated_news.model_dump()
        return await self.update_instance(news_id, news, News)

    async def patch_new(self, news_id: int, updated_news: News) -> News:
        """部分更新一筆最新消息"""
        news = updated_news.model_dump()
        return await self.patch_instance(news_id, news, News)

    async def delete_new(self, news_id: int) -> bool:
        """刪除一筆最新消息"""
        return await self.delete_instance(news_id, News)
