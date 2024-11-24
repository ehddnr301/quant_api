from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.domain.user import User
from src.services import UserService
from src.repository.user_repository import UserRepository
from src.core import get_session  # DB 세션 의존성 주입

router = APIRouter()


@router.get("/users", response_model=list[User])
def list_users(session: Session = Depends(get_session)):
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)
    return user_service.list_users()


@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = Depends(get_session)):
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)
    return user_service.create_user(user)
