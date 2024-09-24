from fastapi import FastAPI

from api.v0.router import router as api_v0_router
from api.v1.router import router as api_v1_router

app = FastAPI()

app.include_router(api_v0_router, prefix="/api/v0", tags=["v0"])
app.include_router(api_v1_router, prefix="/api/v1", tags=["v1"])
