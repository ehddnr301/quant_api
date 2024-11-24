from typing import List, Optional
from src.domain import Transaction
from src.repository import TransactionRepository


class TransactionService:
    def __init__(self, transaction_repository: TransactionRepository):
        self.transaction_repository = transaction_repository

    def get_transaction(self, transaction_id: int) -> Optional[Transaction]:
        return self.transaction_repository.get_transaction_by_id(transaction_id)

    def list_transactions(self) -> List[Transaction]:
        return self.transaction_repository.get_all_transactions()

    def create_transaction(self, transaction: Transaction) -> Transaction:
        return self.transaction_repository.add_transaction(transaction)
