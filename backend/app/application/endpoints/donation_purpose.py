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


@router.get("/{donation_purpose_id}", response_model=DonationPurpose)
async def get_donation_purpose(
    donation_purpose_id: int,
    repository: DonationPurposeRepository = Depends(),
):
    logging.info("取得 Donation Purpose 資料")
    return await repository.get_donation_purpose_by_id(donation_purpose_id)


@router.put("/{donation_purpose_id}", response_model=DonationPurpose)
async def update_donation_purpose(
    donation_purpose_id: int,
    new_donation_purpose: DonationPurposeCreate,
    repository: DonationPurposeRepository = Depends(),
):
    logging.info("更新 Donation Purpose 資料")
    return await repository.update_donation_purpose(donation_purpose_id, new_donation_purpose)


@router.patch("/{donation_purpose_id}", response_model=DonationPurpose)
async def patch_donation_purpose(
    donation_purpose_id: int,
    new_donation_purpose: DonationPurposeCreate,
    repository: DonationPurposeRepository = Depends(),
):
    logging.info("部分更新 Donation Purpose 資料")
    return await repository.patch_donation_purpose(donation_purpose_id, new_donation_purpose)


@router.delete("/{donation_purpose_id}", response_model=DonationPurpose)
async def delete_donation_purpose(
    donation_purpose_id: int,
    repository: DonationPurposeRepository = Depends(),
):
    logging.info("刪除 Donation Purpose 資料")
    return await repository.delete_donation_purpose(donation_purpose_id)