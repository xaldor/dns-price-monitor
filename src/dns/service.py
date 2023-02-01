from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from pydantic import AnyHttpUrl
from typing import Generator, TypeAlias, Optional, Any

from src.schemas import ProductInfo, Price

from src.dns.settings import (
    SELENIUM_WEBDRIVER,
    SELENIUM_TIMEOUT_IN_SECONDS,
    RATING_SCALE,
    PRICE_ELEMENT_SELECTOR,
    TITLE_ELEMENT_SELECTOR,
    DESCRIPTION_ELEMENT_SELECTOR,
    RATING_ELEMENT_SELECTOR,
    BUTTON_TO_SHOW_RATING_SELECTOR,
)


WebElementSelector: TypeAlias = tuple[str, str]


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
            WebElement: web element, or None, if it was not found
        """
        try:
            Wait(self.__driver, SELENIUM_TIMEOUT_IN_SECONDS).until(
                visibility_of_element_located(selector)
            )
        except TimeoutException:
            return None
        else:
            return self.__driver.find_element(*selector)

    def get_product(self, url: AnyHttpUrl) -> ProductInfo:
        """Extracts product full information

        Args:
            url (AnyHttpUrl): product web page url

        Returns:
            ProductInfo
        """
        driver = self.__driver
        driver.get(url)
        driver.fullscreen_window()

        product: dict[str, Any] = {"url": url}

        # Extract title
        element = self.__find_visible_element(TITLE_ELEMENT_SELECTOR)
        product["title"] = element.text.strip()

        # Extract description
        try:
            element = self.__find_visible_element(DESCRIPTION_ELEMENT_SELECTOR)
            product["description"] = element.text.strip()
        except TimeoutException:
            product["description"] = None

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
        driver = self.__driver
        driver.get(url)
        driver.fullscreen_window()

        element = self.__find_visible_element(PRICE_ELEMENT_SELECTOR)
        price = int("".join(filter(str.isdigit, element.text)))
        return price


def get_dns_scraper() -> Generator[DNSWebScraper, None, None]:
    """Generates DNSWebScraper instance. Intended to be used as a dependency."""
    with SELENIUM_WEBDRIVER() as driver:
        yield DNSWebScraper(driver)
