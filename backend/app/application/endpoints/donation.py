import logging
from typing import List
from fastapi import APIRouter, Depends

from app.domain.models.donation import Donations
from app.application.schema.donation import DonationsCreate
from app.infrastructure.repositories.donation import DonationRepository

router = APIRouter()


@router.get("/", response_model=List[Donations])
async def get_donations(
    repository: DonationRepository = Depends(),
):
    logging.info("取得 Donation 資料")
    return await repository.get_all_donations()


@router.post("/", response_model=Donations)
async def create_donation(
    new_donation: DonationsCreate,
    repository: DonationRepository = Depends(),
):
    logging.info("新增 Donation 資料到資料庫")
    return await repository.create_donation(new_donation)


@router.get("/{donation_id}", response_model=Donations)
async def get_donation(
    donation_id: int,
    repository: DonationRepository = Depends(),
):
    logging.info("取得 Donation 資料")
    return await repository.get_donation_by_id(donation_id)


@router.put("/{donation_id}", response_model=Donations)
async def update_donation(
    donation_id: int,
    new_donation: DonationsCreate,
    repository: DonationRepository = Depends(),
):
    logging.info("更新 Donation 資料")
    return await repository.update_donation(donation_id, new_donation)


@router.patch("/{donation_id}", response_model=Donations)
async def patch_donation(
    donation_id: int,
    new_donation: DonationsCreate,
    repository: DonationRepository = Depends(),
):
    logging.info("部分更新 Donation 資料")
    return await repository.patch_donation(donation_id, new_donation)


@router.delete("/{donation_id}", response_model=Donations)
async def delete_donation(
    donation_id: int,
    repository: DonationRepository = Depends(),
):
    logging.info("刪除 Donation 資料")
    return await repository.delete_donation(donation_id)
