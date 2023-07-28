# Amazon ASIN Scraper

[![Amazon_scraper (1)](https://user-images.githubusercontent.com/129506779/249700804-abb11a97-9e0d-4f3c-bf2c-72991e8acd74.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=86) 

Amazon ASIN Scraper is a powerful tool that quickly fetches ASIN numbers
of publicly available Amazon products. This short guide will demonstrate
how to extract ASINs using Oxylabs’ Scraper API.

## How it works

You can retrieve Amazon ASIN numbers by sending a request to our API,
which will return the results in JSON or HTML format.

### **Python code example**

The below code sample shows how you can get parsed Amazon results with
product ASINs in JSON format:

```python
import requests
from pprint import pprint

# Structure payload.
payload = {
   'source': 'amazon_search',
   'query': 'nintendo',
   'user_agent_type': 'desktop',
   'parse': True,
   'domain': 'com',
   'geo_location': '10020',
   'locale': 'en-us',
   'start_page': '1',
   'pages': '1'
}

# Get a response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'), #Your credentials go here
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())

```

Visit our
[<u>documentation</u>](https://docs.oxylabs.io/wmw8gbrbnajdf87/scraper-apis/e-commerce-scraper-api/amazon)
for more details and code examples on using Oxylabs’ Amazon Scraper API.

### Output Example

Here's a partial output sample that includes paid and organic Amazon search results:

```json
{
  "results": [
    {
      "content": {
        "url": "https://www.amazon.com/s?k=nintendo&page=1",
        "page": 1,
        "pages": 1,
        "query": "nintendo",
        "results": {
          "paid": [
            {
              "pos": 1,
              "url": "/sspa/click?ie=UTF8&spc=MTo0OTQyODU2MjAxNjE4NzQwOjE2OTA1MzMwNDM6c3BfYXRmOjIwMDE0MzU3MzAzMTQ5ODo6MDo6&url=/Sonic-Origins-Plus-Nintendo-Switch/dp/B0BZFGSY5W/ref=sr_1_1_sspa?keywords=nintendo&qid=1690533043&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
              "asin": "B0BZFGSY5W",
              "price": 29.99,
              "title": "Sonic Origins Plus - Nintendo Switch",
              "rating": 4,
              "currency": "USD",
              "is_prime": false,
              "url_image": "https://m.media-amazon.com/images/I/81NUog-gECL._AC_UY218_.jpg",
              "variations": [
                {
                  "price": 29.99,
                  "title": "Nintendo Switch",
                  "not_available": false,
                  "price_strikethrough": 39.99
                }
              ],
              "best_seller": false,
              "price_upper": 29.99,
              "is_sponsored": true,
              "manufacturer": "SEGA",
              "sales_volume": "2K+ bought in past month",
              "pricing_count": 1,
              "reviews_count": 0,
              "is_amazons_choice": false,
              "price_strikethrough": 39.99,
              "shipping_information": "FREE delivery Wed, Aug 2 Or fastest delivery Mon, Jul 31"
            }
          ],
          "organic": [
            {
              "pos": 4,
              "url": "/Nintendo-eShop-Gift-Card-Digital/dp/B01LYOCVZF/ref=sr_1_4?keywords=nintendo&qid=1690533043&sr=8-4",
              "asin": "B01LYOCVZF",
              "price": 20,
              "title": "$20 Nintendo eShop Gift Card [Digital Code]",
              "rating": 4.7,
              "currency": "USD",
              "is_prime": false,
              "url_image": "https://m.media-amazon.com/images/I/71cj5cNm7ZL._AC_UY218_.jpg",
              "variations": [
                {
                  "asin": "B01LYOCVZF",
                  "price": 20,
                  "title": "Nintendo Switch",
                  "not_available": false
                }
              ],
              "best_seller": false,
              "price_upper": 20,
              "is_sponsored": false,
              "manufacturer": "Nintendo",
              "pricing_count": 1,
              "reviews_count": 0,
              "is_amazons_choice": false
            }
          ],
          "suggested": [],
          "amazons_choices": [...],
          "instant_recommendations": []
        },
        "parse_status_code": 12000,
        "total_results_count": 60000
      },
      "created_at": "2023-07-28 08:30:35",
      "updated_at": "2023-07-28 08:30:44",
      "page": 1,
      "url": "https://www.amazon.com/s?k=nintendo&page=1",
      "job_id": "7090609474792097793",
      "status_code": 200,
      "parser_type": ""
    }
  ]
}

```

Amazon ASIN Scraper makes it easy to gather product ASIN numbers,
empowering your web scraping pipeline with lighting-fast access to
essential Amazon data.

If you have any questions, feel free to contact our 24/7 support team
via live chat or [<u>email</u>](mailto:support@oxylabs.io).
