from datetime import date
from typing import Optional

from sqlmodel import SQLModel

from app.application.admin.schemas.donation_purpose import DonationPurposeInfo
from app.domain.models.donation import DonationType, DonorType, PubicStatus


class DonationInfo(SQLModel):
    """
    用於返回 Donations 的基本信息，
    適用於讀取操作。
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
    status: Optional[int] = None
    transaction_id: Optional[str] = None
    input_date: Optional[date] = None

    id: int
    purpose_id: int


class PaginatedDonationInfoResponse(SQLModel):
    """
    用於返回分頁的 Donation 的基本信息，
    適用於讀取操作，可返回總筆數。
    """

    total_count: int
    items: list[DonationInfo]


class DonationUpdate(SQLModel):
    """
    用於更新 Donation 的 schema，
    允許捐款更新。
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


class ExcelExportInfo(SQLModel):
    """
    用於返回 ExcelExport 的基本信息，
    適用於讀取操作。
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
    status: Optional[int] = None
    transaction_id: Optional[str] = None
    input_date: Optional[date] = None

    id: int
    purpose: DonationPurposeInfo
