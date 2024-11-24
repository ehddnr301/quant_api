from typing import Optional, List
from sqlmodel import Session, select
from src.domain import Transaction


class TransactionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_transaction_by_id(self, transaction_id: int) -> Optional[Transaction]:
        statement = select(Transaction).where(
            Transaction.transaction_id == transaction_id
        )
        return self.session.exec(statement).first()

    def get_all_transactions(self) -> List[Transaction]:
        statement = select(Transaction)
        return self.session.exec(statement).all()

    def add_transaction(self, transaction: Transaction) -> Transaction:
        self.session.add(transaction)
        self.session.commit()
        self.session.refresh(transaction)
        return transaction
