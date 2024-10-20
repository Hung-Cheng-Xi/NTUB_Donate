from typing import Optional

from sqlmodel import SQLModel


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
