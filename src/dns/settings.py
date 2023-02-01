from selenium.webdriver.common.by import By

from src.settings import env

from .service import WebElementSelector

SELENIUM_TIMEOUT_IN_SECONDS: int = env("SELENIUM_TIMEOUT_IN_SECONDS", cast=int)

PRICE_ELEMENT_SELECTOR: WebElementSelector = (
    By.CLASS_NAME,
    "product-buy__price",
)
