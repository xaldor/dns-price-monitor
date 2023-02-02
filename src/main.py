from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.settings import APP_TITLE, PRICE_UPDATE_INTERVAL_IN_MINUTES

from src.utils import repeat_every
from src.api.router import router
from src.update_price import update_price

from src.views import views

app = FastAPI(title=APP_TITLE)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(router)
app.include_router(views)


@app.on_event("startup")
@repeat_every(seconds=PRICE_UPDATE_INTERVAL_IN_MINUTES * 60)
async def update_price_loop():
    await update_price()
