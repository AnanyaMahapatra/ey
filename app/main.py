from fastapi import FastAPI
from app.views.endpoints import router

app = FastAPI()

app.include_router(router)
