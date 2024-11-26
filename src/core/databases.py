import os
from typing import Generator
from sqlmodel import SQLModel, Session, create_engine
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()

env = os.getenv("ENV", "test")
if env == "prod":
    db_url = os.getenv("PROD_DATABASE_URL")
else:
    db_url = os.getenv("TEST_DATABASE_URL")

engine = create_engine(db_url)


class Database:
    def __init__(self) -> None:
        self._engine = engine

    def create_database(self) -> None:
        SQLModel.metadata.drop_all(self._engine)
        SQLModel.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        session: Session = Session(self._engine)

        try:
            yield session
            session.commit()
        except Exception as e:
            print("Session rollback because of exception:", e)
            session.rollback()
            raise
        finally:
            session.close()
