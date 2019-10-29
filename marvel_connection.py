import hashlib
import time


def get_md5digest(timestamp, public_key):
    """Return the correct md5 hash to connect to the Marvel Api"""
    private_key = "fe908016704e72656499f3726fd686dbc4c37155"

    hash = hashlib.md5((timestamp+private_key+public_key).encode('utf-8'))
    md5digest = str(hash.hexdigest())
    return md5digest


def get_authentication_url(timestamp, public_key, md5digest):
    auth_url = "?ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest
    return auth_url


def get_connection_url(endpoint, auth_url):
    web_url = "https://gateway.marvel.com:80"
    conn_url = web_url+endpoint+auth_url
    return conn_url


def get_data_url(endpoint, timestamp, public_key):
    md5digest = get_md5digest(timestamp, public_key)
    auth_url = get_authentication_url(timestamp, public_key, md5digest)
    conn_url = get_connection_url(endpoint, auth_url)
    return conn_url


# use:
timestamp = str(time.time())
public_key = "02766f539b25f5e7a7621d2c15e60cfd"
endpoint = "/v1/public/characters"

# output to show it works
# Later this evening or tommorow morning I will add the part that connects to Marvel.
print(get_data_url(endpoint, timestamp, public_key))

