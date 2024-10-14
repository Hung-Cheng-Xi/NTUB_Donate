from typing import Optional
from sqlmodel import SQLModel


class UnitBase(SQLModel):
    """Unit 的基本 schema，包含必要的字段，用於創建或更新 Unit 記錄。"""
    name: str


class UnitInDBBase(UnitBase):
    """表示數據庫中 Unit 記錄的基礎結構，
    包含自動生成的 id，並啟用 from_attributes 以允許將 ORM 模型轉換為 Pydantic 模型。
    """
    id: Optional[int]

    class Config:
        from_attributes = True


class UnitInfo(UnitInDBBase):
    """用於返回 Unit 的基本信息，繼承自 UnitInDBBase，適用於讀取操作。"""
    pass
