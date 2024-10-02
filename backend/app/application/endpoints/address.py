import logging
from typing import Dict
from fastapi import APIRouter, Depends

from app.application.schema.address import AddressData
from app.domain.services.address import AddressService

router = APIRouter()


# 呼叫查詢郵遞區號的端點
@router.post("/get_zipcode/")
async def get_zipcode(
    address_data: AddressData,
    address_service: AddressService = Depends()
) -> Dict:
    logging.info("查詢郵遞區號")
    return await address_service.get_zipcode(address_data)
