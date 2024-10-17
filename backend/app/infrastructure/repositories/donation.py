from sqlalchemy.orm import joinedload, selectinload
from sqlmodel import select

from app.application.admin.schemas.donation import (
    DonationInfo as DonationInfoAdmin,
)
from app.application.admin.schemas.donation import DonationUpdate
from app.application.client.schemas.donation import (
    DonationInfo as DonationInfoClient,
)
from app.application.client.schemas.donation import DonationsCreate
from app.domain.models.donation import Donation
from app.domain.models.donation_purpose import DonationPurpose
from app.infrastructure.repositories.base import BaseRepository


class DonationRepository(BaseRepository[Donation]):
    async def create_donation(
        self,
        donation_create: DonationsCreate,
    ) -> Donation:
        """新增一筆捐款"""
        donation = Donation(**donation_create.model_dump())
        return await self.create_instance(donation)

    async def get_donation_by_id(
        self,
        donation_id: int,
    ) -> Donation:
        """根據捐款 ID 取得捐款"""
        return await self.get_by_id(donation_id, Donation)

    async def admin_get_donations(
        self,
        skip,
        limit,
    ) -> list[DonationInfoAdmin]:
        """取得所有捐款分頁資料"""
        donations = await self.get_paginated_all(Donation, skip, limit)
        return [
            DonationInfoAdmin.model_dump(donation) for donation in donations
        ]

    async def client_get_donations(
        self,
        skip,
        limit,
    ) -> list[DonationInfoClient]:
        """取得所有捐款分頁資料，包含捐款目的的詳細信息"""
        donations = await self.model_relations(
            Donation, skip, limit, [joinedload(Donation.purpose)]
        )

        # 將結果轉換為 DonationInfoClient 格式
        donation_info_list = [
            DonationInfoClient.model_validate(donation)
            for donation in donations
            if donation.input_date is not None
        ]

        return donation_info_list

    async def update_donation(
        self,
        donation_id,
        updated_donation: DonationUpdate,
    ) -> DonationUpdate:
        """更新一筆捐款"""
        donation = updated_donation.model_dump()
        return await self.update_instance(donation_id, donation, Donation)

    async def delete_donation(
        self,
        donation_id: int,
    ) -> bool:
        """刪除一筆捐款"""
        return await self.delete_instance(donation_id, Donation)

    async def export_excel(
        self,
        skip: int,
        limit: int,
    ):
        """從資料庫中獲取捐款記錄、捐款目的及受捐單位資料"""
        statement = (
            select(Donation)
            .offset(skip)
            .limit(limit)
            .options(
                selectinload(Donation.purpose).selectinload(
                    DonationPurpose.unit
                )
            )
        )

        results = await self.session.execute(statement)
        return results.scalars().all()
