from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlmodel import or_, select

from app.application.admin.schemas.announcement import (
    AnnouncementCreate,
    AnnouncementInfo,
    AnnouncementUpdate,
    PaginatedAnnouncementInfoResponse,
)
from app.domain.models.announcement import Announcement
from app.infrastructure.repositories.base import BaseRepository


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
        search: str = None,
    ) -> PaginatedAnnouncementInfoResponse:
        """取得分頁的最新消息"""
        statement = self._build_announcement_query(skip, limit, search)
        announcements = await self._execute_announcement_query(statement)
        total_count = await self._get_total_count(search)

        return PaginatedAnnouncementInfoResponse(
            total_count=total_count,
            items=[AnnouncementInfo.model_validate(announcement) for announcement in announcements],
        )

    def _build_announcement_query(self, skip: int, limit: int, search: str = None):
        """建構查詢 Announcement 的 statement"""
        statement = (
            select(Announcement)
            .offset(skip)
            .limit(limit)
            .options(joinedload(Announcement.unit))
        )

        if search:
            statement = statement.where(
                or_(
                    Announcement.title.ilike(f"%{search}%"),
                    Announcement.description.ilike(f"%{search}%"),
                    Announcement.unit.has(Announcement.unit.property.mapper.class_.name.ilike(f"%{search}%"))
                )
            )

        return statement

    async def _execute_announcement_query(self, statement):
        """執行查詢 Announcement 的 statement"""
        results = await self.session.execute(statement)
        return results.scalars().all()

    async def _get_total_count(self, search: str = None):
        """查詢總筆數"""
        total_count_stmt = select(func.count(Announcement.id))

        if search:
            total_count_stmt = total_count_stmt.where(
                or_(
                    Announcement.title.ilike(f"%{search}%"),
                    Announcement.description.ilike(f"%{search}%"),
                    Announcement.unit.has(Announcement.unit.property.mapper.class_.name.ilike(f"%{search}%"))
                )
            )

        return (await self.session.execute(total_count_stmt)).scalar()


    async def update_announcement(
        self,
        announcement_id: int,
        updated_announcement: AnnouncementUpdate,
    ) -> AnnouncementUpdate:
        """更新一筆最新消息"""
        announcement = updated_announcement.model_dump()
        return await self.update_instance(
            announcement_id, announcement, Announcement
        )

    async def patch_announcement(
        self,
        announcement_id: int,
        updated_announcement: Announcement,
    ) -> Announcement:
        """部分更新一筆最新消息"""
        announcement = updated_announcement.model_dump()
        return await self.patch_instance(
            announcement_id, announcement, Announcement
        )

    async def delete_announcement(
        self,
        announcement_id: int,
    ) -> bool:
        """刪除一筆最新消息"""
        return await self.delete_instance(announcement_id, Announcement)
