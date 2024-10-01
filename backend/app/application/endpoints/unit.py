import logging
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.unit import Unit
from app.application.schema.unit import UnitCreate
from app.infrastructure.repositories.unit import UnitRepository

router = APIRouter()


@router.get("/", response_model=List[Unit])
async def read_units(db: AsyncSession = Depends(get_db_session)):
    donation_purpose_repo = UnitRepository(db)
    units = await donation_purpose_repo.get_all_units()
    logging.info("取得 Unit 資料")
    return units


@router.post("/", response_model=Unit)
async def create_unit(new_unit: UnitCreate, db: AsyncSession = Depends(get_db_session)):
    unit_repo = UnitRepository(db)
    created_unit = await unit_repo.create_unit(new_unit)
    logging.info("新增 Unit 資料到資料庫")
    return created_unit
