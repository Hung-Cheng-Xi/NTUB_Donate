from typing import Optional
from sqlmodel import SQLModel

from app.application.admin.schemas.unit import UnitInfo


class AdminDonationPurposeItem(SQLModel):
    """
    用於返回 DonationPurpose 的基本信息，適用於讀取操作。
    """
    title: str
    lump_sum: int
    description: str
    memo: Optional[str] = None
    is_show: bool

    id: int


class DonationPurposeInfo(SQLModel):
    """
    用於返回 DonationPurpose 的基本信息，適用於讀取操作。
    """
    title: str
    lump_sum: int
    description: str
    memo: Optional[str] = None
    total_donation: Optional[float] = None
    achieved_percentage: Optional[float] = None

    id: int
    unit: UnitInfo



class DonationPurposeCreate(SQLModel):
    """
    用於創建 DonationPurpose 紀錄的 schema。
    包含捐款目的提交的所有必要字段。
    """
    title: str
    lump_sum: int
    description: str
    memo: Optional[str] = None
    is_show: bool

    unit_id: int


class DonationPurposeUpdate(SQLModel):
    """
    用於更新 DonationPurpose 的 schema，
    允許捐款目的更新。
    """
    title: str
    lump_sum: int
    description: str
    memo: Optional[str] = None
    is_show: bool

    unit_id: int
