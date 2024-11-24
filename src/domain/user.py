from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field

from .utils import kst_now


class User(SQLModel, table=True):  # table=True로 데이터베이스 테이블 생성
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    is_active: bool = Field(default=False)
    created_at: datetime = Field(default_factory=kst_now)  # 타입 명시
