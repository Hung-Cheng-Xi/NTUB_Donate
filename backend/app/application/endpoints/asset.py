from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.infrastructure.repositories.asset import assetRepository
from app.domain.models.asset import asset

router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)


@router.get("/", response_model=List[asset])
async def read_assets(db: AsyncSession = Depends(get_db)):
    asset_repo = assetRepository(db)
    assets = await asset_repo.get_all_assets()
    return assets


@router.post("/", response_model=asset)
async def create_asset(new_asset: asset, db: AsyncSession = Depends(get_db)):
    asset_repo = assetRepository(db)
    created_asset = await asset_repo.create_asset(new_asset)
    return created_asset
