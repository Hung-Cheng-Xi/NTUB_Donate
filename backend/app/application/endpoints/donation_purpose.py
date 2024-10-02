import logging
from typing import List
from fastapi import APIRouter, Depends

from app.domain.models.donation_purpose import DonationPurpose
from app.application.schema.donation_purpose import DonationPurposeCreate
from app.infrastructure.repositories.donation_purpose import DonationPurposeRepository

router = APIRouter()


@router.get("/", response_model=List[DonationPurpose])
async def get_donation_purposes(
    repository: DonationPurposeRepository = Depends(),
):
    logging.info("取得 Donation Purpose 資料")
    return await repository.get_all_donation_purposes()


@router.post("/", response_model=DonationPurpose)
async def create_donation_purpose(
    new_donation_purpose: DonationPurposeCreate,
    repository: DonationPurposeRepository = Depends(),
):
    logging.info("新增 Donation Purpose 資料到資料庫")
    return await repository.create_donation_purpose(new_donation_purpose)
