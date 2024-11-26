from fastapi import APIRouter, Depends, HTTPException
from src.domain import Limit
from src.services import LimitService

from dependency_injector.wiring import inject, Provide
from src.containers import Container

router = APIRouter()


@router.get("/list", response_model=list[Limit])
@inject
def list_limits(
    limit_service: LimitService = Depends(Provide[Container.limit_service]),
):
    return limit_service.list_limits()


@router.get("/{user_id}", response_model=Limit)
@inject
def get_limit(
    user_id: int,
    limit_service: LimitService = Depends(Provide[Container.limit_service]),
):
    limit = limit_service.get_limit(user_id)
    if not limit:
        raise HTTPException(status_code=404, detail="Limit not found")
    return limit


@router.post("/", response_model=Limit)
@inject
def create_limit(
    limit: Limit,
    limit_service: LimitService = Depends(Provide[Container.limit_service]),
):
    return limit_service.create_limit(limit)


@router.put("/", response_model=Limit)
@inject
def update_limit(
    limit: Limit,
    limit_service: LimitService = Depends(Provide[Container.limit_service]),
):
    return limit_service.update_limit(limit)
