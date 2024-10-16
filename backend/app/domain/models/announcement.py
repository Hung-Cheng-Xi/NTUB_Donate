from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from app.domain.models.unit import Unit


class Announcement(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    date: date
    title: str
    description: str
    is_show: bool

    unit_id: Optional[int] = Field(default=None, foreign_key="unit.id")
    unit: Optional["Unit"] = Relationship(back_populates="announcement")
