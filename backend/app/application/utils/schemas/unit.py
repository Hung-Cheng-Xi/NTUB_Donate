from sqlmodel import SQLModel


class UnitInfo(SQLModel):
    """用於返回 Unit 的基本信息，適用於讀取操作。"""
    name: str

    id: int

    class Config:
        from_attributes = True
