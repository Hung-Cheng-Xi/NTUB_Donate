from typing import Optional
from datetime import datetime

from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime
from sqlmodel import SQLModel, Field, Relationship

class Donation(SQLModel, table=True):
    donation_id: int | None = Field(default=None, primary_key=True)
    amount: Optional[float] = None
    currency: str
    payment_method: str
    payment_status: str
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

    user_id: Optional[int] = Field(default=None, foreign_key="user.user_id")
    user: Optional["User"] = Relationship(back_populates="donations")
