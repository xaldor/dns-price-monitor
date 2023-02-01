from fastapi import FastAPI
from src.settings import APP_TITLE


app = FastAPI(title=APP_TITLE)
