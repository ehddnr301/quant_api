from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field
from decimal import Decimal

from .utils import kst_now


class Asset(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    currency: str = Field()
    balance: Decimal = Field()
    updated_at: datetime = Field(default_factory=kst_now)
