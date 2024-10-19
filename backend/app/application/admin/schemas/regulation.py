from sqlmodel import SQLModel

from app.domain.models.regulation import RegulationCategory


class RegulationInfo(SQLModel):
    """
    用於返回 Regulation 的基本信息，
    適用於讀取操作。
    """

    title: str
    category: RegulationCategory = RegulationCategory.ALL
    description_link: str
    is_show: bool

    id: int


class RegulationCreate(SQLModel):
    """
    用於創建 Regulationt 記錄的 schema，
    包含用戶提交的所有必要字段。
    """

    title: str
    category: RegulationCategory = RegulationCategory.ALL
    description_link: str
    is_show: bool


class RegulationtUpdate(SQLModel):
    """
    用於更新 Regulationt 記錄的 schema，
    允許法規更新。
    """

    title: str
    category: RegulationCategory = RegulationCategory.ALL
    description_link: str
    is_show: bool
