from typing import Optional, List
from sqlmodel import Session, select
from src.domain import Transaction


class TransactionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_transaction_by_id(self, transaction_id: int) -> Optional[Transaction]:
        with self.session() as session:
            statement = select(Transaction).where(
                Transaction.transaction_id == transaction_id
            )
            transaction = session.exec(statement).first()
            return Transaction.model_validate(transaction)

    def get_all_transactions(self) -> List[Transaction]:
        with self.session() as session:
            statement = select(Transaction)
            return [
                Transaction.model_validate(t) for t in session.exec(statement).all()
            ]

    def add_transaction(self, transaction: Transaction) -> Transaction:
        with self.session() as session:
            db_transaction = Transaction.model_validate(transaction)
            session.add(db_transaction)
            session.commit()
            session.refresh(db_transaction)
            return db_transaction
