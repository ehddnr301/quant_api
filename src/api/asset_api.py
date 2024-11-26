from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from src.domain import Asset

from src.containers import Container
from src.services import AssetService

router = APIRouter()


@router.get("/list", response_model=list[Asset])
@inject
def list_assets(
    asset_service: AssetService = Depends(Provide[Container.asset_service]),
):
    return asset_service.list_assets()


@router.get("/{user_id}", response_model=list[Asset])
@inject
def get_asset(
    user_id: int,
    asset_service: AssetService = Depends(Provide[Container.asset_service]),
):
    asset = asset_service.get_assets(user_id)
    return asset


@router.post("/", response_model=Asset)
@inject
def create_asset(
    asset: Asset,
    asset_service: AssetService = Depends(Provide[Container.asset_service]),
):
    return asset_service.create_asset(asset)
