from contextlib import asynccontextmanager
from fastapi import FastAPI

from app import routers
from app.core.model_registry import model_registry
from app.utils import load_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    model_registry.register_model("iris_model", load_model())

    yield

    model_registry.clear()


app = FastAPI(lifespan=lifespan)

app.include_router(routers.router)


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}
