from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    # 只在第一次遇到 TYPE_CHECKING 時，才會執行這個區塊避免循環引用
    from app.domain.models.donation import Donation
    from app.domain.models.unit import Unit


class DonationPurpose(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    lump_sum: int
    description: str
    memo: Optional[str] = None
    is_show: bool
    image_url: Optional[str] = Field(
        default=None,
        description="S3 圖片的 URL 或相對路徑"
    )

    unit_id: int = Field(default=None, foreign_key="unit.id")
    unit: "Unit" = Relationship(back_populates="donation_purposes")
    donations: List["Donation"] = Relationship(back_populates="purpose")
