from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.domain.models.donation import Donation
from app.application.schema.donation import DonationCreate

from app.infrastructure.repositories.base import BaseRepository


class DonationRepository(BaseRepository[Donation]):
    def __init__(self, session: AsyncSession = Depends(get_db)):
        super().__init__(session)

    async def create_donation(self, donation_create: DonationCreate) -> Donation:
        """新增一筆捐款"""
        donation = Donation(**donation_create.model_dump())
        return await self.create_instance(donation)

    async def get_donation_by_id(self, donation_id: int) -> Donation:
        """根據捐款 ID 取得捐款"""
        return await self.get_by_id(donation_id, Donation)

    async def get_all_donations(self) -> list[Donation]:
        """取得所有捐款"""
        return await self.get_all(Donation)

    async def update_donation(self, donation_id, updated_donation: Donation) -> Donation:
        """更新一筆捐款"""
        donation = updated_donation.model_dump()
        return await self.update_instance(donation_id, donation, Donation)

    async def delete_donation(self, donation_id: int) -> bool:
        """刪除一筆捐款"""
        return await self.delete_instance(donation_id, Donation)
