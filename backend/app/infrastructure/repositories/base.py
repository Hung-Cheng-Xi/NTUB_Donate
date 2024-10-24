from typing import Annotated, Generic, List, Optional, Type, TypeVar

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel, select

from app.core.database import get_db_session

T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T]):
    def __init__(
        self, session: Annotated[AsyncSession, Depends(get_db_session)]
    ):
        self.session = session

    async def create_multiple(self, instances: List[T]) -> List[T]:
        """通用的批量新增多個實例到資料庫的方法"""
        self.session.add_all(instances)
        await self.session.commit()
        return instances

    async def create_instance(self, instance: T) -> T:
        """通用的單一新增實例到資料庫的方法"""
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get_by_id(self, id: int, model: Type[T]) -> Optional[T]:
        """根據 ID 獲取實例的方法"""
        result = await self.session.get(model, id)
        return result

    async def get_all(self, model: Type[T]) -> List[T]:
        """取得所有實例資料的方法"""
        statement = select(model)
        results = await self.session.execute(statement)
        return results.scalars().all()

    async def update_instance(
        self, id: int, new_data: dict, model: Type[T]
    ) -> T:
        """更新實例的方法"""
        instance = await self.get_by_id(id, model)
        if not instance:
            raise HTTPException(
                status_code=404,
                detail=f"找不到 ID 為 {id} 的 {model.__name__} 資料",
            )

        for key, value in new_data.items():
            setattr(instance, key, value)

        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def patch_instance(
        self, id: int, new_data: dict, model: Type[T]
    ) -> T:
        """部分更新實例的方法"""
        instance = await self.get_by_id(id, model)
        if not instance:
            raise HTTPException(
                status_code=404,
                detail=f"找不到 ID 為 {id} 的 {model.__name__} 資料",
            )

        for key, value in new_data.items():
            if value is not None:
                setattr(instance, key, value)

        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def delete_instance(self, id: int, model: Type[T]) -> T:
        """刪除實例的方法"""
        instance = await self.get_by_id(id, model)
        if not instance:
            raise HTTPException(
                status_code=404,
                detail=f"找不到 ID 為 {id} 的 {model.__name__} 資料",
            )

        await self.session.delete(instance)
        await self.session.commit()
        return instance

    async def check_exists(
        self, field_name: str, value: str, model: Type[T]
    ) -> bool:
        """通用的檢查某個欄位值是否已存在的方法"""
        statement = select(model).where(getattr(model, field_name) == value)
        result = await self.session.execute(statement)
        return result.scalars().first() is not None
