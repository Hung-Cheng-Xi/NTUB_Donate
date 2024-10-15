from typing import TYPE_CHECKING, List, Optional

from sqlmodel import SQLModel

if TYPE_CHECKING:
    from app.application.admin.schemas.donation_purpose import \
        DonationPurposeInfo
    from app.application.admin.schemas.news import NewsInfo


class UnitBase(SQLModel):
    """Unit 的基本 schema，包含必要的字段，用於創建或更新 Unit 記錄。"""
    name: str


class UnitCreate(UnitBase):
    """用於創建 Unit 記錄的 schema，繼承了 UnitBase，包含用戶提交的所有必要字段。"""
    pass


class UnitUpdate(UnitBase):
    """用於更新 Unit 記錄的 schema，允許部分字段更新。"""
    pass


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


class UnitDetail(UnitInDBBase):
    """用於返回 Unit 的詳細信息，包含與 DonationPurposeInfo 和 News 的關聯。"""
    donation_purposes: List["DonationPurposeInfo"] = []
    news: List["NewsInfo"] = []

    class Config:
        from_attributes = True
