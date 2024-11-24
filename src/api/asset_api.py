from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.domain import Asset
from src.services import AssetService
from src.repository import AssetRepository
from src.core import get_session  # DB 세션 의존성 주입

router = APIRouter()


@router.get("/list", response_model=list[Asset])
def list_assets(session: Session = Depends(get_session)):
    asset_repository = AssetRepository(session)
    asset_service = AssetService(asset_repository)
    return asset_service.list_assets()


@router.get("/{user_id}", response_model=list[Asset])
def get_asset(user_id: int, session: Session = Depends(get_session)):
    asset_repository = AssetRepository(session)
    asset_service = AssetService(asset_repository)
    asset = asset_service.get_assets(user_id)
    print(asset)
    print("-----------------")
    return asset


@router.post("/", response_model=Asset)
def create_asset(asset: Asset, session: Session = Depends(get_session)):
    asset_repository = AssetRepository(session)
    asset_service = AssetService(asset_repository)
    return asset_service.create_asset(asset)
