from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    user_name: str
    user_birthday: Optional[date] = None
    user_id_card: str
    user_phone_number: Optional[int] = None
    user_email: str
    user_identity: str
    user_household_address: str
    user_correspondence_address: str
