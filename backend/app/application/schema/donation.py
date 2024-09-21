from enum import Enum
from pydantic import BaseModel
from typing import Optional

class PublicStatus(str, Enum):
   FULL_PUBLIC = "FULL_PUBLIC"
   PARTIALLY_PUBLIC = "PARTIALLY_PUBLIC"
   NOT_PUBLIC = "NOT_PUBLIC"

class DonationCreate(BaseModel):
    amount: Optional[float] = None
    currency: str
    payment_method: str
    payment_status: str
    transaction_id: str
    user_id: int
    public_status: Optional[PublicStatus] = PublicStatus.FULL_PUBLIC  # 設定預設值

    class Config:
        use_enum_values = True  # 在輸出時使用 Enum 的值，而不是其名稱
