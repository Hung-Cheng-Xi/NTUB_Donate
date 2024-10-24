import logging
from typing import Annotated, List

from fastapi import APIRouter, Depends

from app.application.admin.schemas.announcement import AnnouncementInfo
from app.domain.models.announcement import Announcement
from app.infrastructure.repositories.announcement import AnnouncementRepository

router = APIRouter()


@router.get("/", response_model=List[AnnouncementInfo])
async def client_get_announcements(
    repository: Annotated[AnnouncementRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> List[AnnouncementInfo]:
    logging.info("取得分頁的 Announcement 資料")
    return await repository.get_announcements(skip, limit)


@router.get("/{announcement_id}", response_model=Announcement)
async def client_get_announcement(
    announcement_id: int,
    repository: Annotated[AnnouncementRepository, Depends()],
):
    logging.info("取得 Announcement 資料")
    return await repository.get_announcement(announcement_id)
