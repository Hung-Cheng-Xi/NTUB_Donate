from fastapi import APIRouter
from pydantic import BaseModel
import httpx
from app.core.config import settings

router = APIRouter(
    tags=["BarCode"]
)

# 定義jsondata的結構
class JsonData(BaseModel):
    Group: str = "730044" # 預設值
    SerialNumber: str = "00001" # 預設值
    Time: str = "9991230"  # 預設值
    Money: str = "1000" # 預設值

# 呼叫 getBarCode 的端點
@router.post("/generate-barcode/")
async def generate_barcode(jsondata: JsonData):
    url = settings.barcode_api_url
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=jsondata.model_dump())
        return response.json()
