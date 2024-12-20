"""
    Module for scraping Amazon ASIN data.
"""

import logging
import time

from enum import Enum
from typing import List

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

from seleniumwire import webdriver
from seleniumwire.request import Request

from amazon_asin_scraper.models import Product


logging.getLogger("WDM").setLevel(logging.ERROR)
logging.getLogger("seleniumwire").setLevel(logging.ERROR)


class DriverInitializationError(BaseException):
    message = "Unable to initialize Chrome webdriver for scraping."


class DriverGetProductsError(BaseException):
    message = "Unable to get Amazon product ASIN data with Chrome webdriver."


class ProductXPath(str, Enum):
    PRODUCTS = "//div[@data-component-type='s-search-result']"
    TITLE = ".//h2[@class='a-size-base-plus a-spacing-none a-color-base a-text-normal']/span"
    URL = ".//a[@class='a-link-normal s-no-outline']"


class AmazonASINScraper:
    """Class for scraping Amazon products with ASIN codes"""

    def __init__(self, logger: logging.Logger | None = None) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "keep-alive",
            "Referer": "https://www.amazon.com/",
            "Host": "www.amazon.com",
            "TE": "Trailers",
        }

    def _add_headers_to_request(self, request: Request) -> None:
        """Intercepts selenium requests to add headers"""
        for key, value in self._headers.items():
            request.headers[key] = value

    def _init_chrome_driver(self) -> webdriver.Chrome:
        """Initializes Chrome webdriver"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.request_interceptor = self._add_headers_to_request
        return driver

    def _parse_product_data(self, product: WebElement) -> Product | None:
        """Parses product ASIN code data from the given product element"""
        title_element = product.find_element(By.XPATH, ProductXPath.TITLE)
        title = title_element.text if title_element else None

        url_element = product.find_element(By.XPATH, ProductXPath.URL)
        url = url_element.get_attribute("href") if url_element else None

        asin_code = product.get_attribute("data-asin")

        return Product(title=title, url=url, asin_code=asin_code)

    def _get_product_data_from_page(
        self, url: str, driver: webdriver.Chrome
    ) -> List[Product]:
        """Scrapes the Amazon page for product data"""
        driver.get(url)
        time.sleep(3)
        product_elements = driver.find_elements(By.XPATH, ProductXPath.PRODUCTS)
        parsed_products = []
        for product in product_elements:
            try:
                parsed_product = self._parse_product_data(product)
            except Exception:
                self._logger.exception(
                    "Uexpected error when parsing ASIN code data for product. Skipping.."
                )
                continue
            else:
                parsed_products.append(parsed_product)

        return parsed_products

    def scrape_amazon_products(self, url: str) -> List[Product]:
        """
        Retrieves a list of products with ASIN codes from Amazon for a given Amazon page URL.

        Returns:
            List[Product]: A list of Product objects with ASIN codes.
        Raises:
            DriverInitializationError: If the Chrome webdriver cannot be initialized.
            DriverGetProductsError: If the Amazon ASIN code data cannot be scraped from the Amazon site.
        """
        self._logger.info("Scraping Amazon product data..")

        try:
            driver = self._init_chrome_driver()
        except Exception as e:
            raise DriverInitializationError from e

        try:
            return self._get_product_data_from_page(url, driver)
        except Exception as e:
            raise DriverGetProductsError from e
        finally:
            driver.close()
