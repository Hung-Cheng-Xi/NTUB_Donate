from typing import TYPE_CHECKING, List

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.domain.models.announcement import Announcement
    from app.domain.models.donation_purpose import DonationPurpose


class Unit(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    announcement: List["Announcement"] = Relationship(back_populates="unit")
    donation_purposes: List["DonationPurpose"] = Relationship(
        back_populates="unit"
    )
