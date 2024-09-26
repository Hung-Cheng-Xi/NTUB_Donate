from __future__ import annotations
from typing import TYPE_CHECKING, List
from sqlmodel import SQLModel, Field, Relationship

from app.domain.models.donation_purpose import DonationPurpose

if TYPE_CHECKING:
    from app.domain.models.news import News


class Unit(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

    news: List["News"] = Relationship(back_populates="unit")
    donation_purposes: List["DonationPurpose"] = Relationship(
        back_populates="unit")
