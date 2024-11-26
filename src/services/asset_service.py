from typing import List, Optional
from src.domain import Asset
from src.repository import AssetRepository


class AssetService:
    def __init__(self, repository: AssetRepository):
        self.asset_repository = repository

    def get_assets(self, user_id: int) -> Optional[Asset]:
        return self.asset_repository.get_user_assets_by_id(user_id)

    def list_assets(self) -> List[Asset]:
        return self.asset_repository.get_all_assets()

    def create_asset(self, asset: Asset) -> Asset:
        return self.asset_repository.add_asset(asset)
