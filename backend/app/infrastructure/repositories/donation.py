from typing import Annotated
from fastapi import Depends
from sqlmodel import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.donation import Donations
from app.application.admin.schemas.donation import DonationInfo as DonationInfoAdmin
from app.application.client.schemas.donation import (
    DonationsCreate,
    DonationInfo as DonationInfoClient,
)

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

    async def get_donations_admin_all(self, skip, limit) -> list[DonationInfoAdmin]:
        """取得所有捐款分頁資料"""
        donations = await self.get_paginated_all(Donations, skip, limit)
        return [DonationInfoAdmin.model_dump(donation) for donation in donations]

    async def get_donations_client_all(self, skip, limit) -> list[DonationInfoClient]:
        """取得所有捐款分頁資料，包含捐款目的的詳細信息"""
        async with self.session as session:
            # 使用 select 加載 Donations，並同時載入相關的 DonationPurpose 資料
            result = await session.execute(
                select(Donations)
                .options(selectinload(Donations.purpose))
                .offset(skip)
                .limit(limit)
            )
            donations = result.scalars().all()

            # 將結果轉換為 DonationInfoClient 格式
            donation_info_list = [
                DonationInfoClient(
                    username=donation.username,
                    amount=donation.amount,
                    purpose=donation.purpose,  # 這裡會自動映射到 DonationPurpose 子模型
                    input_date=donation.input_date
                )
                for donation in donations
                if donation.input_date is not None and donation.input_date != "string"
            ]

        return donation_info_list

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
