from fastapi import FastAPI
from core.logger import setup_logging
from api.api import router
setup_logging()
app=FastAPI()
app.include_router(router=router)