# from enum import Enum
from typing import Optional, List
from datetime import datetime, date

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, DateTime, func
# from sqlalchemy import Enum as Column

from app.domain.models.donation import Donation

class User(SQLModel, table=True):
    """
    User model representing a user in the system.

    Attributes:
        user_id (int | None): The unique identifier for the user. Primary key.
        user_name (str): 使用者名稱
        user_birthday (Optional[date]): 使用者生日
        user_id_card (str): 使用者身分證字號
        user_phone_number (Optional[int]): 使用者電話號碼
        user_email (str): 使用者電子郵件
        user_identity (str): 使用者身分
        user_household_address (str): 使用者的戶籍地址
        user_correspondence_address (str): 使用者的通訊地址
        created_at (datetime): The timestamp when the user was created.
        updated_at (datetime): The timestamp when the user was last updated.
        donations (List["Donation"]): The list of donations associated with the user.
    """
    user_id: int | None = Field(default=None, primary_key=True)
    user_name: str
    user_birthday: Optional[date] = None
    user_id_card: str
    user_phone_number: Optional[int] = None
    user_email: str
    user_identity: str
    user_household_address: str
    user_correspondence_address: str

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

    donations: List["Donation"] = Relationship(back_populates="user")  # 修正 back_populates
