from app.domain.models.user import User
from app.application.admin.schemas.user import (
    UserCreate,
    UserUpdate
    )
from app.infrastructure.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    async def create_user(
        self,
        user_create: UserCreate,
    ) -> User:
        """新增一筆用戶"""
        user = User(**user_create.model_dump())
        return await self.create_instance(user)

    async def get_user(
        self,
        user_id: int,
    ) -> User:
        """根據用戶 ID 取得用戶"""
        return await self.get_by_id(user_id, User)

    async def get_users(self) -> list[User]:
        """取得所有用戶"""
        return await self.get_all(User)

    async def update_user(
        self,
        user_id: int,
        updated_user: UserUpdate,
    ) -> UserUpdate:
        """更新一筆用戶"""
        user = updated_user.model_dump()
        return await self.update_instance(user_id, user, User)

    async def delete_user(
        self,
        user_id: int,
    ) -> User:
        """刪除一筆用戶"""
        return await self.delete_instance(user_id, User)
