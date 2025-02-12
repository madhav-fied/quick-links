import os
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from backend.database.init_db import make_db
from backend.api.api_v1 import api_v1_router


@asynccontextmanager
async def ensure_deps(app: FastAPI):
        await make_db()
        yield

app = FastAPI(lifespan=ensure_deps)

app.include_router(api_v1_router)
app.mount("/home", StaticFiles(directory="backend/static/home", html=True))

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["POST", "GET"],
        allow_headers=["*"],
)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
