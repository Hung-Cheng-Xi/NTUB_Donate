from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import httpx

from app.core.config import settings

router = APIRouter()

API_URL = settings.address_api_url


# 定義接收地址的數據模型，並添加範例
class AddressData(BaseModel):
    address: str = Field(..., example="臺中市西屯區臺灣大道三段99號")

# 呼叫查詢郵遞區號的端點
@router.post("/get_zipcode/")
async def get_zipcode(address_data: AddressData):
    url = f"{API_URL}?adrs={address_data.address}"

    async with httpx.AsyncClient() as client:
        try:
            # 非同步請求郵遞區號查詢API
            response = await client.get(url)
            response.raise_for_status()  # 檢查是否有錯誤
            return response.json()  # 同步方法，不需要 await

        except httpx.RequestError as exc:
            raise HTTPException(status_code=500, detail=f"HTTP error occurred: {str(exc)}")

        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(exc)}")
