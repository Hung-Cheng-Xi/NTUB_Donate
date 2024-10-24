from fastapi import APIRouter

from .announcement import router as announcement_router
from .auth import router as auth_router
from .donation import router as donation_router
from .donation_purpose import router as donation_purpose_router
from .excel import router as excel_router
from .ftp import router as ftp_router
from .regulation import router as regulation_router
from .unit import router as unit_router
from .user import router as user_router

admin_router = APIRouter(prefix="/admin")

admin_router.include_router(auth_router, prefix="/auth", tags=["Admin - auth"])

admin_router.include_router(
    excel_router, prefix="/excel", tags=["Admin - excel"]
)

admin_router.include_router(ftp_router, prefix="/ftp", tags=["Admin - ftp"])

admin_router.include_router(
    regulation_router, prefix="/regulation", tags=["Admin - regulation"]
)

admin_router.include_router(
    donation_purpose_router,
    prefix="/donation-purpose",
    tags=["Admin - Donation Purpose"],
)

admin_router.include_router(
    donation_router, prefix="/donation", tags=["Admin - Donation"]
)

admin_router.include_router(
    announcement_router, prefix="/announcement", tags=["Admin - Announcement"]
)

admin_router.include_router(unit_router, prefix="/unit", tags=["Admin - Unit"])

admin_router.include_router(user_router, prefix="/user", tags=["Admin - User"])
