from typing import Optional

from sqlmodel import SQLModel
from app.application.admin.schemas.donation import DonationInfo


class DonationPurposeItem(SQLModel):
    """
    用於返回 DonationPurpose 的基本信息，適用於讀取操作。
    """

    title: str
    lump_sum: int
    description: str
    memo: Optional[str] = None
    is_show: bool
    image_url: Optional[str] = None
    total_donation: float
    achieved_percentage: float

    id: int


class PaginatedDonationPurposeInfoResponse(SQLModel):
    """
    用於返回分頁的 DonationPurpose 的基本信息，
    適用於讀取操作，可返回總筆數。
    """

    total_count: int
    items: list[DonationPurposeItem]
