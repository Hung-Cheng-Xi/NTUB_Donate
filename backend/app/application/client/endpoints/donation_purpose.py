import logging
from typing import List, Annotated
from fastapi import APIRouter, Depends

from app.domain.models.donation_purpose import DonationPurpose
from app.infrastructure.repositories.donation_purpose import (
    DonationPurposeRepository
)

router = APIRouter()


@router.get("/", response_model=List[DonationPurpose])
async def get_donation_purposes(
    repository: Annotated[DonationPurposeRepository, Depends()]
):
    logging.info("取得 Donation Purpose 資料")
    return await repository.get_all_donation_purposes()


@router.get("/{donation_purpose_id}", response_model=DonationPurpose)
async def get_donation_purpose(
    donation_purpose_id: int,
    repository: Annotated[DonationPurposeRepository, Depends()]
):
    logging.info("取得 Donation Purpose 資料")
    return await repository.get_donation_purpose_by_id(donation_purpose_id)
