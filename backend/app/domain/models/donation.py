from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from datetime import datetime, date

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, DateTime, func


if TYPE_CHECKING:
    from app.domain.models.donation_purpose import DonationPurpose


class Donations(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    user_birthday: date
    id_card: str
    phone_number: str
    email: str
    identity: str
    year: str
    gept: str
    res_address: str
    registered_address: str
    public_status: str
    memo: Optional[str] = None
    amount: int
    account: str
    type: str
    status: str
    transaction_id: str
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
    purpose_id: int = Field(foreign_key="donationpurpose.id")


purpose: Optional["DonationPurpose"] = Relationship(back_populates="donations")
