from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "postgresql://postgres:p%40ssw0rd@localhost:5432/NTUB_SecumanageDB"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session
