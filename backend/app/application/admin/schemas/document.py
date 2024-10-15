from typing import Optional

from app.domain.models.domcument import DocumentCategory
from sqlmodel import SQLModel


class DocumentBase(SQLModel):
    """Document 的基本 schema，包含必要的字段，
    這些字段主要用於創建或更新最新消息記錄。
    """
    title: str
    category: DocumentCategory = DocumentCategory.ALL
    description_link: str
    is_show: bool


class DocumentCreate(DocumentBase):
    """用於創建 Document 記錄的 schema，
    繼承了 DocumentBase，包含相關法規提交的所有必要字段。
    """
    pass


class DocumentUpdate(DocumentBase):
    """用於更新 Document 記錄的 schema，
    允許部分字段更新。
    """
    pass


class DocumentInDBBase(DocumentBase):
    """表示數據庫中 Document 記錄的基礎結構，
    包含自動生成的 id，並啟用 from_attributes 以允許將 ORM 模型轉換為 Pydantic 模型。
    """
    id: Optional[int]

    class Config:
        from_attributes = True


class DocumentInfo(DocumentInDBBase):
    """用於返回 Document 的基本信息，
    繼承自 DocumentInDBBase，適用於讀取操作。
    """
    pass
