from sqlmodel import SQLModel


class UserCreate(SQLModel):
    """用於創建 User 記錄的 schema，
    包含用戶提交的所有必要字段。
    """

    account: str


class UserUpdate(SQLModel):
    """
    用於更新 User 記錄的 schema，
    允許用戶更新。
    """

    account: str


class UserInfo(SQLModel):
    """
    用於返回 User 的基本信息，
    適用於讀取操作。
    """

    account: str

    id: int
