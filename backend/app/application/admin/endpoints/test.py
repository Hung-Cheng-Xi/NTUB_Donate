import logging
from fastapi import APIRouter


router = APIRouter()


@router.get("/test")
async def test():
    logging.info("test")
    return "test"
