#!/usr/bin/python3
""" Posting an email """
import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    value = {'email': email}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body_page = response.read()
        print(body_page.decode('utf-8'))
