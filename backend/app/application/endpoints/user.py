import logging
from typing import List
from fastapi import APIRouter, Depends

from app.domain.models.user import User
from app.application.schema.user import UserCreate
from app.infrastructure.repositories.user import UserRepository

router = APIRouter()


@router.get("/", response_model=List[User])
async def get_users(
    repository: UserRepository = Depends(),
):
    logging.info("取得 User 資料")
    return await repository.get_all_users()


@router.post("/", response_model=User)
async def create_user(
    new_user: UserCreate,
    repository: UserRepository = Depends(),
):
    logging.info("新增 User 資料到資料庫")
    return await repository.create_user(new_user)
