import time
import marvel_conn

import http.client
import json

# use:
timestamp = str(time.time())
public_key = "02766f539b25f5e7a7621d2c15e60cfd"
endpoint = "/v1/public/characters"

#Request headers
req_headers = {}

try:
    conn = http.client.HTTPSConnection("gateway.marvel.com")
    conn.request("GET", marvel_conn.get_data_url(endpoint, timestamp, public_key), headers=req_headers)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)

    print(data)
    conn.close()
except Exception as e:
    print("Fout: {} {}".format(e.errno, e.strerror))
