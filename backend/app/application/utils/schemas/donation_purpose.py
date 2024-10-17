from typing import Optional
from sqlmodel import SQLModel

from app.application.utils.schemas.unit import UnitInfo


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


class DonationPurposeItem(SQLModel):
    """
    用於返回 DonationPurpose 的基本信息，適用於讀取操作。
    """
    title: str
    lump_sum: int
    description: str
    memo: Optional[str] = None
    is_show: bool
    total_donation: float
    achieved_percentage: float

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
