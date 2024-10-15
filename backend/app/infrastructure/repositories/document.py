from app.application.admin.schemas.document import DocumentCreate, DocumentInfo
from app.domain.models.domcument import Document
from app.infrastructure.repositories.base import BaseRepository


class DocumentRepository(BaseRepository[Document]):
    async def create_document(
        self,
        document_create: DocumentCreate
    ) -> Document:
        """新增一筆相關法規"""
        document = Document(**document_create.model_dump())
        return await self.create_instance(document)

    async def get_document(
        self,
        document_id: int
    ) -> Document:
        """根據相關法規 ID 取得相關法規"""
        return await self.get_by_id(document_id, Document)

    async def get_documents(
        self,
        skip: int,
        limit: int
    ) -> list[DocumentInfo]:
        """取得分頁的相關法規"""
        documents = await self.get_paginated_all(Document, skip, limit)
        return [DocumentInfo.model_dump(document) for document in documents]

    async def update_document(
        self,
        document_id: int,
        updated_document: Document
    ) -> Document:
        """更新一筆相關法規"""
        document = updated_document.model_dump()
        return await self.update_instance(document_id, document, Document)

    async def patch_document(
        self,
        document_id: int,
        updated_document: Document
    ) -> Document:
        """部分更新一筆相關法規"""
        document = updated_document.model_dump()
        return await self.patch_instance(document_id, document, Document)

    async def delete_document(self, document_id: int) -> bool:
        """刪除一筆相關法規"""
        return await self.delete_instance(document_id, Document)
