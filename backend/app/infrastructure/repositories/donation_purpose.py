from sqlalchemy import func
from sqlalchemy.orm import selectinload
from sqlmodel import or_, select

from app.application.admin.schemas.donation_purpose import (
    DonationPurposeCreate,
    DonationPurposeItem as AdminDonationPurposeItem,
    PaginatedDonationPurposeInfoResponse as AdminPaginatedDonationPurposeInfoResponse,
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

    async def admin_get_donation_purposes(
        self,
        skip: int,
        limit: int,
        search: str = None,
    ) -> AdminPaginatedDonationPurposeInfoResponse:
        """取得分頁的捐款目的，按達到金額上限百分比排序"""

        statement = self._build_donation_purpose_query(skip, limit, search)
        purposes = await self._execute_donation_purpose_query(statement)
        total_count = await self._get_donation_purpose_total_count(search)

        items = [AdminDonationPurposeItem.model_dump(purpose) for purpose in purposes]

        return AdminPaginatedDonationPurposeInfoResponse(
            total_count=total_count,
            items=items,
        )

    def _build_donation_purpose_query(self, skip: int, limit: int, search: str = None):
        """建構查詢 DonationPurpose 的 statement"""
        statement = (
            select(DonationPurpose)
            .offset(skip)
            .limit(limit)
            .options(selectinload(DonationPurpose.donations))
        )

        if search:
            statement = statement.where(
                or_(
                    DonationPurpose.title.ilike(f"%{search}%"),
                    DonationPurpose.description.ilike(f"%{search}%"),
                )
            )

        return statement

    async def _execute_donation_purpose_query(self, statement):
        """執行查詢 DonationPurpose 的 statement"""
        results = await self.session.execute(statement)
        return results.scalars().all()

    async def _get_donation_purpose_total_count(self, search: str = None):
        """查詢捐款目的的總筆數"""
        total_count_stmt = select(func.count(DonationPurpose.id))
        if search:
            total_count_stmt = total_count_stmt.where(
                or_(
                    DonationPurpose.title.ilike(f"%{search}%"),
                    DonationPurpose.description.ilike(f"%{search}%"),
                )
            )

        return (await self.session.execute(total_count_stmt)).scalar()


    async def client_get_donation_purposes(
        self,
        skip: int,
        limit: int,
    ) -> {DonationPurpose, int}:
        """取得分頁的捐款目的，按達到金額上限百分比排序"""

        statement = (
            select(DonationPurpose)
            .offset(skip)
            .limit(limit)
            .options(selectinload(DonationPurpose.donations))
        )
        results = await self.session.execute(statement)

        purposes = results.scalars().all()

        # 查詢總筆數
        total_count_stmt = select((func.count(DonationPurpose.id)))
        total_count = (await self.session.execute(total_count_stmt)).scalar()

        return purposes, total_count
