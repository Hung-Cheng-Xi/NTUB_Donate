import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.admin.schemas.donation import PaginatedDonationInfoResponse, DonationUpdate
from app.application.client.schemas.donation import DonationsCreate
from app.domain.models.donation import Donation
from app.infrastructure.repositories.donation import DonationRepository

router = APIRouter()


@router.get("/", response_model=PaginatedDonationInfoResponse)
async def admin_get_donations(
    repository: Annotated[DonationRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
    search: str = None,
) -> PaginatedDonationInfoResponse:
    logging.info("取得分頁的 Donation 資料")
    return await repository.admin_get_donations(skip, limit, search)


@router.post("/", response_model=Donation)
async def admin_create_donation(
    new_donation: DonationsCreate,
    repository: Annotated[DonationRepository, Depends()],
):
    logging.info("新增 Donation 資料到資料庫")
    return await repository.create_donation(new_donation)


@router.get("/{donation_id}", response_model=Donation)
async def admin_get_donation(
    donation_id: int, repository: Annotated[DonationRepository, Depends()]
):
    logging.info("取得 Donation 資料")
    return await repository.get_donation_by_id(donation_id)


@router.put("/{donation_id}", response_model=Donation)
async def admin_update_donation(
    donation_id: int,
    new_donation: DonationUpdate,
    repository: Annotated[DonationRepository, Depends()],
):
    logging.info("更新 Donation 資料")
    return await repository.update_donation(donation_id, new_donation)


@router.delete("/{donation_id}", response_model=Donation)
async def admin_delete_donation(
    donation_id: int, repository: Annotated[DonationRepository, Depends()]
):
    logging.info("刪除 Donation 資料")
    return await repository.delete_donation(donation_id)
