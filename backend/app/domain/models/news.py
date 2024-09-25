from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from datetime import date

from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from app.domain.models.unit import Unit

class News(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date: date
    title: str
    description: str
    is_show: bool
    unit_id: int = Field(foreign_key="unit.id")

    unit: Optional["Unit"] = Relationship(back_populates="news")
