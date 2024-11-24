from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.domain import Limit
from src.services import LimitService
from src.repository import LimitRepository
from src.core import get_session  # DB 세션 의존성 주입

router = APIRouter()


@router.get("/list", response_model=list[Limit])
def list_limits(session: Session = Depends(get_session)):
    limit_repository = LimitRepository(session)
    limit_service = LimitService(limit_repository)
    return limit_service.list_limits()


@router.get("/{user_id}", response_model=Limit)
def get_limit(user_id: int, session: Session = Depends(get_session)):
    limit_repository = LimitRepository(session)
    limit_service = LimitService(limit_repository)
    limit = limit_service.get_limit(user_id)
    if not limit:
        raise HTTPException(status_code=404, detail="Limit not found")
    return limit


@router.post("/", response_model=Limit)
def create_limit(limit: Limit, session: Session = Depends(get_session)):
    limit_repository = LimitRepository(session)
    limit_service = LimitService(limit_repository)
    return limit_service.create_limit(limit)


@router.put("/", response_model=Limit)
def update_limit(limit: Limit, session: Session = Depends(get_session)):
    limit_repository = LimitRepository(session)
    limit_service = LimitService(limit_repository)
    return limit_service.update_limit(limit)
