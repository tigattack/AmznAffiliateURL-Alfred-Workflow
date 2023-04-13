#!/usr/bin/env python3

import sys
import http.client
import json

# Set vars.
amzn_domain = sys.argv[1]
associate_id = sys.argv[2]
bitly_token = sys.argv[3]
asin = sys.argv[4]
url = f"https://www.{amzn_domain}/dp/{asin}/?tag={associate_id}"

# Define and make the request to the bit.ly API to generate a short URL.
conn = http.client.HTTPSConnection(
									"api-ssl.bitly.com",
									443
)
headers = {
			"Content-Type": "application/json",
			"Authorization": f"Bearer {bitly_token}"
}
params = {
			'long_url': f"{url}",
			'domain': 'bit.ly',
			'group_guid': 'Bkafe1wZ55e'
}
conn.request(
				"POST", "/v4/shorten",
				json.dumps(params),
				headers
)
response = conn.getresponse()
data = response.read()

# Parse JSON and set var
jsonData = json.loads(data)
shortUrl = jsonData["link"]

# Output to STDOUT
sys.stdout.write(shortUrl)
