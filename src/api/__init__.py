from fastapi import APIRouter

from .user.user_api import router as user_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])

__all__ = ["router"]
