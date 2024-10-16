import logging

from typing import List, Annotated
from fastapi import APIRouter, Depends

from app.domain.models.user import User
from app.application.admin.schemas.user import UserCreate
from app.infrastructure.repositories.user import UserRepository

router = APIRouter()


@router.get("/", response_model=List[User])
async def get_users(
    repository: Annotated[UserRepository, Depends()]
):
    logging.info("取得 User 資料")
    return await repository.get_users()


@router.post("/", response_model=User)
async def create_user(
    new_user: UserCreate,
    repository: Annotated[UserRepository, Depends()]
):
    logging.info("新增 User 資料到資料庫")
    return await repository.create_user(new_user)


@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: int,
    repository: Annotated[UserRepository, Depends()]
):
    logging.info("取得 User 資料")
    return await repository.get_user(user_id)


@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    new_user: UserCreate,
    repository: Annotated[UserRepository, Depends()]
):
    logging.info("更新 User 資料")
    return await repository.update_user(user_id, new_user)


@router.delete("/{user_id}", response_model=User)
async def delete_user(
    user_id: int,
    repository: Annotated[UserRepository, Depends()]
) -> User:
    logging.info("刪除 User 資料")
    return await repository.delete_user(user_id)
