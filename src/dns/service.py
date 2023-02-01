from selenium.webdriver.remote.webdriver import WebDriver
from pydantic import AnyHttpUrl
from typing import Generator

from src.schemas import ProductInfo, Price


class DNSWebScraper:
    """Extracts information about products from dns-shop"""

    __driver: WebDriver

    def __init__(self, driver: WebDriver):
        pass

    def get_product(url: AnyHttpUrl) -> ProductInfo:
        """Extracts product full information

        Args:
            url (AnyHttpUrl): product web page url

        Returns:
            ProductInfo
        """
        pass

    def get_product_price(url: AnyHttpUrl) -> Price:
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
