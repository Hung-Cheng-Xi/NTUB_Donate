from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.domain.models.hero import Hero
from app.infrastructure.repositories.hero import HeroRepository
from app.core.config import engine

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

@router.post("/heroes/")
def create_hero(name: str, secret_name: str, session: Session = Depends(get_session)):
    hero_repo = HeroRepository(session)
    hero = Hero(name=name, secret_name=secret_name)
    return hero_repo.create(hero)
