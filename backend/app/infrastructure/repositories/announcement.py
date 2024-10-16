from app.domain.models.announcement import Announcement
from app.infrastructure.repositories.base import BaseRepository
from app.application.admin.schemas.announcement import (
    AnnouncementInfo,
    AnnouncementCreate,
    AnnouncementUpdate
)

from sqlmodel import select
from sqlalchemy.orm import joinedload


class AnnouncementRepository(BaseRepository[Announcement]):
    async def create_announcement(
        self,
        announcement_create: AnnouncementCreate,
    ) -> Announcement:
        """新增一筆最新消息"""
        announcement = Announcement(**announcement_create.model_dump())
        return await self.create_instance(announcement)

    async def get_announcement(
        self,
        announcement_id: int,
    ) -> Announcement:
        """根據最新消息 ID 取得最新消息"""
        return await self.get_by_id(announcement_id, Announcement)

    async def get_announcements(
        self,
        skip: int,
        limit: int,
    ) -> list[AnnouncementInfo]:
        """取得分頁的最新消息"""
        # 查詢 Announcement 並加載與 unit 的關聯
        statement = select(Announcement).offset(skip).limit(
            limit).options(joinedload(Announcement.unit))
        results = await self.session.execute(statement)
        announcements = results.scalars().all()

        return [
            AnnouncementInfo.model_validate(announcement)
            for announcement in announcements
        ]

    async def update_announcement(
        self,
        announcement_id: int,
        updated_announcement: AnnouncementUpdate,
    ) -> AnnouncementUpdate:
        """更新一筆最新消息"""
        announcement = updated_announcement.model_dump()
        return await self.update_instance(
            announcement_id,
            announcement,
            Announcement
        )

    async def patch_announcement(
        self,
        announcement_id: int,
        updated_announcement: Announcement,
    ) -> Announcement:
        """部分更新一筆最新消息"""
        announcement = updated_announcement.model_dump()
        return await self.patch_instance(
            announcement_id,
            announcement,
            Announcement
        )

    async def delete_announcement(
        self,
        announcement_id: int,
    ) -> bool:
        """刪除一筆最新消息"""
        return await self.delete_instance(announcement_id, Announcement)
