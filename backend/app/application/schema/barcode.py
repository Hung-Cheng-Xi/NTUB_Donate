from pydantic import Field
from sqlmodel import SQLModel


class BarCodeData(SQLModel):
    Group: str = Field(..., example="730044")
    SerialNumber: str = Field(..., example="00001")
    Time: str = Field(..., example="9991230")
    Money: str = Field(..., example="1000")
