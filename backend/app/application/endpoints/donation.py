import logging
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.donation import Donations
from app.application.schema.donation import DonationsCreate
from app.infrastructure.repositories.donation import DonationRepository

router = APIRouter()


@router.get("/", response_model=List[Donations])
async def read_donations(db: AsyncSession = Depends(get_db_session)):
    donation_repo = DonationRepository(db)
    donations = await donation_repo.get_all_donations()
    logging.info("取得 Donation 資料")
    return donations


@router.post("/", response_model=Donations)
async def create_donation(new_donation: DonationsCreate, db: AsyncSession = Depends(get_db_session)):
    donation_repo = DonationRepository(db)
    created_donation = await donation_repo.create_donation(new_donation)
    logging.info("新增 Donation 資料到資料庫")
    return created_donation
