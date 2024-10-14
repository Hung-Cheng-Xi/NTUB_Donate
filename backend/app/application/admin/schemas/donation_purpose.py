from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from app.application.admin.schemas.unit import UnitInfo
    from app.application.admin.schemas.donation import DonationInfo


class DonationPurposeBase(SQLModel):
    """包含所有 DonationPurpose 模型的基本字段，
    這些字段通常是創建和更新操作需要的數據。
    不包括自動生成的 id、created_at 和 updated_at。
    """
    name: str
    lump_sum: int
    summary: str
    memo: Optional[str] = None
    is_show: bool


class DonationPurposeCreate(DonationPurposeBase):
    """用於創建 DonationPurpose 時的 schema。
    繼承了 DonationPurposeBase，並且增加了 unit_id，因為創建時需要指定一個單位。
    """
    unit_id: int


class DonationPurposeUpdate(DonationPurposeBase):
    """用於更新 DonationPurpose 的 schema。
    繼承了 DonationPurposeBase，允許更新部分或全部字段。
    """
    pass


class DonationPurposeInDBBase(DonationPurposeBase):
    """表示數據庫中 DonationPurpose 的基本結構。
    包含自動生成的字段，如 id、created_at 和 updated_at。
    from_attributes 被設置為 True 以允許 ORM 模型自動轉換為 Pydantic 模型。
    """
    id: Optional[int]
    # created_at: datetime
    # updated_at: datetime
    unit_id: int

    class Config:
        from_attributes = True


class DonationPurposeInfo(DonationPurposeInDBBase):
    """用於返回 DonationPurpose 的基本信息。
    繼承了 DonationPurposeInDBBase，適用於讀取操作。
    """
    pass


class DonationPurposeDetail(DonationPurposeInDBBase):
    """用於返回 DonationPurpose 的詳細信息。
    包含與 UnitInfo 和 DonationInfo 之間的關聯關係，用於返回更詳細的數據。
    """
    unit: Optional["UnitInfo"]
    donations: List["DonationInfo"] = []

    class Config:
        from_attributes = True
