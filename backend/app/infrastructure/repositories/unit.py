from app.application.admin.schemas.unit import UnitCreate, UnitUpdate
from app.domain.models.unit import Unit
from app.infrastructure.repositories.base import BaseRepository


class UnitRepository(BaseRepository[Unit]):
    async def create_unit(
        self,
        unit_create: UnitCreate,
    ) -> Unit:
        """新增一筆單位"""
        unit = Unit(**unit_create.model_dump())
        return await self.create_instance(unit)

    async def get_unit(
        self,
        unit_id: int,
    ) -> Unit:
        """根據單位 ID 取得單位"""
        return await self.get_by_id(unit_id, Unit)

    async def get_units(self) -> list[Unit]:
        """取得所有單位"""
        return await self.get_all(Unit)

    async def update_unit(
        self,
        unit_id: int,
        updated_unit: UnitUpdate,
    ) -> UnitUpdate:
        """更新一筆單位"""
        unit = updated_unit.model_dump()
        return await self.update_instance(unit_id, unit, Unit)

    async def delete_unit(
        self,
        unit_id: int,
    ) -> bool:
        """刪除一筆單位"""
        return await self.delete_instance(unit_id, Unit)
