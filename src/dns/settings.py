from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from typing import Type

from src.settings import env

DNS_HOST: str = "www.dns-shop.ru"

SELENIUM_TIMEOUT_IN_SECONDS: int = env("SELENIUM_TIMEOUT_IN_SECONDS", cast=int)

RATING_SCALE: int = 5

PRICE_ELEMENT_SELECTOR: tuple[str, str] = (
    By.CLASS_NAME,
    "product-buy__price",
)

ACTIVE_PRICE_ELEMENT_SELECTOR: tuple[str, str] = (
    By.CLASS_NAME,
    "product-buy__price_active",
)

TITLE_ELEMENT_SELECTOR: tuple[str, str] = (
    By.CLASS_NAME,
    "product-card-top__title",
)

DESCRIPTION_ELEMENT_SELECTOR: tuple[str, str] = (
    By.CLASS_NAME,
    "product-card-description-text",
)

BUTTON_TO_SHOW_RATING_SELECTOR: tuple[str, str] = (
    By.CLASS_NAME,
    "product-card-top__rating",
)

RATING_ELEMENT_SELECTOR: tuple[str, str] = (
    By.CLASS_NAME,
    "circle-rating__number",
)

SELENIUM_WEBDRIVER: Type[WebDriver] = Chrome
