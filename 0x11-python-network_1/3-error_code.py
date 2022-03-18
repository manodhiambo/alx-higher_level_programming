#!/usr/bin/python3
""" Managing Error exceptions """
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            body_page = response.read()
            print(body_page.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
