from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from src.core import Database, create_db_and_tables, get_session
from src.api import router as api_router

database = Database()


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1", dependencies=[Depends(get_session)])
