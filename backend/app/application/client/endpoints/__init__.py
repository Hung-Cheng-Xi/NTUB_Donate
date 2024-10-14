from fastapi import APIRouter

from app.application.client.endpoints.donation import router as donation_router
from app.application.client.endpoints.barcode import router as barcode_router
from app.application.client.endpoints.donation_purpose import (
    router as donation_purpose_router
)
from app.application.client.endpoints.news import router as news_purpose_router
from app.application.client.endpoints.address import router as address_router

client_router = APIRouter(prefix="/client")

client_router.include_router(
    donation_router,
    prefix="/donation",
    tags=["Client - Donation"]
)

client_router.include_router(
    donation_purpose_router,
    prefix="/donation_purpose",
    tags=["Client - Donation Purpose"]
)

client_router.include_router(
    news_purpose_router,
    prefix="/news",
    tags=["Client - News"]
)

client_router.include_router(
    barcode_router,
    prefix="/barcode",
    tags=["Client - Barcode"]
)

client_router.include_router(
    address_router,
    prefix="/address",
    tags=["Client - Address"]
)
