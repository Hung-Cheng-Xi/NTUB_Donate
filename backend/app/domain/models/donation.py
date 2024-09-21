from enum import Enum
from typing import Optional
from datetime import datetime

# from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime, func
from sqlalchemy import Enum as SQLAlchemyEnum, Column
from sqlmodel import SQLModel, Field, Relationship

class PublicStatus(str, Enum):
   FULL_PUBLIC = "FULL_PUBLIC"
   PARTIALLY_PUBLIC = "PARTIALLY_PUBLIC"
   NOT_PUBLIC = "NOT_PUBLIC"

class Donation(SQLModel, table=True):
    """
    Represents a donation record in the system.

    Attributes:
        donation_id (int | None): The unique identifier for the donation.
        amount (Optional[float]): 捐款金額
        currency (str): 捐款貨幣類型
        payment_method (str): 支付方式
        payment_status (str): 支付狀態
        transaction_id (str): 金流平台返還ID
        public_status (Optional[PublicStatus]): 狀態是否公開
        created_at (datetime): The timestamp when the donation was created.
        updated_at (datetime): The timestamp when the donation was last updated.
    """

    donation_id: int | None = Field(default=None, primary_key=True)
    amount: Optional[float] = None
    currency: str
    payment_method: str
    payment_status: str
    transaction_id: str
    public_status: Optional[PublicStatus] = Field(
        sa_column=Column(
            SQLAlchemyEnum(PublicStatus, name="publicstatus", create_type=True)
        )
    )

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
