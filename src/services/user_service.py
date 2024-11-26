from typing import List, Optional
from src.domain import User
from src.repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.user_repository = repository

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_user_by_id(user_id)

    def list_users(self) -> List[Optional[User]]:
        users = self.user_repository.get_all_users()
        return users

    def create_user(self, user: User) -> User:
        return self.user_repository.add_user(user)

    def get_user_by_name(self, name: str) -> Optional[User]:
        return self.user_repository.get_user_by_name(name)
