#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    payload = {'email': email}
    req = requests.post(url, data=payload)
    print(req.text)
