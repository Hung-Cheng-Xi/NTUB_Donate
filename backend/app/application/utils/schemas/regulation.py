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
