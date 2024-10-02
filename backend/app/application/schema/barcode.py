from pydantic import Field
from sqlmodel import SQLModel


class BarCodeData(SQLModel):
    group: str = Field(..., example="730044")
    serial_number: str = Field(..., example="00001")
    time: str = Field(..., example="9991230")
    money: str = Field(..., example="1000")
