import os
from typing import Callable, Generator
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


def create_db_and_tables():
    SQLModel.metadata.drop_all(engine)  # 기존 테이블 삭제
    SQLModel.metadata.create_all(engine)


class Database:
    def __init__(self) -> None:
        self._engine = engine

    def create_database(self) -> None:
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


database = Database()


def get_session() -> Generator[Session, None, None]:
    with database.session() as session:
        yield session
