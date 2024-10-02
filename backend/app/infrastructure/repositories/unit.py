from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.unit import Unit
from app.application.schema.unit import UnitCreate

from app.infrastructure.repositories.base import BaseRepository


class UnitRepository(BaseRepository[Unit]):
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        super().__init__(session)

    async def create_unit(self, unit_create: UnitCreate) -> Unit:
        """新增一筆單位"""
        unit = Unit(**unit_create.model_dump())
        return await self.create_instance(unit)

    async def get_unit_by_id(self, unit_id: int) -> Unit:
        """根據單位 ID 取得單位"""
        return await self.get_by_id(unit_id, Unit)

    async def get_all_units(self) -> list[Unit]:
        """取得所有單位"""
        return await self.get_all(Unit)

    async def update_unit(self, unit_id: int, updated_unit: Unit) -> Unit:
        """更新一筆單位"""
        unit = updated_unit.model_dump()
        return await self.update_instance(unit_id, unit, Unit)

    async def patch_unit(self, unit_id: int, updated_unit: Unit) -> Unit:
        """部分更新一筆單位"""
        unit = updated_unit.model_dump()
        return await self.patch_instance(unit_id, unit, Unit)

    async def delete_unit(self, unit_id: int) -> bool:
        """刪除一筆單位"""
        return await self.delete_instance(unit_id, Unit)
