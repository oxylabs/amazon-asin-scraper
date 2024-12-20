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