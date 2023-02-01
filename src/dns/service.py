from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from pydantic import AnyHttpUrl
from typing import Generator, TypeAlias, Optional

from src.schemas import ProductInfo, Price

from .settings import SELENIUM_TIMEOUT_IN_SECONDS


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
        pass

    def get_product_price(self, url: AnyHttpUrl) -> Price:
        """Extracts product price

        Args:
            url (AnyHttpUrl): product web page url

        Returns:
            Price: product current price
        """
        pass


def get_dns_scraper() -> Generator[DNSWebScraper, None, None]:
    """Generates DNSWebScraper instance. Intended to be used as a dependency."""
    pass
