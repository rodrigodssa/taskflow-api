
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers import tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="TaskFlow API",
    description="API REST para gerenciamento de tarefas.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(tasks.router)


@app.get("/")
def home():
    return {"message": "TaskFlow API funcionando!"}
