import logging
from typing import List, Annotated
from fastapi import APIRouter, Depends

from app.domain.models.domcument import Document
from app.application.admin.schemas.document import DocumentCreate
from backend.app.infrastructure.repositories.document import DocumentRepository

router = APIRouter()


@router.get("/", response_model=List[Document])
async def get_documents(
    repository: Annotated[DocumentRepository, Depends()],
):
    logging.info("取得 Document 資料")
    return await repository.get_all_documents()


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
