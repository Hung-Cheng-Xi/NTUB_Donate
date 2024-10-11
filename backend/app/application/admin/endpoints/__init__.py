from fastapi import APIRouter
from .test import router as tese_router
from .excel import router as excel_router
from .ftp import router as ftp_router

admin_router = APIRouter(prefix="/admin")

admin_router.include_router(
    tese_router,
    prefix="/test",
    tags=["Admin - test"]
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
