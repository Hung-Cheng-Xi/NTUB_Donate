import logging

from typing import Annotated, Dict
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.domain.services.excel_export import ExcelService


router = APIRouter()


@router.post("/export/")
async def excel_export(
    excel_service: Annotated[ExcelService, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> Dict:
    logging.info("匯出 Excel")
    workbook = await excel_service.create_workbook(skip, limit)
    output = await excel_service.export_to_bytes(workbook)

    # 使用 StreamingResponse 返回 Excel 檔案
    response = StreamingResponse(
        output,
        media_type=(
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    )
    response.headers["Content-Disposition"] = (
        "attachment; filename=donations.xlsx"
    )
    return response
