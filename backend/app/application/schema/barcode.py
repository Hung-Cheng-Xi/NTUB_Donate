from sqlmodel import SQLModel


class BarCodeData(SQLModel):
    Group: str = "730044" # 預設值
    SerialNumber: str = "00001" # 預設值
    Time: str = "9991230"  # 預設值
    Money: str = "1000" # 預設值
