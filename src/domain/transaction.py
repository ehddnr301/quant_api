from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field

from .utils import kst_now


class Transaction(SQLModel, table=True):
    transaction_id: Optional[int] = Field(primary_key=True, default=None)
    user_id: int = Field(index=True)
    coin_type: str = Field()
    amount: float = Field()
    price: float = Field()
    transaction_type: str = Field()
    transaction_time: datetime = Field(default_factory=kst_now)
