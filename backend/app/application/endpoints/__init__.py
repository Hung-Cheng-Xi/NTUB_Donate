from fastapi import APIRouter

from app.application.endpoints.user import (
    router as user_router
)
from app.application.endpoints.donation import router as donation_router
from app.application.endpoints.barcode import router as barcode_router
from app.application.endpoints.donation_purpose import router as donation_purpose_router
from app.application.endpoints.unit import router as unit_purpose_router
from app.application.endpoints.news import router as news_purpose_router
from app.application.endpoints.address import router as address_router

main_router = APIRouter()

main_router.include_router(
    user_router,
    prefix="/user",
    tags=["User"]
)

main_router.include_router(
    donation_router,
    prefix="/donation",
    tags=["Donation"]
)

main_router.include_router(
    donation_purpose_router,
    prefix="/donation_purpose",
    tags=["Donation Purpose"]
)

main_router.include_router(
    unit_purpose_router,
    prefix="/unit",
    tags=["Unit"]
)

main_router.include_router(
    news_purpose_router,
    prefix="/news",
    tags=["News"]
)

main_router.include_router(
    barcode_router,
    prefix="/barcode",
    tags=["Barcode"]
)

main_router.include_router(
    address_router,
    prefix="/address",
    tags=["Address"]
)
