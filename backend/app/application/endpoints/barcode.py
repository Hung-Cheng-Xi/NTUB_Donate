import logging
from typing import List
from fastapi import APIRouter, Depends

from app.application.schema.barcode import BarCodeData
from app.domain.services.barcode import BarCodeService

router = APIRouter()


# 呼叫 getBarCode 的端點
@router.post("/generate-barcode/")
async def generate_barcode(
    barcode_data: BarCodeData,
    barcode_service: BarCodeService = Depends()
) -> List[str]:
    logging.info("生成條碼")
    return await barcode_service.generate_barcode(barcode_data)
