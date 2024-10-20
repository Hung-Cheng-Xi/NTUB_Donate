from typing import Annotated, Any

from fastapi import Depends

from app.application.client.schemas.donation_purpose import DonationPurposeItem, PaginatedDonationPurposeInfoResponse
from app.infrastructure.repositories.donation_purpose import (
    DonationPurposeRepository,
)


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
    ) -> PaginatedDonationPurposeInfoResponse:
        purposes, total_count = await self.donation_repository.client_get_donation_purposes(
            skip, limit
        )
        donation_purposes = []
        for purpose in purposes:
            total_donation: Any = sum(
                donation.amount for donation in purpose.donations
            )
            achieved_percentage = (
                total_donation / purpose.lump_sum * 100
                if purpose.lump_sum
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

        return PaginatedDonationPurposeInfoResponse(
            total_count=total_count,
            items=sorted_donation_purposes,
        )
