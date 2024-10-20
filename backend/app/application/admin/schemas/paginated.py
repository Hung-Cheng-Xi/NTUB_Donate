from typing import Generic, List, TypeVar
from sqlmodel import SQLModel

# 泛型定義，用於支援不同資料模型的分頁結果
T = TypeVar("T")

class PaginatedResponse(SQLModel, Generic[T]):
    """
    支援泛型的分頁回應模型。
    """
    total_count: int
    items: List[T]
