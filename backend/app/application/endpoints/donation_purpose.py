from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.domain.models.donation_purpose import DonationPurpose
from app.application.schema.donation_purpose import DonationPurposeCreate
from app.infrastructure.repositories.donation_purpose import DonationPurposeRepository

router = APIRouter()


@router.get("/", response_model=List[DonationPurpose])
async def read_donation_purposes(db: AsyncSession = Depends(get_db)):
    donation_purpose_repo = DonationPurposeRepository(db)
    donation_purposes = await donation_purpose_repo.get_all_donation_purposes()
    return donation_purposes


@router.post("/", response_model=DonationPurpose)
async def create_donation_purpose(new_donation_purpose: DonationPurposeCreate, db: AsyncSession = Depends(get_db)):
    donation_purpose_repo = DonationPurposeRepository(db)
    created_donation_purpose = await donation_purpose_repo.create_donation_purpose(new_donation_purpose)
    return created_donation_purpose
