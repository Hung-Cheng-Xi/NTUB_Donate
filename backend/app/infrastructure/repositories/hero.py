from sqlmodel import Session
from app.domain.models.hero import Hero

class HeroRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, hero: Hero) -> Hero:
        self.session.add(hero)
        self.session.commit()
        self.session.refresh(hero)
        return hero
