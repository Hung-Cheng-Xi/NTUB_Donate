from typing import Optional, List
from datetime import datetime, timezone

from sqlmodel import SQLModel, Field, Relationship

from app.domain.models.donation import Donation

class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    user_name: str
    user_email: str
    user_phone_number: Optional[int] = None
    user_address: str
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        sa_column_kwargs={"onupdate": datetime.now(timezone.utc).replace(tzinfo=None)}
    )

    donations: List["Donation"] = Relationship(back_populates="user")  # 修正 back_populates
