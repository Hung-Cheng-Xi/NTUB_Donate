from enum import Enum
from typing import TYPE_CHECKING, Optional
from datetime import date

from sqlmodel import SQLModel, Field, Relationship


class DonationType(str, Enum):
    """表示捐款方式的 Enum。

    STORE: 使用實體店支付。
    BANK: 使用銀行支付。
    """
    STORE = "STORE"
    BANK = "BANK"


class DonorType(Enum):
    """表示捐款者身份的 Enum。

    ALUMNI: 校友
    STAFF: 教職員
    PARENT: 家長
    COMMUNITY: 社區成員
    CORPORATION: 公司
    OTHER: 其他
    """
    ALUMNI = "ALUMNI"
    STAFF = "STAFF"
    PARENT = "PARENT"
    COMMUNITY = "COMMUNITY"
    CORPORATION = "CORPORATION"
    OTHER = "OTHER"


class PubicStatus(str, Enum):
    """表示公開狀態的 Enum。

    PUBLIC: 公開
    ANONYMOUS: 匿名
    PARTIALLY: 匿名但受捐單位知曉
    """
    PUBLIC = "PUBLIC"
    ANONYMOUS = "ANONYMOUS"
    PARTIALLY = "PARTIALLY"


if TYPE_CHECKING:
    from app.domain.models.donation_purpose import DonationPurpose


class Donations(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    user_birthday: date
    id_card: str
    phone_number: str
    email: str
    identity: DonorType = Field(
        default=DonorType.ALUMNI,
        description="捐款者身分"
    )
    year: Optional[str] = None
    gept: Optional[str] = None
    res_address: str
    registered_address: str
    public_status: PubicStatus = Field(
        default=PubicStatus.PUBLIC,
        description="公開狀態"
    )
    memo: Optional[str] = None
    amount: int
    account: str
    type: DonationType = Field(
        default=DonationType.STORE,
        description="捐款方式"
    )
    status: Optional[int] = None
    transaction_id: Optional[str] = None
    input_date: Optional[str] = None

    purpose_id: Optional[int] = Field(
        default=None,
        foreign_key="donationpurpose.id"
    )
    purpose: Optional["DonationPurpose"] = Relationship(
        back_populates="donations"
    )
