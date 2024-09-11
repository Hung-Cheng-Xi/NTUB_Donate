from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.config import get_db
from app.infrastructure.repositories.asset import AssetRepository
from app.domain.models.asset import Asset

router = APIRouter()


@router.get("/assets", response_model=List[Asset])
async def read_assets(db: Session = Depends(get_db)):
    asset_repo = AssetRepository(db)
    return asset_repo.get_all_assets()


@router.post("/assets", response_model=Asset)
async def create_asset(asset: Asset, db: Session = Depends(get_db)):
    asset_repo = AssetRepository(db)
    return asset_repo.create_asset(asset)
