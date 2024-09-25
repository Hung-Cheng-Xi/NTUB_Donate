from datetime import datetime

from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime, func


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    account: str
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
