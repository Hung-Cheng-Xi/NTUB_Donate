from datetime import date
from sqlmodel import SQLModel

from app.application.admin.schemas.unit import UnitInfo


class AnnouncementInfo(SQLModel):
    """
    用於返回 New 的基本信息，
    適用於讀取操作。
    """
    date: date
    title: str
    description: str
    is_show: bool

    id: int
    unit: UnitInfo


class AnnouncementCreate(SQLModel):
    """
    用於創建 Announcement 記錄的 schema，
    包含公告需要提交的所有字段。
    """
    date: date
    title: str
    description: str
    is_show: bool

    unit_id: int


class AnnouncementUpdate(SQLModel):
    """
    用於更新 Announcement 記錄的 schema，
    允許公告更新。
    """
    date: date
    title: str
    description: str
    is_show: bool

    id: int
    unit_id: int
