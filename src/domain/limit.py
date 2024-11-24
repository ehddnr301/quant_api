from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field

from .utils import kst_now


class Limit(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    remaining_trades: int = Field(default=3)
    updated_at: datetime = Field(default_factory=kst_now)  # 타입 명시
