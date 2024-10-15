import logging
from typing import Annotated, Dict

from app.application.client.schemas.address import AddressData
from app.domain.services.address import AddressService
from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("/get_zipcode/")
async def get_zipcode(
    address_data: AddressData,
    address_service: Annotated[AddressService, Depends()]
) -> Dict:
    logging.info("查詢郵遞區號")
    return await address_service.get_zipcode(address_data)
