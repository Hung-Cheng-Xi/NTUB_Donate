from typing import List

import httpx
from app.application.client.schemas.barcode import BarCodeData
from app.core.settings import settings
from fastapi import HTTPException


class BarCodeService:
    async def generate_barcode(
            self,
            barcode_data: BarCodeData
    ) -> List[str]:
        url = settings.barcode_api_url
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url,
                    json=barcode_data.model_dump()
                )
                return response.json()

            except httpx.RequestError as exc:
                raise HTTPException(
                    status_code=500,
                    detail=f"HTTP error occurred: {str(exc)}"
                )

            except Exception as exc:
                raise HTTPException(
                    status_code=500,
                    detail=f"An error occurred: {str(exc)}"
                )
