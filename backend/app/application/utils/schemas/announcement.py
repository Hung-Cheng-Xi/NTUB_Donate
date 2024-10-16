from datetime import date
from sqlmodel import SQLModel

from app.application.utils.schemas.unit import UnitInfo


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
