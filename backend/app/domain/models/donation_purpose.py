from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    # 只在第一次遇到 TYPE_CHECKING 時，才會執行這個區塊避免循環引用
    from app.domain.models.unit import Unit
    from app.domain.models.donation import Donations


class DonationPurpose(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    summary: str
    memo: Optional[str] = None
    is_show: bool

    unit_id: Optional[int] = Field(default=None, foreign_key="unit.id")
    unit: Optional["Unit"] = Relationship(back_populates="donation_purposes")

    donations: List["Donations"] = Relationship(back_populates="purpose")
