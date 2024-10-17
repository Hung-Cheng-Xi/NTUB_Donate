from fastapi import APIRouter

from .barcode import router as barcode_router
from .donation import router as donation_router
from .donation_purpose import (
    router as donation_purpose_router
)
from .address import router as address_router
from .regulation import router as document_router
from .announcement import router as announcement_router

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
    announcement_router,
    prefix="/announcement",
    tags=["Client - Announcement"]
)

client_router.include_router(
    document_router,
    prefix="/regulation",
    tags=["Client - Regulation"]
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
