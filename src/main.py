from fastapi import FastAPI
from src.settings import APP_TITLE, PRICE_UPDATE_INTERVAL_IN_MINUTES

from src.utils import repeat_every
from src.api.router import router
from src.update_price import update_price

app = FastAPI(title=APP_TITLE)

app.include_router(router)


@app.on_event("startup")
@repeat_every(seconds=PRICE_UPDATE_INTERVAL_IN_MINUTES * 60)
async def update_price_loop():
    await update_price()
