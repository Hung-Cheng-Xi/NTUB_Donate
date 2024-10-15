import logging
from typing import Annotated, List

from app.application.admin.schemas.document import DocumentCreate, DocumentInfo
from app.domain.models.domcument import Document
from app.infrastructure.repositories.document import DocumentRepository
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/", response_model=List[DocumentInfo])
async def get_documents(
    repository: Annotated[DocumentRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> List[DocumentInfo]:
    logging.info("取得分頁的 Documents 資料")
    return await repository.get_document_all(skip, limit)


@router.post("/", response_model=Document)
async def create_document(
    new_document: DocumentCreate,
    repository: Annotated[DocumentRepository, Depends()]
):
    logging.info("新增 Document 資料到資料庫")
    return await repository.create_document(new_document)


@router.get("/{document_id}", response_model=Document)
async def get_document(
    document_id: int,
    repository: Annotated[DocumentRepository, Depends()]
):
    logging.info("取得 Document 資料")
    return await repository.get_document_by_id(document_id)


@router.put("/{document_id}", response_model=Document)
async def update_document(
    document_id: int,
    new_document: DocumentCreate,
    repository: Annotated[DocumentRepository, Depends()]
):
    logging.info("更新 Document 資料")
    return await repository.update_document(document_id, new_document)
