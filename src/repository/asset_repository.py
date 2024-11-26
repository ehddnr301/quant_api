from typing import Optional, List
from sqlmodel import Session, select
from src.domain import Asset


class AssetRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user_assets_by_id(self, user_id: int) -> Optional[Asset]:
        with self.session() as session:
            statement = select(Asset).where(Asset.user_id == user_id)
            assets = session.exec(statement).all()
            return [Asset.model_validate(asset) for asset in assets]

    def get_all_assets(self) -> List[Asset]:
        with self.session() as session:
            statement = select(Asset)
            return [
                Asset.model_validate(asset) for asset in session.exec(statement).all()
            ]

    def add_asset(self, asset: Asset) -> Asset:
        with self.session() as session:
            db_asset = Asset.model_validate(asset)
            session.add(db_asset)
            session.commit()
            session.refresh(db_asset)
            return db_asset
