from sqlalchemy import func
from sqlmodel import select
from app.application.admin.schemas.donation_purpose import (
    DonationPurposeUpdate,
)
from app.application.admin.schemas.regulation import (
    PaginatedRegulationInfoResponse,
    RegulationCreate,
    RegulationInfo,
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
    ) -> PaginatedRegulationInfoResponse:
        """取得分頁的相關法規"""
        statement = select(Regulation).offset(skip).limit(limit)
        results = await self.session.execute(statement)
        regulations =  results.scalars().all()

        # 查詢總筆數
        total_count_stmt = select((func.count(Regulation.id)))
        total_count = (await self.session.execute(total_count_stmt)).scalar()

        items = [
            RegulationInfo.model_dump(regulation) for regulation in regulations
        ]

        return PaginatedRegulationInfoResponse(
            total_count=total_count,
            items=items
        )

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
