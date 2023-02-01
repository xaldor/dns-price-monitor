from fastapi import FastAPI
from src.settings import APP_TITLE

from src.api.router import router

app = FastAPI(title=APP_TITLE)

app.include_router(router)
