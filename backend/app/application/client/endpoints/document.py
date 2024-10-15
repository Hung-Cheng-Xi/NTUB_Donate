import logging
from typing import List, Annotated
from fastapi import APIRouter, Depends

from app.domain.models.domcument import Document
from app.application.client.schemas.document import DocumentInfo
from app.infrastructure.repositories.document import DocumentRepository

router = APIRouter()


@router.get("/", response_model=List[DocumentInfo])
async def get_documents(
    repository: Annotated[DocumentRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> List[DocumentInfo]:
    logging.info("取得分頁的 Documents 資料")
    return await repository.get_documents(skip, limit)

@router.get("/{document_id}", response_model=Document)
async def get_document(
    document_id: int,
    repository: Annotated[DocumentRepository, Depends()]
):
    logging.info("取得 Document 資料")
    return await repository.get_document(document_id)
