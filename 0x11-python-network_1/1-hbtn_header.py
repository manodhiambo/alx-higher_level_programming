#!/usr/bin/python3
""" Program that fetches an URL with a header value"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        info_page = response.info()
        print(info_page.get('X-Request-Id'))
