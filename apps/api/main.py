import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from routers import blueprints

load_dotenv()

app = FastAPI(title="Evercrafted API", version="1.0.0")

app.include_router(blueprints.router, prefix="/api/v1")


@app.get("/api/v1/health")
def health():
    return JSONResponse(
        content={
            "status": "healthy",
            "service": "evercrafted-api",
            "version": "v1",
        }
    )
