from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.domcument import Document
from app.application.admin.schemas.document import DocumentCreate

from app.infrastructure.repositories.base import BaseRepository


class DocumentRepository(BaseRepository[Document]):
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db_session)]):
        super().__init__(session)

    async def create_document(self, document_create: DocumentCreate) -> Document:
        """新增一筆相關法規"""
        document = Document(**document_create.model_dump())
        return await self.create_instance(document)

    async def get_document_by_id(self, document_id: int) -> Document:
        """根據相關法規 ID 取得相關法規"""
        return await self.get_by_id(document_id, Document)

    async def get_all_documents(self) -> list[Document]:
        """取得所有相關法規"""
        return await self.get_all(Document)

    async def update_document(self, document_id: int, updated_document: Document) -> Document:
        """更新一筆相關法規"""
        document = updated_document.model_dump()
        return await self.update_instance(document_id, document, Document)

    async def patch_document(self, document_id: int, updated_document: Document) -> Document:
        """部分更新一筆相關法規"""
        document = updated_document.model_dump()
        return await self.patch_instance(document_id, document, Document)

    async def delete_document(self, document_id: int) -> bool:
        """刪除一筆相關法規"""
        return await self.delete_instance(document_id, Document)
