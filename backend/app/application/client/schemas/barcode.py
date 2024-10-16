from pydantic import Field
from sqlmodel import SQLModel


class BarCodeData(SQLModel):
    """
    用於創建 BarCode 記錄的 schema，
    包含 BarCode 需要提交的所有字段。
    """

    Group: str = Field(..., example="730044")
    SerialNumber: str = Field(..., example="00001")
    Time: str = Field(..., example="9991230")
    Money: str = Field(..., example="1000")
