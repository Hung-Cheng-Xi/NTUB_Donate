import logging
from typing import Annotated, List

from fastapi import APIRouter, Depends

from app.application.admin.schemas.announcement import (
    AnnouncementCreate,
    AnnouncementInfo,
    AnnouncementUpdate,
)
from app.domain.models.announcement import Announcement
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


@router.post("/", response_model=Announcement)
async def create_announcement(
    new_announcement: AnnouncementCreate,
    repository: Annotated[AnnouncementRepository, Depends()],
):
    logging.info("新增 Announcement 資料到資料庫")
    return await repository.create_announcement(new_announcement)


@router.get("/{announcement_id}", response_model=Announcement)
async def get_announcement(
    announcement_id: int,
    repository: Annotated[AnnouncementRepository, Depends()],
):
    logging.info("取得 Announcement 資料")
    return await repository.get_announcement(announcement_id)


@router.put("/{announcement_id}", response_model=Announcement)
async def update_announcement(
    announcement_id: int,
    new_announcement: AnnouncementUpdate,
    repository: Annotated[AnnouncementRepository, Depends()],
):
    logging.info("更新 Announcement 資料")
    return await repository.update_announcement(
        announcement_id, new_announcement
    )


@router.delete("/{announcement_id}", response_model=Announcement)
async def delete_announcement(
    announcement_id: int,
    repository: Annotated[AnnouncementRepository, Depends()],
):
    logging.info("刪除 Announcement 資料")
    return await repository.delete_announcement(announcement_id)
