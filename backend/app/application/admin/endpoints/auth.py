import logging
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, Request
from typing import Annotated

from app.domain.services.auth import AuthService
from app.application.admin.schemas.auth import (
    AuthRequest,
    AuthResponse
)

router = APIRouter()


@router.post("/login/")
async def login(
    auth_request: AuthRequest,
    auth_service: Annotated[AuthService, Depends()]
) -> JSONResponse:
    logging.info("Call login API")
    return await auth_service.login(auth_request)


@router.post("/refresh/")
async def refresh(
    auth_service: Annotated[AuthService, Depends()],
    request: Request
) -> AuthResponse:
    logging.info("Call refresh API")
    cookie_value = request.cookies.get("refresh_token")
    logging.debug(cookie_value)
    return await auth_service.refresh(cookie_value)
