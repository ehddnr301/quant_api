from typing import Optional, List
from sqlmodel import select
from src.domain import User
from src.core.databases import Database


class UserRepository:
    def __init__(self, session: Database.session):
        self.session = session

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        with self.session() as session:
            statement = select(User).where(User.id == user_id)
            user = session.exec(statement).first()
            return User.model_validate(user)

    def get_user_by_name(self, name: str) -> Optional[User]:
        with self.session() as session:
            statement = select(User).where(User.name == name)
            user = session.exec(statement).first()
            return User.model_validate(user)

    def get_all_users(self) -> List[User]:
        with self.session() as session:
            statement = select(User)
            return [User.model_validate(i) for i in session.exec(statement).all()]

    def add_user(self, user: User) -> User:
        with self.session() as session:
            db_user = User.model_validate(user)
            session.add(db_user)
            return User.model_validate(db_user)
