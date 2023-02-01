from selenium.webdriver.common.by import By

from src.settings import env

from .service import WebElementSelector

SELENIUM_TIMEOUT_IN_SECONDS: int = env("SELENIUM_TIMEOUT_IN_SECONDS", cast=int)

PRICE_ELEMENT_SELECTOR: WebElementSelector = (
    By.CLASS_NAME,
    "product-buy__price",
)

TITLE_ELEMENT_SELECTOR: WebElementSelector = (
    By.CLASS_NAME,
    "product-card-top__title",
)

DESCRIPTION_ELEMENT_SELECTOR: WebElementSelector = (
    By.CLASS_NAME,
    "product-card-description-text",
)

BUTTON_TO_SHOW_RATING_SELECTOR: WebElementSelector = (
    By.CLASS_NAME,
    "product-card-top__rating",
)

RATING_ELEMENT_SELECTOR: WebElementSelector = (
    By.CLASS_NAME,
    "circle-rating__number",
)
