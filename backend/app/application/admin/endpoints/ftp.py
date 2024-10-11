import logging
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from app.domain.services.ftp_service import FTPService

router = APIRouter()



@router.post("/refresh-data")
async def refresh_data(ftp_service: Annotated[FTPService, Depends()]):
    logging.info("刷新 FTP 伺服器中的檔案")
    try:
        ftp_service.refresh_data()
        return {"message": "Data refreshed"}
    except HTTPException as e:
        logging.error(f"Error refreshing data: {e.detail}")
    finally:
        ftp_service.disconnect()


@router.post("/list-files")
async def list_files(ftp_service: Annotated[FTPService, Depends()]):
    logging.info("列出遠端 FTP 伺服器中的檔案")
    try:
        remote_path = "/"
        files = ftp_service.list_files(remote_path)
        return {"files": files}
    finally:
        ftp_service.disconnect()
