#!/usr/bin/python3
""" POST and Search API """
import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if (len(argv) > 1):
        letter = argv[1]
    else:
        letter = ""
    payload = {'q': letter}
    req = requests.post(url, data=payload)
    try:
        json_body = req.json()
        if (len(json_body) != 0):
            print("[{}] {}".format(json_body['id'], json_body['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
