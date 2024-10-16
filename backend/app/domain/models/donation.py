from enum import Enum
from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlmodel import SQLModel, Field, Relationship


class DonationType(str, Enum):
    """表示捐款方式的 Enum。

    STORE: 使用實體店支付。
    BANK: 使用銀行支付。
    """
    STORE = "STORE"
    BANK = "BANK"

    def to_chinese(self) -> str:
        if self == DonationType.STORE:
            return "實體店支付"
        elif self == DonationType.BANK:
            return "銀行支付"

        return "未知"


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

    def to_chinese(self) -> str:
        if self == DonorType.ALUMNI:
            return "校友"
        elif self == DonorType.STAFF:
            return "教職員"
        elif self == DonorType.PARENT:
            return "家長"
        elif self == DonorType.COMMUNITY:
            return "社區成員"
        elif self == DonorType.CORPORATION:
            return "公司"
        elif self == DonorType.OTHER:
            return "其他"

        return "未知"


class PubicStatus(str, Enum):
    """表示公開狀態的 Enum。

    PUBLIC: 公開
    ANONYMOUS: 匿名
    PARTIALLY: 匿名但受捐單位知曉
    """
    PUBLIC = "PUBLIC"
    ANONYMOUS = "ANONYMOUS"
    PARTIALLY = "PARTIALLY"

    def to_chinese(self) -> str:
        if self == PubicStatus.PUBLIC:
            return "公開"
        elif self == PubicStatus.ANONYMOUS:
            return "匿名"
        elif self == PubicStatus.PARTIALLY:
            return "匿名但受捐單位知曉"

        return "未知"


if TYPE_CHECKING:
    from app.domain.models.donation_purpose import DonationPurpose


class Donation(SQLModel, table=True):
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
    transaction_id: Optional[str] = None
    input_date: Optional[date] = None

    purpose_id: int = Field(
        default=None,
        foreign_key="donationpurpose.id"
    )
    purpose: 'DonationPurpose' = Relationship(
        back_populates="donations"
    )
