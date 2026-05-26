from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from core.database import Base, engine
import orm.models  # noqa: F401 — registers ORM models on Base.metadata
from routers import blueprints, emotion


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create all tables on startup (dev convenience; use Alembic for production)
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Evercrafted API", version="1.0.0", lifespan=lifespan)

# CORS — allow the Next.js frontend in development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blueprints.router, prefix="/api/v1")
app.include_router(emotion.router, prefix="/api/v1")


@app.get("/api/v1/health")
def health():
    return JSONResponse(
        content={
            "status": "healthy",
            "service": "evercrafted-api",
            "version": "v1",
        }
    )
