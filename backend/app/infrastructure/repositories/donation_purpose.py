from typing import List

from sqlalchemy.orm import selectinload
from sqlmodel import select

from app.application.admin.schemas.donation_purpose import (
    AdminDonationPurposeItem,
    DonationPurposeCreate,
)
from app.domain.models.donation_purpose import DonationPurpose
from app.infrastructure.repositories.base import BaseRepository


class DonationPurposeRepository(BaseRepository[DonationPurpose]):
    async def create_donation_purpose(
        self,
        donation_purpose_create: DonationPurposeCreate,
    ) -> DonationPurpose:
        """新增一筆捐款目的"""
        purpose = DonationPurpose(**donation_purpose_create.model_dump())
        return await self.create_instance(purpose)

    async def get_donation_purpose(
        self,
        donation_purpose_id: int,
    ) -> DonationPurpose:
        """根據捐款目的 ID 取得捐款目的"""
        return await self.get_by_id(donation_purpose_id, DonationPurpose)

    async def update_donation_purpose(
        self,
        donation_purpose_id: int,
        updated_donation_purpose: DonationPurpose,
    ) -> DonationPurpose:
        """更新一筆捐款目的"""
        purpose = updated_donation_purpose.model_dump()
        return await self.update_instance(
            donation_purpose_id, purpose, DonationPurpose
        )

    async def delete_donation_purpose(
        self,
        donation_purpose_id: int,
    ) -> bool:
        """刪除一筆捐款目的"""
        return await self.delete_instance(donation_purpose_id, DonationPurpose)

    async def get_donation_purposes(
        self,
        skip: int,
        limit: int,
    ) -> List[AdminDonationPurposeItem]:
        """取得分頁的捐款目的，按達到金額上限百分比排序"""

        statement = (
            select(DonationPurpose)
            .offset(skip)
            .limit(limit)
            .options(selectinload(DonationPurpose.donations))
        )
        results = await self.session.execute(statement)
        return results.scalars().all()
