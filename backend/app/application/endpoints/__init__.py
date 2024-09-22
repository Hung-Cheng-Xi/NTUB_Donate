from fastapi import APIRouter

from app.application.endpoints.user import (
    router as user_router
)
from app.application.endpoints.donation import router as donation_router
from app.application.endpoints.barcode import router as barcode_router

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
    barcode_router,
    prefix="/barcode",
    tags=["Barcode"]
)
