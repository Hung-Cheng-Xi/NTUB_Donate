from fastapi import APIRouter
from .test import router as tese_router
from .excel import router as excel_router

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
