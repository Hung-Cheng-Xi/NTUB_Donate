from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.user import User
from app.application.client.schemas.user import UserCreate

from app.infrastructure.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        super().__init__(session)

    async def create_user(self, user_create: UserCreate) -> User:
        """新增一筆用戶"""
        user = User(**user_create.model_dump())
        return await self.create_instance(user)

    async def get_user_by_id(self, user_id: int) -> User:
        """根據用戶 ID 取得用戶"""
        return await self.get_by_id(user_id, User)

    async def get_all_users(self) -> list[User]:
        """取得所有用戶"""
        return await self.get_all(User)

    async def update_user(self, user_id: int, updated_user: User) -> User:
        """更新一筆用戶"""
        user = updated_user.model_dump()
        return await self.update_instance(user_id, user, User)

    async def patch_user(self, user_id: int, updated_user: User) -> User:
        """部分更新一筆用戶"""
        user = updated_user.model_dump()
        return await self.patch_instance(user_id, user, User)

    async def delete_user(self, user_id: int) -> User:
        """刪除一筆用戶"""
        return await self.delete_instance(user_id, User)
