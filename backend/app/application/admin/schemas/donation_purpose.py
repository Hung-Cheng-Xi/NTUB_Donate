from typing import Optional
from sqlmodel import SQLModel


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
