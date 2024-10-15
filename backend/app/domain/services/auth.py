import logging
from datetime import datetime, timedelta, timezone

import httpx
import jwt
from app.application.admin.schemas.auth import (AuthRequest, AuthResponse,
                                                GoogleTokenResponse)
from app.core.settings import settings
from fastapi import HTTPException
from starlette.responses import JSONResponse


class AuthService:
    def _create_refresh_token(self, data):
        payload = {
            'user_id': data['user_id'],
            'exp': datetime.now(timezone.utc) + timedelta(days=30),
            'iat': datetime.now(timezone.utc)
        }
        return jwt.encode(payload, settings.signing_key, algorithm='HS256')

    def _create_access_token(self, data):
        payload = {
            'user_id': data['user_id'],
            'exp': datetime.now(timezone.utc) + timedelta(minutes=30),
            'iat': datetime.now(timezone.utc)
        }
        return jwt.encode(payload, settings.signing_key, algorithm='HS256')

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(
                token, settings.signing_key, algorithms=['HS256'])
            return payload

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                detail="Token has expired",
                status_code=401
            )

        except jwt.InvalidTokenError:
            raise HTTPException(
                detail="Invalid token",
                status_code=401
            )

        except Exception as exc:
            raise HTTPException(
                detail=f"An error occurred: {str(exc)}",
                status_code=500
            )

    async def login(self, auth_request: AuthRequest) -> JSONResponse:
        logging.info("Verify google login waiting...")
        token_url = "https://oauth2.googleapis.com/token"
        logging.debug(auth_request.code)
        payload = {
            "code": auth_request.code,
            "client_id": settings.google_client_id,
            "client_secret": settings.google_client_secret,
            "redirect_uri": settings.google_redirect_uri,
            "grant_type": "authorization_code"
        }

        async with httpx.AsyncClient() as client:
            google_response = await client.post(token_url, data=payload)
            google_response.raise_for_status()
            token_data = GoogleTokenResponse(**google_response.json())

        logging.info(
            "Access token retrieved successfully, proceeding with verification"
        )

        token_info_url = \
            f"https://oauth2.googleapis.com/tokeninfo?access_token={
                token_data.access_token}"
        async with httpx.AsyncClient() as client:
            token_info_response = await client.get(token_info_url)
            token_info_response.raise_for_status()
            token_info = token_info_response.json()
            logging.debug(f"Token Info: {token_info}")

        user_data = {'user_id': token_info['sub']}
        access_token = self._create_access_token(user_data)
        refresh_token = self._create_refresh_token(user_data)

        response = JSONResponse(
            content={
                "access_token": access_token
            },
            status_code=200
        )
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            max_age=30 * 24 * 60 * 60,
            expires=30 * 24 * 60 * 60,
            path="/",
            samesite="Lax",
            secure=True
        )

        return response

    async def refresh(self, refresh_token: str) -> AuthResponse:
        try:
            payload = jwt.decode(
                refresh_token, settings.signing_key, algorithms=['HS256'])
            user_data = {'user_id': payload['user_id']}
            access_token = self._create_access_token(user_data)

            return AuthResponse(access_token=access_token)

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                detail="Token has expired",
                status_code=401
            )

        except jwt.InvalidTokenError:
            raise HTTPException(
                detail="Invalid token",
                status_code=401
            )

        except Exception as exc:
            raise HTTPException(
                detail=f"An error occurred: {str(exc)}",
                status_code=500
            )
