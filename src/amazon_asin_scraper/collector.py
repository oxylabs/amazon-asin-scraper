"""
    Main module for collecting Amazon ASIN code data.
"""

import logging

from typing import List

import pandas as pd

from amazon_asin_scraper.models import Product
from amazon_asin_scraper.scraper import AmazonASINScraper


DEFAULT_OUTPUT_FILE = "amazon_asin_data.csv"


class AmazonDataCollector:
    """Data collector class for Amazon pages"""

    def __init__(
        self,
        output_file: str | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self._scraper = AmazonASINScraper()
        self._output_file = output_file if output_file else DEFAULT_OUTPUT_FILE
        self._logger = logger if logger else logging.getLogger(__name__)

    def _save_to_csv(self, products: List[Product]) -> None:
        """Saves given list of products with ASIN codes to a CSV file."""
        self._logger.info(f"Writing {len(products)} products to {self._output_file}..")
        product_objects = [product.model_dump() for product in products]
        df = pd.DataFrame(product_objects)
        df.to_csv(self._output_file)

    def collect_amazon_asin_data(self, url: str) -> None:
        """
        Scrapes products with ASIN codes from a given Amazon page and stores it into a CSV file.

        Args:
            url (str): The URL of the Amazon page for which to scrape products with ASIN codes.
        """
        self._logger.info(f"Getting Amazon ASIN code data for url {url}..")
        try:
            products = self._scraper.scrape_amazon_products(url)
        except Exception:
            self._logger.exception(
                f"Error when scraping Amazon ASIN code data for url {url}."
            )
            return

        if not products:
            self._logger.info("No product data found for given Amazon page.")
            return

        self._save_to_csv(products)
