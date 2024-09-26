from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.domain.models.unit import Unit
from app.application.schema.unit import UnitCreate
from app.infrastructure.repositories.unit import UnitRepository

router = APIRouter()


@router.get("/", response_model=List[Unit])
async def read_units(db: AsyncSession = Depends(get_db)):
    donation_purpose_repo = UnitRepository(db)
    units = await donation_purpose_repo.get_all_units()
    return units


@router.post("/", response_model=Unit)
async def create_unit(new_unit: UnitCreate, db: AsyncSession = Depends(get_db)):
    unit_repo = UnitRepository(db)
    created_unit = await unit_repo.create_unit(new_unit)
    return created_unit
