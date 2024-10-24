import logging
from typing import Annotated, List

from fastapi import APIRouter, Depends

from app.application.admin.schemas.unit import UnitCreate, UnitUpdate
from app.domain.models.unit import Unit
from app.infrastructure.repositories.unit import UnitRepository

router = APIRouter()


@router.get("/", response_model=List[Unit])
async def admin_get_units(
    repository: Annotated[UnitRepository, Depends()],
):
    logging.info("取得 Unit 資料")
    return await repository.get_units()


@router.post("/", response_model=Unit)
async def admin_create_unit(
    new_unit: UnitCreate, repository: Annotated[UnitRepository, Depends()]
):
    logging.info("新增 Unit 資料到資料庫")
    return await repository.create_unit(new_unit)


@router.get("/{unit_id}", response_model=Unit)
async def admin_get_unit(
    unit_id: int, repository: Annotated[UnitRepository, Depends()]
):
    logging.info("取得 Unit 資料")
    return await repository.get_unit(unit_id)


@router.put("/{unit_id}", response_model=Unit)
async def admin_update_unit(
    unit_id: int,
    new_unit: UnitUpdate,
    repository: Annotated[UnitRepository, Depends()],
):
    logging.info("更新 Unit 資料")
    return await repository.update_unit(unit_id, new_unit)


@router.delete("/{unit_id}", response_model=Unit)
async def admin_delete_unit(
    unit_id: int, repository: Annotated[UnitRepository, Depends()]
):
    logging.info("刪除 Unit 資料")
    return await repository.delete_unit(unit_id)
