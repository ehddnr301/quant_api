from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.domain import Transaction
from src.services import TransactionService
from src.repository import TransactionRepository
from src.core import get_session  # DB 세션 의존성 주입

router = APIRouter()


@router.get("/list", response_model=list[Transaction])
def list_transactions(session: Session = Depends(get_session)):
    transaction_repository = TransactionRepository(session)
    transaction_service = TransactionService(transaction_repository)
    return transaction_service.list_transactions()


@router.get("/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: int, session: Session = Depends(get_session)):
    transaction_repository = TransactionRepository(session)
    transaction_service = TransactionService(transaction_repository)
    transaction = transaction_service.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.post("/", response_model=Transaction)
def create_transaction(
    transaction: Transaction, session: Session = Depends(get_session)
):
    transaction_repository = TransactionRepository(session)
    transaction_service = TransactionService(transaction_repository)
    return transaction_service.create_transaction(transaction)
