from typing import Any

from app.application.admin.schemas.donation_purpose import (
    DonationPurposeCreate, DonationPurposeItem)
from app.domain.models.donation_purpose import DonationPurpose
from app.infrastructure.repositories.base import BaseRepository
from sqlalchemy.orm import selectinload
from sqlmodel import select


class DonationPurposeRepository(BaseRepository[DonationPurpose]):
    async def create_donation_purpose(
        self,
        donation_purpose_create: DonationPurposeCreate
    ) -> DonationPurpose:
        """新增一筆捐款目的"""
        purpose = DonationPurpose(**donation_purpose_create.model_dump())
        return await self.create_instance(purpose)

    async def get_donation_purpose(
        self,
        donation_purpose_id: int
    ) -> DonationPurpose:
        """根據捐款目的 ID 取得捐款目的"""
        return await self.get_by_id(donation_purpose_id, DonationPurpose)

    async def update_donation_purpose(
        self, donation_purpose_id: int,
        updated_donation_purpose: DonationPurpose
    ) -> DonationPurpose:
        """更新一筆捐款目的"""
        purpose = updated_donation_purpose.model_dump()
        return await self.update_instance(
            donation_purpose_id,
            purpose,
            DonationPurpose
        )

    async def patch_donation_purpose(
        self, donation_purpose_id: int,
        updated_donation_purpose: DonationPurpose
    ) -> DonationPurpose:
        """部分更新一筆捐款目的"""
        purpose = updated_donation_purpose.model_dump()
        return await self.patch_instance(
            donation_purpose_id,
            purpose, DonationPurpose
        )

    async def delete_donation_purpose(self, donation_purpose_id: int) -> bool:
        """刪除一筆捐款目的"""
        return await self.delete_instance(donation_purpose_id, DonationPurpose)

    async def get_donation_purposes(
        self,
        skip: int,
        limit: int
    ) -> list[DonationPurposeItem]:
        """取得分頁的捐款目的，按達到金額上限百分比排序"""
        statement = select(DonationPurpose).options(
            selectinload(DonationPurpose.donations))
        results = await self.session.execute(statement)
        purposes = results.scalars().all()

        donation_purposes = []
        for purpose in purposes:
            total_donation: Any = sum(
                donation.amount for donation in purpose.donations)
            achieved_percentage: Any = (
                total_donation / purpose.lump_sum
                if purpose.lump_sum > 0 else 0
            )

            purpose_dict = purpose.model_dump()
            purpose_dict.update({
                'total_donation': total_donation,
                'achieved_percentage': achieved_percentage
            })
            donation_purposes.append(DonationPurposeItem(**purpose_dict))

        sorted_donation_purposes = sorted(
            donation_purposes,
            key=lambda purpose: purpose.achieved_percentage,
            reverse=True
        )

        return sorted_donation_purposes[skip:skip + limit]
