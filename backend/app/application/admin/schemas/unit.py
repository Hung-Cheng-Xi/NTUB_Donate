from sqlmodel import SQLModel


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
