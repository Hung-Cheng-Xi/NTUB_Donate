from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.domain.models.donation import Donation
from app.application.schema.donation import DonationCreate
from app.infrastructure.repositories.donation import DonationRepository

router = APIRouter()


@router.get("/", response_model=List[Donation])
async def read_donations(db: AsyncSession = Depends(get_db)):
    donation_repo = DonationRepository(db)
    donations = await donation_repo.get_all_donations()
    return donations


@router.post("/", response_model=Donation)
async def create_donation(new_donation: DonationCreate, db: AsyncSession = Depends(get_db)):
    donation_repo = DonationRepository(db)
    created_donation = await donation_repo.create_donation(new_donation)
    return created_donation
