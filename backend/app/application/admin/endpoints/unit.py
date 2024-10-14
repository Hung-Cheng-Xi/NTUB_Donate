import logging
from typing import List, Annotated
from fastapi import APIRouter, Depends

from app.domain.models.unit import Unit
from app.application.admin.schemas.unit import UnitCreate
from app.infrastructure.repositories.unit import UnitRepository

router = APIRouter()


@router.get("/", response_model=List[Unit])
async def get_units(
    repository: Annotated[UnitRepository, Depends()],
):
    logging.info("取得 Unit 資料")
    return await repository.get_all_units()


@router.post("/", response_model=Unit)
async def create_unit(
    new_unit: UnitCreate,
    repository: Annotated[UnitRepository, Depends()]
):
    logging.info("新增 Unit 資料到資料庫")
    return await repository.create_unit(new_unit)


@router.get("/{unit_id}", response_model=Unit)
async def get_unit(
    unit_id: int,
    repository: Annotated[UnitRepository, Depends()]
):
    logging.info("取得 Unit 資料")
    return await repository.get_unit_by_id(unit_id)


@router.put("/{unit_id}", response_model=Unit)
async def update_unit(
    unit_id: int,
    new_unit: UnitCreate,
    repository: Annotated[UnitRepository, Depends()]
):
    logging.info("更新 Unit 資料")
    return await repository.update_unit(unit_id, new_unit)


@router.delete("/{unit_id}", response_model=Unit)
async def delete_unit(
    unit_id: int,
    repository: Annotated[UnitRepository, Depends()]
):
    logging.info("刪除 Unit 資料")
    return await repository.delete_unit(unit_id)
