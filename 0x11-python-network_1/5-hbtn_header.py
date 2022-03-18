#!/usr/bin/python3
""" Displays the value of the variable X-Request-Id in header """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
