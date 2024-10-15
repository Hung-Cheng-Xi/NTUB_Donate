import logging
from typing import Annotated, List

from app.application.admin.schemas.donation import (DonationInfo,
                                                    DonationsCreate)
from app.domain.models.donation import Donations
from app.infrastructure.repositories.donation import DonationRepository
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/", response_model=List[Donations])
async def get_donations(
    repository: Annotated[DonationRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> List[DonationInfo]:
    logging.info("取得分頁的 Donation 資料")
    return await repository.admin_get_donations(skip, limit)


@router.post("/", response_model=Donations)
async def create_donation(
    new_donation: DonationsCreate,
    repository: Annotated[DonationRepository, Depends()]
):
    logging.info("新增 Donation 資料到資料庫")
    return await repository.create_donation(new_donation)


@router.get("/{donation_id}", response_model=Donations)
async def get_donation(
    donation_id: int,
    repository: Annotated[DonationRepository, Depends()]
):
    logging.info("取得 Donation 資料")
    return await repository.get_donation_by_id(donation_id)


@router.put("/{donation_id}", response_model=Donations)
async def update_donation(
    donation_id: int,
    new_donation: DonationsCreate,
    repository: Annotated[DonationRepository, Depends()]
):
    logging.info("更新 Donation 資料")
    return await repository.update_donation(donation_id, new_donation)


@router.patch("/{donation_id}", response_model=Donations)
async def patch_donation(
    donation_id: int,
    new_donation: DonationsCreate,
    repository: Annotated[DonationRepository, Depends()]
):
    logging.info("部分更新 Donation 資料")
    return await repository.patch_donation(donation_id, new_donation)


@router.delete("/{donation_id}", response_model=Donations)
async def delete_donation(
    donation_id: int,
    repository: Annotated[DonationRepository, Depends()]
):
    logging.info("刪除 Donation 資料")
    return await repository.delete_donation(donation_id)
