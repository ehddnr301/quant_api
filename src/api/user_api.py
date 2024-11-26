from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from src.domain import User

from src.containers import Container
from src.services import UserService

from typing import Optional

router = APIRouter()


@router.get("", response_model=list[User])
@inject
def list_users(user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.list_users()


# @router.get("/{user_id}", response_model=User)
# def get_user(user_id: int, session: Session = Depends(get_session)):
#     user_repository = UserRepository(session)
#     user_service = UserService(user_repository)
#     user = user_service.get_user(user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


@router.get("/{name}", response_model=Optional[User])
@inject
def get_user(
    name: str, user_service: UserService = Depends(Provide[Container.user_service])
):
    user = user_service.get_user_by_name(name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("", response_model=User)
@inject
def create_user(
    user: User, user_service: UserService = Depends(Provide[Container.user_service])
):
    return user_service.create_user(user)
