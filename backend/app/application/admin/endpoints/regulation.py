import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.admin.schemas.regulation import (
    RegulationCreate,
    RegulationtUpdate,
    PaginatedRegulationInfoResponse,
)
from app.domain.models.regulation import Regulation
from app.infrastructure.repositories.regulation import RegulationRepository

router = APIRouter()


@router.get("/", response_model=PaginatedRegulationInfoResponse)
async def get_regulations(
    repository: Annotated[RegulationRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
    search: str = None,
) -> PaginatedRegulationInfoResponse:
    logging.info("取得分頁的 Regulations 資料")
    return await repository.get_regulations(skip, limit, search)


@router.post("/", response_model=Regulation)
async def create_regulation(
    new_regulation: RegulationCreate,
    repository: Annotated[RegulationRepository, Depends()],
):
    logging.info("新增 Regulation 資料到資料庫")
    return await repository.create_regulation(new_regulation)


@router.get("/{regulation_id}", response_model=Regulation)
async def get_regulation(
    regulation_id: int, repository: Annotated[RegulationRepository, Depends()]
):
    logging.info("取得 Regulation 資料")
    return await repository.get_regulation(regulation_id)


@router.put("/{regulation_id}", response_model=Regulation)
async def update_regulation(
    regulation_id: int,
    new_regulation: RegulationtUpdate,
    repository: Annotated[RegulationRepository, Depends()],
):
    logging.info("更新 Regulation 資料")
    return await repository.update_regulation(regulation_id, new_regulation)


@router.delete("/{regulation_id}", response_model=Regulation)
async def delete_regulation(
    regulation_id: int, repository: Annotated[RegulationRepository, Depends()]
):
    logging.info("刪除 Regulation 資料")
    return await repository.delete_regulation(regulation_id)
