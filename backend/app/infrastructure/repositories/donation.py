from sqlalchemy import String, func
from sqlalchemy.orm import selectinload
from sqlmodel import cast, or_, select

from app.application.admin.schemas.donation import (
    DonationUpdate,
    DonationInfo as AdminDonationInfo,
    PaginatedDonationInfoResponse as AdminPaginatedDonationInfoResponse,
)
from app.application.client.schemas.donation import (
    DonationsCreate,
    DonationInfo as ClientDonationInfo,
    PaginatedDonationInfoResponse as ClientPaginatedDonationInfoResponse,
)

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
        search,
    ) -> AdminPaginatedDonationInfoResponse:
        """取得捐款分頁資料"""
        statement = self._build_donation_query(skip, limit, search)
        donations = await self._execute_donation_query(statement)
        total_count = await self._get_total_count(search)


        return AdminPaginatedDonationInfoResponse(
            total_count=total_count,
            items=[AdminDonationInfo.model_validate(donation) for donation in donations],
        )

    def _build_donation_query(self, skip: int, limit: int, search: str = None):
        """建構查詢 Donation 的 statement"""
        statement = select(Donation).offset(skip).limit(limit)

        if search:
            statement = statement.where(
                or_(
                    Donation.username.ilike(f"%{search}%"),
                    Donation.phone_number.ilike(f"%{search}%"),
                    Donation.email.ilike(f"%{search}%"),
                    Donation.account.ilike(f"%{search}%"),
                    Donation.transaction_id.ilike(f"%{search}%"),
                    cast(Donation.input_date, String).ilike(f"%{search}%")
                )
            )

        return statement

    async def _execute_donation_query(self, statement):
        """執行查詢 Donation 的 statement"""
        results = await self.session.execute(statement)
        return results.scalars().all()

    async def _get_total_count(self, search: str = None):
        """查詢總筆數"""
        total_count_stmt = select(func.count(Donation.id))

        if search:
            total_count_stmt = total_count_stmt.where(
                or_(
                    Donation.username.ilike(f"%{search}%"),
                    Donation.phone_number.ilike(f"%{search}%"),
                    Donation.email.ilike(f"%{search}%"),
                    Donation.account.ilike(f"%{search}%"),
                    Donation.transaction_id.ilike(f"%{search}%"),
                    cast(Donation.input_date, String).ilike(f"%{search}%")
                )
            )

        return (await self.session.execute(total_count_stmt)).scalar()

    async def client_get_donations(
        self,
        skip,
        limit,
    ) -> ClientPaginatedDonationInfoResponse:
        """取得所有捐款分頁資料，包含捐款目的的詳細信息"""
        statement = (
            select(Donation)
            .offset(skip)
            .limit(limit)
            .options(selectinload(Donation.purpose))
        )
        results = await self.session.execute(statement)
        donations = results.scalars().all()

        # 查詢總筆數
        total_count_stmt = select((func.count(DonationPurpose.id)))
        total_count = (await self.session.execute(total_count_stmt)).scalar()


        # 將結果轉換為 ClientDonationInfo 格式
        items = [
            ClientDonationInfo.model_validate(donation)
            for donation in donations
            if donation.input_date is not None
        ]

        return ClientPaginatedDonationInfoResponse(
            total_count=total_count,
            items=items
        )

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
