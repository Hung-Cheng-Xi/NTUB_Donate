from pydantic import Field
from sqlmodel import SQLModel


class AddressData(SQLModel):
    address: str = Field(..., example="臺中市西屯區臺灣大道三段99號")
