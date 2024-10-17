from sqlmodel import SQLModel


class UnitInfo(SQLModel):
    """用於返回 Unit 的基本信息，適用於讀取操作。"""
    name: str

    id: int

    class Config:
        from_attributes = True


class UnitCreate(SQLModel):
    """
    用於創建 Unit 記錄的 schema，
    包含單位提交的所有必要字段。
    """
    name: str


class UnitUpdate(SQLModel):
    """
    用於更新 Unit 記錄的 schema，
    允許單位更新。
    """
    name: str
