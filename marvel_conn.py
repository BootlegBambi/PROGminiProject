# Import all module needed to run the function below.
import hashlib
import http.client
import json
import time
import urllib
import curio
import curio_http

def get_md5digest(timestamp, public_key):
    """
    :param timestamp: Timestamp of the request
    :param public_key: The public Marvel API key
    :return: Correct md5 hash to connect to the Marvel Api
    NOTE: This function should not be uses as an stand-alone function.
    """
    private_key = "fe908016704e72656499f3726fd686dbc4c37155"

    hash = hashlib.md5((timestamp+private_key+public_key).encode('utf-8'))
    md5digest = str(hash.hexdigest())
    return md5digest


def get_authentication_url(timestamp, public_key, md5digest):
    """
    :param timestamp: Timestamp of the request
    :param public_key: The public Marvel API key
    :param md5digest: The Md5digest - Use get_md5digest() to create
    :return: The authentication part of the API request url.
    NOTE: This function should not be uses as an stand-alone function.
    """
    auth_url = "?ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest
    return auth_url


def get_connection_url(endpoint, auth_url):
    """
    :param endpoint: The request endpoint for the Marvel API.
    :param auth_url: The authentication url - Use get_authentication_url() to create.
    :return: The url(path + auth parameters) that can be used to connect to the Marvel API.
    NOTE: This function should not be uses as an stand-alone function.
    """
    conn_url = endpoint+auth_url
    return conn_url


def get_data_url(endpoint, timestamp, public_key):
    """
    This function calls other functions to create the complete url to make a call to the Marvel API.
    :param endpoint: The request endpoint for the Marvel API.
    :param timestamp: Timestamp of the request
    :param public_key: The public Marvel API key
    :return: The complete url to be used when connection to the Marvel API.
    """
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



