from fastapi import APIRouter

from .auth import router as auth_router
from .excel import router as excel_router
from .ftp import router as ftp_router
from .document import router as document_router


admin_router = APIRouter(prefix="/admin")

admin_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Admin - auth"]
)

admin_router.include_router(
    excel_router,
    prefix="/excel",
    tags=["Admin - excel"]
)

admin_router.include_router(
    ftp_router,
    prefix="/ftp",
    tags=["Admin - ftp"]
)

admin_router.include_router(
    document_router,
    prefix="/document",
    tags=["Admin - document"]
)
