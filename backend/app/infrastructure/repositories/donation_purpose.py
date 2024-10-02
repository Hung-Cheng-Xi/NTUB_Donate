from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.donation_purpose import DonationPurpose
from app.application.schema.donation_purpose import DonationPurposeCreate

from app.infrastructure.repositories.base import BaseRepository


class DonationPurposeRepository(BaseRepository[DonationPurpose]):
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        super().__init__(session)

    async def create_donation_purpose(self, donation_purpose_create: DonationPurposeCreate) -> DonationPurpose:
        """新增一筆捐款目的"""
        purpose = DonationPurpose(**donation_purpose_create.model_dump())
        return await self.create_instance(purpose)

    async def get_donation_purpose_by_id(self, donation_purpose_id: int) -> DonationPurpose:
        """根據捐款目的 ID 取得捐款目的"""
        return await self.get_by_id(donation_purpose_id, DonationPurpose)

    async def get_all_donation_purposes(self) -> list[DonationPurpose]:
        """取得所有捐款目的"""
        return await self.get_all(DonationPurpose)

    async def update_donation_purpose(self, donation_purpose_id: int, updated_donation_purpose: DonationPurpose) -> DonationPurpose:
        """更新一筆捐款目的"""
        purpose = updated_donation_purpose.model_dump()
        return await self.update_instance(donation_purpose_id, purpose, DonationPurpose)

    async def patch_donation_purpose(self, donation_purpose_id: int, updated_donation_purpose: DonationPurpose) -> DonationPurpose:
        """部分更新一筆捐款目的"""
        purpose = updated_donation_purpose.model_dump()
        return await self.patch_instance(donation_purpose_id, purpose, DonationPurpose)

    async def delete_donation_purpose(self, donation_purpose_id: int) -> bool:
        """刪除一筆捐款目的"""
        return await self.delete_instance(donation_purpose_id, DonationPurpose)
