import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.client.schemas.donation_purpose import PaginatedDonationPurposeInfoResponse
from app.domain.models.donation_purpose import DonationPurpose
from app.domain.services.donation_purpose import DonationPurposeService
from app.infrastructure.repositories.donation_purpose import (
    DonationPurposeRepository,
)

router = APIRouter()


@router.get("/", response_model=PaginatedDonationPurposeInfoResponse)
async def client_get_donation_purposes(
    service: Annotated[DonationPurposeService, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> PaginatedDonationPurposeInfoResponse:
    logging.info("取得分頁的 Donation Purpose 資料")
    return await service.get_sorted_donation_purpose(skip, limit)


@router.get("/{donation_purpose_id}", response_model=DonationPurpose)
async def client_get_donation_purpose(
    donation_purpose_id: int,
    repository: Annotated[DonationPurposeRepository, Depends()],
):
    logging.info("取得 Donation Purpose 資料")
    return await repository.get_donation_purpose(donation_purpose_id)
