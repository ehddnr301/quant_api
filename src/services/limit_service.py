from typing import List, Optional
from src.domain import Limit
from src.repository import LimitRepository


class LimitService:
    def __init__(self, limit_repository: LimitRepository):
        self.limit_repository = limit_repository

    def get_limit(self, user_id: int) -> Optional[Limit]:
        return self.limit_repository.get_limit_by_user_id(user_id)

    def list_limits(self) -> List[Limit]:
        return self.limit_repository.get_all_limits()

    def create_limit(self, limit: Limit) -> Limit:
        return self.limit_repository.add_limit(limit)

    def update_limit(self, limit: Limit) -> Limit:
        return self.limit_repository.update_limit(limit)
