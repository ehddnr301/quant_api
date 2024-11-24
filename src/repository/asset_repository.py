from typing import Optional, List
from sqlmodel import Session, select
from src.domain import Asset


class AssetRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user_assets_by_id(self, user_id: int) -> Optional[Asset]:
        statement = select(Asset).where(Asset.user_id == user_id)
        return self.session.exec(statement).all()

    def get_all_assets(self) -> List[Asset]:
        statement = select(Asset)
        return self.session.exec(statement).all()

    def add_asset(self, asset: Asset) -> Asset:
        self.session.add(asset)
        self.session.commit()
        self.session.refresh(asset)
        return asset
