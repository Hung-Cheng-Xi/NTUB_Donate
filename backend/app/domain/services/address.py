from fastapi import HTTPException
import httpx
from typing import Dict

from app.core.config import settings
from app.application.client.schemas.address import AddressData


class AddressService:
    def __init__(self):
        self.API_URL = settings.zipcode_api_url

    async def get_zipcode(
        self,
        address_data: AddressData
    ) -> Dict:
        url = f"{self.API_URL}?adrs={address_data.address}"

        async with httpx.AsyncClient() as client:
            try:
                # 非同步請求郵遞區號查詢API
                response = await client.get(url)
                response.raise_for_status()  # 檢查是否有錯誤
                return response.json()  # 同步方法，不需要 await

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
