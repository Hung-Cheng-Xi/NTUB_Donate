from fastapi import APIRouter
from .test import router as tese_router

admin_router = APIRouter(prefix="/admin")

admin_router.include_router(
    tese_router,
    prefix="/test",
    tags=["Admin - test"]
)
