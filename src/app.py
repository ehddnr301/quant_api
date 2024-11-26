from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core import Database
from src.api import router as api_router
from src.containers import Container


@asynccontextmanager
async def lifespan(app: FastAPI):
    database = Database()
    database.create_database()

    container = Container()
    app.container = container
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")
