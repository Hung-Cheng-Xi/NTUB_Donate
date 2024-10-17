import logging
from typing import Annotated, List

from fastapi import APIRouter, Depends

from app.application.admin.schemas.regulation import RegulationInfo
from app.domain.models.regulation import Regulation
from app.infrastructure.repositories.regulation import RegulationRepository

router = APIRouter()


@router.get("/", response_model=List[RegulationInfo])
async def get_regulations(
    repository: Annotated[RegulationRepository, Depends()],
    skip: int = 0,
    limit: int = 10,
) -> List[RegulationInfo]:
    logging.info("取得分頁的 Regulations 資料")
    return await repository.get_regulations(skip, limit)


@router.get("/{regulation_id}", response_model=Regulation)
async def get_regulation(
    regulation_id: int, repository: Annotated[RegulationRepository, Depends()]
):
    logging.info("取得 Regulation 資料")
    return await repository.get_regulation(regulation_id)
