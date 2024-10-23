import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.client.schemas.donation import (
    DonationsCreate,
    PaginatedDonationInfoResponse,
)
from app.domain.models.donation import Donation
from app.infrastructure.repositories.donation import DonationRepository

router = APIRouter()


@router.get("/", response_model=PaginatedDonationInfoResponse)
async def client_get_donations(
    repository: Annotated[DonationRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> PaginatedDonationInfoResponse:
    logging.info("取得 Donation 資料")
    return await repository.client_get_donations(skip, limit)


@router.post("/", response_model=Donation)
async def client_create_donation(
    new_donation: DonationsCreate,
    repository: Annotated[DonationRepository, Depends()],
):
    logging.info("新增 Donation 資料到資料庫")
    return await repository.create_donation(new_donation)
