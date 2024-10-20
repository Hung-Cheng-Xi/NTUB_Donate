from typing import Annotated, Any

from fastapi import Depends

from app.application.client.schemas.donation_purpose import DonationPurposeItem
from app.infrastructure.repositories.donation_purpose import (
    DonationPurposeRepository,
)
from app.application.admin.schemas.paginated import PaginatedResponse


class DonationPurposeService:
    def __init__(
        self,
        donation_repository: Annotated[DonationPurposeRepository, Depends()],
    ):
        self.donation_repository = donation_repository

    async def get_sorted_donation_purpose(
        self,
        skip: int,
        limit: int,
    ) -> PaginatedResponse[DonationPurposeItem]:
        purposes = await self.donation_repository.get_donation_purposes(
            skip, limit
        )
        donation_purposes = []
        for purpose in purposes.items:
            total_donation: Any = sum(
                donation.amount for donation in purpose.donations
            )
            achieved_percentage: Any = (
                total_donation / purpose.lump_sum
                if purpose.lump_sum > 0
                else 0
            )

            purpose_dict = purpose.model_dump()
            purpose_dict.update(
                {
                    "total_donation": total_donation,
                    "achieved_percentage": achieved_percentage,
                }
            )
            donation_purposes.append(DonationPurposeItem(**purpose_dict))

        sorted_donation_purposes = sorted(
            donation_purposes,
            key=lambda purpose: purpose.achieved_percentage,
            reverse=True,
        )

        return PaginatedResponse(
            total_count=purposes.total_count,
            items=sorted_donation_purposes,
        )
