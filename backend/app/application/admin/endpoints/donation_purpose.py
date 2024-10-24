import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.admin.schemas.donation_purpose import (
    PaginatedDonationPurposeInfoResponse,
    DonationPurposeCreate,
    DonationPurposeUpdate,
)
from app.domain.models.donation_purpose import DonationPurpose
from app.infrastructure.repositories.donation_purpose import (
    DonationPurposeRepository,
)

router = APIRouter()


@router.get("/", response_model=PaginatedDonationPurposeInfoResponse)
async def admin_get_donation_purposes(
    repository: Annotated[DonationPurposeRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
    search: str = None,
) -> PaginatedDonationPurposeInfoResponse:
    logging.info("取得分頁的 Donation Purpose 資料")
    return await repository.admin_get_donation_purposes(skip, limit, search)


@router.post("/", response_model=DonationPurpose)
async def admin_create_donation_purpose(
    new_donation_purpose: DonationPurposeCreate,
    repository: Annotated[DonationPurposeRepository, Depends()],
):
    logging.info("新增 Donation Purpose 資料到資料庫")
    return await repository.create_donation_purpose(new_donation_purpose)


@router.get("/{donation_purpose_id}", response_model=DonationPurpose)
async def admin_get_donation_purpose(
    donation_purpose_id: int,
    repository: Annotated[DonationPurposeRepository, Depends()],
):
    logging.info("取得 Donation Purpose 資料")
    return await repository.get_donation_purpose(donation_purpose_id)


@router.put("/{donation_purpose_id}", response_model=DonationPurpose)
async def admin_update_donation_purpose(
    donation_purpose_id: int,
    new_donation_purpose: DonationPurposeUpdate,
    repository: Annotated[DonationPurposeRepository, Depends()],
):
    logging.info("更新 Donation Purpose 資料")
    return await repository.update_donation_purpose(
        donation_purpose_id, new_donation_purpose
    )


@router.delete("/{donation_purpose_id}", response_model=DonationPurpose)
async def admin_delete_donation_purpose(
    donation_purpose_id: int,
    repository: Annotated[DonationPurposeRepository, Depends()],
):
    logging.info("刪除 Donation Purpose 資料")
    return await repository.delete_donation_purpose(donation_purpose_id)
