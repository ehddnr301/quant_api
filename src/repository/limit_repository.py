from typing import Optional, List
from sqlmodel import Session, select
from src.domain import Limit


class LimitRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_limit_by_user_id(self, user_id: int) -> Optional[Limit]:
        statement = select(Limit).where(Limit.user_id == user_id)
        return self.session.exec(statement).first()

    def get_all_limits(self) -> List[Limit]:
        statement = select(Limit)
        return self.session.exec(statement).all()

    def add_limit(self, limit: Limit) -> Limit:
        self.session.add(limit)
        self.session.commit()
        self.session.refresh(limit)
        return limit

    def update_limit(self, limit: Limit) -> Limit:
        existing_limit = self.get_limit_by_user_id(limit.user_id)
        if existing_limit is None:
            raise ValueError(f"Limit with user_id {limit.user_id} does not exist.")

        existing_limit.remaining_trades = limit.remaining_trades
        existing_limit.updated_at = limit.updated_at

        self.session.commit()
        self.session.refresh(existing_limit)
        return existing_limit
