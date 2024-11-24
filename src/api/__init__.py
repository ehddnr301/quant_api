from fastapi import APIRouter

from .user_api import router as user_router
from .limit_api import router as limit_router
from .transaction_api import router as transaction_router
from .asset_api import router as asset_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(limit_router, prefix="/limits", tags=["limits"])
router.include_router(transaction_router, prefix="/transactions", tags=["transactions"])
router.include_router(asset_router, prefix="/assets", tags=["assets"])

__all__ = ["router"]
