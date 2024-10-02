import logging
from typing import List
from fastapi import APIRouter, Depends

from app.domain.models.unit import Unit
from app.application.schema.unit import UnitCreate
from app.infrastructure.repositories.unit import UnitRepository

router = APIRouter()


@router.get("/", response_model=List[Unit])
async def read_units(
    repository: UnitRepository = Depends(),
):
    logging.info("取得 Unit 資料")
    return await repository.get_all_units()


@router.post("/", response_model=Unit)
async def create_unit(
    new_unit: UnitCreate,
    repository: UnitRepository = Depends(),
):
    logging.info("新增 Unit 資料到資料庫")
    return await repository.create_unit(new_unit)
