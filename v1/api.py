from fastapi import APIRouter

from v1.endpoints import jobs, index

api_router = APIRouter()
api_router.include_router(index.router, tags=["index"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
