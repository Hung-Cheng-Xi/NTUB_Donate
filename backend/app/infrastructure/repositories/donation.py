from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.donation import Donations
from app.application.client.schemas.donation import DonationsCreate

from app.infrastructure.repositories.base import BaseRepository


class DonationRepository(BaseRepository[Donations]):
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db_session)]):
        super().__init__(session)

    async def create_donation(
        self,
        donation_create: DonationsCreate
    ) -> Donations:
        """新增一筆捐款"""
        donation = Donations(**donation_create.model_dump())
        return await self.create_instance(donation)

    async def get_donation_by_id(self, donation_id: int) -> Donations:
        """根據捐款 ID 取得捐款"""
        return await self.get_by_id(donation_id, Donations)

    async def get_all_donations(self) -> list[Donations]:
        """取得所有捐款"""
        return await self.get_all(Donations)

    async def update_donation(
        self,
        donation_id,
        updated_donation: Donations
    ) -> Donations:
        """更新一筆捐款"""
        donation = updated_donation.model_dump()
        return await self.update_instance(donation_id, donation, Donations)

    async def patch_donation(
        self,
        donation_id,
        updated_donation: Donations
    ) -> Donations:
        """部分更新一筆捐款"""
        donation = updated_donation.model_dump()
        return await self.patch_instance(donation_id, donation, Donations)

    async def delete_donation(self, donation_id: int) -> bool:
        """刪除一筆捐款"""
        return await self.delete_instance(donation_id, Donations)
