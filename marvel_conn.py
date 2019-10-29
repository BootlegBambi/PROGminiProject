import hashlib
import http.client
import json
import time
import urllib

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
    conn_url = endpoint+auth_url
    return conn_url


def get_data_url(endpoint, timestamp, public_key):
    md5digest = get_md5digest(timestamp, public_key)
    auth_url = get_authentication_url(timestamp, public_key, md5digest)
    conn_url = get_connection_url(endpoint, auth_url)
    return conn_url


def get_data(endpoint, params={}):
    """
    Get data from the Marvel API.
    :param endpoint: Endpoint path for the marvel API. See: https://developer.marvel.com/docs
    :param params: Dictionary of optional parameters, See: https://developer.marvel.com/docs
    :return: If succesfull the data in JSON format else False.
    Note: You need a legit private and public key and the correct timestamp.
    """
    timestamp = str(time.time())
    public_key = "02766f539b25f5e7a7621d2c15e60cfd"

    # Request headers
    req_headers = {}
    # Parameters
    params = urllib.parse.urlencode(params)

    data_url = get_data_url(endpoint, timestamp, public_key)
    try:
        conn = http.client.HTTPSConnection("gateway.marvel.com")
        conn.request("GET", data_url+"&"+params, headers=req_headers)

        response = conn.getresponse()
        responsetext = response.read()
        data = json.loads(responsetext)

        conn.close()
        return data
    except Exception as e:
        print("Fout: {} {}".format(e.errno, e.strerror))
        return False



