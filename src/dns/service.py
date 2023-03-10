from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from pydantic import AnyHttpUrl, validate_arguments
from typing import Generator, TypeAlias, Optional, Any
from functools import lru_cache

from src.schemas import ProductInfo, Price

from .exceptions import WebElementWasNotFound, InvalidUrl

from src.dns.settings import (
    SELENIUM_WEBDRIVER,
    SELENIUM_TIMEOUT_IN_SECONDS,
    RATING_SCALE,
    ACTIVE_PRICE_ELEMENT_SELECTOR,
    PRICE_ELEMENT_SELECTOR,
    TITLE_ELEMENT_SELECTOR,
    DESCRIPTION_ELEMENT_SELECTOR,
    RATING_ELEMENT_SELECTOR,
    BUTTON_TO_SHOW_RATING_SELECTOR,
    DNS_HOST,
)


WebElementSelector: TypeAlias = tuple[str, str]


@validate_arguments
def validate_url(url: AnyHttpUrl):
    if url.host != DNS_HOST:
        raise InvalidUrl(status_code=400, detail=f"{url} is not a valid dns-shop URL")


class DNSWebScraper:
    """Extracts information about products from dns-shop"""

    __driver: WebDriver

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def __find_visible_element(
        self, selector: WebElementSelector
    ) -> Optional[WebElement]:
        """Helper function that returns web element when it becomes visible.

        Args:
            selector (WebElementSelector): pair of strategy (By.CLASS_NAME, By.ID, etc.) and web element selector (class name, id, css selector, etc.)

        Returns:
            WebElement: web element
        """
        Wait(self.__driver, SELENIUM_TIMEOUT_IN_SECONDS).until(
            visibility_of_element_located(selector)
        )
        return self.__driver.find_element(*selector)

    def get_product(self, url: AnyHttpUrl) -> ProductInfo:
        """Extracts product full information

        Args:
            url (AnyHttpUrl): product web page url

        Returns:
            ProductInfo
        """
        validate_url(url)
        driver = self.__driver
        driver.get(url)
        driver.fullscreen_window()

        product: dict[str, Any] = {"url": url}

        # Extract title
        try:
            element = self.__find_visible_element(TITLE_ELEMENT_SELECTOR)
        except TimeoutException:
            raise WebElementWasNotFound(url, "title")
        else:
            product["title"] = element.text.strip()

        # Extract description
        try:
            element = self.__find_visible_element(DESCRIPTION_ELEMENT_SELECTOR)
        except TimeoutException:
            product["description"] = None
        else:
            product["description"] = element.text.strip()

        # Extract rating
        try:
            self.__find_visible_element(BUTTON_TO_SHOW_RATING_SELECTOR).click()
            element = self.__find_visible_element(RATING_ELEMENT_SELECTOR)
        except TimeoutException:
            product["rating"] = None
        else:
            product["rating"] = float(element.text.strip()) / RATING_SCALE

        return ProductInfo(**product)

    def get_product_price(self, url: AnyHttpUrl) -> Price:
        """Extracts product price

        Args:
            url (AnyHttpUrl): product web page url

        Returns:
            Price: product current price
        """
        validate_url(url)
        driver = self.__driver
        driver.get(url)
        driver.fullscreen_window()

        try:
            element = self.__find_visible_element(ACTIVE_PRICE_ELEMENT_SELECTOR)
        except TimeoutException:
            try:
                element = self.__find_visible_element(PRICE_ELEMENT_SELECTOR)
            except TimeoutException:
                raise WebElementWasNotFound(url, "price")

        # Dirty walkaround solution :)
        # Just remove anything after '???' (including the old price)
        # Now prices with discount are extracted correctly
        price = int("".join(filter(str.isdigit, element.text.split("???")[0])))
        return price


@lru_cache()
def get_selenium_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1420,1080")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    return SELENIUM_WEBDRIVER(chrome_options=options)


def get_dns_scraper() -> Generator[DNSWebScraper, None, None]:
    """Generates DNSWebScraper instance. Intended to be used as a dependency."""
    yield DNSWebScraper(get_selenium_webdriver())
