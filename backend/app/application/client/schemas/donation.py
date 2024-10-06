from typing import TYPE_CHECKING, Optional
from datetime import datetime, date
from sqlmodel import SQLModel

from app.domain.models.donation import DonorType, DonationType


if TYPE_CHECKING:
    from app.application.client.schemas.donation_purpose import DonationPurpose


class DonationsBase(SQLModel):
    """
    Donations 的基本 schema，包含基本的字段定義，用於創建或更新捐款記錄。
    不包含自動生成的字段如 id、created_at 和 updated_at。
    """
    username: str
    user_birthday: date
    id_card: str
    phone_number: str
    email: str
    identity: DonorType = DonorType.ALUMNI
    year: Optional[str] = None
    gept: Optional[str] = None
    res_address: str
    registered_address: str
    public_status: str
    memo: Optional[str] = None
    amount: int
    account: str
    type: DonationType = DonationType.STORE
    status: Optional[int] = None
    transaction_id: Optional[str] = None
    purpose_id: int


class DonationsCreate(DonationsBase):
    """
    用於創建 Donations 記錄的 schema，繼承 DonationsBase。
    包含用戶需要提交的所有字段。
    """
    pass


class DonationsUpdate(DonationsBase):
    """
    用於更新 Donations 記錄的 schema，允許部分字段更新。
    """
    pass


class DonationsInDBBase(DonationsBase):
    """
    表示數據庫中 Donations 記錄的基礎結構。
    包含自動生成的 id、created_at 和 updated_at，並啟用 orm_mode 以允許將 ORM 模型轉換為 Pydantic 模型。
    """
    id: Optional[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Donations(DonationsInDBBase):
    """
    用於返回 Donations 的基本信息。
    繼承 DonationsInDBBase，適用於讀取操作。
    """
    pass


class DonationsDetail(DonationsInDBBase):
    """
    用於返回 Donations 的詳細信息，包含與 DonationPurpose 的關聯。
    """
    purpose: Optional["DonationPurpose"]

    class Config:
        orm_mode = True
