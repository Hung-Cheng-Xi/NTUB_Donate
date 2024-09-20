from pydantic import BaseModel
from typing import Optional

class DonationCreate(BaseModel):
    amount: Optional[float] = None
    currency: str
    payment_method: str
    payment_status: str
    transaction_id: str
    user_id: int
