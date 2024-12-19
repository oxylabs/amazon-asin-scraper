"""
    Pydantic models for Amazon ASIN scraper.
"""

from pydantic import BaseModel


class Product(BaseModel):
    title: str
    url: str
    asin_code: str
