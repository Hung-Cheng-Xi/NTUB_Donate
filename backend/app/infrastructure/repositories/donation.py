from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models.donation import Donation
from app.application.schema.donation import DonationCreate


class DonationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_donation(self, donation_create: DonationCreate) -> Donation:
        donation = Donation(
            amount=donation_create.amount,
            currency=donation_create.currency,
            payment_method=donation_create.payment_method,
            payment_status=donation_create.payment_status,
            transaction_id=donation_create.transaction_id,
            public_status=donation_create.public_status,
            user_id=donation_create.user_id
        )

        self.session.add(donation)
        await self.session.commit()
        await self.session.refresh(donation)
        return donation

    async def get_donation_by_id(self, donation_id: int):
        """根據捐款 ID 取得捐款"""
        result = await self.session.get(Donation, donation_id)
        return result

    async def get_all_donations(self):
        """取得所有捐款"""
        statement = select(Donation)
        results = await self.session.execute(statement)
        return results.scalars().all()

    async def update_donation(self, updated_donation: Donation):
        """更新一筆捐款"""
        self.session.add(updated_donation)
        await self.session.commit()
        await self.session.refresh(updated_donation)
        return updated_donation

    async def delete_donation(self, donation_id: int):
        """刪除一筆捐款"""
        donation_to_delete = await self.get_donation_by_id(donation_id)
        if donation_to_delete:
            await self.session.delete(donation_to_delete)
            await self.session.commit()
            return True
        return False
