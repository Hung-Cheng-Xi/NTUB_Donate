import logging
from typing import Dict, Annotated
from fastapi import APIRouter, Depends, Response

from app.domain.services.excel_export import ExcelService

router = APIRouter()


@router.post("/export/")
async def excel_export(
    excel_service: Annotated[ExcelService, Depends()]
) -> Dict:
    logging.info("匯出 Excel")
    workbook = await excel_service.create_workbook()
    output = await excel_service.export_to_bytes(workbook)

    # 返回 Excel 文件作為下載
    headers = {
        'Content-Disposition': 'attachment; filename="data.xlsx"',
        'Content-Type': (
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    }
    return Response(
        content=output.read(),
        headers=headers,
        media_type=(
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    )
