from typing import Annotated, Any
from fastapi import Depends
from sqlmodel import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.donation_purpose import DonationPurpose
from app.infrastructure.repositories.base import BaseRepository
from app.application.admin.schemas.donation_purpose import (
    DonationPurposeCreate,
    DonationPurposeItem,
)


class DonationPurposeRepository(BaseRepository[DonationPurpose]):
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db_session)]):
        super().__init__(session)

    async def create_donation_purpose(
        self,
        donation_purpose_create: DonationPurposeCreate
    ) -> DonationPurpose:
        """新增一筆捐款目的"""
        purpose = DonationPurpose(**donation_purpose_create.model_dump())
        return await self.create_instance(purpose)

    async def get_donation_purpose_by_id(
        self,
        donation_purpose_id: int
    ) -> DonationPurpose:
        """根據捐款目的 ID 取得捐款目的"""
        return await self.get_by_id(donation_purpose_id, DonationPurpose)

    async def get_all_donation_purposes(self) -> list[DonationPurpose]:
        """取得所有捐款目的"""
        return await self.get_all(DonationPurpose)

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

    async def get_donation_purpose_items(
        self,
        skip: int,
        limit: int
    ) -> list[DonationPurposeItem]:
        """取得分頁的捐款目的，按達到金額上限百分比排序"""
        # 取得 DonationPurpose 並預加載捐款以避免 N+1 問題
        statement = select(DonationPurpose).options(
            selectinload(DonationPurpose.donations))
        results = await self.session.execute(statement)
        purposes = results.scalars().all()

        # 計算每個捐款目的的達成百分比，並存放在暫時屬性中
        response_list = []
        for purpose in purposes:
            total_donation: Any = sum(
                donation.amount for donation in purpose.donations)
            achieved_percentage: Any = (
                total_donation / purpose.lump_sum) if purpose.lump_sum > 0 else 0

            # 使用 model_dump 將 purpose 轉換為字典，然後添加 total_donation
            purpose_dict = purpose.model_dump()
            purpose_dict['total_donation'] = total_donation
            purpose_dict['achieved_percentage'] = achieved_percentage
            response_list.append(DonationPurposeItem(**purpose_dict))

        # 按達成百分比排序
        sorted_purposes = sorted(
            response_list, key=lambda p: p.achieved_percentage, reverse=True)

        # 返回分頁結果
        return sorted_purposes[skip:skip + limit]
