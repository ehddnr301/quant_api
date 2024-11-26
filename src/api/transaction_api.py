from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from src.domain import Transaction

from src.containers import Container
from src.services import TransactionService

router = APIRouter()


@router.get("/list", response_model=list[Transaction])
@inject
def list_transactions(
    transaction_service: TransactionService = Depends(
        Provide[Container.transaction_service]
    ),
):
    return transaction_service.list_transactions()


@router.get("/{transaction_id}", response_model=Transaction)
@inject
def get_transaction(
    transaction_id: int,
    transaction_service: TransactionService = Depends(
        Provide[Container.transaction_service]
    ),
):
    transaction = transaction_service.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.post("/", response_model=Transaction)
@inject
def create_transaction(
    transaction: Transaction,
    transaction_service: TransactionService = Depends(
        Provide[Container.transaction_service]
    ),
):
    return transaction_service.create_transaction(transaction)
