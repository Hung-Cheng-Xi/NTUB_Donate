from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    user_name: str
    user_email: str
    user_phone_number: Optional[int] = None
    user_address: str
