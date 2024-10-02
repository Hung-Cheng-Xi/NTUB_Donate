from pydantic import BaseModel, Field


class AddressData(BaseModel):
    address: str = Field(..., example="臺中市西屯區臺灣大道三段99號")
