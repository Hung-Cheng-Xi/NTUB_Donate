import logging
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.domain.models.user import User
from app.application.schema.user import UserCreate
from app.infrastructure.repositories.user import UserRepository

router = APIRouter()


@router.get("/", response_model=List[User])
async def read_users(db: AsyncSession = Depends(get_db_session)):
    donation_purpose_repo = UserRepository(db)
    users = await donation_purpose_repo.get_all_users()
    logging.info("取得 User 資料")
    return users


@router.post("/", response_model=User)
async def create_user(new_user: UserCreate, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    created_user = await user_repo.create_user(new_user)
    logging.info("新增 User 資料到資料庫")
    return created_user
