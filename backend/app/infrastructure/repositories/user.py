from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models.user import User
from app.application.schema.user import UserCreate

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, new_user: UserCreate):
        """新增一個用戶到資料庫"""
        user = User(
            user_name=new_user.user_name,
            user_email=new_user.user_email,
            user_phone_number=new_user.user_phone_number,
            user_address=new_user.user_address
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user


    async def get_user_by_id(self, user_id: int):
        """根據用戶 ID 取得用戶"""
        result = await self.session.get(User, user_id)
        return result

    async def get_all_users(self):
        """取得所有用戶"""
        statement = select(User)
        results = await self.session.execute(statement)
        return results.scalars().all()

    async def update_user(self, updated_user: User):
        """更新一個用戶"""
        self.session.add(updated_user)
        await self.session.commit()
        await self.session.refresh(updated_user)
        return updated_user

    async def delete_user(self, user_id: int):
        """刪除一個用戶"""
        user_to_delete = await self.get_user_by_id(user_id)
        if user_to_delete:
            await self.session.delete(user_to_delete)
            await self.session.commit()
            return True
        return False
