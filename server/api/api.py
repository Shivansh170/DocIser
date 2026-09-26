from fastapi import APIRouter
from .endpoints.health import router as HealthRouter
router=APIRouter()
router.include_router(HealthRouter,tags=["health"])