from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Chrome, Firefox, Safari, Ie
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from typing import Type

from src.settings import env

SELENIUM_TIMEOUT_IN_SECONDS: int = env("SELENIUM_TIMEOUT_IN_SECONDS", cast=int)

RATING_SCALE: int = 5

PRICE_ELEMENT_SELECTOR: tuple[str, str] = (
    By.CLASS_NAME,
    "product-buy__price",
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

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--log-level=1")
options.add_argument("--start-maximized")
SELENIUM_WEBDRIVER: WebDriver = Chrome(chrome_options=options)
