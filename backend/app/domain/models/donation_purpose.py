from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, DateTime, func


if TYPE_CHECKING:
    from app.domain.models.unit import Unit
    from app.domain.models.donation import Donations


class DonationPurpose(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    summary: str
    memo: Optional[str] = None
    is_show: bool
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now()
        )
    )
    unit_id: int = Field(foreign_key="unit.id")

    unit: Optional["Unit"] = Relationship(back_populates="donation_purposes")
    donations: List["Donations"] = Relationship(back_populates="purpose")
