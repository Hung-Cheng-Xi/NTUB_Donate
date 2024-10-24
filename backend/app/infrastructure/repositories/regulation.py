from sqlalchemy import func
from sqlmodel import or_, select
from app.application.admin.schemas.donation_purpose import (
    DonationPurposeUpdate,
)
from app.application.admin.schemas.regulation import (
    PaginatedRegulationInfoResponse,
    RegulationCreate,
)
from app.domain.models.regulation import Regulation
from app.infrastructure.repositories.base import BaseRepository


class RegulationRepository(BaseRepository[Regulation]):
    async def create_regulation(
        self,
        regulation_create: RegulationCreate,
    ) -> Regulation:
        """新增一筆相關法規"""
        regulation = Regulation(**regulation_create.model_dump())
        return await self.create_instance(regulation)

    async def get_regulation(
        self,
        regulation_id: int,
    ) -> Regulation:
        """根據相關法規 ID 取得相關法規"""
        return await self.get_by_id(regulation_id, Regulation)

    async def get_regulations(
        self,
        skip: int,
        limit: int,
        search: str = None,
    ) -> PaginatedRegulationInfoResponse:
        """取得分頁的相關法規"""
        statement = self._build_regulation_query(skip, limit, search)
        announcements = await self._execute_regulation_query(statement)
        total_count = await self._get_regulation_total_count(search)

        return PaginatedRegulationInfoResponse(
            total_count=total_count,
            items=announcements
        )

    def _build_regulation_query(self, skip: int, limit: int, search: str = None):
        """建構查詢 Regulation 的 statement"""
        statement = select(Regulation).offset(skip).limit(limit)

        if search:
            statement = statement.where(
                or_(
                    Regulation.title.ilike(f"%{search}%"),
                )
            )

        return statement

    async def _execute_regulation_query(self, statement):
        """執行查詢 Regulation 的 statement"""
        results = await self.session.execute(statement)
        return results.scalars().all()

    async def _get_regulation_total_count(self, search: str = None):
        """查詢相關法規的總筆數"""
        total_count_stmt = select(func.count(Regulation.id))
        if search:
            total_count_stmt = total_count_stmt.where(
                or_(
                    Regulation.title.ilike(f"%{search}%"),
                )
            )

        return (await self.session.execute(total_count_stmt)).scalar()

    async def update_regulation(
        self,
        regulation_id: int,
        updated_regulation: DonationPurposeUpdate,
    ) -> DonationPurposeUpdate:
        """更新一筆相關法規"""
        regulation = updated_regulation.model_dump()
        return await self.update_instance(
            regulation_id, regulation, Regulation
        )

    async def delete_regulation(self, regulation_id: int) -> bool:
        """刪除一筆相關法規"""
        return await self.delete_instance(regulation_id, Regulation)
