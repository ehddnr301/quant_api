from typing import Optional, List
from sqlmodel import Session, select
from src.domain.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        statement = select(User).where(User.id == user_id)
        return self.session.exec(statement).first()

    def get_all_users(self) -> List[User]:
        statement = select(User)
        return self.session.exec(statement).all()

    def add_user(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
