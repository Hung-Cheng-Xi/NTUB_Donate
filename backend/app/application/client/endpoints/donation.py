import logging
from typing import List, Annotated
from fastapi import APIRouter, Depends

from app.domain.models.donation import Donations
from app.application.client.schemas.donation import DonationsCreate
from app.infrastructure.repositories.donation import DonationRepository
from app.application.client.schemas.donation import DonationInfo

router = APIRouter()


@router.get("/", response_model=List[DonationInfo])
async def get_donations(
    repository: Annotated[DonationRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> List[DonationInfo]:
    logging.info("取得 Donation 資料")
    return await repository.client_get_donations(skip, limit)


@router.post("/", response_model=Donations)
async def create_donation(
    new_donation: DonationsCreate,
    repository: Annotated[DonationRepository, Depends()]
):
    logging.info("新增 Donation 資料到資料庫")
    return await repository.create_donation(new_donation)
