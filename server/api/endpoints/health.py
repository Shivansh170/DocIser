import logging

from fastapi import APIRouter

router=APIRouter()
logger=logging.getLogger(__name__)
@router.get("/")

def get_health_status():
    logger.info("Health check requested")
    logger.info("Fetching health status...")
    return {
        "success":True,
        "message":"Server running properly"
    }