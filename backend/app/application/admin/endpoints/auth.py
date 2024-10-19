import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from app.application.admin.schemas.auth import AuthRequest, AuthResponse
from app.domain.services.auth import AuthService

router = APIRouter()


@router.post("/login/")
async def login(
    auth_request: AuthRequest, auth_service: Annotated[AuthService, Depends()]
) -> JSONResponse:
    logging.info("Call login API")
    return await auth_service.login(auth_request)


@router.post("/refresh/")
async def refresh(
    auth_service: Annotated[AuthService, Depends()], request: Request
) -> AuthResponse:
    logging.info("Call refresh API")
    cookie_value = request.cookies.get("refresh_token")
    logging.debug(cookie_value)
    return await auth_service.refresh(cookie_value)
