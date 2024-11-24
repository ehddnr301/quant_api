from typing import List, Optional
from src.domain import User
from src.repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_user_by_id(user_id)

    def list_users(self) -> List[User]:
        return self.user_repository.get_all_users()

    def create_user(self, user: User) -> User:
        # if "@" not in user.email:
        #     raise ValueError("Invalid email address")
        return self.user_repository.add_user(user)
