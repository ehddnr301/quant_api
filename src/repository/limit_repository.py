from typing import Optional, List
from sqlmodel import select
from src.domain import Limit
from src.core.databases import Database


class LimitRepository:
    def __init__(self, session: Database.session):
        self.session = session

    def get_limit_by_user_id(self, user_id: int) -> Optional[Limit]:
        with self.session() as session:
            statement = select(Limit).where(Limit.user_id == user_id)
            limit = session.exec(statement).first()
            return Limit.model_validate(limit)

    def get_all_limits(self) -> List[Limit]:
        with self.session() as session:
            statement = select(Limit)
            return [Limit.model_validate(l) for l in session.exec(statement).all()]

    def add_limit(self, limit: Limit) -> Limit:
        with self.session() as session:
            db_limit = Limit.model_validate(limit)
            session.add(db_limit)
            session.commit()
            session.refresh(db_limit)
            return db_limit

    def update_limit(self, limit: Limit) -> Limit:
        existing_limit = self.get_limit_by_user_id(limit.user_id)
        if existing_limit is None:
            raise ValueError(f"Limit with user_id {limit.user_id} does not exist.")

        existing_limit.remaining_trades = limit.remaining_trades
        existing_limit.updated_at = limit.updated_at

        with self.session() as session:
            session.merge(existing_limit)
            return existing_limit
