from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.domain.models.user import User
from app.application.schema.user import UserCreate
from app.infrastructure.repositories.user import UserRepository

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=List[User])
async def read_users(db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    users = await user_repo.get_all_users()
    return users


@router.post("/", response_model=User)
async def create_user(new_user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    created_user = await user_repo.create_user(new_user)
    return created_user
