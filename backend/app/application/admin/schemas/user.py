from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class UserBase(SQLModel):
    """User 的基本 schema，包含必要的字段，如 account。
    不包含自動生成的 id。
    """
    account: str


class UserCreate(UserBase):
    """用於創建 User 記錄的 schema，繼承 UserBase。
    包含用戶提交的所有必要字段。
    """
    pass


class UserUpdate(UserBase):
    """用於更新 User 記錄的 schema，允許部分字段更新。"""
    pass


class UserInDBBase(UserBase):
    """表示數據庫中 User 記錄的基礎結構，包含自動生成的 id。
    from_attributes 設置為 True，以允許 SQLAlchemy 模型轉換為 Pydantic 模型。
    """
    id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True


class UserInfo(UserInDBBase):
    """用於返回 User 的基本信息，繼承 UserInDBBase，適用於讀取操作。"""
    pass
