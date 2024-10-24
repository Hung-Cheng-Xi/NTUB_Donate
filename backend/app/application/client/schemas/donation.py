from datetime import date
from typing import Optional

from sqlmodel import SQLModel

from app.domain.models.donation import DonationType, DonorType, PubicStatus


class DonationsCreate(SQLModel):
    """
    用於創建 Donations 記錄的 schema，
    包含用戶需要提交的所有字段。
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
    public_status: PubicStatus = PubicStatus.PUBLIC
    memo: Optional[str] = None
    amount: int
    account: str
    type: DonationType = DonationType.STORE
    transaction_id: Optional[str] = None
    input_date: Optional[date] = None

    purpose_id: int


class DonationPurposeInfo(SQLModel):
    """
    用於返回 Donation 的子模型，
    適用於讀取操作。
    """

    title: str
    description: str

    class Config:
        from_attributes = True


class DonationInfo(SQLModel):
    """
    用於返回 Donations 的基本信息，
    適用於讀取操作。
    """

    username: str
    amount: int
    input_date: Optional[date] = None
    purpose: DonationPurposeInfo  # 嵌入 DonationPurposeInfo 子模型


class PaginatedDonationInfoResponse(SQLModel):
    """
    用於返回分頁的 Donation 的基本信息，
    適用於讀取操作，可返回總筆數。
    """

    total_count: int
    items: list[DonationInfo]
