#!/usr/bin/python3
""" Sends a POST request to Github API """
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = argv[1]
    passw = argv[2]
    req = requests.get(url, auth=(user, passw))
    if (req.status_code == 200):
        user_json = req.json()
        print(user_json['id'])
    else:
        print("None")
