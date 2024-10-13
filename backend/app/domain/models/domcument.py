from enum import Enum
from sqlmodel import SQLModel, Field


class DocumentCategory(str, Enum):
    """表示相關法規方式的 Enum。

    ALL: 全部
    DEPARTMENT_LAWS: 各部法規
    COMMERCIAL_LAW: 北商大法規
    TAX_RELATED_LAWS: 相關稅法
    DONATION_FORMS_DOWNLOAD: 捐款相關表單下載
    """
    ALL = "ALL"
    DEPARTMENT_LAWS = "DEPARTMENT_LAWS"
    COMMERCIAL_LAW = "COMMERCIAL_LAW"
    TAX_RELATED_LAWS = "TAX_RELATED_LAWS"
    DONATION_FORMS_DOWNLOAD = "DONATION_FORMS_DOWNLOAD"


class Document(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    category: DocumentCategory = Field(
        default=DocumentCategory.ALL,
        description="相關法規類別"
    )
    description_link: str
    is_show: bool
