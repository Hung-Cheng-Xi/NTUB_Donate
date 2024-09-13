from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class asset(SQLModel, table=True):
    asset_id: int | None = Field(default=None, primary_key=True)
    asset_name: str
    asset_type: str
    owner: str
    location: str
    classification_level: str
    risk_level: str
    creation_date: datetime
    status: str
    asset_value: Optional[float] = None
    vendor: Optional[str] = None
    lifetime: Optional[int] = None
    notes: Optional[str] = None
