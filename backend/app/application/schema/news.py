from typing import TYPE_CHECKING, Optional
from datetime import date
from pydantic import BaseModel


if TYPE_CHECKING:
    from app.application.schema.unit import Unit


class NewsBase(BaseModel):
    """
    News 的基本 schema，包含必要的字段，
    這些字段主要用於創建或更新最新消息記錄。
    """
    date: date
    title: str
    description: str
    is_show: bool


class NewsCreate(NewsBase):
    """
    用於創建 News 記錄的 schema，
    繼承了 NewsBase，包含用戶提交的所有必要字段。
    """
    unit_id: int


class NewsUpdate(NewsBase):
    """
    用於更新 News 記錄的 schema，允許部分字段更新。
    """
    pass


class NewsInDBBase(NewsBase):
    """
    表示數據庫中 News 記錄的基礎結構，
    包含自動生成的 id，並啟用 orm_mode 以允許將 ORM 模型轉換為 Pydantic 模型。
    """
    id: Optional[int]

    class Config:
        from_attribute = True


class News(NewsInDBBase):
    """
    用於返回 News 的基本信息，
    繼承自 NewsInDBBase，適用於讀取操作。
    """
    pass


class NewsDetail(NewsInDBBase):
    """
    用於返回 News 的詳細信息，包含與 Unit 的關聯。
    """
    unit: Optional["Unit"]

    class Config:
        from_attribute = True
