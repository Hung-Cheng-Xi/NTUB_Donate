import logging

from typing import List, Annotated
from fastapi import APIRouter, Depends

from app.domain.models.announcement import Announcement
from app.application.utils.schemas.announcement import AnnouncementInfo
from app.infrastructure.repositories.announcement import AnnouncementRepository

router = APIRouter()


@router.get("/", response_model=List[AnnouncementInfo])
async def get_announcements(
    repository: Annotated[AnnouncementRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> List[AnnouncementInfo]:
    logging.info("取得分頁的 Announcement 資料")
    return await repository.get_announcements(skip, limit)


@router.get("/{announcement_id}", response_model=Announcement)
async def get_announcement(
    announcement_id: int,
    repository: Annotated[AnnouncementRepository, Depends()]
):
    logging.info("取得 Announcement 資料")
    return await repository.get_announcement(announcement_id)
